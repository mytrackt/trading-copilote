# README DE TRANSITION — TRADEX-AI
Date : 22/06/2026 | Session : S20 | KB : 1 313 règles (inchangée)

---

## 1. ÉTAT ACTUEL DU PROJET

Session courte hors-roadmap : validation de l'outil d'extraction KB (scraper StockCharts).
Scraper v3.1 VALIDÉ (3 tests PASS) — prêt à alimenter les futurs tickets d'enrichissement.
KB inchangée (1313 règles). Phase C (NT8/ATAS) toujours BLOQUÉE. Mode AUTO BLOQUÉ. Énergie = stub.
Ticket roadmap 0.l (Chap12 Macro) non démarré — reste la prochaine cible d'interstice.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Validation scraper v3 | 3 pages testées (MA/RSI/MACD) | — | ✅ |
| Correctif scraper v3.1 | `images_html()` filtre images `class="inline"` (décoratives) → alignement HTML=.md | ee0f679 | ✅ pushé |
| Rapport validation | `01-pipeline\rapport_validation_scraper_v3.md` | ee0f679 | ✅ pushé |
| CLAUDE.md mis à jour | ligne ÉTAT scraper v3.1 + footer 22/06 | 577a934 | ✅ pushé |

**Résultats tests** : MA 14 certifiées / RSI 16 / MACD 11 — 0 à vérifier, 0 décorative sur les 3.
Non-régression confirmée : aucune image certifiée v2 perdue (6 MA + 15 RSI préservées).

---

## 3. MISSION SUIVANTE

**Ticket 0.l — Chap12 Macro & Actualités (P1 · interstice)** — inchangé depuis S19.

Fichier source : `02-sources-brutes\playbook\TRADEX_KB_Chap12_Macro_Actualites.md`
Pipeline : étapes 3→7 (plan → fabrication → audit → fusion).
Catégories KB candidates : `macro_evenements`, `correlations`, `gestion_risque_entree`.

---

## 4. DÉCISIONS PRISES EN S20

Aucune décision architecturale. Décisions verrouillées inchangées.

**Décision technique scraper (validée)** : sur le HTML rendu GitBook, les images de contenu
sont en `class="block"`, les décoratives répétées en `class="inline"`. Le scraper ne retient
que les `block` (option 2) pour aligner le compte sur les `<figure>` du `.md`. Discriminant
sans signature codée en dur.

---

## 5. DÉCISIONS TEMPORAIRES

Aucune.

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité | Action requise |
|---|----------|----------|----------------|
| P1 | Section-fallback produit des labels non uniques (ex. MACD : 3× "Divergences") | MOYEN | Désambiguïsation côté Agent 2 (suffixe rang) avant fusion KB |
| P2 | Énergie Belkhayate = stub (conflit MFI vs proxy ATR non tranché) | BLOQUÉ | Attendre fin transcriptions Trading Geek |
| P3 | COG non validé sur range bars NT8 | PHASE C | Validation réelle Phase C |
| P4 | Dossier `data\` inexistant | PHASE C | Créer lors de la Phase C |
| P5 | Trading Geek transcription incomplète (38/113) | BACKGROUND | En cours |

---

## 7. STACK TECHNIQUE GELÉE

```
Trading     : NinjaTrader 8 (Windows local) — ATI TCP port 36973
Order flow  : ATAS Pro (Rithmic)
IA cerveau  : claude-sonnet-4-6
Backend     : Python 3.11 + FastAPI
Dashboard   : React 18 + Vite + Tailwind 3.4 (local)
DB          : SQLite
OS          : Windows 11 + PowerShell 7.6.2
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Repo unique : C:\trading-copilote\
Branche     : main
Dernier commit pushé : 577a934 (docs CLAUDE.md scraper v3.1) — confirmé "main -> main"
Commit précédent     : ee0f679 (fix scraper v3.1 + rapport + bundles) — pushé
Non commités (volontaire) : scraper_backup_v2.py · bundles\stockcharts\macd.md + macd_manifest.txt
```

---

## 9. COMMANDES GIT (PowerShell — JAMAIS &&)

Aucune action en attente — tout est pushé.
Vérification au démarrage S21 :
```
git log --oneline -3
```
Exécuter dans : `C:\trading-copilote`

---

## 10. PRE-FLIGHT SESSION SUIVANTE (S21)

- [ ] Lire CLAUDE.md EN ENTIER
- [ ] Lire ce fichier (README_TRANSITION_TRADEX_S20_20260622.md)
- [ ] Lire `00-pilotage\DETTE_TECHNIQUE.md`
- [ ] Ouvrir `00-pilotage\BACKLOG_ENRICHISSEMENTS.md` → confirmer ticket 0.l = prochaine cible
- [ ] Lire `02-sources-brutes\playbook\TRADEX_KB_Chap12_Macro_Actualites.md`

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Je démarre la session S21 de TRADEX-AI.
Lis CLAUDE.md + README_TRANSITION_TRADEX_S20_20260622.md.
KB à 1313 règles (inchangée en S20). Scraper KB v3.1 validé et pushé.
Action immédiate : traiter ticket 0.l — Chap12 Macro (P1) — interstice.
Phase C (NT8) reste bloquée jusqu'à KB complète.
```

---

## 12. ÉTAT KB FIN SESSION S20

KB **inchangée** : aucune brique ajoutée (session outillage, pas d'enrichissement).

| Élément | Valeur |
|---------|--------|
| Fichier | `04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json` |
| Règles totales | **1 313** (= S19) |
| Delta S20 | 0 |

**Tickets BACKLOG (inchangés) :**
- 🟢 0.b (S18) · 0.c · 0.o (S19)
- 📥 0.l Chap12 Macro → **PROCHAIN P1**
- 📥 0.i / 0.h / 0.g / 0.f → P1 suivants · 0. / 0.n / 0.m → P2

Outil prêt pour ces tickets : `01-pipeline\scraper.py` v3.1 (StockCharts).

---

*TRADEX-AI — Usage strictement personnel. Ce document n'est pas du conseil financier.*
