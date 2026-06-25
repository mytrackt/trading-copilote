# Extraction NinjaTrader — 5 Key Indicators for Day Trading Futures
**Source :** `bundles/ninjatrader/5_key_indicators_for_day_trading_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7551 → D7570 · **Page :** https://ninjatrader.com/futures/blogs/5-key-indicators-for-day-trading-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : 5 indicateurs day trading futures (Pivots, OHLC, Opening Range, VWAP, Volume Profile) — utiles pour C1/C2 dans le moteur Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7551 — Pivot Points : calcul sur H/L/C de la veille
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Le pivot point (PP) est la moyenne du High, Low et Close de la session précédente. Il génère 3 niveaux de résistance (R1, R2, R3) au-dessus et 3 supports (S1, S2, S3) en-dessous, utilisables comme entrées potentielles, cibles de profit ou stops.
**TRADEX-AI C1** : Intégrer les pivots journaliers calculés depuis les données NT8 (H/L/C J-1) dans la grille de niveaux-clés pour GC, CL, ZW, HG.
*Catégorie : structure_marche*

### D7552 — Pivot PP comme filtre de biais directionnel intraday
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Le centre PP permet de déterminer le biais directionnel : prix au-dessus du PP = biais haussier ; prix en-dessous = biais baissier.
**TRADEX-AI C1** : Le biais PP doit être cohérent avec la direction Belkhayate (BGC/COG) pour valider un signal. Un PP contra-directionnel constitue un filtre à appliquer avant l'entrée.
*Catégorie : indicateurs_tendance*

### D7553 — Pivot : concentration d'ordres et consolidation aux niveaux
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Les niveaux pivot attirent des concentrations d'ordres. Les jours de tendance (news), ils agissent comme supports/résistances forts après une cassure franche ; un prix traversant rapidement un pivot indique un fort biais directionnel.
**TRADEX-AI C1** : Une cassure rapide d'un pivot avec volume supérieur à la moyenne est un signal de confirmation de la direction, renforçant la confiance du signal TRADEX.
*Catégorie : structure_marche*

### D7554 — Prior Day OHLC : H/L/C de la veille comme S/R intraday
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Les valeurs H, L, C de la session précédente constituent des supports et résistances significatifs pour la séance suivante. L'alignement de ces niveaux avec d'autres indicateurs renforce leur fiabilité.
**TRADEX-AI C1** : Charger systématiquement les OHLC J-1 depuis les fichiers NT8 et les intégrer à la carte des niveaux-clés pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D7555 — Confluence S/R : alignement de plusieurs indicateurs = niveau plus fort
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Quand un niveau OHLC J-1 coïncide avec un pivot ou un autre indicateur de S/R, la force du niveau est considérée comme supérieure.
**TRADEX-AI C1** : La grille de scoring TRADEX doit attribuer un bonus de confluence quand ≥2 indicateurs de S/R se superposent dans une fenêtre de prix étroite (ex. ±0,5% pour GC).
*Catégorie : structure_marche*

### D7556 — Opening Range : haute/basse des 30-60 premières minutes = S/R journaliers
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : La plage d'ouverture (30, 45 ou 60 min après l'open 9h30 ET) établit des hauts et bas qui servent de S/R pour le reste de la journée. Souvent l'un des deux extrêmes devient le haut ou le bas du jour entier.
**TRADEX-AI C1** : Calculer l'Opening Range automatiquement pour GC/CL/ZW/HG sur les premières 30 min de la session principale et l'inclure dans la grille de niveaux-clés.
*Catégorie : timing*

### D7557 — Opening Range Breakout : cassure ORH/ORL = signal de biais directionnel fort
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Une cassure au-dessus du high de l'Opening Range (ORH) rend peu probable (pas impossible) que le marché aille casser le bas (ORL), et vice versa. Ces cassures peuvent signaler un grand mouvement intraday ; un stop ou trailing stop est nécessaire pour la gestion du risque.
**TRADEX-AI C2** : Une cassure d'Opening Range avec volume élevé renforce le signal directionnel intraday dans la grille de scoring.
*Catégorie : gestion_risque_entree*

### D7558 — VWAP : pondération par volume pour un prix moyen plus représentatif
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Le VWAP donne plus de poids aux transactions volumineuses, produisant un prix moyen depuis l'ouverture de session. Les traders pros l'utilisent pour mesurer l'efficacité de leurs entrées/sorties : acheter sous VWAP, vendre au-dessus.
**TRADEX-AI C2** : Intégrer le VWAP live (depuis NT8 données) pour qualifier le biais intraday. Prix > VWAP = contexte haussier ; prix < VWAP = contexte baissier. Facteur de pondération dans la grille /10.
*Catégorie : indicateurs_tendance*

### D7559 — VWAP Standard Deviation Bands : S/R dynamiques intraday
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Les bandes à écart-type autour du VWAP créent des niveaux de S/R dynamiques. Quand le volume augmente fortement (news, open session régulière), ces bandes peuvent se déplacer rapidement.
**TRADEX-AI C2** : Les bandes VWAP ±1σ et ±2σ sont des zones cibles de prix pertinentes pour les ordres take-profit ou stop-loss dans les actifs TRADING (GC, CL, HG, ZW).
*Catégorie : structure_marche*

### D7560 — VWAP : indicateur de surachat/survente relatif au prix de la journée
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Prix trop éloigné du VWAP → retour probable vers le VWAP. La pente du VWAP et la distance prix/VWAP façonnent le biais directionnel du trader.
**TRADEX-AI C1** : Un écart prix/VWAP > 1,5σ dans le sens inverse du signal Belkhayate est un avertissement de timing : attendre le pullback vers VWAP avant d'entrer.
*Catégorie : timing*

### D7561 — Volume Profile POC : prix le plus tradé = niveau magnétique
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : Le Point of Control (POC) est le prix où le plus grand volume a été échangé en session. Il agit comme un aimant qui attire les prix. Les autres pics de volume sur l'histogramme servent de cibles de profit ou de stop-loss.
**TRADEX-AI C2** : Le POC de la session doit être intégré comme niveau-clé dans la grille TRADEX. Un signal dont la cible naturelle (TP) coïncide avec le POC est renforcé.
*Catégorie : volume_liquidite*

### D7562 — Volume Profile Value Area : zone d'acceptation de la valeur (±1σ autour du POC)
🟢 **FAIT VÉRIFIÉ** (Source : 5_key_indicators_for_day_trading_futures.md) : La Value Area représente 1 écart-type au-dessus et en-dessous du POC. Elle indique si le prix actuel est trop éloigné de la valeur consensus. Les traders utilisent la Value Area pour détecter des retours vers le juste prix.
**TRADEX-AI C2** : Prix hors Value Area dans le sens contraire du signal = risque de retour vers la Value Area. Intégrer ce facteur dans le scoring de confiance du signal.
*Catégorie : volume_liquidite*

### D7563 — Combinaison multi-indicateurs : filtres + timeframes multiples
🟡 **SYNTHÈSE** (Source : 5_key_indicators_for_day_trading_futures.md) : L'auteur recommande d'utiliser les indicateurs en combinaison (Pivots + OHLC + OR + VWAP + Volume Profile) et d'analyser plusieurs timeframes pour avoir une image complète du marché. Le trading de futures est aussi influencé par des facteurs externes (news, rapports économiques).
**TRADEX-AI C1** : Cette approche multi-couches est cohérente avec les 7 cercles d'intelligence TRADEX. Les 5 indicateurs NT8 couvrent principalement C1 (Prix) et C2 (OrderFlow), à combiner avec C4 (News Gate).
*Catégorie : configuration*

### D7564 — Analyse technique ET fondamentale : nécessité de combiner les deux
🟡 **SYNTHÈSE** (Source : 5_key_indicators_for_day_trading_futures.md) : Un trading efficace sur futures combine l'analyse technique (indicateurs), l'analyse fondamentale (news, rapports gouvernementaux, facteurs économiques) et la gestion du risque disciplinée.
**TRADEX-AI C4** : Cette validation soutient l'architecture à 3 niveaux de TRADEX : Niveau 1 (filtres techniques Python), Niveau 2 (News Gate + VIX + macro), Niveau 3 (cerveau Claude avec KB Belkhayate).
*Catégorie : macro_evenements*

### D7565 — Plan de trading testé : discipline d'exécution
🔵 **ÉCOLE** (Source : 5_key_indicators_for_day_trading_futures.md) : Le trading efficace requiert la discipline de suivre un plan de trading testé, pas de réagir impulsivement aux mouvements de prix.
**TRADEX-AI C1** : La règle Belkhayate 3/4 trading + 2/3 confirmation = signal valide est exactement ce plan discipliné. Le moteur TRADEX encode cette discipline pour éviter les réactions émotionnelles.
*Catégorie : psychologie*
