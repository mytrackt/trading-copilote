# data\ — Dossier des données live TRADEX-AI

**Emplacement décidé** : `C:\trading-copilote\data\` (Option A — racine projet)
**Décision prise en** : Session S05 — 11/06/2026

## Fichiers attendus

| Fichier | Source | Fréquence | Format |
|---------|--------|-----------|--------|
| `NT8_data.csv` | NinjaTrader 8 (export indicateurs Belkhayate) | Toutes les 2s | CSV |
| `ATAS_signals.json` | ATAS Pro (Order Flow) | Toutes les 2s | JSON |
| `news_feed.json` | News API | Toutes les 5min | JSON |
| `fear_greed_stocks.json` | External API | Toutes les 15min | JSON |
| `gdelt_signals.json` | GDELT | Toutes les 20min | JSON |
| `events_calendar.json` | Calendrier macro | Toutes les 2h | JSON |
| `macro.json` | DX / taux Fed | Toutes les 6h | JSON |
| `cot_data.json` | CFTC COT hebdo | Hebdomadaire | JSON |
| `risk_state.json` | Écrit par risk_manager.py | À chaque signal | JSON |
| `signal_history.json` | Historique signaux | Append | JSON |

## Fichiers de test Phase C-01 (statiques)
- `NT8_data.csv` — données simulées pour valider data_reader.py
- `ATAS_signals.json` — signals simulés pour valider read_atas_signals()

## Phase suivante
Phase C-02 : connecter NinjaTrader 8 pour écrire NT8_data.csv en live.
