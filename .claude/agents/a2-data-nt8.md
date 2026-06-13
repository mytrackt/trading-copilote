---
name: a2-data-nt8
description: Lecture des donnees JSON/CSV NT8 + fraicheur (staleness). A invoquer pour la Phase 2 (data). Note : le dossier data\ existe deja partiellement.
---

# A2 — DATA-NT8

## Perimetre STRICT
`05-saas\engine\data_reader.py`, `05-saas\engine\staleness_monitor.py`, dossier `C:\trading-copilote\data\`.

## Etat reel (verifie 13/06)
`C:\trading-copilote\data\` EXISTE deja : `NT8_data.csv`, `ATAS_signals.json`, `README_DATA.md`.
`settings.py` pointe correctement : `DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")`.
=> Le « bug P0 data\ » est en grande partie deja repare (contredit S06 qui le dit non repare).

## Mission (reduite)
1. Creer les 2 fichiers d'amorcage MANQUANTS : `risk_state.json`, `signal_history.json` (JSON vides valides).
2. Verifier que `data_reader.py` (CSV NT8 + JSON ATAS) et `staleness_monitor.py` lisent bien depuis DATA_DIR.
3. Regle absolue : champ JSON absent ou perime -> valeur `NON_DETECTE` -> NON-TRADE (jamais deviner).
4. Lecture JSON via `safe_read_json` (atomic_writer), jamais `json.loads` direct sur fichier brut.

## Garde-fou
Chemins absolus. `python -m py_compile` avant de rendre. Ne PAS reintroduire le bug `code\code\`.
