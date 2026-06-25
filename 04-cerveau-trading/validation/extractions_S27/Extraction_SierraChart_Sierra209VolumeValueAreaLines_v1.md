# Extraction SierraChart — Volume Value Area Lines
**Source :** `bundles/sierrachart/sierra_209_volume_value_area_lines.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9091 → D9110 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=209
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : VVAH, VVAL et VPOC sont des niveaux de référence Volume Profile essentiels pour la structure de marché (C2) — niveaux de support/résistance dynamiques sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9091 — Étude Volume Value Area Lines : VVAH, VVAL, VPOC
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : La study Sierra Chart ID=209 calcule et affiche trois niveaux Volume Profile : Volume Value Area High (VVAH), Volume Value Area Low (VVAL), et Volume Point of Control (VPOC) sur une période de temps configurable.
**TRADEX-AI C2** : Ces trois niveaux constituent les niveaux de structure de marché Volume Profile de référence pour TRADEX-AI. VPOC = prix où le volume est maximal ; VVAH/VVAL = bornes de la zone où 70% du volume s'est échangé.
*Catégorie : structure_marche*

### D9092 — Volume Value Area % : seuil de définition de la zone (défaut 70%)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : L'input `Volume Value Area %` spécifie le pourcentage du volume total inclus dans la Value Area. La valeur par défaut est **70%**. La Value Area est calculée en ajoutant les price levels autour du VPOC jusqu'à atteindre ce pourcentage cumulé.
**TRADEX-AI C2** : Conserver la valeur par défaut de 70% pour TRADEX-AI conformément au standard Market Profile/Volume Profile. Une modification à 68% (±1 écart-type gaussien) peut être testée en Phase C pour GC.
*Catégorie : structure_marche*

### D9093 — Draw Developing Value Area Lines : statique vs dynamique
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : L'input `Draw Developing Value Area Lines` détermine le mode de calcul : si `No` = les lignes VVAH/VVAL/VPOC sont fixes pour toute la période de temps (valeur finale de la période précédente) ; si `Yes` = les lignes se mettent à jour barre par barre (valeur courante évolutive pendant la séance).
**TRADEX-AI C2** : Mode `No` (statique) = VVAH/VVAL/VPOC de la veille projetés sur la séance courante — utile pour des niveaux stables de référence lors de l'entrée en position. Mode `Yes` (developing) = VVAH/VVAL/VPOC évoluant en temps réel — utile pour suivre l'évolution intraday.
*Catégorie : structure_marche*

### D9094 — Time Period Type et Time Period Length : configuration de la période
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Les inputs `Time Period Type` (ex. Days, Weeks, Months) et `Time Period Length` (ex. 1) définissent conjointement la période de calcul. Pour 1 journée : Type = Days, Length = 1. Le timeframe des barres du chart doit être divisible dans la période spécifiée.
**TRADEX-AI C2** : Configuration standard TRADEX-AI : Time Period Type = Days, Time Period Length = 1 (Value Area de la session journalière). Les range bars NT8 doivent avoir un timeframe compatible (inférieur à la session journalière).
*Catégorie : structure_marche*

### D9095 — Restriction : incompatibilité avec bar types non-temporels
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Sierra Chart indique explicitement que les types de barres suivants sont **incompatibles** avec la study ID=209 : Number of Trades, Volume, Range, Reversal, Renko, Delta Volume, Price Change, Point and Figure Bars. Le résultat serait inexact et incohérent.
**TRADEX-AI C2** : Restriction importante pour TRADEX-AI : la study Volume Value Area Lines ne peut pas être utilisée directement sur des range bars NT8. Elle doit être calculée sur un chart time-based (ex. 5min, 15min, Daily) puis les niveaux VVAH/VVAL/VPOC extraits et reportés sur les range bars.
*Catégorie : structure_marche*

### D9096 — Reference n Periods Back : projection des niveaux sur la période suivante
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : L'input `Reference n Periods Back` (valide uniquement si `Draw Developing Value Area Lines = No`) spécifie combien de périodes en arrière les lignes sont basées. Si n=1 et période=1 Day, les lignes de chaque journée sont basées sur la journée précédente (forward projection de 1 jour). Si n=0, les lignes utilisent les données de la période courante.
**TRADEX-AI C2** : Valeur recommandée : `Reference n Periods Back = 1` pour projeter les niveaux VVAH/VVAL/VPOC de la veille sur la séance courante, conformément à l'usage standard du Volume Profile en trading intraday sur GC/CL/HG/ZW.
*Catégorie : structure_marche*

### D9097 — Fallback automatique sur périodes sans données (max 20 itérations)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Si la période de référence n'a pas de données (ex. jour férié), la study recherche automatiquement en arrière jusqu'à trouver une période valide, avec un maximum de 20 itérations. Exemple : si lundi est férié, le lundi suivant utilisera les données du vendredi précédent.
**TRADEX-AI C2** : Comportement Sierra Chart documenté. Dans TRADEX-AI, implémenter la même logique de fallback en Python : si la période de référence N est vide, chercher N+1, N+2... jusqu'à N+20. Cela garantit des niveaux VVAH/VVAL/VPOC valides même après les jours fériés US (NFP, Thanksgiving, etc.).
*Catégorie : structure_marche*

### D9098 — Tick Size : paramètre critique pour la précision des calculs
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Sierra Chart indique qu'il est essentiel de configurer correctement le `Tick Size` du symbole (via Chart >> Chart Settings). Un Tick Size incorrect peut provoquer des temps de chargement très longs ET des inexactitudes dans les calculs VVAH/VVAL/VPOC.
**TRADEX-AI C2** : Configuration obligatoire pour TRADEX-AI Phase C : vérifier le Tick Size de chaque actif dans Sierra Chart : GC = 0.10 ($/oz), HG = 0.0005 ($/lb), CL = 0.01 ($/bbl), ZW = 0.25 (cents/bushel). Un Tick Size incorrect fausse directement les niveaux VPOC/VVAH/VVAL.
*Catégorie : structure_marche*

### D9099 — New Period At Day Session Start When Using Evening Session
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : L'input `New Period At Day Session Start When Using Evening Session` (applicable uniquement si Time Period = 1 Day) : si `Yes`, les calculs Value Area de la session Day et de la session Evening (nuit/globex) sont séparés. Si `No`, Day et Evening sont calculés ensemble.
**TRADEX-AI C2** : Pour les futures CME (GC, HG, CL) qui ont une session Globex étendue (quasi-24h), configurer cet input à `Yes` pour séparer la session RTH (Regular Trading Hours) de la session Globex. Cela produit des niveaux VPOC/VVAH/VVAL plus représentatifs de l'activité RTH.
*Catégorie : structure_marche*

### D9100 — VPOC : Point of Control = prix avec volume maximum
🔵 **ÉCOLE** (Source : sierra_209_volume_value_area_lines.md) : Le Volume Point of Control (VPOC) est le niveau de prix où le volume échangé est maximal sur la période. Il représente le prix d'équilibre perçu par le marché. Les retours au VPOC sont communs ; le VPOC constitue un niveau de support/résistance significatif.
**TRADEX-AI C2** : Règle structure marché TRADEX-AI : VPOC = niveau de référence pivot pour C2. Prix au-dessus du VPOC = biais haussier ; prix en dessous = biais baissier. Croisement du VPOC = niveau de surveillance pour entrée/sortie.
*Catégorie : structure_marche*

### D9101 — VVAH et VVAL : bornes de la Value Area (70% du volume)
🔵 **ÉCOLE** (Source : sierra_209_volume_value_area_lines.md) : La Value Area High (VVAH) et la Value Area Low (VVAL) sont les bornes supérieure et inférieure de la zone où 70% du volume (ou le pourcentage configuré) a été échangé. Ces niveaux sont calculés selon la méthode de la TPO Profile Chart.
**TRADEX-AI C2** : Dans la grille /10 TRADEX-AI : prix proche de VVAH = résistance de volume (signal short potentiel si rejet) ; prix proche de VVAL = support de volume (signal long potentiel si rebond). Distance VVAH-VVAL = largeur de la Value Area = indicateur de dispersion du volume.
*Catégorie : structure_marche*

### D9102 — Calcul Value Area : référence à la méthode TPO Profile Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Sierra Chart précise que la méthode de calcul de la Value Area et du Point of Control est décrite dans la section Calculations de la page de la study `TPO Profile Chart`. La study ID=209 utilise des volumes réels (non TPO letters).
**TRADEX-AI C2** : Le calcul VVAH/VVAL/VPOC basé sur volumes réels (Volume Profile) est différent du calcul basé sur TPO letters (Time Profile). TRADEX-AI utilise les volumes réels (C2 = Order Flow), donc la méthode Volume Profile de ID=209 est la bonne référence.
*Catégorie : volume_liquidite*

### D9103 — Automatically Correct Invalid Time Period : protection configuration
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : L'input `Automatically Correct Invalid Time Period Type/Length` : si `Yes`, quand le Bar Period passe à Daily ou plus, le Time Period Type est automatiquement mis à Months (Length=1). Si `No`, les paramètres ne changent pas automatiquement lors du changement de timeframe.
**TRADEX-AI C2** : Recommandation TRADEX-AI : laisser cet input à `Yes` pour éviter des configurations invalides lors des changements de timeframe sur les charts Sierra Chart utilisés en analyse.
*Catégorie : structure_marche*

### D9104 — Alternative pour nombre de barres : utiliser Volume by Price
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Si la période de calcul doit être un nombre de barres (plutôt qu'une période temporelle), Sierra Chart recommande d'utiliser la study `Volume by Price` configurée pour afficher uniquement les lignes VVAH/VVAL/VPOC. La study ID=209 ne supporte pas les périodes définies par un nombre de barres.
**TRADEX-AI C2** : Pour des calculs sur les dernières N range bars NT8, utiliser Volume by Price plutôt que Volume Value Area Lines (ID=209). À noter dans la configuration de l'interface Sierra Chart de TRADEX-AI Phase C.
*Catégorie : volume_liquidite*

### D9105 — Session Times : impact sur le calcul des périodes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Le temps de départ de chaque période de calcul est basé sur les `Session Times` configurées dans le chart. Cela signifie que VVAH/VVAL/VPOC sont calculés relativement à l'heure de début de session, pas à minuit.
**TRADEX-AI C2** : Pour GC (Gold), la session RTH commence à 08:20 ET. Configurer les Session Times de Sierra Chart à 08:20-13:30 ET pour obtenir des niveaux Volume Profile qui correspondent à la session RTH des futures or CME.
*Catégorie : structure_marche*

### D9106 — Niveaux VVAH/VVAL/VPOC comme niveaux de prix clés pour TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_209_volume_value_area_lines.md) : La combinaison VVAH + VVAL + VPOC forme un système de trois niveaux de référence : VPOC = équilibre, VVAH = résistance volumique, VVAL = support volumique. Ces niveaux sont reconnus par les institutions (market makers, HFT) car ils reflètent les décisions d'achat/vente massives.
**TRADEX-AI C2** : Ces trois niveaux doivent être intégrés dans la couche C2 (Order Flow) de la grille de scoring /10. Un signal TRADEX-AI généré à proximité de VPOC, VVAH ou VVAL est statistiquement plus fiable qu'un signal en zone intermédiaire.
*Catégorie : structure_marche*

### D9107 — Incompatibilité confirmée avec range bars NT8 (restriction critique)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Les Range Bars sont explicitement listées parmi les types de barres incompatibles avec la study ID=209. Sierra Chart précise "The result will not be accurate and can be inconsistent."
**TRADEX-AI C2** : Décision d'architecture TRADEX-AI : les niveaux VVAH/VVAL/VPOC doivent être calculés sur un chart time-based (5min ou 15min ou Daily) dans Sierra Chart, puis exportés vers TRADEX-AI via JSON NT8 comme niveaux de prix fixes pour la session. Ne pas tenter de calculer Volume Value Area directement sur range bars.
*Catégorie : structure_marche*

### D9108 — Developing Value Area : cohérence entre fin de période et début suivant
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : Quand `Draw Developing Value Area Lines = Yes`, les valeurs en fin de journée (période complète) sont identiques aux valeurs du lendemain si `Draw Developing Value Area Lines = No` et `Reference n Periods Back = 1`. Cette cohérence garantit la continuité des niveaux entre sessions.
**TRADEX-AI C2** : Propriété utile pour les tests de cohérence : vérifier que les niveaux VVAH/VVAL/VPOC calculés en developing mode à la clôture de la veille correspondent aux niveaux statiques projetés sur la séance suivante. Cela confirme que les calculs JSON exportés par Sierra Chart sont corrects.
*Catégorie : structure_marche*

### D9109 — Calcul VVAH/VVAL : méthode d'expansion depuis le VPOC
🔵 **ÉCOLE** (Source : sierra_209_volume_value_area_lines.md) : La Value Area est calculée en partant du VPOC et en ajoutant successivement les price levels adjacents (au-dessus et en dessous) avec le plus grand volume jusqu'à atteindre le seuil de 70%. Cette méthode est décrite en détail dans la section TPO Profile Chart.
**TRADEX-AI C2** : Pour implémenter le calcul VVAH/VVAL en Python (si extraction directe depuis données NT8), utiliser l'algorithme d'expansion bilatérale depuis VPOC : ajouter le niveau de plus grand volume au-dessus ou en dessous selon lequel est le plus grand, jusqu'à 70% du volume total.
*Catégorie : volume_liquidite*

### D9110 — Date de dernière modification : juillet 2024
🟢 **FAIT VÉRIFIÉ** (Source : sierra_209_volume_value_area_lines.md) : La page Sierra Chart Volume Value Area Lines (ID=209) a été modifiée pour la dernière fois le jeudi 18 juillet 2024.
**TRADEX-AI C2** : Documentation à jour pour 2024. Les inputs et comportements documentés sont valides pour la version courante de Sierra Chart. La description de l'input `Automatically Correct Invalid Time Period` semble être une addition récente.
*Catégorie : structure_marche*
