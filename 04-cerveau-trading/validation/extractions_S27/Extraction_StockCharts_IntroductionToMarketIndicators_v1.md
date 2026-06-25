# Extraction StockCharts — Introduction to Market Indicators
**Source :** `bundles/stockcharts/introduction_to_market_indicators.md` (HTTP 200 · ~5 425 car.) + 0 image certifiée
**Méthode images :** double ancrage · 0/0 certifiées (intégrité .md=0 figures vs HTML=0 images)
**Décisions :** D2271 → D2276 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/introduction-to-market-indicators
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (la page ne contient aucune figure ; manifest : .md=0 figures vs HTML=0 images, alignement non applicable).

## DÉCISIONS

### D2271 — Définition d'un Market Indicator
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : « Market Indicators are used to measure the health of a group of related stocks, usually by measuring group participation in a trend. » Le groupe peut être les membres d'un indice large, d'un secteur spécifique, ou d'un marché entier.
**TRADEX-AI C7** : Notion de participation de groupe — pertinente pour la confirmation marchés (ES) et la matrice de corrélations, pas pour un actif isolé.
*Catégorie : indicateurs_tendance*
🔵 ÉCOLE
---

### D2272 — Market Indicator vs Technical Indicator (formule multi-titres)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : Comme un indicateur technique, un market indicator est une série de points dérivés d'une formule ; mais la formule est appliquée aux données de prix de **plusieurs** titres du marché, et non d'un seul. Les données peuvent venir de l'open/high/low/close, du volume, ou des deux.
**TRADEX-AI C7** : Distinction clé — un market indicator agrège plusieurs titres ; il alimente le cercle confirmation/corrélations, pas l'analyse mono-actif (GC/HG/CL/ZW).
*Catégorie : indicateurs_tendance*
---

### D2273 — Les market indicators ont leurs propres tickers
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : Contrairement aux indicateurs techniques, les market indicators ne sont pas tracés au-dessus/dessous d'un graphique : ils SONT ce qui est tracé et ont leurs propres symboles. Ex. $BPSPX et $BPNDX suivent le Bullish Percent Index pour le S&P 500 et le NASDAQ 100 respectivement.
**TRADEX-AI C7** : Implication d'ingestion — un market indicator est une série autonome (ticker dédié) à collecter séparément des flux NT8 par actif.
*Catégorie : indicateurs_tendance*
---

### D2274 — Market Breadth Indicators (participation)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : Les breadth indicators mesurent le nombre/pourcentage de titres participant à une tendance, à partir des données de prix. Ex. l'Advance-Decline Line = nombre d'« advancers » vs « decliners » ; le Net New 52-Week Highs = différence entre % de titres à nouveaux plus-hauts 52 sem. et à nouveaux plus-bas. Indicateurs populaires : Advance-Decline Line, McClellan Oscillator, Net New 52-Week Highs.
**TRADEX-AI C7** : Mesure de la largeur de marché — proxy de confirmation de tendance globale (rôle ES/marchés), non un signal d'entrée sur actif tradable.
*Catégorie : indicateurs_tendance*
---

### D2275 — Sentiment Indicators (mesure du ressenti investisseur)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : « Sentiment Indicators measure whether investors feel bullish or bearish about the market. » Données plus variées que les breadth indicators : souvent un comptage des investisseurs eux-mêmes ou le volume d'argent investi plutôt que prix/volume. Ex. DecisionPoint Rydex Ratio (argent en fonds haussiers/baissiers) ; AAII basé sur sondages.
**TRADEX-AI C5** : Rattachement direct au cercle Sentiment — cadre conceptuel des indicateurs de sentiment (cf. VIX, Put/Call déjà au périmètre).
*Catégorie : indicateurs_momentum*
---

### D2276 — Indicateurs de sentiment populaires (Put/Call, Volatility, Rydex)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_market_indicators.md) : Indicateurs de sentiment populaires cités : Put Call Ratio, Volatility Indices, DecisionPoint Rydex Ratio.
**TRADEX-AI C5** : Le Put/Call Ratio et les Volatility Indices recoupent le périmètre TRADEX-AI (VIX = VX en CONFIRMATION, Put/Call listé en C5) — confirme la pertinence de ces sources de sentiment.
*Catégorie : indicateurs_momentum*
---

## SYNTHÈSE

| Plage | Décisions | Images | Catégories dominantes | Tags |
|-------|-----------|--------|-----------------------|------|
| D2271–D2276 | 6 | 0/0 (aucune figure) | indicateurs_tendance, indicateurs_momentum | 🟢 ×6 · 🔵 ×1 (D2271) |

**Cercles principaux :** C7 (corrélations / breadth de marché) et C5 (sentiment). Page d'introduction courte (~5 425 car.) : extraction des définitions clés, NON paddée (6 décisions sur 20 réservées D2271–D2290).
**Lien Belkhayate :** NON CONCERNÉ (indicateurs de marché agrégés, hors méthode Belkhayate mono-actif). Pertinence indirecte pour les cercles CONFIRMATION (ES) et SENTIMENT (VIX/Put-Call).
**Cas à vérifier :** Le manifest marque la page « (A VERIFIER) » uniquement sur l'intégrité images (.md=0 vs HTML=0 → aucune image, alignement non applicable, pas d'anomalie réelle). Aucune image à certifier ; aucune décision dépendante d'image. Aucun cas de contenu à vérifier.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
