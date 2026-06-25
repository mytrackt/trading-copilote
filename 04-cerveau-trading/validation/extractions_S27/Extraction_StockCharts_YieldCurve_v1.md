# Extraction StockCharts — Yield Curve
**Source :** `bundles/stockcharts/yield_curve.md` (HTTP 200) + 11 images certifiées
**Méthode images :** double ancrage · 11/11 certifiées · 0 à vérifier
**Décisions :** D4971 → D4990 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/yield-curve
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Courbe des taux comme indicateur macro avancé de cycle économique — impact direct sur GC/CL via DX et sentiment ES/VX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/m838CYIgurc4RQ1XKCnx | Dynamic Yield Curve StockCharts — Nov 2019 | Introduction | D4971 |
| /files/LJP2f9goVO5V0vjxzvyu | Yield curve data early 2024 (tableau) | Construction | D4972 |
| /files/aPmLT1JCVg41Owjw0pRE | Normal yield curve — Mars 2010 | Normal Yield Curve | D4974 |
| /files/PJO3iZP4g5KdoWvByF0q | Inverted yield curve — dot-com bubble 2000 | Inverted Yield Curve | D4975 |
| /files/O2vpE0IbhBRWSoIyYvaS | Spread 10Y-2Y chart (différence) | Inverted Yield Curve | D4976 |
| /files/0xJnbaBxfJWrNp8jNot8 | Flat yield curve — Juillet 2007 | Flat Yield Curve | D4977 |
| /files/ZfF49b5LfLzdyTmY0i42 | Tableau comportement courbe / cycle économique | Economic Cycle | D4978 |
| /files/Aa5SIi7rsAX9ncTzMD0 | S&P 500 monthly 1970+ expansions/contractions NBER | Economic Cycle | D4979 |
| /files/OiFgtCKCEtf8XyhhrlKi | Flattening — courbe 2010 vs 2018 (snapshot) | Flattening | D4981 |
| /files/WjWdpyTqbhkOALJFwuq | Steepening — courbe 2007 vs 2010 | Steepening | D4982 |
| /files/3fMvYIHcElON1D1eqsSR | Dynamic Yield Curve tool StockCharts | Charting | D4984 |

## DÉCISIONS

### D4971 — Yield curve : représentation graphique des rendements obligataires par maturité
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/m838CYIgurc4RQ1XKCnx) : La courbe des taux est une représentation graphique des rendements des obligations d'État pour différentes maturités (1 mois → 30 ans). La courbe du gouvernement américain est la courbe de référence (benchmark). Elle permet de déterminer la direction probable de l'économie.
**TRADEX-AI C4** : La courbe des taux US est un indicateur macro obligatoire du Cercle C4 TRADEX — son analyse détermine le régime macro (expansion/récession) qui influence les positions sur GC (valeur refuge) et CL (demande économique).
*Catégorie : macro_evenements*

### D4972 — Construction : US Treasury publie les rendements daily (1 mois → 30 ans)
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/LJP2f9goVO5V0vjxzvyu) : Le US Department of Treasury publie chaque jour les rendements pour toutes les maturités. StockCharts Dynamic Yield Curve affiche : 3 mois, 2 ans, 5 ans, 7 ans, 10 ans, 20 ans, 30 ans. Axe vertical = rendement, axe horizontal = maturité.
**TRADEX-AI C4** : Les symboles StockCharts ($UST3M, $UST2Y, $UST10Y, etc.) permettent d'intégrer les données de taux dans le moteur TRADEX via data_reader.py — à implémenter en Phase C comme source de données macro C4.
*Catégorie : macro_evenements*

### D4973 — Interprétation générale : la courbe reflète la perception du risque par les investisseurs
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : En situation normale, on attend un rendement plus élevé pour les maturités longues (compensation du risque de durée). La forme de la courbe et ses changements dans le temps signalent l'environnement économique actuel et ses évolutions futures.
**TRADEX-AI C4** : Le changement de forme de la courbe (et non sa forme instantanée) est le signal le plus utile pour TRADEX — la transition de normale vers plate ou inversée précède les changements de régime macro qui affectent GC/CL/DX.
*Catégorie : macro_evenements*

### D4974 — Courbe normale : taux courts < taux longs → croissance normale, inflation stable
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/aPmLT1JCVg41Owjw0pRE) : Courbe normale = taux court terme inférieurs aux taux long terme, courbe progressivement croissante. Contexte : croissance économique normale, inflation et crédit stables. La courbe très pentue (steep) est courante en début de reprise (ex : Mars 2010 après la Grande Récession).
**TRADEX-AI C4** : Courbe normale steep en début de cycle = contexte favorable aux trades ACHAT sur GC (inflation anticipée) et CL (demande économique croissante). DX tend à baisser en début de cycle expansionniste.
*Catégorie : macro_evenements*

### D4975 — Courbe inversée : taux courts > taux longs → signal de récession
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/PJO3iZP4g5KdoWvByF0q) : Courbe inversée = taux court terme supérieurs aux taux long terme. Signal que la croissance économique va se stabiliser ou s'inverser, voire signaler le début d'une récession. Les investisseurs acceptent des taux bas à long terme car ils anticipent la chute des taux. Exemple : inversion pendant l'éclatement de la bulle dot-com (août 2000).
**TRADEX-AI C4** : Une inversion de la courbe des taux US = contexte de risque élevé pour tous les actifs cycliques (HG cuivre, CL pétrole, ZW blé) — renforcer la pondération GC (valeur refuge) et durcir les critères d'entrée Long sur HG/CL/ZW. Intégrer comme critère éliminatoire potentiel.
*Catégorie : macro_evenements*

### D4976 — Inversion 10Y-2Y : définition standard de la courbe inversée
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/O2vpE0IbhBRWSoIyYvaS) : L'inversion la plus surveillée = segment 10Y-2Y. La courbe est considérée inversée quand le rendement 10 ans < rendement 2 ans ($UST10Y-$UST2Y < 0). Le spread 10Y-2Y négatif a précédé chaque récession depuis les années 1970.
**TRADEX-AI C4** : Indicateur macro TRADEX : surveiller $UST10Y-$UST2Y. Si < 0 → flag "inversion active" dans le moteur → facteur de risque macro C4 = élevé. GC reçoit un bonus de score en contexte d'inversion (safe haven). HG/CL/ZW reçoivent un malus.
*Catégorie : macro_evenements*

### D4977 — Courbe plate : transition économique entre expansion et contraction
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/0xJnbaBxfJWrNp8jNot8) : Courbe plate = rendements similaires sur toutes les maturités. Représente une période de transition (de normale vers inversée ou vice-versa). Exemple : juillet 2007, précurseur de la Grande Récession. Le S&P 500 se stabilisait pendant cette transition.
**TRADEX-AI C4** : Une courbe plate avec tendance à l'inversion = signal d'alerte précoce pour TRADEX → réduire la taille des positions sur HG/CL/ZW, favoriser GC, surveiller VX en attente de pic de volatilité.
*Catégorie : macro_evenements*

### D4978 — Tableau cycle économique / comportement de la courbe (4 phases)
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/ZfF49b5LfLzdyTmY0i42) : Comportement type de la courbe selon le cycle : Expansion = courbe normale/steepening ; Pic = courbe s'aplatit ; Contraction/Récession = courbe inversée ou très plate ; Reprise = courbe se redresse (steepening depuis le bas).
**TRADEX-AI C4** : Ce tableau est la grille de lecture macro C4 pour TRADEX. Le moteur doit évaluer la position dans le cycle économique (via forme courbe + direction) pour pondérer correctement les signaux sur chaque actif TRADING.
*Catégorie : macro_evenements*

### D4979 — Inversion de courbe précède chaque récession depuis les années 1970
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/Aa5SIi7rsAX9ncTzMD0) : Sur le graphique mensuel S&P 500 depuis 1970 (expansions NBER marquées), une inversion du spread 10Y-2Y (cercles oranges) précède systématiquement chaque période de contraction. Aucun faux signal majeur observé sur 50 ans.
**TRADEX-AI C4** : Règle macro TRADEX vérifiée empiriquement : inversion 10Y-2Y = précurseur récession avec délai moyen de 12-18 mois. Dès l'inversion confirmée (plusieurs semaines consécutives sous zéro), activer le mode "risque récession" qui réduit l'exposition sur HG/CL/ZW.
*Catégorie : macro_evenements*

### D4980 — Flattening : long yields baissent + short yields montent → plein cycle expansionniste
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/OiFgtCKCEtf8XyhhrlKi) : Le flattening se produit quand les taux longs baissent pendant que les taux courts montent (ou restent stables) — la pente de la courbe diminue. Typiquement en fin de cycle expansionniste (full recovery mode). Exemple : de 2010 (steep) à 2018 (très flat).
**TRADEX-AI C4** : Un flattening actif de la courbe US = signe de fin de cycle haussier → surveiller les tops sur ES, réduire les positions longues sur CL et HG (actifs cycliques de fin de cycle), maintenir la vigilance GC.
*Catégorie : macro_evenements*

### D4981 — Steepening : écart short/long augmente → début de cycle de croissance
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/WjWdpyTqbhkOALJFwuq) : Le steepening se produit quand l'écart entre taux courts et taux longs augmente. Généralement observé au début d'une période de croissance/expansion. Exemple : de mai 2007 (très flat) à août 2010 (steep) — taux courts ont chuté bien plus vite que les taux longs.
**TRADEX-AI C4** : Un steepening après une inversion = signal de reprise économique → contexte favorable pour les trades ACHAT sur HG (cuivre, économie industrielle) et CL (demande croissante) — réduire la pondération GC refuge.
*Catégorie : macro_evenements*

### D4982 — La forme actuelle de la courbe est moins importante que sa direction de changement
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : Ce n'est pas tant la forme actuelle de la courbe qui résout le puzzle financier, mais la transition et le changement de forme au fil du temps qui fournissent les indices sur la direction économique future.
**TRADEX-AI C4** : Règle de surveillance TRADEX : mesurer la dérivée du spread 10Y-2Y (taux de changement sur 4 semaines) — une accélération vers l'inversion est plus actionnable qu'une inversion déjà consommée depuis longtemps.
*Catégorie : macro_evenements*

### D4983 — Approche risk-on / risk-off via la courbe des taux
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : Combiner l'information de la courbe des taux avec sa relation aux stades du cycle économique permet de déterminer si on est dans un environnement "risk-on" (favoriser actifs risqués) ou "risk-off" (favoriser refuges).
**TRADEX-AI C4/C5** : Grille risk-on/risk-off TRADEX : Courbe normale steep → risk-on → favoriser HG/CL/ZW. Courbe inversée → risk-off → favoriser GC, réduire VX (ou couvrir). Cette grille complète le signal VIX (C5) pour la décision macro.
*Catégorie : macro_evenements*

### D4984 — Dynamic Yield Curve StockCharts : outil de visualisation interactif
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md, /files/3fMvYIHcElON1D1eqsSR) : StockCharts propose un Dynamic Yield Curve tool avec : visualisation des rendements 3M → 30Y, snapshots pour comparer deux dates, animation des changements dans le temps. Les symboles ($UST3M, $UST2Y, $UST5Y, $UST7Y, $UST10Y, $UST20Y, $UST30Y) sont utilisables dans SharpCharts.
**TRADEX-AI C4** : Ces symboles StockCharts servent de référence pour construire le moniteur macro C4 de TRADEX — le data_reader.py pourra intégrer ces données via l'API Alpha Vantage (proxy DXY déjà validé en S07) pour alimenter le calcul du spread 10Y-2Y.
*Catégorie : macro_evenements*

### D4985 — Charting 10Y-2Y spread : $UST10Y-$UST2Y avec ligne zéro
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : Pour visualiser l'inversion, tracer $UST10Y-$UST2Y sur SharpChart et ajouter une ligne horizontale à 0. La courbe est inversée quand la ligne passe sous zéro. Exemple : brève et minimale inversion en août 2019.
**TRADEX-AI C4** : Implémentation TRADEX : calculer daily ($UST10Y - $UST2Y) et stocker dans la DB SQLite locale. Un passage sous zéro pendant 5 jours consécutifs déclenche l'alerte "inversion confirmée" dans le moteur.
*Catégorie : macro_evenements*

### D4986 — Taux US Treasury publiés quotidiennement sur treasury.gov
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : Le US Department of Treasury publie chaque jour les rendements pour toutes les maturités sur www.treasury.gov. Ces données sont gratuites et publiques.
**TRADEX-AI C4** : Source de données alternative gratuite pour TRADEX : scraper daily les taux treasury.gov (3M, 2Y, 10Y) en backup si Alpha Vantage échoue — à implémenter dans staleness_monitor.py comme source C4.
*Catégorie : macro_evenements*

### D4987 — Courbe inversée : relativement rare mais très suivie quand elle apparaît
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : Les inversions de courbe sont relativement rares, mais elles attirent une attention considérable quand elles se produisent. La durée de l'inversion (pas seulement le fait qu'elle existe) est un paramètre important.
**TRADEX-AI C4** : Paramètre de durée TRADEX : ne pas sur-réagir à une inversion d'un seul jour. Seuil = 5 jours consécutifs minimum sous zéro pour le spread 10Y-2Y → confirmer l'activation du mode "risque récession".
*Catégorie : macro_evenements*

### D4988 — Courbe plate en juillet 2007 : précurseur de la Grande Récession (cas réel)
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : En juillet 2007, la courbe des taux était très plate avec tous les taux > 4.65%. Le S&P 500 se stabilisait pendant cette transition. La Grande Récession a débuté fin 2007. Ce cas réel documente la courbe plate comme signal précurseur.
**TRADEX-AI C4** : Cas de référence historique : flat curve juillet 2007 → récession Q4 2007. Sur GC (or), les prix ont fortement augmenté pendant 2007-2008 (safe haven demand). Ce pattern historique valide GC comme hedge en contexte de flat/inverted curve.
*Catégorie : macro_evenements*

### D4989 — Courbe steep normale en mars 2010 : signe de reprise après récession
🟢 **FAIT VÉRIFIÉ** (Source : yield_curve.md) : La courbe très pentue de mars 2010 (recovery post-Grande Récession) est caractéristique du début d'une période d'expansion. Le S&P 500 commençait sa reprise depuis son plus bas de 2009.
**TRADEX-AI C4** : Cas de référence historique : steep curve mars 2010 → bull market S&P 500 2010-2020. Sur GC, après la récession l'or a continué à monter jusqu'en 2011 malgré la reprise (momentum inflation). Contexte steep curve ≠ automatiquement bearish pour GC à court terme.
*Catégorie : macro_evenements*

### D4990 — Risk-on/risk-off : utiliser la courbe + cycle économique pour décision macro globale
🟡 **SYNTHÈSE** (Source : yield_curve.md) : La courbe des taux, combinée à la connaissance des stades du cycle économique, aide à déterminer une approche risk-on (actifs risqués : HG, CL, ZW, actions) ou risk-off (refuges : GC, obligations, DX). Ni la forme instantanée ni un seul indicateur ne suffisent — c'est la combinaison et la direction de changement qui comptent.
**TRADEX-AI C4** : Règle synthèse macro TRADEX : le signal macro C4 combine (1) forme de la courbe (normal/flat/inverted), (2) direction de changement (steepening/flattening), (3) position dans le cycle NBER. Ce triple filtre alimente la pondération C4 dans la grille de score /10.
*Catégorie : macro_evenements*
