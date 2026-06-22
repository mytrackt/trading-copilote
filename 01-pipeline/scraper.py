# -*- coding: utf-8 -*-
"""
Agent 1 - Scraper TRADEX-AI (Pipeline KB Option B) - v2 DOUBLE ANCRAGE.

Probleme resolu : sur ChartSchool (GitBook), le .md contient le LABEL certifie
(figcaption) mais une adresse image /files/ID NON telechargeable (404). Le HTML
rendu contient la VRAIE URL telechargeable mais sous un autre identifiant.

Solution (certification a deux sources) :
  - .md   : labels figcaption dans l'ordre (source 1, ecrite par l'auteur)
  - HTML  : chaque image suivie immediatement de sa legende -> (vraie_url, label)
            (source 2, ecrite par l'auteur, liee localement a l'image)
  - Une image n'est CERTIFIEE que si label .md == label HTML (meme rang).
  - Tout desaccord / comptes differents -> A VERIFIER MANUELLEMENT (jamais devine).

Usage : py scraper.py "<URL>" <source> <nom_page>
"""

import os
import re
import sys
import time
import html as htmllib

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = "https://chartschool.stockcharts.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (TRADEX-AI Phase1 scraper)"}
TIMEOUT = 25
MIN_CONTENU = 500
SLEEP_IMG = 2  # politesse serveur entre 2 telechargements

MOTS_CLES = [
    "moving average", "rsi", "macd", "adx", "atr", "bollinger", "candlestick",
    "pattern", "support", "resistance", "trend", "volume", "futures",
    "price action", "vwap", "stochastic", "obv", "divergence", "breakout",
]

EXT_PAR_TYPE = {
    "image/png": ".png", "image/jpeg": ".jpg", "image/jpg": ".jpg",
    "image/gif": ".gif", "image/webp": ".webp", "image/svg+xml": ".svg",
}


def construire_url_md(url):
    url = url.strip().rstrip("/")
    if url.endswith(".md"):
        return url, url[:-3]
    return url + ".md", url


def telecharger_markdown(url_md):
    print(f"[1] Telechargement du Markdown : {url_md}")
    r = requests.get(url_md, headers=HEADERS, timeout=TIMEOUT)
    print(f"    Reponse serveur : HTTP {r.status_code}")
    if r.status_code != 200:
        print(f"REJETE : HTTP {r.status_code}.")
        return None
    texte = r.text
    if "# Page Not Found" in texte or "does not exist" in texte:
        print("REJETE : page introuvable (erreur deguisee en 200).")
        return None
    if len(texte) < MIN_CONTENU:
        print(f"REJETE : contenu trop court ({len(texte)} car).")
        return None
    print(f"    OK : {len(texte)} caracteres.")
    return texte


def pre_selecteur(texte):
    print("[2] Pre-selecteur (mots-cles TRADEX)...")
    bas = texte.lower()
    trouves = [mc for mc in MOTS_CLES if mc in bas]
    if not trouves:
        print("REJETE : hors scope TRADEX.")
        return False
    print(f"GARDE : mots-cles -> {', '.join(trouves)}")
    return True


def normaliser(v):
    return re.sub(r"\s+", " ", htmllib.unescape(v or "")).strip()


def nettoyer_titre(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("**", "").replace("`", "")
    t = re.sub(r"\\([&#_*])", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def labels_md(texte):
    """Source 1 : labels figcaption des blocs <figure> du .md, dans l'ordre.

    Renvoie une liste de dict : {label, section} (label '' = decorative).
    """
    out = []
    for m in re.finditer(r"<figure>.*?</figure>", texte, re.DOTALL):
        bloc = m.group(0)
        cap = re.search(r"<figcaption>(.*?)</figcaption>", bloc, re.DOTALL)
        label = normaliser(re.sub(r"<[^>]+>", " ", cap.group(1))) if cap else ""
        section = "(aucune section)"
        for h in re.finditer(r"^#{1,4}\s+(.*)$", texte, re.MULTILINE):
            if h.start() < m.start():
                section = nettoyer_titre(h.group(1))
            else:
                break
        out.append({"label": label, "section": section})
    return out


def images_html(url_html):
    """Source 2 : (vraie_url, label) du HTML rendu, dans l'ordre source.

    Regle d'ancrage local : chaque image de contenu (data-testid=zoom-image)
    prend la legende <figcaption> qui la suit IMMEDIATEMENT. Si le marqueur
    suivant n'est pas une legende -> label '' (decorative).
    """
    print(f"[3] Lecture du HTML rendu (vraies URL) : {url_html}")
    r = requests.get(url_html, headers=HEADERS, timeout=TIMEOUT)
    if r.status_code != 200:
        print(f"    ATTENTION : HTML HTTP {r.status_code}.")
        return None
    html = r.text
    toks = []
    motif = r'data-testid="zoom-image"[^>]*src="([^"]+)"|<figcaption[^>]*>(.*?)</figcaption>'
    for m in re.finditer(motif, html, re.DOTALL):
        if m.group(1):
            toks.append(("I", htmllib.unescape(m.group(1))))
        else:
            toks.append(("C", normaliser(re.sub(r"<[^>]+>", " ", m.group(2)))))
    images = []
    for i, (t, v) in enumerate(toks):
        if t == "I":
            label = toks[i + 1][1] if i + 1 < len(toks) and toks[i + 1][0] == "C" else ""
            images.append({"url": v, "label": label})
    print(f"    {len(images)} image(s) de contenu trouvee(s) dans le HTML.")
    return images


def extension(reponse, url):
    ctype = reponse.headers.get("content-type", "").split(";")[0].strip().lower()
    if ctype in EXT_PAR_TYPE:
        return EXT_PAR_TYPE[ctype]
    ext = os.path.splitext(url)[1].lower()
    return ext if ext in EXT_PAR_TYPE.values() else ".img"


def telecharger_image(url, dossier, numero, cache):
    if url in cache:
        return cache[url]
    time.sleep(SLEEP_IMG)
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            print(f"    ATTENTION : image HTTP {r.status_code} ignoree.")
            return None
        if not r.headers.get("content-type", "").startswith("image/"):
            print(f"    ATTENTION : reponse non-image ignoree.")
            return None
        nom = f"image_{numero:02d}{extension(r, url)}"
        with open(os.path.join(dossier, nom), "wb") as f:
            f.write(r.content)
        cache[url] = nom
        print(f"    Telechargee : {nom}  ({len(r.content)} octets)")
        return nom
    except Exception as e:
        print(f"    ERREUR telechargement : {e}")
        return None


def scraper(texte, source, nom_page, url_html):
    dossier = os.path.join(BASE_DIR, "bundles", source)
    dossier_img = os.path.join(dossier, "images")
    os.makedirs(dossier_img, exist_ok=True)

    chemin_md = os.path.join(dossier, f"{nom_page}.md")
    with open(chemin_md, "w", encoding="utf-8") as f:
        f.write(texte)
    print(f"[4] Markdown sauvegarde : {chemin_md}")

    src1 = labels_md(texte)
    src2 = images_html(url_html)
    if src2 is None:
        src2 = []

    print(f"[5] Source1 (.md figures) : {len(src1)} | Source2 (HTML images) : {len(src2)}")

    lignes, manuels = [], []
    cache = {}
    numero = 0
    nb_cert = nb_manuel = nb_deco = 0

    comptes_ok = (len(src1) == len(src2) and len(src1) > 0)
    if not comptes_ok:
        nb_manuel = max(len(src1), len(src2))
        manuels.append({
            "raison": f"comptes differents (.md={len(src1)} vs HTML={len(src2)})",
            "section": "(global)", "md": "", "html": "", "url": "(voir page)"})
        lignes.append(
            f"(A VERIFIER) | INTEGRITE : .md={len(src1)} figures vs HTML={len(src2)} images "
            f"| url : {url_html} | alignement impossible -> verifier manuellement")
    else:
        for i in range(len(src1)):
            md_label = src1[i]["label"]
            section = src1[i]["section"]
            html_label = src2[i]["label"]
            url_img = src2[i]["url"]

            if not md_label and not html_label:
                nb_deco += 1
                lignes.append(f"(decorative) | rang {i+1} | section : {section} | IGNOREE")
                continue

            if md_label.lower() != html_label.lower():
                nb_manuel += 1
                manuels.append({"raison": "desaccord .md vs HTML", "section": section,
                                "md": md_label or "(vide)", "html": html_label or "(vide)",
                                "url": url_img})
                lignes.append(
                    f"(A VERIFIER) | rang {i+1} | DESACCORD md='{md_label[:40]}' "
                    f"vs html='{html_label[:40]}' | section : {section} | url : {url_img}")
                continue

            numero_essai = numero + 1
            nom = telecharger_image(url_img, dossier_img, numero_essai, cache)
            if nom is None:
                nb_manuel += 1
                manuels.append({"raison": "telechargement echoue", "section": section,
                                "md": md_label, "html": html_label, "url": url_img})
                lignes.append(
                    f"(A VERIFIER) | rang {i+1} | telechargement echoue "
                    f"| label : {md_label[:40]} | url : {url_img}")
                continue
            numero = numero_essai
            nb_cert += 1
            lignes.append(
                f"{nom} | label : {md_label[:60]} | section : {section} "
                f"| CERTIFIE (accord .md + HTML)")

    chemin_manifest = os.path.join(dossier, f"{nom_page}_manifest.txt")
    with open(chemin_manifest, "w", encoding="utf-8") as f:
        f.write(f"# Manifest images pour {nom_page} (source : {source})\n")
        f.write(f"# Page : {url_html}\n")
        f.write(f"# Methode : double ancrage (.md figcaption + HTML legende locale)\n")
        f.write(f"# Bilan : {nb_cert} certifiee(s) | {nb_manuel} a verifier | "
                f"{nb_deco} decorative(s)\n\n")
        f.write("\n".join(lignes))

    print(f"[6] Manifest ecrit : {chemin_manifest}")
    print(f"    BILAN -> {nb_cert} certifiee(s) | {nb_manuel} a verifier | {nb_deco} decorative(s)")

    if manuels:
        print("\n" + "=" * 64)
        print("/!\\  TRAITEMENT MANUEL REQUIS - le pipeline n'est PAS sur a 100%")
        print("=" * 64)
        print(f"Page : {url_html}")
        for i, c in enumerate(manuels, 1):
            print(f"\n  [{i}] Raison    : {c['raison']}")
            print(f"      Section   : {c['section']}")
            if c["md"] or c["html"]:
                print(f"      label .md : {c['md']}")
                print(f"      label HTML: {c['html']}")
            print(f"      URL image : {c['url']}")
        print("\n  >>> Verifie ces images toi-meme sur la page ci-dessus.")
    else:
        print("\nOK : toutes les images CERTIFIEES (accord .md + HTML) - aucun manuel.")


def main():
    if len(sys.argv) != 4:
        print('Usage : py scraper.py "<URL>" <source> <nom_page>')
        sys.exit(1)
    url, source, nom_page = sys.argv[1], sys.argv[2], sys.argv[3]
    print("=" * 64)
    print(f"AGENT 1 - Scraper TRADEX v2 | source={source} | page={nom_page}")
    print("=" * 64)
    url_md, url_html = construire_url_md(url)
    texte = telecharger_markdown(url_md)
    if texte is None:
        sys.exit(2)
    if not pre_selecteur(texte):
        sys.exit(3)
    scraper(texte, source, nom_page, url_html)
    print("\nTERMINE : bundle pret pour l'Agent 2 (analyse).")


if __name__ == "__main__":
    main()
