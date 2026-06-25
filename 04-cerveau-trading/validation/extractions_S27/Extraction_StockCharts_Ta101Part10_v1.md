# Extraction StockCharts — TA 101 Part 10
**Source :** `bundles/stockcharts/ta_101_part_10.md` (HTTP 200) + 1 image certifiée
**Méthode images :** double ancrage · 1/1 certifiées · 0 à vérifier
**Décisions :** D4031 → D4050 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-10
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Confirmation par le volume (expansion en tendance, contraction en correction) — règle fondamentale pour valider les signaux sur GC/HG/CL/ZW et confirmer les tendances avec l'Order Flow (C2).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Volume Confirmation | Volume Confirmation | D4031 |

## DÉCISIONS

### D4031 — Confirmation volume en uptrend : le volume s'expande sur les hausses et se contracte sur les replis
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md, image_01.png) : Dans une tendance haussière, le volume doit s'expandre lorsque les prix montent et se contracter lorsque les prix se replient. Tant que ce schéma continue, le volume confirme l'uptrend.
**TRADEX-AI C2** : Règle de confirmation volume pour GC/CL/HG/ZW — un signal haussier Belkhayate (C1) est renforcé si l'Order Flow (C2 ATAS) montre une expansion de volume sur les bougies haussières.
*Catégorie : volume_liquidite*

### D4032 — Confirmation volume en downtrend : le volume s'expande sur les baisses et se contracte sur les rallies
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md) : La règle opposée s'applique pour les tendances baissières. Le volume doit s'expandre lorsque les prix baissent et se contracter lors des rallies pour confirmer le downtrend.
**TRADEX-AI C2** : Règle symétrique — un signal baissier Belkhayate est renforcé si ATAS montre une expansion de volume sur les bougies baissières et une contraction sur les rebonds de GC/CL/HG/ZW.
*Catégorie : volume_liquidite*

### D4033 — Divergence négative : nouveau plus-haut sur volume en baisse = pression acheteur s'amenuise
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md) : Des divergences négatives peuvent se produire si de nouveaux plus-hauts de prix lors d'une uptrend se font sur un volume déclinant. Ce type d'activité de volume indique une diminution de la pression acheteuse.
**TRADEX-AI C2** : Signal d'alerte pour GC/HG/CL/ZW — si le prix fait un nouveau plus-haut mais que le delta ATAS (C2) est négatif ou en baisse, réduire la confiance du signal haussier. Potentiel de retournement.
*Catégorie : volume_liquidite*

### D4034 — Si le volume s'expande sur les replis après une divergence négative → risque de consolidation ou retournement baissier
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md) : Si le volume commence également à augmenter lors des replis de prix (après une divergence négative sur les hauts), les prix peuvent commencer à se consolider ou à se retourner en downtrend.
**TRADEX-AI C2** : Double alerte baissière : divergence négative prix/volume sur les hauts + expansion du volume sur les replis = signal de retournement potentiel sur GC/CL. Réduire exposition longs.
*Catégorie : volume_liquidite*

### D4035 — Divergence positive : nouveau plus-bas sur volume qui se contracte = pression vendeuse s'amenuise
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md) : Le même concept est vrai pour les divergences positives dans les downtrends. Si le volume commence à se contracter sur de nouveaux plus-bas de prix mais s'expande lors des rallies, les prix peuvent commencer à se consolider ou à se retourner en uptrend.
**TRADEX-AI C2** : Signal de retournement haussier potentiel sur GC/CL : contraction de volume sur nouveaux plus-bas + expansion sur rallies = épuisement vendeur → signal d'achat potentiel en confluence avec Belkhayate C1.
*Catégorie : volume_liquidite*

### D4036 — Principe général : volume confirme la tendance quand il s'expande dans le sens de la tendance
🟡 **SYNTHÈSE** (Source : ta_101_part_10.md) : Le principe fondamental est que le volume doit s'expandre dans le sens de la tendance dominante et se contracter contre la tendance. Toute déviation de ce schéma est une alerte (divergence).
**TRADEX-AI C1/C2** : Règle de cohérence C1+C2 dans TRADEX-AI — un signal Belkhayate valide sur GC/HG/CL/ZW doit être accompagné d'un volume conforme (expansion dans le sens du signal) pour obtenir un score maximal.
*Catégorie : volume_liquidite*

### D4037 — Divergence volume/prix : indicateur avancé de changement de tendance
🟡 **SYNTHÈSE** (Source : ta_101_part_10.md) : Les divergences volume/prix (nouveau high/low sur volume divergent) sont des indicateurs avancés préfigurant une potentielle consolidation ou un retournement de tendance.
**TRADEX-AI C2** : Intégration dans le scoring TRADEX : la présence d'une divergence volume/prix sur GC/CL doit réduire le score de confiance du signal (indicateur d'alerte C2) même si C1 Belkhayate reste positif.
*Catégorie : indicateurs_momentum*

### D4038 — Fin de la section tendances et lignes de tendance — Part 11 portera sur les patterns de prix
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_10.md) : Cette partie clôt la section sur les tendances et lignes de tendance. La Part 11 couvrira les patterns de prix fondamentaux qui résultent de deux lignes de tendance simultanées.
⚫ **HYPOTHÈSE PROJET** : La séquence TA 101 Part 1→10 couvre les fondamentaux prix/volume/tendance — base de C1 et C2 de TRADEX-AI.
**TRADEX-AI C1** : Repère éditorial — les bundles TA 101 Part 11+ aborderont les patterns (triangles, drapeaux, etc.) directement actionnables pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4039 — Volume expansion sur upside breakouts : confirmation obligatoire des cassures haussières
🟡 **SYNTHÈSE** (Source : ta_101_part_10.md + symmetrical_triangle.md cross-référence) : Le principe de confirmation de volume est transversal : pour les breakouts haussiers de patterns (triangles, résistances), l'expansion de volume est un critère de validité obligatoire.
**TRADEX-AI C1/C2** : Pour tout signal d'achat TRADEX-AI sur GC/HG/CL/ZW impliquant une cassure de résistance ou d'un pattern, vérifier l'expansion du volume ATAS (C2) — sine qua non pour le signal haussier.
*Catégorie : gestion_risque_entree*

### D4040 — Contraction de volume lors d'une tendance non confirmée = signal d'attente
🟡 **SYNTHÈSE** (Source : ta_101_part_10.md) : Lorsque le volume se contracte dans le sens de la tendance présumée, la tendance n'est pas confirmée par le volume — signal d'attente plutôt que d'action.
**TRADEX-AI C2** : Règle d'inhibition du signal : si l'Order Flow ATAS (C2) montre une contraction de volume dans le sens du signal Belkhayate C1 sur GC/CL, abaisser le score et passer en mode ATTENDRE.
*Catégorie : gestion_risque_entree*
