# README DE TRANSITION — TRADEX-AI
**Date :** 28/06/2026 · **Session :** S36 · **Score projet :** 62/100

---

## 1. ÉTAT ACTUEL DU PROJET

Circuit Breaker réparé (S36) — moteur Python désormais protégé contre les blocages API.
Phase C Track A engagée : C0A (tokens compact) + C0B (settings) + C1 (COT CFTC) exécutés et committés.
Branche `feature/phase-c-collectors` active avec 1 commit en avance sur main (cot_collector).
Reste à exécuter C2 (macro) + C3 (news) avant merge — et à obtenir les 3 clés API gratuites.
Mode AUTO toujours BLOQUÉ (`AUTO_MODE = False`).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| # | Mission | Commit | Résultat |
|---|---------|--------|----------|
| CB | Circuit Breaker réparé — `protected_call` dans `claude_brain.py` + `data_reader.py` | `3d0065b` | ✅ 21/21 PASS |
| DOCS | DETTE_TECHNIQUE.md — section 6 (CB) + section 2 (data\ existant) | `dc80473` + `78c8038` | ✅ |
| C0A | `load_kb_rules` format compact — 52 032 tokens < 55k — Gate 1 Phase B validé | `84d015d` | ✅ |
| C0B | `settings.py` Phase C paths + clés API + `FEUILLE_DE_ROUTE` décorrélé Gemini batch | `5efb480` | ✅ |
| C1 | `cot_collector.py` — CFTC OData v4 · codes contrats fixes (GC/HG/CL/ZW) | `7917cc4` *(branche)* | ✅ 3 cycles |

**Correction critique C1 :** l'API CFTC était brisée dans le prompt (OData v1 → 404, table TriWeeklyCombined → 404, filtre mot-clé ambigu → données fausses). Codes contrats fixes retenus : GC `088691` · HG `085692` · CL `067651` (WTI NYMEX physique) · ZW `001602` (SRW Chicago).

---

## 3. MISSION SUIVANTE

**Exécuter C2 + C3 dans Claude Code (dans cet ordre), puis merge sur main.**

Ordre d'exécution :
1. Ajouter `data/*.json` au `.gitignore` (avant tout push)
2. Confirmer choix COT : Futures-only (`6dca-aqww`) ou Combined (`jun7-fc8e`) — changer dans `cot_collector.py` si Futures-only
3. Exécuter `PROMPT_S36_C2_MACRO_COLLECTOR.md`
4. Exécuter `PROMPT_S36_C3_NEWS_COLLECTOR.md`
5. Merge `feature/phase-c-collectors` → `main` + push

---

## 4. DÉCISIONS PRISES

| Décision | Détail |
|----------|--------|
| Critère tokens Phase B | Révisé : < 55k (au lieu de 50k) — justifié par prompt caching Claude |
| Batch Gemini découplé Phase C | Gemini batch requis Phase E uniquement — Phase C démarrable à 42/203 vidéos |
| Filtre COT par code contrat | Codes fixes CFTC (pas filtre mot-clé) — non ambigu, stable dans le temps |
| data\ confirmé existant | `C:\trading-copilote\data` existe — DETTE_TECHNIQUE section 2 clôturée |
| C2/C3 dégradation gracieuse | Collecteurs fonctionnent sans clés API (mode GDELT/CFTC uniquement) |

---

## 5. DÉCISIONS TEMPORAIRES

| Décision | Échéance |
|----------|----------|
| COT : Futures-only ou Combined ? | À trancher avant exécution C2 (impact table API) |
| 3 clés API absentes (FRED / EIA / Finnhub) | À obtenir avant mise en prod réelle Phase C |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité | Action |
|---|---------|----------|--------|
| P1 | `data/*.json` non gitignoré — fichiers générés en untracked | P1 | Ajouter `data/*.json` à `.gitignore` AVANT push branche |
| P2 | 3 clés API manquantes : `FRED_API_KEY` · `EIA_API_KEY` · `FINNHUB_API_KEY` | P2 | Inscription gratuite (~5 min chacune) — voir liens ci-dessous |
| P3 | C2 + C3 non exécutés | P2 | Prochaine session — pas de blocage si clés absentes |
| P4 | Phase B Gate 3 : validation humaine 50 règles KB | P3 | Parallèle avec Phase C |
| P5 | Track B collecteurs (NT8 + ATAS) | P3 | Attend NT8/ATAS disponibles |
| P6 | Migration `google.generativeai` → `google.genai` | P2 | Avant mise en prod pipeline Gemini |

**Liens clés API gratuites :**
- FRED : https://fred.stlouisfed.org/docs/api/api_key.html
- EIA : https://www.eia.gov/opendata/register.php
- Finnhub : https://finnhub.io/register

---

## 7. STACK TECHNIQUE GELÉE

```
Python 3.x · requests 2.33.1 · anthropic SDK
Claude API : claude-sonnet-4-6 (system cache : cache_control persistent)
NT8 JSON (2s) → Python Engine → 3/4+2/3 filtre → Claude API → Signal 15 champs
CFTC OData v4 · FRED API v1 · EIA API v2 · Finnhub · GDELT v2
Atomic writes : tempfile + os.replace
AUTO_MODE = False (BLOQUÉ)
```

---

## 8. ÉTAT DES REPOS FIN SESSION

| Branche | HEAD | Contenu |
|---------|------|---------|
| `main` | `78c8038` | CB réparé + C0A + C0B + DETTE_TECHNIQUE |
| `feature/phase-c-collectors` | `7917cc4` | + cot_collector.py |

**Fichiers créés cette session :**
- `05-saas/engine/circuit_breaker.py` (modifié — protected_call actif)
- `05-saas/engine/claude_brain.py` (modifié — tokens 52k + CB)
- `05-saas/engine/data_reader.py` (modifié — CB actif)
- `05-saas/engine/cot_collector.py` (nouveau — branche)
- `05-saas/config/settings.py` (modifié — Phase C paths + clés)
- `00-pilotage/FEUILLE_DE_ROUTE.md` (modifié — Gate 2 + Phase E Gemini)
- `00-pilotage/DETTE_TECHNIQUE.md` (modifié — sections 2/6)
- `00-pilotage/_context/PROMPT_S36_C0A_COMPACT_KB.md`
- `00-pilotage/_context/PROMPT_S36_C0B_SETTINGS_PHASE_C.md`
- `00-pilotage/_context/PROMPT_S36_C1_COT_COLLECTOR.md`
- `00-pilotage/_context/PROMPT_S36_C2_MACRO_COLLECTOR.md`
- `00-pilotage/_context/PROMPT_S36_C3_NEWS_COLLECTOR.md`

**Fichiers encore à exécuter (prompts) :**
- `PROMPT_S36_C2_MACRO_COLLECTOR.md` ← prochaine session
- `PROMPT_S36_C3_NEWS_COLLECTOR.md` ← prochaine session

---

## 9. COMMANDES GIT POUR FIN DE SESSION

*(En PowerShell — une commande à la fois)*

Commande 1/3 :
```
git add 00-pilotage\_context\README_FIN_SESSION_S36_20260628.md
```
Commande 2/3 :
```
git commit -m "docs(session): README S36 — CB repare + Phase C C0A/C0B/C1 cot_collector"
```
Commande 3/3 (après confirmation commit) :
```
git push origin feature/phase-c-collectors
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

```
[ ] Lire CLAUDE.md
[ ] Lire ce fichier
[ ] Lire DETTE_TECHNIQUE.md
[ ] git status — vérifier branche feature/phase-c-collectors
[ ] Décider COT Futures-only (6dca-aqww) ou Combined (jun7-fc8e)
[ ] Ajouter data/*.json au .gitignore
[ ] Exécuter PROMPT_S36_C2_MACRO_COLLECTOR.md (Claude Code)
[ ] Exécuter PROMPT_S36_C3_NEWS_COLLECTOR.md (Claude Code)
[ ] Merger feature/phase-c-collectors → main + push
[ ] Si clés API obtenues : les ajouter dans .env et retester C2/C3
```

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Session S37 — TRADEX-AI.
Dernier commit main = 78c8038 (DETTE_TECHNIQUE section 2 résolue).
Branche active : feature/phase-c-collectors (HEAD = 7917cc4 — cot_collector OK).
KB Master = 1398 règles · Tokens = 52 032 · SHA256 = bcaaaeed.
Décision à prendre : COT Futures-only (6dca-aqww) ou Combined (jun7-fc8e) ?
À exécuter : PROMPT_S36_C2_MACRO_COLLECTOR.md puis C3, puis merger sur main.
Clés API manquantes : FRED_API_KEY · EIA_API_KEY · FINNHUB_API_KEY (gratuites, ~5 min).
```

---

## 12. ÉTAT KB

| Indicateur | Valeur |
|-----------|--------|
| Règles totales | **1 398** |
| Tokens load_kb_rules | **52 032** (compact, < 55k ✅) |
| Critère GO Phase B | ✅ validé |
| Formats coexistants | Vidéo (1 350) + Chapitre (48) |
| SHA256 | `bcaaaeed...` (voir SHA256_KB_MASTER.md) |
| Catégories | 11 (saisonnalite, correlations, timing, indicateurs_tendance, indicateurs_momentum, gestion_risque_entree, gestion_position_active, structure_marche, macro_evenements, volume_liquidite, psychologie) |

**Note :** KB inchangée cette session — seul le format d'affichage dans `load_kb_rules()` a été compacté (métadonnées statut/confiance/fiabilité retirées du texte envoyé à Claude, pas du fichier JSON).

---

*TRADEX-AI · README S36 · 28/06/2026 · Généré par readme-transition v3.4*
