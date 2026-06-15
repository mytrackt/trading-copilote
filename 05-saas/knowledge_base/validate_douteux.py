#!/usr/bin/env python3
"""
validate_douteux.py — Pipeline de validation des règles KB Belkhayate
Version : 1.0 | Session S12 | 15/06/2026

STRATÉGIE :
  Au lieu de 1 265 appels Claude (un par règle),
  on fait MAX 108 appels — un par vidéo, avec toutes ses règles en une fois.
  → 10x moins cher, 10x plus rapide.

ARCHITECTURE 3 PASSES :
  PASSE 1 : Vérification groupée par transcript (max 108 appels Claude)
            Chaque appel vérifie toutes les règles d'une vidéo contre son transcript.
  PASSE 2 : Règles "orphelines" (dans aggregated_rules mais pas dans videos[])
            Recherche cross-corpus avec keyword matching préalable.
  PASSE 3 : Génération des 3 rapports de sortie.

SÉCURITÉS :
  - Resumable : checkpoint JSON après chaque vidéo traitée
  - Rate-limited : 1.5s entre appels Claude (RÈGLE 5 du projet)
  - Anti-hallucination : parse_claude_json() + vérification verbatim
  - Atomic writes : tempfile + os.replace pour tous les JSON
  - Dry-run : mode simulation sans appels API

USAGE :
  python validate_douteux.py --dry-run        # Tester sans dépenser
  python validate_douteux.py                   # Production
  python validate_douteux.py --reset           # Repartir de zéro
  python validate_douteux.py --passe 3         # Rapports seulement

SORTIES (dans 04-cerveau-trading/validation/) :
  checkpoint.json         — Point de reprise (auto)
  RAPPORT_VALIDATION.json — Résultats complets + stats
  KB_VALIDEE.json         — KB reconstruite avec statuts VALIDE/INVALIDE/AMBIGU
  A_VERIFIER_HUMAIN.md    — Cas ambigus avec lien YouTube pour revue rapide
  validate_douteux.log    — Log complet de l'exécution
"""

import os
import re
import sys
import json
import time
import logging
import argparse
import tempfile
from datetime import datetime
from typing import Optional

# =============================================================================
# CHEMINS ABSOLUS (RÈGLE 1 du projet — jamais de chemins relatifs)
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

KB_PATH         = os.path.join(ROOT_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
TRANSCRIPTS_DIR = os.path.join(ROOT_DIR, "03-transcriptions", "nouvelles-sources",
                                "belkhayate-youtube", "transcripts")
OUTPUT_DIR      = os.path.join(ROOT_DIR, "04-cerveau-trading", "validation")

CHECKPOINT_PATH = os.path.join(OUTPUT_DIR, "checkpoint.json")
RAPPORT_PATH    = os.path.join(OUTPUT_DIR, "RAPPORT_VALIDATION.json")
KB_VALIDEE_PATH = os.path.join(OUTPUT_DIR, "KB_VALIDEE.json")
HUMAIN_PATH     = os.path.join(OUTPUT_DIR, "A_VERIFIER_HUMAIN.md")
LOG_PATH        = os.path.join(OUTPUT_DIR, "validate_douteux.log")

# =============================================================================
# PARAMÈTRES
# =============================================================================

RATE_LIMIT_SEC       = 1.5    # Délai entre appels Claude (RÈGLE 5)
MAX_TRANSCRIPT_CHARS = 14000  # Tronque les transcripts trop longs (~3 500 tokens)
MAX_RULES_PER_CALL   = 25     # Limite de règles par appel (éviter timeout)

# Haiku : moins cher pour tâche de classification/recherche
# Sonnet si les résultats sont de mauvaise qualité
CLAUDE_MODEL = "claude-haiku-4-5-20251001"

VERDICTS_VALIDES = {"VALIDE", "INVALIDE", "AMBIGU"}

# =============================================================================
# LOGGING — fichier + console simultanément
# =============================================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


# =============================================================================
# UTILITAIRES
# =============================================================================

def atomic_write(path: str, data: dict) -> None:
    """Écriture JSON atomique (tempfile + os.replace). Jamais de corruption."""
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", dir=dir_path, suffix=".tmp",
        delete=False, encoding="utf-8"
    ) as tmp:
        json.dump(data, tmp, ensure_ascii=False, indent=2)
        tmp_path = tmp.name
    os.replace(tmp_path, path)


def parse_claude_json(text: str) -> Optional[dict]:
    """
    Extrait le JSON de la réponse Claude. Jamais json.loads() direct (RÈGLE 5).
    Tente plusieurs patterns dans l'ordre de fiabilité.
    """
    patterns = [
        r"```json\s*(.*?)\s*```",   # bloc markdown ```json
        r"```\s*(.*?)\s*```",        # bloc markdown générique
        r"(\{.*\})",                  # objet JSON inline
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    # Dernier recours : texte entier
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        return None


def load_kb() -> dict:
    """
    Charge la KB en supprimant les null bytes (bug connu : fichier paddé à taille fixe).
    """
    with open(KB_PATH, "rb") as f:
        raw = f.read()
    clean = raw.replace(b"\x00", b"").decode("utf-8")
    return json.loads(clean)


def load_transcript(transcript_file: str) -> str:
    """
    Charge un transcript. Tronque si > MAX_TRANSCRIPT_CHARS.
    Retourne "" si le fichier est introuvable.
    """
    path = os.path.join(TRANSCRIPTS_DIR, transcript_file)
    if not os.path.exists(path):
        log.warning(f"  ⚠ Transcript introuvable : {transcript_file}")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if len(content) > MAX_TRANSCRIPT_CHARS:
        log.warning(
            f"  ⚠ Transcript tronqué ({len(content)} → {MAX_TRANSCRIPT_CHARS} chars) : {transcript_file}"
        )
        content = content[:MAX_TRANSCRIPT_CHARS] + "\n[...TRANSCRIPT TRONQUÉ...]"
    return content


def build_rule_index(kb: dict) -> dict:
    """
    Construit un index inversé : texte_règle → liste de sources.
    Permet de retrouver rapidement la vidéo d'origine d'une règle.

    Retourne :
    {
      "texte de la règle": [
        {"video_id": "...", "transcript_file": "...", "categorie": "..."},
        ...  (une règle peut apparaître dans plusieurs vidéos)
      ]
    }
    """
    index = {}
    for vid_id, vid_data in kb.get("videos", {}).items():
        tf = vid_data.get("transcript_file", "")
        for cat, rules_list in vid_data.get("rules", {}).items():
            if not isinstance(rules_list, list):
                continue
            for rule_text in rules_list:
                if not isinstance(rule_text, str) or not rule_text.strip():
                    continue
                if rule_text not in index:
                    index[rule_text] = []
                index[rule_text].append({
                    "video_id": vid_id,
                    "transcript_file": tf,
                    "categorie": cat,
                })
    return index


# =============================================================================
# CHECKPOINT — RÉSUMABILITÉ
# =============================================================================

def load_checkpoint() -> dict:
    """Charge le checkpoint existant ou retourne un état vide."""
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"processed_video_ids": [], "results": {}, "started_at": datetime.now().isoformat()}


def save_checkpoint(checkpoint: dict) -> None:
    """Sauvegarde atomique du checkpoint."""
    checkpoint["last_saved"] = datetime.now().isoformat()
    atomic_write(CHECKPOINT_PATH, checkpoint)


# =============================================================================
# APPEL CLAUDE — CŒUR DU SYSTÈME
# =============================================================================

def _build_verification_prompt(transcript_text: str, rules: list, video_title: str) -> str:
    """Construit le prompt de vérification. Séparé pour faciliter les tests."""
    rules_block = "\n".join(
        f'{r["index"]}. [{r["categorie"].upper()}] {r["regle"]}'
        for r in rules
    )
    return f"""Tu es un auditeur rigoureux de règles de trading extraites de vidéos de Mustapha Belkhayate.

MISSION : Vérifier si chaque règle listée est réellement présente dans ce transcript de vidéo.

TRANSCRIPT (vidéo : "{video_title}") :
---
{transcript_text}
---

RÈGLES À VÉRIFIER ({len(rules)} règles) :
{rules_block}

INSTRUCTIONS OBLIGATOIRES :
1. Lis le transcript EN ENTIER avant de répondre.
2. Pour chaque règle, cherche un passage qui la confirme EXPLICITEMENT.
3. "passage" = citation EXACTE, mot pour mot, du transcript. JAMAIS de paraphrase.
4. Si tu ne trouves pas de passage exact, mets null — ne jamais inventer.
5. VALIDE  = un passage du transcript confirme clairement et explicitement la règle.
6. INVALIDE = la règle est absente du transcript ou contredite par lui.
7. AMBIGU  = le transcript aborde le sujet mais pas assez précisément pour confirmer.

Réponds UNIQUEMENT avec ce JSON (aucun texte avant ou après) :
{{
  "resultats": [
    {{
      "index": <numéro entier>,
      "verdict": "VALIDE" | "INVALIDE" | "AMBIGU",
      "passage": "<citation exacte du transcript>" | null,
      "confiance": <nombre entre 0.0 et 1.0>,
      "note": "<explication courte en français, max 100 chars>"
    }}
  ]
}}"""


def verify_rules_against_transcript(
    client,
    transcript_text: str,
    rules: list,
    video_title: str,
) -> list:
    """
    Appel Claude unique pour vérifier N règles contre 1 transcript.

    SÉCURITÉ ANTI-HALLUCINATION :
    Après la réponse Claude, on vérifie que chaque citation existe
    VERBATIM dans le transcript. Si non → downgrade automatique en AMBIGU.

    Args:
        client       : client anthropic initialisé
        transcript_text : contenu du transcript
        rules        : [{"index": int, "regle": str, "categorie": str}]
        video_title  : pour le prompt (lisibilité)

    Returns:
        liste de dict {"index", "verdict", "passage", "confiance", "note"}
    """
    prompt = _build_verification_prompt(transcript_text, rules, video_title)

    try:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = response.content[0].text.strip()
        parsed = parse_claude_json(raw_text)

        if not parsed or "resultats" not in parsed:
            log.error(f"  ✗ JSON invalide de Claude : {raw_text[:200]}")
            return []

        resultats = parsed["resultats"]

        # ── Validation anti-hallucination ──────────────────────────────────
        validated = []
        for res in resultats:
            # Vérifier que le verdict est dans les valeurs attendues
            if res.get("verdict") not in VERDICTS_VALIDES:
                res["verdict"] = "AMBIGU"
                res["note"] = f"[VERDICT INVALIDE CORRIGÉ] {res.get('note', '')}"

            # Vérifier que la citation existe verbatim dans le transcript
            passage = res.get("passage")
            if passage and isinstance(passage, str):
                # Normaliser espaces pour la comparaison
                passage_norm = " ".join(passage.split())
                transcript_norm = " ".join(transcript_text.split())
                if passage_norm not in transcript_norm:
                    log.warning(
                        f"  ⚠ Citation non verbatim → AMBIGU : {passage[:60]}..."
                    )
                    res["verdict"] = "AMBIGU"
                    res["passage"] = None
                    res["note"] = f"[CITATION NON VERBATIM AUTO-CORRIGÉE] {res.get('note', '')}"

            # Clamp confiance entre 0 et 1
            res["confiance"] = max(0.0, min(1.0, float(res.get("confiance", 0.5))))

            validated.append(res)

        return validated

    except Exception as e:
        log.error(f"  ✗ Erreur API Claude : {type(e).__name__}: {e}")
        return []


# =============================================================================
# PASSE 1 — VÉRIFICATION GROUPÉE PAR TRANSCRIPT
# =============================================================================

def passe1_verify_by_transcript(
    kb: dict,
    rule_index: dict,
    dry_run: bool,
    client,
) -> dict:
    """
    Pour chaque vidéo (108 max) :
      1. Collecte toutes ses règles brutes
      2. Charge son transcript
      3. Un seul appel Claude pour vérifier toutes les règles
      4. Sauvegarde checkpoint

    Résumable : les vidéos déjà traitées sont skippées.

    Retourne :
    {
      "texte_règle": {
        "video_id": str,
        "transcript_file": str,
        "categorie": str,
        "verdict": "VALIDE"|"INVALIDE"|"AMBIGU",
        "passage": str|None,
        "confiance": float,
        "note": str,
      }
    }
    """
    checkpoint = load_checkpoint()
    processed  = set(checkpoint.get("processed_video_ids", []))
    results    = checkpoint.get("results", {})

    videos     = kb.get("videos", {})
    video_list = list(videos.items())
    total      = len(video_list)
    nb_skip    = len(processed)

    log.info(f"PASSE 1 — {total} vidéos ({nb_skip} déjà traitées, {total - nb_skip} restantes)")

    for i, (vid_id, vid_data) in enumerate(video_list, 1):
        if vid_id in processed:
            continue

        transcript_file = vid_data.get("transcript_file", "")
        video_title     = transcript_file.replace(".txt", "")[:70]
        prefix          = f"[{i:03d}/{total}] {vid_id}"

        # ── Collecter les règles brutes de cette vidéo ──────────────────
        rules_to_check = []
        for cat, rules_list in vid_data.get("rules", {}).items():
            if not isinstance(rules_list, list):
                continue
            for rule_text in rules_list:
                if isinstance(rule_text, str) and rule_text.strip():
                    rules_to_check.append({
                        "index": len(rules_to_check) + 1,
                        "regle": rule_text.strip(),
                        "categorie": cat,
                    })

        if not rules_to_check:
            log.info(f"{prefix} : 0 règles — skip")
            processed.add(vid_id)
            save_checkpoint({"processed_video_ids": list(processed), "results": results})
            continue

        # ── Charger le transcript ────────────────────────────────────────
        transcript_text = load_transcript(transcript_file)

        if not transcript_text:
            log.warning(f"{prefix} : transcript vide — {len(rules_to_check)} règles → AMBIGU")
            for r in rules_to_check:
                if r["regle"] not in results:
                    results[r["regle"]] = {
                        "video_id": vid_id, "transcript_file": transcript_file,
                        "categorie": r["categorie"], "verdict": "AMBIGU",
                        "passage": None, "confiance": 0.0,
                        "note": "Transcript introuvable",
                    }
            processed.add(vid_id)
            save_checkpoint({"processed_video_ids": list(processed), "results": results})
            continue

        log.info(
            f"{prefix} : {len(rules_to_check)} règles | "
            f"transcript {len(transcript_text)} chars | {video_title[:50]}"
        )

        # ── Découper en batches si trop de règles ───────────────────────
        batches = [
            rules_to_check[j: j + MAX_RULES_PER_CALL]
            for j in range(0, len(rules_to_check), MAX_RULES_PER_CALL)
        ]

        all_api_results = {}

        for b_idx, batch in enumerate(batches):
            if dry_run:
                log.info(f"  [DRY RUN] batch {b_idx + 1}/{len(batches)} — {len(batch)} règles simulées")
                for r in batch:
                    all_api_results[r["index"]] = {
                        "verdict": "DRY_RUN", "passage": None,
                        "confiance": 0.0, "note": "Mode dry-run",
                    }
                continue

            time.sleep(RATE_LIMIT_SEC)
            api_res = verify_rules_against_transcript(
                client, transcript_text, batch, video_title
            )
            for res in api_res:
                all_api_results[res.get("index")] = res

            # Log résumé du batch
            verdicts = [r.get("verdict", "?") for r in api_res]
            v_count  = {v: verdicts.count(v) for v in set(verdicts)}
            log.info(f"  batch {b_idx + 1}/{len(batches)} : {v_count}")

        # ── Stocker les résultats ────────────────────────────────────────
        for r in rules_to_check:
            api_r = all_api_results.get(r["index"], {})
            if r["regle"] not in results:  # Ne pas écraser si déjà traité
                results[r["regle"]] = {
                    "video_id":        vid_id,
                    "transcript_file": transcript_file,
                    "categorie":       r["categorie"],
                    "verdict":         api_r.get("verdict", "AMBIGU"),
                    "passage":         api_r.get("passage"),
                    "confiance":       api_r.get("confiance", 0.0),
                    "note":            api_r.get("note", "Pas de réponse API"),
                }

        processed.add(vid_id)
        save_checkpoint({"processed_video_ids": list(processed), "results": results})

        # Compter verdicts pour cette vidéo
        vid_verdicts = [results[r["regle"]]["verdict"] for r in rules_to_check if r["regle"] in results]
        vc = {v: vid_verdicts.count(v) for v in set(vid_verdicts)}
        log.info(f"  ✓ checkpoint | {vc}")

    log.info(f"PASSE 1 terminée : {len(results)} règles traitées")
    return results


# =============================================================================
# PASSE 2 — RÈGLES ORPHELINES (dans aggregated_rules mais pas dans videos[])
# =============================================================================

def passe2_orphan_rules(
    kb: dict,
    rule_index: dict,
    passe1_results: dict,
    dry_run: bool,
    client,
) -> dict:
    """
    Certaines règles dans aggregated_rules peuvent ne pas avoir
    de correspondance exacte dans videos[] (légères reformulations lors
    de la déduplication). Cette passe les traite.

    Stratégie :
    1. Keyword pre-filter : trouver les transcripts potentiels via mots-clés
    2. Pour chaque transcript candidat : vérification Claude
    3. Si aucun candidat : INVALIDE (hallucination probable)
    """
    agg = kb.get("aggregated_rules", {})

    # Collecter toutes les règles de aggregated_rules
    all_agg_rules = []
    for cat, rules_list in agg.items():
        if not isinstance(rules_list, list):
            continue
        for rule_text in rules_list:
            if isinstance(rule_text, str) and rule_text.strip():
                all_agg_rules.append((cat, rule_text.strip()))

    # Identifier les orphelines : ni dans passe1_results ni dans rule_index
    orphans = [
        (cat, rule_text)
        for cat, rule_text in all_agg_rules
        if rule_text not in passe1_results and rule_text not in rule_index
    ]

    log.info(f"PASSE 2 — {len(orphans)} règles orphelines sur {len(all_agg_rules)} total")

    if not orphans:
        log.info("  Aucune règle orpheline → Passe 2 terminée immédiatement.")
        return {}

    # Pré-charger tous les transcripts (cache mémoire)
    log.info("  Chargement de tous les transcripts en cache...")
    transcript_cache = {}
    for vid_id, vid_data in kb.get("videos", {}).items():
        tf = vid_data.get("transcript_file", "")
        if tf and tf not in transcript_cache:
            transcript_cache[tf] = {
                "text": load_transcript(tf),
                "video_id": vid_id,
            }
    log.info(f"  {len(transcript_cache)} transcripts en cache")

    orphan_results = {}

    for idx, (cat, rule_text) in enumerate(orphans, 1):
        log.info(f"  Orpheline [{idx}/{len(orphans)}] : {rule_text[:70]}...")

        if dry_run:
            orphan_results[rule_text] = {
                "video_id": "ORPHAN", "transcript_file": "UNKNOWN",
                "categorie": cat, "verdict": "DRY_RUN",
                "passage": None, "confiance": 0.0,
                "note": "Orpheline — dry run",
            }
            continue

        # Keyword pre-filter : mots de plus de 5 lettres
        keywords = [w for w in rule_text.split() if len(w) > 5][:6]

        # Trouver les transcripts candidats (ceux qui contiennent au moins 2 mots-clés)
        candidates = []
        for tf, cache_entry in transcript_cache.items():
            text_lower = cache_entry["text"].lower()
            match_count = sum(1 for kw in keywords if kw.lower() in text_lower)
            if match_count >= 2:
                candidates.append((match_count, tf, cache_entry))

        # Trier par pertinence décroissante
        candidates.sort(key=lambda x: x[0], reverse=True)
        candidates = candidates[:3]  # Max 3 transcripts à tester

        if not candidates:
            log.info(f"    → Aucun candidat — INVALIDE")
            orphan_results[rule_text] = {
                "video_id": "ORPHAN", "transcript_file": "NON_TROUVE",
                "categorie": cat, "verdict": "INVALIDE",
                "passage": None, "confiance": 0.0,
                "note": "Absente de tous les transcripts — hallucination probable",
            }
            continue

        # Tester les candidats jusqu'à trouver VALIDE
        found = False
        for match_count, tf, cache_entry in candidates:
            time.sleep(RATE_LIMIT_SEC)
            api_results = verify_rules_against_transcript(
                client,
                cache_entry["text"],
                [{"index": 1, "regle": rule_text, "categorie": cat}],
                tf,
            )
            if api_results:
                res = api_results[0]
                if res.get("verdict") == "VALIDE":
                    orphan_results[rule_text] = {
                        "video_id":        cache_entry["video_id"],
                        "transcript_file": tf,
                        "categorie":       cat,
                        "verdict":         "VALIDE",
                        "passage":         res.get("passage"),
                        "confiance":       res.get("confiance", 0.8),
                        "note":            f"[CROSS-CORPUS, {match_count} kw] {res.get('note', '')}",
                    }
                    log.info(f"    → VALIDE dans {tf[:50]}")
                    found = True
                    break

        if not found:
            orphan_results[rule_text] = {
                "video_id": "ORPHAN", "transcript_file": "NON_CONFIRME",
                "categorie": cat, "verdict": "INVALIDE",
                "passage": None, "confiance": 0.0,
                "note": f"Testée sur {len(candidates)} candidats — non confirmée",
            }
            log.info(f"    → INVALIDE après {len(candidates)} candidats")

    log.info(f"PASSE 2 terminée : {len(orphan_results)} orphelines traitées")
    return orphan_results


# =============================================================================
# PASSE 3 — GÉNÉRATION DES RAPPORTS
# =============================================================================

def passe3_generate_reports(kb: dict, all_results: dict) -> dict:
    """
    Génère 3 fichiers de sortie :

    1. RAPPORT_VALIDATION.json — Résultats complets + statistiques
    2. KB_VALIDEE.json         — KB reconstruite avec statuts
    3. A_VERIFIER_HUMAIN.md   — Cas AMBIGU avec liens YouTube pour revue rapide

    Retourne les statistiques finales.
    """
    agg = kb.get("aggregated_rules", {})

    # ── Compteurs et collecte AMBIGU ──────────────────────────────────────
    stats = {v: 0 for v in [*VERDICTS_VALIDES, "DRY_RUN", "NON_TRAITE"]}
    ambigus = []

    # ── KB validée — reconstruire avec statuts ────────────────────────────
    kb_validee_rules = {}

    for cat, rules_list in agg.items():
        kb_validee_rules[cat] = {"VALIDE": [], "INVALIDE": [], "AMBIGU": []}
        if not isinstance(rules_list, list):
            continue

        for rule_text in rules_list:
            if not isinstance(rule_text, str):
                continue

            result  = all_results.get(rule_text.strip(), {})
            verdict = result.get("verdict", "NON_TRAITE")
            stats[verdict] = stats.get(verdict, 0) + 1

            entry = {
                "texte":             rule_text,
                "statut":            verdict,
                "passage":           result.get("passage"),
                "confiance":         result.get("confiance", 0.0),
                "source_video_id":   result.get("video_id"),
                "source_transcript": result.get("transcript_file"),
                "note":              result.get("note"),
            }

            # Stocker dans le bon bucket
            bucket = verdict if verdict in ["VALIDE", "INVALIDE", "AMBIGU"] else "AMBIGU"
            kb_validee_rules[cat][bucket].append(entry)

            if verdict == "AMBIGU":
                vid_id = result.get("video_id", "")
                ambigus.append({
                    "categorie":       cat,
                    "regle":           rule_text,
                    "video_id":        vid_id,
                    "transcript_file": result.get("transcript_file", ""),
                    "youtube_url":     (
                        f"https://youtube.com/watch?v={vid_id}"
                        if vid_id and vid_id not in ("ORPHAN", "FOUND_CROSS_CORPUS", "")
                        else "URL inconnue"
                    ),
                    "note":            result.get("note", ""),
                })

    total = sum(stats.values())
    taux  = round(stats.get("VALIDE", 0) / max(total, 1) * 100, 1)

    # ── 1. RAPPORT_VALIDATION.json ────────────────────────────────────────
    rapport = {
        "generated_at":    datetime.now().isoformat(),
        "total_regles":    total,
        "stats":           stats,
        "taux_valide_pct": taux,
        "nb_ambigus":      len(ambigus),
        "details":         all_results,
    }
    atomic_write(RAPPORT_PATH, rapport)
    log.info(f"✓ Rapport complet : {RAPPORT_PATH}")

    # ── 2. KB_VALIDEE.json ────────────────────────────────────────────────
    kb_validee = {
        "metadata": {
            **kb.get("metadata", {}),
            "validation": {
                "date":            datetime.now().isoformat(),
                "stats":           stats,
                "taux_valide_pct": taux,
                "script":          "validate_douteux.py v1.0",
            },
        },
        "rules_by_status": kb_validee_rules,
        "note": (
            "Utiliser uniquement les règles statut=VALIDE pour les signaux réels. "
            "AMBIGU = revue humaine requise. INVALIDE = supprimées."
        ),
    }
    atomic_write(KB_VALIDEE_PATH, kb_validee)
    log.info(f"✓ KB validée : {KB_VALIDEE_PATH}")

    # ── 3. A_VERIFIER_HUMAIN.md ───────────────────────────────────────────
    lines = [
        "# RÈGLES À VÉRIFIER HUMAINEMENT",
        "",
        f"> Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}",
        f"> **{len(ambigus)} règles AMBIGU** sur {total} règles totales ({taux}% VALIDE automatiquement)",
        "",
        "## Comment utiliser ce fichier",
        "",
        "Pour chaque règle ci-dessous :",
        "1. Clique sur le lien YouTube",
        "2. Cherche le sujet de la règle dans la vidéo (écoute quelques minutes)",
        "3. Si Belkhayate le dit → écris **VALIDE** à côté",
        "4. Sinon → écris **INVALIDE**",
        "",
        "Tu n'as pas besoin de regarder la vidéo en entier — Claude a déjà trouvé",
        "la vidéo probable. Cherche juste si le concept est présent.",
        "",
        "---",
        "",
    ]

    for idx, a in enumerate(ambigus, 1):
        lines += [
            f"## #{idx:03d} — {a['categorie'].upper()}",
            f"**Règle :** {a['regle']}",
            f"**Vidéo :** `{a['transcript_file']}`",
            f"**Lien :** {a['youtube_url']}",
            f"**Note Claude :** *{a['note']}*",
            "",
            "**Ton verdict :** [ ] VALIDE  [ ] INVALIDE",
            "",
            "---",
            "",
        ]

    with open(HUMAIN_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log.info(f"✓ Revue humaine : {HUMAIN_PATH}")

    return stats


# =============================================================================
# VÉRIFICATION PRÉ-VOL
# =============================================================================

def preflight_checks() -> bool:
    """Vérifie que tout est en place avant de démarrer."""
    ok = True

    if not os.path.exists(KB_PATH):
        log.error(f"KB introuvable : {KB_PATH}")
        ok = False

    if not os.path.isdir(TRANSCRIPTS_DIR):
        log.error(f"Dossier transcripts introuvable : {TRANSCRIPTS_DIR}")
        ok = False
    else:
        nb_txt = len([f for f in os.listdir(TRANSCRIPTS_DIR) if f.endswith(".txt")])
        log.info(f"✓ {nb_txt} transcripts disponibles")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        log.warning("ANTHROPIC_API_KEY non définie — mode dry-run seulement")

    return ok


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validation des règles DOUTEUX de la KB Belkhayate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples :
  python validate_douteux.py --dry-run        # Tester la structure sans dépenser
  python validate_douteux.py                   # Lancer la validation complète
  python validate_douteux.py --reset           # Repartir de zéro
  python validate_douteux.py --passe 3         # Générer rapports depuis checkpoint existant
        """,
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Simuler sans appels Claude (gratuit)")
    parser.add_argument("--reset", action="store_true",
                        help="Supprimer le checkpoint et recommencer depuis le début")
    parser.add_argument("--passe", type=int, choices=[1, 2, 3],
                        help="Exécuter une seule passe (défaut: les 3)")
    args = parser.parse_args()

    # ── Header ──────────────────────────────────────────────────────────
    log.info("=" * 70)
    log.info("VALIDATE_DOUTEUX v1.0 — Pipeline validation KB Belkhayate")
    log.info(f"Mode     : {'DRY RUN (simulation)' if args.dry_run else 'PRODUCTION'}")
    log.info(f"Passe(s) : {args.passe if args.passe else '1 + 2 + 3 (complètes)'}")
    log.info(f"Modèle   : {CLAUDE_MODEL}")
    log.info(f"Output   : {OUTPUT_DIR}")
    log.info("=" * 70)

    # ── Vérification pré-vol ────────────────────────────────────────────
    if not preflight_checks():
        log.error("Pré-vol échoué — arrêt.")
        sys.exit(1)

    # ── Reset checkpoint ────────────────────────────────────────────────
    if args.reset and os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)
        log.info("Checkpoint supprimé — reprise de zéro.")

    # ── Chargement KB ───────────────────────────────────────────────────
    log.info("Chargement KB...")
    kb = load_kb()
    nb_videos = len(kb.get("videos", {}))
    nb_agg    = sum(
        len(v) for v in kb.get("aggregated_rules", {}).values()
        if isinstance(v, list)
    )
    log.info(f"KB chargée : {nb_videos} vidéos | {nb_agg} règles aggregated")

    # ── Index règle → vidéo ─────────────────────────────────────────────
    log.info("Construction index règles → vidéos...")
    rule_index = build_rule_index(kb)
    log.info(f"Index : {len(rule_index)} règles uniques indexées")

    # ── Client Claude ───────────────────────────────────────────────────
    client = None
    if not args.dry_run:
        try:
            import anthropic
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                log.error("ANTHROPIC_API_KEY manquante. Utilisez --dry-run ou définissez la clé.")
                sys.exit(1)
            client = anthropic.Anthropic(api_key=api_key)
            log.info(f"Client Claude initialisé (modèle : {CLAUDE_MODEL})")
        except ImportError:
            log.error("Package 'anthropic' manquant. Lancez :")
            log.error("  pip install anthropic --break-system-packages")
            sys.exit(1)

    # ── PASSE 1 ─────────────────────────────────────────────────────────
    passe1_results = {}
    if not args.passe or args.passe == 1:
        passe1_results = passe1_verify_by_transcript(kb, rule_index, args.dry_run, client)

    # ── PASSE 2 ─────────────────────────────────────────────────────────
    passe2_results = {}
    if not args.passe or args.passe == 2:
        if not passe1_results:
            # Charger depuis checkpoint si passe1 non exécutée
            checkpoint = load_checkpoint()
            passe1_results = checkpoint.get("results", {})
            log.info(f"Passe 1 chargée depuis checkpoint : {len(passe1_results)} règles")
        passe2_results = passe2_orphan_rules(
            kb, rule_index, passe1_results, args.dry_run, client
        )

    # ── PASSE 3 ─────────────────────────────────────────────────────────
    if not args.passe or args.passe == 3:
        # Fusionner résultats des passes 1 et 2
        if not passe1_results and not passe2_results:
            checkpoint = load_checkpoint()
            passe1_results = checkpoint.get("results", {})
            log.info(f"Résultats chargés depuis checkpoint : {len(passe1_results)} règles")

        all_results = {**passe1_results, **passe2_results}
        stats = passe3_generate_reports(kb, all_results)

        # ── Résumé final ─────────────────────────────────────────────
        log.info("")
        log.info("=" * 70)
        log.info("RÉSULTATS FINAUX")
        log.info("-" * 70)
        total = sum(stats.values())
        for verdict in ["VALIDE", "INVALIDE", "AMBIGU", "NON_TRAITE", "DRY_RUN"]:
            count = stats.get(verdict, 0)
            if count > 0:
                pct = round(count / max(total, 1) * 100, 1)
                log.info(f"  {verdict:<15} : {count:>4} ({pct}%)")
        log.info("-" * 70)
        log.info(f"  TOTAL          : {total}")
        log.info(f"  TAUX VALIDE    : {round(stats.get('VALIDE', 0) / max(total, 1) * 100, 1)}%")
        log.info("=" * 70)
        log.info("")
        log.info(f"Rapports disponibles dans : {OUTPUT_DIR}")
        log.info(f"  → {RAPPORT_PATH}")
        log.info(f"  → {KB_VALIDEE_PATH}")
        log.info(f"  → {HUMAIN_PATH}")

    log.info("Terminé.")


if __name__ == "__main__":
    main()
