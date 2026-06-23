# PROMPT GEMINI — PHASE 2/3 : FONCTIONS CORE (UPLOAD + API)
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code
# Prerequis : Phase 1 terminee et validee (python -m py_compile OK)

---

## OBJECTIF DE CETTE PHASE

Remplir les 2 stubs complexes dans `05-saas\utils\gemini_transcriber.py` :
- `construire_prompt()` : prompt Gemini adapte au type de video
- `transcrire_video()` : upload + attente PROCESSING + appel API + retry + cleanup

La validation de cette phase = lint OK + test sur 1 seule video.

---

## REMPLACEMENT DES STUBS

Ouvrir `C:\trading-copilote\05-saas\utils\gemini_transcriber.py`.
Remplacer le stub `construire_prompt()` par le code ci-dessous.
Remplacer le stub `transcrire_video()` par le code ci-dessous.
Ne pas toucher aux autres fonctions (deja implementees en Phase 1).

---

### FONCTION construire_prompt()

```python
def construire_prompt(nom_fichier: str, est_live_video: bool) -> str:
    """
    Construit le prompt Gemini adapte au type de video.
    Les videos live ont une instruction supplementaire pour les moments rapides.
    """
    instruction_live = ""
    if est_live_video:
        instruction_live = (
            "\nIMPORTANT - VIDEO LIVE TRADING : L'ecran peut changer tres rapidement. "
            "Si tu ne peux pas decrire precisement ce qui est affiche a un instant "
            "donne, ecris [ECRAN_CHANGE_RAPIDE] et continue avec la transcription "
            "audio. Ne jamais inventer une description visuelle si tu n'es pas "
            "certain de ce que tu vois.\n"
        )

    return f"""Tu es un transcripteur expert de videos de trading financier en francais.
Transcris cette video de Mustapha Belkhayate en integrant a la fois
l'audio ET le contenu visuel de l'ecran.

REGLE FONDAMENTALE :
Belkhayate enseigne en montrant son ecran (NinjaTrader, TradingView, etc.).
Quand il dit "vous voyez ici", "regardez la", "ici on a" etc., il fait
reference a quelque chose de visible sur son ecran. Tu dois decrire ce
que tu vois sur l'ecran a ce moment precis AVANT de retranscrire ses mots.

FORMAT OBLIGATOIRE :
- Pour chaque passage avec reference visuelle, utilise :
  [VISUEL: description precise de ce que tu vois a l'ecran]
  puis continue avec la transcription audio
- Pour les passages sans reference visuelle :
  transcris simplement ce que Belkhayate dit
- Quand Belkhayate enonce une regle claire et autonome, mets-la en evidence :
  [REGLE: formulation complete de la regle]

DESCRIPTIONS VISUELLES — CE QU'IL FAUT DECRIRE :
- Quel indicateur est visible ? (Belkhayate Trend, COG/Centre de Gravite,
  VWAP, Pivots, Volume Profile, Delta, Footprint)
- Quelle couleur a l'indicateur ? (vert = haussier, rouge = baissier,
  bleu/blanc = neutre)
- Le prix est-il au-dessus ou en dessous du COG / VWAP / moyenne mobile ?
- Y a-t-il une acceleration de volume visible ?
- Quelle est la tendance generale visible sur le graphique ?
- Quel marche est affiche ? (Or GC, Ble ZW, Petrole CL, Cuivre HG,
  SP500 ES, Dollar DX, VIX VX)
- Quel timeframe est affiche ? (5min, 15min, 1h, daily, range bars)

POUR LES PRIX ET NIVEAUX PRECIS — REGLE STRICTE :
NE JAMAIS donner un prix ou niveau chiffre exact lu a l'ecran.
Tu peux te tromper sur les decimales et cela serait dangereux
si ce chiffre etait utilise dans une decision de trading.
A la place, decris UNIQUEMENT en termes relatifs :
  AUTORISE  : "le prix est nettement au-dessus du Centre de Gravite"
  AUTORISE  : "le Centre de Gravite est en zone haute du graphique"
  AUTORISE  : "grand volume visible, bien superieur a la moyenne"
  INTERDIT  : "le COG est a 1852" ou "le prix est a 2340.5"
Exception unique : si Belkhayate PRONONCE lui-meme le chiffre verbalement
dans l'audio → tu peux le transcrire (c'est de l'audio, pas du visuel).
{instruction_live}
Exemple de sortie attendue :
  [VISUEL: Graphique Or GC 5min sur NinjaTrader. Belkhayate Trend rouge.
  Prix sous la moyenne mobile. Volume faible.]
  "Vous voyez ici on est en tendance baissiere sur l'or."
  [REGLE: Quand Belkhayate Trend est rouge et le prix est sous la MM,
  on cherche uniquement des signaux de vente.]
  "Donc dans cette configuration on ne cherche pas a acheter."

Transcris maintenant la video complete. Sois exhaustif.
"""
```

---

### FONCTION transcrire_video()

Structure correcte avec try/finally (bug corrige par rapport au prompt original).
Le `finally` garantit que le fichier est toujours supprime de Gemini meme en cas d'erreur.

```python
def transcrire_video(video_path: Path) -> dict:
    """
    Transcrit une video avec Gemini 1.5 Flash.
    Retourne un dict :
      Success : {"transcript": str, "qualite": str, "live": bool, "erreur": None}
      Echec   : {"erreur": str, "qualite": str, "live": bool}

    Garde-fous integres :
    - Timeout 300s sur la boucle PROCESSING (evite boucle infinie)
    - Retry 3x avec backoff exponentiel sur erreurs API
    - Pause 60s si erreur 429 (quota depasse)
    - max_output_tokens = 32768 (videos longues jusqu'a 2h)
    - Suppression du fichier Gemini dans finally (evite les fuites)
    """
    nom = video_path.name
    qualite = detecter_qualite(video_path)
    live = est_live(nom)
    video_file = None  # initialiser pour le bloc finally

    print(f"  Qualite estimee : {qualite}")
    print(f"  Type live       : {'OUI' if live else 'NON'}")

    try:
        # --- UPLOAD ---
        print(f"  Upload en cours vers Gemini Files API...")
        video_file = genai.upload_file(path=str(video_path), mime_type="video/mp4")

        # --- ATTENTE PROCESSING avec timeout ---
        debut_attente = time.time()
        while video_file.state.name == "PROCESSING":
            if time.time() - debut_attente > MAX_PROCESSING_WAIT_SECONDS:
                return {
                    "erreur": (
                        f"Timeout : fichier bloque en PROCESSING "
                        f"apres {MAX_PROCESSING_WAIT_SECONDS}s"
                    ),
                    "qualite": qualite,
                    "live": live
                }
            time.sleep(5)
            video_file = genai.get_file(video_file.name)

        if video_file.state.name == "FAILED":
            return {
                "erreur": "Upload Gemini echoue (state=FAILED)",
                "qualite": qualite,
                "live": live
            }

        print(f"  Upload OK — transcription en cours...")

        # --- APPEL API avec retry ---
        prompt = construire_prompt(nom, live)
        transcript_brut = None

        for tentative in range(MAX_RETRIES):
            try:
                response = model.generate_content(
                    [video_file, prompt],
                    generation_config={
                        "temperature": 0.1,         # fidelite maximale
                        "max_output_tokens": 32768  # suffisant pour videos 2h
                    }
                )
                transcript_brut = response.text
                break  # succes → sortir du retry

            except Exception as api_err:
                err_str = str(api_err)
                if tentative < MAX_RETRIES - 1:
                    # Pause longue si quota depasse
                    attente = (
                        60 if ("429" in err_str or "quota" in err_str.lower())
                        else RETRY_BACKOFF[tentative]
                    )
                    print(
                        f"  Erreur API (tentative {tentative + 1}/{MAX_RETRIES}) : "
                        f"{err_str[:120]}"
                    )
                    print(f"  Prochaine tentative dans {attente}s...")
                    time.sleep(attente)
                else:
                    return {
                        "erreur": f"Echec apres {MAX_RETRIES} tentatives : {err_str[:200]}",
                        "qualite": qualite,
                        "live": live
                    }

        if transcript_brut is None:
            return {
                "erreur": "Boucle retry terminee sans transcript (cas inattendu)",
                "qualite": qualite,
                "live": live
            }

        # --- POST-TRAITEMENT ---
        transcript_final = flaguer_chiffres_visuels(transcript_brut)

        # Construire l'entete de metadonnees
        entete_lignes = [
            f"[QUALITE_VIDEO: {qualite}]",
            f"[TYPE: {'LIVE_TRADING' if live else 'COURS_PEDAGOGIQUE'}]",
            f"[MODELE: {MODEL_NAME}]",
            f"[DATE_TRANSCRIPTION: {time.strftime('%Y-%m-%d')}]",
            f"[SOURCE: {nom}]",
            "---"
        ]
        if "FAIBLE" in qualite:
            entete_lignes.append(
                "[ATTENTION: qualite video faible — descriptions visuelles a verifier manuellement]"
            )
            entete_lignes.append("---")
        if live:
            entete_lignes.append(
                "[ATTENTION: video live — descriptions visuelles peuvent etre incompletes "
                "sur les moments de changement rapide d'ecran]"
            )
            entete_lignes.append("---")

        entete = "\n".join(entete_lignes) + "\n"

        return {
            "transcript": entete + transcript_final,
            "qualite": qualite,
            "live": live,
            "erreur": None
        }

    except Exception as e:
        return {
            "erreur": f"Erreur inattendue : {str(e)[:300]}",
            "qualite": qualite,
            "live": live
        }

    finally:
        # Toujours supprimer le fichier de Gemini (evite accumulation et frais)
        if video_file is not None:
            try:
                genai.delete_file(video_file.name)
            except Exception:
                pass  # echec de suppression non bloquant
```

---

## VALIDATION PHASE 2

### Etape 1 — Lint
```
python -m py_compile C:\trading-copilote\05-saas\utils\gemini_transcriber.py
```
Aucune sortie = OK.

### Etape 2 — Test sur 1 video

Creer le dossier _temp s'il n'existe pas :
```
mkdir C:\trading-copilote\_temp
```
(sans erreur si deja existant)

Creer le script `C:\trading-copilote\_temp\test_gemini_1video.py` :

```python
"""Test rapide sur 1 video — a supprimer apres validation."""
import sys
import importlib.util
from pathlib import Path

# Charger gemini_transcriber depuis chemin absolu (API stdlib correcte)
spec = importlib.util.spec_from_file_location(
    "gemini_transcriber",
    r"C:\trading-copilote\05-saas\utils\gemini_transcriber.py"
)
mod = importlib.util.module_from_spec(spec)   # CORRECT — pas load_from_spec
spec.loader.exec_module(mod)                   # execute le module

# Prendre la premiere video disponible
videos = sorted(Path(r"D:\Belkhayate-Videos").glob("*.mp4"))
if not videos:
    print("Aucune video trouvee dans D:\\Belkhayate-Videos")
    sys.exit(1)

video = videos[0]
print(f"Test sur : {video.name}")
print(f"Taille   : {video.stat().st_size / 1024 / 1024:.1f} Mo")
print()

resultat = mod.transcrire_video(video)

if resultat.get("erreur"):
    print(f"ERREUR : {resultat['erreur']}")
    sys.exit(1)

t = resultat["transcript"]
print(f"SUCCES — {len(t)} caracteres transcrits")
print()
print("=== DEBUT TRANSCRIPT (50 premieres lignes) ===")
for i, ligne in enumerate(t.split('\n')[:50], 1):
    print(f"{i:3d} | {ligne}")
print()
print("=== STATISTIQUES ===")
print(f"Balises [VISUEL:] : {t.count('[VISUEL:')}")
print(f"Balises [REGLE:]  : {t.count('[REGLE:')}")
print(f"Chiffres flaggues : {t.count('A_VERIFIER')}")
print(f"Qualite estimee   : {resultat['qualite']}")
print(f"Type live         : {resultat['live']}")
```

Lint du script de test avant de le lancer :
```
python -m py_compile C:\trading-copilote\_temp\test_gemini_1video.py
```

Lancer le test :
```
python C:\trading-copilote\_temp\test_gemini_1video.py
```

Resultat attendu :
- `SUCCES — X caracteres transcrits`
- Au moins quelques balises `[VISUEL:]` ou `[REGLE:]` dans les 50 premieres lignes
- Aucune erreur Python

---

## CHECKLIST PHASE 2

- [ ] Stub `construire_prompt()` remplace par le code complet
- [ ] Stub `transcrire_video()` remplace par le code complet avec try/finally
- [ ] `python -m py_compile` passe sans erreur
- [ ] Test sur 1 video : "SUCCES" affiche
- [ ] Les balises [VISUEL:] et/ou [REGLE:] sont presentes dans le transcript

Afficher les resultats du test et attendre la validation.
NE PAS passer a la Phase 3 sans confirmation de l'utilisateur.
NE PAS committer encore.
