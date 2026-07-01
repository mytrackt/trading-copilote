# execution_guardrails.py — v1.1
# Garde-fous chiffres TRADEX-AI — couche d'execution (Scenario B)
# Importe par claude_brain.py. Aucune dependance externe (stdlib only).
#
# CHANGELOG
#   v1.0 -> v1.1 (corrections P0 issues de l'audit 12 passes) :
#   - P4  : controle marge / notional + exposition correlee NQ+ES agregee
#   - P8  : perte PIRE CAS (gap + slippage + commissions) au lieu du seul stop
#   - P7  : news/event blackout dur
#   - P10 : compteur atomique, idempotency card_id, verif expiry AU SENT
#   - P2  : flag CONFIG_NON_VALIDEE tant que les defauts ne sont pas confirmes
#   - fix : bug message d'erreur RR (acces direct -> .get())
#   - send_order() : fonction SEPAREE STAGED -> SENT (jamais dans validate_order)

import threading
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# SPECS CONTRATS — multiplicateurs CME (A VERIFIER aupres du broker)
# NQ (E-mini Nasdaq-100) : 20 $/point | tick 0.25 -> 5 $
# ES (E-mini S&P 500)    : 50 $/point | tick 0.25 -> 12.5 $
# ---------------------------------------------------------------------------
CONTRACT_SPECS = {
    "NQ": {"point_multiplier": 20.0, "tick_value": 5.0,   "margin_per_contract": 0.0},  # AJUSTER margin
    "ES": {"point_multiplier": 50.0, "tick_value": 12.5,  "margin_per_contract": 0.0},  # AJUSTER margin
}

# ---------------------------------------------------------------------------
# LIMITES DURES — AJUSTER puis passer config_validated = True
# ---------------------------------------------------------------------------
GUARDRAILS = {
    "config_validated": False,               # bloque tant que non confirme par Abdelkrim
    "allowlist_instruments": ["NQ", "ES"],

    "max_contracts_per_order": 2,            # AJUSTER
    "max_risk_pct_per_trade": 1.0,           # % du solde reel (perte PIRE CAS)  # AJUSTER
    "max_daily_loss_pct": 3.0,               # coupe-circuit journalier           # AJUSTER
    "max_orders_per_day": 5,                 # AJUSTER
    "min_rr_ratio": 1.5,                     # AJUSTER

    "max_notional_usd": 800_000.0,           # plafond notional d'un ordre        # AJUSTER
    "max_correlated_notional_usd": 1_200_000.0,  # plafond exposition correlee     # AJUSTER
    "correlated_groups": {"index_us": ["NQ", "ES"]},

    # Couts reels d'execution (P8)
    "slippage_ticks": 2,                     # ticks de glissement estime          # AJUSTER
    "commission_per_contract": 4.0,          # USD aller simple                    # AJUSTER
    "gap_buffer_pct": 25.0,                  # % ajoute a la perte stop pour gap    # AJUSTER

    "stop_loss_mandatory": True,
    "averaging_down_forbidden": True,
    "stage_ttl_minutes": 15,
}

# ---------------------------------------------------------------------------
# ETAT PARTAGE — atomicite (in-process). EN PROD : remplacer par Redis (stack gelee).
# ---------------------------------------------------------------------------
_LOCK = threading.Lock()
_STATE = {
    "orders_today": 0,
    "daily_pnl_pct": 0.0,
    "sent_card_ids": set(),   # idempotency
    "day": datetime.now(timezone.utc).date(),
}


def _roll_day_if_needed():
    today = datetime.now(timezone.utc).date()
    if _STATE["day"] != today:
        _STATE["orders_today"] = 0
        _STATE["daily_pnl_pct"] = 0.0
        _STATE["sent_card_ids"].clear()
        _STATE["day"] = today


# ---------------------------------------------------------------------------
# CALCULS
# ---------------------------------------------------------------------------
def compute_notional(card: dict) -> float:
    spec = CONTRACT_SPECS[card["instrument"]]
    return card["size_contracts"] * spec["point_multiplier"] * card["entry_price"]


def compute_worst_case_loss(card: dict) -> float:
    """Perte PIRE CAS = perte au stop + slippage + commissions aller-retour + buffer gap."""
    spec = CONTRACT_SPECS[card["instrument"]]
    size = card["size_contracts"]
    points = abs(card["entry_price"] - card["invalidation_level"])
    base = points * spec["point_multiplier"] * size
    slippage = GUARDRAILS["slippage_ticks"] * spec["tick_value"] * size
    commission = GUARDRAILS["commission_per_contract"] * size * 2  # aller-retour
    gap = base * (GUARDRAILS["gap_buffer_pct"] / 100.0)
    return base + slippage + commission + gap


def is_in_news_blackout(now_utc: datetime, blackout_windows: list[tuple]) -> bool:
    """blackout_windows = [(start_utc, end_utc), ...] alimente par le calendrier amont."""
    for start, end in blackout_windows:
        if start <= now_utc <= end:
            return True
    return False


def correlated_notional(card: dict, open_positions: list[dict]) -> float:
    """Notional total des positions correlees + le nouvel ordre."""
    group = None
    for _, members in GUARDRAILS["correlated_groups"].items():
        if card["instrument"] in members:
            group = members
            break
    if group is None:
        return compute_notional(card)
    total = compute_notional(card)
    for p in open_positions:
        if p.get("instrument") in group:
            spec = CONTRACT_SPECS[p["instrument"]]
            total += abs(p.get("size_contracts", 0)) * spec["point_multiplier"] * p.get("entry_price", 0)
    return total


# ---------------------------------------------------------------------------
# VALIDATION — retourne (verdict, raisons, worst_case_usd)
# verdict in {"STAGED", "NO_TRADE", "REJECTED", "CONFIG_NON_VALIDEE"}
# Ne renvoie JAMAIS "SENT". L'envoi passe par send_order().
# ---------------------------------------------------------------------------
def validate_order(card: dict, account_balance_usd: float,
                   open_positions: list[dict],
                   blackout_windows: list[tuple] | None = None) -> tuple[str, list[str], float]:
    blackout_windows = blackout_windows or []
    reasons = []

    # P2 — config non confirmee
    if not GUARDRAILS["config_validated"]:
        return "CONFIG_NON_VALIDEE", ["GUARDRAILS non valides par l'operateur (defauts en place)"], 0.0

    with _LOCK:
        _roll_day_if_needed()
        orders_today = _STATE["orders_today"]
        daily_pnl_pct = _STATE["daily_pnl_pct"]

    # 0. Coupe-circuit journalier
    if daily_pnl_pct <= -GUARDRAILS["max_daily_loss_pct"]:
        return "REJECTED", [f"Coupe-circuit: perte du jour {daily_pnl_pct}% <= -{GUARDRAILS['max_daily_loss_pct']}%"], 0.0

    # 1. Plafond ordres / jour
    if orders_today >= GUARDRAILS["max_orders_per_day"]:
        return "REJECTED", [f"Plafond atteint: {orders_today} ordres aujourd'hui"], 0.0

    # 2. Instrument autorise
    if card.get("instrument") not in GUARDRAILS["allowlist_instruments"]:
        return "REJECTED", [f"Instrument hors allowlist: {card.get('instrument')}"], 0.0

    # 3. Verdict NO_TRADE explicite (discipline)
    if card.get("verdict") == "NO_TRADE":
        return "NO_TRADE", ["Checker: aucun signal valide -> pas de trade force"], 0.0

    # 4. P7 — news blackout
    if is_in_news_blackout(datetime.now(timezone.utc), blackout_windows):
        return "REJECTED", ["Fenetre news/event a fort impact -> blackout"], 0.0

    # 5. Filtres Belkhayate verrouilles
    f = card.get("filters", {})
    for key, label in [
        ("nq_es_correlation_ok", "correlation NQ/ES"),
        ("gold_dxy_filter_ok", "filtre Gold/DXY"),
        ("semi_log_scale_ok", "echelle semi-log"),
    ]:
        if not f.get(key, False):
            reasons.append(f"Filtre non passe: {label}")
    if reasons:
        return "NO_TRADE", reasons, 0.0

    # 6. Stop obligatoire
    if GUARDRAILS["stop_loss_mandatory"] and not card.get("invalidation_level"):
        return "REJECTED", ["Stop/invalidation manquant (obligatoire)"], 0.0

    # 7. Interdiction averaging down
    if GUARDRAILS["averaging_down_forbidden"]:
        for p in open_positions:
            if (p.get("instrument") == card.get("instrument")
                    and p.get("direction") == card.get("direction")
                    and p.get("unrealized_pnl_usd", 0) < 0):
                return "REJECTED", ["Averaging down interdit (position perdante en cours)"], 0.0

    # 8. Taille <= contrats max
    if card.get("size_contracts", 0) > GUARDRAILS["max_contracts_per_order"]:
        return "REJECTED", [f"Taille {card.get('size_contracts')} > max {GUARDRAILS['max_contracts_per_order']}"], 0.0

    # 9. P4 — notional d'ordre
    notional = compute_notional(card)
    if notional > GUARDRAILS["max_notional_usd"]:
        return "REJECTED", [f"Notional {notional:,.0f}$ > max {GUARDRAILS['max_notional_usd']:,.0f}$"], 0.0

    # 10. P4 — exposition correlee agregee (NQ+ES)
    corr = correlated_notional(card, open_positions)
    if corr > GUARDRAILS["max_correlated_notional_usd"]:
        return "REJECTED", [f"Exposition correlee {corr:,.0f}$ > max {GUARDRAILS['max_correlated_notional_usd']:,.0f}$"], 0.0

    # 11. P8 — risque PIRE CAS (gap+slippage+commissions) vs % solde
    worst = compute_worst_case_loss(card)
    risk_pct = (worst / account_balance_usd * 100) if account_balance_usd else 999
    if risk_pct > GUARDRAILS["max_risk_pct_per_trade"]:
        return "REJECTED", [f"Risque pire cas {risk_pct:.2f}% > max {GUARDRAILS['max_risk_pct_per_trade']}%"], worst

    # 12. RR minimum (fix bug : .get())
    rr = card.get("risk", {}).get("rr_ratio", 0)
    if rr < GUARDRAILS["min_rr_ratio"]:
        return "REJECTED", [f"RR {rr} < min {GUARDRAILS['min_rr_ratio']}"], worst

    return "STAGED", ["Tous garde-fous passes -> en attente d'approbation humaine"], worst


def attach_expiry(card: dict, worst_case_usd: float) -> dict:
    ttl = timedelta(minutes=GUARDRAILS["stage_ttl_minutes"])
    card["expires_at_utc"] = (datetime.now(timezone.utc) + ttl).isoformat()
    card["worst_case_loss_usd"] = round(worst_case_usd, 2)
    card["state"] = "STAGED"
    card["human_approval_required"] = True
    return card


# ---------------------------------------------------------------------------
# ENVOI — fonction SEPAREE (jamais appelee par validate_order)
# Enforce : approbation humaine + non-expire + idempotency. broker_send_fn = hook reel.
# ---------------------------------------------------------------------------
def send_order(card: dict, human_approved: bool, broker_send_fn) -> dict:
    if not human_approved:
        return {"state": "BLOCKED", "reason": "Approbation humaine absente"}

    if card.get("state") != "STAGED":
        return {"state": "BLOCKED", "reason": f"Etat invalide: {card.get('state')}"}

    # Expiry au SENT
    exp = card.get("expires_at_utc")
    if exp and datetime.now(timezone.utc) > datetime.fromisoformat(exp):
        card["state"] = "EXPIRED"
        return {"state": "EXPIRED", "reason": "Ordre STAGED perime"}

    with _LOCK:
        _roll_day_if_needed()
        if card["card_id"] in _STATE["sent_card_ids"]:
            return {"state": "DUPLICATE", "reason": "card_id deja envoye (idempotency)"}
        if _STATE["orders_today"] >= GUARDRAILS["max_orders_per_day"]:
            return {"state": "BLOCKED", "reason": "Plafond ordres atteint au moment du SENT"}
        # reservation atomique AVANT l'appel broker
        _STATE["sent_card_ids"].add(card["card_id"])
        _STATE["orders_today"] += 1

    # Appel broker reel (NinjaTrader / pont d'execution) — HOOK injecte
    try:
        result = broker_send_fn(card)  # doit renvoyer: FILLED | PARTIAL | REJECTED | ERROR
    except Exception as e:
        with _LOCK:  # rollback reservation si echec d'appel
            _STATE["sent_card_ids"].discard(card["card_id"])
            _STATE["orders_today"] -= 1
        return {"state": "ERROR", "reason": f"Echec appel broker: {e}"}

    if result in ("REJECTED", "ERROR"):
        with _LOCK:
            _STATE["sent_card_ids"].discard(card["card_id"])
            _STATE["orders_today"] -= 1
        card["state"] = "CANCELLED"
        return {"state": result, "reason": "Broker a refuse l'ordre"}

    card["state"] = "SENT"
    return {"state": "SENT", "broker_result": result}  # FILLED ou PARTIAL


def register_fill_pnl(pnl_pct: float):
    """A appeler apres cloture pour alimenter le coupe-circuit journalier."""
    with _LOCK:
        _roll_day_if_needed()
        _STATE["daily_pnl_pct"] += pnl_pct
