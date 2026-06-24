# STRATÉGIE MULTI-AGENTS — SCRAPING KB TRADEX-AI

> **Statut :** PROPOSITION — exécution conditionnée à confirmation de scope (RÈGLE 0 + règle globale « confirmer le scope avant de lancer un workflow »).
> **Date :** 23/06/2026 · Session S22
> **Auteur :** Claude Code (gate prompt-gate-audit v4.3 — score 95/100, GÉNÉRER)
> **Périmètre :** 22 sources restantes de `KB_INDEX.md` · pipeline Phase 1→3.
> **Règle d'or héritée :** 0 hallucination · double ancrage texte/image obligatoire · manifest certifié · **un doute = STOP**.
>
> **⚠️ Backlog P1 (ARCH-17, décision 2026-05-02) :** extraction CME specs **HG · CL · ZW** (actifs TRADING verrouillés, specs manquantes). **NQ retiré — hors périmètre** (orphelin, n'appartient à aucune des 3 catégories verrouillées).

---

## 0. PROMPT AMÉLIORÉ (version corrigée du prompt source)

Le prompt initial était bon mais incomplet pour un usage TRADEX. Corrections appliquées :

| # | Faiblesse du prompt initial | Correction apportée |
|---|------------------------------|---------------------|
| 1 | Promettait des commandes « prêtes à copier-coller » pour les 22 sources | Seules les commandes **réellement exécutables aujourd'hui** sont fournies (GitBook). Les autres sont marquées « adaptateur à construire + valider sur 1 page test ». |
| 2 | Mentionnait « Selenium ou Playwright » sans vérifier l'installation | Vérifié : **ni Playwright ni Selenium en Python**. Rendu JS ⇒ outils navigateur MCP, pas une lib. |
| 3 | Ne traitait pas la dépendance Phase 3 (Cartographe + Orchestrateur non construits) | La stratégie distingue ce qui marche **maintenant** (Phase 1 manuelle par source) de ce qui exige de **construire** Phase 2/3. |
| 4 | Risquait de lancer un Dynamic Workflow coûteux sans garde-fou | Aligné sur la règle globale : workflow lourd réservé aux gros lots, **scope confirmé avant lancement**. |
| 5 | Ne précisait pas le critère pass/fail de certification image | Critère explicite : **manifest `0 à vérifier`** = condition de passage à l'extraction D###. |

---

## 1. ANALYSE PRÉALABLE — CE QUI EXISTE RÉELLEMENT

### 1.1 `scraper.py` v3.1 (lu intégralement)
- **Couplé à StockCharts/GitBook** : `SITE_ROOT` codé en dur, astuce `.md` GitBook, sélecteur image `data-testid="zoom-image"`, structure `<figure>/<figcaption>`.
- **Double ancrage** : image CERTIFIÉE seulement si `label .md == label HTML` au même rang. Sinon → `(A VERIFIER)`.
- **Pattern B (ARCH-15)** : figcaption vide → label = titre section `##` parent (sauf blacklist).
- **Filtre v3.1** : images `class="inline"` hors `<figure>` ignorées (décoratives).
- **Fix v3.2 (23/06/2026)** : images écrites dans `bundles/<source>/<nom_page>/images/` (sous-dossier par page) au lieu d'un `images/` partagé — corrige l'écrasement des images entre pages (numérotation `image_01..` commune).
- **Conclusion : réutilisable TEL QUEL uniquement pour les pages GitBook StockCharts.** Toute autre source = nouveau résolveur.

### 1.2 Format manifest certifié (lu : `rsi_manifest.txt`, `macd_manifest.txt`)
```
# Manifest images pour <page> (source : <source>)
# Page : <url>
# Methode : double ancrage ...
# Bilan : N certifiee(s) | M a verifier | K decorative(s)

image_XX.ext | label : <label> | section : <section> | CERTIFIE (accord .md + HTML)
(decorative)  | rang N | section : <section> | IGNOREE
(A VERIFIER)  | rang N | <raison> | url : <url>
```

### 1.3 Libs Python disponibles (vérifié `py -m pip list`)
| Lib | Version | Usage |
|-----|---------|-------|
| requests | 2.33.1 | ✅ HTTP |
| beautifulsoup4 | 4.15.0 | ✅ HTML statique |
| pdfplumber | 0.11.10 | ✅ texte + tableaux PDF |
| pypdf | 6.13.3 | ✅ PDF |
| pypdfium2 | 5.10.1 | ✅ rendu images PDF |
| **playwright** | ❌ ABSENT | rendu JS ⇒ via **MCP** uniquement |
| **selenium** | ❌ ABSENT | idem |

---

## 2. CLASSIFICATION DES 22 SOURCES PAR TYPE TECHNIQUE

| # | Source | Type technique | Outil | Réutilise scraper.py ? |
|---|--------|----------------|-------|------------------------|
| 1 | ADX (StockCharts) | **GitBook** | scraper.py v3.1 | ✅ TEL QUEL |
| 8 | Wyckoff (StockCharts) | **GitBook** | scraper.py v3.1 | ✅ TEL QUEL |
| 3a | Candlestick (StockCharts) | **GitBook** | scraper.py v3.1 | ✅ TEL QUEL |
| 3b | Candlestick Nison (candlecharts.com) | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 12 | bollingerbands.com | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 18 | Investopedia TA | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 19 | Adam Grimes Blog | HTML statique (WordPress) | bs4 + résolveur | ❌ adaptateur |
| 20 | Brooks Trading Course | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 21 | QuantifiedStrategies | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 22 | Fidelity Learning | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 5a | Optimus Footprint (blog) | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 13 | WindoTrader glossaire | HTML statique | bs4 + résolveur | ❌ adaptateur |
| 6/9 | Jim Dalton Trading | HTML statique (WordPress) | bs4 + résolveur | ❌ adaptateur |
| 10a | CME Backtesting (Harvey) | **PDF** | pdfplumber (texte) | ❌ adaptateur PDF |
| 11 | Cannon Behavioral Finance | **PDF** | pdfplumber (texte) | ❌ adaptateur PDF |
| 10b | arXiv Walk-Forward | HTML (`/html/`) ou PDF | bs4 ou pdfplumber | ❌ adaptateur |
| 2 | CME Institute + specs GC/ES (+ HG/CL/ZW à venir) | **JS / anti-bot** | MCP navigateur | ❌ + risque |
| 7/14 | Sierra Chart docs | HTML lourd (PHP) | bs4 (prudence) | ❌ adaptateur |
| 16 | NinjaTrader Learning | **JS** | MCP navigateur | ❌ + risque |
| 17 | NinjaTrader Order Flow | HTML semi-statique | bs4 / MCP | ❌ adaptateur |
| 4 | CFTC COT | HTML + fichiers data | bs4 + download | ❌ adaptateur |
| 15 | belkhayate.ma | HTML statique | **MANUEL** | ❌ trop sensible |

**Répartition :** 3 GitBook (prêtes) · 11 HTML statiques · 2 PDF · 1 arXiv · 3 JS/anti-bot · 1 mixte CFTC · 1 manuel.

---

## 3. ARCHITECTURE MULTI-AGENTS RETENUE

### 3.1 Schéma — pipeline à routage par type
```
                        ┌─────────────────────────────┐
                        │  A0 — ORCHESTRATEUR (lecture)│
                        │  dispatch + contrôle gates   │
                        └───────────────┬─────────────┘
                                        │
        ┌───────────────┬───────────────┼───────────────┬───────────────┐
        ▼               ▼               ▼               ▼               ▼
   CARTOGRAPHE     SCRAPER          SCRAPER          SCRAPER          SCRAPER
   (classe URL)    GitBook          StaticHTML       PDF              JS (MCP)
                   scraper.py       bs4+résolveur    pdfplumber       navigateur
        │               │               │               │               │
        └───────────────┴───────┬───────┴───────────────┴───────────────┘
                                 ▼
                     CERTIFICATEUR (double ancrage)
                     → manifest : N cert | M à vérifier | K déco
                                 │  gate : M == 0 ?
                          ┌──────┴──────┐
                       non│             │oui
                          ▼             ▼
                   TRAITEMENT      A2 — ANALYSTE (extraction D###)
                   MANUEL                │
                   (humain)              ▼
                                  VALIDATEUR QA (a8-qa-audit) — score /100
                                         │  pass ?
                                         ▼
                                  ARCHIVISTE — git commit + MAJ KB_INDEX
```

### 3.2 Rôles, responsabilité unique
| Agent | Type CC | Responsabilité (UNIQUE) | Écrit dans |
|-------|---------|--------------------------|------------|
| **A0 Orchestrateur** | `a0-orchestrateur` | Dispatch + contrôle des gates entre phases. **Lecture seule.** | rien |
| **Cartographe** | `Explore` / `general-purpose` | Classer chaque URL par type, vérifier accessibilité (HTTP 200 non déguisé). | `urls_queue.json` |
| **Scraper GitBook** | déterministe | Lancer `scraper.py`. | `bundles/<src>/` |
| **Scraper StaticHTML** | `general-purpose` | bs4 + résolveur images par site. | `bundles/<src>/` |
| **Scraper PDF** | `general-purpose` | pdfplumber → texte/tableaux. Images PDF = manuel. | `bundles/<src>/` |
| **Scraper JS** | `general-purpose` + MCP | Rendu via navigateur MCP, dump HTML. | `bundles/<src>/` |
| **Certificateur** | déterministe | Double ancrage → manifest. | `bundles/<src>/*_manifest.txt` |
| **A2 Analyste** | natif Claude | Extraction D### + tags + categorie. | `04-cerveau-trading/<src>/` |
| **Validateur QA** | `a8-qa-audit` | Score /100, vérifie manifest `0 à vérifier`. | rapport |
| **Archiviste** | déterministe | git commit + MAJ `KB_INDEX.md`. **Seul** à écrire les fichiers partagés. | `KB_INDEX.md`, git |

### 3.3 Garantie zéro hallucination (certification qualité)
1. **GitBook** : double ancrage natif `scraper.py` (déjà prouvé MA/RSI/MACD).
2. **StaticHTML** : principe du double ancrage répliqué — une image n'est CERTIFIÉE que si sa légende est trouvée par **2 chemins indépendants** (ex. `<figure><figcaption>` ET texte adjacent / `alt`). Désaccord ou source unique → `(A VERIFIER)`. Pas de légende → Pattern B (titre section) ou décorative.
3. **PDF** : **texte fiable** ; les images PDF n'ont pas de légende structurée fiable → **extraction images = MANUELLE par défaut** (jamais certifiées automatiquement).
4. **Gate dur** : aucune extraction D### tant que le manifest contient ≥ 1 ligne `(A VERIFIER)`.
5. **Tags KB** obligatoires : 🟢 uniquement si visible dans source ; sinon 🔴 / ⏳ / 🔵.

### 3.4 Coordination sans conflit
- **Sorties disjointes** : chaque source écrit dans `bundles/<source>/` distinct ; les **images** vont dans un sous-dossier **par page** `bundles/<source>/<nom_page>/images/` (scraper v3.2 — fix anti-écrasement, voir §1.1) → parallélisme sûr, **pas de worktree git nécessaire**.
- **Fichiers partagés** (`KB_INDEX.md`, `KNOWLEDGE_BASE_MASTER.json`) écrits **uniquement par l'Archiviste, séquentiellement** → aucune race condition.
- **Compteur D###** : incrément sérialisé par l'Archiviste (jamais en parallèle).

### 3.5 Temps estimé par source (estimations, réseau-dépendant)
| Type | Temps / page | Cause |
|------|--------------|-------|
| GitBook | 1–3 min | `SLEEP_IMG=2s` × nb images (politesse serveur) |
| StaticHTML | 2–4 min | + écriture/validation résolveur |
| PDF (texte) | < 30 s | pas d'images |
| JS (MCP) | 5–10 min | setup navigateur + rendu |
| Construction d'un adaptateur | 30–60 min | code + test sur 1 page + revue |

### 3.6 Risques & mitigations
| Risque | Niveau | Mitigation |
|--------|--------|------------|
| Adaptateur StaticHTML produit de faux labels | Élevé | Double ancrage obligatoire + gate `0 à vérifier` + test 1 page avant fan-out |
| CME / NinjaTrader anti-bot (Akamai) | Moyen | Tenter MCP navigateur ; échec → **download manuel PDF specs** |
| Images PDF non certifiables | Moyen | Texte seul auto ; images = manuel documenté |
| arXiv preprint = source non peer-reviewed | Moyen | Tag ⏳ + mention « preprint » dans chaque D### |
| belkhayate.ma formule propriétaire | Critique | **Manuel**, garde ⚫ + 🔴 + mention repaint (ARCH-13) |
| Coût tokens workflow lourd | Moyen | Pas de Dynamic Workflow auto ; lots P0→P4 confirmés un par un |

---

## 4. DÉCOUPAGE — QUI FAIT QUOI

### 4.1 ✅ scraper.py v3.1 TEL QUEL (aucun code)
- ADX (P0) · Wyckoff (P3) · Candlestick StockCharts (P1)

### 4.2 ⚙️ Adaptateur spécifique à construire + valider sur 1 page test
- **StaticHTML** : bollingerbands, candlecharts/Nison, Investopedia, Adam Grimes, Brooks, QuantifiedStrategies, Fidelity, Optimus, WindoTrader, Jim Dalton, Sierra Chart, NinjaTrader Order Flow, CFTC.
- **PDF** : CME Backtesting, Cannon Behavioral (texte seul).
- **arXiv** : version `/html/` via bs4 (fallback PDF).

### 4.3 🚫 Trop risqué → EXTRACTION MANUELLE recommandée
- **belkhayate.ma** : propriétaire, formule jamais publiée — manuel + gardes.
- **CME Institute / specs** : si anti-bot → download manuel des PDF de specs contractuelles.
- **NinjaTrader Learning (JS)** : si rendu MCP instable → extraction manuelle ciblée.
- **Images de tout PDF** : manuel par défaut.

---

## 5. PLAN D'EXÉCUTION PRIORISÉ

### Ordre (P0 → P4) et dépendances
```
LOT P0  ADX                    → scraper.py prêt. AUCUNE dépendance. À LANCER EN PREMIER.
   │
   ▼ (gate : manifest 0 à vérifier + D62+ extraites + commit)
LOT P1  Candlestick + CME specs + COT
   │    dépend de : adaptateur StaticHTML validé (Candlestick Nison) + décision CME (MCP vs manuel)
   ▼
LOT P2  Footprint + Market Profile + VWAP   (adaptateurs StaticHTML)
   ▼
LOT P3  Wyckoff (GitBook, sans dép.) + Price Action (StaticHTML)
   ▼
LOT P4  Walk-forward (PDF/arXiv) + Biais cognitifs (PDF)
```

### Points de contrôle qualité OBLIGATOIRES (entre chaque source)
1. **CP1 — URL** : HTTP 200 réel (pas « Page Not Found » déguisé). → STOP sinon.
2. **CP2 — Manifest** : `0 à vérifier`. Sinon → traitement manuel des lignes listées.
3. **CP3 — Extraction** : chaque D### cite `fichier.md + image_XX`. Tag 🟢 seulement si visible.
4. **CP4 — QA** : score /100 ≥ seuil (a8-qa-audit). Sinon → corriger.
5. **CP5 — Archive** : compteur KB_INDEX à jour + commit + push.

---

## 6. TEMPLATES DE MANIFEST PAR TYPE

### 6.1 GitBook / StaticHTML (image certifiable)
```
# Manifest images pour <page> (source : <src>)
# Page : <url>
# Methode : double ancrage (.md/HTML figcaption + ancrage local)
# Bilan : N certifiee(s) | M a verifier | K decorative(s)

image_XX.ext | label : <label> | section : <section> | CERTIFIE (accord 2 sources)
(decorative) | rang N | section : <section> | IGNOREE
(A VERIFIER) | rang N | <raison> | url : <url>
```

### 6.2 PDF (texte seul, images manuelles)
```
# Manifest PDF pour <page> (source : <src>)
# Fichier : <chemin.pdf> | pages : <n>
# Methode : pdfplumber (texte+tableaux). Images = MANUEL.
# Bilan : texte=OK | images_auto=0 | images_a_extraire_manuellement=<k>

texte_page_01..NN.txt | CERTIFIE (extrait direct PDF)
(image manuelle) | page N | <description> | A EXTRAIRE MANUELLEMENT
```

---

## 7. COMMANDES PRÊTES (uniquement les exécutables aujourd'hui)

> ⚠️ Seules les commandes GitBook fonctionnent **sans nouveau code**. Les autres exigent un adaptateur validé d'abord — ne pas les inventer.

### 7.1 P0 — ADX (exécutable maintenant)
```powershell
cd C:\trading-copilote\01-pipeline
# CP1 : tester l'URL d'abord
py -c "import requests; r=requests.get('https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx.md', headers={'User-Agent':'Mozilla/5.0'}, timeout=25); print(r.status_code, len(r.text))"
# Si 200 et taille > 500 :
py scraper.py "https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx" stockcharts adx
```

### 7.2 P3 — Wyckoff (GitBook, exécutable après P0)
```powershell
cd C:\trading-copilote\01-pipeline
py scraper.py "https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial" stockcharts wyckoff
```

### 7.3 Autres sources
> **À CONSTRUIRE** : adaptateur `scraper_static.py` / `scraper_pdf.py` validé sur 1 page test avant tout fan-out. Commande type (NON fonctionnelle tant que l'adaptateur n'existe pas) :
> `py scraper_static.py "<URL>" <source> <nom_page>`

---

## 8. CRITÈRES DE VALIDATION QUALITÉ (PASS / FAIL)

| Critère | PASS | FAIL |
|---------|------|------|
| URL accessible | HTTP 200 + contenu > 500 car | 404 / page déguisée / vide |
| Pré-sélecteur TRADEX | ≥ 1 mot-clé scope | hors scope |
| Manifest images | `0 à vérifier` | ≥ 1 `(A VERIFIER)` non traité |
| Certification image | accord 2 sources | source unique / désaccord |
| Extraction D### | cite source + image | tag 🟢 sans preuve |
| QA score | ≥ seuil a8-qa-audit | < seuil |
| Belkhayate | ⚫ + 🔴 + repaint présents | gardes absentes |

---

## 9. DÉCISION D'EXÉCUTION (à confirmer par Abdelkrim)

Conformément à RÈGLE 0 et à la règle globale « confirmer le scope avant de lancer », **aucune exécution n'est lancée automatiquement**. Trois options :

- **Option A (recommandée)** : lancer **seulement le LOT P0 — ADX** maintenant (scraper prêt, zéro code, zéro risque). Valider la chaîne complète bout-en-bout sur 1 source avant tout le reste.
- **Option B** : construire d'abord l'adaptateur `scraper_static.py` (gate STRICT — code) et le valider sur 1 page test (ex. Fidelity RSI), puis enchaîner P1.
- **Option C** : produire seulement ce document et planifier les lots ultérieurement.

> **Pas de Dynamic Workflow lourd** tant que les adaptateurs ne sont pas validés : sinon = coût tokens élevé sur des résolveurs non fiables (violation règle globale).

---

*STRATEGIE_MULTI_AGENTS_SCRAPING · TRADEX-AI · 23/06/2026 · S22*
*Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
