# transcript_processor_gemini_batch.py
# Pipeline BATCH API Claude : extraction regles Belkhayate depuis *_gemini.txt
# Avantage vs version synchrone : -50% cout, traitement parallele (< 1h pour 100 fichiers)
# Input  : 03-transcriptions/nouvelles-sources/belkhayate-youtube/transcripts-gemini/
# Output : 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json
#
# REMARQUE : les *_gemini.txt deja dans la KB sont automatiquement skipped.
#
# UTILISATION :
#   py 05-saas\knowledge_base\transcript_processor_gemini_batch.py
#   py 05-saas\knowledge_base\transcript_processor_gemini_batch.py --resume
#     (reprendre un batch soumis lors d'une session precedente)
#
# REGLES : D-S39-3 (BASE_DIR 3x dirname) | CLAUDE.md (atomic writes, parse_claude_json)
# D-S39-2 : lancer inject_chapter_rules.py APRES ce script

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request as BatchRequest
except ImportError as e:
    print("ERREUR : module 'anthropic' manquant ou trop ancien.")
    print("  pip install --upgrade anthropic --break-system-packages")
    print("  Detail : " + str(e))
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")
except ImportError:
    pass

# BASE_DIR = 3x dirname car 05-saas/knowledge_base/ (D-S39-3)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INPUT_DIR   = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "belkhayate-youtube" / "transcripts-gemini"
KB_FILE     = Path(BASE_DIR) / "04-cerveau-trading" / "KNOWLEDGE_BASE_MASTER.json"
BATCH_STATE = Path(BASE_DIR) / "04-cerveau-trading" / "batch_processor_state.json"

MODEL                = "claude-sonnet-4-6"
MAX_TOKENS           = 4096
MAX_TRANSCRIPT_CHARS = 60000
POLL_INTERVAL_SEC    = 60

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


# =============================================================================
# Fonctions utilitaires (identiques a transcript_processor_gemini.py)
# =============================================================================

def parse_claude_json(response_text):
    """
    Parse robuste de la reponse JSON de Claude.
    Jamais json.loads() direct sur une reponse Claude (CLAUDE.md).
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
    D-S39-2 : efface les regles chapitres — inject_chapter_rules.py doit suivre.
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
    """Liste tous les *_gemini.txt non-OFTC, tries alphabetiquement."""
    return sorted([
        f for f in input_dir.glob("*_gemini.txt")
        if not f.name.startswith("OFTC")
    ])


# =============================================================================
# Fonctions Batch API
# =============================================================================

def custom_id_from_index(i):
    """Genere un custom_id Batch-safe (regex ^[a-zA-Z0-9_-]{1,64}$)."""
    return "vid-" + str(i).zfill(4)


def construire_requetes(fichiers_a_traiter):
    """
    Construit la liste de BatchRequest pour le Batch API.
    Retourne (requests, mapping) ou mapping = {custom_id: source_id}.
    Les noms de fichiers avec espaces/accents sont encodes via un index.
    """
    requests = []
    mapping  = {}

    for i, fichier in enumerate(fichiers_a_traiter):
        source_id = fichier.stem.replace("_gemini", "")
        cid       = custom_id_from_index(i)
        mapping[cid] = source_id

        try:
            transcript = fichier.read_text(encoding="utf-8")
        except Exception as e:
            print("  ERREUR lecture " + fichier.name + " : " + str(e))
            continue

        if len(transcript) > MAX_TRANSCRIPT_CHARS:
            transcript = transcript[:MAX_TRANSCRIPT_CHARS]

        user_content = (
            "Source : " + source_id + "\n\n"
            "<<<TRANSCRIPT_GEMINI>>>\n" + transcript + "\n<<<FIN_TRANSCRIPT>>>"
        )

        requests.append(BatchRequest(
            custom_id=cid,
            params=MessageCreateParamsNonStreaming(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_content}],
            ),
        ))

    return requests, mapping


def sauvegarder_state(batch_id, mapping):
    """Sauvegarde batch_id + mapping pour reprise eventuelle."""
    state = {
        "batch_id":   batch_id,
        "created_at": datetime.now().isoformat(),
        "mapping":    mapping,
        "status":     "polling",
    }
    tmp = Path(str(BATCH_STATE) + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    os.replace(str(tmp), str(BATCH_STATE))
    print("State sauvegarde : " + str(BATCH_STATE))


def charger_state():
    """Charge le state d'un batch precedent (pour --resume)."""
    if not BATCH_STATE.exists():
        return None
    try:
        with open(BATCH_STATE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def supprimer_state():
    """Supprime le fichier state apres traitement reussi."""
    if BATCH_STATE.exists():
        try:
            os.remove(str(BATCH_STATE))
        except Exception:
            pass


def attendre_batch(client, batch_id):
    """Poll le batch jusqu'a completion. Affiche progression."""
    print()
    print("Batch ID : " + batch_id)
    print("Polling toutes les " + str(POLL_INTERVAL_SEC) + "s (Ctrl+C pour interrompre)")
    print("  -> relancer avec --resume pour reprendre le polling")
    print()

    while True:
        try:
            batch = client.messages.batches.retrieve(batch_id)
        except Exception as e:
            print("  ERREUR retrieve : " + str(e) + " -- retry dans 60s")
            time.sleep(60)
            continue

        if batch.processing_status == "ended":
            print("Batch termine.")
            return batch

        c = batch.request_counts
        ts = datetime.now().strftime("%H:%M:%S")
        print(
            "[" + ts + "] processing=" + str(c.processing)
            + " | succeeded=" + str(c.succeeded)
            + " | errored=" + str(c.errored)
            + " | expired=" + str(c.expired)
        )
        time.sleep(POLL_INTERVAL_SEC)


def traiter_resultats(client, batch_id, mapping, kb):
    """
    Lit les resultats JSONL du batch et met a jour la KB.
    Retourne (nb_ok, nb_erreurs).
    """
    nb_ok      = 0
    nb_erreurs = 0

    print()
    print("Traitement des resultats...")

    for result in client.messages.batches.results(batch_id):
        cid       = result.custom_id
        source_id = mapping.get(cid, cid)

        if result.result.type == "succeeded":
            text   = result.result.message.content[0].text
            regles = parse_claude_json(text)
            if regles:
                nb_regles = sum(len(v) for v in regles.values())
                print("  OK " + source_id + " -- " + str(nb_regles) + " regles")
                nb_ok += 1
                kb.setdefault("videos", {})[source_id] = {
                    "rules":            regles,
                    "source_file":      source_id + "_gemini.txt",
                    "date_extraction":  datetime.now().isoformat(),
                    "statut":           "OK",
                    "extraction_mode":  "batch",
                }
            else:
                print("  PARSE ERREUR " + source_id + " (JSON invalide)")
                nb_erreurs += 1
                kb.setdefault("videos", {})[source_id] = {
                    "rules":            empty_rules(),
                    "source_file":      source_id + "_gemini.txt",
                    "date_extraction":  datetime.now().isoformat(),
                    "statut":           "ERREUR",
                    "extraction_mode":  "batch",
                }

        elif result.result.type == "errored":
            err_type = ""
            try:
                err_type = result.result.error.error.type
            except Exception:
                err_type = "inconnu"
            print("  ERREUR API " + source_id + " (" + err_type + ")")
            nb_erreurs += 1

        elif result.result.type == "expired":
            print("  EXPIRED " + source_id + " (batch > 24h)")
            nb_erreurs += 1

        elif result.result.type == "canceled":
            print("  CANCELED " + source_id)
            nb_erreurs += 1

    return nb_ok, nb_erreurs


# =============================================================================
# Main
# =============================================================================

def main():
    mode_resume = "--resume" in sys.argv

    print("=" * 60)
    print("TRANSCRIPT PROCESSOR GEMINI -- BATCH API -- TRADEX-AI")
    print("=" * 60)
    print("BASE_DIR  : " + str(BASE_DIR))
    print("INPUT_DIR : " + str(INPUT_DIR))
    print("KB_FILE   : " + str(KB_FILE))
    print()

    # Verification API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERREUR : ANTHROPIC_API_KEY manquant dans .env")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # --- MODE RESUME ---
    if mode_resume:
        state = charger_state()
        if not state:
            print("ERREUR : aucun batch en cours (fichier state absent).")
            print("  Relancez sans --resume pour soumettre un nouveau batch.")
            sys.exit(1)

        batch_id = state["batch_id"]
        mapping  = state["mapping"]
        print("RESUME -- Batch ID : " + batch_id)
        print("Cree le           : " + state.get("created_at", "?"))
        print("Videos dans batch : " + str(len(mapping)))
        print()

        batch = attendre_batch(client, batch_id)
        kb    = load_kb()
        nb_ok, nb_erreurs = traiter_resultats(client, batch_id, mapping, kb)

        rebuild_aggregated(kb)
        save_kb_atomic(kb)
        supprimer_state()

        total_regles = sum(len(v) for v in kb.get("aggregated_rules", {}).values())
        print()
        print("=" * 60)
        print("RESUME TERMINE -- OK: " + str(nb_ok) + " | Erreurs: " + str(nb_erreurs))
        print("Regles KB total : " + str(total_regles))
        print()
        print("ETAPE SUIVANTE OBLIGATOIRE (D-S39-2) :")
        print("  py 05-saas\\utils\\inject_chapter_rules.py")
        print("=" * 60)
        return

    # --- MODE NORMAL ---
    if not INPUT_DIR.exists():
        print("ERREUR : INPUT_DIR introuvable : " + str(INPUT_DIR))
        sys.exit(1)

    fichiers = lister_fichiers(INPUT_DIR)
    if not fichiers:
        print("ERREUR : Aucun fichier *_gemini.txt (non-OFTC) dans " + str(INPUT_DIR))
        sys.exit(1)

    kb = load_kb()
    deja_traites = set(kb.get("videos", {}).keys())
    a_traiter    = [
        f for f in fichiers
        if f.stem.replace("_gemini", "") not in deja_traites
    ]

    print("Fichiers disponibles : " + str(len(fichiers)))
    print("Deja dans KB         : " + str(len(deja_traites)))
    print("A traiter en batch   : " + str(len(a_traiter)))

    if not a_traiter:
        print()
        print("Tous les fichiers sont deja dans la KB. Rien a faire.")
        sys.exit(0)

    # Estimation cout (Sonnet 4.6 batch : 1.50$/MTok input, 7.50$/MTok output)
    # ~3000 tokens input par video, ~1000 tokens output
    cout_input  = round(len(a_traiter) * 3000 / 1_000_000 * 1.50, 3)
    cout_output = round(len(a_traiter) * 1000 / 1_000_000 * 7.50, 3)
    cout_total  = round(cout_input + cout_output, 3)
    print("Cout estime (Batch)  : ~" + str(cout_total) + "$ (vs ~" + str(round(cout_total * 2, 3)) + "$ synchrone)")
    print("Duree estimee        : < 1h (traitement parallele)")
    print()

    # Verifier si batch precedent en attente
    state_existant = charger_state()
    if state_existant:
        print("ATTENTION : un batch precedent existe (ID: " + state_existant["batch_id"] + ")")
        print("  Relancez avec --resume pour reprendre ce batch")
        print("  OU continuez pour soumettre un NOUVEAU batch (l'ancien sera ignore)")
        print()
        rep = input("Continuer et soumettre un nouveau batch ? (oui/non) : ").strip().lower()
        if rep != "oui":
            print("  -> Relancez avec --resume pour reprendre l'ancien batch")
            sys.exit(0)
        print()

    confirmation = input("Confirmes-tu le lancement du batch ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Annule.")
        sys.exit(0)
    print()

    # Construction des requetes
    print("Construction des requetes...")
    requests, mapping = construire_requetes(a_traiter)

    if not requests:
        print("ERREUR : aucune requete construite (verifier les fichiers).")
        sys.exit(1)

    print("Requetes construites : " + str(len(requests)))

    # Soumission batch
    print("Soumission du batch...")
    try:
        batch = client.messages.batches.create(requests=requests)
    except Exception as e:
        print("ERREUR soumission : " + str(e))
        sys.exit(1)

    batch_id = batch.id
    sauvegarder_state(batch_id, mapping)
    print("Batch soumis avec succes.")

    # Polling
    batch = attendre_batch(client, batch_id)

    # Traitement des resultats
    nb_ok, nb_erreurs = traiter_resultats(client, batch_id, mapping, kb)

    # Sauvegarde KB
    print()
    print("Reconstruction aggregated_rules + sauvegarde KB...")
    rebuild_aggregated(kb)
    save_kb_atomic(kb)
    supprimer_state()

    total_regles = sum(len(v) for v in kb.get("aggregated_rules", {}).values())

    print()
    print("=" * 60)
    print("BATCH TERMINE -- OK: " + str(nb_ok) + " | Erreurs: " + str(nb_erreurs))
    print("Regles KB total : " + str(total_regles))
    if total_regles >= 800:
        print("OBJECTIF        : OK >= 800 regles atteint")
    else:
        print("OBJECTIF        : ATTENTION < 800 regles -- verifier qualite")
    print()
    print("ETAPE SUIVANTE OBLIGATOIRE (D-S39-2) :")
    print("  py 05-saas\\utils\\inject_chapter_rules.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
