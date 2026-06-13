# STRATÉGIE TRADEX — MÉTHODE BELKHAYATE — VERSION CORRIGÉE CLAUDE.md
**Version 2.0 — 13 juin 2026 — Usage strictement privé (Abdelkrim / TRADEX-AI)**

> ⚠️ **Règle de vérité** : chaque élément porte une étiquette **[DOCUMENTÉ]** (source publique), **[RECONSTRUCTION]** (formule communautaire, original jamais publié), **[NON DOCUMENTÉ]**, **[AMÉLIORATION PROPOSÉE]** ou **[HYPOTHÈSE TESTABLE]** (paramètre de départ à backtester, jamais une vérité).

> 🔧 **Journal des corrections v1.0 → v2.0** (alignement CLAUDE.md) :
> - C1 : BTC (MBT) et Yen (6J) reclassés RÉFÉRENCE — zéro ordre possible
> - C2 : EUR/USD (6E) et T-Notes (ZN) supprimés — absents du référentiel TRADEX
> - C3 : Blé (ZW) ajouté en TRADING — actif verrouillé dans CLAUDE.md
> - C4 : Dollar Index (DX) et VIX (VX) ajoutés en CONFIRMATION
> - C5 : Architecture données = JSON NT8 uniquement (pas de screenshot, pas de Vision API)
> - C6 : News Gate corrigé à 30 min avant / 15 min après (était ±15 min)
> - C7 : Règle d'entrée 3/4 + 2/3 ajoutée comme pré-condition éliminatoire (Étape 0)
> - C8 : Règle intermarché "5/8" remplacée par logique TRADEX 4+3+2

---

# PARTIE 1 — FONDATIONS : MÉTHODE BELKHAYATE

## 1.1 Les 3 piliers

### Pilier 1 — Centre de Gravité / Barycentre (COG dynamique)
**[DOCUMENTÉ]** : régression polynomiale non paramétrique sur ~250 périodes ; ligne centrale bleue (biais haussier) ou rouge (biais baissier) ; 3 écarts-types au-dessus (bandes rouges = zone de vente) et 3 en dessous (bandes vertes = zone d'achat) ; amplitudes proportionnelles au nombre d'or φ ≈ 1,618 ; prix à l'intérieur des bandes ~90–95 % du temps (claim écosystème, non audité). **Formule officielle jamais divulguée.**  
Indicateur **repeignant** (recalcule le passé) — confirmé par ProRealCode.

**[RECONSTRUCTION]** :
```
Sur N = 250 barres (x = 1..N, y = clôtures) :
ŷ(x) = a₀ + a₁x + a₂x² (+ a₃x³)        ← moindres carrés, degré 2–3
σ = std(y − ŷ)                           ← écart-type des résidus
Bandes : ŷ ± k·σ, k ∈ {1.618 ; 2.618 ; 4.236}
TRADEX : mode « endpoint figé » obligatoire (on ne conserve que la valeur à la
dernière barre clôturée) → supprime le repaint, rend le backtest honnête.
```

> **Source de données TRADEX [VERROUILLÉ C5]** : les valeurs COG, bandes et Timing sont lues depuis les fichiers JSON produits par NinjaTrader 8. Aucun screenshot, aucune capture d'écran, aucune Vision IA. Si un champ JSON est absent ou périmé → `NON_DÉTECTÉ` → NON-TRADE automatique.

### Pilier 2 — Belkhayate Timing (COG statique)
**[DOCUMENTÉ]** : oscillateur sous le graphique, échelle ±10 (ou 0–100) ; zone centrale neutre (50/50, interdiction d'entrer), zones extrêmes rouge/verte (signal possible), zones d'alerte au-delà (probabilité supérieure). **Entrée valide : Timing entre 4 et 8 (vente) ou −4 et −8 (achat).**  
**[RECONSTRUCTION]** (ports LazyBear/MBFX) : normalisation du prix médian (H+L)/2 par rapport au range des N dernières barres, projetée sur ±10 — analogue à un stochastique non lissé.

### Pilier 3 — Momentum / Énergie (Belkhayate Cycle)
**[NON DOCUMENTÉ]** en formule. **[AMÉLIORATION PROPOSÉE]** — proxy TRADEX assumé :
```
Energie = (Volume_barre / MoyVolume_20) × (ATR_14 / MedianeATR_100)
Lecture : ≥ 1,2 = mouvement « nourri » ; < 0,8 = mouvement anémique (méfiance).
```

## 1.2 Règles d'entrée / sortie / invalidation
**[DOCUMENTÉ]** (R1–R7) puis **[AMÉLIORATION PROPOSÉE]** (R8–R10) :

| # | Règle | Type |
|---|---|---|
| R1 | Jamais d'achat si COG rouge ; jamais de vente si COG bleu | DOCUMENTÉ |
| R2 | Achat : prix dans bandes vertes ; Vente : prix dans bandes rouges | DOCUMENTÉ |
| R3 | Confluence : bande extrême touchée **ET** Timing dans [4;8] / [−8;−4] | DOCUMENTÉ |
| R4 | Privilégier bandes resserrées (volatilité comprimée) | DOCUMENTÉ |
| R5 | TP1 = ligne COG ; TP2 = bandes opposées si sens de la tendance | DOCUMENTÉ |
| R6 | SL au-delà de la 3e bande | DOCUMENTÉ |
| R7 | Trader dans le sens du COG | DOCUMENTÉ |
| R8 | **Invalidation** : COG change de couleur avant TP1 → sortie immédiate au marché | AMÉLIORATION |
| R9 | **Invalidation** : clôture de barre AU-DELÀ de la 3e bande = échec du mean reversion → sortie, pas de moyenne à la baisse | AMÉLIORATION |
| R10 | **Invalidation** : news majeure imprévue sur le marché tradé → fermeture ou réduction immédiate | AMÉLIORATION |

## 1.3 Classification des actifs TRADEX [VERROUILLÉ CLAUDE.md]

> ⚠️ La version 1.0 référençait la « matrice 8 marchés Ortogonex » (GC, CL, 6E, ZN, ES, HG, BTC, 6J). Cette liste est **incompatible avec CLAUDE.md**. La classification TRADEX ci-dessous s'y substitue définitivement.

### Catégorie 1 — TRADING (ordres possibles)
| Code | Actif | Bourse |
|------|-------|--------|
| GC | Or | CME |
| HG | Cuivre | CME |
| CL | Pétrole WTI | CME |
| ZW | Blé | CBOT |

### Catégorie 2 — CONFIRMATION (analyse uniquement — zéro ordre)
| Code | Actif | Rôle |
|------|-------|------|
| DX | Dollar Index | Macro — proxy via DXY Alpha Vantage |
| ES | S&P 500 | Confirmation marchés risqués |
| VX | VIX | Sentiment / peur |

### Catégorie 3 — RÉFÉRENCE inter-marché (corrélations — zéro ordre)
| Code | Actif | Rôle |
|------|-------|------|
| MBT | Bitcoin Micro | Référence crypto inter-marché |
| 6J | Yen Japonais | Référence devise refuge |

**Règle absolue** : MBT et 6J n'apparaissent JAMAIS dans les actifs tradables. Aucun ordre, aucune position, jamais.

> **Actifs absents du référentiel TRADEX** : EUR/USD (6E) et T-Notes 10 ans (ZN) sont présents dans la matrice Ortogonex originale mais ne font partie d'aucune catégorie TRADEX. Ils ne sont pas tradés, pas analysés comme signaux, et peuvent éventuellement servir de contexte macro informel non scoré.

---

# PARTIE 2 — AMÉLIORATIONS EXHAUSTIVES PAR COUCHE
*(Toute la partie = [AMÉLIORATION PROPOSÉE] ; les seuils chiffrés = [HYPOTHÈSE TESTABLE].)*

## Couche 1 — Confirmation
| Filtre | Règle de départ | Rejet du signal si |
|---|---|---|
| Volume | Volume barre signal vs moyenne 20 | < 1,0 × moyenne (touche « vide ») |
| Structure | Pas de cassure d'un swing majeur opposé dans les 20 dernières barres | Cassure récente contre le trade |
| Volatilité | ATR(14) vs médiane ATR(100) | ATR > 2 × médiane (marché en choc) |

## Couche 2 — Multi-timeframe (HTF/LTF)
- **Biais HTF** : COG H4 (couleur + position du prix vs centre) — lu depuis JSON NT8.
- **Signal LTF** : setup complet R1–R7 sur H1 (ou M15 pour scalp) — lu depuis JSON NT8.
- Règle : signal LTF **contre** le biais H4 = NON-TRADE (réduit les faux signaux contre-tendance, le défaut n°1 du mean reversion).

## Couche 3 — Optimisation de l'entrée par retracement
Au lieu d'entrer au premier contact de la bande 2 :
1. Attendre la **clôture de barre** dans la zone (anti-mèche).
2. Entrée en **limit** sur retracement de 38,2–50 % de la barre de signal, ou sur retest de la bande.
3. Si pas exécuté en 3 barres → signal expiré (pas de chasse).

Effet : améliore le prix moyen d'entrée → rend le R/R 1:2 atteignable (voir Couche 4).

## Couche 4 — Risque : position sizing dynamique + R/R ≥ 1:2
- **Risque par trade** : 1 % du capital (max 2 %).
  `Contrats = floor( (Capital × 1 %) / (Distance_SL_ticks × Valeur_tick) )` ; si résultat = 0 → utiliser le **micro-contrat** ou NON-TRADE.
- **Ajustement volatilité** : si ATR > 1,5 × médiane → risque réduit à 0,5 %.
- **Tension documentée et résolue** : la sortie originale TP1 = COG donne souvent ~1:1 à 1:1,5. Pour exiger **R/R ≥ 1:2** : (a) entrée améliorée par retracement (Couche 3), et/ou (b) entrée uniquement sur la **bande 3** (extrême), et/ou (c) sorties partielles (Couche 5) avec TP2 = bandes opposées. Si la géométrie du setup ne donne pas 1:2 → **NON-TRADE**.

## Couche 5 — Sorties : trailing adaptatif + partielles
- **50 % de la position à TP1 (ligne COG)** → SL du reste déplacé au break-even.
- **Reste** : trailing stop = `max(SL_initial, prix − 2 × ATR_14)` (achat ; symétrique vente), objectif TP2 = première bande opposée.
- Sortie temps : position non gagnante après 24 barres LTF → clôture (le mean reversion a échoué « en silence »).

## Couche 6 — Contexte macro [CORRIGÉ C6 + C8]
- **Sessions** : trader chaque actif TRADING sur sa session liquide (tableau Partie 3) ; éviter les rollovers de contrats et les veilles de jours fériés US.
- **News Gate [CORRIGÉ C6]** : blocage **30 min AVANT** NFP, CPI, FOMC (timezone ET explicite) et **15 min APRÈS** la publication. Le module news TRADEX (Claude) score l'impact −100/+100 ; |score| > 60 = NON-TRADE sur les actifs affectés.
- **Corrélations inter-marché [CORRIGÉ C8]** — logique TRADEX 4+3+2 :
  - **DX fort (haussier)** → pression baissière sur GC, HG, CL, ZW.
  - **ES baissier** → signal d'alerte sur GC (refuge) et CL (demande).
  - **VX (VIX) > seuil critique** → mode AUTO suspendu ; mode Manuel : signal affiché uniquement (décision Abdelkrim).
  - **MBT et 6J** : utilisés uniquement pour lire le régime risk-on / risk-off — jamais comme base d'ordre.
  - **Règle biais inter-marché [CORRIGÉ C8]** : si les **3 actifs CONFIRMATION (DX, ES, VX) donnent un biais global opposé** au trade envisagé → signal pénalisé (−1,0 pt au score) ou NON-TRADE si score < seuil après pénalité.

---

# PARTIE 3 — APPLICATION SUR LES ACTIFS TRADEX

> Spécifications de contrats CME = ordres de grandeur standard **à vérifier sur cmegroup.com avant tout trade**. Paramètres COG/Timing = **[HYPOTHÈSE TESTABLE]**, point de départ du backtest. Micro-contrats recommandés pour un compte < 25 k$.

## Catégorie TRADING — Actifs avec ordres possibles

| Actif | Contrat (micro) | Tick ≈ valeur | Session clé | Profil | Rôle inter-marché |
|---|---|---|---|---|---|
| Or | GC (MGC) | 0,10 = 10 $ (1 $) | Londres + NY 14h30–17h ET | Mean reversion correct hors chocs géopolitiques | Anti-dollar, refuge |
| Cuivre | HG (MHG) | 0,0005 = 12,50 $ | Londres + NY matin | Sensible Chine ; tendances longues | Baromètre croissance |
| Pétrole WTI | CL (MCL) | 0,01 = 10 $ (1 $) | NY 15h30–20h30 ET ; stocks mercredi 16h30 | Très nerveux, gaps news | Inflation, géopolitique |
| Blé | ZW (MZW) | 0,25 = 12,50 $ | CBOT 10h30–14h15 CT | Saisonnier, sensible USDA | Matière première agricole |

**Paramètres de départ [HYPOTHÈSE TESTABLE]** : COG N=250, degré 3, bandes k={1.618; 2.618; 4.236} ; Timing n=50.  
Ajustements à tester : CL → entrée seulement bande 3 + risque 0,5 % (volatilité élevée) ; ZW → filtre volume renforcé (liquidité plus faible que GC/CL).

## Catégorie CONFIRMATION — Lecture uniquement (zéro ordre)

| Actif | Code | Lecture | Rôle dans le signal |
|---|---|---|---|
| Dollar Index | DX | JSON / Alpha Vantage DXY | Biais macro — DX fort = pression sur GC, HG, CL, ZW |
| S&P 500 | ES | JSON NT8 | Risk-on/off — ES haussier = contexte favorable CL/HG |
| VIX | VX | JSON NT8 | Seuil critique → suspension mode AUTO |

## Catégorie RÉFÉRENCE — Corrélation uniquement (zéro ordre, jamais)

| Actif | Code | Rôle | Règle absolue |
|---|---|---|---|
| Bitcoin Micro | MBT | Signal risk-on spéculatif | **AUCUN ORDRE — JAMAIS** |
| Yen Japonais | 6J | Signal refuge / risk-off | **AUCUN ORDRE — JAMAIS** |

**Setup type (exemple pédagogique, Or MGC H1)** : COG bleu (JSON NT8), prix touche bande verte 2 avec clôture dedans, Timing −5,8 (JSON NT8), volume 1,3×, biais H4 haussier (JSON NT8), news calmes (30 min après dernier NFP), DX faible + ES neutre + VX < seuil. Pré-condition 3/4 validée (GC + HG + CL alignés haussier = 3/4 ✅, DX + ES alignés = 2/3 ✅). Entrée limit 38 % de retracement 2 408 $, SL sous bande 3 à 2 399 $ (9 $), TP1 = COG 2 421 $ (50 %), TP2 = bande rouge 1 à 2 430 $ → R/R global ≈ 1:2. Invalidation : COG vire rouge (JSON NT8) ou clôture < 2 399 $.

---

# PARTIE 4 — SYSTÈME DE DÉCISION TRADEX (ÉTAPE 0 + SCORE 0–10)

**[AMÉLIORATION PROPOSÉE]** — logique **entièrement déterministe** (calculée par le code TRADEX depuis les JSON NT8 ; Claude fournit uniquement l'analyse KB ; `NON_DÉTECTÉ` si champ JSON absent = NON-TRADE automatique).

## Étape 0 — Pré-condition éliminatoire [AJOUTÉ C7 — VERROUILLÉ CLAUDE.md]

> **Cette étape est vérifiée AVANT tout calcul de score. Si elle échoue, le score n'est pas calculé.**

| Condition | Vérification | Résultat si KO |
|---|---|---|
| **3/4 actifs TRADING alignés** | GC, HG, CL, ZW : au moins 3 COG de même couleur | NON-TRADE — stop |
| **2/3 actifs CONFIRMATION alignés** | DX, ES, VX : au moins 2 dans le même sens que le trade | NON-TRADE — stop |

Exemple : trade ACHAT GC — il faut que ≥ 3 parmi {GC, HG, CL, ZW} soient haussiers (COG bleu) ET que ≥ 2 parmi {DX faible, ES haussier, VX < seuil} soient favorables à l'achat.

## Score 0–10 (calculé uniquement si Étape 0 validée)

**[AMÉLIORATION PROPOSÉE]** — grille **déterministe** :

| Critère | Points |
|---|---|
| COG : couleur alignée au sens du trade (R1) | **Éliminatoire** (score = 0 si non) |
| Prix en zone de bande 2 ou 3 avec clôture dedans (R2) | 2,0 |
| Timing dans [4;8] / [−8;−4] (R3) | 2,0 |
| Bandes resserrées (largeur < médiane 100 barres) (R4) | 1,0 |
| Biais H4 aligné (Couche 2) | 1,5 |
| Volume ≥ 1,2× moyenne 20 (Couche 1) | 1,0 |
| ATR normal (pas de choc) (Couche 1) | 0,5 |
| Structure non cassée contre le trade (Couche 1) | 0,5 |
| Biais CONFIRMATION favorable ou neutre (DX/ES/VX) (Couche 6) | 1,0 |
| News : aucun événement ±30 min avant / 15 min après, \|score news\| ≤ 60 | 0,5 |
| **Total** | **10,0** |

**Seuils [HYPOTHÈSE TESTABLE]** :
- **Score ≥ 7,0 ET aucun critère éliminatoire ET R/R ≥ 1:2** → signal proposé (validation humaine obligatoire en mode Manuel).
- 5,0–6,9 → « setup à surveiller », pas de trade.
- < 5,0 → ignoré.

**Cas de NON-TRADE absolus** (même à score 10) :
1. Étape 0 non validée (3/4 + 2/3 non atteint).
2. Un champ JSON NT8 renvoyé `NON_DÉTECTÉ` ou périmé (staleness monitor BLOQUÉ).
3. R/R < 1:2 sur la géométrie du setup.
4. Taille de position calculée = 0 contrat (risque 1 % impossible) sans micro disponible.
5. Fenêtre news : dans les 30 min avant NFP/CPI/FOMC ou 15 min après.
6. VX (VIX) > seuil critique → mode AUTO suspendu.
7. 2 pertes consécutives dans la journée → arrêt (anti revenge-trading).
8. Budget API mensuel TRADEX dépassé → système en pause (garde-fou).
9. Circuit breaker actif (timeout NT8 → fallback ATTENDRE).

---

# PARTIE 5 — PERFORMANCE ET LIMITES HONNÊTES

## 5.1 État réel des métriques
| Métrique | Statut |
|---|---|
| Win Rate audité de la méthode | **NON DOCUMENTÉ** — le « >80 % » circule uniquement sur des sites vendeurs, invérifiable |
| Profit Factor / Drawdown max | **NON DOCUMENTÉ** — aucun audit indépendant n'existe |
| Championnat 1999 (+400 %) | DOCUMENTÉ comme revendication (presse + site officiel), trades non publics |
| Mansa Moussa (« 3–4 %/mois ») | Revendication auto-déclarée, incohérente entre sources, sans prospectus public |
| Test public Ortogonex 8 marchés | DOCUMENTÉ : **1 signal gagnant sur 8** (~12,5 %) |

**Conséquence** : la SEULE source future de Win Rate/PF/DD fiable est **ton propre backtest**, protocole :
1. Indicateurs en mode **non-repaint** (endpoint figé) — sinon résultats invalides.
2. **Walk-forward** : optimisation 2 ans / validation 6 mois, glissant, par marché.
3. Coûts inclus (commissions + slippage 1 tick).
4. Rejet si PF hors-échantillon < 1,1 ou drawdown > 15 % sur le marché testé.
5. Ensuite **paper trading 30 jours** via TRADEX avant tout argent réel.

## 5.2 Conditions favorables vs défavorables *(hypothèse raisonnée)*
✅ Ranges larges et liquides (GC, HG hors crise Chine) · volatilité stable · bandes resserrées puis touche extrême confirmée · 3 actifs TRADING + 2 actifs CONFIRMATION alignés.  
❌ Tendances fortes mono-directionnelles (HG cycles Chine longs, CL choc géopolitique) : le prix « colle » à la bande, séries de pertes · chocs news (CL stocks mercredi, FOMC) · faible liquidité ZW (hors session CBOT) · pré-condition Étape 0 non atteinte (marché en désaccord).

## 5.3 Limites et risques réels
1. **Repaint** de l'indicateur original : toute démonstration historique « propre » est trompeuse ; TRADEX impose l'endpoint figé (valeur dernière barre clôturée uniquement).
2. **Formule propriétaire jamais publiée** : tout est reconstruction ; fidélité non garantie.
3. **Aucune validation indépendante** ; le seul test public multi-marchés connu est défavorable.
4. Contre-tendance par nature : sans les couches 1–2, séries de pertes en tendance.
5. Paramètres (250, φ) non justifiés théoriquement : conventions, pas mathématiques démontrées.
6. **Source des données TRADEX [VERROUILLÉ C5]** : toutes les lectures (COG, Timing, prix, volume) viennent des fichiers JSON produits par NinjaTrader 8. Si un champ est absent → `NON_DÉTECTÉ` → NON-TRADE. Jamais de lecture par screenshot ou Vision IA.

## 5.4 ⚠️ Disclaimer
> Le trading de futures, devises et crypto comporte un **risque élevé de perte pouvant excéder le capital déposé**. **Les performances passées ne préjugent pas des performances futures.** Cette stratégie est une étude à usage strictement privé, non auditée, fondée en partie sur des reconstructions d'indicateurs non publiés ; elle ne constitue pas un conseil en investissement. TRADEX est une aide à la décision : **validation humaine, stop-loss et risque ≤ 1–2 % par trade obligatoires**. Tous les seuils chiffrés sont des hypothèses à backtester avant tout usage réel.

---

## Sources principales
Admiral Markets (COG : 250 périodes, 3σ, φ, formule non divulguée) · Blog officiel Belkhayate (règles Barycentre/Timing) · ProRealCode (repaint confirmé ; MBFX Timing) · TradingView LazyBear (port Timing) · IQ Option (zones, règle 4–8) · Forex-Station/ForexProfitWay (usage système — sites vendeurs, claims non audités) · Stradoji (exposé repaint/origine TradeStation) · TradingSat/BFM (bio, 1999, Mansa Moussa) · CME Group (specs contrats — à vérifier avant trade) · **CLAUDE.md TRADEX-AI (classification actifs, règles architecture, garde-fous — source de vérité absolue)**.

---

## Récapitulatif des corrections v1.0 → v2.0

| # | Correction | Avant (v1.0) | Après (v2.0) | Ref. CLAUDE.md |
|---|---|---|---|---|
| C1 | BTC et Yen | Listés comme tradables | RÉFÉRENCE — zéro ordre | Règle absolue |
| C2 | EUR/USD (6E) | Actif tradable | Supprimé du référentiel TRADEX | Absent de CLAUDE.md |
| C2 | T-Notes (ZN) | Actif tradable | Supprimé du référentiel TRADEX | Absent de CLAUDE.md |
| C3 | Blé (ZW) | Absent | Actif TRADING ajouté | TRADING verrouillé |
| C4 | DX + VX | Absents | Actifs CONFIRMATION ajoutés | CONFIRMATION verrouillé |
| C5 | Architecture données | "vision IA / screenshot" | JSON NT8 uniquement | Décision C2 verrouillée |
| C6 | News Gate | ±15 min | 30 min avant / 15 min après | Sécurité obligatoire |
| C7 | Règle d'entrée | Absente du scoring | Étape 0 éliminatoire avant score | Règle d'entrée verrouillée |
| C8 | Règle intermarché | "5/8 marchés Ortogonex" | "3 actifs CONFIRMATION alignés" | Classification 4+3+2 |

*Version 2.0 — Alignée CLAUDE.md du 11/06/2026 — Généré le 13/06/2026*
