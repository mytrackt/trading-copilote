# README DE TRANSITION — TRADEX-AI
**Date :** 22/06/2026 · **Session :** S1 · **Score projet :** N/A (pipeline KB)

---

## 1. ÉTAT ACTUEL DU PROJET

Pipeline KB Phase 1 **entièrement validé** sur deux pages StockCharts (Moving Averages + RSI).
Le scraper v2 (double ancrage `.md` figcaption + HTML légende locale) garantit 100% de fiabilité
image↔label ou déclaration manuelle explicite. 39 décisions KB produites (D1–D39), toutes certifiées.
Phase 2 (Agents 3+4+Archiviste) non encore construite — c'est le prochain chantier.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| 1.1 | scraper.py v2 double ancrage · RSI 15/15 images · backup v1 | 84bf97a | ✅ |
| 1.2 | Extraction RSI D18–D39 · KB_INDEX sur disque + à jour | dc0a823 | ✅ |

---

## 3. MISSION SUIVANTE

**Option A (recommandée) — Phase 2 pipeline**
Construire Agent 3 (Formateur), Agent 4 (Validateur), Archiviste (git auto).
Objectif : rendre le pipeline autonome end-to-end (scraper → extraction → commit).

**Option B — Extraction MACD (D40+)**
Même workflow : scraper RSI → Agent 2. Bloque Couche 0 NinjaScript.

---

## 4. DÉCISIONS PRISES CETTE SESSION

| Code | Décision |
|------|----------|
| ARCH-14 | Liaison image : DOUBLE ANCRAGE (.md figcaption + HTML légende locale) · accord 2 sources sinon manuel |
| ARCH-11 (MàJ) | Dossier : BRUT `01-pipeline/bundles/` · TRAITÉ `04-cerveau-trading/[source]/` |
| — | Nommage extraction : `Extraction_[Source]_[Sujet]_v1.md` dans `04-cerveau-trading\` |
| — | KB_INDEX.md créé sur disque (`C:\trading-copilote\KB_INDEX.md`) — n'existait que dans Claude.ai |

---

## 5. DÉCISIONS TEMPORAIRES

| # | Décision | Condition de levée |
|---|----------|--------------------|
| T1 | Scraper calibré StockCharts uniquement | Chaque nouvelle source nécessite son propre résolveur |
| T2 | Agent 2 = analyse manuelle (Claude) | Sera remplacé par Agent 3+4 automatique (Phase 2) |
| T3 | `15 Golden Point Daily.txt` en racine repo | À déplacer vers `02-sources-brutes\playbook\youtube\` |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité |
|---|----------|----------|
| P1 | `moving_averages_v1.md` est dans `02-sources-brutes\` (ancien emplacement) · à migrer vers `04-cerveau-trading\chartschool\` | Faible |
| P2 | Phase 2 pipeline non construite → extraction encore manuelle | Moyen |
| P3 | 3 transcripts Belkhayate YouTube en racine → non classés | Faible |

---

## 7. STACK TECHNIQUE GELÉE

```
Langage      : Python (py / py -m py_compile)
Plateforme   : Windows · Claude Code (exécution scripts)
Scraper      : 01-pipeline\scraper.py v2 (double ancrage)
Backup       : 01-pipeline\scraper_backup_v1.py
Bundles      : 01-pipeline\bundles\[source]\ (brut)
Extractions  : 04-cerveau-trading\[source]\ (traité)
KB_INDEX     : C:\trading-copilote\KB_INDEX.md (sur disque + projet Claude.ai)
GitHub       : mytrackt/trading-copilote · branch main
```

---

## 8. ÉTAT DES REPOS FIN SESSION

| Repo | Branch | Dernier commit | État |
|------|--------|----------------|------|
| trading-copilote | main | dc0a823 | ✅ Propre · remote à jour |

---

## 9. COMMANDES GIT (PowerShell — UNE à la fois)

Pour la prochaine session (déplacer moving_averages_v1.md si souhaité) :

```powershell
# Depuis C:\trading-copilote
git mv 02-sources-brutes\playbook\stockcharts\moving_averages_v1.md 04-cerveau-trading\chartschool\moving_averages_v1.md
```
```powershell
git commit -m "refactor: deplace moving_averages vers 04-cerveau-trading"
```
```powershell
git push origin main
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

- [ ] Vérifier compteur D### dans KB_INDEX.md → doit afficher **D40** comme prochaine décision
- [ ] Confirmer le choix : Phase 2 pipeline OU extraction MACD
- [ ] Si MACD → lancer scraper.py sur l'URL MACD StockCharts directement
- [ ] KB_INDEX.md à jour dans le projet Claude.ai (voir bandeau ci-dessous)

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « TRADEX-AI · Pipeline Phase 1 validée (commits 84bf97a + dc0a823). Scraper v2 DOUBLE ANCRAGE opérationnel (.md figcaption + HTML légende locale · accord 2 sources sinon manuel). Moving Averages D1–D17 ✅ · RSI D18–D39 ✅ (15/15 images). Prochaine décision : **D40**. Extractions traitées dans `04-cerveau-trading\chartschool\`. Aujourd'hui : **Phase 2 pipeline** (Agent 3 Formateur + Agent 4 Validateur + Archiviste) OU extraction MACD (D40+). »

---

## 12. ÉTAT KB FIN SESSION

| Élément | Valeur |
|---------|--------|
| Compteur début session | D17 |
| Compteur fin session | **D39** |
| Décisions ajoutées | +22 (D18→D39 · RSI complet) |
| Fichiers produits | `Extraction_StockCharts_RSI_v1.md` |
| KB_INDEX régénéré | **OUI** → à ré-uploader dans le projet Claude.ai |
| Prochain à extraire | MACD (D40+) · StockCharts + Fidelity |

---

*README de transition · TRADEX-AI · Session S1 · 22/06/2026*
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
