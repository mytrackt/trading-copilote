# PROMPT CLAUDE CODE — S36 · C0A · Compact load_kb_rules (Gate 1 Phase B)

> MODE CLAUDE CODE · Branche : `main` (bug fix)
> Commit cible : `fix(brain): load_kb_rules format compact — 52k tokens`

---

## CONTEXTE

`load_kb_rules()` dans `05-saas\engine\claude_brain.py` génère ~57k tokens de texte KB.
Critère GO Phase B : < 55k tokens.
Cause : préfixes redondants `[statut confiance]` sur les 1350 règles vidéo
et `[fiabilite]` sur les 48 règles chapitres.
Fix : supprimer ces préfixes → ~52k tokens → critère validé.

---

## VALIDATION PRÉALABLE

```
python -m py_compile 05-saas\engine\claude_brain.py
```
→ 0 erreur

---

## MODIFICATION — `05-saas\engine\claude_brain.py`

Localiser la fonction `load_kb_rules()`.

**Remplacer** (dans la boucle `for categorie, briques in aggregated.items()`) :

```python
            if rule.get("id"):
                # Type Chapitre
                titre = rule.get("titre", rule.get("id", ""))
                corps = rule.get("contenu", "")
                fiabilite = rule.get("fiabilite", "")
                rules_text += f"### {titre} [{fiabilite}]\n{corps}\n\n"
            else:
                # Type Video
                regle = rule.get("regle", "")
                statut = rule.get("statut", "")
                confiance = rule.get("confiance", "")
                rules_text += f"- [{statut} {confiance}] {regle}\n"
```

**Par** :

```python
            if rule.get("id"):
                # Type Chapitre (compact : sans tag fiabilite)
                titre = rule.get("titre", rule.get("id", ""))
                corps = rule.get("contenu", "")
                rules_text += f"### {titre}\n{corps}\n\n"
            else:
                # Type Video (compact : regle seule, sans statut/confiance redondants)
                regle = rule.get("regle", "")
                rules_text += f"- {regle}\n"
```

---

## VALIDATIONS POST-MODIFICATION

**Étape 1** — Lint :
```
python -m py_compile 05-saas\engine\claude_brain.py
```
→ 0 erreur

**Étape 2** — Compter les tokens :
```
python -c "
import json, sys
sys.path.insert(0, '05-saas')
kb_path = '04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json'
with open(kb_path, encoding='utf-8') as f:
    kb_data = json.load(f)
aggregated = kb_data.get('aggregated_rules', {})
rules_text = '# KNOWLEDGE BASE TRADEX-AI\n\n'
rules_text += f'Total regles : {sum(len(v) for v in aggregated.values())}\n\n'
for cat, briques in aggregated.items():
    rules_text += f'## {cat.upper()}\n'
    for rule in briques:
        if rule.get('id'):
            rules_text += f\"### {rule.get('titre', rule.get('id',''))}\n{rule.get('contenu','')}\n\n\"
        else:
            rules_text += f\"- {rule.get('regle','')}\n\"
tokens = len(rules_text) // 4
print(f'Tokens estimés : {tokens}')
print(f'Critère : < 55 000 — {chr(10240)}' + ('OK' if tokens < 55000 else 'DEPASSE'))
"
```
→ doit afficher < 55 000 tokens

**Étape 3** — Tests complets :
```
cd 05-saas\engine && python test_risk_guardrails.py
```
→ 21/21 PASS

**Étape 4** — Vérifier KB inchangée :
```
python -c "import json; kb=json.load(open('04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json', encoding='utf-8')); print(sum(len(v) for v in kb['aggregated_rules'].values()))"
```
→ 1398

---

## COMMIT

```
git add 05-saas\engine\claude_brain.py
git commit -m "fix(brain): load_kb_rules format compact — 52k tokens Gate1 PhaseB"
git push origin main
```

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\engine\claude_brain.py
```

---

*TRADEX-AI · S36 · C0A · 27/06/2026*
