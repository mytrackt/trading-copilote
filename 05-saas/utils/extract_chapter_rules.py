# extract_chapter_rules.py — Phase 0 reconstruction KB
# Extrait les 62 regles chapitres (sans source_video_id) et les sauvegarde.
#
# Usage (PowerShell depuis C:/trading-copilote) :
#   python 05-saas/utils/extract_chapter_rules.py
#
# Decisions : D-S39-1 (filtre source_video_id), D-S39-3 (BASE_DIR 3x dirname)

import os
import json
import sys
import time

# D-S39-3 : 3× dirname car ce script est dans 05-saas/utils/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

KB_FILE      = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE  = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")

EXPECTED_COUNT = 62  # D-S39-1 : 14 id_brique + 48 id/contenu/source_origine


def main():
    print("=" * 60)
    print("Phase 0 — Extraction règles chapitres (backup)")
    print(f"BASE_DIR  : {BASE_DIR}")
    print(f"KB_FILE   : {KB_FILE}")
    print(f"BACKUP    : {BACKUP_FILE}")
    print("=" * 60)

    # Vérifications préalables
    if not os.path.exists(KB_FILE):
        print(f"ERREUR : KB introuvable → {KB_FILE}")
        sys.exit(1)

    # Lecture KB
    print("\n[1/3] Lecture de la KB...")
    with open(KB_FILE, "r", encoding="utf-8") as f:
        kb = json.load(f)

    aggregated = kb.get("aggregated_rules", {})
    if not aggregated:
        print("ERREUR : aggregated_rules absent ou vide dans la KB.")
        sys.exit(1)

    # D-S39-1 : filtre = if "source_video_id" not in e
    # Les règles chapitres sont des dicts sans clé source_video_id.
    # Les règles vidéo normales ont source_video_id ou sont des strings.
    print("\n[2/3] Extraction des règles chapitres...")
    chapter_rules = {}
    total = 0

    for categorie, rules_list in aggregated.items():
        chapter_entries = []
        for e in rules_list:
            if isinstance(e, dict) and "source_video_id" not in e:
                chapter_entries.append(e)
                total += 1
        if chapter_entries:
            chapter_rules[categorie] = chapter_entries

    # Rapport
    print(f"\n  Règles chapitres extraites : {total}")
    for cat, entries in chapter_rules.items():
        print(f"    {cat:40s} : {len(entries)}")

    # Contrôle D-S39-1
    if total == EXPECTED_COUNT:
        print(f"\n  ✓ Contrôle OK : {total} règles (attendu {EXPECTED_COUNT})")
    else:
        print(f"\n  ⚠️  ATTENTION : obtenu {total}, attendu {EXPECTED_COUNT}")
        print("     Vérifier la KB avant de continuer.")
        # Ne pas bloquer — sauvegarder quand même ce qui existe
        response = input("  Continuer la sauvegarde malgré l'écart ? (oui/non) : ").strip().lower()
        if response != "oui":
            print("  Abandon. Aucun fichier écrit.")
            sys.exit(1)

    # Sauvegarde atomique (tempfile + os.replace — CLAUDE.md règle technique)
    print("\n[3/3] Sauvegarde atomique...")
    import tempfile

    tmp_path = BACKUP_FILE + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(chapter_rules, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, BACKUP_FILE)
        print(f"  ✓ Backup créé : {BACKUP_FILE}")
    except Exception as exc:
        print(f"  ERREUR sauvegarde : {exc}")
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        sys.exit(1)

    # Vérification lecture
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        verify = json.load(f)
    verify_total = sum(len(v) for v in verify.values())
    if verify_total != total:
        print(f"  ⚠️  Vérification échouée : {verify_total} relu vs {total} extrait")
        sys.exit(1)
    print(f"  ✓ Vérification lecture : {verify_total} règles relues avec succès")

    print("\n" + "=" * 60)
    print("Phase 0 terminée.")
    print(f"BACKUP : {BACKUP_FILE}")
    print(f"TOTAL  : {total} règles chapitres sauvegardées")
    if total == EXPECTED_COUNT:
        print("STATUT : ✓ 62/62 — Prêt pour Phase 1")
    else:
        print(f"STATUT : ⚠️  {total}/{EXPECTED_COUNT} — Vérifier avant Phase 1")
    print("=" * 60)


if __name__ == "__main__":
    main()
