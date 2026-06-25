# Extraction AdamGrimes — Chart of the Day: Nested Pullback in Crude Oil
**Source :** `bundles/adamgrimes/chart_of_the_day_nested_pullback_in_crude_oil.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5511 → D5522 · **Page :** https://www.adamhgrimes.com/chart-of-the-day-nested-pullback-in-crude-oil/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : DIRECTEMENT sur CL (Pétrole WTI — actif TRADING Catégorie 1). Pattern Nested Pullback sur CL avec contexte multi-timeframe et gestion du gap overnight.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D5511 — Nested Pullback : définition et caractéristiques (CL direct)
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Le "Nested Pullback" (terme Grimes, "The Art & Science of Technical Analysis") est une petite consolidation sur timeframe inférieur qui se forme dans la résolution d'un pattern directionnel sur timeframe supérieur. En l'espèce, CL montre une petite consolidation daily pointant à la baisse, elle-même imbriquée dans une casse de trendline sur le weekly.
**TRADEX-AI C1** : Sur CL (Pétrole — actif TRADING), détecter les consolidations daily qui s'inscrivent dans un contexte directionnel weekly. Ce pattern multi-timeframe est prioritaire pour les entrées à fort R/R.
*Catégorie : configuration*

### D5512 — Nested Pullback : caractéristiques R/R exceptionnelles
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Grimes qualifie les Nested Pullbacks de trades offrant "des caractéristiques de R/R exceptionnelles avec une forte probabilité de résolution profitable." Le fait d'entrer sur le timeframe inférieur dans le contexte du timeframe supérieur comprime le risque et amplifie le potentiel.
**TRADEX-AI C1** : Le score /10 TRADEX doit bonifier les signaux Nested Pullback sur CL/GC/HG/ZW. R/R attendu > 1:2 (critère éliminatoire TRADEX si inférieur). Ce pattern peut constituer un bonus de score dans la grille.
*Catégorie : gestion_risque_entree*

### D5513 — CL : casse de trendline weekly → contexte baissier dominant
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Le Pétrole (CL) consolide à la baisse après une casse de trendline sur le weekly. Le contexte directionnel hebdomadaire est baissier. La consolidation daily s'inscrit dans ce contexte dominant.
**TRADEX-AI C1** : Sur CL, vérifier l'alignement weekly avant tout signal daily. Une casse de trendline sur weekly impose un biais directionnel à maintenir jusqu'à invalidation. Intégrer dans la logique de détection multi-timeframe.
*Catégorie : structure_marche*

### D5514 — Nested Pullback : lisibilité plus claire sur weekly que sur daily
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Grimes précise que le pattern Nested Pullback est "peut-être plus clair sur le graphique weekly" que sur le daily. La lecture multi-timeframe est indispensable pour identifier correctement le pattern.
**TRADEX-AI C1** : Le moteur TRADEX doit analyser CL sur minimum 2 timeframes (weekly + daily) avant de valider un signal. Le contexte supérieur prime sur le signal inférieur.
*Catégorie : configuration*

### D5515 — Utilisation USO comme proxy de CL pour éviter le futures gap overnight
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Grimes note que "USO peut être utilisé pour exécuter ce trade plutôt que les futures, mais il faut être attentif au risque de gap overnight." L'ETF USO est un proxy de CL pour les comptes qui ne tradent pas les futures CME.
**TRADEX-AI C4** : TRADEX-AI utilise CL directement via NinjaTrader 8 (futures CME). Le risque de gap overnight sur CL futures est réel et doit être intégré dans la gestion de position (stop placement au-delà des gaps probables, ou sortie avant clôture session).
*Catégorie : gestion_risque_entree*

### D5516 — Gap overnight CL : risque spécifique à gérer activement
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Le gap overnight est un risque explicitement mentionné par Grimes pour CL. Ce risque doit être pris en compte dans la gestion de position, notamment pour les positions conservées sur plusieurs sessions.
**TRADEX-AI C1** : En mode Auto sur CL, le moteur doit appliquer une règle de gestion overnight : soit réduire la position avant fermeture session principale, soit élargir le stop pour absorber un gap potentiel. Documenter dans risk_manager.py.
*Catégorie : gestion_position_active*

### D5517 — Nested Pullback : entrée sur timeframe inférieur dans contexte directionnel supérieur
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : La logique d'entrée du Nested Pullback consiste à entrer sur le timeframe inférieur (daily dans l'exemple CL) pendant que le timeframe supérieur (weekly) donne la direction. Cette combinaison comprime le drawdown potentiel car on entre dans le sens du mouvement supérieur.
**TRADEX-AI C1** : Pattern d'entrée à intégrer dans la grille de détection TRADEX. Sur CL/GC/HG/ZW : signal daily dans le sens du contexte weekly = Nested Pullback potentiel. Vérification croisée weekly obligatoire avant validation.
*Catégorie : configuration*

### D5518 — Référence livre Art & Science pour le Nested Pullback
🔵 **ÉCOLE** (Source : chart_of_the_day_nested_pullback_in_crude_oil.md) : Le terme "Nested Pullback" et son usage sont documentés dans "The Art & Science of Technical Analysis" d'Adam Grimes. Source primaire avec statistiques et exemples supplémentaires.
**TRADEX-AI C1** : Source KB à référencer pour le pattern Nested Pullback. Les statistiques de réussite issues du livre doivent alimenter le scoring /10 de ce pattern.
*Catégorie : configuration*
