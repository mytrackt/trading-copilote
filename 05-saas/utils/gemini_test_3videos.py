"""
Test Gemini Transcriber sur 3 videos.
A lancer AVANT le traitement complet pour valider la qualite.
Sortie dans : transcripts-gemini\test\
"""

import sys
import time
from pathlib import Path
import importlib.util

# Charger gemini_transcriber depuis son chemin absolu
spec = importlib.util.spec_from_file_location(
    "gemini_transcriber",
    r"C:\trading-copilote\05-saas\utils\gemini_transcriber.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TEST_OUTPUT = mod.OUTPUT_DIR / "test"
TEST_OUTPUT.mkdir(parents=True, exist_ok=True)

def main():
    videos = sorted(mod.VIDEO_DIR.glob("*.mp4"))
    if not videos:
        print(f"Aucun MP4 dans {mod.VIDEO_DIR}")
        sys.exit(1)

    # Prendre 3 videos differentes si possible
    # 1 courte, 1 moyenne, 1 avec "live" dans le nom si disponible
    selection = []
    for v in videos:
        if len(selection) == 0:
            selection.append(v)  # premiere video disponible
        elif len(selection) == 1 and v.stat().st_size > 200 * 1024 * 1024:
            selection.append(v)  # video plus lourde (> 200 Mo)
        elif len(selection) <= 2 and "live" in v.name.lower():
            selection.append(v)  # video live si existe
        if len(selection) >= 3:
            break

    # Completer si moins de 3 trouvees
    for v in videos:
        if v not in selection:
            selection.append(v)
        if len(selection) >= 3:
            break

    print("=" * 60)
    print(f"  TEST GEMINI — {len(selection)} videos selectionnees")
    print("=" * 60)
    for v in selection:
        taille = v.stat().st_size / 1024 / 1024
        print(f"  - {v.name} ({taille:.1f} Mo)")
    print()

    resultats = []

    for i, video in enumerate(selection, 1):
        print(f"\n[{i}/{len(selection)}] {video.name}")
        debut = time.time()

        resultat = mod.transcrire_video(video)
        duree = time.time() - debut

        if resultat.get("erreur"):
            print(f"  ERREUR : {resultat['erreur']}")
            resultats.append({"video": video.name, "ok": False, "erreur": resultat["erreur"]})
        else:
            out_path = TEST_OUTPUT / f"{video.stem}_gemini_TEST.txt"
            out_path.write_text(resultat["transcript"], encoding="utf-8")

            t = resultat["transcript"]
            nb_visuel = t.count("[VISUEL:")
            nb_regle = t.count("[REGLE:")
            nb_flags = t.count("A_VERIFIER")
            nb_lignes = len(t.split("\n"))

            print(f"  OK ({duree:.0f}s)")
            print(f"  Lignes        : {nb_lignes}")
            print(f"  Balises VISUEL: {nb_visuel}")
            print(f"  Balises REGLE : {nb_regle}")
            print(f"  Chiffres flagg: {nb_flags}")
            print(f"  Qualite       : {resultat['qualite']}")
            print(f"  Live          : {resultat['live']}")
            print(f"\n  --- 30 premieres lignes ---")
            for j, ligne in enumerate(t.split("\n")[:30], 1):
                print(f"  {j:3d} | {ligne}")

            resultats.append({
                "video": video.name, "ok": True,
                "nb_visuel": nb_visuel, "nb_regle": nb_regle
            })

    print("\n" + "=" * 60)
    print("  BILAN DU TEST")
    print("=" * 60)
    ok = sum(1 for r in resultats if r["ok"])
    print(f"  Reussis : {ok}/{len(resultats)}")
    for r in resultats:
        if r["ok"]:
            print(f"  OK  : {r['video']} — {r['nb_visuel']} VISUEL, {r['nb_regle']} REGLE")
        else:
            print(f"  ERR : {r['video']} — {r['erreur'][:80]}")
    print()
    print(f"  Transcripts de test sauvegardes dans : {TEST_OUTPUT}")
    print()
    print("  ETAPE SUIVANTE : lire les transcripts de test et valider la qualite.")
    print("  Si OK → lancer le traitement complet :")
    print("    python C:\\trading-copilote\\05-saas\\utils\\gemini_transcriber.py")

if __name__ == "__main__":
    main()
