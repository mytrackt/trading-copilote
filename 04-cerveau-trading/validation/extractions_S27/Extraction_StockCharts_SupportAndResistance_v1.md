# Extraction StockCharts — Support & Resistance
**Source :** `bundles/stockcharts/support_and_resistance.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D3951 → D3970 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/support-and-resistance
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : fondamentaux support/résistance applicables directement à GC/HG/CL/ZW pour définir les niveaux d'entrée, stops et objectifs dans la méthode Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Example of support levels on the chart of Amazon.com, Inc. (AMZN) | What Is Support? | D3951 |
| image_02 | Example of resistance level in a price chart | What Is Resistance? | D3953 |
| image_03 | Example of support and resistance levels based on highs and lows | Highs and Lows | D3955 |
| image_04 | Example of resistance level turning into a support level | Support Equals Resistance | D3956 |
| image_05 | Example of support level turning into resistance level | Support Equals Resistance | D3957 |
| image_06 | Support and resistance levels when a stock is in a trading range | Trading Range | D3959 |
| image_07 | Chart displaying support and resistance zones | What Are Support and Resistance Zones? | D3963 |

## DÉCISIONS

### D3951 — Définition du support : niveau où la demande est assez forte pour stopper le déclin
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_01) : "Le support est le niveau de prix auquel la demande est censée être assez forte pour empêcher le prix de décliner davantage." Logique : à mesure que le prix baisse vers le support, les acheteurs deviennent plus enclins à acheter et les vendeurs moins enclins à vendre. On croit que la demande surmontera l'offre au niveau du support.
**TRADEX-AI C1** : Définition fondamentale à intégrer dans la KB — sur GC/CL/ZW, le support est une zone d'entrée potentielle en mode Manuel si le contexte Belkhayate est haussier.
*Catégorie : structure_marche*

### D3952 — Rupture de support : signal de nouvelle volonté de vendre
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Le support ne tient pas toujours. Une rupture sous le support signale que les bears ont pris le dessus. Un déclin sous le support indique une nouvelle volonté de vendre et/ou un manque d'incitation à acheter. Les vendeurs ont réduit leurs attentes et sont prêts à vendre à des prix encore plus bas. Une fois le support rompu, un nouveau niveau de support devra être établi à un niveau inférieur.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, rupture de support = signal d'alerte critique — enclenche la vérification du circuit breaker TRADEX et invalide les signaux d'achat en cours.
*Catégorie : structure_marche*

### D3953 — Définition de la résistance : niveau où l'offre est assez forte pour stopper la hausse
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_02) : "La résistance est le niveau de prix auquel la vente est censée être assez forte pour empêcher le prix de monter davantage." Logique : à mesure que le prix monte vers la résistance, les vendeurs deviennent plus enclins à vendre et les acheteurs moins enclins à acheter.
**TRADEX-AI C1** : Définition fondamentale à intégrer dans la KB — sur GC/CL, la résistance est une zone de prise de profit ou de placement de stop en mode Manuel.
*Catégorie : structure_marche*

### D3954 — Rupture de résistance : signal de nouveau leadership des bulls
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : La résistance ne tient pas toujours. Une rupture au-dessus de la résistance signale que les bulls ont pris le dessus. Une rupture de résistance montre une nouvelle volonté d'acheter et/ou un manque d'incitation à vendre. Une fois la résistance rompue, un nouveau niveau de résistance devra être établi à un niveau supérieur.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, rupture de résistance sur volume = signal de continuation haussière — valide une entrée longue si les autres cercles Belkhayate confirment.
*Catégorie : structure_marche*

### D3955 — Etablissement des niveaux : hauts précédents = résistance, bas précédents = support
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_03) : Le support peut être établi avec les bas de réaction précédents (reaction lows), la résistance avec les hauts de réaction précédents (reaction highs). Exemple Halliburton (HAL) : le bas d'octobre (31) devient support ; le stock y revient 3 fois (33 et 32,5). La rupture d'un support précédent (42,5 en septembre) devient la première résistance.
**TRADEX-AI C1** : Sur GC/CL/ZW, utiliser les creux et pics récents NT8 comme niveaux de S/R — méthode la plus directe et objective pour calculer le R/R ≥ 1:2 TRADEX.
*Catégorie : structure_marche*

### D3956 — Principe clé : le support rompu devient résistance
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_04) : "Le support peut se transformer en résistance et vice versa." Une fois que le prix casse sous un niveau de support, ce support rompu peut devenir résistance. La rupture du support signale que les forces de l'offre ont surmonté les forces de la demande. Si le prix revient à ce niveau, il y aura probablement une augmentation de l'offre, donc de la résistance. Exemple NASDAQ 100 : résistance à 935 rompue en mai 1997, devient support, confirmé deux fois à 935.
**TRADEX-AI C1** : Règle de base Belkhayate — sur GC/CL, après une rupture de support, l'ancien support devient la zone de résistance pour le retour technique (dead-cat bounce).
*Catégorie : structure_marche*

### D3957 — Principe clé : la résistance rompue devient support
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_05) : Quand le prix passe au-dessus d'une résistance, cela signale des changements dans l'offre et la demande. La cassure au-dessus prouve que la demande a submergé l'offre. Si le prix revient à ce niveau, la demande augmentera probablement et du support sera trouvé. Exemple PeopleSoft : support à 18 (oct 98 - jan 99), rompu en mars 99, devient résistance (juin 99 - oct 99), puis support à nouveau après épuisement de l'offre.
**TRADEX-AI C1** : Sur GC/CL, l'ancienne résistance cassée = nouveau support — zone prioritaire pour placer un stop en dessous et calculer R/R sur la prochaine jambe haussière.
*Catégorie : structure_marche*

### D3958 — Psychologie derrière le support/résistance : effet "overhead supply"
🟡 **SYNTHÈSE** (Source : support_and_resistance.md) : L'offre excédentaire (overhead supply) autour d'une ancienne résistance s'explique par : des acheteurs qui ont acheté au support initial et se retrouvent en perte quand le support est rompu. Quand le prix remonte au niveau d'ancienne résistance, ces acheteurs-en-perte saisissent l'opportunité de vendre à break-even ou avec peu de perte — créant la résistance. Quand cette offre est épuisée, la demande peut l'emporter.
**TRADEX-AI C3** : Sur GC/HG/CL/ZW, les positions institutionnelles bloquées (overhead supply) aux anciens supports créent des résistances techniques mesurables — pertinent pour C3 (COT/OI).
*Catégorie : psychologie*

### D3959 — Trading range : signaux de cassure déterminent le gagnant (bulls ou bears)
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_06) : Un trading range est quand les prix évoluent dans une fourchette relativement étroite, signalant que l'offre et la demande sont équilibrées. "Une cassure au-dessus est une victoire pour les bulls (demande), et une cassure en-dessous est une victoire pour les bears (offre)." Un faux breakout (red oval) peut se produire — nécessite confirmation (le gap down a annulé le breakout WorldCom).
**TRADEX-AI C1** : Sur GC/CL/ZW, distinguer faux breakout de vrai breakout — la confirmation par le volume ATAS et la clôture sont essentielles avant de signaler en mode Auto.
*Catégorie : structure_marche*

### D3960 — Après rupture d'un trading range, retour au niveau = deuxième chance
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Après une rupture d'un trading range, le prix peut revenir tester le nouveau niveau (ancien support devenu résistance). Ce retour offre une deuxième chance pour les longs de sortir et les shorts d'entrer. "Cela n'arrive pas toujours, mais un retour au nouveau niveau de résistance offre une deuxième chance."
**TRADEX-AI C1** : Sur GC/CL, après cassure d'un range, attendre le retest de l'ancien support (maintenant résistance) avant une entrée short — améliore le R/R.
*Catégorie : gestion_risque_entree*

### D3961 — Importance du volume lors de la cassure (exemple Lucent head & shoulders)
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Sur Lucent Technologies (LU), une cassure de support (tête-épaules à 60) s'est produite si vite qu'il était impossible de sortir au-dessus de 44. Le support break à 61 (neckline inclinée) aurait donné 1 point supplémentaire pour agir. "Un trader doit agir immédiatement pour éviter une chute brutale." Les creux s'alignent bien avec la neckline oblique.
**TRADEX-AI C1** : Sur GC/CL, les cassures de support sur head & shoulders peuvent être violentes — en mode Auto, les ordres stop doivent être pré-placés, pas attendus.
*Catégorie : gestion_risque_entree*

### D3962 — Signaux de retournement dans un trading range : hammers et gaps
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Après déclin de Lucent à 40-41, trading range 40,5-47,5 pendant 2 mois. Résistance clairement marquée par 3 pics à 47,5. Signes de demande croissante autour de 44 mi-à-fin février : nombreux chandeliers avec longues mèches basses (hammers). Cassure finale avec 2 gaps haussiers (24-25 fév), close > 48 = demande gagnant clairement sur l'offre. 2 jours supplémentaires pour entrer, puis gap vers > 56.
**TRADEX-AI C1** : Sur GC/CL, les hammers répétés au support + gap de confirmation = signal d'entrée haute probabilité — à croiser avec le volume ATAS et les indicateurs Belkhayate.
*Catégorie : configuration*

### D3963 — Support et résistance zones plutôt que niveaux exacts
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md, image_07) : Créer des zones de support/résistance plutôt que des niveaux exacts est souvent plus pratique, car l'analyse technique n'est pas une science exacte. Règle : si le trading range est étroit (< 2 mois, faible range), utiliser des niveaux exacts. Si le trading range est étendu (plusieurs mois, grand range), utiliser des zones.
**TRADEX-AI C1** : Sur GC (actif très volatile), préférer des zones de S/R (ex : GC 2400-2420$) plutôt que des niveaux ponctuels — réduire les faux signaux de cassure dans le moteur.
*Catégorie : structure_marche*

### D3964 — Critère zone vs niveau exact : extension > 20% = zone
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Exemple HAL : le haut de novembre du trading range (32-44) s'étend de plus de 20% au-dessus du bas d'octobre — range assez grand pour nécessiter une zone plutôt qu'un niveau. Règle générale : si le haut dépasse le bas de > 20%, utiliser des zones de support/résistance.
**TRADEX-AI C1** : Sur GC/CL (grandes amplitudes), calculer la largeur relative du range — si > 20%, définir une zone S/R plutôt qu'un point exact dans le moteur Python.
*Catégorie : structure_marche*

### D3965 — Identification du support/résistance : ingrédient essentiel de l'analyse technique
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : "L'identification des niveaux clés de support et de résistance est un ingrédient essentiel pour réussir en analyse technique." Même s'il est difficile d'établir des niveaux exacts, connaître leur existence et leur localisation peut grandement améliorer les capacités d'analyse et de prévision.
**TRADEX-AI C1** : Fondement du cercle C1 TRADEX — les niveaux S/R sont la première couche de l'analyse Belkhayate avant tout signal momentum.
*Catégorie : structure_marche*

### D3966 — Signal d'alerte : approche d'un support = vigilance accrue à l'achat
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : "Si un titre approche un niveau de support important, cela peut servir d'alerte pour être particulièrement vigilant en cherchant des signes de pression d'achat accrue et d'un retournement potentiel."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, approche d'un support majeur = déclencher une analyse Claude niveau 3 anticipée — alerter Abdelkrim en mode Manuel avant que le signal soit formel.
*Catégorie : gestion_risque_entree*

### D3967 — Signal d'alerte : approche d'une résistance = vigilance accrue à la vente
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : "Si un titre approche un niveau de résistance, cela peut servir d'alerte pour des signes de pression de vente accrue et d'un retournement potentiel."
**TRADEX-AI C1** : Sur GC/CL, approche d'une résistance majeure = signal d'alerte pour prise de profits partielle ou resserrement du stop — à intégrer dans la logique de gestion de position active.
*Catégorie : gestion_position_active*

### D3968 — Rupture de S/R = changement dans la relation offre/demande
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : "Si un niveau de support ou de résistance est rompu, la relation entre l'offre et la demande a changé." Une rupture de résistance signale que les bulls (demande) ont pris le dessus ; une rupture de support signale que les bears (offre) ont gagné.
**TRADEX-AI C1** : Principe fondamental à intégrer dans le prompt Claude KB : une rupture confirmée de S/R = changement de régime de marché — modifie le biais directionnel pour les signaux suivants.
*Catégorie : structure_marche*

### D3969 — Support/résistance comme opportunité d'achat/vente dans un range
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : "Le support peut être regardé comme une opportunité d'acheter, et la résistance comme une opportunité de vendre [dans un trading range]." Cette logique s'applique tant que le trading range est considéré valide (prix dans les limites définies).
**TRADEX-AI C1** : Sur GC/ZW en phase de trading range (ADX < 20), utiliser les zones S/R comme niveaux d'entrée/sortie — stratégie de mean reversion complémentaire à la stratégie de breakout.
*Catégorie : gestion_risque_entree*

### D3970 — Zones de S/R : application pratique des FAQs
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance.md) : Les niveaux de S/R sont importants car : (1) ils aident à la prévision et à l'analyse, (2) ils agissent comme alertes pour les retournements potentiels, (3) ils signifient des changements dans la relation offre/demande. Le lien S/R avec offre/demande : support = demande forte > offre ; résistance = offre forte > demande ; price latéral = offre = demande.
**TRADEX-AI C1** : Framework offre/demande directement aligné avec la méthode Belkhayate (équilibre vs déséquilibre) — les niveaux S/R traduisent en prix les déséquilibres institutionnels détectables via COT (C3).
*Catégorie : structure_marche*
