# Extraction StockCharts — StochRSI
**Source :** `bundles/stockcharts/stochrsi.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D3911 → D3930 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochrsi
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : indicateur de momentum haute sensibilité applicable à GC/HG/CL/ZW/ES pour détecter les extremes de RSI et identifier les tendances court terme.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | RSI - Spreadsheet 1 | Calculation | D3912 |
| image_02 | StochRSI - Chart 1 | Interpretation | D3914 |
| image_03 | StochRSI - Chart 2 | Overbought/Oversold | D3916 |
| image_04 | StochRSI - Chart 3 | Overbought/Oversold | D3917 |
| image_05 | StochRSI - Chart 4 | Trend Identification | D3919 |
| image_06 | StochRSI - Chart 1 (Chart 6 du texte) | Trend Identification | D3921 |

## DÉCISIONS

### D3911 — Origine et définition du StochRSI
🔵 **ÉCOLE** (Source : stochrsi.md) : Développé par Tushar Chande et Stanley Kroll, présenté dans leur livre *The New Technical Trader* (1994). Le StochRSI applique la formule du stochastique aux valeurs du RSI (et non aux prix), produisant un oscillateur entre 0 et 1. C'est un indicateur d'indicateur — deux étapes (formules) séparent le prix du StochRSI.
**TRADEX-AI C1** : Le StochRSI est plus sensible que le RSI brut — utile sur GC/CL pour détecter les extremes de momentum que le RSI 14j manquerait.
*Catégorie : indicateurs_momentum*

### D3912 — Formule de calcul du StochRSI
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_01) : `StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)`. Le nombre de périodes utilisé pour calculer le StochRSI est reporté dans le RSI. Exemple : StochRSI 14 jours utilise le RSI 14 jours courant et le range haut-bas sur 14 jours du RSI 14 jours.
🟢 **FAIT VÉRIFIÉ** : StochRSI 14j = 0 quand RSI au plus bas sur 14j ; = 1 quand RSI au plus haut sur 14j ; = 0,5 au milieu du range ; = 0,2 près du bas ; = 0,80 près du haut.
**TRADEX-AI C1** : Formule implémentable en Python pour GC/HG/CL/ZW — calcul direct sur la série RSI NT8.
*Catégorie : indicateurs_momentum*

### D3913 — Pourquoi StochRSI a été créé : limite du RSI sur les zones extrêmes
🔵 **ÉCOLE** (Source : stochrsi.md) : Chande et Kroll expliquent que le RSI peut osciller entre 80 et 20 pendant des périodes prolongées sans atteindre les zones extrêmes (notons qu'ils utilisent 80/20 et non 70/30). Les traders cherchant à entrer sur la base d'un signal suracheté/survendu du RSI peuvent se retrouver continuellement en dehors du marché.
**TRADEX-AI C1** : Sur GC/CL (marchés très tendanciels), le RSI peut rester suracheté longtemps — le StochRSI détecte des extremes relatifs dans ce contexte.
*Catégorie : indicateurs_momentum*

### D3914 — Niveaux suracheté/survendu du StochRSI
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_02) : StochRSI > 0,80 est considéré suracheté. StochRSI < 0,20 est considéré survendu. En tant qu'oscillateur borné, la ligne centrale est à 0,50. StochRSI reflète une tendance haussière quand il est consistamment au-dessus de 0,50 et baissière quand consistamment en-dessous de 0,50.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, StochRSI > 0,80 = signal de prudence pour les acheteurs ; < 0,20 = opportunité potentielle d'achat en tendance haussière.
*Catégorie : indicateurs_momentum*

### D3915 — Règle clé : trader dans la direction de la tendance principale
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : La règle essentielle est de chercher des conditions survendues quand la tendance principale est haussière, et des conditions surachetées quand la tendance principale est baissière. Pour un StochRSI 14j (indicateur court terme), il faut identifier la tendance moyen terme avant d'utiliser les signaux suracheté/survendu.
**TRADEX-AI C1** : Sur GC/CL, utiliser StochRSI en mode "oversold dans uptrend" — ne pas vendre sur signal suracheté si la tendance Belkhayate est haussière.
*Catégorie : indicateurs_tendance*

### D3916 — Exemple : StochRSI survendu dans un uptrend moyen terme (Boeing)
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_03) : Sur Boeing, tendance moyen terme haussière (SMA 10j > SMA 60j). StochRSI(14) est devenu survendu au moins 4 fois de décembre à février. Le RSI 14j n'a pas atteint le survendu pendant cette période car il est moins sensible. Le survendu n'est pas équivalent à haussier — c'est un avertissement de guetter un rebond. Un catalyseur est nécessaire (ex : prix revenant au-dessus de la SMA 10j, ou StochRSI remontant au-dessus de 0,50).
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en uptrend, StochRSI < 0,20 = zone d'attention pour entrée longue, mais attendre confirmation (close > SMA 10j ou StochRSI > 0,50).
*Catégorie : gestion_risque_entree*

### D3917 — Exemple : StochRSI suracheté dans un downtrend moyen terme (Flour Corp)
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_04) : Sur Flour Corp, tendance moyen terme baissière (SMA 10j < SMA 60j). Les lectures surachetées de StochRSI sont exploitées (> 0,80). Le retour de StochRSI sous 0,50 confirme la fin du rebond technique. On peut aussi surveiller le retour du prix sous la SMA 10j.
**TRADEX-AI C1** : Sur GC/CL en downtrend, StochRSI > 0,80 = zone de prudence pour les longs — possible signal de sortie ou de réduction de position.
*Catégorie : gestion_position_active*

### D3918 — Lissage du StochRSI par une moyenne mobile pour identification de tendance
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Pour identifier la tendance court terme, allonger la période de calcul et appliquer une moyenne mobile courte sur le StochRSI. La SMA 10 jours du StochRSI au-dessus de 0,50 = momentum favorisant la hausse ; en-dessous de 0,50 = momentum favorisant la baisse.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, SMA 5j du StochRSI(20) > 0,50 confirme un momentum haussier à court terme — filtre de tendance supplémentaire pour le score /10.
*Catégorie : indicateurs_tendance*

### D3919 — Exemple : SMA 5j du StochRSI 20j pour trend-following (Chevron)
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_05) : Sur Chevron (CVX), le SMA 5j du StochRSI(20) est passé au-dessus de 0,50 mi-février juste après un gap haussier. Gap + croisement > 0,50 = signaux haussiers court terme. La tendance a tenu jusqu'à fin avril même si le StochRSI(20) a brièvement plongé sous 0,50 en mars (car la SMA 5j a tenu > 0,50). Signal court terme devenu tendance de 2 mois.
**TRADEX-AI C1** : Sur GC/CL, SMA 5j du StochRSI(20) > 0,50 comme filtre de momentum pour maintenir les positions longues tant que la SMA reste au-dessus.
*Catégorie : gestion_position_active*

### D3920 — Risque de faux signaux (whipsaws) avec le lissage
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Même avec la SMA 5j du StochRSI(20), des whipsaws se produisent. Lors d'une consolidation dans une tendance, la SMA 5j peut osciller au-dessus/en-dessous de 0,50 avant de reprendre ou d'inverser. Exemple Yahoo! : la SMA 5j a brièvement plongé sous 0,50 deux fois lors d'un canal baissier avant de reprendre la hausse.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ne pas sortir d'une position sur un seul croisement < 0,50 de la SMA 5j du StochRSI — attendre confirmation par le prix (ex : rupture de support).
*Catégorie : gestion_position_active*

### D3921 — Signal baissier StochRSI qui ne se déclenche pas immédiatement
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md, image_06) : Sur Yahoo!, le SMA 5j du StochRSI(20) est passé sous 0,50 (signal baissier) mais Yahoo! a surgi à 18 quelques jours après, créant un bear trap. Même si le prix a rebondi fortement, la SMA 5j du StochRSI est restée sous 0,50 (le momentum n'a pas confirmé). Le gap à 17,50 s'est révélé un exhaustion gap — Yahoo! a ensuite fortement baissé.
**TRADEX-AI C1** : Sur GC/CL, maintenir le biais baissier si SMA StochRSI reste < 0,50 même sur rebond — le non-confirmation du momentum valide la direction baissière.
*Catégorie : indicateurs_momentum*

### D3922 — StochRSI est "RSI sur stéroïdes" : plus de signaux, plus de bruit
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : "StochRSI est comme RSI sur stéroïdes." Le RSI produit relativement peu de signaux ; StochRSI augmente dramatiquement leur nombre. Il y aura plus de lectures suracheté/survendu, plus de croisements de la ligne centrale, plus de bons signaux et plus de mauvais signaux. La vitesse a un prix.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, utiliser StochRSI comme filtre secondaire (non primaire) — toujours confirmer avec d'autres éléments Belkhayate avant de signaler.
*Catégorie : indicateurs_momentum*

### D3923 — Indicateurs complémentaires recommandés pour confirmer StochRSI
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Pour confirmer les signaux StochRSI, utiliser : gaps, ruptures de support/résistance, patterns de prix (chartistes), et indicateurs basés sur le volume comme l'On Balance Volume (OBV) ou la Accumulation/Distribution Line. Ces indicateurs de volume ne chevauchent pas les oscillateurs de momentum.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, croiser StochRSI avec le volume ATAS (delta cumulé, OBV) pour filtrer les faux signaux — confirmation multi-source obligatoire.
*Catégorie : volume_liquidite*

### D3924 — Paramétrage par défaut et utilisation dans SharpCharts
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Paramètre par défaut = 14 périodes. Une moyenne mobile peut être appliquée en options avancées comme overlay. L'indicateur peut être affiché au-dessus, en-dessous ou derrière le graphique de prix.
**TRADEX-AI C1** : Paramétrage initial suggéré pour TRADEX : StochRSI(14) avec SMA(5) overlay — ajustable selon les marchés (GC/CL plus volatils peuvent nécessiter période > 14).
*Catégorie : indicateurs_momentum*

### D3925 — Scan : StochRSI survendu dans uptrend moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Filtre scan : SMA(10, close) > SMA(60, close) [uptrend moyen terme] ET close < SMA(10, close) [pull-back court terme] ET StochRSI(14) < 0,10 [fortement survendu]. Filtre de liquidité : SMA(20, volume) > 40 000 et SMA(60, close) > 10$.
**TRADEX-AI C1** : Logique transposable sur NT8 pour GC/HG/CL/ZW — déclencher l'analyse Claude uniquement quand SMA 10 > SMA 60 ET StochRSI < 0,10 (ultra-survendu).
*Catégorie : configuration*

### D3926 — Scan : StochRSI suracheté dans downtrend moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : stochrsi.md) : Filtre scan : SMA(10, close) < SMA(60, close) [downtrend moyen terme] ET close > SMA(10, close) [rebond technique] ET StochRSI(14) > 0,90 [fortement suracheté]. Filtre de liquidité identique au scan précédent.
**TRADEX-AI C1** : Sur GC/CL en downtrend, StochRSI > 0,90 sur rebond = zone de vigilance pour sortie ou réduction de position longue.
*Catégorie : configuration*
