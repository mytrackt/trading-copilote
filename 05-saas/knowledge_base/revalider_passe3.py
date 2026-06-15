#!/usr/bin/env python3
"""
revalider_passe3.py -- 3e passe de validation sur les regles AMBIGU
Version : 1.0 | Session S14 | 15/06/2026

CONTEXTE :
  Apres S13, il reste 103 AMBIGU dont :
    - 63 "Pas de reponse API" : echec technique, pas ambigus par nature
    - 40 autres : franchement ambigus -> revue humaine (intouches ici)

STRATEGIE :
  Les 63 "Pas de reponse API" -> passe semantique Sonnet
  (meme approche que Groupe B de S13, la plus efficace : +276 VALIDE)
  Les 40 autres restent AMBIGU.

ENTREE  : 04-cerveau-trading/validation/KB_VALIDEE.json
SORTIES : KB_VALIDEE.json (mise a jour), A_VERIFIER_HUMAIN.md (reduit), RAPPORT_PASSE3.json

USAGE :
  py revalider_passe3.py --dry-run     # Simuler sans appels API
  py revalider_passe3.py               # Production
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
# CHEMINS ABSOLUS (REGLE 1)
# =============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

TRANSCRIPTS_DIR = os.path.join(ROOT_DIR, "03-transcriptions", "nouvelles-sources",
                                "belkhayate-youtube", "transcripts")
VALIDATION_DIR  = os.path.join(ROOT_DIR, "04-cerveau-trading", "validation")
KB_VALIDEE_PATH = os.path.join(VALIDATION_DIR, "KB_VALIDEE.json")
HUMAIN_PATH     = os.path.join(VALIDATION_DIR, "A_VERIFIER_HUMAIN.md")
RAPPORT_PATH    = os.path.join(VALIDATION_DIR, "RAPPORT_PASSE3.json")
LOG_PATH        = os.path.join(VALIDATION_DIR, "revalider_passe3.log")

# =============================================================================
# PARAMETRES
# =============================================================================

RATE_LIMIT_SEC       = 0.3   # 6 appels seulement -- pas de risque de rate limit
MAX_TRANSCRIPT_CHARS = 14000
MAX_RULES_PER_CALL   = 20

MODEL_SEMANTIQUE = "claude-sonnet-4-6"   # Passe semantique (meilleure comprehension)
VERDICTS_VALIDES = {"VALIDE", "INVALIDE", "AMBIGU"}

# =============================================================================
# LOGGING
# =============================================================================

os.makedirs(VALIDATION_DIR, exist_ok=True)

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
    """Ecriture JSON atomique (tempfile + os.replace). REGLE 6."""
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
    """Extrait le JSON de la reponse Claude. Jamais json.loads() direct (REGLE 5)."""
    patterns = [
        r"```json\s*(.*?)\s*```",
        r"```\s*(.*?)\s*```",
        r"(\{.*\})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        return None


def load_transcript(transcript_file: str) -> str:
    """Charge un transcript. Tronque si > MAX_TRANSCRIPT_CHARS."""
    path = os.path.join(TRANSCRIPTS_DIR, transcript_file)
    if not os.path.exists(path):
        log.warning(f"  Transcript introuvable : {transcript_file}")
        return ""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    if len(content) > MAX_TRANSCRIPT_CHARS:
        content = content[:MAX_TRANSCRIPT_CHARS] + "\n[...TRONQUE...]"
    return content


def load_kb_validee() -> dict:
    """Charge KB_VALIDEE.json."""
    with open(KB_VALIDEE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# EXTRACTION DES "PAS DE REPONSE API"
# =============================================================================

def extraire_pas_reponse(kb_validee: dict) -> tuple:
    """
    Extrait les AMBIGU en 2 groupes :
      - pas_reponse : "Pas de reponse API" -> 3e passe Sonnet
      - humain      : autres -> revue humaine (intouches)
    """
    pas_reponse = []
    humain      = []

    for cat, buckets in kb_validee.get("rules_by_status", {}).items():
        for entry in buckets.get("AMBIGU", []):
            note = entry.get("note", "")
            item = {
                "categorie":         cat,
                "texte":             entry.get("texte", ""),
                "source_video_id":   entry.get("source_video_id", ""),
                "source_transcript": entry.get("source_transcript", ""),
                "note":              note,
            }
            if "Pas de r" in note and "ponse API" in note:
                pas_reponse.append(item)
            else:
                humain.append(item)

    log.info(f"Extraction -> pas_reponse:{len(pas_reponse)}  humain:{len(humain)}")
    return pas_reponse, humain


# =============================================================================
# PROMPT SEMANTIQUE
# =============================================================================

def prompt_semantique(transcript_text: str, rules: list, video_title: str) -> str:
    rules_block = "\n".join(
        f'{r["index"]}. [{r["categorie"].upper()}] {r["texte"]}'
        for r in rules
    )
    return (
        f'Tu es un expert de la methode de trading Mustapha Belkhayate.\n\n'
        f'TRANSCRIPT (video : "{video_title}") :\n---\n{transcript_text}\n---\n\n'
        f'REGLES A VERIFIER ({len(rules)} regles) :\n{rules_block}\n\n'
        f'MISSION : Verifier si le CONCEPT de chaque regle est present dans ce transcript.\n\n'
        f'IMPORTANT : On ne cherche PAS une citation mot-a-mot.\n'
        f'On cherche si l\'IDEE est presente, meme exprimee differemment.\n'
        f'La paraphrase ou l\'implication claire est suffisante.\n\n'
        f'CRITERES :\n'
        f'  VALIDE   = concept clairement present (directement ou par implication forte).\n'
        f'  INVALIDE = concept absent ou contredit.\n'
        f'  AMBIGU   = concept effleure mais pas assez developpe pour confirmer.\n\n'
        f'Reponds UNIQUEMENT avec ce JSON :\n'
        f'{{"resultats": [{{"index": <int>, "verdict": "VALIDE"|"INVALIDE"|"AMBIGU", '
        f'"passage": "<extrait illustratif>", "confiance": <float 0-1>, "note": "<max 100 chars>"}}]}}'
    )


# =============================================================================
# APPEL CLAUDE
# =============================================================================

def appel_claude(client, prompt: str, rules: list) -> list:
    """Passe semantique Sonnet sans check verbatim."""
    try:
        response = client.messages.create(
            model=MODEL_SEMANTIQUE,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = response.content[0].text.strip()
        parsed = parse_claude_json(raw_text)

        if not parsed or "resultats" not in parsed:
            log.error(f"  JSON invalide : {raw_text[:200]}")
            return []

        validated = []
        for res in parsed["resultats"]:
            if res.get("verdict") not in VERDICTS_VALIDES:
                res["verdict"] = "AMBIGU"
                res["note"] = f"[VERDICT INVALIDE CORRIGE] {res.get('note', '')}"
            res["confiance"] = max(0.0, min(1.0, float(res.get("confiance", 0.5))))
            validated.append(res)

        return validated

    except Exception as e:
        log.error(f"  Erreur API : {type(e).__name__}: {e}")
        return []


# =============================================================================
# TRAITEMENT
# =============================================================================

def traiter_pas_reponse(rules: list, dry_run: bool, client) -> dict:
    """
    Passe semantique Sonnet sur les regles 'Pas de reponse API'.
    Regroupe par transcript pour economiser les appels.
    """
    log.info(f"=== 3e PASSE SEMANTIQUE -- {len(rules)} regles ===")

    by_transcript: dict = {}
    for item in rules:
        tf = item.get("source_transcript", "UNKNOWN")
        if tf not in by_transcript:
            by_transcript[tf] = []
        by_transcript[tf].append(item)

    log.info(f"  -> {len(by_transcript)} transcripts uniques")

    results = {}

    for tf_idx, (transcript_file, tf_rules) in enumerate(by_transcript.items(), 1):
        video_title = transcript_file.replace(".txt", "")[:70]
        log.info(f"  [{tf_idx:03d}/{len(by_transcript)}] {video_title[:55]} -- {len(tf_rules)} regles")

        transcript_text = load_transcript(transcript_file)

        if not transcript_text:
            for item in tf_rules:
                results[item["texte"]] = {
                    "verdict": "AMBIGU", "passage": None,
                    "confiance": 0.0, "note": "Transcript introuvable",
                }
            continue

        batches = [
            tf_rules[j: j + MAX_RULES_PER_CALL]
            for j in range(0, len(tf_rules), MAX_RULES_PER_CALL)
        ]

        for b_idx, batch in enumerate(batches):
            batch_indexed = [{**item, "index": i + 1} for i, item in enumerate(batch)]

            if dry_run:
                log.info(f"    [DRY RUN] batch {b_idx+1}/{len(batches)} -- {len(batch)} regles simulees")
                for item in batch:
                    results[item["texte"]] = {
                        "verdict": "DRY_RUN", "passage": None,
                        "confiance": 0.0, "note": "3e passe -- dry run",
                    }
                continue

            time.sleep(RATE_LIMIT_SEC)
            prompt = prompt_semantique(transcript_text, batch_indexed, video_title)
            api_res = appel_claude(client, prompt, batch_indexed)

            api_by_index = {r.get("index"): r for r in api_res}

            for item in batch_indexed:
                r = api_by_index.get(item["index"], {})
                if not r or "verdict" not in r:
                    results[item["texte"]] = {
                        "verdict": "AMBIGU", "passage": None,
                        "confiance": 0.0,
                        "note": "Pas de reponse API (passe 3)",
                    }
                else:
                    results[item["texte"]] = r

            verdicts = [results[item["texte"]]["verdict"] for item in batch_indexed]
            vc = {v: verdicts.count(v) for v in set(verdicts)}
            log.info(f"    batch {b_idx+1}/{len(batches)} : {vc}")

    log.info(f"  3e passe terminee : {len(results)} regles traitees")
    return results


# =============================================================================
# MISE A JOUR KB_VALIDEE.JSON
# =============================================================================

def mettre_a_jour_kb(kb_validee: dict, nouveaux_verdicts: dict) -> tuple:
    """Deplace les AMBIGU vers VALIDE/INVALIDE selon les nouveaux verdicts."""
    stats = {"VALIDE_gagne": 0, "INVALIDE_gagne": 0, "reste_AMBIGU": 0, "DRY_RUN": 0}

    for cat, buckets in kb_validee.get("rules_by_status", {}).items():
        anciens = buckets.get("AMBIGU", [])
        nouveaux_ambigu = []

        for entry in anciens:
            texte = entry.get("texte", "")
            if texte not in nouveaux_verdicts:
                nouveaux_ambigu.append(entry)
                stats["reste_AMBIGU"] += 1
                continue

            nv = nouveaux_verdicts[texte]
            verdict = nv.get("verdict", "AMBIGU")

            if verdict == "DRY_RUN":
                nouveaux_ambigu.append(entry)
                stats["DRY_RUN"] += 1

            elif verdict == "VALIDE":
                e = dict(entry)
                e["statut"]    = "VALIDE"
                e["passage"]   = nv.get("passage")
                e["confiance"] = nv.get("confiance", 0.8)
                e["note"]      = f"[REVALIDE S14 passe3] {nv.get('note', '')}"
                buckets.setdefault("VALIDE", []).append(e)
                stats["VALIDE_gagne"] += 1

            elif verdict == "INVALIDE":
                e = dict(entry)
                e["statut"]    = "INVALIDE"
                e["passage"]   = None
                e["confiance"] = nv.get("confiance", 0.1)
                e["note"]      = f"[REVALIDE S14 passe3] {nv.get('note', '')}"
                buckets.setdefault("INVALIDE", []).append(e)
                stats["INVALIDE_gagne"] += 1

            else:  # AMBIGU
                nouveaux_ambigu.append(entry)
                stats["reste_AMBIGU"] += 1

        buckets["AMBIGU"] = nouveaux_ambigu

    log.info(f"KB mise a jour -> {stats}")
    return kb_validee, stats


# =============================================================================
# REGENERATION A_VERIFIER_HUMAIN.MD
# =============================================================================

def generer_humain_md(kb_validee: dict) -> int:
    """Regenere A_VERIFIER_HUMAIN.md avec les AMBIGU restants."""
    ambigus = []

    for cat, buckets in kb_validee.get("rules_by_status", {}).items():
        for entry in buckets.get("AMBIGU", []):
            vid_id = entry.get("source_video_id", "")
            ambigus.append({
                "categorie":       cat,
                "regle":           entry.get("texte", ""),
                "video_id":        vid_id,
                "transcript_file": entry.get("source_transcript", ""),
                "youtube_url": (
                    f"https://youtube.com/watch?v={vid_id}"
                    if vid_id and vid_id not in ("ORPHAN", "FOUND_CROSS_CORPUS", "")
                    else "URL inconnue"
                ),
                "note": entry.get("note", ""),
            })

    lines = [
        "# REGLES A VERIFIER HUMAINEMENT (apres revalidation S14 passe3)",
        "",
        f"> Genere le {datetime.now().strftime('%d/%m/%Y a %H:%M')}",
        f"> **{len(ambigus)} regles AMBIGU restantes** (apres 3e passe automatique)",
        "",
        "## Comment utiliser ce fichier",
        "",
        "Pour chaque regle ci-dessous :",
        "1. Clique sur le lien YouTube",
        "2. Cherche le sujet dans la video (quelques minutes suffisent)",
        "3. Belkhayate le dit clairement -> ecris **VALIDE**",
        "4. Absent ou contredit -> ecris **INVALIDE**",
        "",
        "---",
        "",
    ]

    for idx, a in enumerate(ambigus, 1):
        lines += [
            f"## #{idx:03d} -- {a['categorie'].upper()}",
            f"**Regle :** {a['regle']}",
            f"**Video :** `{a['transcript_file']}`",
            f"**Lien :** {a['youtube_url']}",
            f"**Note :** *{a['note']}*",
            "",
            "**Ton verdict :** [ ] VALIDE  [ ] INVALIDE",
            "",
            "---",
            "",
        ]

    with open(HUMAIN_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    log.info(f"A_VERIFIER_HUMAIN.md regenere -> {len(ambigus)} cas restants")
    return len(ambigus)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="3e passe semantique Sonnet -- regles AMBIGU Pas de reponse API",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Simuler sans appels Claude (aucun fichier modifie)")
    args = parser.parse_args()

    log.info("=" * 70)
    log.info("REVALIDER_PASSE3 v1.0 -- 3e passe semantique KB Belkhayate")
    log.info(f"Mode    : {'DRY RUN' if args.dry_run else 'PRODUCTION'}")
    log.info(f"Modele  : {MODEL_SEMANTIQUE}")
    log.info("=" * 70)

    if not os.path.exists(KB_VALIDEE_PATH):
        log.error(f"KB_VALIDEE.json introuvable : {KB_VALIDEE_PATH}")
        sys.exit(1)

    if not os.path.isdir(TRANSCRIPTS_DIR):
        log.error(f"Dossier transcripts introuvable : {TRANSCRIPTS_DIR}")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        log.error("ANTHROPIC_API_KEY manquante. Utilisez --dry-run ou definissez la cle.")
        sys.exit(1)

    client = None
    if not args.dry_run:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        log.info("Client Claude initialise")

    kb_validee = load_kb_validee()
    total_avant = sum(
        len(rules)
        for buckets in kb_validee.get("rules_by_status", {}).values()
        for rules in buckets.values()
    )
    log.info(f"KB chargee : {total_avant} regles")

    pas_reponse, humain = extraire_pas_reponse(kb_validee)
    log.info(f"  -> {len(pas_reponse)} 'Pas de reponse API' a traiter")
    log.info(f"  -> {len(humain)} autres AMBIGU laisses pour revue humaine")

    nb_transcripts = len(set(r["source_transcript"] for r in pas_reponse))
    log.info(f"  -> {nb_transcripts} transcripts uniques ({MODEL_SEMANTIQUE})")

    resultats = traiter_pas_reponse(pas_reponse, args.dry_run, client)

    kb_validee, stats = mettre_a_jour_kb(kb_validee, resultats)

    kb_validee.setdefault("metadata", {})["revalidation_s14_passe3"] = {
        "date":    datetime.now().isoformat(),
        "entree":  {"pas_reponse": len(pas_reponse), "humain": len(humain)},
        "gains":   stats,
    }

    if not args.dry_run:
        atomic_write(KB_VALIDEE_PATH, kb_validee)
        log.info("KB_VALIDEE.json mis a jour (atomic write)")
        nb_restants = generer_humain_md(kb_validee)
    else:
        log.info("[DRY RUN] Aucun fichier modifie")
        nb_restants = sum(
            len(b.get("AMBIGU", []))
            for b in kb_validee.get("rules_by_status", {}).values()
        )

    # Rapport
    totaux_finaux = {}
    for buckets in kb_validee.get("rules_by_status", {}).values():
        for status, rules in buckets.items():
            totaux_finaux[status] = totaux_finaux.get(status, 0) + len(rules)

    if not args.dry_run:
        rapport = {
            "generated_at":    datetime.now().isoformat(),
            "session":         "S14",
            "script":          "revalider_passe3.py v1.0",
            "stats":           stats,
            "totaux_finaux":   totaux_finaux,
            "ambigu_restants": nb_restants,
        }
        atomic_write(RAPPORT_PATH, rapport)

    log.info("")
    log.info("=" * 70)
    log.info("RESULTATS FINAUX")
    log.info("-" * 70)
    log.info(f"  VALIDE gagnes   : +{stats.get('VALIDE_gagne', 0)}")
    log.info(f"  INVALIDE gagnes : +{stats.get('INVALIDE_gagne', 0)}")
    log.info(f"  Restent AMBIGU  :  {stats.get('reste_AMBIGU', 0)}")
    log.info("-" * 70)
    for status in ["VALIDE", "INVALIDE", "AMBIGU"]:
        nb = totaux_finaux.get(status, 0)
        total = sum(totaux_finaux.values())
        pct = round(nb / max(total, 1) * 100, 1)
        log.info(f"  {status:<15} : {nb:>4} ({pct}%)")
    log.info("-" * 70)
    log.info(f"  A_VERIFIER_HUMAIN.md : {nb_restants} cas restants")
    log.info("=" * 70)
    log.info("Termine.")


if __name__ == "__main__":
    main()
