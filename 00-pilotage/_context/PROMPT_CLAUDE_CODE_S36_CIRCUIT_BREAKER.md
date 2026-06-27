# PROMPT CLAUDE CODE — Mission S36 : Réparer le Circuit Breaker

> MODE CLAUDE CODE · Dossier racine : `C:\trading-copilote`
> Commit cible : `fix(engine): circuit breaker actif — protected_call dans claude_brain + data_reader`

---

## CONTEXTE

`circuit_breaker.py` contient 2 niveaux :

| Niveau | Ce que ça fait | Problème |
|--------|---------------|---------|
| `CircuitBreaker.call(func)` | État OPEN/CLOSED, comptage échecs | **0 timeout** — un appel bloqué = thread bloqué indéfiniment |
| `protected_call(cb, func, timeout_sec, retry_max)` | Timeout + retry + fallback ATTENDRE | **Jamais appelée en prod** |

`claude_brain.py` ligne 98 appelle `CB_CLAUDE.call(_call)` directement → pas de timeout 15s.
`data_reader.py` lignes 17 et 42 appellent `CB_NT8.call()` / `CB_ATAS.call()` directement → même problème.

**Résultat** : un appel Claude API ou lecture JSON qui traîne bloque tout le moteur sans retour ATTENDRE.

---

## VALIDATIONS PRÉALABLES (avant toute modification)

**Étape 1** — dans PowerShell, dossier `C:\trading-copilote` :
```
git log --oneline -3
```
Résultat attendu : dernière ligne = `c8ffb0f ...`

**Étape 2** :
```
python -m py_compile 05-saas\engine\circuit_breaker.py
```
Résultat attendu : aucune sortie (= OK)

**Étape 3** :
```
cd 05-saas\engine && python test_risk_guardrails.py
```
Résultat attendu : `16/16 tests PASS`

---

## MODIFICATIONS À EFFECTUER

### Fichier 1 : `05-saas\engine\claude_brain.py`

**Modification 1/2 — Import (lignes 41-45)**

Remplacer :
```python
# Import circuit breaker
try:
    from .circuit_breaker import CB_CLAUDE
except ImportError:
    CB_CLAUDE = None
    logger.warning("circuit_breaker non disponible")
```

Par :
```python
# Import circuit breaker
try:
    from .circuit_breaker import CB_CLAUDE, protected_call as _cb_protected_call
except ImportError:
    CB_CLAUDE = None
    _cb_protected_call = None
    logger.warning("circuit_breaker non disponible")
```

---

**Modification 2/2 — Appel dans `call_claude_kb` (lignes 97-99)**

Remplacer :
```python
    if CB_CLAUDE is not None:
        return CB_CLAUDE.call(_call)
    else:
        return _call()
```

Par :
```python
    if CB_CLAUDE is not None and _cb_protected_call is not None:
        result = _cb_protected_call(CB_CLAUDE, _call, timeout_sec=15, retry_max=2)
        # Si protected_call a déclenché le fallback → on lève pour que get_signal gère
        if isinstance(result, dict) and str(result.get("raison", "")).startswith("CB_FALLBACK"):
            raise RuntimeError(f"Circuit breaker declenche : {result['raison']}")
        return result
    else:
        return _call()
```

---

### Fichier 2 : `05-saas\engine\data_reader.py`

**Modification 1/2 — `read_nt8_asset` (lignes 12-19)**

Remplacer :
```python
    from engine.circuit_breaker import CB_NT8
    from utils.atomic_writer import safe_read_json
    from config.settings import get_nt8_path
    path = get_nt8_path(symbol)
    try:
        result = CB_NT8.call(lambda: safe_read_json(path))
    except Exception:
        return {}
    return result if isinstance(result, dict) else {}
```

Par :
```python
    from engine.circuit_breaker import CB_NT8, protected_call as _cb_protected_call
    from utils.atomic_writer import safe_read_json
    from config.settings import get_nt8_path
    path = get_nt8_path(symbol)
    try:
        result = _cb_protected_call(CB_NT8, lambda: safe_read_json(path),
                                    timeout_sec=5, retry_max=1)
        if isinstance(result, dict) and str(result.get("raison", "")).startswith("CB_FALLBACK"):
            return {}
        return result if isinstance(result, dict) else {}
    except Exception:
        return {}
```

---

**Modification 2/2 — `read_atas_signals` (lignes 38-44)**

Remplacer :
```python
    from engine.circuit_breaker import CB_ATAS
    from utils.atomic_writer import safe_read_json
    from config.settings import ATAS_DATA_PATH
    try:
        result = CB_ATAS.call(lambda: safe_read_json(ATAS_DATA_PATH))
    except Exception:
        return {}
    return result if isinstance(result, dict) else {}
```

Par :
```python
    from engine.circuit_breaker import CB_ATAS, protected_call as _cb_protected_call
    from utils.atomic_writer import safe_read_json
    from config.settings import ATAS_DATA_PATH
    try:
        result = _cb_protected_call(CB_ATAS, lambda: safe_read_json(ATAS_DATA_PATH),
                                    timeout_sec=5, retry_max=1)
        if isinstance(result, dict) and str(result.get("raison", "")).startswith("CB_FALLBACK"):
            return {}
        return result if isinstance(result, dict) else {}
    except Exception:
        return {}
```

---

## VALIDATIONS POST-MODIFICATION (dans l'ordre)

**Étape A** — Lint des 3 fichiers modifiés :
```
python -m py_compile 05-saas\engine\claude_brain.py
python -m py_compile 05-saas\engine\data_reader.py
python -m py_compile 05-saas\engine\circuit_breaker.py
```
Résultat attendu : aucune sortie pour chacun (= 0 erreur syntaxe)

**Étape B** — Suite de tests complète :
```
cd 05-saas\engine && python test_risk_guardrails.py
```
Résultat attendu : `16/16 tests PASS`

Si un test échoue → STOP, ne pas continuer. Afficher l'erreur et attendre confirmation.

**Étape C** — Test KB inchangée (vérification de non-régression) :
```
python -c "import json; kb=json.load(open('04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json')); print(sum(len(v) for v in kb['aggregated_rules'].values()))"
```
Résultat attendu : `1398`

---

## MISE À JOUR DETTE_TECHNIQUE.md

Après validation des étapes A/B/C, mettre à jour `00-pilotage\DETTE_TECHNIQUE.md` :

1. **Retirer** (bugs S35 corrigés) :
   - Section "## 1." → changer `✅ PARTIELLEMENT RÉPARÉ` → `✅ RÉPARÉ COMPLET (S35, commit c8ffb0f)` et noter que `KB_DIR`/`KB_PATH` dans `settings.py` sont corrects
   - Section "## 3." → déjà `✅ RÉPARÉ`, ajouter note : "`load_kb_rules()` réparé S35 — lit `aggregated_rules` + 2 formats KB"

2. **Ajouter** une nouvelle section "## 6." :
```markdown
## 6. ✅ RÉPARÉ (S36) — Circuit Breaker INACTIF

### Problème
`protected_call()` (timeout 15s + retry 2x + fallback ATTENDRE) implémentée dans
`circuit_breaker.py` mais jamais appelée en production.
`claude_brain.py` et `data_reader.py` utilisaient `CB.call()` directement → 0 timeout.
Un appel Claude API ou lecture JSON bloqué gelait le thread moteur indéfiniment.

### Correctif appliqué (S36)
- `claude_brain.py` : `CB_CLAUDE.call(_call)` → `protected_call(CB_CLAUDE, _call, timeout_sec=15, retry_max=2)`
- `data_reader.py` : `CB_NT8.call()` / `CB_ATAS.call()` → `protected_call(..., timeout_sec=5, retry_max=1)`
- Détection fallback dict CB_FALLBACK → comportement correct dans get_signal() et data_reader

### Validation
Tests `test_risk_guardrails.py` : 16/16 PASS (tests CB préexistants couvrent tous les cas)

### Mode AUTO
Toujours BLOQUÉ (`AUTO_MODE = False`). La réparation du circuit breaker est un prérequis
**nécessaire mais pas suffisant** pour envisager le mode AUTO.
```

---

## COMMIT

Après DETTE_TECHNIQUE.md mis à jour :
```
git add 05-saas\engine\claude_brain.py
git add 05-saas\engine\data_reader.py
git add 00-pilotage\DETTE_TECHNIQUE.md
git commit -m "fix(engine): circuit breaker actif — protected_call dans claude_brain + data_reader"
git push origin main
```

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\engine\claude_brain.py
git checkout -- 05-saas\engine\data_reader.py
```
Puis reporter le bug dans DETTE_TECHNIQUE.md avec l'erreur observée.

---

*TRADEX-AI · Mission S36 · 27/06/2026 · Usage strictement personnel — aucun conseil financier*
