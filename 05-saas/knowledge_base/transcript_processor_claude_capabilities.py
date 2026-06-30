"""
transcript_processor_claude_capabilities.py - TRADEX-AI
Extrait capacites et astuces Claude depuis transcriptions *_gemini.txt.
Utilise Gemini API (GEMINI_API_KEY) car credits Anthropic epuises.

SOURCES :
  - 03-transcriptions/nouvelles-sources/Claude NinjaTrader/
  - 03-transcriptions/nouvelles-sources/Alex Carter/
  - 03-transcriptions/nouvelles-sources/claude-trading/transcripts-gemini/

Output :
  - 00-pilotage/CLAUDE_CAPABILITIES_TRADING.md
  - 04-cerveau-trading/KB_CLAUDE_CAPABILITIES.json

Usage : python 05-saas\\knowledge_base\\transcript_processor_claude_capabilities.py
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from google import genai
except ImportError:
    print("ERREUR : pip install google-genai --break-system-packages")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INPUT_DIRS = [
    Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "Claude NinjaTrader",
    Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "Alex Carter",
    Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "claude-trading" / "transcripts-gemini",
]

KB_FILE  = Path(BASE_DIR) / "04-cerveau-trading" / "KB_CLAUDE_CAPABILITIES.json"
MD_FILE  = Path(BASE_DIR) / "00-pilotage" / "CLAUDE_CAPABILITIES_TRADING.md"
LOG_FILE = Path(BASE_DIR) / "04-cerveau-trading" / "processor_claude_capabilities_status.json"

MODEL      = "gemini-2.5-flash"
MAX_TOKENS = 16384
RATE_LIMIT = 2.0
MAX_CHARS  = 12000

CATEGORIES = [
    "prompt_engineering_trading",
    "architecture_llm_trading",
    "tools_use_function_calling",
    "gestion_cout_tokens",
    "fiabilite_hallucinations",
    "analyse_technique_llm",
    "gestion_risque_llm",
    "workflow_automatisation",
    "nouvelles_fonctionnalites",
    "retours_experience",
]

PROMPT_SYSTEME = """Tu es un architecte expert de systemes de trading algorithmique assistes par LLM.

On te donne la transcription d'une video sur l'utilisation de Claude ou d'un LLM en trading.

OBJECTIF : Extraire les informations concretes et actionnables pour construire TRADEX-AI.

CONTEXTE TRADEX-AI : Python + Claude API + NinjaTrader 8. Actifs : Or GC, Petrole CL, Cuivre HG, Ble ZW.

Categories autorisees (exactement ces 10 cles JSON) :
- prompt_engineering_trading : formulations de prompts pour signaux et analyse de marche
- architecture_llm_trading : comment connecter Claude aux donnees de marche
- tools_use_function_calling : usage des tools/functions Claude en trading
- gestion_cout_tokens : techniques pour reduire les couts API (caching, modele adaptatif)
- fiabilite_hallucinations : garde-fous contre les hallucinations en trading
- analyse_technique_llm : comment Claude interprete les indicateurs techniques
- gestion_risque_llm : risk management integre dans les prompts
- workflow_automatisation : pipelines automatises trading + Claude
- nouvelles_fonctionnalites : nouvelles features Anthropic utiles pour TRADEX
- retours_experience : resultats mesures, erreurs vecues, lecons apprises

REGLE : Chaque element = 1 phrase autonome directement reutilisable dans TRADEX.
Maximum 15 elements par categorie. Liste vide si rien de pertinent.
Ne jamais inventer une information absente du transcript.

REPONSE : JSON strict uniquement, sans texte avant ou apres.

{
  "source_video_id": "id de la video",
  "regles": {
    "prompt_engineering_trading": [],
    "architecture_llm_trading": [],
    "tools_use_function_calling": [],
    "gestion_cout_tokens": [],
    "fiabilite_hallucinations": [],
    "analyse_technique_llm": [],
    "gestion_risque_llm": [],
    "workflow_automatisation": [],
    "nouvelles_fonctionnalites": [],
    "retours_experience": []
  }
}"""


def parse_json(reponse):
    """Parse la reponse JSON de Gemini (mode JSON natif — pas de markdown)."""
    try:
        return json.loads(reponse)
    except json.JSONDecodeError:
        # Fallback : extraire le bloc JSON si du texte s'est glisse quand meme
        match = re.search(r"\{.*\}", reponse, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
    return None


def charger_kb():
    if KB_FILE.exists():
        try:
            with open(KB_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "meta": {
            "description": "Capacites et astuces Claude pour TRADEX-AI",
            "derniere_maj": "",
            "nb_videos": 0,
            "nb_regles": 0,
        },
        "videos_traitees": [],
        "aggregated_rules": {cat: [] for cat in CATEGORIES},
    }


def sauvegarder_kb(kb):
    nb = sum(len(v) for v in kb["aggregated_rules"].values())
    kb["meta"]["derniere_maj"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    kb["meta"]["nb_regles"] = nb
    kb["meta"]["nb_videos"] = len(kb["videos_traitees"])
    tmp = KB_FILE.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)
    os.replace(str(tmp), str(KB_FILE))
    print("  KB sauvegardee : " + str(nb) + " regles total")


def generer_md(kb):
    titres = {
        "prompt_engineering_trading": "## 1. Prompt Engineering pour le Trading",
        "architecture_llm_trading":   "## 2. Architecture LLM + Trading",
        "tools_use_function_calling": "## 3. Tools Use / Function Calling",
        "gestion_cout_tokens":        "## 4. Gestion Cout / Tokens",
        "fiabilite_hallucinations":   "## 5. Fiabilite et Anti-Hallucinations",
        "analyse_technique_llm":      "## 6. Analyse Technique avec LLM",
        "gestion_risque_llm":         "## 7. Gestion du Risque avec LLM",
        "workflow_automatisation":    "## 8. Workflow et Automatisation",
        "nouvelles_fonctionnalites":  "## 9. Nouvelles Fonctionnalites Anthropic",
        "retours_experience":         "## 10. Retours d Experience",
    }
    lignes = [
        "# CLAUDE CAPABILITIES TRADING -- Reference TRADEX-AI\n\n",
        "> Genere automatiquement depuis " + str(kb["meta"]["nb_videos"]) + " videos.\n",
        "> Derniere MAJ : " + kb["meta"]["derniere_maj"] + "  \n",
        "> Total regles : " + str(kb["meta"]["nb_regles"]) + "\n\n---\n\n",
    ]
    for cat, titre in titres.items():
        regles = kb["aggregated_rules"].get(cat, [])
        lignes.append(titre + "\n\n")
        if regles:
            for r in regles:
                lignes.append("- " + r + "\n")
        else:
            lignes.append("*Aucune regle extraite.*\n")
        lignes.append("\n")
    lignes.append("---\n*Sources : " + ", ".join(kb["videos_traitees"]) + "*\n")
    tmp = MD_FILE.with_suffix(".tmp")
    tmp.write_text("".join(lignes), encoding="utf-8")
    os.replace(str(tmp), str(MD_FILE))
    print("  MD genere : " + str(MD_FILE.name))


def collecter_fichiers():
    vus = {}
    for dossier in INPUT_DIRS:
        if not dossier.exists():
            print("  Dossier absent (skip) : " + str(dossier))
            continue
        for f in sorted(dossier.glob("*_gemini.txt")):
            vid_id = re.sub(r"^\d+_", "", f.stem.replace("_gemini", ""))
            if vid_id not in vus:
                vus[vid_id] = f
            else:
                if f.stat().st_size > vus[vid_id].stat().st_size:
                    print("  Doublon " + vid_id + " : garde " + f.name)
                    vus[vid_id] = f
                else:
                    print("  Doublon " + vid_id + " : ignore " + f.name)
    return list(vus.items())


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERREUR : GEMINI_API_KEY manquant dans .env")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print("Collecte des fichiers sources...")
    fichiers = collecter_fichiers()
    if not fichiers:
        print("Aucun fichier *_gemini.txt trouve.")
        sys.exit(1)

    print("=" * 60)
    print("PROCESSOR -- Capacites Claude pour TRADEX-AI (via Gemini)")
    print("Modele  : " + MODEL)
    print("Fichiers: " + str(len(fichiers)))
    print("=" * 60)

    kb = charger_kb()
    log = {}
    nb_ok = nb_skip = nb_err = 0

    for i, (vid_id, fichier) in enumerate(fichiers, 1):
        print("\n[" + str(i) + "/" + str(len(fichiers)) + "] " + vid_id + " -- " + fichier.name)

        if vid_id in kb["videos_traitees"]:
            print("  Deja traite -- skip")
            nb_skip += 1
            continue

        texte = fichier.read_text(encoding="utf-8")
        if len(texte) < 200:
            print("  Trop court (" + str(len(texte)) + " chars) -- skip")
            nb_err += 1
            log[vid_id] = "trop_court"
            continue

        if len(texte) > MAX_CHARS:
            texte = texte[:MAX_CHARS]
            print("  Tronque a " + str(MAX_CHARS) + " chars")

        prompt_complet = PROMPT_SYSTEME + "\n\nVideo ID : " + vid_id + "\n\nTRANSCRIPT :\n" + texte

        try:
            print("  Appel Gemini API...")
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt_complet,
                config=genai.types.GenerateContentConfig(
                    temperature=0.1,
                    max_output_tokens=MAX_TOKENS,
                    response_mime_type="application/json",
                )
            )
            reponse_brute = response.text
            time.sleep(RATE_LIMIT)

        except Exception as e:
            erreur = str(e)
            print("  ERREUR API : " + erreur)
            nb_err += 1
            log[vid_id] = "erreur_api: " + erreur
            with open(LOG_FILE, "w", encoding="utf-8") as f_log:
                json.dump(log, f_log, ensure_ascii=False, indent=2)
            continue

        data = parse_json(reponse_brute)
        if not data or "regles" not in data:
            print("  ERREUR JSON invalide. Debut reponse : " + reponse_brute[:300])
            nb_err += 1
            log[vid_id] = "json_invalide"
            continue

        regles_video = data.get("regles", {})
        nb_new = 0
        for cat in CATEGORIES:
            nouvelles = regles_video.get(cat, [])
            if nouvelles:
                existantes = set(kb["aggregated_rules"][cat])
                ajouts = [r for r in nouvelles if r not in existantes]
                kb["aggregated_rules"][cat].extend(ajouts)
                nb_new += len(ajouts)

        kb["videos_traitees"].append(vid_id)
        print("  +" + str(nb_new) + " regles extraites")
        log[vid_id] = "ok: " + str(nb_new) + " regles"
        nb_ok += 1
        sauvegarder_kb(kb)

    generer_md(kb)

    with open(LOG_FILE, "w", encoding="utf-8") as f_log:
        json.dump(log, f_log, ensure_ascii=False, indent=2)

    nb_total = sum(len(v) for v in kb["aggregated_rules"].values())
    print("\n" + "=" * 60)
    print("TERMINE -- OK: " + str(nb_ok) + " | Skip: " + str(nb_skip) + " | Erreurs: " + str(nb_err))
    print("Total regles KB : " + str(nb_total))
    print("MD genere       : " + str(MD_FILE))
    print("=" * 60)

    return 0 if nb_err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
