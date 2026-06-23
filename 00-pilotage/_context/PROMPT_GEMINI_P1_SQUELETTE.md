# PROMPT GEMINI — PHASE 1/3 : SQUELETTE + UTILITAIRES
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code
# Prerequis : pip install google-generativeai python-dotenv (deja fait)

---

## OBJECTIF DE CETTE PHASE

Creer le fichier `05-saas\utils\gemini_transcriber.py` avec :
- Tous les imports
- Toutes les constantes
- 3 fonctions utilitaires simples : detecter_qualite(), est_live(), flaguer_chiffres_visuels()
- Des STUBS vides pour les fonctions complexes (construire_prompt, transcrire_video, main)

La validation de cette phase = `python -m py_compile` sans erreur.

---

## VERIFICATION PREALABLE

Avant de creer le fichier, verifier :

1. Le fichier existe-t-il deja ?
   ```
   dir C:\trading-copilote\05-saas\utils\gemini_transcriber.py
   ```
   Si oui → faire un backup AVANT d'ecraser :
   ```
   copy C:\trading-copilote\05-saas\utils\gemini_transcriber.py C:\trading-copilote\05-saas\utils\gemini_transcriber.py.bak
   ```
   Rollback si probleme : `copy gemini_transcriber.py.bak gemini_transcriber.py`

2. Le dossier de sortie existe-t-il ?
   ```
   dir C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\
   ```
   Le sous-dossier `transcripts-gemini\` sera cree par le script (mkdir exist_ok).

---

## FICHIER A CREER

`C:\trading-copilote\05-saas\utils\gemini_transcriber.py`

Contenu exact :

```python
"""
Gemini Multimodal Transcriber — TRADEX-AI
Transcription audio + visuel des videos Belkhayate via Gemini 1.5 Flash.
Construit en 3 phases — Phase 1 : squelette et utilitaires.
Audit v2.2 applique — toutes corrections bloquantes integrees.
Usage personnel uniquement. Pas de conseil financier.
"""

import os
import sys
import time
import re
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

# Charger .env — chemin absolu obligatoire (Windows)
load_dotenv(r"C:\trading-copilote\.env")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# CONFIGURATION
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY manquant dans C:\\trading-copilote\\.env\n"
        "Ajouter la ligne : GEMINI_API_KEY=AIzaSy..."
    )

VIDEO_DIR = Path(r"D:\Belkhayate-Videos")
OUTPUT_DIR = Path(
    r"C:\trading-copilote\03-transcriptions"
    r"\nouvelles-sources\belkhayate-youtube\transcripts-gemini"
)
RAPPORT_PATH = Path(
    r"C:\trading-copilote\03-transcriptions"
    r"\nouvelles-sources\belkhayate-youtube\RAPPORT_QUALITE_GEMINI.md"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Modele stable (pas experimental)
genai.configure(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# Timeouts et retry
MAX_PROCESSING_WAIT_SECONDS = 300   # 5 min max pour l'upload Gemini
MAX_RETRIES = 3
RETRY_BACKOFF = [10, 30, 60]        # secondes entre tentatives

# Mots-cles detection video live
KEYWORDS_LIVE = ["live", "5 days challenge", "5 days", "session live", "trading live"]

# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================

def detecter_qualite(video_path: Path) -> str:
    """
    Evalue la qualite probable de la video par taille.
    Retourne FAIBLE_APPROX / MOYENNE_APPROX / BONNE_APPROX.
    Note : taille = proxy imparfait (H.265 compresse peut etre HD a 15 Mo).
    Le suffixe _APPROX rappelle que c'est une estimation.
    """
    taille_mo = video_path.stat().st_size / (1024 * 1024)
    if taille_mo < 30:
        return "FAIBLE_APPROX"
    elif taille_mo < 150:
        return "MOYENNE_APPROX"
    else:
        return "BONNE_APPROX"


def est_live(nom_fichier: str) -> bool:
    """
    Detecte si la video est un live trading par son nom.
    Insensible a la casse.
    """
    nom_lower = nom_fichier.lower()
    return any(kw.lower() in nom_lower for kw in KEYWORDS_LIVE)


def flaguer_chiffres_visuels(texte: str) -> str:
    """
    Dans chaque bloc [VISUEL: ...], ajoute le flag A_VERIFIER
    apres chaque chiffre. Insensible a la casse (re.IGNORECASE).
    Multiligne (re.DOTALL) pour les blocs qui s'etendent sur plusieurs lignes.

    Exemple :
      Entree : [VISUEL: COG a 1852, prix actuel 1848]
      Sortie : [VISUEL: COG a 1852A_VERIFIER, prix actuel 1848A_VERIFIER]
    """
    def remplacer_chiffres(match):
        bloc = match.group(0)
        return re.sub(r'\b(\d+[\.,]?\d*)\b', r'\1⚠️_A_VERIFIER', bloc)

    return re.sub(
        r'\[VISUEL:.*?\]',
        remplacer_chiffres,
        texte,
        flags=re.DOTALL | re.IGNORECASE
    )


# ============================================================
# STUBS — seront remplis en Phase 2 et Phase 3
# ============================================================

def construire_prompt(nom_fichier: str, est_live_video: bool) -> str:
    """STUB Phase 2 — construit le prompt Gemini adapte au type de video."""
    raise NotImplementedError("construire_prompt() sera implemente en Phase 2")


def transcrire_video(video_path: Path) -> dict:
    """STUB Phase 2 — upload + transcription Gemini avec retry et timeout."""
    raise NotImplementedError("transcrire_video() sera implemente en Phase 2")


def main():
    """STUB Phase 3 — boucle principale sur toutes les videos."""
    raise NotImplementedError("main() sera implemente en Phase 3")


# ============================================================
# POINT D'ENTREE
# ============================================================

if __name__ == "__main__":
    main()
```

---

## VALIDATION OBLIGATOIRE

Executer dans PowerShell depuis `C:\trading-copilote` :

```
python -m py_compile 05-saas\utils\gemini_transcriber.py
```

Resultat attendu : aucune sortie = pas d'erreur de syntaxe = OK.

Si erreur → corriger avant de continuer. Afficher l'erreur complete.

Puis tester fonctionnellement les 3 utilitaires (sans appeler Gemini) :

```
python -c "
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location('g', r'C:\trading-copilote\05-saas\utils\gemini_transcriber.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

assert m.est_live('trading_live_or.mp4') == True, 'est_live FAIL sur live'
assert m.est_live('lecon_01_belkhayate.mp4') == False, 'est_live FAIL sur cours'
assert m.est_live('5 Days Challenge Gold.mp4') == True, 'est_live FAIL sur 5days'

t = m.flaguer_chiffres_visuels('[VISUEL: COG a 1852, prix 1848]')
assert 'A_VERIFIER' in t, 'flaguer_chiffres_visuels FAIL'

t2 = m.flaguer_chiffres_visuels('pas de visuel ici 1852')
assert 'A_VERIFIER' not in t2, 'flaguer_chiffres FAIL hors VISUEL'

print('Utilitaires OK — est_live / flaguer_chiffres_visuels valides')
"
```

Resultat attendu : `Utilitaires OK — est_live / flaguer_chiffres_visuels valides`

---

## CHECKLIST PHASE 1

- [ ] Fichier cree : `05-saas\utils\gemini_transcriber.py`
- [ ] `python -m py_compile` passe sans erreur
- [ ] Les 3 fonctions utilitaires sont presentes (detecter_qualite, est_live, flaguer_chiffres_visuels)
- [ ] Les 3 stubs sont presents (construire_prompt, transcrire_video, main)
- [ ] Le fichier ne contient pas de cle API en dur

NE PAS committer a la fin de cette phase — attendre la Phase 3 (complete).
NE PAS lancer Phase 2 sans confirmation que la Phase 1 est validee.
