"""
prompt_builder.py -- Constructeur du prompt GOD_MODE pour Claude API
TRADEX-AI Phase C -- Injecte le contexte NT8 + données externes (COT/Macro/News)

Format de sortie attendu de Claude (JSON 15 champs) :
{
  "signal": "LONG|SHORT|ATTENDRE",
  "confiance": 0-100,
  "raison": "...",
  "taille": "mini|standard|grande",
  "taille_contrats": 1,
  "stop_loss": float|null,
  "take_profit": float|null,
  "mode_auto_autorise": false,
  "alerte": "...",
  "score_kb": float,
  "timing_belkhayate": "...",
  "bandes_belkhayate": "...",
  "cot_contexte": "...",
  "macro_contexte": "...",
  "news_contexte": "..."
}
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _fmt_cot(cot: dict) -> str:
    """Résumé COT compact pour le prompt (évite les blocs JSON bruts)."""
    if not cot:
        return "COT : données non disponibles."
    lines = []
    for actif in ("GC", "HG", "CL", "ZW"):
        info = cot.get(actif)
        if not isinstance(info, dict):
            continue
        if not info.get("disponible"):
            lines.append(f"  {actif}: indisponible")
            continue
        longs = info.get("net_longs_commerciaux")
        trend = info.get("trend_net_longs")
        age = info.get("age_jours")
        warn = " ⚠️ données >7j" if info.get("staleness_warning") else ""
        lines.append(
            f"  {actif}: net_longs_commerciaux={longs} | trend={trend} | "
            f"age={age}j{warn}"
        )
    collected = cot.get("_collected_at", "")[:10]
    if lines:
        return "COT CFTC (positions commerciaux, indicateur contrarian) :\n" + "\n".join(lines) + f"\n  [collecté: {collected}]"
    return "COT : données non disponibles."


def _fmt_macro(macro: dict) -> str:
    """Résumé macro FRED/EIA compact."""
    if not macro:
        return "MACRO : données non disponibles."
    parts = []
    if macro.get("treasury_10y") is not None:
        parts.append(f"T10Y={macro['treasury_10y']:.2f}%")
    if macro.get("fed_funds_rate") is not None:
        parts.append(f"FedFunds={macro['fed_funds_rate']:.2f}%")
    if macro.get("dtwexbgs_broad") is not None:
        parts.append(f"Dollar_TWI={macro['dtwexbgs_broad']:.1f} (panier large, ≠DXY)")
    if macro.get("inflation_expectation_5y") is not None:
        parts.append(f"Inflation5Y={macro['inflation_expectation_5y']:.2f}%")
    if macro.get("crude_inventory_barils") is not None:
        inv = macro["crude_inventory_barils"]
        parts.append(f"CrudeInventory={inv:.0f}k_barils_hors_SPR")
    collected = macro.get("_collected_at", "")[:10]
    if parts:
        return "MACRO (FRED/EIA) :\n  " + " | ".join(parts) + f"\n  [collecté: {collected}]"
    return "MACRO : données non disponibles."


def _fmt_news(news: dict) -> str:
    """Résumé news et news gate."""
    if not news:
        return "NEWS : données non disponibles."
    gate_events = news.get("news_gate_events", [])
    count = news.get("count", 0)
    finnhub_ok = news.get("finnhub_disponible", False)
    gdelt_ok = news.get("gdelt_disponible", False)
    sources = []
    if finnhub_ok:
        sources.append("Finnhub")
    if gdelt_ok:
        sources.append("GDELT")
    src_str = "/".join(sources) if sources else "aucune source disponible"
    collected = news.get("_collected_at", "")[:16].replace("T", " ")

    lines = [f"NEWS ({src_str}) : {count} articles récents [collecté: {collected}]"]
    if gate_events:
        lines.append(f"  ⚠️ NEWS GATE ACTIF — événements détectés : {', '.join(gate_events)}")
        lines.append("  → Entrée INTERDITE 30min avant / 15min après chaque événement.")
    else:
        lines.append("  ✅ Aucun événement NFP/FOMC/CPI/GDP/PPI détecté — zone libre.")
    # Extraire titres d'articles si présents (max 3)
    articles = news.get("articles", [])
    if articles:
        lines.append("  Titres récents :")
        for art in articles[:3]:
            titre = art.get("titre", art.get("headline", ""))
            if titre:
                lines.append(f"    - {titre[:120]}")
    return "\n".join(lines)


def build_god_mode_prompt(context: dict) -> str:
    """
    Construit le prompt GOD_MODE complet envoyé à Claude.

    context = {
        "actif"       : str  (ex: "GC"),
        "timeframe"   : str  (ex: "H1"),
        "c1"          : {bgc_signal, direction, direction_ok, timing, ...},
        "c2"          : {delta_positif, big_trades_ok, ...},
        "risk"        : {dd_today, dd_week},
        "vix"         : float,
        "no_news_gate": bool,
        "phase_c"     : {cot, macro, news},   # optionnel
    }

    Retourne une chaîne de caractères (le message user envoyé à Claude API).
    """
    actif       = context.get("actif", "INCONNU")
    timeframe   = context.get("timeframe", "H1")
    c1          = context.get("c1", {})
    c2          = context.get("c2", {})
    risk        = context.get("risk", {})
    vix         = context.get("vix", 0.0)
    no_news_gate = context.get("no_news_gate", True)
    phase_c     = context.get("phase_c", {})

    cot_data    = phase_c.get("cot", {})
    macro_data  = phase_c.get("macro", {})
    news_data   = phase_c.get("news", {})

    # --- Section NT8 (données temps réel) ---
    direction   = c1.get("direction", "INDÉFINI")
    bgc_signal  = "✅ OUI" if c1.get("bgc_signal") else "❌ NON"
    dir_ok      = "✅ OUI" if c1.get("direction_ok") else "❌ NON"
    timing_val  = c1.get("timing", "N/A")
    delta_pos   = "✅ OUI" if c2.get("delta_positif") else "❌ NON"
    big_trades  = "✅ OUI" if c2.get("big_trades_ok") else "❌ NON"
    dd_today    = risk.get("dd_today", 0.0)
    dd_week     = risk.get("dd_week", 0.0)
    news_ok     = "✅ LIBRE" if no_news_gate else "⚠️ NEWS GATE ACTIF"

    cot_section   = _fmt_cot(cot_data)
    macro_section = _fmt_macro(macro_data)
    news_section  = _fmt_news(news_data)

    prompt = f"""Tu es TRADEX-AI, analyste expert de la méthode Belkhayate.
Utilise ta Knowledge Base (KB) pour analyser le contexte ci-dessous et produire un signal de trading.

============================================================
CONTEXTE MARCHÉ — {actif} / {timeframe}
============================================================

## SIGNAUX NT8 (temps réel)
- Actif analysé    : {actif}
- Timeframe        : {timeframe}
- Direction COG/BGC: {direction}
- BGC signal actif : {bgc_signal}
- Direction OK     : {dir_ok}
- Timing Belkhayate: {timing_val}
- Delta positif    : {delta_pos}
- Big trades OK    : {big_trades}
- VIX              : {vix:.1f}
- News Gate        : {news_ok}
- Drawdown today   : {dd_today*100:.2f}%
- Drawdown week    : {dd_week*100:.2f}%

## DONNÉES EXTERNES (Phase C)

{cot_section}

{macro_section}

{news_section}

============================================================
INSTRUCTION
============================================================

Analyse CE contexte précis avec la KB Belkhayate.
Produis un JSON STRICT avec exactement ces 15 champs :

{{
  "signal"            : "LONG" | "SHORT" | "ATTENDRE",
  "confiance"         : 0-100,
  "raison"            : "explication courte (max 120 car)",
  "taille"            : "mini" | "standard" | "grande",
  "taille_contrats"   : 1,
  "stop_loss"         : float | null,
  "take_profit"       : float | null,
  "mode_auto_autorise": false,
  "alerte"            : "avertissement important ou chaîne vide",
  "score_kb"          : 0.0-10.0,
  "timing_belkhayate" : "résumé timing KB",
  "bandes_belkhayate" : "résumé bandes KB",
  "cot_contexte"      : "interprétation COT (1 phrase)",
  "macro_contexte"    : "interprétation macro (1 phrase)",
  "news_contexte"     : "interprétation news/gate (1 phrase)"
}}

RÈGLES ABSOLUES :
1. mode_auto_autorise = false TOUJOURS (mode Auto bloqué par défaut).
2. Si News Gate actif → signal = "ATTENDRE", confiance = 0.
3. Si drawdown_today >= 2% → signal = "ATTENDRE".
4. Si score_kb < 7.0 → signal = "ATTENDRE".
5. Ne jamais inventer de données non présentes dans ce contexte.
6. Répondre UNIQUEMENT avec le JSON, sans texte avant ni après.
"""
    return prompt
