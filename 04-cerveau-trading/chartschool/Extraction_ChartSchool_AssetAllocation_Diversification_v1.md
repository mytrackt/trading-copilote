# Extraction KB — ChartSchool : Asset Allocation & Diversification
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/asset-allocation-and-diversification  
**Version :** v1 enrichie (texte + descriptions visuelles 6 charts)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS ANTI-HALLUCINATION

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart ou la source officielle lue |
| 🟡 | Interprétation plausible basée sur observation visuelle, non certaine |
| 🔵 | Règle générale citée par auteur reconnu |
| ⏳ | À vérifier dans une autre source avant usage en signal |
| 🔴 | Affirmation risquée ou non prouvée |
| ⚫ | Non auditable |

---

## 1. POSITIONNEMENT KB TRADEX

🔵 Cette page couvre la gestion de portefeuille (allocation, diversification, corrélations inter-actifs). Pour TRADEX, la valeur principale est : **comprendre les corrélations entre actifs** — notamment Or/Dollar, indices US/EAFE — pour contextualiser les signaux Belkhayate sur les futures.

---

## 2. ALLOCATION D'ACTIFS — CADRE GÉNÉRAL

### 2.1 Allocation typique d'un portefeuille d'investissement

🟢 **Diagramme camembert gauche — "Example Asset Allocation of a Typical Investment Portfolio" :**

| Classe d'actif | Part estimée |
|----------------|-------------|
| Stocks (actions) | ~40% (bleu, part dominante) |
| Bonds (obligations) | ~30% (orange) |
| Cash (liquidités) | ~15% (jaune) |
| Cmdty (matières premières) | ~15% (gris) |

🔵 **Principe :** diversifier entre classes d'actifs non corrélées réduit le risque global sans sacrifier autant de rendement.

### 2.2 Diversification interne à l'allocation actions

🟢 **Diagramme camembert droit — "Diversification within the Stock Allocation" :**

| Sous-catégorie | Part estimée |
|---------------|-------------|
| Large Cap | ~40% (bleu) |
| Mid Cap | ~25% (orange) |
| Small Cap | ~10% (gris) |
| Int'l (international développé) | ~10% (jaune) |
| Emrg Mkts (marchés émergents) | ~15% (bleu foncé) |

🔵 **Règle de diversification intra-actions :** même dans une classe d'actif unique, diversifier par capitalisation et géographie réduit la volatilité du portefeuille.

---

## 3. FORMES HISTORIQUES DE DIVERSIFICATION

🟢 **Diagramme camembert — "Early Forms of Diversification" :**

| Tiers | Description |
|-------|-------------|
| Real Estate (immobilier) | ~33% — actif physique, inflation-hedge |
| Business (activité commerciale) | ~33% — revenu actif, croissance |
| Reserves (réserves/cash) | ~33% — liquidité, sécurité |

🔵 **Contexte historique :** avant les marchés financiers modernes, la diversification consistait à répartir la richesse entre biens physiques productifs (immobilier, commerce) et réserves liquides. Principes identiques à la gestion moderne, actifs différents.

🟡 **Lien TRADEX :** l'Or (TRADEX cible les gold futures) appartient historiquement à la catégorie "Reserves" — actif de préservation de capital. Ce positionnement influence son comportement (refuge en crise, anti-corrélé aux actions en stress).

---

## 4. CORRÉLATION INTER-MARCHÉS #1 — INDICES INTERNATIONAUX VS SPX

🟢 **Chart $IEE (iShares MSCI EAFE) Weekly + $SPX (fév 2012 → jan 2015) :**

| Indicateur | Valeur | Date |
|------------|--------|------|
| $IEE (rouge) | 60.25 | 13 jan 2015 |
| $SPX (noir + zone verte) | 2034.10 | 13 jan 2015 |
| CORR($IEE,$SPX,20) | **0.10** | Panneau inférieur |

### Observations visuelles :

**2012→mi-2014 :** les deux indices progressent ensemble (corrélation positive), avec $IEE qui suit globalement $SPX avec un léger retard.

**Mi-2014→jan 2015 :** **divergence majeure** — $SPX continue de monter (1900→2034) tandis que $IEE recule de ~67 vers ~60. SPX surperforme nettement les marchés internationaux développés sur cette période.

**Corrélation 0.10 :** proche de zéro = les deux indices sont **quasi-indépendants** à ce moment (jan 2015). Les marchés EAFE (Europe, Australasie, Extrême-Orient) ne suivent plus le SPX.

🔵 **Règle de diversification géographique :** une corrélation basse (< 0.3) entre deux actifs indique qu'ils se comportent différemment → intérêt de les combiner dans un portefeuille. Quand la corrélation monte vers 1.0 (crise), la diversification protège moins.

🟡 **Application TRADEX :** si CORR(NQ,$IEE) < 0.2, un signal long sur NQ ne se confirme pas par les marchés étrangers → signal isolé = confiance réduite. ⏳ À tester empiriquement.

---

## 5. CORRÉLATION INTER-MARCHÉS #2 — OR vs DOLLAR (CRITIQUE TRADEX)

🟢 **Chart $USD Weekly + $GOLD (fév 2012 → jan 2015) :**

| Indicateur | Valeur | Date |
|------------|--------|------|
| $USD (noir) | 92.22 | 12 jan 2015 |
| $GOLD (zone dorée) | 1233.40 | 12 jan 2015 |
| CORR($USD,$GOLD,20) | **-0.37** | Panneau inférieur |

### Chronologie observée :

**Fév→sept 2012 :** Or autour de ~$1600-1700 (sommet zone dorée). Dollar relativement faible (~79-80).

**Oct 2012→juin 2013 :** Or descend de ~$1700 vers ~$1200. Dollar modéré ~80-82.

**Juin 2013→début 2014 :** Or stabilisé ~$1200-1350. Dollar oscille ~79-81.

**Mi-2014→jan 2015 :** **Dollar monte fortement** de ~80 → **92.22** (+15%). **Or baisse** de ~$1350 → **~$1200** (-11%). La relation inverse est clairement visible.

**Corrélation -0.37 :** négative modérée. Pas parfaitement inverse (-1.0) mais **la relation Dollar fort = Or faible est réelle et mesurable**.

🔵 **Règle Or/Dollar fondamentale :** l'Or est libellé en USD. Quand le Dollar monte, l'Or coûte plus cher en devises étrangères → demande étrangère réduite → prix baisse. Relation inverse structurelle, non systématique.

🔵 **Règle de corrélation négative pour la diversification :** deux actifs avec CORR = -0.37 à -0.5 sont d'excellents compléments de portefeuille. Quand l'un baisse, l'autre tend à monter.

🔴 **ATTENTION (critique pour TRADEX) :** la corrélation -0.37 n'est PAS constante. Elle varie dans le temps (visible sur le panneau inférieur : parfois proche de 0, parfois -0.5 à -0.75). **Ne jamais assumer une relation Or/Dollar fixe.** En 2012, des périodes de corrélation positive sont visibles (Or et Dollar montent ensemble).

🟢 **Application TRADEX DIRECTE :** avant tout signal COG Belkhayate sur Gold Futures (GC/MGC) :
1. Vérifier la direction du DXY (Dollar Index)
2. Si Dollar en forte hausse + corrélation Or/Dollar négative active → **filtrer les signaux long sur Or** (vent contraire macro)
3. Si Dollar en baisse → **contexte favorable aux signaux long Or**
4. Intégrer comme filtre dans Couche 1 (ingestion + circuit breaker) ⏳

---

## 6. ROTATION SECTORIELLE — DISPERSION INTRA-S&P 500

🟢 **Chart S&P 500 SPDRs — Performance par secteur (07 juil 2023 → 09 juil 2024, 253 jours) :**

| Secteur | Code couleur | Performance |
|---------|-------------|-------------|
| Technology | Magenta | **+9.39%** 🟢 |
| Comm. Services | Vert | **+6.96%** 🟢 |
| Financials | Bleu clair | **-2.08%** |
| Industrials | Cyan | -12.69% |
| Discretionary | Bleu foncé | -15.43% |
| Energy | Teal | -14.97% |
| Health Care | Orange | -14.33% |
| Materials | Noir | **-18.92%** |
| Utilities | Rouge foncé | **-19.68%** |
| Staples | Violet | **-20.51%** |
| Real Estate | Vert foncé | **-23.24%** 🔴 |

🟢 **Observation clef :** sur cette période de 253 jours, **9 secteurs sur 11 sont négatifs**, mais **Tech +9.39% et Comm. Services +6.96% sont positifs**. L'indice global ($SPX) peut paraître modérément négatif pendant que deux secteurs tirent la croissance.

🔵 **Règle de rotation sectorielle :** même dans un marché globalement baissier, des poches de surperformance existent (ici Tech et Comm. Services). Identifier ces secteurs via Relative Strength permet de rester long sur les actifs forts même en contexte difficile.

🟡 **Application TRADEX :** NQ (Nasdaq Futures, dominé par Tech) aurait surperformé ES (S&P 500) sur cette période → signal de biais long NQ vs short ES en cas d'arbitrage. ⏳ À confirmer sur les données de période correspondante.

---

## 7. CYCLES DE MARCHÉ SUR LONG TERME — SPY MONTHLY + MA(20)

🟢 **Chart SPY (S&P 500 ETF, Monthly, 1996 → fév 2015) :**
- Prix le 4 fév 2015 : 204.87 (High: 205.07, Low: 197.86, Volume: 356.5M)
- MA(20) mensuelle (bleue) : 186.47

### Cycles bull/bear identifiables visuellement :

| Phase | Période | Prix approx. | SPY vs MA(20) |
|-------|---------|-------------|---------------|
| **Bull #1** | 1996 → mars 2000 | ~45 → ~155 | Au-dessus |
| **Bear #1** (dot-com) | Mars 2000 → oct 2002 | ~155 → ~70 | En-dessous |
| **Bull #2** | Oct 2002 → oct 2007 | ~70 → ~155 | Au-dessus |
| **Bear #2** (crise 2008) | Oct 2007 → mars 2009 | ~155 → ~65 | En-dessous |
| **Bull #3** | Mars 2009 → fév 2015 | ~65 → ~205 | Au-dessus |

🟢 **Signal MA(20) mensuelle :** la MA(20) mensuelle (bleu épais) crée des "arches" ou "humps" qui délimitent parfaitement chaque cycle. Quand le prix croise la MA(20) mensuelle à la baisse → bear market. Quand il la croise à la hausse → bull market.

🔵 **Règle MA longue période :** la MA(20) mensuelle est un filtre de tendance primaire (Dow Theory). Ne pas shorter un actif au-dessus de sa MA(20) mensuelle sans raison forte. Ne pas buyer un actif en-dessous sans signal de retournement clair.

🟡 **Application TRADEX :** vérifier la MA(20) mensuelle du sous-jacent avant tout signal Belkhayate. Un signal long alors que le prix est sous la MA(20) mensuelle = **risque aggravé**. Ce filtre s'applique au Gold Monthly et au NQ Monthly. ⏳ À coder dans Couche 1.

---

## 8. RÈGLES GÉNÉRALES DÉDUITES (APPLICABLES TRADEX)

🔵 **R1 — Or/Dollar : relation inverse structurelle mais non constante :** surveiller CORR($USD,$GOLD,20). Si corrélation > 0 (inhabituel) → contexte anormal, prudence accrue sur signaux or.

🔵 **R2 — Ma(20) mensuelle comme filtre de cycle primaire :** signal Belkhayate long sous MA(20) mensuelle = risque aggravé. Réduire la taille de position ou filtrer.

🔵 **R3 — Rotation sectorielle visible sans indicateur complexe :** comparer performance relative des secteurs via RS. Favoriser les trades dans la direction du secteur dominant.

🔵 **R4 — Corrélation inter-marchés varie dans le temps :** une corrélation de 0.10 ou -0.37 sur 20 semaines peut basculer à ±0.75 en quelques semaines. Recalculer régulièrement, ne jamais fixer en dur.

🔵 **R5 — Diversification = corrélation faible, pas absence totale :** des actifs avec CORR 0.1-0.3 se diversifient bien. Des actifs CORR > 0.8 ne se diversifient pas réellement (se comportent comme un seul actif en crise).

🔵 **R6 — Or = actif "Reserves" historique :** comportement refuge attendu en stress de marché. Mais cela casse lors de crise de liquidité extrême (ex: mars 2020, or vendu pour couvrir les marges). ⏳ Circuit breaker TRADEX doit couvrir ces cas.

---

## 9. CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Méthode de calcul de la corrélation (CORR sur StockCharts) → non détaillée ici
⏳ Seuil de corrélation Or/Dollar qui déclenche le filtre TRADEX → à définir empiriquement
⏳ Comportement des corrélations en crise (mars 2020, oct 2008) → à extraire depuis d'autres sources
⏳ Application aux futures spécifiquement (NQ, ES, GC) → général dans cette page

---

*Fin d'extraction — ChartSchool Asset Allocation & Diversification — v1 enrichie visuellement (6 charts)*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
