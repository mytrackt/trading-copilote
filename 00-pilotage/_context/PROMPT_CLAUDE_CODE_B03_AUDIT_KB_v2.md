# PROMPT CLAUDE CODE — PHASE B-03 : AUDIT QUALITÉ KB (v2)
> Cowork → Claude Code | S10 | Post-audit hostile — 8 correctifs intégrés
>
> CORRECTIFS v2 vs v1 :
> [🔴] Bug client corrigé (plus de double Anthropic() dans audit_batch)
> [🔴] Retry ×2 + timeout 30s sur chaque appel Claude API
> [🔴] PROMPT_SYSTEM hostile anti-biais de confirmation + Timing zones retirées
> [🟠] Reprise au niveau BATCH (et non catégorie entière)
> [🟠] Guard coût API ($2.00 max, coût réel affiché en fin de run)
> [🟠] Rapport horodaté (AUDIT_KB_RAPPORT_YYYYMMDD_HHMM.md)
> [🟠] parse_claude_json renforcé (3 stratégies + regex fallback)
> [🟡] Disclaimer légal dans le rapport généré

---

## CONTEXTE

- KB : `C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json`
- Structure : `{"metadata", "videos" (108), "aggregated_rules" (11 catégories → listes de strings)}`
- Total règles : **1462**
- Bug JSON connu : null bytes en queue — corrigé par fix_kb_nullbytes.py (Étape 0)
- Objectif : auditer les 1462 règles → rapport → décision de lever `kb_provisoire=True`

---

## RÈGLES ABSOLUES

1. `ANTHROPIC_API_KEY` = toujours `os.getenv("ANTHROPIC_API_KEY")` — jamais en dur
2. `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` en tête de chaque .py
3. `python -m py_compile fichier.py` avant toute exécution
4. Rate limiting : `time.sleep(2.0)` entre chaque batch
5. Pas d'accents dans les messages git
6. Chemins absolus `C:\trading-copilote\` uniquement
7. Terminal PowerShell : séparateur `;` (jamais `&&`)

---

## ÉTAPE 0 — CORRIGER LE BUG JSON NULL BYTES

Crée `C:\trading-copilote\05-saas\knowledge_base\fix_kb_nullbytes.py` :

```python
"""
Fix KB : supprime les octets nuls en queue de KNOWLEDGE_BASE_MASTER.json.
Le JSON valide se termine avant les null bytes ; le reste est ignoré.
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

    decoder = json.JSONDecoder()
    try:
        obj, idx = decoder.raw_decode(content)
    except json.JSONDecodeError as e:
        print(f"ERREUR decodage : {e}")
        sys.exit(1)

    reste = content[idx:].strip('\x00').strip()
    print(f"JSON valide : {idx} chars | Reste : {len(content) - idx} chars (attendu = null bytes)")

    if reste:
        print(f"ATTENTION : contenu non-null apres le JSON : {repr(reste[:100])}")
        print("Abandon — verification manuelle requise.")
        sys.exit(1)

    videos = obj.get('videos', {})
    agg = obj.get('aggregated_rules', {})
    total_rules = sum(len(r) for r in agg.values())
    print(f"Videos : {len(videos)} | Regles aggregated : {total_rules}")

    if len(videos) != 108:
        print(f"ERREUR : attendu 108 videos, trouve {len(videos)}. Abandon.")
        sys.exit(1)

    dir_kb = os.path.dirname(KB_PATH)
    tmp_fd, tmp_path = tempfile.mkstemp(dir=dir_kb, suffix='.tmp')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, KB_PATH)
        print(f"KB corrigee et sauvegardee.")
    except Exception as e:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        print(f"ERREUR ecriture : {e}")
        sys.exit(1)

    print("OK — null bytes supprimes.")


if __name__ == '__main__':
    main()
```

**Exécution :**
```powershell
python -m py_compile 05-saas\knowledge_base\fix_kb_nullbytes.py
python 05-saas\knowledge_base\fix_kb_nullbytes.py
```

**Résultat attendu :**
```
JSON valide : 465124 chars | Reste : 119803 chars (attendu = null bytes)
Videos : 108 | Regles aggregated : 1462
KB corrigee et sauvegardee.
OK — null bytes supprimes.
```

**Commit Étape 0 :**
```powershell
git add 05-saas\knowledge_base\fix_kb_nullbytes.py
git add 04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
git commit -m "fix(kb): supprime null bytes queue json knowledge base"
```

---

## ÉTAPE 1 — CRÉER LE SCRIPT D'AUDIT (v2)

Crée `C:\trading-copilote\05-saas\knowledge_base\audit_kb.py` :

```python
"""
Phase B-03 — Audit qualite des 1462 regles de KNOWLEDGE_BASE_MASTER.json.
VERSION v2 (post-audit hostile S10) :
  - Bug client corrige : plus de double Anthropic() dans audit_batch()
  - Retry x2 sur JSONDecodeError + timeout 30s (set sur client)
  - PROMPT_SYSTEM hostile anti-biais de confirmation
  - Timing zones [4;8]/[-8;-4] retirees du PROMPT_SYSTEM (statut HYPOTHESE non valide)
  - Reprise au niveau BATCH (cle = cat_batchstart)
  - Guard cout API ($2.00 max, cout reel affiche)
  - Fichier rapport horodate (AUDIT_KB_RAPPORT_YYYYMMDD_HHMM.md)
  - parse_claude_json renforce (3 strategies + regex fallback)
  - Disclaimer legal dans le rapport
"""
import os
import sys
import json
import re
import time
import tempfile
from datetime import datetime
import anthropic

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')
RESULTS_DIR = os.path.join(BASE_DIR, '..', '04-cerveau-trading')
# Fichier courant (permet la reprise batch par batch)
RESULTS_PATH = os.path.join(RESULTS_DIR, 'AUDIT_KB_RESULTS.json')

BATCH_SIZE = 20
RATE_LIMIT_SLEEP = 2.0      # secondes entre chaque batch
MODEL = 'claude-sonnet-4-6'
MAX_COST_USD = 2.0           # guard cout API

CATEGORIES_FR = {
    'saisonnalite': 'Saisonnalite',
    'correlations': 'Correlations inter-marches',
    'timing': 'Timing Belkhayate',
    'indicateurs_tendance': 'Indicateurs de tendance (COG / Direction)',
    'indicateurs_momentum': 'Indicateurs de momentum',
    'gestion_risque_entree': 'Gestion du risque et entree',
    'gestion_position_active': 'Gestion de position active',
    'structure_marche': 'Structure de marche',
    'macro_evenements': 'Macro et evenements',
    'volume_liquidite': 'Volume et liquidite',
    'psychologie': 'Psychologie du trading',
}

# [CORRECTIF 🔴] PROMPT_SYSTEM hostile + Timing zones retirees
PROMPT_SYSTEM = """Tu es un auditeur HOSTILE et exigeant de la methode de trading Belkhayate (Mustapha Belkhayate).

AVERTISSEMENT CRITIQUE : les regles que tu vas auditer ont probablement ete generees par un modele IA
(claude-sonnet-4-6) a partir de transcrits. Tu dois etre particulierement severe et resistant au biais
de confirmation. En cas de doute -> DOUTEUX, pas VALIDE.

METHODE BELKHAYATE — FAITS CONFIRMES par transcrits officiels uniquement :
- COG (Centre de Gravite) : regression polynomiale ordre 3, periode 180 (CONFIRME TRANSCRITS)
- Bandes COG : x0.618 (petrole) CONFIRME | x1.618 (autres) CONFIRME
  x2.618 et x4.236 = extension communautaire NON-BELKHAYATE
- Timing : oscillateur +/-10 CONFIRME
  IMPORTANT : les zones d'entree specifiques du Timing = HYPOTHESE NON VALIDEE PAR TRANSCRITS
  -> Ne pas utiliser comme reference pour valider ou invalider une regle
- Direction : indicateur de tendance proprietaire Belkhayate
- Energie : NON CODEE — conflit non tranche (MFI 20/80 vs proxy ATR)
  -> Toute regle portant sur l'Energie = DOUTEUX par defaut
- Marches trades UNIQUEMENT : GC (Or), HG (Cuivre), CL (Petrole WTI), ZW (Ble)
- Bitcoin et Yen = reference inter-marche, JAMAIS tradables
- Regle d'entree : 3/4 marches trading alignes ET 2/3 marches confirmation alignes

CRITERES DE VERDICT — applique-les strictement :
- VALIDE : regle SPECIFIQUE, ACTIONNABLE, coherente avec les faits CONFIRMES ci-dessus,
  non contradictoire, verifiable depuis un transcript
- DOUTEUX : regle vague, generique, non verifiable, attribution Belkhayate incertaine,
  basee sur Timing zones ou Energie (references non validees),
  ou applicable a n'importe quelle methode de trading
- INVALIDE : regle fausse, contradictoire avec les decisions verrouillees
  (ex: trader Bitcoin/Yen), ou dangereuse
- DOUBLON : quasi-identique a une autre regle du MEME batch — indiquer l'index de l'original

REGLE D'OR : prefere DOUTEUX a VALIDE si tu n'es pas certain a 90%.

Reponds UNIQUEMENT en JSON valide. Aucun texte avant ou apres le JSON."""


def load_kb():
    """Charge la KB (robuste aux null bytes residuels)."""
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(content)
    return obj


# [CORRECTIF 🟠] parse_claude_json renforce : 3 strategies + regex fallback
def parse_claude_json(raw: str) -> list:
    """Parse robuste de la reponse Claude : bloc ```json```, JSON direct, regex fallback."""
    raw = raw.strip()

    # Strategie 1 : bloc ```json ... ```
    if '```' in raw:
        parts = raw.split('```')
        for part in parts[1::2]:
            part = part.strip()
            if part.lower().startswith('json'):
                part = part[4:].strip()
            try:
                result = json.loads(part)
                if isinstance(result, list):
                    return result
            except json.JSONDecodeError:
                continue

    # Strategie 2 : JSON direct
    try:
        result = json.loads(raw)
        if isinstance(result, list):
            return result
    except json.JSONDecodeError:
        pass

    # Strategie 3 : regex — chercher le premier tableau JSON dans le texte
    match = re.search(r'\[.*?\]', raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise json.JSONDecodeError("Aucun JSON valide trouve dans la reponse", raw, 0)


# [CORRECTIF 🔴] audit_batch : utilise le client passe en arg + retry x2 + timeout sur client
def audit_batch(client, categorie: str, rules_batch: list, start_idx: int):
    """
    Envoie un batch de regles a Claude pour audit.
    Retourne (list[dict], usage).
    Retry x2 sur JSONDecodeError. Timeout gere au niveau client (voir main()).
    """
    rules_text = '\n'.join(
        f'{start_idx + i}. {r}' for i, r in enumerate(rules_batch)
    )
    prompt_user = (
        f"Categorie : {CATEGORIES_FR.get(categorie, categorie)}\n\n"
        f"Regles a auditer :\n{rules_text}\n\n"
        f"Reponds en JSON : "
        f'[{{"index": <numero>, "statut": "VALIDE|DOUTEUX|INVALIDE|DOUBLON", "motif": "<raison courte>"}}]\n'
        f"Couvre exactement {len(rules_batch)} regles "
        f"(indices {start_idx} a {start_idx + len(rules_batch) - 1})."
    )

    last_json_error = None
    for attempt in range(3):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=2000,
                system=PROMPT_SYSTEM,
                messages=[{'role': 'user', 'content': prompt_user}],
            )
            raw = response.content[0].text
            verdicts = parse_claude_json(raw)
            return verdicts, response.usage
        except json.JSONDecodeError as e:
            last_json_error = e
            if attempt < 2:
                print(f" [retry {attempt + 1}/2 JSONDecodeError]", end='', flush=True)
                time.sleep(2.0)
                continue
        # Erreurs reseau/API/timeout : propager immediatement (pas de retry silencieux)

    raise json.JSONDecodeError(
        f"Echec parse JSON apres 3 tentatives : {last_json_error}", "", 0
    )


def save_atomic(path: str, obj):
    """Ecriture atomique via tempfile + os.replace."""
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


# [CORRECTIF 🟠] Reprise au niveau BATCH
def load_existing_batches() -> dict:
    """Charge les batches deja audites depuis AUDIT_KB_RESULTS.json (reprise)."""
    if not os.path.exists(RESULTS_PATH):
        return {}
    try:
        with open(RESULTS_PATH, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        batches = existing.get('completed_batches', {})
        if batches:
            print(f"Reprise detectee : {len(batches)} batches deja audites.")
        return batches
    except Exception as e:
        print(f"Impossible de charger la reprise : {e} — repartir de zero.")
        return {}


def compute_cost(input_tokens: int, output_tokens: int) -> float:
    """Calcule le cout reel en USD (sonnet-4-6 : $3/M input, $15/M output)."""
    return (input_tokens * 3 + output_tokens * 15) / 1_000_000


# [CORRECTIF 🟡] Disclaimer legal + horodatage dans le rapport
def generate_markdown(output: dict, timestamp: str) -> str:
    stats = output.get('stats', {})
    categories = output.get('categories', {})
    usage = output.get('token_usage', {})
    cost = output.get('cost_estimate_usd', 0)
    total = sum(stats.values())

    lines = [
        '# AUDIT QUALITE KB — TRADEX-AI',
        f'**Date :** {timestamp[:8][:4]}-{timestamp[4:6]}-{timestamp[6:8]}  '
        f'| **Heure :** {timestamp[9:11]}:{timestamp[11:13]} UTC',
        f'**Modele :** {MODEL}  |  **Phase :** B-03  |  **Usage personnel uniquement**',
        '',
        '> **DISCLAIMER LEGAL :** Ce rapport est produit a titre strictement personnel',
        '> par un systeme IA pour usage prive. Il ne constitue pas un conseil financier.',
        '> Aucune regle issue de ce rapport ne doit etre appliquee sans validation',
        '> humaine prealable. TRADEX-AI est un outil d\'aide a la decision, pas un oracle.',
        '',
        '---',
        '',
        '## Resume global',
        '',
        '| Statut | Nb | % |',
        '|--------|----|----|',
    ]
    for s in ['VALIDE', 'DOUTEUX', 'INVALIDE', 'DOUBLON', 'NON_AUDITE']:
        n = stats.get(s, 0)
        pct = round(100 * n / total, 1) if total else 0
        lines.append(f'| {s} | {n} | {pct}% |')

    lines += [
        '',
        f'**Total audite :** {total} regles',
        f'**Tokens :** {usage.get("input", 0):,} input + {usage.get("output", 0):,} output',
        f'**Cout reel :** ${cost:.4f} USD',
        '',
    ]

    valide = stats.get('VALIDE', 0)
    douteux = stats.get('DOUTEUX', 0)
    invalide = stats.get('INVALIDE', 0)
    non_audite = stats.get('NON_AUDITE', 0)
    pct_valide = round(100 * valide / total, 1) if total else 0

    lines += ['## Decision recommandee', '']

    if non_audite > 0:
        lines.append(f'⚠️ **{non_audite} regles NON_AUDITE** (erreurs API) — relancer le script pour les completer.')
        lines.append('')

    if invalide > 0:
        lines.append(f'❌ **BLOQUANT : {invalide} regle(s) INVALIDE — purge obligatoire avant de lever kb_provisoire.**')
        lines.append('→ Lancer `purge_kb.py --statuts INVALIDE` puis re-auditer.')
    elif pct_valide >= 85 and non_audite == 0:
        lines.append('✅ **SEUIL ATTEINT (>=85% VALIDE, 0 INVALIDE, 0 NON_AUDITE)**')
        lines.append('→ Purger les DOUTEUX et DOUBLON si souhaite, puis passer `kb_provisoire=False` dans `settings.py`.')
        lines.append('→ Valider manuellement un echantillon de 5% (73 regles aleatoires) avant de lever le provisoire.')
    else:
        lines.append(f'⚠️ **Seuil non atteint** : {pct_valide}% VALIDE (seuil = 85%) ou NON_AUDITE > 0.')
        lines.append('→ Ne pas lever kb_provisoire. Relancer le script ou revoir les regles DOUTEUX.')

    lines += ['', '---', '', '## Detail par categorie', '']

    for cat, cat_results in categories.items():
        cat_stats = {'VALIDE': 0, 'DOUTEUX': 0, 'INVALIDE': 0, 'DOUBLON': 0, 'NON_AUDITE': 0}
        for r in cat_results:
            s = r.get('statut', 'NON_AUDITE')
            cat_stats[s] = cat_stats.get(s, 0) + 1

        cat_label = CATEGORIES_FR.get(cat, cat)
        lines.append(f'### {cat_label} ({len(cat_results)} regles)')
        stat_line = ' | '.join(f'{s}:{n}' for s, n in cat_stats.items() if n > 0)
        lines.append(stat_line)
        lines.append('')

        non_valide = [r for r in cat_results if r.get('statut') not in ('VALIDE',)]
        if non_valide:
            lines.append('**Regles a examiner :**')
            for r in non_valide:
                idx = r.get('index', '?')
                statut = r.get('statut', '?')
                motif = r.get('motif', '')
                regle = str(r.get('regle', ''))[:100]
                lines.append(f'- [{statut}] #{idx} — {regle}... | {motif}')
            lines.append('')

    return '\n'.join(lines)


def main():
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print('ERREUR : ANTHROPIC_API_KEY non definie.')
        sys.exit(1)

    # [CORRECTIF 🔴] Client cree UNE SEULE FOIS avec timeout — utilise dans audit_batch()
    client = anthropic.Anthropic(
        api_key=api_key,
        timeout=anthropic.Timeout(30.0, connect=5.0),
    )

    print('=== PHASE B-03 — AUDIT KB v2 ===')
    print(f'KB : {KB_PATH}')
    print(f'Modele : {MODEL} | Batch : {BATCH_SIZE} regles | Sleep : {RATE_LIMIT_SLEEP}s | Guard cout : ${MAX_COST_USD}')
    print()

    kb = load_kb()
    agg = kb.get('aggregated_rules', {})
    total_rules = sum(len(r) for r in agg.values())
    nb_batches = sum(-(-len(r) // BATCH_SIZE) for r in agg.values())
    print(f'Regles : {total_rules} | Categories : {len(agg)} | Batches estimes : {nb_batches}')
    print(f'Cout estime : $0.15-0.50 selon verbosité (non garanti)')
    print()

    # [CORRECTIF 🟠] Reprise niveau batch
    completed_batches = load_existing_batches()

    total_input_tokens = 0
    total_output_tokens = 0
    all_results = {}

    for cat, rules in agg.items():
        print(f'\n=== {CATEGORIES_FR.get(cat, cat)} ({len(rules)} regles) ===')
        cat_results = []

        for batch_start in range(0, len(rules), BATCH_SIZE):
            batch = rules[batch_start:batch_start + BATCH_SIZE]
            batch_key = f'{cat}_{batch_start}'
            batch_end = batch_start + len(batch) - 1

            # Skip si deja audite
            if batch_key in completed_batches:
                cat_results.extend(completed_batches[batch_key])
                print(f'  [{batch_start}-{batch_end}] SKIP (deja audite)')
                continue

            # [CORRECTIF 🟠] Guard cout avant chaque batch
            current_cost = compute_cost(total_input_tokens, total_output_tokens)
            if current_cost >= MAX_COST_USD:
                print(f'\nGUARD COUT : ${current_cost:.4f} >= ${MAX_COST_USD}. Arret propre.')
                print('Relancer le script pour continuer (reprise automatique).')
                break

            print(f'  [{batch_start}-{batch_end}/{len(rules) - 1}]...', end=' ', flush=True)

            try:
                verdicts, usage = audit_batch(client, cat, batch, batch_start)
                total_input_tokens += usage.input_tokens
                total_output_tokens += usage.output_tokens
                current_cost = compute_cost(total_input_tokens, total_output_tokens)

                # Aligner les verdicts sur les regles du batch
                verdict_map = {v['index']: v for v in verdicts}
                batch_results = []
                for i, regle in enumerate(batch):
                    idx = batch_start + i
                    v = verdict_map.get(idx, {'statut': 'NON_AUDITE', 'motif': 'non retourne par le modele'})
                    batch_results.append({
                        'index': idx,
                        'regle': regle,
                        'statut': v.get('statut', 'NON_AUDITE'),
                        'motif': v.get('motif', ''),
                    })

                cat_results.extend(batch_results)
                completed_batches[batch_key] = batch_results

                print(f'OK ({len(batch_results)} verdicts | cout cumule ${current_cost:.4f})')

                # Sauvegarde intermediaire apres CHAQUE BATCH
                intermediate = {
                    'last_updated': datetime.utcnow().isoformat() + 'Z',
                    'completed_batches': completed_batches,
                    'token_usage': {
                        'input': total_input_tokens,
                        'output': total_output_tokens,
                    },
                }
                save_atomic(RESULTS_PATH, intermediate)

            except Exception as e:
                print(f'ERREUR : {e}')
                for i, regle in enumerate(batch):
                    cat_results.append({
                        'index': batch_start + i,
                        'regle': regle,
                        'statut': 'NON_AUDITE',
                        'motif': str(e)[:200],
                    })

            time.sleep(RATE_LIMIT_SLEEP)

        all_results[cat] = cat_results

    # Stats globales
    stats = {'VALIDE': 0, 'DOUTEUX': 0, 'INVALIDE': 0, 'DOUBLON': 0, 'NON_AUDITE': 0}
    for cat_results in all_results.values():
        for r in cat_results:
            s = r.get('statut', 'NON_AUDITE')
            stats[s] = stats.get(s, 0) + 1

    final_cost = compute_cost(total_input_tokens, total_output_tokens)

    # [CORRECTIF 🟠] Rapport horodate
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M')
    rapport_path = os.path.join(RESULTS_DIR, f'AUDIT_KB_RAPPORT_{timestamp}.md')

    output = {
        'audited_at': datetime.utcnow().isoformat() + 'Z',
        'model': MODEL,
        'stats': stats,
        'categories': all_results,
        'token_usage': {
            'input': total_input_tokens,
            'output': total_output_tokens,
        },
        'cost_estimate_usd': round(final_cost, 4),
    }
    save_atomic(RESULTS_PATH, output)

    md = generate_markdown(output, timestamp)
    with open(rapport_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f'\n=== RESULTAT FINAL ===')
    total = sum(stats.values())
    for s in ['VALIDE', 'DOUTEUX', 'INVALIDE', 'DOUBLON', 'NON_AUDITE']:
        n = stats.get(s, 0)
        pct = round(100 * n / total, 1) if total else 0
        print(f'  {s}: {n} ({pct}%)')
    print(f'\nCout reel : ${final_cost:.4f} USD')
    print(f'Tokens    : {total_input_tokens:,} input + {total_output_tokens:,} output')
    print(f'Rapport   : {rapport_path}')
    print(f'JSON      : {RESULTS_PATH}')


if __name__ == '__main__':
    main()
```

---

## ÉTAPE 2 — LINT + EXÉCUTION

```powershell
python -m py_compile 05-saas\knowledge_base\audit_kb.py
python 05-saas\knowledge_base\audit_kb.py
```

**Comportement attendu :**
```
=== PHASE B-03 — AUDIT KB v2 ===
KB : C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
Modele : claude-sonnet-4-6 | Batch : 20 regles | Sleep : 2.0s | Guard cout : $2.0
Regles : 1462 | Categories : 11 | Batches estimes : 74
Cout estime : $0.15-0.50 selon verbosité (non garanti)

=== Saisonnalite (22 regles) ===
  [0-19] OK (20 verdicts | cout cumule $0.0XXX)
  [20-21] OK (2 verdicts | cout cumule $0.0XXX)
...
=== RESULTAT FINAL ===
  VALIDE: XXXX (XX%)
  DOUTEUX: XXX (XX%)
  ...
Cout reel : $X.XXXX USD
Rapport   : C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RAPPORT_20260614_XXXX.md
```

**Si interruption → relancer la même commande** : le script reprend depuis le dernier batch sauvegardé.

---

## ÉTAPE 3 — LIRE ET AFFICHER LE RAPPORT

Après exécution, lis `C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RAPPORT_*.md` (le plus récent) et affiche :

1. Le tableau résumé global (VALIDE / DOUTEUX / INVALIDE / DOUBLON / NON_AUDITE)
2. Le coût réel en USD
3. La décision recommandée (section "Decision recommandee")
4. La liste complète des règles INVALIDE (si > 0)
5. Le top 10 des règles DOUTEUX par catégorie

---

## ÉTAPE 4 — VALIDATION MANUELLE 5% (recommandée)

Avant de lever `kb_provisoire`, tirer un échantillon de 73 règles aléatoires (5% de 1462) et les valider manuellement :

```powershell
python -c "
import json, random, os
with open('C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json', 'r', encoding='utf-8') as f:
    content = f.read()
import json as _j
from json import JSONDecoder
obj, _ = JSONDecoder().raw_decode(content)
agg = obj['aggregated_rules']
all_rules = [(cat, i, r) for cat, rules in agg.items() for i, r in enumerate(rules)]
random.seed(42)
sample = random.sample(all_rules, 73)
for cat, idx, rule in sample:
    print(f'[{cat}] #{idx}: {rule[:120]}')
"
```

Valider manuellement chaque règle (accord / désaccord avec le verdict IA dans AUDIT_KB_RESULTS.json).
Si désaccord > 10% → ne pas lever kb_provisoire, revoir le PROMPT_SYSTEM.

---

## ROLLBACK

```powershell
# Supprimer les fichiers d'audit si corrompus
del C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RESULTS.json
del C:\trading-copilote\04-cerveau-trading\AUDIT_KB_RAPPORT_*.md

# Restaurer la KB depuis git si modifiee par erreur
git checkout HEAD -- 04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
```

---

## COMMITS

**Après Étape 0 (déjà documenté ci-dessus)**

**Après Étape 2 (audit terminé) :**
```powershell
git add 05-saas\knowledge_base\audit_kb.py
git add 04-cerveau-trading\AUDIT_KB_RESULTS.json
git add 04-cerveau-trading\AUDIT_KB_RAPPORT_*.md
git commit -m "feat(kb): phase b-03 audit qualite 1462 regles v2"
git push
```

---

## NOTE : ÉTAPE SUIVANTE APRÈS AUDIT

Si résultat satisfaisant (>=85% VALIDE, 0 INVALIDE, 0 NON_AUDITE) :
1. Créer `05-saas/knowledge_base/purge_kb.py` (prompt séparé à demander à Cowork)
2. Purger les règles INVALIDE + DOUBLON de `aggregated_rules`
3. Modifier `05-saas/config/settings.py` : `kb_provisoire = False`
4. Valider l'échantillon 5% manuellement

---

*Phase B-03 v2 — Prompt post-audit hostile | Cowork S10*
*8 correctifs intégrés (3 bloquants + 4 importants + 1 mineur)*
