# README DE TRANSITION — TRADEX-AI
**Date** : 26/06/2026 | **Session** : S30 | **Mode** : Cowork (gouvernance) + Claude Code (batch Gemini — background)

---

## 1. ÉTAT ACTUEL DU PROJET

Session S30 entièrement dédiée à la **gouvernance** : restructuration CLAUDE.md + création des fichiers de pilotage + analyse de 2 documents d'architecture. Le batch Gemini (203 vidéos) tourne en parallèle dans Claude Code. Le code Python n'a pas été touché — aucun module commencé. 17 décisions verrouillées au total (D-S30-1 à D-S30-17). Prochain document d'Abdelkrim en attente.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| # | Mission | Résultat |
|---|---|---|
| 1 | Alléger CLAUDE.md | ✅ ~70 lignes — index pur, ne grossit plus |
| 2 | Créer DECISIONS_VEROUILLEES.md | ✅ 17 décisions verrouillées D-S30-1→D-S30-17 |
| 3 | Créer ARCHITECTURE_CONSTRUCTION.md v2 | ✅ Post-audit 9 corrections — 7 modules + gates + branches |
| 4 | Analyse Document 1 (CDC) | ✅ D-S30-1 à D-S30-9 verrouillées |
| 5 | Analyse Document 2 (App évolutive) | ✅ D-S30-10 à D-S30-17 verrouillées |
| 6 | Relecture critique doc 2 | ✅ D-S30-17 corrigé (12→15 prompts) · D-S30-16 amendé (désactivation seuil fort) |
| 7 | Lancer batch Gemini (203 vidéos) | ✅ Test validé (Kasper Gold 28Ko) · Batch lancé dans Claude Code |

---

## 3. MISSION SUIVANTE

**Recevoir et analyser Document 3** (Abdelkrim envoie les docs un par un).
Approche : audit comparatif vs TRADEX-AI → débat → verrouillage décisions.
Règle appliquée : challenger toute règle verrouillée si le doc propose mieux → présenter avantages/inconvénients → Abdelkrim décide.

---

## 4. DÉCISIONS PRISES CETTE SESSION

### Décisions D-S30-1 à D-S30-9 (Document 1 — CDC)

| ID | Décision |
|---|---|
| D-S30-1 | R/R ZW → 1:1,5 (vs 1:2 autres actifs) |
| D-S30-2 | Signal 15 champs (structure complète) |
| D-S30-3 | → REMPLACÉ PAR D-S30-17 |
| D-S30-4 | → ENRICHI PAR D-S30-10 |
| D-S30-5 | Risque par trade : 0,25%–0,50% du capital |
| D-S30-6 | → REMPLACÉ PAR D-S30-16 |
| D-S30-7 | Architecture modulaire 7 modules (max 200 lignes chacun) |
| D-S30-8 | Gouvernance : branches feature/module-XX · sous-agents · rollback obligatoire |
| D-S30-9 | Trading Geek Whisper archivé → 113 vidéos RE-TRANSCRIRE avec Gemini · 203 vidéos total |

### Décisions D-S30-10 à D-S30-17 (Document 2 — App évolutive)

| ID | Décision |
|---|---|
| D-S30-10 | Mémoire 10 types enrichie (6 paramètres par type : données · importance · usage · erreurs · durée · indicateurs) |
| D-S30-11 | Taxonomie 20 erreurs détectables → engine/error_tracker.py |
| D-S30-12 | Optimisation contrôlée : 10 règles + 15 critères → engine/optimizer.py |
| D-S30-13 | Frontend 7 blocs verrouillés (Verdict · Score 5D · Plan · Raisons pour · Raisons contre · Checklist 8 · 5 boutons) |
| D-S30-14 | Module Anti-Répétition (10 fonctions) → engine/anti_repetition.py |
| D-S30-15 | 8 types de rapports → engine/report_generator.py |
| D-S30-16 | Strategy Lab 20 champs + 18 fonctionnalités · désactivation AUTO sur seuil fort (drawdown > X% ou N pertes consécutives) + alerte immédiate → réactivation manuelle uniquement |
| D-S30-17 | **15 prompts fusionnés Option B** (12 fusionnés + 3 garde-fous récupérés : fallback 65% · discipline 3e trade · VIX élevé) |

---

## 5. DÉCISIONS TEMPORAIRES

| Sujet | État |
|---|---|
| Seuils désactivation stratégie (drawdown X% · N pertes) | Valeurs exactes à définir dans settings.py — à débattre en SESSION suivante |
| Sujet 1 — Frontend : discussion avant conception MODULE 03 | En attente — GATE bloquant MODULE 03 |
| Sujet 2 — Explication fonctionnement complet app | En attente — valider avec Abdelkrim |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Impact | Action |
|---|---|---|---|
| B1 | git.lock (batch Gemini actif) | Commit D-S30-10→17 non pushé | Faire le commit après arrêt batch : `git add . && git commit -m "feat(governance): lock D-S30-10 to D-S30-17"` |
| B2 | Circuit Breaker INACTIF (DETTE_TECHNIQUE.md Bug #2) | Mode AUTO strictement interdit | Réparer dans MODULE 02 |
| B3 | Batch Gemini (203 vidéos) — toujours en cours | MODULE 01 bloqué tant que batch non terminé | Vérifier état dans Claude Code |
| B4 | KB fusion (476 extractions S27) non commencée | MODULE 01 bloqué | Après batch terminé |
| B5 | Données dossier `data\` paths incorrects | Bug #2 DETTE_TECHNIQUE.md | Réparer dans MODULE 00 |

---

## 7. STACK TECHNIQUE GELÉE

```
Python 3.11 · Claude API (claude-sonnet-4-6 / haiku-4-5)
Gemini 2.5 Flash (transcriptions) · yt-dlp (download)
NT8 ATI TCP/IP port 36973 (Module 06 — BLOQUÉ)
React 18 + Vite + Tailwind 3.4 (MODULE 03 — à concevoir)
```

---

## 8. ÉTAT DES FICHIERS FIN SESSION

| Fichier | État |
|---|---|
| `00-pilotage\CLAUDE.md` | ✅ v2 — index court ~70 lignes |
| `00-pilotage\DECISIONS_VEROUILLEES.md` | ✅ 17 décisions verrouillées · 1 commit en attente (D-S30-10→17) |
| `00-pilotage\ARCHITECTURE_CONSTRUCTION.md` | ✅ v2 post-audit · MODULE 03/04/05 enrichis |
| `00-pilotage\SOURCES_TRIAGE_S30.md` | ✅ Trading Geek corrigé |
| `00-pilotage\_context\PROMPT_CLAUDE_CODE_BATCH_GEMINI_S30.md` | ✅ Prompt batch 203 vidéos |
| `05-saas\` (code Python) | ⏳ Aucun module commencé |
| `03-transcriptions\` | ⏳ Batch en cours |

---

## 9. COMMANDES GIT (PowerShell — UNE À LA FOIS)

⚠️ Batch Gemini peut encore tourner → vérifier si git.lock disparu avant.

**Vérifier le lock :**
```powershell
# Dans PowerShell — dossier C:\trading-copilote
Test-Path .git\index.lock
```
Si `True` → attendre fin batch.
Si `False` → exécuter dans l'ordre :

**Commande 1/3 :**
```powershell
cd C:\trading-copilote
git add 00-pilotage\DECISIONS_VEROUILLEES.md 00-pilotage\ARCHITECTURE_CONSTRUCTION.md 00-pilotage\_context\README_FIN_SESSION_S30_20260626.md
```
→ Attendre confirmation.

**Commande 2/3 :**
```powershell
git commit -m "feat(governance): lock D-S30-10 to D-S30-17 + README S30"
```
→ Attendre hash visible.

**Commande 3/3 :**
```powershell
git push origin main
```
→ Attendre "main -> main".

---

## 10. PRE-FLIGHT SESSION SUIVANTE

```
[ ] Lire CLAUDE.md EN ENTIER
[ ] Lire DECISIONS_VEROUILLEES.md (D-S30-1 → D-S30-17)
[ ] Lire ce README S30
[ ] Lire DETTE_TECHNIQUE.md
[ ] Vérifier état batch Gemini (03-transcriptions\ — combien de fichiers ?)
[ ] Confirmer git push S30 réussi (commit en attente)
[ ] Abdelkrim envoie Document 3 → lancer analyse comparative
```

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Session S31 TRADEX-AI.
Lis CLAUDE.md, DECISIONS_VEROUILLEES.md, README_FIN_SESSION_S30_20260626.md et DETTE_TECHNIQUE.md.
Annonce l'état en 1 ligne et la prochaine action.
```

---

## 12. DOCUMENTS REÇUS / EN ATTENTE

| # | Document | Analysé | Décisions |
|---|---|---|---|
| Doc 1 | CAHIER DES CHARGES (CDC) | ✅ | D-S30-1 à D-S30-9 |
| Doc 2 | APPLICATION DE TRADING ÉVOLUTIVE | ✅ | D-S30-10 à D-S30-17 |
| Doc 3 | ??? | ⏳ En attente | — |
| Doc N | ??? | ⏳ En attente | — |
| **Après tous les docs** | Mettre à jour FEUILLE_DE_ROUTE.md + GARDE_FOUS.md + 7 MODULE files | ⏳ | — |

---

*README généré par Cowork — Session S30 — 26/06/2026*
*Commit en attente : feat(governance): lock D-S30-10 to D-S30-17 + README S30*
