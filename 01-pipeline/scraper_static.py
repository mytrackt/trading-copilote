# -*- coding: utf-8 -*-
"""
Agent 1bis - Scraper STATIQUE TRADEX-AI (sites HTML hors GitBook) - v1.

Complement de scraper.py (GitBook). Pour les sites HTML classiques rendus
cote serveur (bollingerbands, optimusfutures, investopedia, etc.).

CERTIFICATION IMAGE (adaptation du double ancrage a une source unique) :
  - Une image n'est CERTIFIEE que si elle est dans un <figure> avec une
    <figcaption> NON VIDE (legende ecrite par l'auteur, liee localement a
    l'image). Si un attribut alt non vide est present, il est note comme
    second ancrage (figcaption+alt).
  - Image sans figcaption -> (decorative) IGNOREE (jamais devinee).
  - Aucune invention : pas de figcaption = pas de label.

TEXTE : extraction du contenu principal (article/main/body) en .md brut.
Le texte d'une page est toujours certifiable (c'est la source litterale).

Usage : py scraper_static.py "<URL>" <source> <nom_page>
"""

import os
import re
import sys
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
}
TIMEOUT = 25
MIN_CONTENU = 500
SLEEP_IMG = 2

MOTS_CLES = [
    "moving average", "rsi", "macd", "adx", "atr", "bollinger", "candlestick",
    "pattern", "support", "resistance", "trend", "volume", "futures",
    "price action", "vwap", "stochastic", "obv", "divergence", "breakout",
    "market profile", "footprint", "delta", "order flow", "wyckoff",
    "backtest", "walk-forward", "overfitting", "bias", "cot",
]

EXT_PAR_TYPE = {
    "image/png": ".png", "image/jpeg": ".jpg", "image/jpg": ".jpg",
    "image/gif": ".gif", "image/webp": ".webp", "image/svg+xml": ".svg",
}


def telecharger_html(url):
    print(f"[1] Telechargement HTML : {url}")
    r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
    print(f"    Reponse serveur : HTTP {r.status_code}")
    if r.status_code != 200:
        print(f"REJETE : HTTP {r.status_code} (probable anti-bot/JS).")
        return None
    if "html" not in r.headers.get("content-type", ""):
        print("REJETE : reponse non-HTML.")
        return None
    # Fix encodage : eviter le defaut ISO-8859-1 quand le charset n'est pas
    # declare dans l'en-tete (sinon mojibake sur apostrophes/accents).
    if r.encoding is None or r.encoding.lower() in ("iso-8859-1", "latin-1"):
        r.encoding = r.apparent_encoding or "utf-8"
    if len(r.text) < MIN_CONTENU:
        print(f"REJETE : contenu trop court ({len(r.text)} car).")
        return None
    print(f"    OK : {len(r.text)} caracteres.")
    return r.text


def pre_selecteur(texte):
    print("[2] Pre-selecteur (mots-cles TRADEX)...")
    bas = texte.lower()
    trouves = [mc for mc in MOTS_CLES if mc in bas]
    if not trouves:
        print("REJETE : hors scope TRADEX.")
        return False
    print(f"GARDE : mots-cles -> {', '.join(trouves[:10])}")
    return True


def extraire_contenu(soup):
    """Renvoie l'element de contenu principal (article/main) ou body."""
    for sel in ("article", "main", "div[role=main]"):
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > MIN_CONTENU:
            return el
    return soup.body or soup


def texte_markdown(contenu):
    """Texte brut lisible : titres prefixes #, paragraphes, listes."""
    lignes = []
    for el in contenu.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        t = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
        if not t:
            continue
        tag = el.name
        if tag in ("h1", "h2", "h3", "h4"):
            lignes.append("\n" + "#" * int(tag[1]) + " " + t)
        elif tag == "li":
            lignes.append("- " + t)
        else:
            lignes.append(t)
    return "\n\n".join(lignes)


def section_courante(fig):
    """Dernier titre h1-h4 precedant la figure dans le flux du document."""
    titres = fig.find_all_previous(["h1", "h2", "h3", "h4"])
    if titres:
        return re.sub(r"\s+", " ", titres[0].get_text(" ", strip=True)).strip()
    return "(aucune section)"


def _slug_corrobore(label, src):
    """True si >=2 mots du label (>3 lettres) apparaissent dans le nom de
    fichier de l'image -> second ancrage independant de l'alt/figcaption."""
    fichier = os.path.basename(src.split("?")[0]).lower()
    fichier = re.sub(r"[^a-z0-9]+", " ", fichier)
    mots = [m for m in re.sub(r"[^a-z0-9]+", " ", label.lower()).split() if len(m) > 3]
    hits = sum(1 for m in mots if m in fichier)
    return hits >= 2


def collecter_figures(contenu, base_url):
    """Figures <figure> contenant un <img>. Label = figcaption non vide,
    sinon alt non vide. Certification notee selon les ancrages disponibles.
    Les <figure> sans <img> (embeds video, etc.) sont ignorees."""
    out = []
    for fig in contenu.find_all("figure"):
        img = fig.find("img")
        if img is None:
            continue  # embed (YouTube, iframe...) -> pas une image de contenu
        cap = fig.find("figcaption")
        figcap = re.sub(r"\s+", " ", cap.get_text(" ", strip=True)).strip() if cap else ""
        alt = re.sub(r"\s+", " ", (img.get("alt") or "")).strip()
        src = img.get("src") or img.get("data-src") or ""
        # v1.1 : resolution robuste des URLs (relatif / absolu / scheme-relative)
        if src:
            src = urljoin(base_url, src)

        # Label + base d'ancrage (transparence dans le manifest)
        if figcap:
            label = figcap
            ancrage = "figcaption+alt" if alt else "figcaption"
        elif alt:
            label = alt
            ancrage = "alt+filename" if _slug_corrobore(alt, src) else "alt-seul"
        else:
            label, ancrage = "", "aucun"
        out.append({"label": label, "ancrage": ancrage, "src": src,
                    "section": section_courante(fig)})
    return out


def extension(reponse, url):
    ctype = reponse.headers.get("content-type", "").split(";")[0].strip().lower()
    if ctype in EXT_PAR_TYPE:
        return EXT_PAR_TYPE[ctype]
    ext = os.path.splitext(url.split("?")[0])[1].lower()
    return ext if ext in EXT_PAR_TYPE.values() else ".img"


def telecharger_image(url, dossier, numero, cache):
    if not url or url in cache:
        return cache.get(url)
    time.sleep(SLEEP_IMG)
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200 or not r.headers.get("content-type", "").startswith("image/"):
            print(f"    ATTENTION : image HTTP {r.status_code} / non-image ignoree.")
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


def scraper(html, source, nom_page, url):
    dossier = os.path.join(BASE_DIR, "bundles", source)
    dossier_img = os.path.join(dossier, nom_page, "images")
    os.makedirs(dossier_img, exist_ok=True)

    soup = BeautifulSoup(html, "html.parser")
    contenu = extraire_contenu(soup)

    chemin_md = os.path.join(dossier, f"{nom_page}.md")
    with open(chemin_md, "w", encoding="utf-8") as f:
        f.write(f"# SOURCE: {url}\n\n")
        f.write(texte_markdown(contenu))
    print(f"[3] Texte sauvegarde : {chemin_md}")

    figures = collecter_figures(contenu, url)
    print(f"[4] Figures <figure>+<figcaption> trouvees : {len(figures)}")

    lignes, cache = [], {}
    numero = nb_cert = nb_deco = 0
    for i, fig in enumerate(figures):
        if not fig["label"]:
            nb_deco += 1
            lignes.append(f"(decorative) | rang {i+1} | section : {fig['section']} | sans figcaption -> IGNOREE")
            continue
        nom = telecharger_image(fig["src"], dossier_img, numero + 1, cache)
        if nom is None:
            lignes.append(f"(A VERIFIER) | rang {i+1} | telechargement echoue | label : {fig['label'][:50]} | url : {fig['src']}")
            continue
        numero += 1
        nb_cert += 1
        lignes.append(
            f"{nom} | label : {fig['label'][:70]} | section : {fig['section']} "
            f"| CERTIFIE ({fig['ancrage']})")

    nb_manuel = sum(1 for l in lignes if l.startswith("(A VERIFIER)"))
    chemin_manifest = os.path.join(dossier, f"{nom_page}_manifest.txt")
    with open(chemin_manifest, "w", encoding="utf-8") as f:
        f.write(f"# Manifest images pour {nom_page} (source : {source}) [STATIC]\n")
        f.write(f"# Page : {url}\n")
        f.write(f"# Methode : ancrage figcaption locale (source unique HTML) + alt si present\n")
        f.write(f"# Bilan : {nb_cert} certifiee(s) | {nb_manuel} a verifier | {nb_deco} decorative(s)\n\n")
        f.write("\n".join(lignes) if lignes else "(aucune figure <figure>+<figcaption> sur la page)")

    print(f"[5] Manifest ecrit : {chemin_manifest}")
    print(f"    BILAN -> {nb_cert} certifiee(s) | {nb_manuel} a verifier | {nb_deco} decorative(s)")
    if nb_manuel:
        print("\n/!\\  Traitement manuel requis (voir manifest).")
    else:
        print("\nOK : figures certifiees par figcaption (ou aucune figure).")
    print("\nNB : sur source HTML unique, certification = figcaption locale "
          "(pas le double ancrage .md+HTML du GitBook). Texte = source litterale.")


def main():
    if len(sys.argv) != 4:
        print('Usage : py scraper_static.py "<URL>" <source> <nom_page>')
        sys.exit(1)
    url, source, nom_page = sys.argv[1], sys.argv[2], sys.argv[3]
    print("=" * 64)
    print(f"AGENT 1bis - Scraper STATIC TRADEX | source={source} | page={nom_page}")
    print("=" * 64)
    html = telecharger_html(url)
    if html is None:
        sys.exit(2)
    if not pre_selecteur(html):
        sys.exit(3)
    scraper(html, source, nom_page, url)
    print("\nTERMINE : bundle pret pour l'Agent 2 (analyse).")


if __name__ == "__main__":
    main()
