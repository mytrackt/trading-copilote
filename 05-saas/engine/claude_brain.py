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


def _calculate_fallback_score(context: dict) -> int:
    """
    Score local simplifié 7 cercles (sans Claude).
    Utilisé uniquement en fallback — MAX 65% confiance.
    """
    score = 0

    # C1 — Prix Belkhayate
    c1 = context.get("c1", {})
    if c1.get("bgc_signal"):   score += 3
    if c1.get("direction_ok"): score += 2
    if c1.get("energie_ok"):   score += 1

    # C5 — VIX sentiment
    vix = context.get("vix", 20)
    if vix < 18:  score += 2
    elif vix < 25: score += 1

    # C4 — Macro
    if context.get("no_news_gate"): score += 2

    # C2 — Order Flow
    c2 = context.get("c2", {})
    if c2.get("delta_positif"): score += 2
    if c2.get("big_trades_ok"): score += 1

    return score  # /21 points max


def get_signal(context: dict, kb_rules: str) -> dict:
    """
    Point d'entrée principal.
    1. Construit le prompt GOD_MODE
    2. Appelle Claude avec la KB en cache
    3. En cas d'échec → fallback local (max 65%, Auto bloqué)

    context = {
        "c1": {"bgc_signal": bool, "direction": "LONG"|"SHORT", ...},
        "c2": {"delta_positif": bool, "big_trades_ok": bool},
        "risk": {"dd_today": float, "dd_week": float},
        "vix": float,
        "no_news_gate": bool,
        "actif": str,
        "timeframe": str,
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
        return result

    except Exception as e:
        logger.error(f"Claude API indisponible : {e}")
        score = _calculate_fallback_score(context)
        risk  = context.get("risk", {})
        dd    = risk.get("dd_today", 0.0)

        # Fallback : score >= 17 ET DD < 2% → signal local possible
        if score >= 17 and dd < 0.02:
            direction = context.get("c1", {}).get("direction", "ATTENDRE")
            confiance = min(score * 3, 65)  # JAMAIS > 65% en fallback
            return {
                "signal":           direction,
                "confiance":        confiance,
                "raison":           "FALLBACK_LOCAL — score suffisant",
                "taille":           "mini",
                "taille_contrats":  1,
                "mode_auto_autorise": False,   # Auto TOUJOURS bloqué en fallback
                "alerte":           f"Claude API indisponible : {str(e)[:100]}"
            }

        # Conditions insuffisantes → ATTENDRE obligatoire
        return {
            "signal":           "ATTENDRE",
            "confiance":        0,
            "raison":           f"FALLBACK_LOCAL — score {score}/21 insuffisant",
            "taille_contrats":  0,
            "mode_auto_autorise": False,
            "alerte":           f"Claude API indisponible + conditions KO : {str(e)[:80]}"
        }


def load_kb_rules(kb_path: str = None) -> str:
    """
    Charge la Knowledge Base Belkhayate (2337 règles) depuis le fichier JSON.
    Retourne une chaîne formatée pour le system prompt Claude.
    """
    if kb_path is None:
        kb_path = os.path.join(os.path.dirname(BASE_DIR), "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")

    if not os.path.exists(kb_path):
        logger.warning(f"KB introuvable : {kb_path} — utiliser fallback vide")
        return "Tu es TRADEX-AI, assistant trading Belkhayate. KB non chargée."

    with open(kb_path, "r", encoding="utf-8") as f:
        kb_data = json.load(f)

    # Formater les règles pour le system prompt
    rules_text = "# KNOWLEDGE BASE TRADEX-AI — Méthode Belkhayate\n\n"
    rules_text += f"Total règles : {len(kb_data.get('rules', []))}\n\n"
    for rule in kb_data.get("rules", []):
        rules_text += f"## {rule.get('categorie', 'GENERAL')}\n"
        rules_text += f"{rule.get('contenu', '')}\n\n"

    return rules_text
