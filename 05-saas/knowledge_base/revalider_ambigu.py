#!/usr/bin/env python3
"""
revalider_ambigu.py -- 2e passe de validation sur les regles AMBIGU
Version : 1.1 | Session S13 | 15/06/2026

PROBLEME :
  validate_douteux.py v1.0 a produit 388 AMBIGU dont :
    - 220 "[CITATION NON VERBATIM]" : Claude a trouve le concept mais pas mot-a-mot
    - 132 "Pas de reponse API"       : timeout/erreur -- jamais traite
    -  36 autres                      : cas franchement ambigus -> revue humaine

STRATEGIE :
  GROUPE A -- "Pas de reponse API" (132)
    -> Re-run identique a validate_douteux.py (Haiku, check verbatim)
    -> Regroupe par transcript pour economiser les appels API

  GROUPE B -- "NON VERBATIM" (220)
    -> Passe semantique avec Sonnet : concept present ? (pas besoin de verbatim)
    -> NO verbatim check : Claude est autorise a confirmer par paraphrase
    -> Regroupe par transcript

  GROUPE C -- Autres (36)
    -> Gardes AMBIGU -> revue humaine dans A_VERIFIER_HUMAIN.md

ENTREE  : 04-cerveau-trading/validation/KB_VALIDEE.json
SORTIES : KB_VALIDEE.json (mise a jour), A_VERIFIER_HUMAIN.md (reduit), RAPPORT_REVALIDATION.json

USAGE :
  py revalider_ambigu.py --dry-run     # Tester sans depenser (aucun appel API, aucun fichier modifie)
  py revalider_ambigu.py               # Production
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
RAPPORT_PATH    = os.path.join(VALIDATION_DIR, "RAPPORT_REVALIDATION.json")
LOG_PATH        = os.path.join(VALIDATION_DIR, "revalider_ambigu.log")

# =============================================================================
# PARAMETRES
# =============================================================================

RATE_LIMIT_SEC       = 1.5
MAX_TRANSCRIPT_CHARS = 14000
MAX_RULES_PER_CALL   = 20

MODEL_GROUPE_A = "claude-haiku-4-5-20251001"   # Re-run erreurs API (moins cher)
MODEL_GROUPE_B = "claude-sonnet-4-6"            # Passe semantique (meilleure comprehension)

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
    """Ecriture JSON atomique (tempfile + os.replace)."""
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
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if len(content) > MAX_TRANSCRIPT_CHARS:
        content = content[:MAX_TRANSCRIPT_CHARS] + "\n[...TRONQUE...]"
    return content


def load_kb_validee() -> dict:
    """Charge KB_VALIDEE.json."""
    with open(KB_VALIDEE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# EXTRACTION DES AMBIGU
# =============================================================================

def extraire_ambigus(kb_validee: dict) -> tuple:
    """
    Parcourt KB_VALIDEE.json et extrait les 388 AMBIGU en 3 groupes.
    Retourne (groupe_a, groupe_b, groupe_c)
    """
    groupe_a = []  # Pas de reponse API -> re-run
    groupe_b = []  # NON VERBATIM -> passe semantique
    groupe_c = []  # Autres -> humain

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
            if "Pas de reponse API" in note or "Pas de réponse API" in note:
                groupe_a.append(item)
            elif "NON VERBATIM" in note:
                groupe_b.append(item)
            else:
                groupe_c.append(item)

    log.info(f"Groupes extraits -> A:{len(groupe_a)}  B:{len(groupe_b)}  C:{len(groupe_c)}")
    return groupe_a, groupe_b, groupe_c


# =============================================================================
# PROMPT GROUPE A -- Verification classique (check verbatim)
# =============================================================================

def prompt_groupe_a(transcript_text: str, rules: list, video_title: str) -> str:
    rules_block = "\n".join(
        f'{r["index"]}. [{r["categorie"].upper()}] {r["texte"]}'
        for r in rules
    )
    return (
        f'Tu es un auditeur rigoureux de regles de trading Belkhayate.\n\n'
        f'TRANSCRIPT (video : "{video_title}") :\n---\n{transcript_text}\n---\n\n'
        f'REGLES A VERIFIER ({len(rules)} regles) :\n{rules_block}\n\n'
        f'INSTRUCTIONS :\n'
        f'1. Pour chaque regle, cherche un passage EXPLICITE dans le transcript.\n'
        f'2. VALIDE  = passage confirme clairement la regle.\n'
        f'3. INVALIDE = regle absente ou contredite.\n'
        f'4. AMBIGU  = sujet aborde mais pas assez precisement.\n'
        f'5. "passage" = citation exacte mot-a-mot. null si pas trouve.\n\n'
        f'Reponds UNIQUEMENT avec ce JSON :\n'
        f'{{"resultats": [{{"index": <int>, "verdict": "VALIDE"|"INVALIDE"|"AMBIGU", '
        f'"passage": "<citation exacte>"|null, "confiance": <float 0-1>, "note": "<max 100 chars>"}}]}}'
    )


# =============================================================================
# PROMPT GROUPE B -- Passe semantique (PAS de check verbatim)
# =============================================================================

def prompt_groupe_b(transcript_text: str, rules: list, video_title: str) -> str:
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
# APPEL CLAUDE -- GENERIQUE
# =============================================================================

def appel_claude(
    client,
    prompt: str,
    rules: list,
    check_verbatim: bool,
    transcript_text: str,
) -> list:
    """
    Appel Claude unique.
    check_verbatim=True  -> Groupe A (verification mot-a-mot anti-hallucination)
    check_verbatim=False -> Groupe B (passe semantique, pas de check verbatim)
    """
    try:
        model = MODEL_GROUPE_A if check_verbatim else MODEL_GROUPE_B
        response = client.messages.create(
            model=model,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        raw_text = response.content[0].text.strip()
        parsed = parse_claude_json(raw_text)

        if not parsed or "resultats" not in parsed:
            log.error(f"  JSON invalide : {raw_text[:200]}")
            return []

        resultats = parsed["resultats"]
        validated = []

        for res in resultats:
            if res.get("verdict") not in VERDICTS_VALIDES:
                res["verdict"] = "AMBIGU"
                res["note"] = f"[VERDICT INVALIDE CORRIGE] {res.get('note', '')}"

            if check_verbatim:
                passage = res.get("passage")
                if passage and isinstance(passage, str):
                    passage_norm    = " ".join(passage.split())
                    transcript_norm = " ".join(transcript_text.split())
                    if passage_norm not in transcript_norm:
                        log.warning(f"  Citation non verbatim -> AMBIGU : {passage[:60]}...")
                        res["verdict"] = "AMBIGU"
                        res["passage"] = None
                        res["note"]    = f"[NON VERBATIM GROUPE A] {res.get('note', '')}"

            res["confiance"] = max(0.0, min(1.0, float(res.get("confiance", 0.5))))
            validated.append(res)

        return validated

    except Exception as e:
        log.error(f"  Erreur API : {type(e).__name__}: {e}")
        return []


# =============================================================================
# TRAITEMENT D'UN GROUPE (A ou B)
# =============================================================================

def traiter_groupe(
    group_name: str,
    rules: list,
    build_prompt_fn,
    check_verbatim: bool,
    dry_run: bool,
    client,
) -> dict:
    """
    Traite un groupe de regles AMBIGU.
    Regroupe par transcript pour minimiser les appels API.
    Retourne : {texte_regle: {verdict, passage, confiance, note}}
    """
    log.info(f"=== GROUPE {group_name} -- {len(rules)} regles ===")

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
        log.info(f"  [{tf_idx:03d}/{len(by_transcript)}] {video_title[:50]} -- {len(tf_rules)} regles")

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
            batch_indexed = [
                {**item, "index": i + 1}
                for i, item in enumerate(batch)
            ]

            if dry_run:
                log.info(f"    [DRY RUN] batch {b_idx+1}/{len(batches)} -- {len(batch)} regles simulees")
                for item in batch:
                    results[item["texte"]] = {
                        "verdict": "DRY_RUN", "passage": None,
                        "confiance": 0.0, "note": f"Groupe {group_name} -- dry run",
                    }
                continue

            time.sleep(RATE_LIMIT_SEC)
            prompt = build_prompt_fn(transcript_text, batch_indexed, video_title)
            api_res = appel_claude(client, prompt, batch_indexed, check_verbatim, transcript_text)

            api_by_index = {r.get("index"): r for r in api_res}

            for item in batch_indexed:
                r = results[item["texte"]] = api_by_index.get(item["index"], {})
                if not r or "verdict" not in r:
                    results[item["texte"]] = {
                        "verdict": "AMBIGU", "passage": None,
                        "confiance": 0.0,
                        "note": f"Pas de reponse API (Groupe {group_name})",
                    }

            verdicts = [results[item["texte"]]["verdict"] for item in batch_indexed]
            vc = {v: verdicts.count(v) for v in set(verdicts)}
            log.info(f"    batch {b_idx+1}/{len(batches)} : {vc}")

    log.info(f"  Groupe {group_name} termine : {len(results)} regles")
    return results


# =============================================================================
# MISE A JOUR KB_VALIDEE.JSON
# =============================================================================

def mettre_a_jour_kb(kb_validee: dict, nouveaux_verdicts: dict) -> tuple:
    """
    Deplace les regles AMBIGU vers VALIDE ou INVALIDE selon les nouveaux verdicts.
    Les DRY_RUN et les non-traites restent AMBIGU.
    """
    stats_update = {"VALIDE_gagne": 0, "INVALIDE_gagne": 0, "reste_AMBIGU": 0, "DRY_RUN": 0}

    for cat, buckets in kb_validee.get("rules_by_status", {}).items():
        anciens_ambigus = buckets.get("AMBIGU", [])
        nouveaux_ambigus = []

        for entry in anciens_ambigus:
            texte = entry.get("texte", "")
            if texte in nouveaux_verdicts:
                nv = nouveaux_verdicts[texte]
                nouveau_verdict = nv.get("verdict", "AMBIGU")

                if nouveau_verdict == "DRY_RUN":
                    nouveaux_ambigus.append(entry)
                    stats_update["DRY_RUN"] += 1

                elif nouveau_verdict == "VALIDE":
                    entry_v = dict(entry)
                    entry_v["statut"]    = "VALIDE"
                    entry_v["passage"]   = nv.get("passage")
                    entry_v["confiance"] = nv.get("confiance", 0.8)
                    entry_v["note"]      = f"[REVALIDE S13] {nv.get('note', '')}"
                    buckets.setdefault("VALIDE", []).append(entry_v)
                    stats_update["VALIDE_gagne"] += 1

                elif nouveau_verdict == "INVALIDE":
                    entry_i = dict(entry)
                    entry_i["statut"]    = "INVALIDE"
                    entry_i["passage"]   = None
                    entry_i["confiance"] = nv.get("confiance", 0.1)
                    entry_i["note"]      = f"[REVALIDE S13] {nv.get('note', '')}"
                    buckets.setdefault("INVALIDE", []).append(entry_i)
                    stats_update["INVALIDE_gagne"] += 1

                else:
                    nouveaux_ambigus.append(entry)
                    stats_update["reste_AMBIGU"] += 1
            else:
                nouveaux_ambigus.append(entry)
                stats_update["reste_AMBIGU"] += 1

        buckets["AMBIGU"] = nouveaux_ambigus

    log.info(f"Mise a jour KB -> {stats_update}")
    return kb_validee, stats_update


# =============================================================================
# GENERATION A_VERIFIER_HUMAIN.MD
# =============================================================================

def generer_humain_md(kb_validee: dict) -> int:
    """Regenere A_VERIFIER_HUMAIN.md avec les AMBIGU restants. Retourne le nb."""
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
        "# REGLES A VERIFIER HUMAINEMENT (apres revalidation S13)",
        "",
        f"> Genere le {datetime.now().strftime('%d/%m/%Y a %H:%M')}",
        f"> **{len(ambigus)} regles AMBIGU restantes** (apres 2e passe automatique)",
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

    log.info(f"A_VERIFIER_HUMAIN.md -> {len(ambigus)} cas restants")
    return len(ambigus)


# =============================================================================
# RAPPORT FINAL
# =============================================================================

def generer_rapport(stats_update: dict, nb_restants: int, kb_validee: dict) -> None:
    totaux = {}
    for cat, buckets in kb_validee.get("rules_by_status", {}).items():
        for status, rules in buckets.items():
            totaux[status] = totaux.get(status, 0) + len(rules)

    rapport = {
        "generated_at":  datetime.now().isoformat(),
        "session":       "S13",
        "script":        "revalider_ambigu.py v1.1",
        "stats_update":  stats_update,
        "totaux_finaux": totaux,
        "ambigu_restants": nb_restants,
    }
    atomic_write(RAPPORT_PATH, rapport)
    log.info(f"Rapport : {RAPPORT_PATH}")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="2e passe de validation -- regles AMBIGU de KB_VALIDEE.json",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Simuler sans appels Claude (aucun fichier modifie)")
    args = parser.parse_args()

    log.info("=" * 70)
    log.info("REVALIDER_AMBIGU v1.1 -- 2e passe semantique KB Belkhayate")
    log.info(f"Mode     : {'DRY RUN (simulation - aucun fichier modifie)' if args.dry_run else 'PRODUCTION'}")
    log.info(f"Groupe A : {MODEL_GROUPE_A} (re-run erreurs API)")
    log.info(f"Groupe B : {MODEL_GROUPE_B} (passe semantique NON VERBATIM)")
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

    log.info("Chargement KB_VALIDEE.json...")
    kb_validee = load_kb_validee()
    total_avant = sum(
        len(rules)
        for buckets in kb_validee.get("rules_by_status", {}).values()
        for rules in buckets.values()
    )
    log.info(f"KB chargee : {total_avant} regles au total")

    groupe_a, groupe_b, groupe_c = extraire_ambigus(kb_validee)
    log.info(f"Total AMBIGU : {len(groupe_a) + len(groupe_b) + len(groupe_c)}")
    log.info(f"  A (erreurs API)  : {len(groupe_a)}")
    log.info(f"  B (NON VERBATIM) : {len(groupe_b)}")
    log.info(f"  C (autres/humain): {len(groupe_c)}")

    a_transcripts = len(set(r["source_transcript"] for r in groupe_a))
    b_transcripts = len(set(r["source_transcript"] for r in groupe_b))
    log.info(f"Appels API estimes : {a_transcripts} Haiku + {b_transcripts} Sonnet")

    resultats_a = {}
    if groupe_a:
        resultats_a = traiter_groupe(
            group_name="A", rules=groupe_a,
            build_prompt_fn=prompt_groupe_a, check_verbatim=True,
            dry_run=args.dry_run, client=client,
        )

    resultats_b = {}
    if groupe_b:
        resultats_b = traiter_groupe(
            group_name="B", rules=groupe_b,
            build_prompt_fn=prompt_groupe_b, check_verbatim=False,
            dry_run=args.dry_run, client=client,
        )

    log.info(f"Groupe C ({len(groupe_c)} regles) -> reste AMBIGU (revue humaine)")

    nouveaux_verdicts = {**resultats_a, **resultats_b}
    kb_validee, stats_update = mettre_a_jour_kb(kb_validee, nouveaux_verdicts)

    kb_validee.setdefault("metadata", {})["revalidation_s13"] = {
        "date":         datetime.now().isoformat(),
        "stats_groupes": {
            "A_erreurs_api":  len(groupe_a),
            "B_non_verbatim": len(groupe_b),
            "C_humain":       len(groupe_c),
        },
        "gains": stats_update,
    }

    if not args.dry_run:
        atomic_write(KB_VALIDEE_PATH, kb_validee)
        log.info("KB_VALIDEE.json mis a jour")
        nb_restants = generer_humain_md(kb_validee)
        generer_rapport(stats_update, nb_restants, kb_validee)
    else:
        log.info("[DRY RUN] KB_VALIDEE.json NON modifie")
        log.info("[DRY RUN] A_VERIFIER_HUMAIN.md NON regenere")
        nb_restants = sum(
            len(buckets.get("AMBIGU", []))
            for buckets in kb_validee.get("rules_by_status", {}).values()
        )

    log.info("")
    log.info("=" * 70)
    log.info("RESULTATS FINAUX")
    log.info("-" * 70)
    log.info(f"  VALIDE gagnes   : +{stats_update.get('VALIDE_gagne', 0)}")
    log.info(f"  INVALIDE gagnes : +{stats_update.get('INVALIDE_gagne', 0)}")
    log.info(f"  Restent AMBIGU  :  {stats_update.get('reste_AMBIGU', 0)}")
    if args.dry_run:
        log.info(f"  DRY_RUN         :  {stats_update.get('DRY_RUN', 0)}")
    log.info("-" * 70)

    totaux_finaux = {}
    for buckets in kb_validee.get("rules_by_status", {}).values():
        for status, rules in buckets.items():
            totaux_finaux[status] = totaux_finaux.get(status, 0) + len(rules)

    total_final = sum(totaux_finaux.values())
    for status in ["VALIDE", "INVALIDE", "AMBIGU", "DRY_RUN"]:
        nb = totaux_finaux.get(status, 0)
        if nb > 0:
            pct = round(nb / max(total_final, 1) * 100, 1)
            log.info(f"  {status:<15} : {nb:>4} ({pct}%)")
    log.info("-" * 70)
    log.info(f"  TOTAL           : {total_final}")
    log.info("=" * 70)
    log.info(f"  A_VERIFIER_HUMAIN.md : {nb_restants} cas a verifier manuellement")
    log.info("=" * 70)
    log.info("Termine.")


if __name__ == "__main__":
    main()
