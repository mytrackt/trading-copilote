# PROMPT CLAUDE CODE — S36 · C0B · settings.py + FEUILLE_DE_ROUTE (Gate 2 Phase B)

> MODE CLAUDE CODE · Branche : `main` (docs + config)
> Commit cible : `chore(config): Phase C paths + API keys + GO criteria decorreles`
> Exécuter APRÈS C0A

---

## CONTEXTE

2 actions dans ce prompt :
1. Ajouter dans `settings.py` les chemins et clés API des 3 collecteurs Phase C
2. Mettre à jour `FEUILLE_DE_ROUTE.md` : décorréler batch Gemini de Phase C + critère tokens révisé

---

## MODIFICATION 1 — `05-saas\config\settings.py`

Ajouter à la fin du fichier (après la section CIRCUIT_BREAKER) :

```python
# =============================================================================
# PHASE C — COLLECTEURS DE DONNÉES EXTERNES
# Clés API : jamais ici → os.getenv() uniquement
# =============================================================================

# Chemins sorties (écriture atomic_write_json)
COT_DATA_PATH   = os.path.join(DATA_DIR, "cot_data.json")
MACRO_DATA_PATH = os.path.join(DATA_DIR, "macro_data.json")
NEWS_DATA_PATH  = os.path.join(DATA_DIR, "news_data.json")

# Références clés API Phase C (lues depuis .env)
# Ajouter dans .env :
#   FRED_API_KEY=xxxx        (https://fred.stlouisfed.org → Compte gratuit)
#   EIA_API_KEY=xxxx         (https://www.eia.gov/opendata → Compte gratuit)
#   FINNHUB_API_KEY=xxxx     (https://finnhub.io → Plan gratuit suffisant)
#   CFTC : API publique — aucune clé requise

FRED_API_KEY    = os.getenv("FRED_API_KEY", "")
EIA_API_KEY     = os.getenv("EIA_API_KEY", "")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY", "")

# Staleness Phase C (compléter STALENESS existant)
STALENESS["cot_max_age_hours"]   = 168   # hebdomadaire
STALENESS["macro_max_age_hours"] = 24    # quotidien
STALENESS["news_max_age_min"]    = 5     # 5 minutes
```

---

## MODIFICATION 2 — `00-pilotage\FEUILLE_DE_ROUTE.md`

### 2A — Critère tokens Phase B

Localiser dans la section `### PHASE B — KB Belkhayate` le tableau GO criteria.

Remplacer :
```
| KB < 50k tokens | Comptage tokens prompt système | < 50 000 tokens |
```
Par :
```
| KB < 55k tokens | Script compact (C0A) | < 55 000 tokens (prompt caching OK) |
```

Remplacer dans la colonne NO-GO :
```
**NO-GO si :** ... · tokens > 50k
```
Par :
```
**NO-GO si :** ... · tokens > 55k
```

---

### 2B — Décorrélation batch Gemini

Localiser dans `### PHASE B — KB Belkhayate` le tableau GO criteria.

Remplacer :
```
| Batch Gemini terminé | `ls 03-transcriptions\nouvelles-sources\` | 203 fichiers |
```
Par :
```
| Batch Gemini (partiel OK) | `ls 03-transcriptions\nouvelles-sources\` | ≥ 42 fichiers (complet requis Phase E uniquement) |
```

---

### 2C — Phase C GO criteria

Localiser `### PHASE C — Collecteurs de données`.

Remplacer :
```
| Phase B validée | GO Phase B | ✅ |
```
Par :
```
| Phase B partielle validée | KB chargeable + tokens < 55k + dossier data\ créé | ✅ |
```

---

### 2D — Phase E prérequis batch Gemini

Localiser `### PHASE E — Signal Scorer + Régime + WFO + Loop3`.

Ajouter une ligne dans le tableau GO criteria (avant la première ligne existante) :
```
| Batch Gemini terminé | `ls 03-transcriptions\nouvelles-sources\` | 203 fichiers |
```

---

## VALIDATIONS POST-MODIFICATION

**Étape 1** — Lint settings.py :
```
python -m py_compile 05-saas\config\settings.py
```
→ 0 erreur

**Étape 2** — Vérifier que les 3 chemins sont accessibles :
```
python -c "
import sys; sys.path.insert(0,'05-saas')
from config.settings import COT_DATA_PATH, MACRO_DATA_PATH, NEWS_DATA_PATH, DATA_DIR
import os
print('DATA_DIR:', DATA_DIR, '—', 'existe' if os.path.exists(DATA_DIR) else 'ABSENT')
print('COT_DATA_PATH:', COT_DATA_PATH)
print('MACRO_DATA_PATH:', MACRO_DATA_PATH)
print('NEWS_DATA_PATH:', NEWS_DATA_PATH)
"
```
→ DATA_DIR doit exister · les 3 paths affichés correctement

---

## COMMIT

```
git add 05-saas\config\settings.py
git add 00-pilotage\FEUILLE_DE_ROUTE.md
git commit -m "chore(config): Phase C paths + API keys + GO criteria decorreles batch Gemini"
git push origin main
```

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\config\settings.py
git checkout -- 00-pilotage\FEUILLE_DE_ROUTE.md
```

---

*TRADEX-AI · S36 · C0B · 27/06/2026*
