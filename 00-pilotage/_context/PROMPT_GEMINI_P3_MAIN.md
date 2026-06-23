# PROMPT GEMINI — PHASE 3/3 : MAIN() + SCRIPT TEST + COMMIT
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code
# Prerequis : Phase 2 terminee, validee et confirmee par Abdelkrim

---

## OBJECTIF DE CETTE PHASE

1. Remplir le stub `main()` dans `gemini_transcriber.py`
2. Creer `gemini_test_3videos.py` (test sur 3 videos avant le batch complet)
3. Lint final + test 3 videos + commit

---

## ETAPE 1 — REMPLIR main() et generer_rapport()

⚠️ ORDRE OBLIGATOIRE DANS LE FICHIER :
Coller `generer_rapport()` EN PREMIER, puis `main()` EN SECOND.
En Python, `main()` appelle `generer_rapport()` — si `generer_rapport()`
est definie apres `main()` dans le fichier, cela reste valide a l'execution,
mais pour la lisibilite et eviter toute confusion, respecter cet ordre.

## REMPLIR generer_rapport() et main()

Ouvrir `C:\trading-copilote\05-saas\utils\gemini_transcriber.py`.
Remplacer le stub `main()` par le code ci-dessous.

```python
def main():
    """
    Boucle principale : transcrit toutes les videos MP4 de VIDEO_DIR.
    - Affiche l'estimation de cout avant de commencer (confirmation requise)
    - Saute les videos deja traitees (reprise possible apres interruption)
    - Ecriture atomique (tempfile + replace) : pas de fichier partiel
    - Rate limiting : 2s entre chaque video
    - Genere RAPPORT_QUALITE_GEMINI.md en fin de traitement
    """
    videos = sorted(VIDEO_DIR.glob("*.mp4"))
    if not videos:
        print(f"Aucun MP4 trouve dans {VIDEO_DIR}")
        print("Verifier que le dossier D:\\Belkhayate-Videos existe et contient des .mp4")
        sys.exit(1)

    # --- ESTIMATION COUT AVANT LANCEMENT ---
    cout_min = len(videos) * 0.02
    cout_max = len(videos) * 0.10
    duree_min = len(videos) * 3
    duree_max = len(videos) * 6

    print("=" * 60)
    print(f"  GEMINI TRANSCRIBER — TRADEX-AI")
    print("=" * 60)
    print(f"  Modele       : {MODEL_NAME}")
    print(f"  Videos       : {len(videos)} fichiers dans {VIDEO_DIR}")
    print(f"  Sortie       : {OUTPUT_DIR}")
    print(f"  Cout estime  : {cout_min:.2f}€ — {cout_max:.2f}€")
    print(f"  Duree estimee: {duree_min} — {duree_max} minutes")
    print()

    # Compter les videos deja traitees
    deja_faites = sum(
        1 for v in videos
        if (OUTPUT_DIR / f"{v.stem}_gemini.txt").exists()
    )
    if deja_faites > 0:
        print(f"  {deja_faites} video(s) deja traitees — seront sautees (SKIP)")
        print(f"  {len(videos) - deja_faites} video(s) restantes a traiter")
    print()

    confirmation = input("Confirmes-tu le lancement ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Annule. Lance python gemini_transcriber.py quand tu es pret.")
        sys.exit(0)
    print()

    # --- BOUCLE PRINCIPALE ---
    rapport = []
    nb_ok = 0
    nb_skip = 0
    nb_erreurs = 0
    debut_global = time.time()

    for i, video in enumerate(videos, 1):
        out_path = OUTPUT_DIR / f"{video.stem}_gemini.txt"

        # Skip si deja traite
        if out_path.exists():
            nb_skip += 1
            print(f"[{i:3d}/{len(videos)}] SKIP : {video.name}")
            continue

        print(f"[{i:3d}/{len(videos)}] {video.name}")
        debut_video = time.time()

        resultat = transcrire_video(video)

        duree_video = time.time() - debut_video

        if resultat.get("erreur"):
            nb_erreurs += 1
            print(f"  ERREUR : {resultat['erreur']}")
            rapport.append({
                "fichier": video.name,
                "statut": "ERREUR",
                "qualite": resultat.get("qualite", "?"),
                "live": resultat.get("live", False),
                "detail": resultat["erreur"][:120]
            })
        else:
            # Ecriture atomique : tempfile → replace (jamais de fichier partiel)
            tmp_path = Path(str(out_path) + ".tmp")
            tmp_path.write_text(resultat["transcript"], encoding="utf-8")
            tmp_path.replace(out_path)

            nb_ok += 1
            nb_balises_visuel = resultat["transcript"].count("[VISUEL:")
            nb_regles = resultat["transcript"].count("[REGLE:")
            print(
                f"  OK ({duree_video:.0f}s) — "
                f"{len(resultat['transcript'])} chars | "
                f"{nb_balises_visuel} [VISUEL] | {nb_regles} [REGLE]"
            )
            rapport.append({
                "fichier": video.name,
                "statut": "OK",
                "qualite": resultat["qualite"],
                "live": resultat["live"],
                "detail": f"{nb_balises_visuel} VISUEL, {nb_regles} REGLE"
            })

        # Rate limiting Gemini (evite erreurs 429)
        time.sleep(2)

    # --- RAPPORT QUALITE ---
    duree_totale = time.time() - debut_global
    generer_rapport(rapport, nb_ok, nb_skip, nb_erreurs, duree_totale, len(videos))

    print()
    print("=" * 60)
    print(f"  TERMINE")
    print(f"  OK: {nb_ok} | Skip: {nb_skip} | Erreurs: {nb_erreurs}")
    print(f"  Duree totale : {duree_totale / 60:.1f} minutes")
    print(f"  Rapport : {RAPPORT_PATH}")
    print("=" * 60)
    print()
    print("GARDE-FOUS — rappels de lecture des transcripts :")
    print("  - [QUALITE_VIDEO: FAIBLE_APPROX] → verifier manuellement les [VISUEL]")
    print("  - [TYPE: LIVE_TRADING] + [ECRAN_CHANGE_RAPIDE] → passage incomplet")
    print("  - Chiffre suivi de A_VERIFIER → ne jamais integrer en KB sans verif")
    print("  - [REGLE: ...] → passages les plus exploitables pour la KB")
    print("  - Descriptions relatives (haussier/baissier) → fiables")


def generer_rapport(rapport: list, nb_ok: int, nb_skip: int,
                    nb_erreurs: int, duree_totale: float, nb_total: int):
    """Genere RAPPORT_QUALITE_GEMINI.md apres le traitement."""
    lignes = [
        "# RAPPORT QUALITE TRANSCRIPTIONS GEMINI",
        f"",
        f"- Date : {time.strftime('%Y-%m-%d %H:%M')}",
        f"- Modele : {MODEL_NAME}",
        f"- Total : {nb_total} | OK : {nb_ok} | Skip : {nb_skip} | Erreurs : {nb_erreurs}",
        f"- Duree : {duree_totale / 60:.1f} minutes",
        "",
        "## Resultats par video",
        "",
        "| Fichier | Statut | Qualite | Live | Detail |",
        "|---------|--------|---------|------|--------|"
    ]
    for r in rapport:
        live_str = "OUI" if r.get("live") else "NON"
        lignes.append(
            f"| {r['fichier']} | {r['statut']} | {r.get('qualite','?')} "
            f"| {live_str} | {r.get('detail','')} |"
        )
    lignes += [
        "",
        "## Precautions de lecture",
        "",
        "- **QUALITE_VIDEO FAIBLE_APPROX** : verifier manuellement les descriptions visuelles",
        "- **TYPE LIVE_TRADING** : certaines descriptions peuvent etre incompletes",
        "- **Chiffre suivi de A_VERIFIER** : confirmer sur la video originale avant KB",
        "- **[REGLE: ...]** : passages les plus exploitables pour la KB TRADEX-AI",
        "- **Descriptions relatives** (haussier/baissier, au-dessus/en dessous) : fiables",
        "- **Chiffres exacts visuels** : interdits — utiliser les descriptions uniquement"
    ]
    RAPPORT_PATH.write_text("\n".join(lignes), encoding="utf-8")
```

---

## ETAPE 2 — CREER gemini_test_3videos.py

Creer `C:\trading-copilote\05-saas\utils\gemini_test_3videos.py` :

```python
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
```

---

## ETAPE 3 — VALIDATION FINALE

### Lint complet
```
python -m py_compile C:\trading-copilote\05-saas\utils\gemini_transcriber.py
python -m py_compile C:\trading-copilote\05-saas\utils\gemini_test_3videos.py
```
Les deux doivent passer sans erreur.

### Lancer le test 3 videos
```
python C:\trading-copilote\05-saas\utils\gemini_test_3videos.py
```

Attendre la fin (5-15 min selon les 3 videos choisies).
Afficher le resultat complet et les 30 premieres lignes de chaque transcript.

---

## ETAPE 4 — COMMIT (apres validation par Abdelkrim)

Attendre que Abdelkrim confirme que la qualite des 3 transcripts est satisfaisante.

Puis committer :
```
git status
```
Verifier que les fichiers listes sont bien les 3 attendus (pas plus).
```
git add 05-saas\utils\gemini_transcriber.py
git add 05-saas\utils\gemini_test_3videos.py
git add 03-transcriptions\README-SOURCES.md
```
Verifier le contenu du commit avant de valider :
```
git diff --cached --stat
```
Si le diff est correct :
```
git commit -m "feat(gemini): pipeline transcription multimodal audio-visuel Belkhayate"
git push origin main
```

---

## CHECKLIST PHASE 3

- [ ] `main()` et `generer_rapport()` implemente dans gemini_transcriber.py
- [ ] `gemini_test_3videos.py` cree
- [ ] Lint OK sur les 2 fichiers
- [ ] Test 3 videos lance et resultats affiches
- [ ] Au moins 1 video avec des balises [VISUEL:] et [REGLE:]
- [ ] Abdelkrim a valide la qualite des transcripts
- [ ] Commit + push confirme

---

## APRES LE COMMIT — TRAITEMENT COMPLET

Seulement apres validation des 3 transcripts de test :
```
python C:\trading-copilote\05-saas\utils\gemini_transcriber.py
```

Duree estimee : 6-14h pour 164 videos.
Laisser tourner la nuit. Le script reprend automatiquement si interrompu.
