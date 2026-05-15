# -*- coding: utf-8 -*-
"""
video_filter.py
Filtre les vidéos trading par mots-clés et durée.
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\video_filter.py
"""

TRADING_KEYWORDS = [
    # Indicateurs techniques
    "ema", "rsi", "macd", "bollinger", "stochastique", "stochastic",
    "ichimoku", "moyenne mobile", "moving average", "fibonacci", "atr",
    # Stratégies
    "scalping", "swing", "day trading", "price action", "setup",
    "strategie", "stratégie", "strategy", "configuration", "methode",
    # Patterns
    "cassure", "breakout", "divergence", "croisement", "crossover",
    "support", "resistance", "résistance", "tendance", "trend",
    "retracement", "canal", "channel",
    # Bougies
    "heikin", "candlestick", "bougie", "marubozu", "doji", "engulfing",
    # Gestion risque
    "stop loss", "take profit", "risk reward", "ratio",
    # Analyse
    "analyse technique", "technical analysis", "signal", "entree",
    "forex", "crypto", "indices", "futures", "cac", "nasdaq",
    # Méthodes spécifiques TRADEX-AI
    "belkhayate", "ict", "smart money", "wyckoff", "elliott", "vwap",
    "order block", "fair value gap", "fvg", "liquidity",
]

DURATION_MIN_SEC = 3 * 60    # 3 minutes
DURATION_MAX_SEC = 50 * 60   # 50 minutes


def is_trading_video(video: dict) -> tuple:
    """
    Évalue si une vidéo est une vidéo de trading.

    Returns:
        (bool, str) — (acceptée, raison)
    """
    title = (video.get("title") or "").lower()
    description = (video.get("description") or "").lower()
    duration = video.get("duration") or 0

    # Filtre durée
    if duration > 0:
        if duration < DURATION_MIN_SEC:
            return False, f"trop courte ({duration // 60}min < 3min)"
        if duration > DURATION_MAX_SEC:
            return False, f"trop longue ({duration // 60}min > 50min)"

    # Filtre mots-clés
    text = title + " " + description
    matches = [kw for kw in TRADING_KEYWORDS if kw in text]

    if not matches:
        return False, "aucun mot-clé trading détecté"

    return True, f"{len(matches)} mot(s)-clé(s) : {', '.join(matches[:3])}"


def filter_videos(videos: list, verbose: bool = True) -> list:
    """Retourne uniquement les vidéos de trading acceptées."""
    accepted = []
    for v in videos:
        ok, reason = is_trading_video(v)
        title_short = (v.get("title") or "")[:52]
        if ok:
            accepted.append(v)
            if verbose:
                print(f"   ✅ {title_short:<52} ({reason})")
        else:
            if verbose:
                print(f"   ❌ {title_short:<52} ({reason})")

    print(f"\n   🎯 Résultat filtre : {len(accepted)}/{len(videos)} vidéos retenues")
    return accepted
