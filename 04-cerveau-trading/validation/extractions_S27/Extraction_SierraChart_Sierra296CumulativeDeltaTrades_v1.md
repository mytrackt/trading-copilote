# Extraction SierraChart — Cumulative Delta Bars - Trades (ID 296)
**Source :** `bundles/sierrachart/sierra_296_cumulative_delta_trades.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9171 → D9190 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=296
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Mesure l'agressivité des acheteurs vs vendeurs (trades Ask vs Bid) de façon cumulative — indicateur order flow clé pour le cercle C2 Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9171 — Définition Cumulative Delta Bars - Trades
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Cumulative Delta Bars - Trades = somme cumulée de la différence entre le nombre de trades à l'Ask et le nombre de trades à la Bid, affichée sous forme de chandeliers High-Low. Différent du Cumulative Delta basé sur le volume (quantité) — ici c'est le NOMBRE de trades.
**TRADEX-AI C2** : Distinction critique : cet indicateur mesure le NOMBRE de transactions, non le volume de contrats. Un grand nombre de petits trades Ask = acheteurs agressifs mais pas nécessairement volume institutionnel. À combiner avec Volume Delta (ATAS) pour distinguer retail vs institutionnel dans le cercle C2.
*Catégorie : volume_liquidite*

### D9172 — Calcul : DifferenceHigh et DifferenceLow par barre
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Pour chaque barre, Sierra Chart maintient le MAXIMUM (DifferenceHigh) et le MINIMUM (DifferenceLow) de la différence Ask_trades − Bid_trades calculée en tick-by-tick. Ces deux valeurs forment le High et le Low du chandelier CDB.
**TRADEX-AI C2** : Le chandelier CDB a donc une mèche haute (DifferenceHigh) et basse (DifferenceLow) qui montrent l'étendue de l'agressivité dans la barre. Une grande mèche basse sur une barre haussière = tentative de pression baissière rejetée → signal bullish. Pertinent pour la méthode Belkhayate (structure des bougies).
*Catégorie : volume_liquidite*

### D9173 — Construction du chandelier CDB : Open, High, Low, Close
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : 
- CDB Open = CDB Close de la barre précédente (ou 0 si première barre / reset journée)
- CDB High = CDB Close précédent + DifferenceHigh
- CDB Low = CDB Close précédent + DifferenceLow
- CDB Close = CDB Close précédent + (AskTrades − BidTrades) de la barre principale
**TRADEX-AI C2** : La construction en chandeliers cumulatifs permet de lire les CDB avec les mêmes outils d'analyse que les prix (supports/résistances, patterns bougies). Dans TRADEX-AI, une divergence entre le prix Close et le CDB Close (prix monte, delta baisse) = avertissement de faiblesse cachée → signal de vigilance.
*Catégorie : volume_liquidite*

### D9174 — Input "Reset at Start of Trading Day"
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Quand activé (Yes), le calcul cumulatif est remis à zéro au début de chaque session de trading. L'heure de début est déterminée par les Session Times dans Chart Settings (Start Time, ou Evening Start Time si session du soir activée).
**TRADEX-AI C2** : Pour les futures (GC, HG, CL, ZW) avec sessions overnight, choisir la session appropriée. Reset = Yes recommandé pour l'analyse intraday : compare l'agressivité de la journée en cours uniquement. Reset = No pour analyse multi-sessions (contexte plus long).
*Catégorie : configuration*

### D9175 — Input "Reset at Both Session Start Times"
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Quand activé, implique Reset at Start of Trading Day = Yes ET ajoute un second reset au Evening Start Time si la session du soir est activée. Deux resets par jour au lieu d'un.
**TRADEX-AI C2** : Sur GC (Or), qui trade quasi 24h, deux resets (session jour + session nuit) permettent d'analyser séparément l'agressivité de la session asiatique et de la session américaine. Pertinent pour détecter si la pression directionnelle vient d'Asia vs US traders — information macro C4.
*Catégorie : configuration*

### D9176 — Exigence tick-by-tick data pour précision
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : "Important Note : In order for the study to provide an accurate result there must be tick by tick data in the Intraday chart data file. Otherwise, the results of this study will not be accurate." — citation directe de la documentation Sierra Chart.
**TRADEX-AI C2** : Condition OBLIGATOIRE pour utiliser cet indicateur dans TRADEX-AI : le feed Rithmic via ATAS doit fournir des données tick-by-tick. Sans cela, le Cumulative Delta Trades est inexact. À vérifier dans la configuration ATAS avant activation du cercle C2 dans le moteur Python. Staleness monitor doit valider la présence de tick data.
*Catégorie : volume_liquidite*

### D9177 — Affichage en chandeliers High-Low (CandleStick)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Le Cumulative Delta Bars - Trades est affiché sous forme de chandeliers High-Low, permettant l'utilisation des Drawing Tools Sierra Chart directement sur le graphique CDB (supports, résistances, trendlines).
**TRADEX-AI C2** : La compatibilité avec les Drawing Tools permet à Abdelkrim de tracer des supports/résistances sur le delta cumulatif, pas seulement sur le prix. Dans le mode Manuel TRADEX-AI, l'affichage CDB comme chandelier dans l'interface React facilitera la lecture visuelle de la pression directionnelle.
*Catégorie : volume_liquidite*

### D9178 — Companion study : Number of Trades-Ask
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Sierra Chart mentionne que le study "Number of Trades-Ask" peut être ajouté au chart pour afficher le nombre de trades à l'Ask par barre séparément.
**TRADEX-AI C2** : En combinant CDB (tendance cumulative) + Number of Trades-Ask (agressivité instantanée Ask) dans ATAS, TRADEX-AI peut détecter les pics d'agressivité acheteur qui précèdent les breakouts. Signal composite C2 : CDB trending haussier + spike Trades-Ask = confirmation momentum institutionnel.
*Catégorie : volume_liquidite*

### D9179 — Companion study : Number of Trades-Bid
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : Le study "Number of Trades-Bid" permet d'afficher le nombre de trades à la Bid par barre, complémentaire au CDB.
**TRADEX-AI C2** : Ratio Trades-Ask / Trades-Bid > 1,5 sur plusieurs barres consécutives = dominance acheteurs significative. Ce ratio peut être calculé dans le moteur Python TRADEX-AI comme signal C2 booléen (ask_dominance = True/False) intégrable dans la grille /10.
*Catégorie : volume_liquidite*

### D9180 — Ajustement automatique de l'Open si hors range High-Low
🟢 **FAIT VÉRIFIÉ** (Source : sierra_296_cumulative_delta_trades.md) : "The Open is adjusted to be within the range of the High and Low of the Cumulative Delta chart bar at the same index if it is out of that range." — le CDB Open peut ne pas être exactement 0 en début de session si ajustement nécessaire.
**TRADEX-AI C2** : Détail technique à gérer dans la lecture des données CDB : le Open du premier chandelier de la journée peut ne pas être à 0 même avec Reset activé. Le code data_reader.py doit lire le Close (pas l'Open) pour l'interprétation directionnelle du CDB.
*Catégorie : configuration*

### D9181 — Différence CDB-Trades vs CDB-Volume
🟡 **SYNTHÈSE** (Source : sierra_296_cumulative_delta_trades.md) : CDB-Trades mesure l'ACTIVITÉ (nombre de transactions), CDB-Volume mesure la TAILLE (quantité de contrats). Un marché avec de nombreux petits trades à l'Ask peut avoir un CDB-Trades haussier mais un CDB-Volume neutre si les trades Bid sont peu nombreux mais gros.
**TRADEX-AI C2** : Utiliser CDB-Trades + CDB-Volume en parallèle dans ATAS. Divergence (Trades haussier mais Volume neutre) = petits traders agressifs mais gros joueurs absents → signal moins fiable. Convergence (les deux haussiers) = conviction institutionnelle → signal C2 fort pour la grille /10.
*Catégorie : volume_liquidite*

### D9182 — Résolution des divergences CDB : lien fourni
🔵 **ÉCOLE** (Source : sierra_296_cumulative_delta_trades.md) : Sierra Chart référence "Resolving Cumulative Delta Bars Differences" comme ressource dédiée aux cas où le CDB affiche des valeurs inattendues ou incohérentes.
**TRADEX-AI C2** : En cas d'anomalie CDB dans le feed ATAS/Rithmic, consulter cette ressource Sierra Chart avant d'investiguer dans le code TRADEX-AI. Les incohérences viennent souvent du feed (tick data manquants) plutôt que du calcul. La vérification feed doit être intégrée dans le circuit_breaker.py (CB_ATAS).
*Catégorie : configuration*

### D9183 — Pertinence CDB pour GC (Or) : détection absorption institutionnelle
🟡 **SYNTHÈSE** (Source : sierra_296_cumulative_delta_trades.md) : Sur GC (Or), les institutionnels absorbent souvent les trades de vente à des niveaux de support clé — le CDB-Trades reste stable ou monte même si le prix corrige légèrement.
**TRADEX-AI C2** : Pattern d'absorption : prix en baisse + CDB-Trades en hausse = vendeurs liquidés par acheteurs institutionnels = support fort. Dans la grille /10 TRADEX-AI, ce pattern C2 peut valoir +1 point pour signal ACHAT si le prix est proche d'un pivot Belkhayate C1.
*Catégorie : structure_marche*
