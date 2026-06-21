# -*- coding: utf-8 -*-
"""
Agent 1 — Scraper + Pre-selecteur pour TRADEX-AI (Pipeline KB Option B, Phase 1).

Recupere la version Markdown (.md) d'une page GitBook ChartSchool (source de verite
pour le texte et les sections), resout les vraies adresses d'images via la page HTML,
et telecharge tout en garantissant un lien texte<->image fiable (manifest).

Usage :
    py scraper.py "<URL>" <source> <nom_page>

Exemple :
    py scraper.py "https://chartschool.stockcharts.com/.../moving-averages-simple-and-exponential" stockcharts moving_averages

6 garde-fous :
    1. Telecharger le .md
    2. Detecter la page d'erreur deguisee ("# Page Not Found") -> arret
    3. Pre-selecteur par mots-cles
    4. Resoudre les vraies images via le HTML + telecharger (type reel + dedoublonnage)
    5. Generer le manifest texte<->image (section juste au-dessus de chaque image)
    6. Anti-ambiguite : si 2 images partagent le MEME texte alt -> ALERTE + marquage
       "association ambigue a verifier manuellement" (zero association incertaine silencieuse)
"""

import os
import re
import sys
import time
import html as htmllib

import requests

# --- Constantes ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = "https://chartschool.stockcharts.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (TRADEX-AI Phase1 scraper)"}
TIMEOUT = 25
MIN_CONTENU = 500  # taille minimale (caracteres) pour considerer la page valide

MOTS_CLES = [
    "moving average", "rsi", "macd", "adx", "atr", "bollinger", "candlestick",
    "pattern", "support", "resistance", "trend", "volume", "futures",
    "price action", "vwap", "stochastic", "obv", "divergence", "breakout",
]

# Type de fichier reel -> extension (les URL GitBook n'ont pas d'extension)
EXT_PAR_TYPE = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
}


def construire_url_md(url):
    """Ajoute '.md' a la fin de l'URL si absent ; renvoie aussi l'URL HTML (sans .md)."""
    url = url.strip().rstrip("/")
    if url.endswith(".md"):
        url_html = url[:-3]
    else:
        url_html = url
        url = url + ".md"
    return url, url_html


def telecharger_markdown(url_md):
    """Garde-fou 1+2 : recupere le .md et refuse une page d'erreur deguisee."""
    print(f"[1] Telechargement du Markdown : {url_md}")
    r = requests.get(url_md, headers=HEADERS, timeout=TIMEOUT)
    print(f"    Reponse serveur : HTTP {r.status_code}")
    if r.status_code != 200:
        print(f"REJETE : le serveur a renvoye une erreur HTTP {r.status_code}.")
        return None

    texte = r.text
    if "# Page Not Found" in texte or "does not exist" in texte:
        print("REJETE : page introuvable (erreur deguisee en 'HTTP 200').")
        for titre, lien in re.findall(r"\[([^\]]+)\]\((https://[^)]+\.md)\)", texte)[:6]:
            print(f"      - {titre} -> {lien}")
        return None

    if len(texte) < MIN_CONTENU:
        print(f"REJETE : contenu trop court ({len(texte)} caracteres < {MIN_CONTENU}).")
        return None

    print(f"    OK : {len(texte)} caracteres recuperes.")
    return texte


def pre_selecteur(texte):
    """Garde-fou 3 : la page contient-elle au moins un mot-cle TRADEX ?"""
    print("[2] Pre-selecteur (mots-cles TRADEX)...")
    bas = texte.lower()
    trouves = [mc for mc in MOTS_CLES if mc in bas]
    if not trouves:
        print("REJETE : page hors scope TRADEX (aucun mot-cle trouve).")
        return False
    print(f"GARDE : mots-cles trouves -> {', '.join(trouves)}")
    return True


def normaliser_alt(valeur):
    """Nettoie un texte alt pour permettre une comparaison fiable .md <-> HTML."""
    return re.sub(r"\s+", " ", htmllib.unescape(valeur or "")).strip()


def resoudre_images_html(url_html):
    """Garde-fou 4 : lit la page HTML et associe chaque texte alt a ses vraies URL.

    Renvoie un dict : alt_normalise -> liste d'URL d'images (dans l'ordre du HTML).
    """
    print(f"[3] Resolution des vraies images via le HTML : {url_html}")
    r = requests.get(url_html, headers=HEADERS, timeout=TIMEOUT)
    if r.status_code != 200:
        print(f"    ATTENTION : HTML inaccessible (HTTP {r.status_code}). Images non resolues.")
        return {}

    alt_vers_urls = {}
    for tag in re.findall(r"<img\b[^>]*>", r.text):
        m_src = re.search(r'src="([^"]+)"', tag)
        m_alt = re.search(r'alt="([^"]*)"', tag)
        if not m_src or not m_alt:
            continue
        alt = normaliser_alt(m_alt.group(1))
        if not alt:
            continue  # images decoratives (alt vide) ignorees
        src = htmllib.unescape(m_src.group(1))
        alt_vers_urls.setdefault(alt, []).append(src)

    print(f"    {len(alt_vers_urls)} texte(s) alt distinct(s) trouves dans le HTML.")
    return alt_vers_urls


def extension_image(reponse, url):
    """Deduit l'extension a partir du vrai type de fichier."""
    ctype = reponse.headers.get("content-type", "").split(";")[0].strip().lower()
    if ctype in EXT_PAR_TYPE:
        return EXT_PAR_TYPE[ctype]
    ext_url = os.path.splitext(url)[1].lower()
    return ext_url if ext_url in EXT_PAR_TYPE.values() else ".img"


def nettoyer_titre(titre):
    """Retire les residus GitBook/Markdown d'un titre de section (lisibilite manifest)."""
    titre = re.sub(r"<[^>]+>", "", titre)        # balises HTML (ex. <a href=...>)
    titre = titre.replace("**", "").replace("`", "")  # gras / code Markdown
    titre = re.sub(r"\\([&#_*])", r"\1", titre)  # antislashs d'echappement (\& -> &)
    return re.sub(r"\s+", " ", titre).strip()


def titre_avant_position(texte, position):
    """Dernier titre Markdown (#..####) situe AVANT une position donnee (nettoye)."""
    titre = "(aucune section)"
    for m in re.finditer(r"^#{1,4}\s+(.*)$", texte, re.MULTILINE):
        if m.start() < position:
            titre = nettoyer_titre(m.group(1))
        else:
            break
    return titre


def telecharger_une_image(url_img, dossier_img, numero, cache):
    """Telecharge une image (avec dedoublonnage par URL). Renvoie le nom de fichier local ou None."""
    if url_img in cache:
        return cache[url_img]
    time.sleep(2)  # politesse serveur
    try:
        ri = requests.get(url_img, headers=HEADERS, timeout=TIMEOUT)
        if ri.status_code != 200:
            print(f"    ATTENTION : image HTTP {ri.status_code} ignoree.")
            return None
        ext = extension_image(ri, url_img)
        nom_fichier = f"image_{numero:02d}{ext}"
        with open(os.path.join(dossier_img, nom_fichier), "wb") as fi:
            fi.write(ri.content)
        cache[url_img] = nom_fichier
        print(f"    Telechargee : {nom_fichier}  ({len(ri.content)} octets)")
        return nom_fichier
    except Exception as e:
        print(f"    ERREUR telechargement image : {e}")
        return None


def scraper(texte, source, nom_page, alt_vers_urls):
    """Garde-fous 4+5+6 : sauvegarde texte, telecharge images, manifest + anti-ambiguite."""
    dossier = os.path.join(BASE_DIR, "bundles", source)
    dossier_img = os.path.join(dossier, "images")
    os.makedirs(dossier_img, exist_ok=True)

    chemin_md = os.path.join(dossier, f"{nom_page}.md")
    with open(chemin_md, "w", encoding="utf-8") as f:
        f.write(texte)
    print(f"[4] Markdown sauvegarde : {chemin_md}")

    occurrences = list(re.finditer(r'<img[^>]*>', texte))
    print(f"[5] Balises image dans le .md : {len(occurrences)}")

    # Pre-calcul : combien de fois chaque alt apparait cote .md (images de contenu)
    md_alts = []
    for occ in occurrences:
        m_alt = re.search(r'alt="([^"]*)"', occ.group(0))
        md_alts.append(normaliser_alt(m_alt.group(1)) if m_alt else "")
    compte_md = {}
    for a in md_alts:
        if a:
            compte_md[a] = compte_md.get(a, 0) + 1

    cache_url = {}            # URL -> nom fichier (dedoublonnage)
    urls_restantes = {a: list(v) for a, v in alt_vers_urls.items()}  # consommation par alt
    lignes_manifest = []
    numero = 0
    nb_ambigu = 0
    nb_ok = 0
    nb_decoratif = 0
    nb_absent = 0

    for occ, alt in zip(occurrences, md_alts):
        section = titre_avant_position(texte, occ.start())

        # Image decorative (alt vide) -> ignoree proprement
        if not alt:
            nb_decoratif += 1
            lignes_manifest.append(
                f"(decorative) | alt vide | section : {section} | IGNOREE"
            )
            continue

        urls_html = alt_vers_urls.get(alt, [])

        # GARDE-FOU 6 : ambiguite si le meme alt designe plusieurs images
        ambigu = compte_md.get(alt, 0) > 1 or len(urls_html) > 1

        if not urls_html:
            nb_absent += 1
            print(f"    ALERTE : alt absent du HTML, image non resolue -> section : {section}")
            lignes_manifest.append(
                f"(NON RESOLUE) | alt : {alt[:60]} | section : {section} "
                f"| ⚠️ image introuvable dans le HTML a verifier manuellement"
            )
            continue

        # Choisir l'URL : si ambigu, on prend la suivante non encore consommee (ordre HTML)
        restantes = urls_restantes.get(alt) or list(urls_html)
        url_img = restantes.pop(0) if restantes else urls_html[0]
        urls_restantes[alt] = restantes

        deja = url_img in cache_url
        if not deja:
            numero += 1
        nom_fichier = telecharger_une_image(url_img, dossier_img, numero, cache_url)
        if nom_fichier is None:
            if not deja:
                numero -= 1
            lignes_manifest.append(
                f"(ECHEC) | alt : {alt[:60]} | section : {section} "
                f"| ⚠️ telechargement echoue a verifier manuellement"
            )
            continue

        if ambigu:
            nb_ambigu += 1
            print(f"    ALERTE AMBIGUITE : plusieurs images partagent ce alt -> {nom_fichier}")
            lignes_manifest.append(
                f"{nom_fichier} | alt : {alt[:60]} | section : {section} "
                f"| ⚠️ association ambigue a verifier manuellement"
            )
        else:
            nb_ok += 1
            lignes_manifest.append(
                f"{nom_fichier} | alt : {alt[:60]} | section : {section} | OK"
            )

    chemin_manifest = os.path.join(dossier, f"{nom_page}_manifest.txt")
    with open(chemin_manifest, "w", encoding="utf-8") as f:
        f.write(f"# Manifest images pour {nom_page} (source : {source})\n")
        f.write(
            f"# Bilan : {nb_ok} OK | {nb_ambigu} ambigue(s) | "
            f"{nb_absent} non resolue(s) | {nb_decoratif} decorative(s) ignoree(s)\n\n"
        )
        f.write("\n".join(lignes_manifest))

    print(f"[6] Manifest ecrit : {chemin_manifest}")
    print(
        f"    BILAN -> {nb_ok} image(s) OK | {nb_ambigu} ambigue(s) | "
        f"{nb_absent} non resolue(s) | {nb_decoratif} decorative(s) ignoree(s)"
    )
    if nb_ambigu or nb_absent:
        print("    >>> Des associations doivent etre VERIFIEES MANUELLEMENT (voir manifest).")


def main():
    if len(sys.argv) != 4:
        print('Usage : py scraper.py "<URL>" <source> <nom_page>')
        sys.exit(1)

    url, source, nom_page = sys.argv[1], sys.argv[2], sys.argv[3]
    print("=" * 64)
    print(f"AGENT 1 — Scraper TRADEX | source={source} | page={nom_page}")
    print("=" * 64)

    url_md, url_html = construire_url_md(url)

    texte = telecharger_markdown(url_md)
    if texte is None:
        sys.exit(2)

    if not pre_selecteur(texte):
        sys.exit(3)

    alt_vers_urls = resoudre_images_html(url_html)
    scraper(texte, source, nom_page, alt_vers_urls)
    print("\nTERMINE : bundle pret pour l'Agent 2 (analyse).")


if __name__ == "__main__":
    main()
