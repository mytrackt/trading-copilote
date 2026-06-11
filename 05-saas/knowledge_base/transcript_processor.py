"""
transcript_processor.py
Pipeline d'extraction des regles Belkhayate depuis les transcripts Whisper.

Etapes :
  1. Charge KNOWLEDGE_BASE_MASTER.json existant (skip videos deja traitees)
  2. Lit chaque whisper_*.txt depuis 04-kb-sources/youtube-a-scraper/transcripts/
  3. Envoie chaque transcript a Claude Haiku 4.5
  4. Extrait 11 categories de regles en JSON strict
  5. Sauvegarde atomiquement la KB apres CHAQUE video (relancable sans perte)
  6. Rate limit 1.5s entre chaque appel API

Usage :
  set ANTHROPIC_API_KEY="sk-ant-..."
  python -m py_compile transcript_processor.py
  python transcript_processor.py
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("ERREUR : module 'anthropic' manquant. Installe-le :")
    print("  pip install anthropic")
    sys.exit(1)

# Optionnel : .env si python-dotenv installe
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

# --- Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # C:\trading-copilote\
TRANSCRIPTS_DIR = PROJECT_ROOT / "03-transcriptions" / "transcripts-bruts"
KB_DIR = PROJECT_ROOT / "04-cerveau-trading"
KB_FILE = KB_DIR / "KNOWLEDGE_BASE_MASTER.json"
KB_TMP_FILE = KB_DIR / "KNOWLEDGE_BASE_MASTER.json.tmp"
LOG_FILE = KB_DIR / "processor_status.json"

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 4096
RATE_LIMIT_SECONDS = 1.5
MAX_TRANSCRIPT_CHARS = 60000  # garde-fou cout (env. 15k tokens)

CATEGORIES = [
    "saisonnalite",
    "correlations",
    "timing",
    "indicateurs_tendance",
    "indicateurs_momentum",
    "gestion_risque_entree",
    "gestion_position_active",
    "structure_marche",
    "macro_evenements",
    "volume_liquidite",
    "psychologie",
]

SYSTEM_PROMPT = """Tu es un analyste expert de la methode de trading Belkhayate.
On te donne le transcript d'une video de Mostafa Belkhayate.
Ta mission : extraire UNIQUEMENT les regles, principes et observations concrets et actionnables que Belkhayate enonce.

Categories autorisees (exactement ces 11 cles, aucune autre) :
- saisonnalite : effets calendaires, mois/jours/heures favorables ou non
- correlations : liens entre actifs (Or/Dollar, Petrole/Cuivre, SP500/VIX, etc.)
- timing : moments d'entree/sortie, sessions, ouverture/cloture
- indicateurs_tendance : Barycenter, Direction, pivots Sol/Fa/Mi/Re/Do, MM, supports/resistances
- indicateurs_momentum : Belkhayate Energie, RSI, MACD, divergences
- gestion_risque_entree : taille de position, stop loss, ratio R/R, regles 3/4 + 2/3
- gestion_position_active : trailing stop, scaling out, prises de benefices partielles
- structure_marche : zones d'accumulation/distribution, ranges, breakouts, faux signaux
- macro_evenements : NFP, FOMC, CPI, banques centrales, geopolitique
- volume_liquidite : volume confirmant, divergences volume/prix, liquidite sessions
- psychologie : discipline, patience, biais cognitifs, gestion emotions

REGLES STRICTES :
1. Une regle = une phrase courte, autoporteuse, en francais.
2. Si rien dans une categorie : tableau vide [].
3. Pas d'invention. Si Belkhayate ne le dit pas, ne l'ecris pas.
4. Pas de marketing, pas de promo, pas de "abonnez-vous".
5. Tu reponds UNIQUEMENT en JSON valide, sans texte avant ni apres, sans backticks.

Format de sortie EXACT :
{
  "saisonnalite": ["regle 1", "regle 2"],
  "correlations": [],
  "timing": [],
  "indicateurs_tendance": [],
  "indicateurs_momentum": [],
  "gestion_risque_entree": [],
  "gestion_position_active": [],
  "structure_marche": [],
  "macro_evenements": [],
  "volume_liquidite": [],
  "psychologie": []
}"""


def get_anthropic_client() -> Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERREUR : variable d'environnement ANTHROPIC_API_KEY non definie.")
        print("Definis-la dans PowerShell :")
        print('  setx ANTHROPIC_API_KEY "sk-ant-..."')
        print("Puis ouvre une nouvelle fenetre PowerShell.")
        sys.exit(1)
    return Anthropic(api_key=api_key)


def empty_rules() -> dict:
    return {cat: [] for cat in CATEGORIES}


def load_kb() -> dict:
    """Charge la KB master existante ou cree une structure vierge."""
    if KB_FILE.exists():
        with open(KB_FILE, "r", encoding="utf-8") as f:
            kb = json.load(f)
        # Defensif : verifier la structure minimale
        kb.setdefault("metadata", {})
        kb.setdefault("videos", {})
        kb.setdefault("aggregated_rules", empty_rules())
        return kb
    return {
        "metadata": {
            "version": "1.0",
            "model": MODEL,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "categories": CATEGORIES,
        },
        "videos": {},
        "aggregated_rules": empty_rules(),
    }


def save_kb_atomic(kb: dict) -> None:
    """Ecrit dans .tmp puis renomme : aucune corruption si crash."""
    kb["metadata"]["last_updated"] = datetime.utcnow().isoformat() + "Z"
    with open(KB_TMP_FILE, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2, ensure_ascii=False)
    os.replace(KB_TMP_FILE, KB_FILE)


def append_log(entry: dict) -> None:
    """Append-only log pour auditer succes/echecs."""
    logs = []
    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def list_transcripts() -> list[Path]:
    """Liste tous les transcripts whisper_*.txt non vides."""
    if not TRANSCRIPTS_DIR.exists():
        print(f"ERREUR : dossier introuvable : {TRANSCRIPTS_DIR}")
        sys.exit(1)
    files = sorted(TRANSCRIPTS_DIR.glob("whisper_*.txt"))
    return [f for f in files if f.stat().st_size > 0]


def extract_video_id(filename: str) -> str:
    """whisper_ABC123.txt -> ABC123"""
    match = re.match(r"^whisper_(.+)\.txt$", filename)
    if not match:
        raise ValueError(f"Nom de fichier inattendu : {filename}")
    return match.group(1)


def parse_json_response(raw: str) -> dict | None:
    """Parse la reponse Claude. Tolere du bruit autour du JSON."""
    raw = raw.strip()
    # Tentative directe
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    # Extraction du premier objet { ... } equilibre
    start = raw.find("{")
    if start == -1:
        return None
    depth = 0
    for i in range(start, len(raw)):
        if raw[i] == "{":
            depth += 1
        elif raw[i] == "}":
            depth -= 1
            if depth == 0:
                candidate = raw[start:i + 1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    return None
    return None


def normalize_rules(parsed: dict) -> dict:
    """Garantit les 11 cles, listes de strings non vides uniquement."""
    out = empty_rules()
    if not isinstance(parsed, dict):
        return out
    for cat in CATEGORIES:
        value = parsed.get(cat, [])
        if isinstance(value, list):
            out[cat] = [str(item).strip() for item in value if isinstance(item, (str, int, float)) and str(item).strip()]
    return out


def call_claude(client: Anthropic, transcript: str, video_id: str) -> dict | None:
    """Appelle Claude Haiku et retourne les regles normalisees, ou None si echec."""
    if len(transcript) > MAX_TRANSCRIPT_CHARS:
        print(f"  Tronque {len(transcript)} -> {MAX_TRANSCRIPT_CHARS} caracteres")
        transcript = transcript[:MAX_TRANSCRIPT_CHARS]

    user_prompt = (
        f"Transcript de la video YouTube (id={video_id}) :\n\n"
        f"<<<TRANSCRIPT>>>\n{transcript}\n<<<FIN_TRANSCRIPT>>>\n\n"
        "Extrais maintenant les regles Belkhayate au format JSON specifie."
    )

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as e:
        print(f"  ECHEC API : {e}")
        return None

    if not response.content:
        print("  Reponse vide")
        return None

    raw = response.content[0].text
    parsed = parse_json_response(raw)
    if parsed is None:
        print(f"  JSON invalide. Debut reponse : {raw[:200]!r}")
        return None

    return normalize_rules(parsed)


def rebuild_aggregated(kb: dict) -> None:
    """Recalcule aggregated_rules depuis toutes les videos (deduplique)."""
    agg = empty_rules()
    seen = {cat: set() for cat in CATEGORIES}
    for vid in kb["videos"].values():
        rules = vid.get("rules", {})
        for cat in CATEGORIES:
            for rule in rules.get(cat, []):
                key = rule.lower().strip()
                if key and key not in seen[cat]:
                    seen[cat].add(key)
                    agg[cat].append(rule)
    kb["aggregated_rules"] = agg


def main() -> int:
    print("=" * 60)
    print("Transcript Processor - Belkhayate Knowledge Base")
    print("=" * 60)
    print(f"Transcripts source : {TRANSCRIPTS_DIR}")
    print(f"KB cible           : {KB_FILE}")
    print(f"Modele             : {MODEL}")
    print(f"Rate limit         : {RATE_LIMIT_SECONDS}s")
    print("-" * 60)

    client = get_anthropic_client()
    kb = load_kb()
    transcripts = list_transcripts()
    total = len(transcripts)
    if total == 0:
        print("Aucun transcript whisper_*.txt trouve. Stop.")
        return 0

    already_done = set(kb["videos"].keys())
    to_do = [f for f in transcripts if extract_video_id(f.name) not in already_done]

    print(f"Total transcripts        : {total}")
    print(f"Deja traites (skip)      : {total - len(to_do)}")
    print(f"A traiter dans cette run : {len(to_do)}")
    print("-" * 60)

    success = 0
    failed = 0

    for idx, transcript_path in enumerate(to_do, 1):
        video_id = extract_video_id(transcript_path.name)
        print(f"[{idx}/{len(to_do)}] {video_id}")

        with open(transcript_path, "r", encoding="utf-8") as f:
            transcript = f.read()

        if len(transcript.strip()) < 100:
            print("  Transcript trop court, skip")
            append_log({
                "video_id": video_id,
                "status": "skipped_too_short",
                "chars": len(transcript),
                "timestamp": datetime.utcnow().isoformat() + "Z",
            })
            continue

        rules = call_claude(client, transcript, video_id)

        if rules is None:
            failed += 1
            append_log({
                "video_id": video_id,
                "status": "failed",
                "timestamp": datetime.utcnow().isoformat() + "Z",
            })
            time.sleep(RATE_LIMIT_SECONDS)
            continue

        kb["videos"][video_id] = {
            "video_id": video_id,
            "transcript_file": transcript_path.name,
            "transcript_chars": len(transcript),
            "model": MODEL,
            "processed_at": datetime.utcnow().isoformat() + "Z",
            "rules": rules,
        }
        rebuild_aggregated(kb)
        save_kb_atomic(kb)

        n_rules = sum(len(v) for v in rules.values())
        success += 1
        print(f"  OK ({n_rules} regles extraites)")
        append_log({
            "video_id": video_id,
            "status": "success",
            "rules_count": n_rules,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        })

        if idx < len(to_do):
            time.sleep(RATE_LIMIT_SECONDS)

    print("-" * 60)
    print(f"TERMINE : {success} succes / {failed} echecs")
    print(f"KB sauvegardee : {KB_FILE}")
    print(f"Total videos en KB : {len(kb['videos'])}")
    total_rules = sum(len(v) for v in kb["aggregated_rules"].values())
    print(f"Total regles agregees (deduplique) : {total_rules}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
