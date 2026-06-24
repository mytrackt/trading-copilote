# -*- coding: utf-8 -*-
"""Runner batch generique : execute un scraper sur une file <url><TAB><nom>.

Usage : py run_queue.py <queue.tsv> <scraper.py> <source> [--start N]
Journalise dans <queue>.log (1 ligne/page : OK/REJET/ERR + code).
Reprend proprement : saute une page dont le bundle .md existe deja.
"""
import os
import subprocess
import sys
import time

BASE = os.path.dirname(os.path.abspath(__file__))


def main():
    queue, scraper, source = sys.argv[1], sys.argv[2], sys.argv[3]
    start = 0
    if "--start" in sys.argv:
        start = int(sys.argv[sys.argv.index("--start") + 1])

    rows = [l.split("\t") for l in
            open(os.path.join(BASE, queue), encoding="utf-8").read().splitlines() if l.strip()]
    log = os.path.join(BASE, queue + ".log")
    total = len(rows)
    ok = rejet = err = skip = 0

    with open(log, "a", encoding="utf-8") as lf:
        lf.write(f"\n=== RUN {source} | {total} pages | start={start} ===\n")
        lf.flush()
        for i, (url, nom) in enumerate(rows):
            if i < start:
                continue
            bundle = os.path.join(BASE, "bundles", source, nom + ".md")
            if os.path.exists(bundle):
                skip += 1
                line = f"[{i+1}/{total}] SKIP (existe) {nom}"
                print(line, flush=True)
                lf.write(line + "\n"); lf.flush()
                continue
            try:
                r = subprocess.run(
                    ["py", os.path.join(BASE, scraper), url, source, nom],
                    capture_output=True, text=True, timeout=300)
                code = r.returncode
                if code == 0:
                    ok += 1; tag = "OK"
                elif code == 3:
                    rejet += 1; tag = "REJET-scope"
                elif code == 2:
                    rejet += 1; tag = "REJET-http"
                else:
                    err += 1; tag = f"ERR({code})"
            except subprocess.TimeoutExpired:
                err += 1; tag = "TIMEOUT"
            except Exception as e:
                err += 1; tag = f"EXC:{e}"
            line = f"[{i+1}/{total}] {tag} {nom}"
            print(line, flush=True)
            lf.write(line + "\n"); lf.flush()
            time.sleep(1)  # politesse entre pages

        summary = f"=== FIN {source} : OK={ok} REJET={rejet} ERR={err} SKIP={skip} ==="
        print(summary, flush=True)
        lf.write(summary + "\n"); lf.flush()


if __name__ == "__main__":
    main()
