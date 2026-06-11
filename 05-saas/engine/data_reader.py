import os
import pandas as pd
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")  # C:\trading-copilote\data

def get_vix_delta_pct(minutes: int = 15) -> float:
    try:
        df = pd.read_csv(os.path.join(DATA_DIR, "NT8_data.csv"))
        vix_df = df[df['symbol'] == 'VX'].copy()
        vix_df['timestamp'] = pd.to_datetime(vix_df['timestamp'])
        vix_df = vix_df.sort_values('timestamp')
        if len(vix_df) < 2:
            return 0.0
        cutoff = datetime.now() - timedelta(minutes=minutes)
        recent = vix_df[vix_df['timestamp'] >= cutoff]
        if len(recent) < 2:
            return 0.0
        vix_start = recent.iloc[0]['close']
        vix_end   = recent.iloc[-1]['close']
        if vix_start == 0:
            return 0.0
        return round(abs((vix_end - vix_start) / vix_start), 4)
    except Exception:
        return 0.0

def read_nt8_data() -> list:
    from engine.circuit_breaker import CB_NT8
    return CB_NT8.call(
        lambda: pd.read_csv(os.path.join(DATA_DIR, "NT8_data.csv")).to_dict('records')
    )

def read_atas_signals() -> dict:
    from engine.circuit_breaker import CB_ATAS
    from utils.atomic_writer import safe_read_json
    return CB_ATAS.call(
        lambda: safe_read_json(os.path.join(DATA_DIR, "ATAS_signals.json"))
    )
