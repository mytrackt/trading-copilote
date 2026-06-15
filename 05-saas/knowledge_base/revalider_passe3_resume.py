#!/usr/bin/env python3
"""
revalider_passe3_resume.py -- 3e passe avec cache par transcript
Version : 1.0 | Session S14

USAGE :
  py revalider_passe3_resume.py --status          # Voir l'avancement
  py revalider_passe3_resume.py --next            # Traiter le prochain transcript
  py revalider_passe3_resume.py --merge           # Fusionner dans KB_VALIDEE.json (quand tout est fini)
  py revalider_passe3_resume.py --dry-run --next  # Simuler sans API
"""

import os, re, sys, json, time, logging, argparse, tempfile
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

TRANSCRIPTS_DIR = os.path.join(ROOT_DIR, "03-transcriptions", "nouvelles-sources",
                                "belkhayate-youtube", "transcripts")
VALIDATION_DIR  = os.path.join(ROOT_DIR, "04-cerveau-trading", "validation")
KB_VALIDEE_PATH = os.path.join(VALIDATION_DIR, "KB_VALIDEE.json")
HUMAIN_PATH     = os.path.join(VALIDATION_DIR, "A_VERIFIER_HUMAIN.md")
CACHE_PATH      = os.path.join(VALIDATION_DIR, "passe3_cache.json")

MODEL = "claude-sonnet-4-6"
MAX_TRANSCRIPT_CHARS = 14000
MAX_RULES_PER_CALL   = 25

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


def atomic_write(path, data):
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=dir_path, suffix=".tmp",
                                      delete=False, encoding="utf-8") as tmp:
        json.dump(data, tmp, ensure_ascii=False, indent=2)
        tmp_path = tmp.name
    os.replace(tmp_path, path)


def parse_claude_json(text):
    for pattern in [r"```json\s*(.*?)\s*```", r"```\s*(.*?)\s*```", r"(\{.*\})"]:
        m = re.search(pattern, text, re.DOTALL)
        if m:
            try: return json.loads(m.group(1))
            except: continue
    try: return json.loads(text.strip())
    except: return None


def load_kb():
    with open(KB_VALIDEE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"done": [], "results": {}, "created_at": datetime.now().isoformat()}


def extraire_pas_reponse(kb):
    """Retourne toutes les regles AMBIGU 'Pas de reponse API' groupees par transcript."""
    by_transcript = {}
    for cat, buckets in kb.get("rules_by_status", {}).items():
        for entry in buckets.get("AMBIGU", []):
            note = entry.get("note", "")
            if "Pas de r" in note and "ponse API" in note:
                tf = entry.get("source_transcript", "UNKNOWN")
                if tf not in by_transcript:
                    by_transcript[tf] = []
                by_transcript[tf].append({
                    "categorie": cat,
                    "texte": entry.get("texte", ""),
                    "source_video_id": entry.get("source_video_id", ""),
                    "source_transcript": tf,
                })
    return by_transcript


def cmd_status():
    kb = load_kb()
    by_tf = extraire_pas_reponse(kb)
    cache = load_cache()
    done = set(cache.get("done", []))

    log.info(f"\n{'='*60}")
    log.info(f"PASSE 3 -- STATUT")
    log.info(f"{'='*60}")
    log.info(f"Total transcripts : {len(by_tf)}")
    log.info(f"Traites           : {len(done)}")
    log.info(f"Restants          : {len(by_tf) - len(done)}")
    log.info(f"")
    for i, (tf, rules) in enumerate(sorted(by_tf.items()), 1):
        status = "✅" if tf in done else "⏳"
        nb_res = len([k for k in cache.get("results", {}) if k.startswith(tf[:20])])
        log.info(f"  {status} [{i:02d}/06] {tf[:60]} ({len(rules)} regles)")
    log.info(f"{'='*60}")
    nb_done = sum(1 for v in cache.get("results", {}).values() if v.get("verdict") == "VALIDE")
    log.info(f"  VALIDE recuperes jusqu'ici : {nb_done}")
    log.info(f"{'='*60}\n")


def cmd_next(dry_run=False):
    kb = load_kb()
    by_tf = extraire_pas_reponse(kb)
    cache = load_cache()
    done = set(cache.get("done", []))

    pending = [tf for tf in sorted(by_tf.keys()) if tf not in done]
    if not pending:
        log.info("Tous les transcripts ont ete traites ! Lance --merge pour finaliser.")
        return

    tf = pending[0]
    rules = by_tf[tf]
    log.info(f"\n{'='*60}")
    log.info(f"TRAITEMENT : {tf[:65]}")
    log.info(f"  {len(rules)} regles | transcript {list(sorted(by_tf.keys())).index(tf)+1}/{len(by_tf)}")
    log.info(f"{'='*60}")

    # Charger transcript
    tf_path = os.path.join(TRANSCRIPTS_DIR, tf)
    if not os.path.exists(tf_path):
        log.warning(f"Transcript introuvable : {tf}")
        for rule in rules:
            cache["results"][rule["texte"]] = {
                "verdict": "AMBIGU", "passage": None,
                "confiance": 0.0, "note": "Transcript introuvable",
            }
        cache["done"].append(tf)
        atomic_write(CACHE_PATH, cache)
        log.info("Transcript introuvable -> toutes gardees AMBIGU. Cache mis a jour.")
        return

    with open(tf_path, "r", encoding="utf-8", errors="replace") as f:
        transcript_text = f.read()
    if len(transcript_text) > MAX_TRANSCRIPT_CHARS:
        transcript_text = transcript_text[:MAX_TRANSCRIPT_CHARS] + "\n[...TRONQUE...]"
    log.info(f"  Transcript charge : {len(transcript_text)} chars")

    if dry_run:
        for rule in rules:
            cache["results"][rule["texte"]] = {
                "verdict": "DRY_RUN", "passage": None,
                "confiance": 0.0, "note": "dry-run passe3",
            }
        cache["done"].append(tf)
        atomic_write(CACHE_PATH, cache)
        log.info(f"[DRY RUN] {len(rules)} regles simulees. Cache mis a jour.")
        return

    # Appel API
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        log.error("ANTHROPIC_API_KEY manquante.")
        sys.exit(1)

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    video_title = tf.replace(".txt", "")[:70]
    batches = [rules[j:j+MAX_RULES_PER_CALL] for j in range(0, len(rules), MAX_RULES_PER_CALL)]

    all_results = {}
    for b_idx, batch in enumerate(batches):
        batch_indexed = [{**r, "index": i+1} for i, r in enumerate(batch)]
        rules_block = "\n".join(
            f'{r["index"]}. [{r["categorie"].upper()}] {r["texte"]}'
            for r in batch_indexed
        )
        prompt = (
            f'Tu es un expert de la methode de trading Mustapha Belkhayate.\n\n'
            f'TRANSCRIPT (video : "{video_title}") :\n---\n{transcript_text}\n---\n\n'
            f'REGLES A VERIFIER ({len(batch_indexed)} regles) :\n{rules_block}\n\n'
            f'MISSION : Verifier si le CONCEPT de chaque regle est present dans ce transcript.\n\n'
            f'IMPORTANT : On ne cherche PAS une citation mot-a-mot.\n'
            f'On cherche si l\'IDEE est presente, meme exprimee differemment.\n'
            f'La paraphrase ou l\'implication claire est suffisante.\n\n'
            f'CRITERES :\n'
            f'  VALIDE   = concept clairement present (directement ou par implication forte).\n'
            f'  INVALIDE = concept absent ou contredit.\n'
            f'  AMBIGU   = concept effleure mais pas assez developpe pour confirmer.\n\n'
            f'Reponds UNIQUEMENT avec ce JSON (rien d\'autre) :\n'
            f'{{"resultats": [{{"index": <int>, "verdict": "VALIDE"|"INVALIDE"|"AMBIGU", '
            f'"passage": "<extrait illustratif>", "confiance": <float 0-1>, "note": "<max 80 chars>"}}]}}'
        )

        log.info(f"  Appel API batch {b_idx+1}/{len(batches)} ({len(batch)} regles)...")
        t0 = time.time()
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=3000,
                messages=[{"role": "user", "content": prompt}],
            )
            elapsed = time.time() - t0
            raw = resp.content[0].text.strip()
            parsed = parse_claude_json(raw)
            if not parsed or "resultats" not in parsed:
                log.error(f"  JSON invalide ({elapsed:.1f}s): {raw[:150]}")
                for r in batch:
                    all_results[r["texte"]] = {"verdict": "AMBIGU", "note": "JSON invalide passe3"}
                continue

            for res in parsed["resultats"]:
                if res.get("verdict") not in {"VALIDE", "INVALIDE", "AMBIGU"}:
                    res["verdict"] = "AMBIGU"
                res["confiance"] = max(0.0, min(1.0, float(res.get("confiance", 0.5))))

            api_by_idx = {r.get("index"): r for r in parsed["resultats"]}
            verdicts = {}
            for item in batch_indexed:
                r = api_by_idx.get(item["index"], {})
                if not r:
                    all_results[item["texte"]] = {"verdict": "AMBIGU", "note": "Pas de reponse API (passe3)"}
                else:
                    all_results[item["texte"]] = r
                verdicts[item["texte"]] = all_results[item["texte"]].get("verdict", "?")

            vc = {}
            for v in verdicts.values(): vc[v] = vc.get(v, 0) + 1
            log.info(f"  Batch {b_idx+1} OK ({elapsed:.1f}s) : {vc}")

        except Exception as e:
            log.error(f"  Erreur API : {e}")
            for r in batch:
                all_results[r["texte"]] = {"verdict": "AMBIGU", "note": f"Erreur: {str(e)[:60]}"}

    # Sauvegarder dans cache
    cache["results"].update(all_results)
    cache["done"].append(tf)
    cache["last_updated"] = datetime.now().isoformat()
    atomic_write(CACHE_PATH, cache)

    valide_count = sum(1 for v in all_results.values() if v.get("verdict") == "VALIDE")
    log.info(f"\n  Cache mis a jour. Transcript {tf[:40]} : {valide_count}/{len(rules)} VALIDE")

    pending_left = [t for t in sorted(by_tf.keys()) if t not in set(cache["done"])]
    log.info(f"  Restants : {len(pending_left)} transcripts")
    if pending_left:
        log.info(f"  Prochain : {pending_left[0][:60]}")
        log.info(f"  -> Relance : py revalider_passe3_resume.py --next")
    else:
        log.info(f"  TOUS LES TRANSCRIPTS TRAITES !")
        log.info(f"  -> Finalise : py revalider_passe3_resume.py --merge")


def cmd_merge():
    cache = load_cache()
    if not cache.get("results"):
        log.error("Cache vide. Lance --next d'abord.")
        sys.exit(1)

    kb = load_kb()
    by_tf = extraire_pas_reponse(kb)
    done = set(cache.get("done", []))
    pending = [t for t in sorted(by_tf.keys()) if t not in done]
    if pending:
        log.warning(f"ATTENTION : {len(pending)} transcripts pas encore traites :")
        for t in pending:
            log.warning(f"  - {t[:60]}")
        rep = input("Fusionner quand meme ? (oui/NON) : ").strip().lower()
        if rep != "oui":
            log.info("Fusion annulee.")
            return

    results = cache.get("results", {})
    stats = {"VALIDE_gagne": 0, "INVALIDE_gagne": 0, "reste_AMBIGU": 0}

    for cat, buckets in kb.get("rules_by_status", {}).items():
        anciens = buckets.get("AMBIGU", [])
        nouveaux = []
        for entry in anciens:
            texte = entry.get("texte", "")
            if texte not in results:
                nouveaux.append(entry)
                stats["reste_AMBIGU"] += 1
                continue
            nv = results[texte]
            verdict = nv.get("verdict", "AMBIGU")
            if verdict == "VALIDE":
                e = dict(entry)
                e["statut"]    = "VALIDE"
                e["passage"]   = nv.get("passage")
                e["confiance"] = nv.get("confiance", 0.8)
                e["note"]      = f"[REVALIDE S14 passe3] {nv.get('note', '')}"
                buckets.setdefault("VALIDE", []).append(e)
                stats["VALIDE_gagne"] += 1
            elif verdict == "INVALIDE":
                e = dict(entry)
                e["statut"]    = "INVALIDE"
                e["passage"]   = None
                e["confiance"] = nv.get("confiance", 0.1)
                e["note"]      = f"[REVALIDE S14 passe3] {nv.get('note', '')}"
                buckets.setdefault("INVALIDE", []).append(e)
                stats["INVALIDE_gagne"] += 1
            else:
                nouveaux.append(entry)
                stats["reste_AMBIGU"] += 1
        buckets["AMBIGU"] = nouveaux

    kb.setdefault("metadata", {})["revalidation_s14_passe3"] = {
        "date": datetime.now().isoformat(),
        "stats": stats,
    }
    atomic_write(KB_VALIDEE_PATH, kb)

    # Regenerer A_VERIFIER_HUMAIN.md
    ambigus = []
    for cat, buckets in kb.get("rules_by_status", {}).items():
        for entry in buckets.get("AMBIGU", []):
            vid_id = entry.get("source_video_id", "")
            ambigus.append({
                "categorie": cat, "regle": entry.get("texte", ""),
                "video_id": vid_id,
                "transcript_file": entry.get("source_transcript", ""),
                "youtube_url": (f"https://youtube.com/watch?v={vid_id}"
                                if vid_id and vid_id not in ("ORPHAN", "FOUND_CROSS_CORPUS", "")
                                else "URL inconnue"),
                "note": entry.get("note", ""),
            })

    lines = [
        "# REGLES A VERIFIER HUMAINEMENT (apres revalidation S14 passe3)",
        "",
        f"> Genere le {datetime.now().strftime('%d/%m/%Y a %H:%M')}",
        f"> **{len(ambigus)} regles AMBIGU restantes** (apres 3e passe automatique)",
        "",
        "## Comment utiliser ce fichier",
        "",
        "Pour chaque regle ci-dessous :",
        "1. Clique sur le lien YouTube",
        "2. Cherche le sujet dans la video (quelques minutes suffisent)",
        "3. Belkhayate le dit clairement -> ecris **VALIDE**",
        "4. Absent ou contredit -> ecris **INVALIDE**",
        "",
        "---",
        "",
    ]
    for idx, a in enumerate(ambigus, 1):
        lines += [
            f"## #{idx:03d} -- {a['categorie'].upper()}",
            f"**Regle :** {a['regle']}",
            f"**Video :** `{a['transcript_file']}`",
            f"**Lien :** {a['youtube_url']}",
            f"**Note :** *{a['note']}*",
            "",
            "**Ton verdict :** [ ] VALIDE  [ ] INVALIDE",
            "",
            "---",
            "",
        ]
    with open(HUMAIN_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    totaux = {}
    for buckets in kb.get("rules_by_status", {}).values():
        for st, rules in buckets.items():
            totaux[st] = totaux.get(st, 0) + len(rules)

    log.info(f"\n{'='*60}")
    log.info(f"FUSION TERMINEE")
    log.info(f"  +VALIDE   : {stats['VALIDE_gagne']}")
    log.info(f"  +INVALIDE : {stats['INVALIDE_gagne']}")
    log.info(f"  AMBIGU    : {stats['reste_AMBIGU']}")
    log.info(f"  ---")
    for st in ["VALIDE", "INVALIDE", "AMBIGU"]:
        nb = totaux.get(st, 0)
        log.info(f"  {st:<10} : {nb}")
    log.info(f"  A_VERIFIER_HUMAIN.md : {len(ambigus)} cas")
    log.info(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--status",   action="store_true")
    parser.add_argument("--next",     action="store_true")
    parser.add_argument("--merge",    action="store_true")
    parser.add_argument("--dry-run",  action="store_true")
    args = parser.parse_args()

    if args.status:   cmd_status()
    elif args.next:   cmd_next(dry_run=args.dry_run)
    elif args.merge:  cmd_merge()
    else:
        print("Usage: py revalider_passe3_resume.py --status | --next | --merge | --dry-run --next")


if __name__ == "__main__":
    main()
