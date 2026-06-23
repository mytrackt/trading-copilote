# -*- coding: utf-8 -*-
"""
Agent 1ter - Scraper PDF TRADEX-AI - v1.

Pour les sources PDF (CME backtesting, Cannon behavioral finance, etc.).

CERTIFICATION (strategie §3.3) :
  - TEXTE : extrait directement du PDF (pdfplumber) = source litterale fiable.
  - IMAGES : NON certifiables automatiquement (pas de legende structuree
    fiable dans un PDF) -> extraction MANUELLE par defaut. Le manifest liste
    le nombre d'images detectees par page comme rappel, jamais comme certifie.

Accepte une URL (telechargement) ou un chemin local .pdf.
Usage : py scraper_pdf.py "<URL_ou_chemin.pdf>" <source> <nom_page>
"""

import os
import sys

import requests
import pdfplumber

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
}
TIMEOUT = 30
MIN_CONTENU = 500

MOTS_CLES = [
    "backtest", "walk-forward", "overfitting", "sharpe", "bias", "behavioral",
    "trading", "trend", "volatility", "risk", "drawdown", "momentum",
    "market", "price", "volume", "futures",
]


def obtenir_pdf(source_arg, dossier):
    """Renvoie le chemin local du PDF (telecharge si URL)."""
    if source_arg.lower().startswith("http"):
        print(f"[1] Telechargement PDF : {source_arg}")
        r = requests.get(source_arg, headers=HEADERS, timeout=TIMEOUT)
        print(f"    Reponse serveur : HTTP {r.status_code}")
        if r.status_code != 200:
            print(f"REJETE : HTTP {r.status_code} (probable anti-bot).")
            return None
        if "pdf" not in r.headers.get("content-type", "").lower():
            print(f"REJETE : content-type non-PDF ({r.headers.get('content-type')}).")
            return None
        chemin = os.path.join(dossier, "source.pdf")
        with open(chemin, "wb") as f:
            f.write(r.content)
        print(f"    OK : {len(r.content)} octets -> {chemin}")
        return chemin
    if os.path.isfile(source_arg) and source_arg.lower().endswith(".pdf"):
        print(f"[1] PDF local : {source_arg}")
        return source_arg
    print("REJETE : argument ni URL http ni fichier .pdf existant.")
    return None


def pre_selecteur(texte):
    print("[2] Pre-selecteur (mots-cles TRADEX)...")
    bas = texte.lower()
    trouves = [mc for mc in MOTS_CLES if mc in bas]
    if not trouves:
        print("REJETE : hors scope TRADEX.")
        return False
    print(f"GARDE : mots-cles -> {', '.join(trouves[:10])}")
    return True


def main():
    if len(sys.argv) != 4:
        print('Usage : py scraper_pdf.py "<URL_ou_chemin.pdf>" <source> <nom_page>')
        sys.exit(1)
    source_arg, source, nom_page = sys.argv[1], sys.argv[2], sys.argv[3]
    print("=" * 64)
    print(f"AGENT 1ter - Scraper PDF TRADEX | source={source} | page={nom_page}")
    print("=" * 64)

    dossier = os.path.join(BASE_DIR, "bundles", source)
    os.makedirs(dossier, exist_ok=True)

    chemin_pdf = obtenir_pdf(source_arg, dossier)
    if chemin_pdf is None:
        sys.exit(2)

    print("[3] Extraction texte (pdfplumber)...")
    pages_txt, nb_images = [], 0
    with pdfplumber.open(chemin_pdf) as pdf:
        nb_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            t = page.extract_text() or ""
            nb_images += len(page.images)
            pages_txt.append(f"\n\n===== PAGE {i}/{nb_pages} =====\n{t}")
    texte = "".join(pages_txt)
    print(f"    {nb_pages} page(s) | {len(texte)} caracteres | {nb_images} image(s) detectee(s)")

    if len(texte) < MIN_CONTENU:
        print(f"REJETE : texte extrait trop court ({len(texte)} car) - PDF scanne/image ?")
        sys.exit(3)
    if not pre_selecteur(texte):
        sys.exit(4)

    chemin_md = os.path.join(dossier, f"{nom_page}.md")
    with open(chemin_md, "w", encoding="utf-8") as f:
        f.write(f"# SOURCE PDF: {source_arg}\n")
        f.write(texte)
    print(f"[4] Texte sauvegarde : {chemin_md}")

    chemin_manifest = os.path.join(dossier, f"{nom_page}_manifest.txt")
    with open(chemin_manifest, "w", encoding="utf-8") as f:
        f.write(f"# Manifest PDF pour {nom_page} (source : {source})\n")
        f.write(f"# Fichier : {chemin_pdf} | pages : {nb_pages}\n")
        f.write(f"# Methode : pdfplumber (texte). Images = MANUEL (strategie §3.3).\n")
        f.write(f"# Bilan : texte=OK | images_auto=0 | images_detectees={nb_images}\n\n")
        f.write(f"texte_{nom_page}.md | {nb_pages} pages | CERTIFIE (extrait direct PDF)\n")
        if nb_images:
            f.write(f"(images) | {nb_images} image(s) detectee(s) dans le PDF | A EXTRAIRE MANUELLEMENT si besoin\n")
    print(f"[5] Manifest ecrit : {chemin_manifest}")
    print("\nTERMINE : texte certifie. Images = traitement manuel si necessaire.")


if __name__ == "__main__":
    main()
