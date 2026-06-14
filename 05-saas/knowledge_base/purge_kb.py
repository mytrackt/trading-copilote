"""
Phase B-04 — Purge des regles INVALIDE et DOUBLON de KNOWLEDGE_BASE_MASTER.json.

Entree :
  - AUDIT_KB_RESULTS.json (verdicts de l'audit B-03)
  - KNOWLEDGE_BASE_MASTER.json (KB courante)

Action :
  - Supprime de aggregated_rules toutes les regles dont statut in {INVALIDE, DOUBLON}.
  - NE TOUCHE PAS les DOUTEUX (contenu conserve).
  - NE TOUCHE PAS videos[].rules (trace historique brute conservee a dessein :
    une reconstruction de aggregated re-injecterait les regles purgees).
  - NE LEVE PAS kb_provisoire (decision posterieure a l'echantillon 5%).
  - Ecriture atomique (tempfile + os.replace).
  - Trace : PURGE_KB_LOG_<timestamp>.md.

Matching par TEXTE EXACT : aggregated_rules etant dedupliquee, chaque texte
de regle est unique par categorie -> plus robuste qu'un matching par index.
"""
import os
import sys
import json
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')
RESULTS_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'AUDIT_KB_RESULTS.json')
LOG_DIR = os.path.join(BASE_DIR, '..', '04-cerveau-trading')

STATUTS_A_PURGER = {'INVALIDE', 'DOUBLON'}


def load_json_robuste(path: str):
    """Charge un JSON en tolerant d'eventuels null bytes residuels en queue."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    obj, _ = json.JSONDecoder().raw_decode(content)
    return obj


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


def main():
    if not os.path.exists(RESULTS_PATH):
        print(f'ERREUR : resultats d audit introuvables : {RESULTS_PATH}')
        sys.exit(1)
    if not os.path.exists(KB_PATH):
        print(f'ERREUR : KB introuvable : {KB_PATH}')
        sys.exit(1)

    results = load_json_robuste(RESULTS_PATH)
    kb = load_json_robuste(KB_PATH)

    categories = results.get('categories', {})
    agg = kb.get('aggregated_rules', {})

    # Construit, par categorie, l'ensemble des textes de regles a supprimer
    to_remove = {}
    audit_counts = {}  # nb verdicts INVALIDE/DOUBLON dans l'audit (attendu)
    for cat, rows in categories.items():
        textes = set()
        n = 0
        for r in rows:
            if r.get('statut') in STATUTS_A_PURGER:
                textes.add(r.get('regle', ''))
                n += 1
        to_remove[cat] = textes
        audit_counts[cat] = n

    print('=== PHASE B-04 — PURGE INVALIDE + DOUBLON ===')
    print(f'KB : {KB_PATH}')
    print(f'Statuts purges : {", ".join(sorted(STATUTS_A_PURGER))}')
    print(f'DOUTEUX : conserves (non touches)')
    print('-' * 64)

    total_avant = 0
    total_supprime = 0
    total_apres = 0
    detail = []  # (cat, avant, supprime, apres, attendu)

    for cat in agg:
        rules = agg[cat]
        avant = len(rules)
        remove_set = to_remove.get(cat, set())
        kept = [rule for rule in rules if rule not in remove_set]
        supprime = avant - len(kept)
        apres = len(kept)
        agg[cat] = kept

        total_avant += avant
        total_supprime += supprime
        total_apres += apres
        attendu = audit_counts.get(cat, 0)
        detail.append((cat, avant, supprime, apres, attendu))

        flag = '' if supprime == attendu else f'  /!\\ attendu {attendu}'
        print(f'  {cat:<28} avant {avant:>4} | supprime {supprime:>3} | restant {apres:>4}{flag}')

    print('-' * 64)
    print(f'  {"TOTAL":<28} avant {total_avant:>4} | supprime {total_supprime:>3} | restant {total_apres:>4}')

    # Garde-fou : coherence avec l'audit
    total_attendu = sum(audit_counts.values())
    if total_supprime != total_attendu:
        print()
        print(f'AVERTISSEMENT : {total_supprime} regles supprimees mais {total_attendu} '
              f'verdicts INVALIDE/DOUBLON dans l audit.')
        print('Ecart possible si un texte de regle differe entre audit et KB. '
              'Verification recommandee avant commit.')

    # Met a jour metadata (kb_provisoire NON leve)
    kb.setdefault('metadata', {})
    kb['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
    kb['metadata']['purge_b04'] = {
        'purged_statuts': sorted(STATUTS_A_PURGER),
        'rules_before': total_avant,
        'rules_removed': total_supprime,
        'rules_after': total_apres,
        'kb_provisoire': True,
        'note': 'videos[].rules non touchees (trace brute). DOUTEUX conserves.',
    }

    # Ecriture atomique de la KB purgee
    save_atomic(KB_PATH, kb)
    print()
    print(f'KB purgee et sauvegardee (atomique) : {KB_PATH}')

    # Trace markdown horodatee
    ts = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')
    log_path = os.path.join(LOG_DIR, f'PURGE_KB_LOG_{ts}.md')
    lines = [
        '# PURGE KB — TRADEX-AI (Phase B-04)',
        f'**Date :** {ts[:4]}-{ts[4:6]}-{ts[6:8]} {ts[9:11]}:{ts[11:13]} UTC',
        f'**Statuts purges :** {", ".join(sorted(STATUTS_A_PURGER))}  |  **DOUTEUX :** conserves',
        '',
        f'- Regles avant : **{total_avant}**',
        f'- Regles supprimees : **{total_supprime}**',
        f'- Regles restantes : **{total_apres}**',
        f'- kb_provisoire : **True** (non leve — echantillon 5% requis)',
        '',
        '> Note : seules les `aggregated_rules` sont purgees. Les `videos[].rules`',
        '> (extraction brute par video) sont conservees comme trace historique.',
        '',
        '## Detail par categorie',
        '',
        '| Categorie | Avant | Supprimees | Restantes |',
        '|-----------|------:|-----------:|----------:|',
    ]
    for cat, avant, supprime, apres, _ in detail:
        lines.append(f'| {cat} | {avant} | {supprime} | {apres} |')
    lines += [
        f'| **TOTAL** | **{total_avant}** | **{total_supprime}** | **{total_apres}** |',
        '',
    ]
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f'Log de purge : {log_path}')


if __name__ == '__main__':
    main()
