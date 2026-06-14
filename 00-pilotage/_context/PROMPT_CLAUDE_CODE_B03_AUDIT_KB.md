# PROMPT CLAUDE CODE — PHASE B-03 : AUDIT QUALITÉ KB
> Cowork → Claude Code | Date : 14/06/2026 | Session S10

---

## CONTEXTE (lis avant d'agir)

- KB : `C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json`
- Structure KB : `{"metadata": {...}, "videos": {108 entrées...}, "aggregated_rules": {11 catégories → listes de strings}}`
- Total règles : **1462** réparties en 11 catégories
- Problème JSON connu : 119 803 octets nuls (`\x00`) en queue de fichier (vestige écriture atomique). Le JSON valide se termine à char 465124. À corriger en Étape 0.
- Objectif : auditer les 1462 règles → générer un rapport → lever `kb_provisoire=True` si résultat satisfaisant

---

## RÈGLES ABSOLUES (ne jamais déroger)

1. `ANTHROPIC_API_KEY` : toujours `os.getenv("ANTHROPIC_API_KEY")` — jamais en dur
2. `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` en tête de chaque .py
3. `python -m py_compile fichier.py` avant toute exécution
4. Rate limiting : `time.sleep(1.5)` entre chaque appel Claude API
5. Pas d'accents dans les messages git
6. Chemins absolus `C:\trading-copilote\` uniquement
7. Terminal PowerShell : séparateur `;` (jamais `&&`)

---

## ÉTAPE 0 — CORRIGER LE BUG JSON NULL BYTES

Crée le script `C:\trading-copilote\05-saas\knowledge_base\fix_kb_nullbytes.py` :

```python
"""
Fix KB : supprime les octets nuls en queue de KNOWLEDGE_BASE_MASTER.json.
Le JSON valide se termine à char 465124 ; le reste = bytes nuls.
"""
import os
import sys
import json
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')

def main():
    print(f"Lecture : {KB_PATH}")
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Taille originale : {len(content)} chars")

    # Extraire le JSON valide
    decoder = json.JSONDecoder()
    try:
        obj, idx = decoder.raw_decode(content)
    except json.JSONDecodeError as e:
        print(f"ERREUR décodage : {e}")
        sys.exit(1)

    clean_content = content[:idx]
    reste = content[idx:].strip('\x00').strip()
    print(f"JSON valide : {idx} chars | Reste après JSON : {len(content) - idx} chars (attendu = null bytes)")

    if reste:
        print(f"ATTENTION : du contenu non-null existe après le JSON : {repr(reste[:100])}")
        print("Abandon — vérification manuelle requise.")
        sys.exit(1)

    # Vérification : le JSON lu est complet
    videos = obj.get('videos', {})
    agg = obj.get('aggregated_rules', {})
    total_rules = sum(len(r) for r in agg.values())
    print(f"Vidéos : {len(videos)} | Règles aggregated : {total_rules}")

    if len(videos) != 108:
        print(f"ERREUR : attendu 108 vidéos, trouvé {len(videos)}. Abandon.")
        sys.exit(1)

    # Écriture atomique
    dir_kb = os.path.dirname(KB_PATH)
    tmp_fd, tmp_path = tempfile.mkstemp(dir=dir_kb, suffix='.tmp')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, KB_PATH)
        print(f"KB corrigée et sauvegardée : {KB_PATH}")
    except Exception as e:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        print(f"ERREUR écriture : {e}")
        sys.exit(1)

    print("OK — null bytes supprimés.")

if __name__ == '__main__':
    main()
```

**Exécution :**
```powershell
cd C:\trading-copilote
python -m py_compile 05-saas\knowledge_base\fix_kb_nullbytes.py
python 05-saas\knowledge_base\fix_kb_nullbytes.py
```

**Résultat attendu :**
```
JSON valide : 465124 chars | Reste après JSON : 119803 chars (attendu = null bytes)
Vidéos : 108 | Règles aggregated : 1462
KB corrigée et sauvegardée : ...KNOWLEDGE_BASE_MASTER.json
OK — null bytes supprimés.
```

---

## ÉTAPE 1 — CRÉER LE SCRIPT D'AUDIT

Crée `C:\trading-copilote\05-saas\knowledge_base\audit_kb.py` :

```python
"""
Phase B-03 — Audit qualité des 1462 règles de KNOWLEDGE_BASE_MASTER.json.
Envoie les règles à Claude API par batch de 20, collecte les verdicts,
génère AUDIT_KB_RESULTS.json + AUDIT_KB_RAPPORT.md.
"""
import os
import sys
import json
import time
import tempfile
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')
RESULTS_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'AUDIT_KB_RESULTS.json')
RAPPORT_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'AUDIT_KB_RAPPORT.md')

BATCH_SIZE = 20
RATE_LIMIT_SLEEP = 1.5
MODEL = 'claude-sonnet-4-6'

CATEGORIES_FR = {
    'saisonnalite': 'Saisonnalité',
    'correlations': 'Corrélations inter-marchés',
    'timing': 'Timing Belkhayate',
    'indicateurs_tendance': 'Indicateurs de tendance (COG / Direction)',
    'indicateurs_momentum': 'Indicateurs de momentum',
    'gestion_risque_entree': 'Gestion du risque et entrée',
    'gestion_position_active': 'Gestion de position active',
    'structure_marche': 'Structure de marché',
    'macro_evenements': 'Macro et événements',
    'volume_liquidite': 'Volume et liquidité',
    'psychologie': 'Psychologie du trading',
}

PROMPT_SYSTEM = """Tu es un auditeur expert de la méthode de trading BELKHAYATE (Mustapha Belkhayate).

MÉTHODE BELKHAYATE — rappels clés :
- COG (Centre de Gravité) : régression polynomiale ordre 3, période 180, bandes ×0.618 (pétrole) ou ×1.618 (autres)
- Timing : oscillateur ±10 ; zones d'entrée [4;8] (long) et [-8;-4] (short)
- Direction : indicateur de tendance propriétaire
- Énergie : non encore codée (conflit MFI 20/80 vs proxy ATR non tranché)
- Marchés tradés UNIQUEMENT : GC (Or), HG (Cuivre), CL (Pétrole WTI), ZW (Blé)
- Bitcoin et Yen = référence inter-marché, JAMAIS tradables
- Règle d'entrée : 3/4 marchés trading alignés ET 2/3 marchés confirmation alignés

CRITÈRES DE VERDICT :
- VALIDE : règle spécifique et actionnable, cohérente avec Belkhayate ou trading professionnel solide, non contradictoire
- DOUTEUX : règle vague, trop générique, non vérifiable depuis les transcrits, attribution Belkhayate incertaine, ou potentiellement applicable à n'importe quelle méthode
- INVALIDE : règle fausse ou contradictoire avec les décisions verrouillées du projet, ou dangereuse (trading Bitcoin, etc.)
- DOUBLON : quasi-identique à une autre règle du même batch (pointer l'index de l'original)

Réponds UNIQUEMENT en JSON valide. Aucun texte avant ou après."""


def load_kb():
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    # Robuste : ignore les null bytes en queue
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(content)
    return obj


def parse_claude_json(raw: str) -> list:
    """Parse robuste : gère les blocs ```json ... ```."""
    raw = raw.strip()
    if '```' in raw:
        parts = raw.split('```')
        for part in parts[1::2]:
            if part.startswith('json'):
                part = part[4:]
            try:
                return json.loads(part.strip())
            except json.JSONDecodeError:
                continue
    return json.loads(raw)


def audit_batch(client, categorie: str, rules_batch: list, start_idx: int) -> list:
    import anthropic
    rules_text = '\n'.join(f'{start_idx + i}. {r}' for i, r in enumerate(rules_batch))

    prompt_user = f"""Catégorie : {CATEGORIES_FR.get(categorie, categorie)}

Règles à auditer :
{rules_text}

Réponds en JSON : [{{"index": <numéro>, "statut": "VALIDE|DOUTEUX|INVALIDE|DOUBLON", "motif": "<raison en 1 phrase>"}}]
Couvre exactement {len(rules_batch)} règles (indices {start_idx} à {start_idx + len(rules_batch) - 1})."""

    import anthropic as _anthropic
    client_obj = _anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    response = client_obj.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=PROMPT_SYSTEM,
        messages=[{'role': 'user', 'content': prompt_user}]
    )
    raw = response.content[0].text
    return parse_claude_json(raw)


def save_atomic(path: str, obj):
    dir_ = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=dir_, suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def generate_markdown(output: dict) -> str:
    lines = [
        '# AUDIT QUALITÉ KB — TRADEX-AI',
        f'**Date :** {output["audited_at"][:10]}  |  **Modèle :** {MODEL}  |  **Phase :** B-03',
        '',
        '## Résumé global',
        '',
        f'| Statut | Nb | % |',
        f'|--------|----|---|',
    ]
    total = sum(output['stats'].values())
    for s, n in sorted(output['stats'].items(), key=lambda x: -x[1]):
        pct = round(100 * n / total, 1) if total else 0
        lines.append(f'| {s} | {n} | {pct}% |')
    lines += ['', f'**Total audité :** {total} règles', '']

    # Décision recommandée
    valide = output['stats'].get('VALIDE', 0)
    douteux = output['stats'].get('DOUTEUX', 0)
    invalide = output['stats'].get('INVALIDE', 0)
    pct_valide = round(100 * valide / total, 1) if total else 0
    lines += [
        '## Décision recommandée',
        '',
        f'- VALIDE : {valide} ({pct_valide}%)',
        f'- DOUTEUX + INVALIDE : {douteux + invalide} ({round(100*(douteux+invalide)/total,1) if total else 0}%)',
        '',
    ]
    if pct_valide >= 85 and invalide == 0:
        lines.append('✅ **RECOMMANDATION : lever `kb_provisoire=True` → passer `kb_provisoire=False`**')
        lines.append('→ Purger les règles DOUTEUX et INVALIDE avant, ou les marquer dans la KB.')
    elif invalide > 0:
        lines.append(f'❌ **BLOCANT : {invalide} règle(s) INVALIDE détectée(s) — purge obligatoire avant de lever le provisoire.**')
    else:
        lines.append(f'⚠️ **DOUTEUX trop nombreux ({douteux}) — relecture manuelle des DOUTEUX recommandée avant décision.**')

    lines += ['', '---', '', '## Détail par catégorie', '']
    for cat, cat_results in output['categories'].items():
        cat_stats = {'VALIDE': 0, 'DOUTEUX': 0, 'INVALIDE': 0, 'DOUBLON': 0, 'NON_AUDITE': 0}
        for r in cat_results:
            cat_stats[r.get('statut', 'NON_AUDITE')] = cat_stats.get(r.get('statut', 'NON_AUDITE'), 0) + 1

        lines.append(f'### {CATEGORIES_FR.get(cat, cat)} ({len(cat_results)} règles)')
        lines.append(f'VALIDE:{cat_stats["VALIDE"]} | DOUTEUX:{cat_stats["DOUTEUX"]} | INVALIDE:{cat_stats["INVALIDE"]} | DOUBLON:{cat_stats["DOUBLON"]}')
        lines.append('')

        # Lister uniquement les NON-VALIDE
        non_valide = [r for r in cat_results if r.get('statut') != 'VALIDE']
        if non_valide:
            lines.append('**Règles à examiner :**')
            for r in non_valide:
                idx = r.get('index', '?')
                statut = r.get('statut', '?')
                motif = r.get('motif', '')
                regle = str(r.get('regle', ''))[:100]
                lines.append(f'- [{statut}] #{idx} — {regle}… | {motif}')
            lines.append('')

    return '\n'.join(lines)


def main():
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print('ERREUR : ANTHROPIC_API_KEY non définie.')
        sys.exit(1)

    print('=== PHASE B-03 — AUDIT KB ===')
    print(f'KB : {KB_PATH}')
    print(f'Modèle : {MODEL}')
    print(f'Batch size : {BATCH_SIZE} | Sleep : {RATE_LIMIT_SLEEP}s')
    print()

    kb = load_kb()
    agg = kb.get('aggregated_rules', {})
    total_rules = sum(len(r) for r in agg.values())
    print(f'Règles à auditer : {total_rules} dans {len(agg)} catégories')
    nb_batches = sum(-(-len(r) // BATCH_SIZE) for r in agg.values())
    print(f'Batches estimés : {nb_batches}')
    print(f'Coût estimé : ~{nb_batches * 0.002:.2f}$ (estimé, non garanti)')
    print()

    # Reprendre depuis résultats existants si interruption
    existing_results = {}
    if os.path.exists(RESULTS_PATH):
        try:
            with open(RESULTS_PATH, 'r', encoding='utf-8') as f:
                existing = json.load(f)
            existing_results = existing.get('categories', {})
            print(f'Reprise détectée : {len(existing_results)} catégories déjà auditées.')
        except Exception:
            pass

    results = dict(existing_results)
    global_stats = {'VALIDE': 0, 'DOUTEUX': 0, 'INVALIDE': 0, 'DOUBLON': 0, 'NON_AUDITE': 0}

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    for cat, rules in agg.items():
        if cat in results:
            print(f'[SKIP] {cat} — déjà audité ({len(results[cat])} règles)')
            for r in results[cat]:
                s = r.get('statut', 'NON_AUDITE')
                global_stats[s] = global_stats.get(s, 0) + 1
            continue

        print(f'\n=== {CATEGORIES_FR.get(cat, cat)} ({len(rules)} règles) ===')
        cat_results = []

        for batch_start in range(0, len(rules), BATCH_SIZE):
            batch = rules[batch_start:batch_start + BATCH_SIZE]
            print(f'  [{batch_start+1}-{batch_start+len(batch)}/{len(rules)}]...', end=' ', flush=True)

            try:
                verdicts = audit_batch(client, cat, batch, batch_start)
                # Aligner les verdicts avec les règles
                verdict_map = {v['index']: v for v in verdicts}
                for i, regle in enumerate(batch):
                    idx = batch_start + i
                    verdict = verdict_map.get(idx, {'statut': 'NON_AUDITE', 'motif': 'non retourné par le modèle'})
                    statut = verdict.get('statut', 'NON_AUDITE')
                    cat_results.append({
                        'index': idx,
                        'regle': regle,
                        'statut': statut,
                        'motif': verdict.get('motif', ''),
                    })
                    global_stats[statut] = global_stats.get(statut, 0) + 1
                print(f'OK')
            except Exception as e:
                print(f'ERREUR : {e}')
                for i, regle in enumerate(batch):
                    idx = batch_start + i
                    cat_results.append({'index': idx, 'regle': regle, 'statut': 'NON_AUDITE', 'motif': str(e)})
                    global_stats['NON_AUDITE'] = global_stats.get('NON_AUDITE', 0) + 1

            time.sleep(RATE_LIMIT_SLEEP)

        results[cat] = cat_results

        # Sauvegarde intermédiaire après chaque catégorie (reprise possible)
        intermediate = {
            'audited_at': datetime.utcnow().isoformat() + 'Z',
            'stats': global_stats,
            'categories': results,
        }
        save_atomic(RESULTS_PATH, intermediate)
        print(f'  Sauvegarde intermédiaire : {cat} OK')

    # Rapport final
    output = {
        'audited_at': datetime.utcnow().isoformat() + 'Z',
        'stats': global_stats,
        'categories': results,
    }
    save_atomic(RESULTS_PATH, output)

    md = generate_markdown(output)
    with open(RAPPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f'\n=== RÉSULTAT FINAL ===')
    total = sum(global_stats.values())
    for s, n in sorted(global_stats.items(), key=lambda x: -x[1]):
        pct = round(100 * n / total, 1) if total else 0
        print(f'  {s}: {n} ({pct}%)')
    print(f'\nRapport JSON : {RESULTS_PATH}')
    print(f'Rapport MD   : {RAPPORT_PATH}')


if __name__ == '__main__':
    main()
```

---

## ÉTAPE 2 — LINT + EXÉCUTION

```powershell
cd C:\trading-copilote
python -m py_compile 05-saas\knowledge_base\audit_kb.py
python 05-saas\knowledge_base\audit_kb.py
```

**Résultat attendu :**
```
=== PHASE B-03 — AUDIT KB ===
KB : C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
Modèle : claude-sonnet-4-6
Règles à auditer : 1462 dans 11 catégories
Batches estimés : 74
...
[CATÉGORIE PAR CATÉGORIE]
...
=== RÉSULTAT FINAL ===
  VALIDE: XXXX (XX%)
  DOUTEUX: XXX (XX%)
  ...
Rapport MD : C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RAPPORT.md
```

**Si interruption :** relancer la même commande — le script reprend depuis la dernière catégorie sauvegardée.

---

## ÉTAPE 3 — LIRE LE RAPPORT ET AFFICHER LE RÉSUMÉ

Après l'exécution, lis `C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RAPPORT.md` et affiche :
1. Le tableau des stats globales (VALIDE / DOUTEUX / INVALIDE / DOUBLON)
2. La recommandation (lever ou non `kb_provisoire`)
3. La liste des règles INVALIDE (si > 0)
4. Le top 5 des règles DOUTEUX les plus problématiques

---

## ÉTAPE 4 — ROLLBACK (si problème)

Si erreur critique → ne pas modifier la KB. Les fichiers créés sont :
- `04-cerveau-trading/AUDIT_KB_RESULTS.json` → supprimer si corrompu
- `04-cerveau-trading/AUDIT_KB_RAPPORT.md` → supprimer si corrompu
- `KNOWLEDGE_BASE_MASTER.json` → l'étape 0 l'écrit atomiquement ; en cas de doute, restaurer depuis git : `git checkout HEAD -- 04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json`

---

## COMMIT APRÈS ÉTAPE 0

```powershell
cd C:\trading-copilote
git add 05-saas\knowledge_base\fix_kb_nullbytes.py
git add 04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
git commit -m "fix(kb): supprime null bytes queue json knowledge base"
```

## COMMIT APRÈS ÉTAPE 2 (audit terminé)

```powershell
cd C:\trading-copilote
git add 05-saas\knowledge_base\audit_kb.py
git add 04-cerveau-trading\AUDIT_KB_RESULTS.json
git add 04-cerveau-trading\AUDIT_KB_RAPPORT.md
git commit -m "feat(kb): phase b-03 audit qualite 1462 regles"
```

---

*Phase B-03 — Prompt produit par Cowork S10 | Exécution : Claude Code*
