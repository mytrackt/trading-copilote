"""
claude_brain.py -- Cerveau Claude de TRADEX-AI
Appel Claude API avec prompt caching (KB 4142 regles)
Circuit breaker + fallback local (max 65% confiance, Auto interdit)
"""
import os
import json
import time
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

KB_PROVISOIRE_DEFAUT = False
BANNIERE_KB_PROVISOIRE = "KB provisoire -- transcription Whisper non terminee"
SEUIL_FALLBACK = 7.0
CONFIANCE_MAX_FALLBACK = 65
FALLBACK_GRID = {
    "bgc_signal":    3.0,
    "direction_ok":  2.0,
    "vix_favorable": 2.0,
    "no_news_gate":  2.0,
    "delta_positif": 0.7,
    "big_trades_ok": 0.3,
}

try:
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
except ImportError:
    client = None
    logger.warning("Package anthropic non installe -- fallback local uniquement")

try:
    from .circuit_breaker import CB_CLAUDE, protected_call as _cb_protected_call
except ImportError:
    CB_CLAUDE = None
    _cb_protected_call = None
    logger.warning("circuit_breaker non disponible")

try:
    from .rate_limiter import RATE_LIMITER, RateLimitExceeded
except ImportError:
    RATE_LIMITER = None
    RateLimitExceeded = Exception
    logger.warning("rate_limiter non disponible")

try:
    from .data_collector_runner import load_current_phase_c
    _PHASE_C_AVAILABLE = True
except ImportError:
    _PHASE_C_AVAILABLE = False
    logger.debug("data_collector_runner non disponible (normal en test)")


def _parse_claude_json(response_text: str) -> dict:
    """Parse securise du JSON retourne par Claude."""
    text = response_text.strip()
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()
    start = text.find("{")
    end   = text.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError(f"Aucun JSON trouve dans la reponse : {text[:200]}")
    return json.loads(text[start:end])

parse_claude_json = _parse_claude_json


def call_claude_kb(kb_rules: str, god_mode_prompt: str, kb_capabilities: str = "") -> dict:
    """
    Appel Claude API avec prompt caching sur la KB.
    - Bloc 1 : KB Belkhayate (4142 regles) -- cache TTL 1h
    - Bloc 2 (optionnel) : KB Claude Capabilities (82 regles) -- cache TTL 1h
    Rate limiting : 1 appel / 10s maximum.
    """
    if client is None:
        raise RuntimeError("Client Anthropic non initialise")

    if RATE_LIMITER is not None:
        RATE_LIMITER.check_and_increment()

    def _call():
        system_blocks = [{
            "type": "text",
            "text": kb_rules,
            "cache_control": {"type": "ephemeral", "ttl": "1h"}
        }]
        if kb_capabilities:
            system_blocks.append({
                "type": "text",
                "text": kb_capabilities,
                "cache_control": {"type": "ephemeral", "ttl": "1h"}
            })

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=system_blocks,
            messages=[{"role": "user", "content": god_mode_prompt}]
        )
        time.sleep(1.5)
        logger.info(
            f"[CACHE] read={response.usage.cache_read_input_tokens} | "
            f"write={response.usage.cache_creation_input_tokens} | "
            f"input={response.usage.input_tokens}"
        )
        return _parse_claude_json(response.content[0].text)

    if CB_CLAUDE is not None and _cb_protected_call is not None:
        result = _cb_protected_call(CB_CLAUDE, _call, timeout_sec=15, retry_max=2)
        if isinstance(result, dict) and str(result.get("raison", "")).startswith("CB_FALLBACK"):
            raise RuntimeError(f"Circuit breaker declenche : {result['raison']}")
        return result
    else:
        return _call()


def _calculate_fallback_score(context: dict) -> float:
    """Score local simplifie sur /10 -- fallback uniquement, MAX 65% confiance."""
    c1 = context.get("c1", {})
    c2 = context.get("c2", {})
    vix = context.get("vix", 20)
    score = 0.0
    if c1.get("bgc_signal"):        score += FALLBACK_GRID["bgc_signal"]
    if c1.get("direction_ok"):      score += FALLBACK_GRID["direction_ok"]
    if vix < 18:                    score += FALLBACK_GRID["vix_favorable"]
    elif vix < 25:                  score += FALLBACK_GRID["vix_favorable"] / 2.0
    if context.get("no_news_gate"): score += FALLBACK_GRID["no_news_gate"]
    if c2.get("delta_positif"):     score += FALLBACK_GRID["delta_positif"]
    if c2.get("big_trades_ok"):     score += FALLBACK_GRID["big_trades_ok"]
    return round(score, 2)


def _enforce_kb_provisoire(result: dict, kb_provisoire: bool) -> dict:
    """KB provisoire -> Auto interdit + banniere sur le signal."""
    if kb_provisoire:
        result["mode_auto_autorise"] = False
        result["kb_provisoire"] = True
        result["banniere"] = BANNIERE_KB_PROVISOIRE
    return result


def load_phase_c_data() -> dict:
    """Charge les donnees Phase C (COT / Macro / News) depuis fichiers JSON existants."""
    if _PHASE_C_AVAILABLE:
        try:
            return load_current_phase_c()
        except Exception as e:
            logger.warning(f"load_phase_c_data : erreur runner -- {e}")
    return {"cot": {}, "macro": {}, "news": {}}


def load_kb_capabilities(kb_caps_path: str = None) -> str:
    """
    Charge les 82 regles prioritaires depuis KB_CLAUDE_CAPABILITIES.json.
    Categories : fiabilite_hallucinations (36) + gestion_risque_llm (46).
    Retourne str formate pour Bloc 2 prompt caching (TTL 1h).
    Si fichier introuvable : retourne "" (Bloc 2 desactive silencieusement).
    """
    if kb_caps_path is None:
        kb_caps_path = os.path.join(
            os.path.dirname(BASE_DIR), "04-cerveau-trading", "KB_CLAUDE_CAPABILITIES.json"
        )
    if not os.path.exists(kb_caps_path):
        logger.warning(f"KB Capabilities introuvable : {kb_caps_path} -- bloc 2 desactive")
        return ""

    with open(kb_caps_path, "r", encoding="utf-8") as f:
        kb_data = json.load(f)

    target_cats = {"fiabilite_hallucinations", "gestion_risque_llm"}
    aggregated = kb_data.get("aggregated_rules", {})

    text = "# KB CLAUDE CAPABILITIES -- Fiabilite & Gestion Risque LLM\n\n"
    total = 0
    for cat, rules in aggregated.items():
        if cat not in target_cats:
            continue
        text += f"## {cat.upper()}\n"
        for rule in rules:
            total += 1
            if isinstance(rule, str):
                text += f"- {rule}\n"
            elif isinstance(rule, dict):
                r = rule.get("regle", rule.get("contenu", ""))
                if r:
                    text += f"- {r}\n"
        text += "\n"

    logger.info(f"KB Capabilities chargee : {total} regles (fiabilite_hallucinations + gestion_risque_llm)")
    return text


def get_signal(context: dict, kb_rules: str, kb_provisoire: bool = KB_PROVISOIRE_DEFAUT,
               phase_c_data: dict = None, kb_capabilities: str = "") -> dict:
    """
    Point d'entree principal.
    1. Construit le prompt GOD_MODE
    2. Appelle Claude avec KB en cache (Bloc 1 Belkhayate + Bloc 2 Capabilities)
    3. En cas d'echec : fallback local /10 (max 65%, Auto bloque)

    kb_capabilities (optionnel) : str pre-charge depuis KB_CLAUDE_CAPABILITIES.json
      -> si vide : auto-charge (82 regles : fiabilite_hallucinations + gestion_risque_llm)
      -> passer explicitement pour eviter une relecture disque a chaque appel
    """
    try:
        ctx_enrichi = dict(context)
        if phase_c_data is not None:
            ctx_enrichi["phase_c"] = phase_c_data
        elif "phase_c" not in ctx_enrichi:
            ctx_enrichi["phase_c"] = {"cot": {}, "macro": {}, "news": {}}

        from .prompt_builder import build_god_mode_prompt
        prompt = build_god_mode_prompt(ctx_enrichi)

        # Charger KB Capabilities si non fournie (82 regles : fiabilite_hallucinations + gestion_risque_llm)
        kb_caps = kb_capabilities if kb_capabilities else load_kb_capabilities()
        result = call_claude_kb(kb_rules, prompt, kb_capabilities=kb_caps)

        result.setdefault("signal", "ATTENDRE")
        result.setdefault("confiance", 0)
        result.setdefault("raison", "")
        result.setdefault("taille_contrats", 1)
        result.setdefault("mode_auto_autorise", False)

    except Exception as e:
        logger.error(f"Claude API indisponible : {e}")
        score = _calculate_fallback_score(context)
        dd = context.get("risk", {}).get("dd_today", 0.0)

        if score >= SEUIL_FALLBACK and dd < 0.02:
            direction = context.get("c1", {}).get("direction", "ATTENDRE")
            confiance = min(round(score / 10.0 * CONFIANCE_MAX_FALLBACK), CONFIANCE_MAX_FALLBACK)
            result = {
                "signal":             direction,
                "confiance":          confiance,
                "raison":             "FALLBACK_LOCAL -- score suffisant (/10)",
                "taille":             "mini",
                "taille_contrats":    1,
                "mode_auto_autorise": False,
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
    """
    if kb_path is None:
        kb_path = os.path.join(os.path.dirname(BASE_DIR), "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")

    if not os.path.exists(kb_path):
        logger.warning(f"KB introuvable : {kb_path} -- fallback vide")
        rules_text = "Tu es TRADEX-AI, assistant trading Belkhayate. KB non chargee."
    else:
        with open(kb_path, "r", encoding="utf-8") as f:
            kb_data = json.load(f)
        aggregated = kb_data.get("aggregated_rules", {})
        total = sum(len(v) for v in aggregated.values())
        rules_text = "# KNOWLEDGE BASE TRADEX-AI -- Methode Belkhayate\n\n"
        rules_text += f"Total regles : {total}\n\n"
        for categorie, briques in aggregated.items():
            rules_text += f"## {categorie.upper()}\n"
            for rule in briques:
                if isinstance(rule, str):
                    rules_text += f"- {rule}\n"
                elif isinstance(rule, dict):
                    if rule.get("id"):
                        titre = rule.get("titre", rule.get("id", ""))
                        corps = rule.get("contenu", "")
                        rules_text += f"### {titre}\n{corps}\n\n"
                    else:
                        regle = rule.get("regle", "")
                        if regle:
                            rules_text += f"- {regle}\n"
            rules_text += "\n"
        logger.info(f"KB chargee : {total} regles depuis {kb_path}")

    banniere = BANNIERE_KB_PROVISOIRE if kb_provisoire else None
    return {
        "rules":         rules_text,
        "kb_provisoire": kb_provisoire,
        "banniere":      banniere,
    }
