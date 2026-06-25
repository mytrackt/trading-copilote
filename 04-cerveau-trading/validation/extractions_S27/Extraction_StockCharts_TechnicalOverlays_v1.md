# Extraction StockCharts — Technical Overlays
**Source :** `bundles/stockcharts/technical_overlays.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle (page index) · 0/0 certifiées · 0 à vérifier
**Décisions :** D4411 → D4430 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Catalogue des overlays prix — outils directement superposés au prix de GC/HG/CL/ZW pour niveaux clés, tendance, stops et canaux.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D4411 — Bollinger Bands
🔵 **ÉCOLE** (Source : technical_overlays.md) : Les Bollinger Bands tracent des bandes au-dessus et en dessous d'une MA centrale, basées sur l'écart-type des prix. Elles définissent les limites « normales » du mouvement prix — prix en dehors des bandes = condition exceptionnelle.
**TRADEX-AI C1** : Les Bollinger Bands sont applicables à GC/HG/CL/ZW pour identifier les compressions (faible volatilité avant breakout) et les extensions (surachat/survente) ; une sortie de bande en direction de la tendance Belkhayate renforce la conviction du signal.
*Catégorie : indicateurs_tendance*

### D4412 — Ichimoku Cloud
🔵 **ÉCOLE** (Source : technical_overlays.md) : L'Ichimoku Cloud est un overlay complet définissant support/résistance, direction de tendance, momentum, et signaux de trading — composé de Tenkan-sen, Kijun-sen, Senkou Span A/B (le nuage), Chikou Span.
**TRADEX-AI C1** : L'Ichimoku est pertinent comme confirmation C1 pour GC/HG/CL/ZW — prix au-dessus du nuage = tendance haussière ; signal d'entrée renforcé quand il est aligné avec la Direction Belkhayate et le BGC.
*Catégorie : indicateurs_tendance*

### D4413 — Moving Averages (SMA et EMA)
🔵 **ÉCOLE** (Source : technical_overlays.md) : Les moyennes mobiles simples (SMA) et exponentielles (EMA) lissent les données de prix pour montrer la valeur « moyenne » dans le temps. Les SMA pondèrent uniformément ; les EMA pondèrent davantage les prix récents.
**TRADEX-AI C1** : Les MAs sont les overlays de base du Cercle C1 — les croisements MA court/long terme sur GC (ex. MA 20/50) servent de premier filtre de tendance avant analyse Belkhayate. Déjà intégrées dans la KB mais ce catalogue confirme leur rôle central.
*Catégorie : indicateurs_tendance*

### D4414 — Parabolic SAR
🔵 **ÉCOLE** (Source : technical_overlays.md) : Le Parabolic SAR (Stop And Reverse) place des points en dessous des prix en tendance haussière et au-dessus en tendance baissière — indique des points de retournement potentiels et fournit des niveaux de stop dynamiques.
**TRADEX-AI C1** : Le Parabolic SAR fournit des stops dynamiques automatiques applicables à GC/HG/CL/ZW — une inversion SAR confirme un changement de tendance et peut déclencher la condition de sortie ou blocage signal.
*Catégorie : gestion_position_active*

### D4415 — Pivot Points
🔵 **ÉCOLE** (Source : technical_overlays.md) : Les Pivot Points sont un overlay qui montre les points de retournement en dessous des prix en tendance haussière et au-dessus en tendance baissière — calculés à partir du H/L/C de la session précédente.
**TRADEX-AI C1** : Les Pivots Points sont directement liés aux « Pivots » du Cercle C1 Belkhayate — TRADEX-AI utilise des pivots NT8 ; ce module StockCharts confirme la méthodologie standard (H+L+C/3 pour le pivot central, R1/R2/S1/S2).
*Catégorie : structure_marche*

### D4416 — Keltner Channels
🔵 **ÉCOLE** (Source : technical_overlays.md) : Les Keltner Channels tracent des bandes au-dessus et en dessous d'une MA basées sur l'Average True Range (ATR) — similaires aux Bollinger Bands mais fondés sur la volatilité ATR plutôt que l'écart-type.
**TRADEX-AI C1** : Les Keltner Channels combinés aux Bollinger Bands forment la base du TTM Squeeze (C5) ; sur GC/HG/CL une compression Bollinger dans les Keltner précède souvent un mouvement directionnel exploitable par TRADEX.
*Catégorie : indicateurs_tendance*

### D4417 — Chandelier Exit
🔵 **ÉCOLE** (Source : technical_overlays.md) : Le Chandelier Exit est un indicateur de stop trailing — place le stop à N×ATR en dessous du plus haut récent (pour long) ou N×ATR au-dessus du plus bas récent (pour short), s'adaptant dynamiquement à la volatilité.
**TRADEX-AI C1** : Méthodologie de stop dynamique directement applicable aux positions TRADEX-AI sur GC/HG/CL/ZW — le Chandelier Exit basé sur ATR est cohérent avec la gestion de risque adaptative requise par les garde-fous.
*Catégorie : gestion_position_active*

### D4418 — Volume By Price (VBP)
🔵 **ÉCOLE** (Source : technical_overlays.md) : Volume By Price affiche un histogramme horizontal montrant le volume échangé à chaque niveau de prix — révèle les zones de fort volume (zones de valeur/Value Area) et les zones de faible volume (nœuds de faible résistance).
**TRADEX-AI C2** : Le VBP est un outil d'Order Flow (C2) complémentaire au Market Profile / Volume Profile déjà dans la KB — les High Volume Nodes sur GC/CL identifient des zones de support/résistance institutionnel fiables.
*Catégorie : volume_liquidite*

### D4419 — Anchored VWAP et VWAP
🔵 **ÉCOLE** (Source : technical_overlays.md) : Le VWAP (Volume-Weighted Average Price) est un indicateur intraday basé sur la valeur totale échangée divisée par le volume total — représente le prix moyen payé dans la journée. L'Anchored VWAP permet de définir manuellement le point de départ du calcul.
**TRADEX-AI C2** : Le VWAP est une référence institutionnelle majeure pour le Cercle C2 — les institutions traquent le VWAP ; un prix sous le VWAP en intraday sur GC/CL indique une pression vendeuse institutionnelle à intégrer dans l'analyse Order Flow.
*Catégorie : volume_liquidite*

### D4420 — Moving Average Envelopes et Price Channels
🔵 **ÉCOLE** (Source : technical_overlays.md) : Moving Average Envelopes = canal formé par des SMAs décalées d'un pourcentage fixe au-dessus/dessous. Price Channels = canal formé par le plus haut et le plus bas sur N périodes (Donchian Channels).
**TRADEX-AI C1** : Les Price Channels (Donchian) sont pertinents pour la détection de breakout sur GC/HG/CL/ZW — un cassure du canal des N dernières barres confirme une nouvelle tendance ; les envelopes servent de zones de retour à la moyenne.
*Catégorie : structure_marche*

### D4421 — ZigZag
🔵 **ÉCOLE** (Source : technical_overlays.md) : Le ZigZag filtre les mouvements de prix inférieurs à un pourcentage donné et ne trace que les mouvements significatifs — utile pour identifier les swings majeurs, les configurations de prix et les retracements Fibonacci.
**TRADEX-AI C1** : Le ZigZag est un outil d'identification des swings Belkhayate — il permet de tracer automatiquement les hauts/bas majeurs sur GC/HG/CL/ZW pour mesurer les retracements et projeter les extensions avec les niveaux Fibonacci.
*Catégorie : structure_marche*
