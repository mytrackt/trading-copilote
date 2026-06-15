# PROMPT CLAUDE CODE — Validation règles DOUTEUX KB
> Session S12 | 15/06/2026 | MODE CLAUDE CODE

## CONTEXTE

Le script `05-saas/knowledge_base/validate_douteux.py` est déjà écrit et compilé.
Il valide les 1 265 règles KB Belkhayate contre les 110 transcripts existants.

**Coût estimé** : ~$0.18 avec Haiku (108 appels × ~3 600 tokens)
**Durée estimée** : ~10-15 min (rate-limited 1.5s/appel)
**Résumable** : oui — checkpoint auto après chaque vidéo

---

## TÂCHE 1 — Vérifier l'environnement

```powershell
# Dans VS Code terminal (PowerShell) :
cd C:\trading-copilote

# Vérifier que le script compile
python -m py_compile 05-saas\knowledge_base\validate_douteux.py
# Attendu : pas d'erreur (silence = succès)

# Vérifier que la clé API est disponible
python -c "import os; key = os.getenv('ANTHROPIC_API_KEY'); print('OK' if key else 'MANQUANTE')"
# Si MANQUANTE : voir Tâche 2
```

---

## TÂCHE 2 (si clé absente) — Charger la clé API

```powershell
# Charger temporairement pour cette session PowerShell :
$env:ANTHROPIC_API_KEY = "sk-ant-..."   # Remplace par ta vraie clé

# OU : créer le fichier .env (déjà dans .gitignore)
# Ajoute cette ligne dans C:\trading-copilote\.env :
# ANTHROPIC_API_KEY=sk-ant-...

# Puis charger depuis .env :
Get-Content C:\trading-copilote\.env | ForEach-Object {
    if ($_ -match '^([^#=]+)=(.+)$') {
        [System.Environment]::SetEnvironmentVariable($Matches[1].Trim(), $Matches[2].Trim(), 'Process')
    }
}
```

---

## TÂCHE 3 — Lancer le dry-run (test gratuit)

```powershell
cd C:\trading-copilote
python 05-saas\knowledge_base\validate_douteux.py --dry-run
```

**Résultat attendu** :
```
✓ 110 transcripts disponibles
PASSE 1 — 108 vidéos (0 déjà traitées, 108 restantes)
[001/108] video_id : X règles | transcript Y chars | ...
  [DRY RUN] batch 1/1 — X règles simulées
  ✓ checkpoint | {'DRY_RUN': X}
...
PASSE 2 — X règles orphelines
PASSE 3 — rapports générés
```

Si tu vois ça → tout est OK, lance la production.

---

## TÂCHE 4 — Lancer la validation complète (production)

```powershell
cd C:\trading-copilote
python 05-saas\knowledge_base\validate_douteux.py
```

**En cas d'interruption** (Ctrl+C, coupure, etc.) :
```powershell
# Reprendre là où ça s'était arrêté (checkpoint auto) :
python 05-saas\knowledge_base\validate_douteux.py
# Le script skip automatiquement les vidéos déjà traitées.
```

---

## TÂCHE 5 — Vérifier les résultats

```powershell
# Où sont les fichiers ?
ls C:\trading-copilote\04-cerveau-trading\validation\

# Afficher les statistiques finales :
python -c "
import json
with open(r'C:\trading-copilote\04-cerveau-trading\validation\RAPPORT_VALIDATION.json', encoding='utf-8') as f:
    r = json.load(f)
print('RÉSULTATS:')
for k, v in r['stats'].items():
    if v > 0:
        pct = round(v / r['total_regles'] * 100, 1)
        print(f'  {k:15} : {v:>4} ({pct}%)')
print(f'  TOTAL          : {r[\"total_regles\"]}')
print(f'  TAUX VALIDE    : {r[\"taux_valide_pct\"]}%')
"
```

---

## TÂCHE 6 — Commit

```powershell
cd C:\trading-copilote

# Vérifier ce qui va être commité :
git status

# Ajouter uniquement les bons fichiers :
git add 05-saas/knowledge_base/validate_douteux.py
git add 04-cerveau-trading/validation/RAPPORT_VALIDATION.json
git add 04-cerveau-trading/validation/KB_VALIDEE.json
git add 04-cerveau-trading/validation/A_VERIFIER_HUMAIN.md
git add 00-pilotage/_context/PROMPT_CLAUDE_CODE_VALIDATE_DOUTEUX.md

# NE PAS ajouter checkpoint.json ni validate_douteux.log (temporaires)

git commit -m "feat(kb): validation douteux passe1+2+3 terminee"
```

---

## EN CAS DE PROBLÈME

### Erreur "ModuleNotFoundError: No module named 'anthropic'"
```powershell
pip install anthropic --break-system-packages
```

### Erreur "JSONDecodeError" sur la KB
```powershell
python -c "
with open(r'C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json', 'rb') as f:
    raw = f.read().replace(b'\x00', b'')
import json; kb = json.loads(raw)
print('KB OK :', len(kb.get('videos', {})), 'videos')
"
```

### Reprendre depuis passe 2 seulement
```powershell
python 05-saas\knowledge_base\validate_douteux.py --passe 2
```

### Regenerer uniquement les rapports (depuis checkpoint existant)
```powershell
python 05-saas\knowledge_base\validate_douteux.py --passe 3
```

---

## RÉSULTATS ATTENDUS

Après la passe 3, dans `04-cerveau-trading/validation/` :

| Fichier | Contenu |
|---------|---------|
| `RAPPORT_VALIDATION.json` | Stats + détails complets de chaque règle |
| `KB_VALIDEE.json` | KB reconstruite avec VALIDE/INVALIDE/AMBIGU par règle |
| `A_VERIFIER_HUMAIN.md` | Liste des AMBIGU avec liens YouTube pour revue rapide |
| `validate_douteux.log` | Log complet de l'exécution |

**Objectif** : réduire les 1 225 DOUTEUX en VALIDE (confirmés) + INVALIDE (supprimés) + AMBIGU (revue humaine par Abdelkrim sur les cas ambigus uniquement).

Après validation → seules les règles VALIDE alimenteront les signaux de trading.

---

*Prompt généré par Cowork S12 — exécuter dans VS Code Claude Code*
