# Extraction StockCharts — TRIX
**Source :** `bundles/stockcharts/trix.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D4671 → D4690 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/trix.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : oscillateur momentum à triple lissage applicable sur GC/HG/CL/ZW pour filtrer le bruit et détecter divergences, croisements signal et crossings de la ligne zéro.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/8VpJzEwIRMMcNlxDtugH | Tableau calcul EMA lissages successifs | Calcul | D4672 |
| /files/bBfz2g3vRiduZO1klTba | TRIX - Chart 1 : triple-smoothed EMA vs prix SPY | Calcul | D4673 |
| /files/n7e6gKzYhv0joZHPoy1k | TRIX - Chart 2 : TRIX négatif/positif selon direction EMA triple | Calcul | D4674 |
| /files/Ab051OwciyVWQonpvubQ | TRIX - Chart 3 : comparaison TRIX vs MACD | Interprétation | D4675 |
| /files/L43Hc67p2v5tdH7oguQe | TRIX - Chart 4 : six croisements signal Intel (INTC) | Signal line crossovers | D4677 |
| /files/GTMIfrxnrUnWDY1xXogZ | TRIX - Chart 5 : cinq signaux centerline Raytheon (RTN) | Centerline crossovers | D4680 |
| /files/gUttJPcBh7MFZcCpFUqW | TRIX - Chart 6 : divergences baissières BHP Billiton | Divergences | D4682 |
| /files/9uplrrZa5BGlqdfExrMe | TRIX - Chart 7 : divergence haussière réussie eBay (EBAY) | Divergences | D4683 |
| /files/nD5IG2uojcH8IK9obsa4 | TRIX - Chart 8 : vue globale indicateur | Bottom Line | D4686 |
| /files/svXRnBxB5mREEIHlMmMV | TRIX - Chart 7 SharpCharts : configuration | SharpCharts | D4688 |

## DÉCISIONS

### D4671 — TRIX : définition et objectif
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : TRIX est un oscillateur momentum qui affiche le taux de variation en pourcentage d'une moyenne mobile triple exponentiellement lissée. Développé dans les années 1980 par Jack Hutson. Son triple lissage est conçu pour filtrer les mouvements de prix insignifiants.
**TRADEX-AI C1** : TRIX applicable sur GC/HG/CL/ZW comme filtre de momentum ; son triple lissage le rend particulièrement utile pour éliminer le bruit de marché avant d'émettre un signal.
*Catégorie : indicateurs_momentum*

### D4672 — TRIX : formule de calcul en 4 étapes
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_8VpJzEwIRMMcNlxDtugH) : Pour un TRIX(15) : 1) EMA simple = EMA 15 périodes des clôtures ; 2) EMA double = EMA 15 périodes de l'EMA simple ; 3) EMA triple = EMA 15 périodes de l'EMA double ; 4) TRIX = variation % 1 période de l'EMA triple.
**TRADEX-AI C1** : Implémenter TRIX dans le moteur Python de `05-saas/engine/` avec paramètre par défaut TRIX_PERIOD = 15 ; calculer sur les données NT8 JSON pour GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

### D4673 — TRIX : comportement de l'EMA triple lissée
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_bBfz2g3vRiduZO1klTba) : L'EMA triple lissée est plus plate et plus lente que les EMA simple et double. Plus le lissage augmente, plus la ligne s'aplatit. TRIX est négatif tant que l'EMA triple 15j descend, et devient positif quand elle remonte.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, TRIX en territoire négatif = tendance baissière persistante sur l'EMA triple ; TRIX qui remonte vers zéro depuis le bas = momentum baissier qui s'épuise.
*Catégorie : indicateurs_momentum*

### D4674 — TRIX : le triple lissage exige plus d'un jour pour renverser
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_n7e6gKzYhv0joZHPoy1k) : Le lissage supplémentaire garantit que les retournements à la hausse et à la baisse sont maintenus au minimum. Cela signifie qu'il faut plus d'une séance de hausse pour renverser une tendance baissière.
**TRADEX-AI C1** : Avantage filtrant sur GC/HG/CL/ZW : un seul spike ne déclenchera pas un faux signal TRIX ; utile pour éviter les entrées prématurées sur news volatiles.
*Catégorie : gestion_risque_entree*

### D4675 — TRIX vs MACD : similitudes et différences
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_Ab051OwciyVWQonpvubQ) : TRIX(15,9) est similaire à MACD(12,26,9). Les deux sont des oscillateurs momentum fluctuant autour de zéro avec une ligne signal en EMA 9. TRIX est plus lisse ; ses lignes sont moins erratiques et ont tendance à tourner un peu plus tard.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, TRIX peut remplacer ou compléter le MACD dans la grille de décision ; préférer TRIX quand le marché est très volatile (ex : annonce économique récente) pour réduire les whipsaws.
*Catégorie : indicateurs_momentum*

### D4676 — TRIX : trois signaux principaux
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : Les trois signaux principaux à surveiller avec TRIX sont : 1) croisements de la ligne signal (plus fréquents) ; 2) croisements de la ligne centrale (biais momentum général) ; 3) divergences haussières/baissières (anticipation de retournement).
**TRADEX-AI C1** : Intégrer les 3 types de signaux TRIX dans la grille /10 de TRADEX-AI pour GC/HG/CL/ZW ; chaque type peut contribuer à un point différent de la grille de score.
*Catégorie : indicateurs_momentum*

### D4677 — TRIX : croisements de la ligne signal
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_L43Hc67p2v5tdH7oguQe) : La ligne signal est une EMA 9 du TRIX. Un croisement haussier (TRIX monte au-dessus de la ligne signal) = première indication haussière. Un croisement baissier (TRIX descend sous la ligne signal) = première implication négative. Ces signaux fréquents peuvent générer des whipsaws en l'absence d'un mouvement fort.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, filtrer les croisements signal TRIX : valider uniquement si le marché est en tendance forte ou si le croisement est confirmé par un autre indicateur du cercle C1 ou C2.
*Catégorie : indicateurs_momentum*

### D4678 — TRIX : whipsaws fréquents sans tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_L43Hc67p2v5tdH7oguQe) : Intel (INTC) a produit 6 croisements signal en 7 mois, dont 3 bons signaux et 3 mauvais (whipsaws). En l'absence d'un mouvement fort, le lag de l'EMA triple produit des signaux tardifs générateurs de pertes.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en range ou faible volatilité, réduire le poids du signal TRIX dans la grille /10 ; augmenter le seuil de confirmation minimum à 2 indicateurs supplémentaires.
*Catégorie : gestion_risque_entree*

### D4679 — TRIX : croisements de la ligne centrale (zéro)
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : Le croisement de la ligne centrale indique si le "verre est à moitié plein" (haussier) ou "à moitié vide" (baissier). L'EMA triple monte quand TRIX est positif, descend quand négatif. Le momentum favorise les bulls quand TRIX est positif, les bears quand négatif.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, utiliser TRIX > 0 comme filtre directionnel dans la grille C1 : n'accepter les signaux ACHETER que si TRIX est positif ou en cours de crossover zéro.
*Catégorie : indicateurs_momentum*

### D4680 — TRIX : croisement centerline + cassure résistance = signal renforcé
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_GTMIfrxnrUnWDY1xXogZ) : Sur Raytheon (RTN), le 4ème signal (nov. 2009) coïncidait avec une cassure de résistance sur le graphique prix, produisant une avance de +20%. Combinaison signal indicateur + signal chartiste = renforcement mutuel.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, si le croisement centerline TRIX coïncide avec une cassure de résistance identifiée (pivot Belkhayate ou pattern chart), augmenter le score de décision ; cette combinaison est plus fiable que chaque signal seul.
*Catégorie : configuration*

### D4681 — TRIX : divergences baissières inefficaces en forte tendance haussière
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_gUttJPcBh7MFZcCpFUqW) : Les divergences baissières ne fonctionnent pas bien dans les fortes tendances haussières. Tant que l'indicateur est au-dessus de sa ligne centrale, le momentum reste haussier même si l'indicateur forme des plus bas hauts.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en fort uptrend, ignorer les divergences baissières TRIX tant que TRIX reste positif ; une divergence n'est significative que si TRIX croise aussi en dessous de zéro.
*Catégorie : indicateurs_momentum*

### D4682 — TRIX : divergences haussières inefficaces en forte tendance baissière
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : Les divergences haussières ne fonctionnent pas bien dans les fortes tendances baissières. Tant que l'indicateur reste en dessous de sa ligne centrale, le momentum baissier est plus fort que le haussier.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en fort downtrend, ignorer les divergences haussières TRIX tant que TRIX reste négatif ; condition minimale : TRIX doit croiser au-dessus de zéro pour valider le retournement.
*Catégorie : indicateurs_momentum*

### D4683 — TRIX : divergence haussière réussie — séquence de confirmation
🟢 **FAIT VÉRIFIÉ** (Source : trix.md, image_9uplrrZa5BGlqdfExrMe) : Sur eBay (EBAY), la divergence haussière a été confirmée par : 1) TRIX au-dessus de sa ligne signal ; 2) cassure de résistance chartiste avec bon volume ; 3) TRIX passant en territoire positif. Malgré une confirmation tardive, les signaux de force ont validé le breakout.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, valider une divergence haussière TRIX seulement après confirmation triple : TRIX > signal line + cassure résistance prix + TRIX > 0. Ce filtre réduit les faux positifs.
*Catégorie : configuration*

### D4684 — TRIX : paramétrage selon sensibilité souhaitée
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : Paramétrage standard : TRIX(15) pour l'EMA triple, signal line EMA(9). Pour plus de sensibilité → période courte (ex. 5 vs 15), meilleur pour crossings centerline. Pour moins de sensibilité → période longue (ex. 45 vs 15), meilleur pour crossings signal line.
**TRADEX-AI C1** : Sur GC (marché or lent) : envisager TRIX(45,9) pour réduire le bruit. Sur CL (pétrole volatile) : TRIX(15,9) standard ou TRIX(5,9) pour réactivité max. Paramétrable par actif dans `config/settings.py`.
*Catégorie : indicateurs_momentum*

### D4685 — TRIX : toujours combiner avec d'autres éléments d'analyse
🟢 **FAIT VÉRIFIÉ** (Source : trix.md) : Comme pour tous les indicateurs, TRIX doit être utilisé conjointement avec d'autres aspects de l'analyse technique, comme les patterns chartistes.
**TRADEX-AI C1** : TRIX seul ne constitue pas un signal valide dans TRADEX-AI ; combiner obligatoirement avec au moins un signal des cercles C1 (structure prix/Belkhayate) et C2 (order flow) pour tout actif TRADING.
*Catégorie : gestion_risque_entree*
