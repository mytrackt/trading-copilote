# README DE TRANSITION — TRADEX-AI
**Date :** 13/06/2026 | **Session :** S06 | **Mode :** Cowork

---

## 1. ÉTAT ACTUEL DU PROJET

Aucun code écrit cette session. Session de documentation stratégique intensive :
8 fichiers audités contre CLAUDE.md + STRATEGIE_TRADEX_CORRIGEE v2.0.
La stratégie corrigée v2.0 est générée et sauvegardée dans `00-pilotage\`.
Le moteur SaaS (05-saas\) est intouché. Whisper toujours en cours (état inconnu, était 39/110 début session).
Mode AUTO : BLOQUÉ. Bug `data\` : toujours non réparé (BLOCKER Phase C).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Fichier produit | Statut |
|---|---|---|---|
| Audit v1.0 vs CLAUDE.md | 8 incompatibilités identifiées dans STRATEGIE_TRADEX_8_MARCHES.md | — | ✅ |
| Génération v2.0 | STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md (8 corrections C1–C8 appliquées) | `00-pilotage\STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md` | ✅ |
| Cross-audit KB_MASTER vs TRADEX_CORRIGEE | Deux docs complémentaires, non concurrents | — | ✅ |
| Audit KB_MASTER méthode Belkhayate officielle | Limites honnêtes déclarées, corrections 1-2 solides, 3-7 à valider | — | ✅ |
| Audit batch 1 (4 fichiers) vs TRADEX_CORRIGEE | BACKLOG, DETTE_TECHNIQUE, GUIDE MAÎTRE, MBK-report | — | ✅ |
| Audit batch 2 (4 fichiers) vs TRADEX_CORRIGEE | competence-intermarches, indices-marches, prompt-intermarches, STRATEGIE v1.0 | — | ✅ |
| Mise à jour mémoire persistante | Étapes 1+2+3 documentées | `memory/project_tradex_phase_b.md` | ✅ |

---

## 3. MISSION SUIVANTE

**Option A (passive)** : Attendre fin Whisper (X/110) → récupérer AUDIT_QUALITE.md → extraction KB Phase B-02.

**Option B (active)** : Démarrer Phase B-01 maintenant → Academia.edu PDF "belkhayate gravity center" + Pine Script TradingView → coder `05-saas\engine\belkhayate_formulas.py`.

**Décision en attente :** choisir A ou B au démarrage de S07.

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| D1 | Bitcoin (MBT) et Yen (6J) = RÉFÉRENCE uniquement, zéro ordre — jamais rouvrir | 🔒 VERROUILLÉ |
| D2 | Score signal = /10 (TRADEX_CORRIGEE) — prompts /100 = génériques incompatibles | 🔒 VERROUILLÉ |
| D3 | Précondition entrée = 3/4 TRADING + 2/3 CONFIRMATION (Step 0) — "≥5/8" = incompatible | 🔒 VERROUILLÉ |
| D4 | EUR/USD (6E) supprimé définitivement de la liste des marchés TRADEX | 🔒 VERROUILLÉ |
| D5 | Architecture = JSON NT8 (pas de screenshot, pas de Vision API) | 🔒 VERROUILLÉ |
| D6 | News gate = 30 min AVANT NFP/FOMC/CPI (±15 min était faux) | 🔒 VERROUILLÉ |

---

## 5. RÉSULTATS AUDIT 8 FICHIERS — SYNTHÈSE

### Batch 1 (audité contre TRADEX_CORRIGEE v2.0)
| Fichier | Verdict | Action requise |
|---|---|---|
| BACKLOG_ENRICHISSEMENTS.md | ✅ Compatible | Score /21 à trancher (Phase D) ; 6 modes trading à garder |
| DETTE_TECHNIQUE.md | ✅ Utile | Bug `data\` doit être réparé AVANT Phase C |
| GUIDE MAÎTRE Belkhayate | ⚠️ Partiel | Setup Squeeze/Tir à l'arc = à intégrer ? VWAP+MFI à ajouter ? TF 30min/15min vs H4/H1 ? |
| MBK-deep-research-report | ⚠️ Partiel | COG lookback : 100-125 barres (communauté) vs 250 barres (Admiral Markets) → à backtester |

### Batch 2
| Fichier | Verdict | Action requise |
|---|---|---|
| competence-intermarches.txt | ⚠️ Partiel | Remplacer seuil "5/8" par "3/4+2/3" — source utile couche intermarché |
| indices-marches.txt | ✅ Bon | Ajouter ZW ; clarifier BTC = référence zéro ordre |
| prompt-systeme-trading-intermarches.txt | 🔴 Incompatible | BTC+Yen tradables, score /100, pas Belkhayate — à NE PAS utiliser comme système |
| STRATEGIE_8_MARCHES-6023779b.md | ❌ Obsolète | Version v1.0 remplacée par v2.0 — ne plus utiliser |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🔴 P0 | Bug `data\` folder inexistant → staleness_monitor, data_reader, settings cassés | OUI — Phase C |
| 🟡 P1 | Whisper pipeline : état inconnu (était 39/110) — relancer sur PC Abdelkrim | NON |
| 🟡 P1 | Score /21 (7 cercles CLAUDE.md) vs /10 (TRADEX_CORRIGEE) → à trancher Phase D | NON |
| 🟡 P1 | COG lookback : 100-125 barres vs 250 barres → à décider via backtest | NON |
| 🟡 P2 | Philosophie entrée : Squeeze/breakout (GUIDE MAÎTRE) vs mean reversion (TRADEX_CORRIGEE) → à valider transcripts réels | NON |
| 🟡 P2 | VWAP et MFI : à intégrer dans TRADEX ou pas ? → attendre transcripts | NON |
| 🟡 P2 | KB entière invalide (142 fichiers = synthèses NotebookLM, pas vrais transcripts) → rebuild Phase B | NON |

---

## 7. STACK TECHNIQUE GELÉE (inchangée)

```
Plateforme trading  : NinjaTrader 8 (port 36973 ATI)
Order flow          : ATAS Pro (connecté Rithmic)
Backend             : Python 3.11 + FastAPI
Dashboard           : React 18 + Vite + Tailwind 3.4
DB                  : SQLite
Cerveau IA          : Claude API claude-sonnet-4-6
Exécution ordres    : NT8 ATI TCP/IP local
OS                  : Windows 11 + PowerShell 7.6.2
```

**Actifs verrouillés :**
- TRADING : GC, HG, CL, ZW
- CONFIRMATION : DX, ES, VX
- RÉFÉRENCE (zéro ordre) : MBT, 6J

---

## 8. ÉTAT DES FICHIERS FIN SESSION

| Fichier | État |
|---|---|
| `00-pilotage\STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md` | ✅ CRÉÉ cette session (v2.0) |
| `00-pilotage\_context\README_TRANSITION_TRADEX_S06_20260613.md` | ✅ CE FICHIER |
| `memory/project_tradex_phase_b.md` | ✅ MIS À JOUR (Étapes 1+2+3) |
| `05-saas\` (code SaaS) | ⏸️ NON TOUCHÉ |
| `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` | ⏸️ NON TOUCHÉ (invalide — à reconstruire) |

---

## 9. COMMANDES GIT (PowerShell)

```powershell
cd C:\trading-copilote
git add .
git commit -m "chore: session S06 audit 8 fichiers termine"
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

Avant toute action en S07 :

1. Lire `CLAUDE.md` EN ENTIER
2. Lire CE fichier (`README_TRANSITION_TRADEX_S06_20260613.md`)
3. Lire `00-pilotage\DETTE_TECHNIQUE.md`
4. Vérifier état Whisper : combien de vidéos traitées sur 110 ?
5. Choisir Option A ou B (Whisper terminé ou pas)
6. Confirmer bug `data\` toujours non réparé avant toute Phase C

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> "Je reprends TRADEX-AI session S07. Lis CLAUDE.md + README_TRANSITION_TRADEX_S06_20260613.md. Décisions verrouillées : JSON NT8, FastAPI, port 36973, BTC/Yen = référence zéro ordre, score /10, précondition 3/4+2/3. Whisper est [terminé X/110 / toujours en cours à X/110]. Je choisis [Option A / Option B]."

---

*README_TRANSITION_TRADEX_S06_20260613.md — généré automatiquement fin session S06*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
