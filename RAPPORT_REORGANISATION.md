# RAPPORT DE RÉORGANISATION — `C:\trading-copilote\`

> Document de proposition uniquement — **aucune action effectuée**.
> Source : `CHECKLIST_FICHIERS_INUTILES.md` (29 items identifiés) + audit complet du workspace.
> **Date** : 2026-05-03.
> Objectif : passer de **28 fichiers + 22 dossiers à la racine** à une structure
> propre où la racine ne contient plus que les **6 fichiers projets stratégiques**.

---

## 1. AVANT / APRÈS — Vue d'ensemble

### Situation actuelle (problèmes)

```
Racine = 28 fichiers (.md, .pdf, .txt, .ps1, .gitignore) + 22 dossiers
├── 6 dossiers VIDES doublons code/ (api, collectors, config, engine, execution, utils)
├── 2 dossiers .tmp.drive*/ (~400 MB de junk Google Drive)
├── 8 fichiers MBK historiques éparpillés (racine + docs/)
├── 7 PDF méthodes (Belkhayate + externes) en vrac à la racine
├── 3 .md analyses Belkhayate à la racine (devraient être dans docs/)
├── 2 scripts Windows .ps1 à la racine
├── 1 README.txt obsolete + 1 audit prompt obsolete
└── Confusion structurelle kb/ racine vs code/knowledge_base/
```

### Cible proposée (après réorganisation)

```
Racine = 6 fichiers stratégiques + dossiers fonctionnels uniquement
├── CLAUDE.md, README.md, .gitignore
├── FEUILLE_DE_ROUTE.md, GARDE_FOUS_PROPOSES.md
├── RAPPORT_ORTOGONEX_V4_POST_AUDIT.md       (blueprint, CLAUDE.md priorité 2)
│
├── _context/                                  briefings de session
├── _archive/                                  archives historiques (sous-catégories)
├── code/                                      TOUT LE CODE
├── docs/                                      documentation technique
├── 01-methode-belkhayate/                     corpus méthode
├── 02-marches-trading/                        actifs trading (GC/HG/CL/ZW)
├── 03-marches-confirmation/                   actifs confirmation (DX/ES/VX)
├── 04-kb-sources/                             sources KB (transcripts)
├── 05-skills/                                 skills Claude
├── 06-playbook/                               playbooks opérationnels
├── data/                                      runtime JSON
├── logs/                                      runtime logs
├── scripts/                                   NOUVEAU : utilitaires Windows
└── kb/                                        À DÉCIDER (Phase B)
```

---

## 2. STRUCTURE CIBLE DÉTAILLÉE

### Racine (6 fichiers stratégiques + dotfiles)

| Fichier | Rôle | Pourquoi à la racine |
|---------|------|----------------------|
| `CLAUDE.md` | décisions verrouillées projet | obligatoire pour Claude Code (lecture règle 0) |
| `README.md` | readme projet | convention universelle |
| `.gitignore` | config git | obligatoire à la racine |
| `FEUILLE_DE_ROUTE.md` | roadmap 11 phases A→K | référence active de la session |
| `GARDE_FOUS_PROPOSES.md` | 32 garde-fous | référence active de la session |
| `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | blueprint TRADEX-AI complet | CLAUDE.md priorité 2 |

> Note : `CHECKLIST_FICHIERS_INUTILES.md` et `RAPPORT_REORGANISATION.md` (ce
> fichier) sont aussi à la racine **temporairement** — ils sont déplacés en
> `_archive/audits-prompts/` une fois la réorganisation exécutée.

### `_archive/` — Sous-catégories (création de 4 sous-dossiers)

```
_archive/
├── (15 fichiers existants restent en place — historique antérieur)
├── MBK/                          ← NOUVEAU
│   ├── AUDIT_FINAL_MBK_TRADER_30042026.md
│   ├── PROMPT_CORRECTION_MBK_AUDIT_P0P1_v1.0.md
│   ├── PROMPT_TRADING_SAAS_MBK_v1.0.md
│   ├── CDC_MBK_TRADER_TECHNIQUE_v1.0.md      (si non supprimé)
│   ├── CDC_MBK_TRADER_VISION_v1.0.md         (si non supprimé)
│   ├── AUDIT_MASTER_MBK.md                    (depuis docs/)
│   ├── MASTER_MBK_TRADING_SAAS_COMPLET.md     (depuis docs/)
│   ├── PLAN_12_MISSIONS_ATOMIQUES_MBK.md      (depuis docs/)
│   ├── STRATEGIE_CORRECTION_MBK_v2.md         (depuis docs/)
│   └── mbk-trader/                             (sous-dossier complet depuis docs/)
│       ├── CDC_MBK_TRADER_TECHNIQUE_v1.1.md
│       └── CDC_MBK_TRADER_VISION_v1.1.md
├── external-methods/             ← NOUVEAU
│   ├── Méthode Bao (Modern Rock).pdf
│   ├── Méthode Brian Lee pour la Maîtrise des Marchés.pdf
│   ├── Méthode de Day Trading d'Alex Temiz.pdf
│   └── Maîtriser le Trading de Small Caps par le Recyclage de Position.pdf
├── sources-pdf-externes/         ← NOUVEAU (gitignored)
│   └── Guide Stratégique Automatisation du Trading Boursier avec Claude AI.pdf
├── audits-prompts/               ← NOUVEAU
│   ├── AUDIT_PROMPT_TRADING.md
│   ├── README — CONTEXTE DE LA DISCUSSION.txt
│   ├── CHECKLIST_FICHIERS_INUTILES.md         (ce fichier après exécution)
│   └── RAPPORT_REORGANISATION.md              (ce fichier après exécution)
```

### `01-methode-belkhayate/` — Ajout des 3 PDF Belkhayate racine

```
01-methode-belkhayate/
├── (corpus existant)
├── pdfs-references/              ← NOUVEAU sous-dossier (regroupe les PDF)
│   ├── Architecture et Implémentation du Système Belkhayate pour Assistant de Trading IA.pdf
│   ├── Méthode Belkhayate Compétences à Maîtriser.pdf
│   └── MÉTHODE DE TRADING MUSTAPHA BELKHAYATE.pdf
```

### `docs/` — Ajout sous-dossier analyses + nettoyage MBK

```
docs/
├── MASTER_TRADEX_AI_v2.md        (fichier maître — reste)
├── APPORTS_GUIDE_EXTERNE.md      (reste)
├── MODULES.md                     (reste)
├── PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md   ← DÉPLACÉ depuis racine (KB phase ref)
├── analyses-belkhayate/          ← NOUVEAU
│   ├── INVENTAIRE_BELKHAYATE.md
│   ├── METHODE_BELKHAYATE_RESTRUCTURE.md
│   └── RAPPORT_AUDIT_BELKHAYATE.md
└── (les 4 fichiers MBK + sous-dossier mbk-trader/ → DÉPLACÉS vers _archive/MBK/)
```

### `scripts/` — NOUVEAU dossier

```
scripts/
├── disable-sleep.ps1
└── restore-sleep.ps1
```

### `code/` — Aucune modification dans cette réorganisation

Décision structurelle `kb/` traitée séparément en Phase B (cf section 6).

---

## 3. MOUVEMENTS DÉTAILLÉS — 6 GROUPES = 6 COMMITS LOGIQUES

> Chaque groupe = 1 commit cohérent. Permet rollback ciblé si besoin.

### Groupe G1 — Nettoyage URGENT (sans risque)

```powershell
# Suppression 6 dossiers vides racine (doublons code/)
Remove-Item ./api, ./collectors, ./config, ./engine, ./execution, ./utils -Recurse -Force

# Suppression 2 dossiers temp Google Drive
Remove-Item .tmp.driveupload -Recurse -Force      # ~400 MB
Remove-Item .tmp.drivedownload -Recurse -Force    # ~0 B

# Mise à jour .gitignore (ajouter .tmp.drivedownload/)
# (édition manuelle ou via Edit tool)
```

**Commit message proposé** : `chore: nettoyage racine - dossiers vides duplicates code/ + .tmp.drive cleanup`

**Diff impact** : suppression de 8 dossiers (dont 1 ~400 MB), modification `.gitignore`.

---

### Groupe G2 — Archivage MBK (8 fichiers + 1 sous-dossier)

```powershell
# Créer destination
New-Item -Path _archive/MBK -ItemType Directory -Force

# Déplacer 4 fichiers MBK racine
git mv AUDIT_FINAL_MBK_TRADER_30042026.md       _archive/MBK/
git mv PROMPT_CORRECTION_MBK_AUDIT_P0P1_v1.0.md _archive/MBK/
git mv PROMPT_TRADING_SAAS_MBK_v1.0.md          _archive/MBK/
git mv CDC_MBK_TRADER_TECHNIQUE_v1.0.md         _archive/MBK/    # OU git rm si U4
git mv CDC_MBK_TRADER_VISION_v1.0.md            _archive/MBK/    # OU git rm si U5

# Déplacer 4 fichiers MBK depuis docs/
git mv docs/AUDIT_MASTER_MBK.md                 _archive/MBK/
git mv docs/MASTER_MBK_TRADING_SAAS_COMPLET.md  _archive/MBK/
git mv docs/PLAN_12_MISSIONS_ATOMIQUES_MBK.md   _archive/MBK/
git mv docs/STRATEGIE_CORRECTION_MBK_v2.md      _archive/MBK/

# Déplacer le sous-dossier mbk-trader/
git mv docs/mbk-trader _archive/MBK/mbk-trader
```

**Commit message proposé** : `chore: archive MBK - projet en pause, deplacement vers _archive/MBK/`

**Diff impact** : 9 déplacements (~210 KB), historique git préservé via `git mv`.

---

### Groupe G3 — Archivage méthodes externes (4 PDF)

```powershell
New-Item -Path _archive/external-methods -ItemType Directory -Force

git mv "Méthode Bao (Modern Rock).pdf"                                     _archive/external-methods/
git mv "Méthode Brian Lee pour la Maîtrise des Marchés.pdf"                _archive/external-methods/
git mv "Méthode de Day Trading d'Alex Temiz.pdf"                           _archive/external-methods/
git mv "Maîtriser le Trading de Small Caps par le Recyclage de Position.pdf" _archive/external-methods/
```

**Commit message proposé** : `chore: archive methodes externes - hors scope TRADEX-AI`

**Diff impact** : 4 PDF déplacés (~520 KB), historique préservé.

---

### Groupe G4 — Rangement corpus Belkhayate (3 PDF + 3 .md analyses)

```powershell
# Sous-dossier dans corpus existant
New-Item -Path 01-methode-belkhayate/pdfs-references -ItemType Directory -Force

git mv "Architecture et Implémentation du Système Belkhayate pour Assistant de Trading IA.pdf" 01-methode-belkhayate/pdfs-references/
git mv "Méthode Belkhayate Compétences à Maîtriser.pdf"                                        01-methode-belkhayate/pdfs-references/
git mv "MÉTHODE DE TRADING MUSTAPHA BELKHAYATE.pdf"                                            01-methode-belkhayate/pdfs-references/

# Analyses .md vers docs/
New-Item -Path docs/analyses-belkhayate -ItemType Directory -Force

git mv INVENTAIRE_BELKHAYATE.md            docs/analyses-belkhayate/
git mv METHODE_BELKHAYATE_RESTRUCTURE.md   docs/analyses-belkhayate/
git mv RAPPORT_AUDIT_BELKHAYATE.md         docs/analyses-belkhayate/
```

**Commit message proposé** : `chore: rangement corpus belkhayate - pdf vers 01-methode + analyses vers docs`

**Diff impact** : 6 fichiers déplacés (~750 KB), 2 nouveaux sous-dossiers, historique préservé.

---

### Groupe G5 — Scripts utilitaires Windows + PROMPT_1 vers docs

```powershell
# Créer dossier scripts/
New-Item -Path scripts -ItemType Directory -Force

git mv disable-sleep.ps1 scripts/
git mv restore-sleep.ps1 scripts/

# PROMPT_1 (KB phase ref) vers docs/ (cohérence)
git mv PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md docs/
```

**Commit message proposé** : `chore: organisation - scripts windows vers scripts/ + prompt_1 KB vers docs/`

**Diff impact** : 3 fichiers déplacés.

---

### Groupe G6 — Audits anciens + README contexte vers _archive

```powershell
New-Item -Path _archive/audits-prompts -ItemType Directory -Force
New-Item -Path _archive/sources-pdf-externes -ItemType Directory -Force

git mv AUDIT_PROMPT_TRADING.md                 _archive/audits-prompts/
git mv "README — CONTEXTE DE LA DISCUSSION.txt" _archive/audits-prompts/

# Le PDF source (gitignored) est déplacé manuellement (pas tracké)
Move-Item "Guide Stratégique Automatisation du Trading Boursier avec Claude AI.pdf" _archive/sources-pdf-externes/

# Mettre à jour .gitignore pour pointer vers le nouveau chemin
# Edit .gitignore:
#   /Guide Stratégique...AI.pdf  →  /_archive/sources-pdf-externes/Guide Stratégique...AI.pdf
```

**Commit message proposé** : `chore: archive audits anciens + README contexte historique`

**Diff impact** : 3 déplacements + 1 update .gitignore.

---

## 4. FICHIERS QUI RESTENT À LA RACINE (final)

```
C:\trading-copilote\
├── .gitignore
├── CLAUDE.md
├── README.md
├── FEUILLE_DE_ROUTE.md
├── GARDE_FOUS_PROPOSES.md
└── RAPPORT_ORTOGONEX_V4_POST_AUDIT.md
```

**6 fichiers seulement** — racine épurée, lisible.

---

## 5. DÉCISIONS STRUCTURELLES À TRANCHER (Phase B)

### D1. `kb/` racine vs `code/knowledge_base/` vs `code/kb/`

État actuel :
- `./kb/` — vide, mentionné CLAUDE.md projet
- `./code/knowledge_base/` — vide, créé en migration
- Code (`claude_brain.py:177`, `settings.py:69`) cherche `code/kb/` qui **n'existe pas**

**Recommandation : Option (c)**
- Garder `code/knowledge_base/` comme cible
- Modifier `code/engine/claude_brain.py:177` : `"kb"` → `"knowledge_base"`
- Modifier `code/config/settings.py:69` : `"kb"` → `"knowledge_base"`
- Supprimer `./kb/` racine
- Mettre à jour `CLAUDE.md` projet (section Arborescence) : retirer `kb/` racine

**Pourquoi** : cohérent avec la règle "tout dans `code/`" + nom plus explicite + une seule modification dans le code.

→ **À valider Abdelkrim au début de Phase B.**

---

### D2. CLAUDE.md projet à mettre à jour POST-réorganisation

Sections à modifier dans `CLAUDE.md` :

**Section "Arborescence complète"** (~ligne 80) :
- Retirer mentions `code/scraper/` et `code/transcripts/` (n'existent pas — ils sont dans `04-kb-sources/youtube-a-scraper/`)
- Retirer `kb/` racine si décision D1 = (c)

**Section "FICHIERS CLÉS — LIRE DANS CET ORDRE"** :
- Priorité 4 : `PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md` → mettre à jour chemin vers `docs/PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md`

**Section "ÉTAT ACTUEL"** :
- Marquer Phase A done
- Mettre à jour structure `code/` réelle
- Pointer vers `_context/briefing-2026-05-03-fin-phase-A.md`

→ Mise à jour dans un commit dédié final : `chore: CLAUDE.md - mise a jour arborescence + chemins post-reorganisation`

---

## 6. ORDRE D'EXÉCUTION RECOMMANDÉ

| Ordre | Action | Commit | Réversible ? |
|-------|--------|--------|--------------|
| 1 | Backup disque préalable | — | OUI (déjà fait `BACKUP_TRADEX_20260503_011804`) |
| 2 | G1 — Nettoyage urgent | `chore: nettoyage racine ...` | OUI (git revert) |
| 3 | G2 — Archive MBK | `chore: archive MBK ...` | OUI |
| 4 | G3 — Archive méthodes externes | `chore: archive methodes externes ...` | OUI |
| 5 | G4 — Rangement corpus Belkhayate | `chore: rangement corpus belkhayate ...` | OUI |
| 6 | G5 — Scripts + PROMPT_1 | `chore: organisation scripts ...` | OUI |
| 7 | G6 — Audits + README contexte | `chore: archive audits anciens ...` | OUI |
| 8 | (Phase B) D1 — Décision `kb/` | `refactor: alignement kb/knowledge_base` | OUI |
| 9 | Final | `chore: CLAUDE.md - mise a jour arborescence` | OUI |
| 10 | `git push origin master` | — | OUI |

**Estimation** : 6 commits réorganisation + 1 commit alignement code (Phase B) + 1 commit doc finale = 8 commits.
**Effort** : 1 session courte (30-60 min) hors décision Phase B.

---

## 7. RISQUES ET MITIGATION

| Risque | Probabilité | Mitigation |
|--------|-------------|------------|
| Casser une référence dans un .md (lien vers fichier déplacé) | moyenne | `grep -r "ancien-chemin"` avant chaque déplacement |
| Casser `claude_brain.py` ou `settings.py` (chemins en dur) | faible | Aucun déplacement dans `code/` cette réorganisation (sauf D1 Phase B) |
| Perdre l'historique git d'un fichier | faible | Utiliser `git mv` (pas `mv` puis `git add`) |
| Supprimer un fichier important par erreur | faible | Backup `BACKUP_TRADEX_20260503_011804` toujours disponible |
| `.gitignore` pointe vers chemin obsolète après G6 | moyenne | Mettre à jour explicitement dans G6 |

---

## 8. CE QUI N'EST **PAS** RÉORGANISÉ (volontairement)

- `_archive/` (15 fichiers existants) — laissés en flat archive, pas de re-classification
- `code/` arborescence — aucun déplacement (sauf D1 Phase B)
- `_context/` — convention briefing déjà propre
- `01-methode-belkhayate/`, `02-marches-trading/`, `03-marches-confirmation/`, `04-kb-sources/`, `05-skills/`, `06-playbook/` — corpus existants intouchés
- `data/`, `logs/` — runtime emplacements documentés CLAUDE.md
- `.claude/` — config Claude Code

---

## 9. SYNTHÈSE QUANTIFIÉE

| Action | Items | Espace |
|--------|-------|--------|
| 🗑️ Suppression dossiers vides + tmp | 8 dossiers | ~400 MB libérés |
| 📦 Archivage MBK | 9 items → `_archive/MBK/` | ~210 KB |
| 📦 Archivage méthodes externes | 4 PDF → `_archive/external-methods/` | ~520 KB |
| 📦 Archivage audits + README ancien | 3 items → `_archive/audits-prompts/` | ~25 KB |
| 📦 Archivage PDF source guide | 1 PDF → `_archive/sources-pdf-externes/` | 723 KB |
| 📁 Rangement PDF Belkhayate | 3 PDF → `01-methode-belkhayate/pdfs-references/` | ~665 KB |
| 📁 Rangement analyses Belkhayate | 3 .md → `docs/analyses-belkhayate/` | ~50 KB |
| 📁 Création scripts/ | 2 .ps1 → `scripts/` | ~2 KB |
| 📁 PROMPT_1 vers docs/ | 1 .md → `docs/` | 53 KB |

**Bilan racine** :
- AVANT : 28 fichiers + 22 dossiers à la racine
- APRÈS : 6 fichiers + 14 dossiers à la racine (-22 fichiers, -8 dossiers)

---

## 10. CE QUI ARRIVE APRÈS RÉORGANISATION

1. Phase B (KB Belkhayate) peut démarrer sur une racine propre
2. Décision D1 `kb/knowledge_base/` tranchée en début de Phase B
3. CLAUDE.md projet mis à jour
4. Push final → workspace propre et synchronisé

---

*Document généré le 2026-05-03 — proposition uniquement, aucun déplacement effectué.*
*Aucune modification de code dans cette proposition.*
