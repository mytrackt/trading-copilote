# PROMPT CLAUDE CODE — PIPELINE GEMINI MULTIMODAL BELKHAYATE
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code
# Prerequis : cle API Gemini dans le fichier .env (GEMINI_API_KEY=...)

---

Tu vas construire un pipeline Python complet qui transcrit les videos
Belkhayate avec Gemini 2.0 Flash (audio + visuel simultanes).
Le resultat remplace les transcriptions Whisper actuelles en capturant
a la fois ce que Belkhayate DIT et ce qu'il MONTRE a l'ecran.

---

## CONTEXTE PROJET

Videos source : D:\Belkhayate-Videos\ (MP4 locaux, 164 fichiers)
Sortie        : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini\
Log qualite   : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\RAPPORT_QUALITE_GEMINI.md
KB cible      : C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json (NE PAS MODIFIER)

---

## LIMITES CONNUES DE GEMINI — PRECAUTIONS OBLIGATOIRES

Ces limites doivent etre codees dans le pipeline sous forme de garde-fous.
Ne jamais les ignorer. Ne jamais les contourner.

### LIMITE 1 — Qualite video
Gemini lit l'ecran. Si la video est floue, compressee ou de basse resolution,
sa description visuelle sera approximative ou fausse.

Garde-fou : mesurer la taille du fichier MP4.
  < 50 Mo pour une video > 20 min → probablement basse qualite → marquer [QUALITE_VIDEO_FAIBLE]
  > 500 Mo → bonne qualite probable → OK

Action : dans le transcript genere, ajouter en tete :
  [QUALITE_VIDEO: FAIBLE | MOYENNE | BONNE]
Les descriptions visuelles d'un fichier FAIBLE sont a verifier manuellement.

### LIMITE 2 — Mouvements rapides (sessions live)
Les sessions de trading en direct changent d'ecran toutes les secondes.
Gemini peut rater des moments cles ou confondre deux signaux differents.

Garde-fou : detecter les videos "live" par leur titre.
  Si le titre contient : LIVE, live, Live, trading live, session live, 5 Days Challenge
  → ajouter flag [TYPE: LIVE_TRADING] en tete du transcript
  → ajouter un avertissement : [ATTENTION: video live — descriptions visuelles
    peuvent etre incompletes sur les moments de changement rapide d'ecran]

Action dans le prompt Gemini pour ces videos :
  Ajouter l'instruction : "Cette video est un live trading.
  Si l'ecran change trop rapidement pour etre decrit precisement,
  ecris [ECRAN_CHANGE_RAPIDE] et continue avec l'audio."

### LIMITE 3 — Prix exacts lus a l'ecran
Gemini peut lire un prix affiché a l'ecran mais se tromper sur les decimales
ou les chiffres precis (ex: lire 1852 au lieu de 1852.5, ou 450 au lieu de 4500).

Garde-fou : tout chiffre specifique lu a l'ecran (prix, niveau, ratio)
doit etre marque avec un flag de verification.

Detection : si Gemini decrit un prix ou niveau precis dans une description visuelle
(pattern : [VISUEL: prix X, niveau Y, ratio Z])
→ ajouter automatiquement le suffixe ⚠️_A_VERIFIER apres chaque chiffre

Exemple de sortie attendue :
  [VISUEL: COG a 1852⚠️_A_VERIFIER, prix actuel 1848⚠️_A_VERIFIER,
  Belkhayate Trend vert] "Vous voyez ici le prix est sous le centre de
  gravite donc on attend qu'il remonte avant d'acheter."

Ces chiffres marques ne doivent JAMAIS etre integres dans la KB sans
verification manuelle par Abdelkrim sur la video originale.

---

## PHASE 1 — INSTALLATION ET CONFIGURATION

### Fichier : 05-saas\utils\gemini_transcriber.py

Creer ce fichier. Verifier d'abord s'il existe deja.

```python
"""
Gemini Multimodal Transcriber — TRADEX-AI
Transcription audio + visuel des videos Belkhayate via Gemini 1.5 Flash.
Audit v2.2 applique — corrections bloquantes integrees.
"""

import os
import sys
import time
import json
import re
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv  # CORRECTION 1 : charger le .env

load_dotenv(r"C:\trading-copilote\.env")  # chemin absolu obligatoire

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY manquant dans C:\\trading-copilote\\.env")

VIDEO_DIR    = Path(r"D:\Belkhayate-Videos")
OUTPUT_DIR   = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini")
RAPPORT_PATH = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\RAPPORT_QUALITE_GEMINI.md")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

genai.configure(api_key=GEMINI_API_KEY)
# CORRECTION 2 : utiliser gemini-1.5-flash (stable, non experimental)
model = genai.GenerativeModel("gemini-1.5-flash")

# CORRECTION 3 : timeout boucle processing
MAX_PROCESSING_WAIT_SECONDS = 300  # 5 minutes max

# CORRECTION 4 : retry sur erreurs API
MAX_RETRIES = 3
RETRY_BACKOFF = [10, 30, 60]  # secondes entre chaque tentative

# --- Seuils qualite video ---
SEUIL_FAIBLE_MO_PAR_MIN = 2.5  # < 2.5 Mo/min = qualite faible

# --- Mots-cles detection live ---
KEYWORDS_LIVE = ["live", "LIVE", "Live", "5 days challenge", "5 Days", "session live"]

def detecter_qualite(video_path: Path) -> str:
    """
    Evalue la qualite probable de la video.
    CORRECTION 9 : la taille seule est un proxy approximatif.
    Un fichier H.265 de 15 Mo peut etre en HD. Marquer toujours APPROXIMATIF.
    """
    taille_mo = video_path.stat().st_size / (1024 * 1024)
    if taille_mo < 30:
        return "FAIBLE_APPROX"   # A verifier manuellement
    elif taille_mo < 150:
        return "MOYENNE_APPROX"
    else:
        return "BONNE_APPROX"

def est_live(nom_fichier: str) -> bool:
    """Detecte si la video est un live trading."""
    return any(kw.lower() in nom_fichier.lower() for kw in KEYWORDS_LIVE)

def flaguer_chiffres_visuels(texte: str) -> str:
    """
    Ajoute le flag A_VERIFIER apres chaque chiffre dans un bloc [VISUEL: ...].
    CORRECTION 6 : regex insensible a la casse + robuste multiligne.
    """
    def remplacer_chiffres(match):
        bloc = match.group(0)
        return re.sub(r'\b(\d+[\.,]?\d*)\b', r'\1⚠️_A_VERIFIER', bloc)

    # CORRECTION : re.IGNORECASE pour capter [Visuel:] [VISUEL:] [visuel:]
    return re.sub(r'\[VISUEL:.*?\]', remplacer_chiffres, texte,
                  flags=re.DOTALL | re.IGNORECASE)

def construire_prompt(nom_fichier: str, est_live_video: bool) -> str:
    """Construit le prompt Gemini adapte au type de video."""

    instruction_live = ""
    if est_live_video:
        instruction_live = """
IMPORTANT - VIDEO LIVE TRADING : Cette video est une session de trading en direct.
L'ecran peut changer tres rapidement. Si tu ne peux pas decrire precisement
ce qui est a l'ecran a un instant donne, ecris [ECRAN_CHANGE_RAPIDE] et
continue avec la transcription audio. Ne jamais inventer une description
visuelle si tu n'es pas certain de ce que tu vois.
"""

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

DESCRIPTIONS VISUELLES — CE QU'IL FAUT DECRIRE :
- Quel indicateur est visible ? (Belkhayate Trend, COG/Centre de Gravite, VWAP, Pivots, Volume)
- Quelle couleur a l'indicateur ? (vert = haussier, rouge = baissier, bleu/blanc = neutre)
- Le prix est-il au-dessus ou en dessous du COG / VWAP / moyenne mobile ?
- Y a-t-il une acceleration de volume visible ?
- Quelle est la tendance generale visible sur le graphique ?
- Quel marche est affiche ? (Or GC, Ble ZW, Petrole CL, Nasdaq, etc.)
- Quel timeframe est affiche ? (5min, 15min, 1h, daily, range bars)

POUR LES PRIX ET NIVEAUX PRECIS — REGLE STRICTE :
NE JAMAIS donner un prix ou niveau chiffre exact lu a l'ecran.
Tu peux te tromper sur les decimales et cela serait dangereux
si ce chiffre etait utilise dans une decision de trading.
A la place, decris UNIQUEMENT en termes relatifs :
  BON   : "le prix est nettement au-dessus du Centre de Gravite"
  BON   : "le Centre de Gravite est en zone haute du graphique"
  BON   : "grand volume visible, bien superieur a la moyenne"
  INTERDIT : "le COG est a 1852" ou "le prix est a 2340.5"
Exception unique : si Belkhayate PRONONCE lui-meme le chiffre verbalement
dans l'audio → tu peux le transcrire (c'est de l'audio, pas du visuel).
{instruction_live}
REGLES A EXTRAIRE EN PRIORITE :
Quand Belkhayate enonce une regle claire (sans reference visuelle obligatoire),
mets-la en evidence avec :
  [REGLE: formulation de la regle]

Exemple de sortie attendue :
  [VISUEL: Graphique Or GC 5min sur NinjaTrader. Belkhayate Trend rouge.
  Prix sous la moyenne mobile 209. Volume faible.]
  "Vous voyez ici on est en tendance baissiere sur l'or."
  [REGLE: Quand Belkhayate Trend est rouge et le prix est sous la MM209,
  on cherche uniquement des signaux de vente.]
  "Donc dans cette configuration on ne cherche pas a acheter."

Transcris maintenant la video complete. Sois exhaustif.
"""

def transcrire_video(video_path: Path) -> dict:
    """Transcrit une video avec Gemini. Retourne dict avec transcript et metadata."""
    nom = video_path.name
    qualite = detecter_qualite(video_path)
    live = est_live(nom)

    print(f"  Qualite estimee : {qualite}")
    print(f"  Type live       : {'OUI' if live else 'NON'}")

    # Upload vers Gemini Files API
    print(f"  Upload en cours...")
    video_file = genai.upload_file(path=str(video_path), mime_type="video/mp4")

    # CORRECTION 3 : attente avec timeout pour eviter boucle infinie
    debut_attente = time.time()
    while video_file.state.name == "PROCESSING":
        if time.time() - debut_attente > MAX_PROCESSING_WAIT_SECONDS:
            return {"erreur": f"Timeout : fichier bloque en PROCESSING apres {MAX_PROCESSING_WAIT_SECONDS}s",
                    "qualite": qualite, "live": live}
        time.sleep(5)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        return {"erreur": "Upload Gemini echoue", "qualite": qualite}

    print(f"  Transcription en cours...")
    prompt = construire_prompt(nom, live)

    # CORRECTION 4+5 : max_output_tokens augmente + retry sur erreur
    for tentative in range(MAX_RETRIES):
        try:
            response = model.generate_content(
                [video_file, prompt],
                generation_config={
                    "temperature": 0.1,      # Bas pour maximiser fidelite
                    "max_output_tokens": 32768,  # CORRECTION : 8192 insuffisant pour videos longues
                }
            )
            transcript_brut = response.text
            break  # succes → sortir de la boucle retry

        except Exception as api_err:
            err_str = str(api_err)
            if tentative < MAX_RETRIES - 1:
                attente = RETRY_BACKOFF[tentative]
                # CORRECTION 10 : pause longue si quota depasse (429)
                if "429" in err_str or "quota" in err_str.lower():
                    attente = 60
                print(f"  Erreur API (tentative {tentative+1}/{MAX_RETRIES}) : {err_str}")
                print(f"  Nouvelle tentative dans {attente}s...")
                time.sleep(attente)
            else:
                return {"erreur": f"Echec apres {MAX_RETRIES} tentatives : {err_str}",
                        "qualite": qualite, "live": live}
    else:
        return {"erreur": "Boucle retry epuisee sans succes", "qualite": qualite, "live": live}

        # Appliquer le flag sur les chiffres visuels
        transcript_final = flaguer_chiffres_visuels(transcript_brut)

        # Ajouter les metadonnees en tete
        entete = f"""[QUALITE_VIDEO: {qualite}]
[TYPE: {'LIVE_TRADING' if live else 'COURS_PEDAGOGIQUE'}]
[MODELE: gemini-2.0-flash-exp]
[DATE_TRANSCRIPTION: {time.strftime('%Y-%m-%d')}]
[SOURCE: {nom}]
---
"""
        if qualite == "FAIBLE":
            entete += "[ATTENTION: qualite video faible — descriptions visuelles a verifier manuellement]\n---\n"
        if live:
            entete += "[ATTENTION: video live — descriptions visuelles peuvent etre incompletes sur moments rapides]\n---\n"

        return {
            "transcript": entete + transcript_final,
            "qualite": qualite,
            "live": live,
            "erreur": None
        }

    except Exception as e:
        return {"erreur": str(e), "qualite": qualite, "live": live}

    finally:
        # Supprimer le fichier de Gemini apres transcription
        try:
            genai.delete_file(video_file.name)
        except:
            pass

def main():
    videos = sorted(VIDEO_DIR.glob("*.mp4"))
    if not videos:
        print(f"Aucun MP4 trouve dans {VIDEO_DIR}")
        sys.exit(1)

    # CORRECTION 7 : estimation cout avant lancement
    cout_min = len(videos) * 0.02
    cout_max = len(videos) * 0.10
    print(f"=== GEMINI TRANSCRIBER — {len(videos)} videos ===")
    print(f"Modele       : gemini-1.5-flash (stable)")
    print(f"Sortie       : {OUTPUT_DIR}")
    print(f"Cout estime  : {cout_min:.2f}€ — {cout_max:.2f}€ selon duree des videos")
    print(f"Duree estimee: {len(videos) * 3} — {len(videos) * 6} minutes")
    print()
    confirmation = input("Confirmes-tu le lancement ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Annule.")
        sys.exit(0)
    print()

    rapport = []
    ok = 0
    skip = 0
    erreurs = 0

    for i, video in enumerate(videos, 1):
        stem = video.stem
        out_path = OUTPUT_DIR / f"{stem}_gemini.txt"

        if out_path.exists():
            skip += 1
            print(f"[{i}/{len(videos)}] SKIP (deja transcrit) : {video.name}")
            continue

        print(f"[{i}/{len(videos)}] {video.name}")

        resultat = transcrire_video(video)

        if resultat.get("erreur"):
            erreurs += 1
            print(f"  ERREUR : {resultat['erreur']}")
            rapport.append({
                "fichier": video.name,
                "statut": "ERREUR",
                "detail": resultat["erreur"],
                "qualite": resultat.get("qualite", "?"),
                "live": resultat.get("live", False)
            })
        else:
            # Ecriture atomique
            import tempfile
            tmp = Path(str(out_path) + ".tmp")
            tmp.write_text(resultat["transcript"], encoding="utf-8")
            tmp.replace(out_path)
            ok += 1
            print(f"  OK → {out_path.name}")
            rapport.append({
                "fichier": video.name,
                "statut": "OK",
                "qualite": resultat["qualite"],
                "live": resultat["live"],
                "detail": ""
            })

        # Rate limiting — Gemini Flash a des limites de requetes
        time.sleep(2)

    # Generer rapport qualite
    lines = [
        "# RAPPORT QUALITE TRANSCRIPTIONS GEMINI",
        f"Date : {time.strftime('%Y-%m-%d')}",
        f"Total : {len(videos)} | OK : {ok} | Skip : {skip} | Erreurs : {erreurs}",
        "",
        "| Fichier | Statut | Qualite | Live | Detail |",
        "|---------|--------|---------|------|--------|"
    ]
    for r in rapport:
        lines.append(
            f"| {r['fichier']} | {r['statut']} | {r.get('qualite','?')} "
            f"| {'OUI' if r.get('live') else 'NON'} | {r.get('detail','')} |"
        )
    lines += [
        "",
        "## PRECAUTIONS DE LECTURE",
        "- QUALITE_VIDEO FAIBLE : verifier manuellement les descriptions visuelles",
        "- TYPE LIVE_TRADING : certaines descriptions peuvent etre incompletes",
        "- Tout chiffre marque ⚠️_A_VERIFIER doit etre confirme sur la video originale",
        "- Les prix exacts lus a l'ecran ne sont jamais fiables a 100% — utiliser",
        "  uniquement les DESCRIPTIONS (haussier/baissier, au-dessus/en dessous)",
        "- Les [REGLE: ...] sont les passages les plus exploitables pour la KB"
    ]

    RAPPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n=== TERMINE ===")
    print(f"OK: {ok} | Skip: {skip} | Erreurs: {erreurs}")
    print(f"Rapport : {RAPPORT_PATH}")

if __name__ == "__main__":
    main()
```

---

## PHASE 2 — INSTALLATION DES DEPENDANCES

Avant de lancer le script, executer dans PowerShell (dossier C:\trading-copilote) :

```
pip install google-generativeai python-dotenv --break-system-packages
```
# CORRECTION 1 : python-dotenv est obligatoire pour lire la GEMINI_API_KEY depuis .env

Verifier l'installation :
```
python -m py_compile 05-saas\utils\gemini_transcriber.py
```

Si aucune erreur : le script est syntaxiquement correct.

---

## PHASE 3 — CONFIGURATION .env

Verifier que le fichier C:\trading-copilote\.env contient :
```
GEMINI_API_KEY=AIzaSy...  (ta cle Google AI Studio)
```

Verifier que .env est dans .gitignore :
```
git check-ignore C:\trading-copilote\.env
```
Si pas de sortie → STOP : ajouter .env dans .gitignore avant tout push.

---

## PHASE 4 — TEST SUR 3 VIDEOS AVANT TRAITEMENT COMPLET

IMPERATIF : ne pas lancer sur les 164 videos avant d'avoir valide la qualite.

Creer un script de test : 05-saas\utils\gemini_test_3videos.py

Ce script doit :
1. Prendre les 3 premieres videos de D:\Belkhayate-Videos
2. Appeler gemini_transcriber.transcrire_video() pour chacune
3. Sauvegarder dans OUTPUT_DIR\test\
4. Afficher les 50 premieres lignes de chaque transcript genere

Lancer :
  python 05-saas\utils\gemini_test_3videos.py

Attendre la validation d'Abdelkrim sur la qualite des 3 transcripts.
NE PAS lancer le traitement complet sans cette validation.

---

## PHASE 5 — TRAITEMENT COMPLET (apres validation)

Lancer seulement apres OK d'Abdelkrim :
  python 05-saas\utils\gemini_transcriber.py

Le script :
- Saute les videos deja traitees (reprise possible apres interruption)
- Attend 2 secondes entre chaque video (respect rate limits Gemini)
- Genere RAPPORT_QUALITE_GEMINI.md en fin de traitement

Duree estimee : 2-5 min par video → 164 videos = 6-14h (laisser tourner la nuit)

---

## GARDE-FOUS LECTURE DES TRANSCRIPTS GEMINI

Apres la transcription, rappeler a l'utilisateur :

1. QUALITE_VIDEO: FAIBLE → relire manuellement la video pour les passages [VISUEL]
2. TYPE: LIVE_TRADING + [ECRAN_CHANGE_RAPIDE] → ce passage est incomplet
3. ⚠️_A_VERIFIER apres un chiffre → ne jamais integrer ce chiffre en KB
   sans verifier sur la video originale
4. [REGLE: ...] → ce sont les passages les plus exploitables pour la KB
5. Les DESCRIPTIONS (haussier/baissier, vert/rouge, au-dessus/en dessous)
   sont fiables. Les CHIFFRES PRECIS ne le sont pas.

---

## VERIFICATION FINALE

- [ ] 05-saas\utils\gemini_transcriber.py cree et compile sans erreur
- [ ] 05-saas\utils\gemini_test_3videos.py cree
- [ ] pip install google-generativeai confirme
- [ ] .env contient GEMINI_API_KEY et est dans .gitignore
- [ ] Test 3 videos lance et affiche resultat
- [ ] Commit : git add . && git commit -m "feat(gemini): pipeline transcription multimodal audio-visuel Belkhayate"
- [ ] Push : git push origin main

COMMENCE par la Phase 1 (creer gemini_transcriber.py).
Puis Phase 2 (installation), puis Phase 3 (verifier .env), puis Phase 4 (test 3 videos).
ATTENDRE la validation avant Phase 5.
