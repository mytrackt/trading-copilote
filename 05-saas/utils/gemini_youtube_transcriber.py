"""
gemini_youtube_transcriber.py — TRADEX-AI
Transcription de videos YouTube via Gemini 2.5 Flash multimodal.
Methode officielle validee S35-S40 (voir CLAUDE.md).
Adapte pour des videos HORS Belkhayate (ex: Claude + trading).

Usage :
  python 05-saas\\utils\\gemini_youtube_transcriber.py

Les URLs sont definies dans la liste YOUTUBE_URLS ci-dessous.
Sortie : 03-transcriptions\\nouvelles-sources\\claude-trading\\transcripts-gemini\\
"""

import os
import sys
import time
import re
import json
from pathlib import Path
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Charger .env
load_dotenv(r"C:\trading-copilote\.env")

# BASE_DIR = racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# CONFIGURATION — modifier ici selon le sujet des videos
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("ERREUR : GEMINI_API_KEY manquant dans C:\\trading-copilote\\.env")
    sys.exit(1)

# Dossier de sortie — adapte au sujet des videos
OUTPUT_DIR = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "claude-trading" / "transcripts-gemini"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Rapport de qualite
RAPPORT_PATH = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "claude-trading" / "RAPPORT_QUALITE_CLAUDE_TRADING.md"

# URLs YouTube a transcrire
YOUTUBE_URLS = [
    "https://youtu.be/RetsRS5u-8Q",
    "https://youtu.be/nLQhKkjkuWI",
    "https://youtu.be/lIMu8ysJW68",
    "https://youtu.be/VfiwA1YThSc",
    "https://youtu.be/G7zv25c7Z8M",
    "https://youtu.be/ANUXcTgrpg0",
    "https://youtu.be/CPkrCoIbBIA",
    "https://youtu.be/y_bsjZThP0o",
]

# Modele Gemini officiel (stable, pas experimental)
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-2.5-flash"

# Retry et rate limiting
MAX_RETRIES = 3
RETRY_BACKOFF = [10, 30, 60]
RATE_LIMIT_SECONDS = 5   # pause entre chaque video


# ============================================================
# PROMPT ADAPTE — Claude + trading (pas Belkhayate)
# ============================================================

PROMPT_CLAUDE_TRADING = """Tu es un expert en systemes de trading algorithmique assistes par LLM.
Transcris cette video en francais en integrant l'audio ET le contenu visuel de l'ecran.

CONTEXTE :
Cette video porte sur l'utilisation de Claude (Anthropic) ou de modeles LLM dans le trading
financier : construction de signaux, analyse de marche, prompts de trading, architecture
de systemes IA, gestion du risque avec LLM, etc.

FORMAT OBLIGATOIRE :
- Quand l'ecran montre du code, une interface, un graphique ou un schema :
  [VISUEL: description precise de ce qui est affiche]
  puis continue avec la transcription audio
- Quand l'intervenant enonce un principe, une methode ou une regle concrete :
  [REGLE: formulation complete de la regle ou du principe]
- Pour les passages sans contenu visuel important :
  transcris simplement ce qui est dit

CE QU'IL FAUT CAPTURER EN PRIORITE :
- Prompts utilises pour analyser les marches ou generer des signaux
- Architecture technique : comment Claude/LLM est connecte aux donnees de marche
- Methodes de prompt engineering specifiques au trading
- Gestion du risque et garde-fous avec les LLM
- Actifs traites (Or, Petrole, Crypto, Indices, Forex, etc.)
- Indicateurs techniques utilises en combinaison avec le LLM
- Resultats mesures (performance, precision, drawdown, etc.)
- Erreurs et pieges a eviter avec les LLM en trading
- Frameworks et outils utilises (LangChain, Anthropic SDK, etc.)

DESCRIPTIONS VISUELLES — CE QU'IL FAUT DECRIRE :
- Code visible a l'ecran (langage, fonction principale, logique)
- Interface ou dashboard affiche
- Graphique de prix ou de performance
- Schema d'architecture
- Tableau de resultats ou de backtest

REGLE STRICTE SUR LES CHIFFRES VISUELS :
Ne jamais lire un chiffre precis sur un graphique ou tableau
si tu n'es pas certain a 100%. A la place, utilise des termes relatifs :
  AUTORISE : "performance positive sur la periode"
  AUTORISE : "drawdown visible sur la partie droite du graphique"
  INTERDIT : "le modele a fait +34.2%" si tu n'en es pas certain

Exemple de sortie attendue :
  [VISUEL: Code Python visible. Appel a l'API Anthropic avec un prompt
  contenant les donnees OHLCV des 20 dernieres bougies.]
  "Donc ici je passe les donnees de marche directement dans le prompt."
  [REGLE: Inclure uniquement les 20 dernieres bougies dans le contexte
  pour eviter de depasser la fenetre de tokens et controler le cout.]
  "Et ca me permet de garder un cout raisonnable par signal."

Transcris maintenant la video complete. Sois exhaustif et precis.
"""


# ============================================================
# UTILITAIRES
# ============================================================

def video_id_depuis_url(url: str) -> str:
    """Extrait l'identifiant YouTube (11 caracteres) depuis une URL."""
    patterns = [
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
        r"youtube\.com/shorts/([A-Za-z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    # Fallback : utilise les 11 derniers caracteres de l'URL
    return url.split("/")[-1][:11].replace("?", "_")


def nom_fichier_sortie(url: str, index: int) -> str:
    """Genere un nom de fichier de sortie stable depuis l'URL."""
    vid_id = video_id_depuis_url(url)
    return f"{index:02d}_{vid_id}_gemini.txt"


def fichier_existe_deja(output_path: Path) -> bool:
    """Verifie si la transcription existe deja (reprise sur interruption)."""
    return output_path.exists() and output_path.stat().st_size > 500


# ============================================================
# TRANSCRIPTION D'UNE URL YOUTUBE
# ============================================================

def transcrire_url(url: str, index: int, nb_total: int) -> dict:
    """
    Transcrit une URL YouTube via Gemini 2.5 Flash.
    Gemini accepte les URLs YouTube directement — aucun telechargement necessaire.

    Retourne :
      Success : {"transcript": str, "erreur": None}
      Echec   : {"transcript": None, "erreur": str}
    """
    vid_id = video_id_depuis_url(url)
    print(f"\n[{index}/{nb_total}] {url}")
    print(f"  ID video : {vid_id}")

    for tentative in range(MAX_RETRIES):
        try:
            print(f"  Tentative {tentative + 1}/{MAX_RETRIES} — appel Gemini...")
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[
                    types.Content(
                        parts=[
                            types.Part(
                                file_data=types.FileData(file_uri=url)
                            ),
                            types.Part(text=PROMPT_CLAUDE_TRADING),
                        ]
                    )
                ],
                config=genai.types.GenerateContentConfig(
                    temperature=0.1,
                    max_output_tokens=32768,
                )
            )

            texte = response.text
            if not texte or len(texte) < 100:
                raise ValueError(f"Reponse trop courte ({len(texte)} chars) — possible erreur silencieuse")

            # Entete standard (meme format que gemini_transcriber.py)
            entete = (
                f"[SOURCE_URL: {url}]\n"
                f"[VIDEO_ID: {vid_id}]\n"
                f"[SUJET: claude-trading]\n"
                f"[MODELE: {MODEL_NAME}]\n"
                f"[DATE_TRANSCRIPTION: {time.strftime('%Y-%m-%d')}]\n"
                "---\n"
            )

            print(f"  OK — {len(texte)} caracteres")
            return {"transcript": entete + texte, "erreur": None}

        except Exception as e:
            err_str = str(e)[:120]
            print(f"  Erreur tentative {tentative + 1} : {err_str}")

            if tentative < MAX_RETRIES - 1:
                if "429" in err_str or "quota" in err_str.lower():
                    attente = 60
                    print(f"  Quota depasse — pause {attente}s...")
                else:
                    attente = RETRY_BACKOFF[tentative]
                    print(f"  Pause {attente}s...")
                time.sleep(attente)

    return {"transcript": None, "erreur": f"Echec apres {MAX_RETRIES} tentatives"}


# ============================================================
# PIPELINE PRINCIPAL
# ============================================================

def main():
    print("=" * 60)
    print("GEMINI YOUTUBE TRANSCRIBER — Claude + Trading")
    print(f"Modele    : {MODEL_NAME}")
    print(f"Videos    : {len(YOUTUBE_URLS)}")
    print(f"Sortie    : {OUTPUT_DIR}")
    print("=" * 60)

    nb_total = len(YOUTUBE_URLS)
    resultats = []

    for index, url in enumerate(YOUTUBE_URLS, 1):
        vid_id   = video_id_depuis_url(url)
        nom_out  = nom_fichier_sortie(url, index)
        out_path = OUTPUT_DIR / nom_out

        # Reprise sur interruption — skip si deja transcrit
        if fichier_existe_deja(out_path):
            print(f"\n[{index}/{nb_total}] {vid_id} — DEJA TRANSCRIT, skip")
            resultats.append({"url": url, "vid_id": vid_id, "statut": "skip", "fichier": nom_out})
            continue

        result = transcrire_url(url, index, nb_total)

        if result["transcript"]:
            # Ecriture atomique (CLAUDE.md : tempfile + os.replace)
            tmp_path = out_path.with_suffix(".tmp")
            tmp_path.write_text(result["transcript"], encoding="utf-8")
            os.replace(str(tmp_path), str(out_path))
            print(f"  Sauvegarde : {nom_out}")
            resultats.append({"url": url, "vid_id": vid_id, "statut": "OK", "fichier": nom_out})
        else:
            print(f"  ECHEC : {result['erreur']}")
            resultats.append({"url": url, "vid_id": vid_id, "statut": "ERREUR", "erreur": result["erreur"]})

        # Pause entre videos (rate limiting)
        if index < nb_total:
            print(f"  Pause {RATE_LIMIT_SECONDS}s...")
            time.sleep(RATE_LIMIT_SECONDS)

    # ---- Rapport final ----
    nb_ok    = sum(1 for r in resultats if r["statut"] == "OK")
    nb_skip  = sum(1 for r in resultats if r["statut"] == "skip")
    nb_err   = sum(1 for r in resultats if r["statut"] == "ERREUR")

    print("\n" + "=" * 60)
    print(f"TERMINE — OK: {nb_ok} | Skip: {nb_skip} | Erreurs: {nb_err}")
    print("=" * 60)

    # Ecriture rapport Markdown
    lignes = [
        "# Rapport Transcription — Claude + Trading\n",
        f"Date : {time.strftime('%Y-%m-%d %H:%M')}\n",
        f"Modele : {MODEL_NAME}\n\n",
        f"| # | Video ID | Statut | Fichier |\n",
        "|---|----------|--------|---------|\n",
    ]
    for i, r in enumerate(resultats, 1):
        statut  = r["statut"]
        fichier = r.get("fichier", r.get("erreur", ""))
        lignes.append(f"| {i} | {r['vid_id']} | {statut} | {fichier} |\n")

    RAPPORT_PATH.write_text("".join(lignes), encoding="utf-8")
    print(f"Rapport : {RAPPORT_PATH}")

    if nb_err > 0:
        print("\nVIDEOS EN ERREUR :")
        for r in resultats:
            if r["statut"] == "ERREUR":
                print(f"  {r['url']} — {r.get('erreur', '')}")

    return 0 if nb_err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
