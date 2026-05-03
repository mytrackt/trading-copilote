# CHECKLIST FICHIERS INUTILES — `C:\trading-copilote\`

> Document de proposition uniquement — **aucun fichier supprimé** dans ce document.
> Source : audit `ls -la` + `git ls-files` + `grep MBK` sur tous les .md.
> **Date** : 2026-05-03.
> Classement par priorité : 🔴 URGENT — 🟡 OPTIONNEL.
>
> ⚠️ **À LIRE AVANT TOUTE SUPPRESSION** :
> - Les fichiers marqués "tracked" sont dans git → `git rm <fichier>` (puis commit)
> - Les fichiers marqués "untracked" sont hors git → `rm <fichier>` (sans commit)
> - Les dossiers vides → `rmdir <dossier>` (Windows : `Remove-Item -Recurse`)

---

## 🔴 URGENT — 8 items (suppression sans risque)

### U1. 6 dossiers vides racine — doublons de `code/`

Vestiges du commit `a1e5205 refactor: migrate python modules from root to code/ directory` (les fichiers ont été déplacés mais les dossiers vides sont restés).

| Dossier | État | Doublon de | Tracked ? |
|---------|------|------------|-----------|
| `./api/` | vide | `code/api/` | non (dossiers vides non trackés) |
| `./collectors/` | vide | `code/collectors/` | non |
| `./config/` | vide | `code/config/` | non |
| `./engine/` | vide | `code/engine/` | non |
| `./execution/` | vide | `code/execution/` | non |
| `./utils/` | vide | `code/utils/` | non |

**Action recommandée** : `Remove-Item ./api, ./collectors, ./config, ./engine, ./execution, ./utils -Recurse`

---

### U2. `.tmp.drivedownload/` — sync Google Drive accidentel

| Item | Détail |
|------|--------|
| Chemin | `./.tmp.drivedownload/` |
| Contenu | 2 fichiers binaires anonymes (`355980.1777644066604324`, `...4119384664`) |
| Taille | ~0 B (placeholders) |
| Origine | Sync Google Drive — pas voulu dans le repo |
| `.gitignore` actuel | **NON ignoré** (seul `.tmp.driveupload/` l'est) |

**Action recommandée** :
1. Ajouter `/.tmp.drivedownload/` à `.gitignore`
2. `Remove-Item .tmp.drivedownload -Recurse -Force`

---

### U3. `.tmp.driveupload/` — sync Google Drive accidentel

| Item | Détail |
|------|--------|
| Chemin | `./.tmp.driveupload/` |
| Contenu | ~50+ fichiers binaires anonymes (`355091`, `355095`, ...) |
| Taille | **~400 MB** (le plus gros : `355139` = 49 MB) |
| Origine | Sync Google Drive — pas voulu dans le repo |
| `.gitignore` actuel | ✅ ignoré (`.tmp.driveupload/` ligne 1) |

**Action recommandée** : `Remove-Item .tmp.driveupload -Recurse -Force` (libère ~400 MB disque)

---

### U4. `CDC_MBK_TRADER_TECHNIQUE_v1.0.md` (racine)

| Item | Détail |
|------|--------|
| Chemin | `./CDC_MBK_TRADER_TECHNIQUE_v1.0.md` |
| Taille | 26 KB |
| Tracked ? | ✅ tracked |
| Doublon de | `docs/mbk-trader/CDC_MBK_TRADER_TECHNIQUE_v1.1.md` (version plus récente) |
| Pertinence projet | MBK Trader = projet en pause, TRADEX-AI le remplace (CLAUDE.md global) |

**Action recommandée** : `git rm CDC_MBK_TRADER_TECHNIQUE_v1.0.md` puis archiver `docs/mbk-trader/CDC_MBK_TRADER_TECHNIQUE_v1.1.md` vers `_archive/MBK/` (cf RAPPORT_REORGANISATION).

---

### U5. `CDC_MBK_TRADER_VISION_v1.0.md` (racine)

Identique à U4 — version v1.1 dans `docs/mbk-trader/`.

| Chemin | Taille | Tracked | Doublon de |
|--------|--------|---------|------------|
| `./CDC_MBK_TRADER_VISION_v1.0.md` | 6.3 KB | ✅ | `docs/mbk-trader/CDC_MBK_TRADER_VISION_v1.1.md` |

**Action recommandée** : `git rm CDC_MBK_TRADER_VISION_v1.0.md`.

---

### U6. `AUDIT_PROMPT_TRADING.md` (racine)

| Item | Détail |
|------|--------|
| Chemin | `./AUDIT_PROMPT_TRADING.md` |
| Date | 27 avr. 2026 |
| Taille | 14 KB |
| Tracked ? | ✅ tracked |
| Référencé par | aucun fichier (vérifié `grep`) |
| Pertinence | audit ancien d'un prompt trading générique, pas TRADEX-AI |

**Action recommandée** : `git rm AUDIT_PROMPT_TRADING.md` (ou archiver `_archive/audits-prompts/`).

---

### U7. Doublons supplémentaires `code/scraper/__pycache__` (à vérifier)

> ⚠️ Le `.gitignore` couvre `__pycache__/` globalement. Mais à confirmer pour
> `04-kb-sources/youtube-a-scraper/__pycache__/` qui contient peut-être des
> .pyc trackés par erreur.

**Action recommandée** : `git ls-files | grep __pycache__` → si vide, OK. Sinon `git rm --cached`.

---

### U8. Confusion structurelle `kb/` racine vs `code/knowledge_base/`

⚠️ **PAS À SUPPRIMER MAINTENANT — décision Phase B.**

| Existence | Chemin | État |
|-----------|--------|------|
| Dossier vide | `./kb/` | racine, mentionné CLAUDE.md projet |
| Dossier vide | `./code/knowledge_base/` | dans code/, créé en migration |
| Référence dans le code | `code/engine/claude_brain.py:177` → `os.path.join(BASE_DIR, "kb", ...)` où BASE_DIR = `code/` → **cible `code/kb/` qui N'EXISTE PAS** |
| Référence dans la config | `code/config/settings.py:69` → idem `KB_DIR = code/kb/` |

**3 alternatives possibles à trancher Phase B** :
- (a) Garder `kb/` à la racine et **modifier le code** pour pointer dessus (`os.path.join(os.path.dirname(BASE_DIR), "kb", ...)`).
- (b) Renommer `code/knowledge_base/` en `code/kb/` (aligne le code, supprime `kb/` racine).
- (c) Garder `code/knowledge_base/` et **modifier le code** pour pointer dessus (`os.path.join(BASE_DIR, "knowledge_base", ...)`), supprimer `kb/` racine.

→ **Décision à prendre par Abdelkrim au début de Phase B**. Pour l'instant : **NE RIEN SUPPRIMER**.

---

## 🟡 OPTIONNEL — 19 items (à reclasser, pas à supprimer)

### O1-O5. Fichiers MBK historiques (racine + docs)

MBK Trader = projet Electron en pause depuis l'arrivée de TRADEX-AI (cf CLAUDE.md global). Utile comme historique mais encombre.

| # | Chemin | Taille | Tracked | Action |
|---|--------|--------|---------|--------|
| O1 | `./AUDIT_FINAL_MBK_TRADER_30042026.md` | 14 KB | ✅ | déplacer `_archive/MBK/` |
| O2 | `./PROMPT_CORRECTION_MBK_AUDIT_P0P1_v1.0.md` | 24 KB | ✅ | déplacer `_archive/MBK/` |
| O3 | `./PROMPT_TRADING_SAAS_MBK_v1.0.md` | 20 KB | ✅ | déplacer `_archive/MBK/` |
| O4 | `./docs/AUDIT_MASTER_MBK.md` | 28 KB | ✅ | déplacer `_archive/MBK/` |
| O5 | `./docs/MASTER_MBK_TRADING_SAAS_COMPLET.md` | 39 KB | ✅ | déplacer `_archive/MBK/` |
| O6 | `./docs/PLAN_12_MISSIONS_ATOMIQUES_MBK.md` | 27 KB | ✅ | déplacer `_archive/MBK/` (12 missions terminées) |
| O7 | `./docs/STRATEGIE_CORRECTION_MBK_v2.md` | 38 KB | ✅ | déplacer `_archive/MBK/` |
| O8 | `./docs/mbk-trader/` (sous-dossier complet, v1.1 docs) | ~30 KB | ✅ | déplacer `_archive/MBK/` |

**Total à archiver** : ~210 KB, 8 items.

---

### O9-O12. Méthodes externes (PDF à la racine)

Méthodes alternatives lues mais hors scope TRADEX-AI (focus = Belkhayate sur futures GC/HG/CL/ZW).

| # | Chemin | Taille | Pertinence |
|---|--------|--------|------------|
| O9 | `./Méthode Bao (Modern Rock).pdf` | 130 KB | externe — small caps action |
| O10 | `./Méthode Brian Lee pour la Maîtrise des Marchés.pdf` | 124 KB | externe — généraliste |
| O11 | `./Méthode de Day Trading d'Alex Temiz.pdf` | 135 KB | externe — actions |
| O12 | `./Maîtriser le Trading de Small Caps par le Recyclage de Position.pdf` | 133 KB | **hors scope** — small caps ≠ futures |

**Action recommandée** : déplacer vers `_archive/external-methods/`.

---

### O13-O15. PDF Belkhayate à la racine

À ranger dans le corpus Belkhayate existant.

| # | Chemin | Taille | Destination |
|---|--------|--------|-------------|
| O13 | `./Architecture et Implémentation du Système Belkhayate pour Assistant de Trading IA.pdf` | 121 KB | `01-methode-belkhayate/` |
| O14 | `./Méthode Belkhayate Compétences à Maîtriser.pdf` | 189 KB | `01-methode-belkhayate/` |
| O15 | `./MÉTHODE DE TRADING MUSTAPHA BELKHAYATE.pdf` | 355 KB | `01-methode-belkhayate/` |

---

### O16-O18. Documents d'analyse Belkhayate (racine → `docs/`)

| # | Chemin | Taille | Pertinence |
|---|--------|--------|------------|
| O16 | `./INVENTAIRE_BELKHAYATE.md` | 10 KB | analyse corpus |
| O17 | `./METHODE_BELKHAYATE_RESTRUCTURE.md` | 26 KB | analyse méthode |
| O18 | `./RAPPORT_AUDIT_BELKHAYATE.md` | 14 KB | rapport audit |

**Action recommandée** : déplacer vers `docs/analyses-belkhayate/`.

---

### O19. Scripts utilitaires Windows

| # | Chemin | Taille | Usage |
|---|--------|--------|-------|
| O19a | `./disable-sleep.ps1` | 1.1 KB | empêche veille pendant scraping long |
| O19b | `./restore-sleep.ps1` | 1.0 KB | restaure veille |

**Action recommandée** : déplacer vers `scripts/` (à créer).

---

### O20. README ancien

| Item | Détail |
|------|--------|
| Chemin | `./README — CONTEXTE DE LA DISCUSSION.txt` |
| Date | 24 avr. 2026 |
| Taille | 9.4 KB |
| Tracked ? | ✅ |
| Pertinence | contexte initial (pré-TRADEX-AI), historique uniquement |

**Action recommandée** : déplacer vers `_archive/` (ou `git rm` si pas de valeur historique).

---

### O21. Guide Stratégique PDF (racine, gitignored)

| Item | Détail |
|------|--------|
| Chemin | `./Guide Stratégique Automatisation du Trading Boursier avec Claude AI.pdf` |
| Taille | 723 KB |
| Tracked ? | ❌ (gitignored ligne 30) |
| Usage | source utilisée pour générer `docs/APPORTS_GUIDE_EXTERNE.md` |

**Action recommandée** : déplacer vers `_archive/sources-pdf-externes/` (reste gitignored).

---

## 📋 FICHIERS À GARDER EXPLICITEMENT (pour éviter toute suppression accidentelle)

### Documents projet actifs (ne pas toucher)
- `CLAUDE.md` — décisions verrouillées projet
- `README.md` — readme projet
- `.gitignore` — config git
- `FEUILLE_DE_ROUTE.md` — roadmap 11 phases
- `GARDE_FOUS_PROPOSES.md` — 32 garde-fous
- `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` — blueprint TRADEX-AI (CLAUDE.md priorité 2)
- `PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md` — KB phase ref (CLAUDE.md priorité 4)

### Dossiers projet actifs (ne pas toucher)
- `code/` — tout le code
- `docs/MASTER_TRADEX_AI_v2.md` + `docs/APPORTS_GUIDE_EXTERNE.md` + `docs/MODULES.md`
- `_context/` — briefings de session
- `_archive/` — déjà des archives (15 fichiers)
- `01-methode-belkhayate/`, `02-marches-trading/`, `03-marches-confirmation/`, `04-kb-sources/`, `05-skills/`, `06-playbook/`
- `data/`, `logs/` — emplacements runtime documentés CLAUDE.md
- `.claude/` — config Claude Code

---

## 📊 SYNTHÈSE QUANTIFIÉE

| Catégorie | Items | Espace libéré (estimé) | Action |
|-----------|-------|------------------------|--------|
| 🔴 URGENT (suppression) | 7 (U1-U7) | ~400 MB (surtout U3) | `rm` / `git rm` |
| 🔴 URGENT (à trancher Phase B) | 1 (U8) | 0 | décision structurelle |
| 🟡 OPTIONNEL MBK historique | 8 (O1-O8) | ~210 KB | déplacer `_archive/MBK/` |
| 🟡 OPTIONNEL méthodes externes | 4 (O9-O12) | ~520 KB | déplacer `_archive/external-methods/` |
| 🟡 OPTIONNEL Belkhayate à ranger | 6 (O13-O18) | ~750 KB | déplacer dans corpus existant ou `docs/` |
| 🟡 OPTIONNEL scripts utilitaires | 1 (O19) | ~2 KB | déplacer `scripts/` |
| 🟡 OPTIONNEL README ancien | 1 (O20) | 9 KB | archiver |
| 🟡 OPTIONNEL Guide PDF source | 1 (O21) | 723 KB | déplacer `_archive/sources-pdf-externes/` |
| **TOTAL** | **29 items** | **~402 MB** | — |

**Note** : 99 % du gain disque vient de la suppression de `.tmp.driveupload/` (~400 MB).

---

## 🚦 ORDRE D'EXÉCUTION RECOMMANDÉ

> Tout doit être validé un par un avant exécution. Aucune suppression sans OK.

1. **Phase nettoyage urgent** (zéro risque)
   - U1 : 6 dossiers vides racine
   - U2 + U3 : `.tmp.drive*/`
   - U7 : __pycache__ trackés (si trouvés)
2. **Phase doublons confirmés**
   - U4 + U5 : MBK v1.0 racine (v1.1 dans docs/mbk-trader/)
   - U6 : AUDIT_PROMPT_TRADING.md
3. **Phase réorganisation** (cf `RAPPORT_REORGANISATION.md`)
   - O1-O8 : MBK → `_archive/MBK/`
   - O9-O12 : méthodes externes → `_archive/external-methods/`
   - O13-O15 : PDF Belkhayate → `01-methode-belkhayate/`
   - O16-O18 : analyses Belkhayate → `docs/analyses-belkhayate/`
   - O19 : scripts Windows → `scripts/`
   - O20 + O21 : README ancien + PDF source → `_archive/`
4. **Phase B (décision structurelle)**
   - U8 : trancher `kb/` vs `code/knowledge_base/` vs `code/kb/`

---

*Document généré le 2026-05-03 — proposition uniquement, aucune suppression effectuée.*
