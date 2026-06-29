# PROMPT CLAUDE CODE — S36 · C1 · cot_collector.py

> MODE CLAUDE CODE · Branche : `feature/phase-c-collectors`
> Commit cible : `feat(collector): cot_collector — CFTC COT weekly GC/HG/CL/ZW`
> Exécuter APRÈS C0A et C0B

---

## CONTEXTE

Collecteur COT (Commitments of Traders) — données hebdomadaires CFTC.
Source : API publique CFTC OData (aucune clé API requise).
Données ciblées : positions nettes des spéculateurs Non-Commerciaux sur GC/HG/CL/ZW.
Sortie : `C:\trading-copilote\data\cot_data.json` (atomic write).

Le COT est le Cercle C3 — Institutionnels (biais hebdomadaire uniquement, pas intraday).

---

## ÉTAPE 0 — Créer la branche

```
git checkout -b feature/phase-c-collectors
```

---

## ÉTAPE 1 — Vérifier que requests est disponible

```
python -m pip show requests
```
Si absent :
```
pip install requests --break-system-packages
```

---

## ÉTAPE 2 — Créer le fichier

Créer `C:\trading-copilote\05-saas\engine\cot_collector.py` :

```python
"""
cot_collector.py -- Collecteur COT (Commitments of Traders) CFTC
Phase C TRADEX-AI -- Cercle C3 Institutionnels
Source : CFTC API OData publique (pas de cle API)
Sortie : C:/trading-copilote/data/cot_data.json (atomic write)

ATTENTION : donnees hebdomadaires (publiees chaque vendredi 15h30 ET).
Usage : biais de fond uniquement -- INTERDIT comme trigger intraday.
"""
import os
import json
import time
import logging
import requests
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

# ⚠️ À VÉRIFIER : URL exacte de l'API CFTC OData
# Documentation officielle : https://publicreporting.cftc.gov/
# Table "TriWeeklyCombined" = rapport COT legacy hebdomadaire
CFTC_API_BASE = "https://publicreporting.cftc.gov/api/odata/v1"
CFTC_TABLE    = "TriWeeklyCombined"

# Correspondance actif NT8 → mot-clé CFTC market_and_exchange_names
# ⚠️ À VÉRIFIER : les noms exacts dans la base CFTC peuvent différer
CFTC_MARKET_KEYWORDS = {
    "GC": "GOLD",
    "HG": "COPPER",
    "CL": "CRUDE OIL, LIGHT SWEET",
    "ZW": "WHEAT",
}

TIMEOUT_SEC = 15


def _fetch_cot_for_market(keyword: str) -> dict | None:
    """
    Récupère les dernières données COT CFTC pour un actif.
    Retourne None si l'appel échoue ou si aucune donnée trouvée.
    """
    url = f"{CFTC_API_BASE}/{CFTC_TABLE}"
    params = {
        "$filter": f"contains(market_and_exchange_names, '{keyword}')",
        "$orderby": "report_date_as_yyyy_mm_dd desc",
        "$top": "1",
        "$select": (
            "market_and_exchange_names,"
            "report_date_as_yyyy_mm_dd,"
            "noncomm_positions_long_all,"
            "noncomm_positions_short_all,"
            "comm_positions_long_all,"
            "comm_positions_short_all,"
            "change_in_noncomm_long_all,"
            "change_in_noncomm_short_all"
        ),
    }
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        data = resp.json()
        values = data.get("value", [])
        if not values:
            logger.warning(f"[cot_collector] Aucune donnée pour keyword='{keyword}'")
            return None
        return values[0]
    except requests.RequestException as e:
        logger.error(f"[cot_collector] Erreur CFTC API pour '{keyword}' : {e}")
        return None


def collect_cot() -> dict:
    """
    Collecte les données COT pour les 4 actifs trading : GC, HG, CL, ZW.
    Retourne un dict structuré avec positions nettes et biais.
    """
    result = {}
    for symbol, keyword in CFTC_MARKET_KEYWORDS.items():
        raw = _fetch_cot_for_market(keyword)
        time.sleep(1.0)  # Rate limiting CFTC API
        if raw is None:
            result[symbol] = {
                "disponible": False,
                "erreur": "Aucune donnée CFTC",
            }
            continue

        long_nc  = int(raw.get("noncomm_positions_long_all",  0) or 0)
        short_nc = int(raw.get("noncomm_positions_short_all", 0) or 0)
        net      = long_nc - short_nc
        change_l = int(raw.get("change_in_noncomm_long_all",  0) or 0)
        change_s = int(raw.get("change_in_noncomm_short_all", 0) or 0)
        net_change = change_l - change_s

        result[symbol] = {
            "disponible":       True,
            "date_rapport":     raw.get("report_date_as_yyyy_mm_dd", ""),
            "long_nc":          long_nc,
            "short_nc":         short_nc,
            "net_speculateur":  net,
            "variation_nette":  net_change,
            "biais":            "LONG" if net > 0 else "SHORT" if net < 0 else "NEUTRE",
            "biais_croissant":  net_change > 0,
            "nom_cftc":         raw.get("market_and_exchange_names", ""),
        }
        logger.info(f"[cot_collector] {symbol} — net={net:+d} · biais={result[symbol]['biais']}")

    return result


def write_cot(data: dict) -> None:
    """Écrit atomiquement dans data/cot_data.json."""
    from utils.atomic_writer import atomic_write_json
    from config.settings import COT_DATA_PATH
    data["_collected_at"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(COT_DATA_PATH, data)
    logger.info(f"[cot_collector] Écrit → {COT_DATA_PATH}")


def run_once() -> dict:
    """1 cycle complet : collect + write."""
    try:
        data = collect_cot()
        write_cot(data)
        actifs_ok = sum(1 for v in data.values() if isinstance(v, dict) and v.get("disponible"))
        logger.info(f"[cot_collector] TERMINÉ — {actifs_ok}/4 actifs disponibles")
        return data
    except Exception as e:
        logger.error(f"[cot_collector] ERREUR run_once : {e}")
        return {}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_once()
    print(json.dumps(result, indent=2, default=str))
```

---

## ÉTAPE 3 — Lint

```
python -m py_compile 05-saas\engine\cot_collector.py
```
→ 0 erreur

---

## ÉTAPE 4 — Test 10 cycles (mode dry-run)

```
cd 05-saas
python -c "
import sys; sys.path.insert(0,'.')
import engine.cot_collector as c
for i in range(3):
    r = c.collect_cot()
    print(f'Cycle {i+1}:', {k: v.get('biais','ERR') for k,v in r.items() if isinstance(v,dict)})
    import time; time.sleep(2)
print('OK — 3 cycles sans crash')
"
```
→ doit afficher les biais GC/HG/CL/ZW sans erreur

Si l'API CFTC retourne une erreur de connexion → noter le message exact et stopper.
⚠️ Si la réponse indique une URL incorrecte → vérifier https://publicreporting.cftc.gov/ et corriger `CFTC_TABLE` dans le fichier.

---

## ÉTAPE 5 — Vérifier l'écriture atomic

```
python -c "
import sys; sys.path.insert(0,'05-saas')
import engine.cot_collector as c
r = c.run_once()
import json, os
from config.settings import COT_DATA_PATH
if os.path.exists(COT_DATA_PATH):
    d = json.load(open(COT_DATA_PATH, encoding='utf-8'))
    print('Fichier écrit OK — champs:', list(d.keys()))
else:
    print('ERREUR : fichier non créé')
"
```
→ doit afficher les clés GC/HG/CL/ZW + `_collected_at`

---

## COMMIT

```
git add 05-saas\engine\cot_collector.py
git commit -m "feat(collector): cot_collector — CFTC COT weekly GC/HG/CL/ZW"
```
(Pas de push — attendre C2 et C3 avant le push final de la branche)

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\engine\cot_collector.py
```
Ou supprimer le fichier si non encore commité.

---

*TRADEX-AI · S36 · C1 · 27/06/2026*
