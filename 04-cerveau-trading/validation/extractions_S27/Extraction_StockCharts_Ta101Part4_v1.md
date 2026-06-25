# Extraction StockCharts — TA 101 Part 4
**Source :** `bundles/stockcharts/ta_101_part_4.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D4231 → D4250 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-4
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : types de charts et lecture du sentiment acheteur/vendeur — applicable à GC/HG/CL/ZW/ES/VX/DX pour identifier la direction et la conviction des mouvements.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Line chart showing higher highs and lower lows | Line Charts | D4231 |
| image_02 | Illustration of an Open-High-Low-Close (OHLC) chart | OHLC Charts | D4234 |
| image_03 | SharpChart of AAPL illustrating the OHLC format | OHLC Charts | D4236 |
| image_04 | Illustration showing bar colors of an OHLC chart | OHLC Bar Colors | D4238 |
| image_05 | Example of colored OHLC price bars are shown in the AAPL SharpChart | OHLC Bar Colors | D4239 |

## DÉCISIONS

### D4231 — Line chart : visualisation de la direction des prix
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_01) : Les line charts sont créés en traçant une ligne entre les prix de clôture de chaque période. Sur un chart journalier, une ligne est tracée entre les clôtures journalières. Les line charts sont utiles pour visualiser la direction des prix et déduire rapidement l'ampleur des rallyes et des corrections dans les tendances.
**TRADEX-AI C1** : Le line chart closing-price est le filtre de direction le plus simple pour GC/HG/CL/ZW — utile pour valider la tendance de fond (C1 Direction Belkhayate) avant d'entrer sur un signal.
*Catégorie : indicateurs_tendance*

### D4232 — Tendance haussière : pattern higher highs & higher lows
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_01) : Entre mars et mi-mai 2008 sur AAPL, la direction des prix est clairement apparente avec des plus hauts et des plus bas successivement plus élevés (higher highs and higher lows — annotés en vert).
🔵 **ÉCOLE** (StockCharts/Dow Theory) : La définition classique de la tendance haussière est "une succession de higher highs et higher lows".
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, la validation de tendance haussière = higher highs + higher lows sur le timeframe range bars NT8 — condition d'entrée LONG valide.
*Catégorie : indicateurs_tendance*

### D4233 — Tendance baissière : pattern lower highs & lower lows
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_01) : Après mi-mai 2008 sur AAPL, les prix commencent à faire des plus hauts et plus bas successivement plus bas (lower highs and lower lows — annotés en rouge).
🔵 **ÉCOLE** (StockCharts/Dow Theory) : La définition classique de la tendance baissière est "une succession de lower highs et lower lows".
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, la validation de tendance baissière = lower highs + lower lows sur range bars NT8 — condition d'entrée SHORT valide.
*Catégorie : indicateurs_tendance*

### D4234 — OHLC bar chart : fournit l'information de volatilité absente du line chart
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_02) : Les graphiques OHLC (Open-High-Low-Close) fournissent des informations de volatilité que les line charts n'ont pas. L'analyste peut évaluer la volatilité par la hauteur des barres et la conviction des acheteurs/vendeurs par l'écart de prix entre les marques d'ouverture et de clôture.
**TRADEX-AI C1** : NT8 fournit les données OHLC pour GC/HG/CL/ZW — la hauteur de barre = range = mesure de volatilité directe; utilisable pour calibrer les stops et targets.
*Catégorie : structure_marche*

### D4235 — Barre haussière OHLC : clôture > ouverture = sentiment acheteur
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_02) : Pour la barre de prix gauche, la marque CLOSE est au-dessus de la marque OPEN indiquant que le prix a terminé plus haut pour la journée — "up day". Cette barre est considérée haussière. Le sentiment haussier est présent quand la cupidité de gain dépasse la peur de perdre et que les prix montent.
**TRADEX-AI C1** : Barre haussière sur GC/HG/CL/ZW = Close > Open → force acheteuse dominante — indicateur de conviction dans le sens de la tendance haussière.
*Catégorie : structure_marche*

### D4236 — Barre baissière OHLC : ouverture > clôture = sentiment vendeur
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_02) : Pour la barre de prix droite, l'OPEN est au-dessus du CLOSE indiquant que le prix a terminé plus bas — "down day". C'est une barre baissière. Le sentiment baissier est présent quand la peur de perdre est plus grande que la cupidité de gain et que les prix baissent.
**TRADEX-AI C1** : Barre baissière sur GC/HG/CL/ZW = Open > Close → force vendeuse dominante — renforce la conviction d'un signal SHORT.
*Catégorie : structure_marche*

### D4237 — Line chart vs OHLC : les swings intraday traversent les niveaux de clôture
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_03) : Le SharpChart AAPL en OHLC illustre comment les swings de prix intraday traversent les marques de référence rouges et vertes faites aux niveaux de clôture du Line Chart précédent. Cela illustre pourquoi les line charts sont utiles pour visualiser la direction des prix.
🟡 **SYNTHÈSE** : Le line chart fournit le "backbone" directionnel; le chart OHLC révèle la dynamique intraday — les deux sont complémentaires pour l'analyse multi-échelle.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, utiliser le line chart (clôtures) pour la direction macro et les barres OHLC range NT8 pour les entrées/sorties précises.
*Catégorie : timing*

### D4238 — Coloration des barres OHLC : basée sur la clôture vs clôture précédente
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_04) : Avec l'option 'Color Prices', les barres de prix sont colorées en noir ou rouge selon que le prix de clôture se situe par rapport à la clôture du jour précédent. Si la clôture est plus haute que la clôture précédente → barre noire. Si la clôture est plus basse que la clôture précédente → barre rouge.
🟢 **FAIT VÉRIFIÉ** : Il est possible d'avoir une barre noire avec une clôture inférieure à l'ouverture (si la clôture reste supérieure à la clôture de la veille).
**TRADEX-AI C1** : La coloration par rapport à la clôture précédente est plus informative que la simple comparaison Open/Close — une barre "rouge" en NT8 pour GC signifie que le momentum séance est baissier relativement à hier.
*Catégorie : structure_marche*

### D4239 — La couleur d'une barre OHLC ne reflète pas l'intraday mais le momentum inter-séance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_05) : La couleur de la barre de prix est uniquement basée sur le prix de clôture du jour précédent, PAS sur le prix d'ouverture du jour courant. Les barres "up day" et "down day" sont généralement noires et rouges respectivement, mais pas toujours.
🟡 **SYNTHÈSE** : La distinction couleur Open/Close (momentum intraday) vs couleur Close/Close précédente (momentum inter-séance) donne deux types d'information différents — l'un sur la session, l'autre sur la continuité.
**TRADEX-AI C1** : Pour TRADEX, combiner les deux lectures : momentum intraday (Open vs Close de la barre) + momentum inter-séance (Close vs Close précédente) pour évaluer la persistance du signal sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

### D4240 — Line chart : utile uniquement avec données de clôture disponibles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : Un line chart est tracé par défaut quand seuls les prix de fin de journée (clôture) sont disponibles pour un symbole. Exemples : tous les fonds communs de placement et certains indices de marché. Cependant, des barres hebdomadaires et mensuelles peuvent être créées pour des symboles avec seulement des cotations EOD.
🟡 **SYNTHÈSE** : DX (Dollar Index) et VX (VIX) peuvent n'être disponibles qu'en EOD via certains fournisseurs — dans ce cas, le line chart est le seul format applicable.
**TRADEX-AI C4/C5** : Vérifier la disponibilité OHLC pour DX et VX dans NT8 — si seulement EOD, utiliser les clôtures pour la direction macro et non pas les barres intraday.
*Catégorie : volume_liquidite*

### D4241 — OHLC : évaluation de la conviction via l'écart Open-Close
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : L'analyste peut évaluer "la conviction des acheteurs et des vendeurs par l'écart de prix entre les marques d'ouverture et de clôture".
🟡 **SYNTHÈSE** : Plus l'écart Open-Close est grand, plus la conviction directionnelle est forte. Une petite range Open-Close signale une indécision (potentiel doji/spinning top).
**TRADEX-AI C1** : Pour les barres GC/HG/CL/ZW, un grand écart Open-Close dans le sens du signal augmente la conviction — facteur de pondération dans le scoring /10 TRADEX.
*Catégorie : indicateurs_momentum*

### D4242 — Volatilité intraday : mesurable par la hauteur de la barre OHLC
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : L'analyste peut évaluer la volatilité par la hauteur des barres OHLC (High-Low range).
🟡 **SYNTHÈSE** : Une barre de grande hauteur = forte volatilité intraday = spread bid/ask plus large potentiel = risque d'exécution plus élevé.
**TRADEX-AI C5** : La hauteur des barres GC/HG/CL/ZW est un proxy de volatilité utilisable dans C5 Sentiment — barres très hautes + VIX élevé = conditions de trading dégradées → réduire ou bloquer l'auto-mode.
*Catégorie : gestion_risque_entree*

### D4243 — Sentiment : greed vs fear comme moteur fondamental du prix
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : La source explicite : "Le sentiment haussier est présent quand la cupidité de gain (greed) dépasse la peur de perdre (fear) et que les prix montent. Le sentiment baissier est présent quand la peur de perdre est plus grande que la cupidité de gain et que les prix baissent."
🔵 **ÉCOLE** (StockCharts) : La psychologie fear/greed est le mécanisme fondamental qui fait bouger les prix — l'AT est une mesure de ce déséquilibre.
**TRADEX-AI C5** : VX (VIX) mesure directement ce déséquilibre fear/greed — intégration naturelle dans le scoring TRADEX pour tous les actifs.
*Catégorie : psychologie*

### D4244 — Up day OHLC : définition formelle
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : Un "up day" OHLC = la marque CLOSE est au-dessus de la marque OPEN pour la période considérée. Ce n'est PAS basé sur la comparaison avec la veille mais sur la relation Open-Close de la même barre.
**TRADEX-AI C1** : Sur range bars NT8 pour GC/HG/CL/ZW, "up bar" = Close > Open → condition de base pour signal LONG dans la méthode Belkhayate (alignement directionnel intrabar).
*Catégorie : structure_marche*

### D4245 — Down day OHLC : définition formelle
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : Un "down day" OHLC = l'OPEN est au-dessus du CLOSE pour la période. Le prix a terminé plus bas pour la journée.
**TRADEX-AI C1** : Sur range bars NT8 pour GC/HG/CL/ZW, "down bar" = Open > Close → condition de base pour signal SHORT — nécessaire mais non suffisant (3/4 trading + 2/3 confirmation requis).
*Catégorie : structure_marche*

### D4246 — La hauteur des barres OHLC révèle la volatilité, les niveaux de clôture la direction
🟡 **SYNTHÈSE** (Source : ta_101_part_4.md) : La combinaison line chart (clôtures) + OHLC (volatilité + conviction) donne une vision complète : la direction via les clôtures successives et la dynamique intraday via la hauteur et le body des barres.
**TRADEX-AI C1** : Architecture d'analyse TRADEX pour GC/HG/CL/ZW : (1) direction = trailing des clôtures, (2) timing d'entrée = structure des barres OHLC, (3) conviction = ratio body/total range.
*Catégorie : indicateurs_tendance*

### D4247 — Intraday swings traversent les niveaux de support/résistance inter-séance
🟡 **SYNTHÈSE** (Source : ta_101_part_4.md, image_03) : Les oscillations intraday traversent les marques de clôture précédentes, ce qui illustre que les niveaux de clôture deviennent des niveaux de référence (support/résistance potentiels).
**TRADEX-AI C1** : Les pivots Belkhayate (calculés sur les clôtures/OHLC) correspondent exactement à ces niveaux de référence — confirmant leur rôle de S/R naturels pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D4248 — Coloration 'Color Prices' : outil visuel rapide de lecture du momentum
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md) : Avec la coloration, les barres noires signalent une activité d'achat forte/faible et les barres rouges signalent une activité de vente forte/faible — "Color volume bars allow the chartist to quickly see where heavy or weak buying and selling activity is happening."
**TRADEX-AI C2** : Le color-coding volume dans ATAS (barres colorées selon delta) est la version order-flow de cette même logique — acheteurs (vert) vs vendeurs (rouge) visualisés directement dans les barres.
*Catégorie : volume_liquidite*

### D4249 — OHLC : confirmation visuelle de la direction du line chart
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_03) : En superposant les niveaux de clôture (line chart) sur le chart OHLC, on voit que les swings intraday gravitent autour de ces niveaux. Le line chart est "utile pour visualiser la direction des prix" même quand on travaille en OHLC.
**TRADEX-AI C1** : Multi-chart view pour TRADEX : afficher simultanément le line chart de direction (macro) et les barres range NT8 (micro-timing) pour GC/HG/CL/ZW dans le dashboard React.
*Catégorie : timing*

### D4250 — Barres OHLC : couleur reflète la dynamique inter-séance, pas forcément l'intraday
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_4.md, image_05) : La couleur d'une barre OHLC est basée sur la clôture précédente, pas sur l'ouverture courante — donc une barre peut être noire (close > close précédente) ET down day (close < open courant). Cette distinction est explicitement illustrée dans le chart.
🟡 **SYNTHÈSE** : Une barre noire avec close < open représente un "gap up" partiel suivi d'un retournement — potentiel signal de fatigue haussière.
**TRADEX-AI C1** : Scénario de piège haussier sur GC/HG/CL/ZW : barre noire (momentum inter-séance positif) MAIS down day (intraday reversal) → signal d'affaiblissement potentiel; nécessite confirmation C2 order flow.
*Catégorie : gestion_risque_entree*
