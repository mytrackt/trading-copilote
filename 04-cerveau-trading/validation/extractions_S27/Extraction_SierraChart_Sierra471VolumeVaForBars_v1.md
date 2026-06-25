# Extraction SierraChart — Volume Value Area for Bars
**Source :** `bundles/sierrachart/sierra_471_volume_va_for_bars.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9391 → D9400 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=471
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : VVAH/VVAL = bornes de la Value Area par barre — zones de support/résistance basées sur le volume pour identifier les niveaux d'entrée/sortie sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9391 — Définition VVAH/VVAL : bornes haute et basse de la Value Area par barre
🟢 **FAIT VÉRIFIÉ** (Source : sierra_471_volume_va_for_bars.md) : L'étude Volume Value Area for Bars calcule et affiche deux niveaux pour chaque barre : Volume Value Area High (VVAH) et Volume Value Area Low (VVAL). Ces niveaux délimitent la zone de prix dans laquelle s'est concentré un pourcentage défini du volume total de la barre.
**TRADEX-AI C2** : VVAH et VVAL sont des niveaux de support/résistance intra-barre basés sur le volume réel transacté — fondement de l'analyse Market Profile / Volume Profile. Utilisables comme niveaux de référence pour les ordres dans TRADEX-AI (Cercle C2).
*Catégorie : structure_marche*

### D9392 — Paramètre Value Area Percentage : défaut 70%
🟢 **FAIT VÉRIFIÉ** (Source : sierra_471_volume_va_for_bars.md) : L'input `Value Area Percentage` spécifie le pourcentage du volume total de la barre qui doit être inclus dans la Value Area. La valeur par défaut est 70%.
**TRADEX-AI C2** : Le seuil de 70% est la convention standard du Market Profile (théorie de Steidlmayer). Pour TRADEX-AI, conserver 70% comme valeur de référence. Un seuil plus élevé (80-85%) produit une Value Area plus large — utile pour les marchés très volatils comme CL.
*Catégorie : structure_marche*

### D9393 — Représentation visuelle : carrés décalés à gauche (left offset squares)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_471_volume_va_for_bars.md) : Par défaut, VVAH et VVAL sont représentés comme des "left offset squares" (carrés décalés à gauche de la barre). Ce format permet de voir les bornes sans masquer l'action des prix de la barre.
**TRADEX-AI C2** : L'affichage en carrés décalés à gauche est non-intrusif — il ne perturbe pas la lecture visuelle des barres de prix Belkhayate. Compatible avec un affichage simultané des indicateurs C1 (BGC, Direction, Energie, Pivots).
*Catégorie : structure_marche*

### D9394 — Dépendance tick size : paramètre critique pour la précision du calcul
🟢 **FAIT VÉRIFIÉ** (Source : sierra_471_volume_va_for_bars.md) : La documentation Sierra Chart avertit explicitement : le Tick Size doit être configuré correctement dans Chart >> Chart Settings. Un Tick Size incorrect peut causer des temps de chargement très longs des données du chart et des inexactitudes dans l'étude.
**TRADEX-AI C2** : Avertissement critique pour TRADEX-AI — contrairement au Bar Delta (affichage seulement), une mauvaise configuration du Tick Size sur cette étude impacte directement la précision des niveaux VVAH/VVAL calculés. Tick Size GC = 0.10, HG = 0.0005, CL = 0.01, ZW = 0.25 doivent être vérifiés avant tout usage.
*Catégorie : structure_marche*

### D9395 — Méthode de calcul : référence au TPO Profile Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_471_volume_va_for_bars.md) : La documentation Sierra Chart précise explicitement que la méthode de calcul de la Value Area est décrite dans la section "Calculations" de la page de l'étude "TPO Profile Chart" — les deux études partagent le même algorithme de calcul de la Value Area.
**TRADEX-AI C2** : La Value Area de cette étude suit la même méthode que le TPO Profile Chart — elle additionne le volume par niveau de prix (par pas de tick) depuis le Point of Control (POC) vers le haut et vers le bas jusqu'à atteindre le pourcentage cible (70%).
*Catégorie : structure_marche*

### D9396 — Point of Control implicite : niveau de prix à plus grand volume
🟡 **SYNTHÈSE** (Source : sierra_471_volume_va_for_bars.md) : Bien que non mentionné explicitement dans cette page, le calcul de la Value Area part toujours du Point of Control (POC) — le niveau de prix avec le plus grand volume — et étend la zone vers le haut et vers le bas jusqu'à atteindre le seuil de pourcentage défini.
**TRADEX-AI C2** : Le POC est la zone de prix à "fair value" selon la théorie Market Profile — le marché a tendance à revenir au POC après s'en être éloigné. Pour TRADEX-AI, un prix au-dessus du VVAH ou en-dessous du VVAL indique une extension hors value area — signal de potentiel retournement C2.
*Catégorie : structure_marche*

### D9397 — Usage comme support/résistance dynamique par barre
🟡 **SYNTHÈSE** (Source : sierra_471_volume_va_for_bars.md) : VVAH et VVAL sont calculés pour chaque barre individuellement, ce qui signifie qu'ils varient d'une barre à l'autre. Ils ne constituent pas des niveaux statiques mais des niveaux dynamiques reflétant la distribution du volume pour chaque période.
**TRADEX-AI C2** : Distinction importante : les VVAH/VVAL par barre (cette étude) sont différents des VVAH/VVAL de session (Volume Profile de session). Pour TRADEX-AI, les niveaux par barre servent à identifier le contexte d'une barre spécifique, tandis que les niveaux de session (à intégrer séparément) servent comme zones de support/résistance majeurs.
*Catégorie : structure_marche*

### D9398 — Condition préalable : nécessite données volume par niveau de prix
🟡 **SYNTHÈSE** (Source : sierra_471_volume_va_for_bars.md) : Le calcul de la Value Area requiert des données de volume détaillées par niveau de prix (volume at price), et non simplement le volume total de la barre. Ces données nécessitent un feed de données tick-by-tick ou une connexion à un service de données order flow.
**TRADEX-AI C2** : Pour TRADEX-AI, cela signifie que le Volume Value Area for Bars ne peut être calculé qu'avec un feed Rithmic tick-by-tick (disponible via ATAS Pro). Un feed daily OHLCV ne suffit pas. À confirmer lors de la Phase C avec le collecteur NT8/ATAS.
*Catégorie : volume_liquidite*

### D9399 — Interprétation trading : prix hors value area = opportunité
🟡 **SYNTHÈSE** (Source : sierra_471_volume_va_for_bars.md) : Dans la théorie Market Profile (non explicitée dans la page Sierra Chart mais fondement académique de la Value Area), un prix qui s'éloigne de la Value Area sans volume suffisant pour maintenir ce niveau tend à retourner dans la Value Area.
**TRADEX-AI C2** : Règle opérationnelle potentielle pour TRADEX-AI : si le prix de GC clôture au-dessus du VVAH de la barre précédente avec un signal Belkhayate C1 aligné, cela constitue une confirmation C2 de breakout haussier. À valider en Phase C.
*Catégorie : gestion_risque_entree*

### D9400 — Complémentarité avec Bar Delta (ID 444)
🟡 **SYNTHÈSE** (Source : sierra_471_volume_va_for_bars.md) : Volume Value Area for Bars (ID 471) et Bar Delta Below Bar (ID 444) sont complémentaires : la Value Area indique où se concentre le volume (niveaux de prix), tandis que le Delta indique la direction de l'agressivité (acheteurs vs vendeurs).
**TRADEX-AI C2** : Combinaison puissante pour C2 : un prix au VVAH avec un delta fortement positif = acheteurs agressifs à la borne haute de la value area = confirmation de breakout. Un prix au VVAL avec un delta fortement négatif = vendeurs agressifs à la borne basse = confirmation de breakdown.
*Catégorie : volume_liquidite*
