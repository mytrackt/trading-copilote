# transcript_processor_gemini.py
# Pipeline extraction regles Belkhayate depuis transcriptions Gemini (_gemini.txt)
# Input  : 03-transcriptions/nouvelles-sources/belkhayate-youtube/transcripts-gemini/
# Output : 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json
#
# Differences vs transcript_processor.py (Whisper) :
#   - Pas de MANIFESTE - lit directement les *_gemini.txt
#   - Filtre OFTC automatique (noms commencant par "OFTC")
#   - source_video_id = stem du fichier sans "_gemini" (ex: "11")
#   - Reconnait les marqueurs Gemini [VISUEL:], [REGLE:], [QUALITE_VIDEO:]
#
# REGLES : D-S39-3 (BASE_DIR 3x dirname) | CLAUDE.md (atomic writes, rate limit 1.5s)
# D-S39-2 : NE PAS relancer transcript_processor.py apres ce script
#            inject_chapter_rules.py doit etre la DERNIERE ecriture KB

import json
import os
import sys
import time
import re
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("ERREUR : module 'anthropic' manquant.")
    print("  pip install anthropic --break-system-packages")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")
except ImportError:
    pass

# BASE_DIR = 3x dirname car 05-saas/knowledge_base/ (D-S39-3)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INPUT_DIR = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "belkhayate-youtube" / "transcripts-gemini"
KB_FILE   = Path(BASE_DIR) / "04-cerveau-trading" / "KNOWLEDGE_BASE_MASTER.json"
LOG_FILE  = Path(BASE_DIR) / "04-cerveau-trading" / "processor_gemini_status.json"

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 4096
RATE_LIMIT_SECONDS = 1.5
MAX_TRANSCRIPT_CHARS = 60000

CATEGORIES = [
    "saisonnalite", "correlations", "timing",
    "indicateurs_tendance", "indicateurs_momentum",
    "gestion_risque_entree", "gestion_position_active",
    "structure_marche", "macro_evenements", "volume_liquidite", "psychologie",
]

SYSTEM_PROMPT = (
    "Tu es un analyste expert de la methode de trading Belkhayate.\n"
    "On te donne le transcript d'une video de Mostafa Belkhayate.\n"
    "Ce transcript a ete produit par Gemini multimodal -- il contient des marqueurs :\n"
    "  [VISUEL: description de l'ecran] -- ce que Gemini voit sur l'ecran\n"
    "  [REGLE: formulation d'une regle] -- regles explicitement enoncees\n"
    "  [QUALITE_VIDEO: ...] -- metadata a ignorer\n"
    "  [TYPE: ...] -- metadata a ignorer\n"
    "\n"
    "Ta mission : extraire UNIQUEMENT les regles, principes et observations concrets\n"
    "et actionnables que Belkhayate enonce (verbalement OU via [REGLE:]).\n"
    "Ignore commentaires meta, promotions, anecdotes personnelles.\n"
    "\n"
    "Categories autorisees (exactement ces 11 cles) :\n"
    "- saisonnalite : effets calendaires, mois/jours/heures favorables ou non\n"
    "- correlations : liens entre actifs (Or/Dollar, Petrole/Cuivre, SP500/VIX, etc.)\n"
    "- timing : moments entree/sortie, sessions, ouverture/cloture marches\n"
    "- indicateurs_tendance : Barycenter/COG, Belkhayate Trend, pivots, MM, S/R\n"
    "- indicateurs_momentum : Belkhayate Energie, RSI, MACD, divergences\n"
    "- gestion_risque_entree : stop loss, confirmation entree, filtres, taille position\n"
    "- gestion_position_active : trailing stop, sorties partielles, gestion en cours\n"
    "- structure_marche : range vs tendance, niveaux cles, cassures, configurations\n"
    "- macro_evenements : impact news economiques, banques centrales, saisonnalite macro\n"
    "- volume_liquidite : volume, open interest, delta, footprint, liquidite\n"
    "- psychologie : discipline, emotions, patience, money management comportemental\n"
    "\n"
    "CONTRAINTES CRITIQUES :\n"
    "1. JAMAIS inventer une regle absente du transcript\n"
    "2. JAMAIS inclure de chiffres exacts visuels (marques A_VERIFIER)\n"
    "3. Chaque regle = phrase complete, autonome, actionnable\n"
    "4. Si contenu hors sujet Belkhayate -> retourner listes vides\n"
    "5. Min 0 regle, max 30 regles par categorie\n"
    "\n"
    "Reponds UNIQUEMENT avec ce JSON valide, sans texte avant ni apres :\n"
    "{\n"
    '  "saisonnalite": ["regle1", ...],\n'
    '  "correlations": [...],\n'
    '  "timing": [...],\n'
    '  "indicateurs_tendance": [...],\n'
    '  "indicateurs_momentum": [...],\n'
    '  "gestion_risque_entree": [...],\n'
    '  "gestion_position_active": [...],\n'
    '  "structure_marche": [...],\n'
    '  "macro_evenements": [...],\n'
    '  "volume_liquidite": [...],\n'
    '  "psychologie": [...]\n'
    "}"
)


def parse_claude_json(response_text):
    """
    Parse la reponse JSON de Claude de facon robuste.
    Jamais json.loads() direct sur une reponse Claude (CLAUDE.md).
    Gere les backticks markdown et le texte parasite avant/apres le JSON.
    """
    text = response_text.strip()
    text = re.sub(r"^```json\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^```\s*", "", text, flags=re.MULTILINE)
    text = text.strip()

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return None

    json_str = text[start : end + 1]
    try:
        data = json.loads(json_str)
        for cat in CATEGORIES:
            if cat not in data:
                data[cat] = []
            if not isinstance(data[cat], list):
                data[cat] = []
        return data
    except (json.JSONDecodeError, ValueError):
        return None


def load_kb():
    """Charge la KB existante ou retourne une KB vide."""
    if KB_FILE.exists():
        try:
            with open(KB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {"videos": {}, "aggregated_rules": {cat: [] for cat in CATEGORIES}}


def save_kb_atomic(kb):
    """Sauvegarde atomique via tempfile + os.replace (CLAUDE.md)."""
    tmp = Path(str(KB_FILE) + ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(kb, f, ensure_ascii=False, indent=2)
        os.replace(str(tmp), str(KB_FILE))
    except Exception:
        if tmp.exists():
            try:
                os.remove(str(tmp))
            except Exception:
                pass
        raise


def empty_rules():
    return {cat: [] for cat in CATEGORIES}


def rebuild_aggregated(kb):
    """
    Reconstruit aggregated_rules depuis kb['videos'] uniquement.
    D-S39-2 : efface les regles chapitres (dict sans source_video_id).
    => inject_chapter_rules.py doit etre lance APRES ce processeur.
    """
    agg = empty_rules()
    seen = {cat: set() for cat in CATEGORIES}
    for vid in kb.get("videos", {}).values():
        rules = vid.get("rules", {})
        for cat in CATEGORIES:
            for rule in rules.get(cat, []):
                if isinstance(rule, str):
                    key = rule.lower().strip()
                    if key and key not in seen[cat]:
                        seen[cat].add(key)
                        agg[cat].append(rule)
    kb["aggregated_rules"] = agg


def lister_fichiers(input_dir):
    """
    Liste tous les *_gemini.txt non-OFTC, tries alphabetiquement.
    Reproductible : meme ordre a chaque execution.
    """
    return sorted([
        f for f in input_dir.glob("*_gemini.txt")
        if not f.name.startswith("OFTC")
    ])


def extraire_regles(client, transcript, source_id):
    """
    Appel Claude avec retry x3 et rate limiting.
    Retourne dict des 11 categories ou None si echec.
    """
    if len(transcript) > MAX_TRANSCRIPT_CHARS:
        print("  Tronque : " + str(len(transcript)) + " -> " + str(MAX_TRANSCRIPT_CHARS) + " chars")
        transcript = transcript[:MAX_TRANSCRIPT_CHARS]

    user_content = (
        "Source : " + source_id + "\n\n"
        "<<<TRANSCRIPT_GEMINI>>>\n" + transcript + "\n<<<FIN_TRANSCRIPT>>>"
    )

    for tentative in range(3):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_content}],
            )
            result = parse_claude_json(response.content[0].text)
            if result is not None:
                return result
            print("  Parse JSON echoue (tentative " + str(tentative + 1) + "/3)")
        except Exception as e:
            err = str(e)[:100]
            wait = 60 if "429" in err else [10, 30, 60][tentative]
            print("  Erreur API (tentative " + str(tentative + 1) + "/3) : " + err)
            if tentative < 2:
                time.sleep(wait)
    return None


def main():
    print("=" * 60)
    print("TRANSCRIPT PROCESSOR GEMINI -- TRADEX-AI")
    print("=" * 60)
    print("BASE_DIR  : " + str(BASE_DIR))
    print("INPUT_DIR : " + str(INPUT_DIR))
    print("KB_FILE   : " + str(KB_FILE))
    print()

    # Verifications
    if not INPUT_DIR.exists():
        print("ERREUR : INPUT_DIR introuvable : " + str(INPUT_DIR))
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERREUR : ANTHROPIC_API_KEY manquant dans .env")
        sys.exit(1)

    # Inventaire
    fichiers = lister_fichiers(INPUT_DIR)
    if not fichiers:
        print("ERREUR : Aucun fichier *_gemini.txt (non-OFTC) dans " + str(INPUT_DIR))
        sys.exit(1)
    print("Fichiers disponibles : " + str(len(fichiers)))

    # Charger KB et detecter deja traites
    kb = load_kb()
    deja_traites = set(kb.get("videos", {}).keys())
    a_traiter = [
        f for f in fichiers
        if f.stem.replace("_gemini", "") not in deja_traites
    ]

    print("Deja traites         : " + str(len(deja_traites)))
    print("A traiter            : " + str(len(a_traiter)))

    if not a_traiter:
        print("Tous les fichiers sont deja traites. Rien a faire.")
        sys.exit(0)

    cout_min = round(len(a_traiter) * 0.01, 2)
    cout_max = round(len(a_traiter) * 0.05, 2)
    duree_min = len(a_traiter) * 2
    duree_max = len(a_traiter) * 5
    print("Cout estime          : " + str(cout_min) + "$ -- " + str(cout_max) + "$")
    print("Duree estimee        : " + str(duree_min) + " -- " + str(duree_max) + " minutes")
    print()

    confirmation = input("Confirmes-tu le lancement ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Annule.")
        sys.exit(0)
    print()

    client = Anthropic(api_key=api_key)

    nb_ok = 0
    nb_erreurs = 0
    debut = time.time()

    for i, fichier in enumerate(a_traiter, 1):
        source_id = fichier.stem.replace("_gemini", "")
        print("[" + str(i).rjust(3) + "/" + str(len(a_traiter)) + "] " + fichier.name)

        # Lire transcript
        try:
            transcript = fichier.read_text(encoding="utf-8")
        except Exception as e:
            print("  ERREUR lecture : " + str(e))
            nb_erreurs += 1
            continue

        # Extraire regles via Claude
        regles = extraire_regles(client, transcript, source_id)

        if regles is None:
            print("  ERREUR extraction -- video marquee ERREUR")
            nb_erreurs += 1
            kb.setdefault("videos", {})[source_id] = {
                "rules": empty_rules(),
                "source_file": fichier.name,
                "date_extraction": datetime.now().isoformat(),
                "statut": "ERREUR",
            }
        else:
            nb_regles = sum(len(v) for v in regles.values())
            print("  OK -- " + str(nb_regles) + " regles extraites")
            nb_ok += 1
            kb.setdefault("videos", {})[source_id] = {
                "rules": regles,
                "source_file": fichier.name,
                "date_extraction": datetime.now().isoformat(),
                "statut": "OK",
            }

        # Rebuild aggregated + sauvegarde atomique apres CHAQUE video
        rebuild_aggregated(kb)
        save_kb_atomic(kb)

        time.sleep(RATE_LIMIT_SECONDS)

    # Rapport final
    duree_totale = time.time() - debut
    total_regles = sum(
        len(v) for v in kb.get("aggregated_rules", {}).values()
    )

    print()
    print("=" * 60)
    print("TERMINE -- OK: " + str(nb_ok) + " | Erreurs: " + str(nb_erreurs))
    print("Duree totale    : " + str(round(duree_totale / 60, 1)) + " minutes")
    print("Regles KB total : " + str(total_regles))
    if total_regles >= 800:
        print("OBJECTIF        : OK >= 800 regles atteint")
    else:
        print("OBJECTIF        : ATTENTION < 800 regles -- verifier qualite")
    print()
    print("ETAPE SUIVANTE OBLIGATOIRE (D-S39-2) :")
    print("  python 05-saas/utils/inject_chapter_rules.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
