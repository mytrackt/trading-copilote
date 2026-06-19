# RAPPORT D'EXTRACTION — PDF « MBK VIP Groupe »

**Date :** 2026-06-17
**Mission :** extraire le texte réel des PDF (réputés non extractibles, type Google Docs à police sous-ensemble) pour évaluer leur valeur pour TRADEX.
**Source :** `D:\TRADING MBK\MBK VIP Groupe\` (lecture seule).
**Sorties brutes :** `C:\trading-copilote\_temp_extraction\PDF_OCR\<nom>.txt`
**Outils :** Python 3.12 + `pdfplumber` 0.11.10 (fallback `pypdf` 6.13.3). **Aucun OCR n'a été nécessaire** : les 6 PDF ont rendu du texte direct lisible (> 200 caractères cohérents). Tesseract non sollicité.

> ⚠️ **Note anti-hallucination** : seuls les textes réellement extraits ont été analysés. Tous les chiffres de performance/projection (BlackRock, JSTX) sont des **CLAIMS NON VÉRIFIÉS** et ne doivent jamais être présentés comme des faits.

---

## SOMMAIRE

1. [code Smeers](#1--code-smeers) — 🟢
2. [sachant_que_je_veux_decortiquer…3_phases](#2--sachant_que_je_veux_decortiquer_un_mouvement_boursier_en_3_phases) — 🔴
3. [cadeau pour mes abonnes VIP](#3--cadeau-pour-mes-abonnes-vip) — 🟢
4. [Why This Project Can Interest BlackRock](#4--why-this-project-can-interest-blackrock) — 🔴
5. [JSTX Financial Projections](#5--jstx-financial-projections-unlocking-africas-potential) — 🔴
6. [AI World Championship v.2](#6--ai-world-championship-v2) — 🔴
7. [Tableau de synthèse](#tableau-de-synthèse)

---

## 1 — code Smeers

- **Pages :** 2 — **Méthode :** texte direct (pdfplumber) — 2 689 caractères.
- **Nature :** code source d'un indicateur **TradingView Pine Script v5** intitulé `"Smart Trend Matrix Advanced"`.

**Résumé factuel :**
Indicateur de tendance combinant plusieurs briques : un **filtre de Kalman simplifié** appliqué à une EMA, un **ATR pondéré par le volume (VWATR)** pour tracer support/résistance dynamiques, un momentum = (RSI/100) × ligne MACD, des niveaux de **Fibonacci dynamiques** (×1.618 / ×0.618 autour de l'EMA), et une confirmation de volume. Les signaux d'achat/vente combinent proximité support/résistance + couleur de tendance + volume confirmé + momentum + position vs Fibonacci. Le code est complet et fonctionnel (compilable tel quel sur TradingView).

**Formules / paramètres concrets (VERBATIM) :**
- `length_ema = input(14)` ; `length_atr = input(14)` ; `proximity_threshold = input(1.0)` (% ) ; `volume_multiplier = input(1.5)`
- Kalman : `p := p + q` ; `k := p / (p + r)` ; `x_est := x_est + k * (x - x_est)` ; `p := (1 - k) * p` — appelé avec `q=0.001, r=0.1`
- VWATR : `atr_value = ta.atr(length_atr) * (volume / ta.sma(volume, length_atr))`
- Support/résistance : `support_level = low - atr_value` ; `resistance_level = high + atr_value`
- Momentum : `momentum = (rsi_value / 100) * macd_line` avec `ta.rsi(close,14)` et `ta.macd(close,12,26,9)`
- Fibonacci : `fib_upper = ema_value * 1.618` ; `fib_lower = ema_value * 0.618`
- Confirmation volume : `volume > ta.sma(volume,20) * volume_multiplier`
- `buy_signal = is_near_support and trend==green and volume_confirmed and momentum>0 and close>fib_lower` (et symétrique pour `sell_signal`)

**VERDICT : 🟢 matière exploitable** — code réel, paramétré, immédiatement reproductible. Briques réutilisables pour TRADEX : lissage Kalman d'une moyenne, ATR normalisé par le volume (VWATR), et schéma de confluence multi-filtres. À backtester (les valeurs Fibonacci ×1.618 d'une EMA sont peu orthodoxes et à valider). Pas de preuve de performance fournie.

---

## 2 — sachant_que_je_veux_decortiquer_un_mouvement_boursier_en_3_phases

- **Pages :** 1 — **Méthode :** texte direct (pdfplumber) — 649 caractères.
- **Nature :** **prompt** (suite de questions adressées à une IA), PAS un document de méthode.

**Résumé factuel :**
Le document est la transcription d'une demande utilisateur : décortiquer un mouvement boursier en **3 phases** (phase imprévisible / phase de repos / phase prévisible) en **combinant la constante de Feigenbaum** (« appliquée au carnet d'ordre ») avec les **coefficients de Lyapunov** pour identifier ces phases en temps réel, et demande le code d'un indicateur **NinjaTrader**. Suivent des questions ouvertes (« les mathématiques fractales peuvent-elles affiner l'indicateur ? », « en quoi Lyapunov aide à identifier les meilleures zones ? »). **Aucune réponse, aucun code, aucune formule n'est présent dans ce fichier.**

**Sur Feigenbaum / Lyapunov / les 3 phases :** il s'agit d'une **IDÉE / intention de recherche**, pas d'une méthode opérationnelle. Le texte énonce un souhait de combinaison (Feigenbaum sur le carnet d'ordre + exposants de Lyapunov → segmentation en 3 régimes) mais ne définit **aucun** seuil, fenêtre, calcul ou règle. Rien n'indique comment la constante de Feigenbaum (δ ≈ 4.669, propre aux cascades de doublement de période) s'appliquerait concrètement à un carnet d'ordre — affirmation non étayée.

**Formules / paramètres :** aucune formule exploitable.

**VERDICT : 🔴 narratif / intention sans valeur technique** (dans CE fichier). À noter : la piste « exposant de Lyapunov pour mesurer la prévisibilité » est reprise et **discutée sérieusement dans le doc n°3 (cadeau VIP)**, qui la juge *non faisable* en pratique sur 30 points. Voir §3.

---

## 3 — cadeau pour mes abonnes VIP

- **Pages :** 24 — **Méthode :** texte direct (pdfplumber) — 42 521 caractères.
- **Nature :** dossier de recherche (style généré par IA / Grok) sur la construction d'un **« indice de prévisibilité » par corridor de 30 minutes**, avec **code complet NinjaTrader (C#/NinjaScript)** fourni. C'est le document le plus substantiel techniquement.

**Résumé factuel :**
Le document explore et compare plusieurs mesures mathématiques pour quantifier la prévisibilité d'un marché sur des fenêtres de 30 min (≈ 30 barres 1 min) :
1. **Coefficient de Hurst + Entropie de permutation** : Hurst mesure la mémoire long terme (mean-reversion < 0.5, aléatoire = 0.5, tendance > 0.5) ; l'entropie de permutation mesure la complexité court terme. Indice proposé = **`H - PE`** (élevé ⇒ plus prévisible).
2. **R² d'une régression multiple** (recommandé) : régresser les variations de prix sur le **volume** et le **delta bid/ask** : `ΔP_t = a + b·V_t + c·D_t + ε_t`, avec `R² = 1 − (var(ε) / var(ΔP))`. R² élevé ⇒ volume + flux d'ordres expliquent bien le prix ⇒ marché plus prévisible.
3. **Prédiction du « rendement espéré »** du corridor suivant : `expected_return = R² × (somme des ΔP du corridor courant)`.
Le doc fournit du **code C# NinjaScript complet et compilable** : agrégation tick→minute, calcul du delta (BuyVolume = trades à l'ask, SellVolume = trades au bid), buffer glissant de 30 minutes, résolution moindres carrés via inversion d'une matrice 3×3 (XᵀX), calcul du R² et tracé. Il évalue aussi — et **écarte comme non faisables** sur 30 points / en Pine Script — l'information mutuelle, l'**exposant de Lyapunov**, la dimension fractale/multifractale, les modèles VAR, le lambda de Kyle et la mesure d'illiquidité d'Amihud.

**Formules / paramètres concrets (VERBATIM) :**
- Indice 1 : `predictability = Hurst Coefficient − Permutation Entropy` (`H − PE`)
- Modèle 2 : `ΔP_t = a + b·V_t + c·D_t + ε_t` ; `R² = 1 − (variance ε_t / variance ΔP_t)`
- Delta : `delta = BuyVolume − SellVolume` (Buy = `LastPrice ≈ Ask`, Sell = `LastPrice ≈ Bid`)
- Prédiction : `expected_return = rSquared × total_price_change` où `total_price_change = Σ ΔP du corridor`
- Fenêtre : `corridorSize = 30` minutes (barres 1 min) ; relation Hurst/variance ratio citée : `VR(k) = k^(2H−1)`
- Edge cases : matrice singulière ⇒ `R² = NaN` ⇒ `expected_return = 0`

**VERDICT : 🟢 matière exploitable (la plus riche)** — concepts opérationnels + code prêt à porter. Pistes directement utiles à TRADEX : (a) **indice de prévisibilité par régime/fenêtre** combinant mémoire (Hurst) et complexité (entropie de permutation) ; (b) **R² volume+delta** comme jauge de « marché lisible » pour filtrer les périodes de trading ; (c) le mapping clair de ce qui est **faisable vs. non faisable** en temps réel (écarte Lyapunov/multifractal). ⚠️ Réserves à intégrer telles quelles dans le doc lui-même : 30 points = sur-apprentissage probable de la régression à 3 paramètres ; le lien « R² élevé ⇒ rendement futur » n'est pas démontré et **doit être backtesté** ; aucune preuve de performance n'est fournie.

---

## 4 — Why This Project Can Interest BlackRock

- **Pages :** 4 — **Méthode :** texte direct (pdfplumber) — 6 666 caractères.
- **Nature :** document **commercial / pitch** (anglais) argumentant pourquoi BlackRock s'associerait à « JSTX », plateforme de tokenisation d'actifs africains.

**Résumé factuel :**
Argumentaire de partenariat : accès aux marchés africains « inexploités » via tokenisation (obligations, mines, immobilier, hôtels, terres), alignement ESG, fractionnement de propriété, liquidité, conformité (FSCA/SEC/ESMA), avantage de premier entrant, synergies technologiques (mention d'intégration avec la plateforme **Aladdin** de BlackRock et d'une « Qwen AI »). Propose une structure de partenariat (prise de participation minoritaire, joint-ventures, listings, partage de savoir).

**Formules / paramètres :** aucune. Le « 10 000 milliards $ d'AUM de BlackRock » est un fait public ; tout le reste relève de l'argumentaire.

**VERDICT : 🔴 marketing-business sans valeur technique** pour TRADEX. Aucune méthode, aucun signal, aucun code. Le rapprochement BlackRock = **CLAIM NON VÉRIFIÉ** (simple hypothèse de pitch, aucune relation attestée).

---

## 5 — JSTX Financial Projections: Unlocking Africa's Potential

- **Pages :** 3 — **Méthode :** texte direct (pdfplumber) — 4 713 caractères.
- **Nature :** **projections financières** d'une plateforme de tokenisation (JSTX).

**Résumé factuel :**
Hypothèses : 45 Md$ d'actifs tokenisés (5 obligations / 10 mines / 15 immobilier / 5 hôtels / 10 terres) ; pénétration 10 %→30 %→60 % sur 3 ans ; revenus = frais de trading 0,2 %/transaction + frais de listing 50 000 $/actif + frais de garde 0,1 %/an. Tableau de projection annonçant un **profit net cumulé « > 500 M$ sur 3 ans »** (33,5 → 150,5 → 321 M$). Ton promotionnel (« Are you ready to transform Africa's wealth… ? »).

**Paramètres cités (VERBATIM, en tant qu'HYPOTHÈSES, pas de formule de trading) :**
- Frais : trading 0,2 % ; listing 50 000 $/actif ; custody 0,1 %/an
- Coûts : setup 10 M$ ; opex annuel ~20–60 M$
- Profit cumulé revendiqué : **505 M$ sur 3 ans**

**VERDICT : 🔴 business / projections — CLAIMS NON VÉRIFIÉS.** Aucune valeur technique trading. Tous les chiffres sont des **projections hypothétiques** (taux de pénétration choisis arbitrairement), à ne jamais présenter comme des résultats.

---

## 6 — AI World Championship v.2

- **Pages :** 21 — **Méthode :** texte direct (pdfplumber) — 16 189 caractères. (PDF de 13,5 Mo : poids dû aux images ; le texte est néanmoins propre, OCR inutile.)
- **Nature :** **brochure d'événement** — présentation d'un « AI World Championship » organisé à **ADNEC, Abu Dhabi, 7–9 avril 202x** (objectif affiché : faire des EAU un leader mondial de l'IA).

**Résumé factuel :**
Plaquette institutionnelle : définition de l'événement, catégories de compétition (NLP, vision, robotique, jeux, santé, **AI financière**, IA éthique), critères de participation et de jugement, opportunités de networking/sponsoring, format de l'événement final, soutien du Department of Culture and Tourism d'Abu Dhabi. La catégorie « Financial AI » est citée en une ligne (trading algorithmique, risque, fraude) sans aucun contenu technique.

**Formules / paramètres :** aucune formule exploitable.

**VERDICT : 🔴 marketing événementiel sans valeur technique** pour TRADEX.

---

## Tableau de synthèse

| PDF | Pages | Méthode | Formules/paramètres ? | Verdict utilité |
|---|---|---|---|---|
| code Smeers | 2 | Texte direct | ✅ Oui — Pine Script v5 complet (Kalman, VWATR, Fibo, momentum) | 🟢 Exploitable |
| sachant…3_phases | 1 | Texte direct | ❌ Non (prompt/intention) | 🔴 Narratif |
| cadeau pour mes abonnes VIP | 24 | Texte direct | ✅ Oui — Hurst−PE, R²(ΔP~V,D), code NinjaScript C# | 🟢 Exploitable (le + riche) |
| Why This Project…BlackRock | 4 | Texte direct | ❌ Non | 🔴 Marketing (claim non vérifié) |
| JSTX Financial Projections | 3 | Texte direct | ⚠️ Hypothèses business (pas de formule trading) | 🔴 Business (claims non vérifiés) |
| AI World Championship v.2 | 21 | Texte direct | ❌ Non | 🔴 Marketing événementiel |

---

> ## 📦 BILAN
> **PDF TRAITÉS : 6 | TEXTE RÉCUPÉRÉ : 6 | ÉCHECS OCR : 0** (aucun OCR requis — extraction texte direct suffisante pour tous)
> **DONT MATIÈRE TECHNIQUE EXPLOITABLE (🟢) : 2** → `code Smeers` (indicateur Pine Script paramétré) et `cadeau pour mes abonnes VIP` (indice de prévisibilité Hurst/entropie + R² volume/delta + code NinjaScript).
>
> **PROCHAINE ACTION :** backtester les deux pistes 🟢 avant toute intégration TRADEX —
> (1) valider le R²(ΔP ~ volume + delta) sur 30 min comme **filtre de régime** (et tester une fenêtre > 30 points pour éviter le sur-apprentissage de la régression 3-paramètres) ;
> (2) extraire de `code Smeers` les briques **VWATR** (ATR normalisé volume) et **lissage Kalman d'EMA** pour évaluation isolée.
> Les 4 PDF 🔴 (BlackRock, JSTX, AI World Championship, doc 3-phases) sont à archiver : aucune valeur technique, chiffres financiers = claims non vérifiés.
