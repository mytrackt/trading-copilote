"""
claude_brain.py — Cerveau Claude de TRADEX-AI
Appel Claude API avec prompt caching (KB 2337 règles)
Circuit breaker + fallback local (max 65% confiance, Auto interdit)
"""
import os
import json
import time
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

# --- A5 (Phase 6) : KB provisoire + bareme fallback aligne /10 ---
KB_PROVISOIRE_DEFAUT = True
BANNIERE_KB_PROVISOIRE = "KB provisoire -- transcription Whisper non terminee"
SEUIL_FALLBACK = 7.0            # aligne sur signal_engine.SEUIL_SIGNAL (/10)
CONFIANCE_MAX_FALLBACK = 65     # plafond confiance fallback ; Auto toujours interdit
# Bareme fallback local sur /10 (mirror partiel de signal_engine.SCORE_GRID). N'utilise PAS l'Energie (non codee).
FALLBACK_GRID = {
    "bgc_signal":    3.0,
    "direction_ok":  2.0,
    "vix_favorable": 2.0,
    "no_news_gate":  2.0,
    "delta_positif": 0.7,
    "big_trades_ok": 0.3,
}

# Client Anthropic — clé via variable d'environnement UNIQUEMENT
try:
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
except ImportError:
    client = None
    logger.warning("Package anthropic non installé — fallback local uniquement")

# Import circuit breaker
try:
    from .circuit_breaker import CB_CLAUDE
except ImportError:
    CB_CLAUDE = None
    logger.warning("circuit_breaker non disponible")


def _parse_claude_json(response_text: str) -> dict:
    """
    Parse sécurisé du JSON retourné par Claude.
    Ne jamais appeler json.loads() directement sur une réponse Claude.
    """
    text = response_text.strip()
    # Extraire le bloc JSON si Claude a ajouté du texte autour
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()
    # Trouver le premier { et le dernier }
    start = text.find("{")
    end   = text.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError(f"Aucun JSON trouvé dans la réponse : {text[:200]}")
    return json.loads(text[start:end])


# Nom public : toute reponse Claude passe par ici (jamais json.loads direct dessus).
parse_claude_json = _parse_claude_json


def call_claude_kb(kb_rules: str, god_mode_prompt: str) -> dict:
    """
    Appel Claude API avec prompt caching sur la KB.
    Le system (KB 2337 règles) est mis en cache → ~90% d'économies tokens.
    Rate limiting : 1 appel / 10s maximum.
    """
    if client is None:
        raise RuntimeError("Client Anthropic non initialisé")

    def _call():
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=[{
                "type": "text",
                "text": kb_rules,
                "cache_control": {"type": "persistent"}   # Prompt caching
            }],
            messages=[{
                "role": "user",
                "content": god_mode_prompt
            }]
        )
        time.sleep(1.5)  # Rate limiting inter-appels
        return _parse_claude_json(response.content[0].text)

    if CB_CLAUDE is not None:
        return CB_CLAUDE.call(_call)
    else:
        return _call()


def _calculate_fallback_score(context: dict) -> float:
    """
    Score local simplifie sur /10 (sans Claude, SANS Energie -- non codee).
    Utilise UNIQUEMENT en fallback (Claude API indisponible). Approximation degradee ;
    le score deterministe autoritaire reste celui de signal_engine. MAX 65% confiance ensuite.
    """
    c1 = context.get("c1", {})
    c2 = context.get("c2", {})
    vix = context.get("vix", 20)

    score = 0.0
    if c1.get("bgc_signal"):    score += FALLBACK_GRID["bgc_signal"]    # C1 -- COG/BGC aligne
    if c1.get("direction_ok"):  score += FALLBACK_GRID["direction_ok"]  # C1 -- direction
    if vix < 18:                score += FALLBACK_GRID["vix_favorable"]  # C5 -- VIX bas
    elif vix < 25:              score += FALLBACK_GRID["vix_favorable"] / 2.0
    if context.get("no_news_gate"): score += FALLBACK_GRID["no_news_gate"]  # C4 -- pas de news
    if c2.get("delta_positif"): score += FALLBACK_GRID["delta_positif"]  # C2 -- order flow
    if c2.get("big_trades_ok"): score += FALLBACK_GRID["big_trades_ok"]  # C2

    return round(score, 2)  # /10 max (= 10.0)


def _enforce_kb_provisoire(result: dict, kb_provisoire: bool) -> dict:
    """KB provisoire -> Auto interdit + banniere sur le signal.
    Aucun signal reel ne s'appuie sur la KB provisoire (transcription Whisper non terminee)."""
    if kb_provisoire:
        result["mode_auto_autorise"] = False
        result["kb_provisoire"] = True
        result["banniere"] = BANNIERE_KB_PROVISOIRE
    return result


def get_signal(context: dict, kb_rules: str, kb_provisoire: bool = KB_PROVISOIRE_DEFAUT) -> dict:
    """
    Point d'entrée principal.
    1. Construit le prompt GOD_MODE
    2. Appelle Claude avec la KB en cache
    3. En cas d'échec → fallback local /10 (max 65%, Auto bloqué)

    Si kb_provisoire=True (defaut tant que la KB Whisper n'est pas reconstruite) :
    Auto interdit + banniere « KB provisoire » sur CHAQUE signal retourne.

    context = {
        "c1": {"bgc_signal": bool, "direction": "LONG"|"SHORT", "direction_ok": bool, ...},
        "c2": {"delta_positif": bool, "big_trades_ok": bool},
        "risk": {"dd_today": float, "dd_week": float},
        "vix": float, "no_news_gate": bool, "actif": str, "timeframe": str,
    }
    """
    try:
        from .prompt_builder import build_god_mode_prompt
        prompt = build_god_mode_prompt(context)
        result = call_claude_kb(kb_rules, prompt)
        # S'assurer que le résultat a tous les champs obligatoires
        result.setdefault("signal", "ATTENDRE")
        result.setdefault("confiance", 0)
        result.setdefault("raison", "")
        result.setdefault("taille_contrats", 1)
        result.setdefault("mode_auto_autorise", False)

    except Exception as e:
        logger.error(f"Claude API indisponible : {e}")
        score = _calculate_fallback_score(context)            # /10
        dd = context.get("risk", {}).get("dd_today", 0.0)

        # Fallback : score >= 7.0 (aligne signal_engine) ET DD < 2% -> signal local possible
        if score >= SEUIL_FALLBACK and dd < 0.02:
            direction = context.get("c1", {}).get("direction", "ATTENDRE")
            confiance = min(round(score / 10.0 * CONFIANCE_MAX_FALLBACK), CONFIANCE_MAX_FALLBACK)
            result = {
                "signal":             direction,
                "confiance":          confiance,           # JAMAIS > 65% en fallback
                "raison":             "FALLBACK_LOCAL -- score suffisant (/10)",
                "taille":             "mini",
                "taille_contrats":    1,
                "mode_auto_autorise": False,               # Auto TOUJOURS bloque en fallback
                "score_fallback":     score,
                "alerte":             f"Claude API indisponible : {str(e)[:100]}",
            }
        else:
            result = {
                "signal":             "ATTENDRE",
                "confiance":          0,
                "raison":             f"FALLBACK_LOCAL -- score {score}/10 insuffisant",
                "taille_contrats":    0,
                "mode_auto_autorise": False,
                "score_fallback":     score,
                "alerte":             f"Claude API indisponible + conditions KO : {str(e)[:80]}",
            }

    return _enforce_kb_provisoire(result, kb_provisoire)


def load_kb_rules(kb_path: str = None, kb_provisoire: bool = KB_PROVISOIRE_DEFAUT) -> dict:
    """
    Charge la Knowledge Base Belkhayate depuis le fichier JSON.
    Renvoie {rules: str, kb_provisoire: bool, banniere: str|None}.

    kb_provisoire=True tant que la KB n'a pas ete reconstruite a partir des VRAIS transcripts
    Whisper (la KB actuelle = syntheses NotebookLM, invalide). Dans ce cas : mode Auto interdit
    et banniere affichee (enforce par get_signal / _enforce_kb_provisoire).
    """
    if kb_path is None:
        kb_path = os.path.join(os.path.dirname(BASE_DIR), "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")

    if not os.path.exists(kb_path):
        logger.warning(f"KB introuvable : {kb_path} -- fallback vide")
        rules_text = "Tu es TRADEX-AI, assistant trading Belkhayate. KB non chargee."
    else:
        with open(kb_path, "r", encoding="utf-8") as f:
            kb_data = json.load(f)
        rules_text = "# KNOWLEDGE BASE TRADEX-AI -- Methode Belkhayate\n\n"
        rules_text += f"Total regles : {len(kb_data.get('rules', []))}\n\n"
        for rule in kb_data.get("rules", []):
            rules_text += f"## {rule.get('categorie', 'GENERAL')}\n"
            rules_text += f"{rule.get('contenu', '')}\n\n"

    return {
        "rules": rules_text,
        "kb_provisoire": kb_provisoire,
        "banniere": BANNIERE_KB_PROVISOIRE if kb_provisoire else None,
    }
