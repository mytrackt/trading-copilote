# inject_chapter_rules.py -- Phase 8 reconstruction KB (DERNIERE ECRITURE)
# Reinsere les 62 regles chapitres dans aggregated_rules apres reconstruction.
# A executer APRES transcript_processor_gemini.py -- JAMAIS avant.
#
# D-S39-2 : rebuild_aggregated() efface les chapitres apres chaque video.
#            Ce script est le filet permanent contre cette fragilite.
# D-S39-3 : BASE_DIR 3x dirname car 05-saas/utils/

import os
import json
import sys
from pathlib import Path

# BASE_DIR = 3x dirname car 05-saas/utils/ (D-S39-3)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

KB_FILE     = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")

EXPECTED_COUNT = 62

CATEGORIES = [
    "saisonnalite", "correlations", "timing",
    "indicateurs_tendance", "indicateurs_momentum",
    "gestion_risque_entree", "gestion_position_active",
    "structure_marche", "macro_evenements", "volume_liquidite", "psychologie",
]


def main():
    print("=" * 60)
    print("Phase 8 -- Injection regles chapitres (derniere ecriture KB)")
    print("BASE_DIR : " + str(BASE_DIR))
    print("KB_FILE  : " + str(KB_FILE))
    print("BACKUP   : " + str(BACKUP_FILE))
    print("=" * 60)

    # Verifications
    for path, label in [(KB_FILE, "KB_FILE"), (BACKUP_FILE, "BACKUP_FILE")]:
        if not os.path.exists(path):
            print("ERREUR : " + label + " introuvable : " + path)
            sys.exit(1)

    # Charger les deux fichiers
    print("\n[1/4] Lecture des fichiers...")
    with open(KB_FILE, "r", encoding="utf-8") as f:
        kb = json.load(f)
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        chapter_rules = json.load(f)

    total_backup = sum(len(v) for v in chapter_rules.values())
    print("  Regles chapitres dans backup : " + str(total_backup))

    if total_backup != EXPECTED_COUNT:
        print("  ATTENTION : attendu " + str(EXPECTED_COUNT) + ", obtenu " + str(total_backup))
        r = input("  Continuer quand meme ? (oui/non) : ").strip().lower()
        if r != "oui":
            print("  Abandon.")
            sys.exit(1)

    # Etat avant injection
    aggregated = kb.get("aggregated_rules", {})
    regles_avant = sum(len(aggregated.get(cat, [])) for cat in CATEGORIES)
    print("\n[2/4] Etat KB avant injection...")
    print("  Regles aggregated avant : " + str(regles_avant))

    # Detecter chapitres deja presents (eviter doublons)
    chapitres_existants = 0
    for cat in CATEGORIES:
        for e in aggregated.get(cat, []):
            if isinstance(e, dict) and "source_video_id" not in e:
                chapitres_existants += 1
    print("  Chapitres deja presents : " + str(chapitres_existants))

    if chapitres_existants > 0:
        print("  ATTENTION : des regles chapitres existent deja -- injection dupliquera.")
        r = input("  Continuer quand meme ? (oui/non) : ").strip().lower()
        if r != "oui":
            print("  Abandon.")
            sys.exit(1)

    # Injection
    print("\n[3/4] Injection de " + str(total_backup) + " regles chapitres...")
    if "aggregated_rules" not in kb:
        kb["aggregated_rules"] = {cat: [] for cat in CATEGORIES}

    injected = 0
    for cat, rules_list in chapter_rules.items():
        if cat not in kb["aggregated_rules"]:
            kb["aggregated_rules"][cat] = []
        for rule in rules_list:
            kb["aggregated_rules"][cat].append(rule)
            injected += 1
        if rules_list:
            print("  " + cat.ljust(40) + " +" + str(len(rules_list)))

    regles_apres = sum(
        len(kb["aggregated_rules"].get(cat, [])) for cat in CATEGORIES
    )

    # Sauvegarde atomique (tempfile + os.replace -- CLAUDE.md)
    print("\n[4/4] Sauvegarde atomique...")
    tmp_path = KB_FILE + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(kb, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, KB_FILE)
        print("  OK KB sauvegardee : " + KB_FILE)
    except Exception as exc:
        print("  ERREUR sauvegarde : " + str(exc))
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        sys.exit(1)

    # Verification lecture
    with open(KB_FILE, "r", encoding="utf-8") as f:
        verify = json.load(f)
    verify_total = sum(
        len(verify.get("aggregated_rules", {}).get(cat, [])) for cat in CATEGORIES
    )

    print("\n" + "=" * 60)
    print("Phase 8 terminee.")
    print("Regles avant injection     : " + str(regles_avant))
    print("Regles chapitres injectees : " + str(injected))
    print("Regles apres injection     : " + str(regles_apres))
    print("Verification lecture       : " + str(verify_total))

    if verify_total == regles_apres:
        print("STATUT : OK injection validee")
    else:
        print("STATUT : ATTENTION ecart -- verifier manuellement")

    print("\nETAPE SUIVANTE : tests 69/69 + commit")
    print("  cd C:/trading-copilote")
    print("  python -m pytest 05-saas/engine/test_claude_brain.py ...")
    print("=" * 60)


if __name__ == "__main__":
    main()
