# Extraction StockCharts — TA 101 Part 13 (Head and Shoulders Reversal)
**Source :** `bundles/stockcharts/ta_101_part_13.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D4091 → D4110 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-13.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Head & Shoulders est le pattern de retournement majeur — directement applicable à GC/HG/CL/ZW pour détecter les inversions de tendance importantes, notamment en corrélation avec ES/DX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Illustration of Head and Shoulders Top Reversal Pattern | Head and Shoulders | D4091 |
| image_02 | Illustration of Head and Shoulders Bottom Reversal Pattern | Head and Shoulders | D4097 |

## DÉCISIONS

### D4091 — Head & Shoulders Top : structure de base
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md, image_01) : Le Head & Shoulders Top pattern se forme dans un uptrend et sa complétion marque un retournement de tendance. Il contient trois pics successifs : le pic central (tête) est le plus haut, les deux pics extérieurs (épaules) sont plus bas. Les creux réactifs de chaque pic peuvent être reliés pour former une ligne de support appelée neckline. Le pattern de retournement top est complété quand le prix casse sous la neckline.
**TRADEX-AI C1** : Surveiller la formation H&S Top sur GC lors d'un sommet de tendance haussière prolongée — la cassure sous la neckline = signal VENDRE potentiel fort.
*Catégorie : structure_marche*

### D4092 — Head & Shoulders Top : asymétrie des épaules autorisée
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "While it is preferable that the left and right shoulders be symmetrical, it is not an absolute requirement. They can be different widths as well as different heights."
**TRADEX-AI C1** : Ne pas rejeter un H&S sur HG/CL parce que les épaules ne sont pas parfaitement symétriques — la structure globale (3 pics + neckline) prime sur la symétrie exacte.
*Catégorie : structure_marche*

### D4093 — Head & Shoulders Top : le point de bascule psychologique
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Up until the point where prices move back below the level of the left shoulder, things look like a normal, ongoing uptrend. It is only when the left shoulder's price level is violated that the bulls become fearful and the bears start to smell blood."
**TRADEX-AI C1/C5** : Alerte critique sur GC/HG : si le prix, après avoir formé ce qui ressemble à une tête, revient sous le niveau de l'épaule gauche, c'est le signe que les bulls perdent confiance — augmenter la vigilance baissière (C5 sentiment retournement).
*Catégorie : psychologie*

### D4094 — Head & Shoulders Top : formation de l'épaule droite
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "The right shoulder forms as the bulls try to reestablish the uptrend and then fail - usually because many of the more skittish investors will take profits at that point."
🟡 **SYNTHÈSE** : L'épaule droite représente une tentative haussière faible — les vendeurs/profit-takers dominent les acheteurs restants.
**TRADEX-AI C1/C3** : Lors de la formation de l'épaule droite sur GC, surveiller les COT data (C3) — si les commerciaux (smart money) réduisent leurs longs simultanément, confirmation institutionnelle du retournement.
*Catégorie : psychologie*

### D4095 — Head & Shoulders Top : rôle du volume pendant la formation
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Buying volume (volume on up days) will slowly translate into selling volume (volume on down days) as the pattern develops. This is seen when volume that previously expanded on rallies begins to expand on declines and contract on rallies."
**TRADEX-AI C2** : Sur ATAS, surveiller la transition progressive du delta volume positif (acheteurs dominants) vers delta négatif (vendeurs dominants) pendant la formation H&S sur GC/HG — cette transition volume confirme le changement de sentiment avant la cassure neckline.
*Catégorie : volume_liquidite*

### D4096 — H&S Top : volume confirme le retournement
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Volume plays an important role in confirmation" du H&S Top. Le volume évolue progressivement de volume d'achat vers volume de vente au fur et à mesure que le pattern se développe.
**TRADEX-AI C2** : Règle de confirmation obligatoire pour H&S sur TRADEX : sans transition du volume d'achat vers volume de vente, le H&S n'est pas confirmé — traiter comme pattern incertain, ne pas exécuter en mode Auto.
*Catégorie : gestion_risque_entree*

### D4097 — Head & Shoulders Bottom (Inverse) : structure miroir
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md, image_02) : Le H&S Bottom reversal pattern est exactement l'inverse du Top reversal pattern, avec le volume agissant comme confirmation.
**TRADEX-AI C1** : Surveiller H&S Bottom sur GC/ZW lors de creux importants — la cassure au-dessus de la neckline d'un H&S Inverse = signal ACHETER fort, particulièrement après une tendance baissière prolongée.
*Catégorie : structure_marche*

### D4098 — H&S Bottom : volume confirme le retournement haussier
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Volume that was previously expanding on declines begins to expand on rallies and contract on declines as the trend reversal develops." Les traders remarquent un volume de vente plus léger sur les baisses et un volume d'achat plus lourd sur les hausses.
**TRADEX-AI C2** : Sur ATAS pour GC/CL : si pendant un H&S Bottom le delta devient progressivement positif sur les rallyes et négatif sur les baisses, la confirmation de retournement haussier est en cours — préparer signal ACHETER.
*Catégorie : volume_liquidite*

### D4099 — H&S Bottom : acheteurs remarqués par le marché
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "This kind of price and volume action is quickly noticed by the market which results in additional buying volume supporting the trend reversal." La détection du retournement génère de nouveaux acheteurs qui amplifient le signal.
**TRADEX-AI C5** : L'auto-renforcement du signal H&S Bottom (acheteurs attirant plus d'acheteurs) est un phénomène de momentum psychologique — dans TRADEX, augmenter le score confiance si le prix franchit la neckline avec un accélération du volume.
*Catégorie : psychologie*

### D4100 — H&S Top : multiples épaules gauches possibles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Sometimes several left shoulders will form before a true head appears." Le pattern peut avoir une phase préliminaire avec plusieurs épaules gauches.
**TRADEX-AI C1** : Sur les marchés futures (GC, HG), ne pas précipiter l'identification du H&S — attendre la formation complète (tête + épaule droite + retour proche neckline) avant de signaler le pattern.
*Catégorie : timing*

### D4101 — H&S Top : multiples épaules droites possibles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Sometimes several right shoulders appear before a true neckline break occurs." La cassure de neckline peut prendre du temps et plusieurs tentatives de rally peuvent échouer.
**TRADEX-AI C1** : Règle de patience pour TRADEX : ne pas entrer en VENDRE anticipé sur un H&S incomplet sur CL/HG — attendre la cassure effective de la neckline pour valider le signal.
*Catégorie : gestion_risque_entree*

### D4102 — H&S Top : objectif de prix minimum après cassure neckline
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "When a neckline break occurs, the stock will often fall at least as much as the distance from the neckline to the top of the head." La mesure de l'objectif de cours = distance tête-neckline projetée depuis le point de cassure.
**TRADEX-AI C1** : Règle d'objectif de prix pour TRADEX — après cassure neckline H&S sur GC, calculer l'objectif minimum = prix cassure - (prix tête - prix neckline au niveau de la tête). Utiliser pour le calcul R/R (seuil ≥ 1:2).
*Catégorie : gestion_position_active*

### D4103 — Autres patterns de retournement : variations du H&S
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Here's a trade secret - most of those [other reversal patterns] are just variations of the Head and Shoulders reversal pattern that didn't form 'perfectly' for some reason. For example, the Triple Top is a Head and Shoulders pattern where the head doesn't go above the left shoulder."
**TRADEX-AI C1** : Simplification opérationnelle validée par la source : Triple Top, Double Top, Rounding Bottom sont des variantes dégradées du H&S — les traiter avec le même framework d'analyse que le H&S dans TRADEX.
*Catégorie : structure_marche*

### D4104 — Reversal Patterns : focus sur le changement fear/greed, pas sur le nom
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "The key point here is this - don't worry about what type of reversal is occurring. Knowing it's a Triple Top instead of a Head & Shoulders won't make you more money. Focus on what the chart is telling you—the fear/greed ratio is changing—and react accordingly."
**TRADEX-AI C5** : Règle pragmatique pour TRADEX — l'important est de détecter le changement de sentiment (peur/avidité) via C5, pas de classifier parfaitement le pattern. Réagir au signal réel, pas à l'étiquette.
*Catégorie : psychologie*

### D4105 — H&S : pattern de retournement le plus commun
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "One of the most common reversal patterns is the Head and Shoulders pattern." C'est le pattern de retournement de référence dans l'analyse technique.
**TRADEX-AI C1** : Dans le module de détection de patterns TRADEX, le H&S doit avoir la priorité de traitement parmi les patterns de retournement — haute fréquence d'occurrence sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4106 — H&S Top : se forme dans un uptrend, complètion = retournement
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "This pattern forms in an uptrend and its completion marks a trend reversal." Le contexte d'uptrend préalable est une condition nécessaire pour le H&S Top.
**TRADEX-AI C1** : Condition préalable obligatoire pour identifier un H&S Top valide sur GC/CL : il doit y avoir un uptrend établi avant la formation — un H&S en marché latéral n'est pas un H&S Top valide.
*Catégorie : structure_marche*

### D4107 — Neckline : rôle de support dans le H&S
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : La neckline est formée en reliant les creux réactifs de chaque pic. Elle constitue une ligne de support que le prix doit franchir à la baisse pour compléter le pattern Top.
**TRADEX-AI C1** : La neckline d'un H&S sur GC/HG est le niveau de support clé à surveiller — placer une alerte prix automatique à ce niveau dans NT8 pour détecter la cassure en temps réel.
*Catégorie : gestion_risque_entree*

### D4108 — H&S Bottom : volume d'achat croissant sur les rallyes
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : "Traders begin noticing lighter selling volume on the declines and heavier buying volume on the rallies." Ce comportement volume est le signal clé de confirmation du H&S Bottom.
**TRADEX-AI C2** : Checklist ATAS pour H&S Bottom sur GC/ZW : (1) Volume vente décroissant sur les baisses successives, (2) Volume achat croissant sur les rallyes successifs — les deux ensemble = confirmation forte.
*Catégorie : volume_liquidite*

### D4109 — H&S : le pattern le plus "infamous" de l'AT
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : Le titre de la section est "The Infamous Head and Shoulders Reversal Pattern" — qualifié d'"infamous" souligne sa notoriété et son importance dans la communauté des traders techniques.
🟡 **SYNTHÈSE** : Sa notoriété signifie aussi que de nombreux traders le surveillent simultanément — ce qui peut créer des prophéties auto-réalisatrices lors de la cassure neckline.
**TRADEX-AI C5** : L'effet "self-fulfilling prophecy" du H&S amplifie les mouvements de prix à la cassure — sur GC, attendre la confirmation du volume avant d'entrer (risque de faux breakout si beaucoup de traders ont placé des ordres au même niveau).
*Catégorie : psychologie*

### D4110 — Autres patterns de retournement référencés
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_13.md) : La source mentionne explicitement d'autres patterns de retournement catalogués : "rounding bottom, the V-reversal, double tops, triple bottoms, and others" — avec référence au ChartSchool area pour les détails.
**TRADEX-AI C1** : Inventaire des patterns de retournement complémentaires à intégrer dans TRADEX pour GC/HG/CL/ZW : Rounding Bottom (accumulation lente), V-Reversal (retournement brutal), Double Top/Bottom, Triple Top/Bottom — tous traités comme variantes H&S.
*Catégorie : structure_marche*
