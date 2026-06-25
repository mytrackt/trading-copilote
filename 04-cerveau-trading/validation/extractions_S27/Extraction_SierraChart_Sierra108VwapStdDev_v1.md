# Extraction SierraChart — VWAP with Standard Deviation Lines (ID 108)
**Source :** `bundles/sierrachart/sierra_108_vwap_std_dev.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8891 → D8910 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=108
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : VWAP avec bandes d'écart-type — outil d'ancrage prix/volume essentiel pour C1 et C2 sur GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D8891 — VWAP Sierra Chart ID 108 : définition et fondement mathématique
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Le VWAP Sierra Chart (ID 108) calcule le prix moyen pondéré par le volume sur une période paramétrable. Il donne un poids plus élevé aux prix ayant un volume plus important. Le calcul se réinitialise au début de chaque nouvelle période.
**TRADEX-AI C2** : Le VWAP est le référentiel prix/volume institutionnel central — sur GC (Or) et CL (Pétrole), le prix relatif au VWAP journalier indique si les institutionnels achètent ou vendent au-dessus ou en dessous de leur prix moyen de référence (couche C2 + C3).
*Catégorie : volume_liquidite*

### D8892 — VWAP Sierra Chart : paramètre Time Period Type et Time Period Length configurables
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Le VWAP ID 108 dispose des inputs : Time Period Type (Days, Sessions, etc.) et Time Period Length (quantité). Pour un VWAP journalier : Time Period Type = Days, Time Period Length = 1. Le démarrage est déterminé par les Session Times dans Chart >> Chart Settings.
**TRADEX-AI C2** : Configuration opérationnelle pour TRADEX — VWAP journalier sur GC : Time Period Type = Days, Length = 1, Session Times = CME Globex GC (18h00-17h00 ET). La session doit être correctement configurée pour que le VWAP se réinitialise à la bonne heure.
*Catégorie : configuration*

### D8893 — VWAP Sierra Chart : paramètre Base on Underlying Data — précision et cohérence multi-timeframe
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : L'input "Base on Underlying Data" (défaut : No) — quand réglé sur Yes, le calcul utilise les données de tick sous-jacentes plutôt que les barres du chart. Pour la précision maximale et la cohérence entre différents timeframes, il est recommandé de régler sur Yes avec des données tick-by-tick. Quand réglé sur No, les valeurs VWAP seront différentes entre timeframes, ce qui est attendu.
**TRADEX-AI C2** : Règle opérationnelle TRADEX — pour comparer le VWAP sur range bars NT8 vs Sierra Chart, activer "Base on Underlying Data = Yes" dans Sierra Chart avec données tick. Sans cette option, les VWAP de différents timeframes ne sont pas comparables — risque de faux signaux de divergence.
*Catégorie : configuration*

### D8894 — VWAP Sierra Chart : incompatibilité Base on Underlying Data avec barres non-time (Range, Renko, Delta)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : "It is expected for the VWAP values to be different among different chart bar timeframe settings when using Number of Trades, Volume, Range, Reversal, Renko, Delta Volume, Price Change, Point and Figure Bars. This is because there is not a consistent starting time for a bar with these bar types. Enabling Chart >> Chart Settings >> New Bar at Session Start can help with this."
**TRADEX-AI C2** : Contrainte critique — TRADEX-AI utilise des range bars NT8. Sur Sierra Chart avec range bars, le VWAP sera différent du VWAP calculé sur barres temporelles. Activer "New Bar at Session Start" est obligatoire pour aligner le VWAP au début de session et rendre les comparaisons cohérentes entre range bars et barres temporelles.
*Catégorie : configuration*

### D8895 — VWAP Sierra Chart : bandes d'écart-type — calcul et multiplicateurs Band 1 à 4
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Le VWAP ID 108 supporte jusqu'à 4 bandes d'écart-type (Top Band 1-4 / Bottom Band 1-4). Formule : TB_j = VWAP + j*b*Off(X,n) et BB_j = VWAP - j*b*Off(X,n) où b est le multiplicateur (Band # Std. Deviation Multiplier). Les bandes 2, 3, 4 multiplient respectivement par 2b, 3b, 4b l'offset.
**TRADEX-AI C1** : Configuration standard TRADEX pour GC : VWAP + bande 1 (1 SD) + bande 2 (2 SD). Le prix en dehors de la bande 2 SD (environ 95% du temps inclus) indique un mouvement extrême — signal de retour vers le VWAP pertinent pour la méthode Belkhayate (retour à la moyenne).
*Catégorie : indicateurs_tendance*

### D8896 — VWAP Sierra Chart : méthodes de calcul des bandes — 4 options disponibles
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : L'input "Standard Deviation Band Calculation Method" offre 4 options : (1) VWAP Variance : Off = Var(X,n), (2) Standard Deviation : Off = SD(X,n), (3) Fixed Offset : décalage fixe en points, (4) Percentage : pourcentage du VWAP. Pour Fixed Offset, les 4 bandes ont exactement le même décalage. Pour Percentage, le décalage est proportionnel au prix.
**TRADEX-AI C1** : Pour GC (Or) dont le prix absolu fluctue ($1800-$3500), utiliser "Percentage" ou "Standard Deviation" plutôt que "Fixed Offset" — un Fixed Offset serait inadapté car le même nombre de points a une signification différente selon le niveau de prix.
*Catégorie : configuration*

### D8897 — VWAP Sierra Chart : Volume Type configurable — Total, Bid, Ask Volume
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : L'input "Volume Type to Use" propose : Total Volume (défaut), Bid Volume, Ask Volume. Quand Bid Volume ou Ask Volume est sélectionné, "Base on Underlying Data" doit être réglé sur Yes, sinon le Total Volume sera utilisé automatiquement.
**TRADEX-AI C2** : Fonction avancée pour TRADEX — un VWAP calculé sur Bid Volume uniquement mesure la pression vendeuse moyenne pondérée, tandis que le VWAP Ask Volume mesure la pression acheteuse. La divergence entre ces deux VWAP directionnel est un signal d'order flow potentiellement utilisable pour C2.
*Catégorie : volume_liquidite*

### D8898 — VWAP Sierra Chart : paramètre Start Date-Time — VWAP ancré à une date/heure spécifique
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : L'input "Start Date-Time" permet de fixer un point de départ spécifique pour le VWAP. Date ET Heure doivent être spécifiés (pas l'heure seule). Time Period Length et Time Period Type continuent de s'appliquer. Le Start Date-Time réduit la quantité de calculs en commençant à une date précise.
**TRADEX-AI C1** : VWAP ancré utilisable dans TRADEX pour ancrer un VWAP depuis une date clé (ex : depuis un bas majeur de GC, depuis un rapport NFP/FOMC). C'est le "Anchored VWAP" institutionnel — les grandes mains voient souvent le VWAP depuis ces niveaux pivots.
*Catégorie : structure_marche*

### D8899 — VWAP Sierra Chart : outil Draw Anchored VWAP — dessin interactif sur chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Sierra Chart propose l'outil "Draw Anchored VWAP" (Tools >> Draw Anchored VWAP) permettant de cliquer sur une barre du chart pour démarrer un VWAP interactif depuis ce point. La date/heure de la barre cliquée devient le point de départ. Si les données Volume at Price nécessaires ne sont pas chargées, le chart se recharge automatiquement.
**TRADEX-AI C1** : Fonctionnalité opérationnelle directe pour Abdelkrim — en mode Manuel, après un signal TRADEX sur GC, Abdelkrim peut rapidement ancrer un VWAP depuis le dernier point pivot important pour valider la zone d'entrée par rapport au VWAP institutionnel.
*Catégorie : configuration*

### D8900 — VWAP Sierra Chart : modification interactive du VWAP ancré
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Un VWAP ancré dessiné peut être modifié interactivement en activant "Global Settings >> Tool Settings >> Enable Drawn Volume Profiles Selection", puis en cliquant sur le marqueur du VWAP ancré et en le déplaçant. Les lignes VWAP se mettent à jour en temps réel lors du déplacement.
**TRADEX-AI C1** : En mode analyse TRADEX, Abdelkrim peut ajuster dynamiquement le point d'ancrage du VWAP pour tester différents scénarios (ex : VWAP depuis la séance asiatique vs depuis l'ouverture CME) — l'analyse en temps réel est possible sans recharger l'indicateur.
*Catégorie : configuration*

### D8901 — VWAP Sierra Chart : différences VWAP entre charts Historical Daily et Intraday
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Les données d'un chart Historical Daily sont différentes d'un chart Intraday. Même avec "Base on Underlying Data = Yes", le VWAP sera différent entre les deux types. Sur les charts Daily, le volume par barre est plus élevé. Le prix de clôture diffère : Historical Daily utilise le settlement officiel, Intraday utilise le dernier trade.
**TRADEX-AI C2** : Règle technique TRADEX — comparer uniquement des VWAPs calculés sur le même type de chart (Intraday vs Intraday). Pour TRADEX en surveillance 2s, seuls les charts Intraday (range bars NT8) sont pertinents — les VWAPs Historical Daily sont à exclure des signaux temps réel.
*Catégorie : configuration*

### D8902 — VWAP Sierra Chart : paramètre "Ignore Time Period Type and Length" — VWAP sur tout le chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : Quand "Ignore Time Period Type and Length = Yes", le VWAP est calculé depuis la première barre du chart (ou depuis le Start Date-Time si défini), ignorant la périodicité. C'est le VWAP "depuis le début du chart".
**TRADEX-AI C3** : Ce VWAP "depuis l'origine" est le VWAP institutionnel long terme — sur GC, un chart chargé depuis 6 mois avec "Ignore = Yes" donne le prix moyen pondéré par volume sur 6 mois, indicateur utilisé par les grands fonds pour mesurer leur prix d'acquisition moyen. Pertinent C3.
*Catégorie : indicateurs_tendance*

### D8903 — VWAP Sierra Chart : précision tick-by-tick recommandée pour cohérence multi-barres
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : "For the highest accuracy and the same values on different timeframe bars, it is necessary to set the Base on Underlying Data Input to Yes, so that the study uses the underlying data that makes up the bars. It is also necessary to have tick by tick data in the chart data file for the highest accuracy."
**TRADEX-AI C2** : Pour TRADEX sur GC avec range bars et barres temporelles multiples, les données tick-by-tick Rithmic (déjà disponibles via ATAS/Rithmic) doivent être configurées dans Sierra Chart pour le VWAP. Sans tick data, les bandes SD ne sont pas comparables entre timeframes.
*Catégorie : configuration*

### D8904 — VWAP Sierra Chart : variance VWAP — formule de calcul documentée
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : La Variance est calculée comme suit : Var(X,n) = VWAP_Variance sur la période, utilisant le volume pondéré. L'Écart-type SD(X,n) = racine de la Variance. L'offset de la bande j vaut : TB_j = VWAP + j*b*Off et BB_j = VWAP - j*b*Off, avec j = 1, 2, 3, 4.
**TRADEX-AI C1** : La formule confirme que les bandes VWAP SD de Sierra Chart sont des bandes de déviation standard pondérées par le volume — elles sont statistiquement plus robustes que les Bollinger Bands (qui utilisent la SD du prix simple). Pour TRADEX, préférer les bandes VWAP SD aux Bollinger Bands pour les niveaux support/résistance sur GC.
*Catégorie : indicateurs_tendance*

### D8905 — VWAP Sierra Chart : Study Collection pour configuration Draw Anchored VWAP
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : La préconfiguration du Draw Anchored VWAP nécessite : (1) créer une Study Collection avec le VWAP paramétré, (2) la sauvegarder via "Save Single", (3) la référencer dans Global Settings >> Tool Configs >> Draw Anchored VWAP >> TC1-TC24. Jusqu'à 24 configurations (TC1-TC24) sont stockables.
**TRADEX-AI C1** : Procédure opérationnelle Sierra Chart — créer une Study Collection "TRADEX_VWAP_GC" avec les paramètres TRADEX (Daily, SD Method = Standard Deviation, Band multiplier = 2.0) et l'assigner à TC1 pour un accès rapide en mode analyse manuelle.
*Catégorie : configuration*

### D8906 — VWAP Sierra Chart : les bandes SD sur barres différentes peuvent être différentes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : "The Standard Deviation Lines for the Volume Weighted Average Price on different timeframe bars can be different. This is because the Standard Deviation is calculated in part using the chart bar values, and the chart bar values can be significantly different between chart bar timeframes."
**TRADEX-AI C2** : Contrainte documentée — sur TRADEX, si le signal vient d'un chart 5 minutes et que la validation se fait sur range bars, les bandes SD du VWAP seront mathématiquement différentes. Ne pas interpréter une divergence de bandes SD entre timeframes comme un signal — c'est un artefact de calcul.
*Catégorie : configuration*

### D8907 — VWAP Sierra Chart : suppression d'un VWAP ancré — 3 méthodes disponibles
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : 3 méthodes pour supprimer un VWAP ancré dessiné : (1) Analysis >> Studies >> sélectionner le VWAP >> Remove >> OK, (2) Right-click sur la Region Data Line >> Remove >> sélectionner le VWAP spécifique, (3) Erase Chart Drawing (méthodes standard Sierra Chart).
**TRADEX-AI C1** : Information opérationnelle — en analyse manuelle TRADEX, après validation ou invalidation d'un scénario VWAP ancré, Abdelkrim peut effacer rapidement le VWAP via clic droit sur la Region Data Line (méthode la plus rapide en trading live).
*Catégorie : configuration*

### D8908 — VWAP Sierra Chart : Chart Data Type Intraday Only recommandé pour Base on Underlying Data
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : "It is recommended when using this setting [Base on Underlying Data = Yes] that since Intraday charts are required, select Chart >> Chart Settings and select Chart Data Type >> Intraday Chart Only to always ensure the chart is set to use Intraday data."
**TRADEX-AI C2** : Configuration obligatoire pour TRADEX Sierra Chart — tous les charts GC, HG, CL, ZW utilisés pour le VWAP doivent être configurés en "Intraday Chart Only" pour garantir la cohérence des calculs VWAP avec données tick sous-jacentes.
*Catégorie : configuration*

### D8909 — VWAP Sierra Chart : distinction VWAP Rolling vs VWAP with Standard Deviation Lines
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : La documentation mentionne deux études VWAP dans Sierra Chart : "Volume Weighted Average Price - VWAP - Rolling with Standard Deviation Lines" et "Volume Weighted Average Price - VWAP - with Standard Deviation Lines" (ID 108). Ces deux études sont distinctes dans le catalogue.
**TRADEX-AI C2** : TRADEX doit utiliser le VWAP ID 108 (with Standard Deviation Lines) pour les bandes SD. Le VWAP Rolling est une variante différente avec comportement de rolling window — à ne pas confondre avec le VWAP standard journalier (ID 108) recommandé pour TRADEX.
*Catégorie : configuration*

### D8910 — VWAP Sierra Chart : incompatibilité avec TPO Profile Charts
🟢 **FAIT VÉRIFIÉ** (Source : sierra_108_vwap_std_dev.md) : "You cannot use the Draw Anchored VWAP tool with TPO Profile Charts. There is no support for this."
**TRADEX-AI C2** : Contrainte Sierra Chart — si TRADEX utilise des TPO Profile Charts pour l'analyse C2 (Market Profile), le Draw Anchored VWAP interactif ne sera pas disponible sur ces charts. Le VWAP ancré doit être ajouté manuellement via Analysis >> Studies sur les TPO charts, pas via l'outil Draw.
*Catégorie : configuration*
