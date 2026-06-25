# Extraction StockCharts — TA 101 Part 15 (Gaps)
**Source :** `bundles/stockcharts/ta_101_part_15.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D4131 → D4150 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-15
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Patterns de gaps applicables à GC/HG/CL/ZW pour identifier ruptures et épuisements de tendance ; gaps de continuité utilisables comme mesure de cible de mouvement.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Gaps | Gaps | D4131 |
| image_02.png | Gaps | Gaps | D4135 |

## DÉCISIONS

### D4131 — Définition et nature des gaps de prix
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md, image_01) : Les gaps sont des espaces vides sur un graphique de prix représentant des plages de prix où aucune transaction n'a eu lieu. Ils résultent d'un intérêt extraordinaire d'achat ou de vente se développant quand le marché est fermé.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un gap à l'ouverture (session Globex) signale un déséquilibre offre/demande développé hors séance — signal d'alerte C1 à qualifier avec volume.
*Catégorie : structure_marche*

### D4132 — Up gap : définition et biais directionnel
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Pour qu'un up gap se forme, le prix bas après clôture du gap day doit être supérieur au prix haut du jour précédent. Les up gaps sont généralement considérés haussiers.
**TRADEX-AI C1** : GC/CL : un up gap à l'ouverture de séance avec volume supérieur à la moyenne renforce un signal ACHETER déjà validé par les 3/4 actifs trading.
*Catégorie : structure_marche*

### D4133 — Down gap : définition et biais directionnel
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Un down gap est l'opposé d'un up gap : le prix haut du gap day doit être inférieur au prix bas du jour précédent. Les down gaps sont généralement considérés baissiers.
**TRADEX-AI C1** : HG/ZW : un down gap confirme la pression vendeuse — compatible avec signal VENDRE si les cercles C2 (order flow) et C4 (macro) s'alignent.
*Catégorie : structure_marche*

### D4134 — Condition de significativité : volume supérieur à la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les up gaps et down gaps sont considérés significatifs lorsqu'ils sont accompagnés d'un volume supérieur à la moyenne.
🟡 **SYNTHÈSE** : Sans volume supérieur à la moyenne, un gap reste ambigu et ne suffit pas à valider un signal directionnel.
**TRADEX-AI C2** : Croiser le gap price avec le volume ATAS — big trades C2 dans le sens du gap = confirmation institutionnelle.
*Catégorie : volume_liquidite*

### D4135 — Gaps intraday temporaires : pas de signification technique
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md, image_02) : Les prix gappent souvent à l'ouverture du marché puis comblent le gap avant la clôture. Ces gaps intraday temporaires ne doivent pas être considérés comme ayant plus de signification que la volatilité normale du marché.
**TRADEX-AI C1** : Sur range bars NT8, ignorer les micro-gaps de début de séance sur GC/CL si comblés dans la première heure — éviter les faux signaux.
*Catégorie : structure_marche*

### D4136 — Idée fausse : les gaps se comblent toujours
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : De nombreux investisseurs croient à tort que les gaps influencent les prix futurs au point de finir par se combler. Les gaps ont peu ou pas d'influence sur l'action des prix des semaines ou mois après leur formation.
🟡 **SYNTHÈSE** : Seuls les gaps se comblant dans les quelques jours suivant leur formation peuvent être significatifs.
**TRADEX-AI C1** : Ne pas attendre systématiquement le comblement d'un gap sur GC/ZW — la règle Belkhayate s'applique sur les faits présents, pas sur une hypothèse de comblement tardif.
*Catégorie : psychologie*

### D4137 — Gap de rupture (Breakaway Gap) : changement de psychologie de marché
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les breakaway gaps signalent un changement de psychologie de marché, particulièrement accompagnés d'un volume supérieur à la moyenne. Un bullish breakaway gap se forme quand un titre gappe à la hausse après un déclin prolongé, une base étendue ou une période de consolidation.
**TRADEX-AI C1/C5** : GC/CL : breakaway gap haussier après consolidation = signal fort C1 ; croiser avec VX (C5) — si VIX en baisse simultanément, la combinaison est très favorable.
*Catégorie : structure_marche*

### D4138 — Gap de rupture baissier (Bearish Breakaway Gap)
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Un bearish breakaway gap se forme quand un titre gappe à la baisse après une avancée prolongée, un sommet étendu ou une période de consolidation.
**TRADEX-AI C1** : HG/ZW : bearish breakaway gap après rally prolongé = signal VENDRE prioritaire — vérifier COT (C3) pour positionnement institutionnel en accord.
*Catégorie : structure_marche*

### D4139 — Gap commun (Common Gap) : volatilité sans changement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les common gaps se produisent dans un trading range ou peu après un mouvement brutal comme une réaction. Ils ne reflètent pas un changement de psychologie de marché mais représentent de la volatilité de prix ou un déséquilibre temporaire offre/demande.
**TRADEX-AI C1** : Exemple : si GC a décliné 20% en une semaine et gappe à la hausse, c'est un common gap — ne pas interpréter comme signal d'achat.
*Catégorie : structure_marche*

### D4140 — Gap de continuation (Continuation / Measuring / Runaway Gap)
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les continuation gaps se forment près du milieu d'une tendance courte ou intermédiaire dans la même direction. Ces gaps signalent une continuation de la tendance précédente. Ils peuvent être déclenchés par des événements d'actualité.
🟡 **SYNTHÈSE** : La position à mi-tendance du gap (measuring gap) permet d'estimer l'objectif de prix : distance du début de tendance au gap, projetée au-delà du gap.
**TRADEX-AI C1/C6** : CL/GC : un gap de continuation déclenché par une news macro (NFP, FOMC, géopolitique) près du milieu du mouvement valide la cible Belkhayate projetée.
*Catégorie : structure_marche*

### D4141 — Gap d'épuisement (Exhaustion Gap) : fin de tendance probable
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les exhaustion gaps se produisent dans la direction de tendances prolongées. Pour être valide, les prix doivent inverser rapidement après le gap et combler le gap. Dans les dernières phases d'une tendance, l'étendue de la tendance est largement rapportée, causant finalement une poussée d'activité qui ne peut être soutenue. Ces événements marquent souvent la fin de la tendance.
**TRADEX-AI C1/C5** : GC/CL : un gap d'épuisement en fin de tendance avec comblement rapide = signal d'inversion — renforcer avec VIX (C5) et COT (C3) pour confirmer le retournement institutionnel.
*Catégorie : gestion_risque_entree*

### D4142 — Titres très peu liquides : éviter les gaps répétés
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Un graphique de prix avec des gaps presque chaque jour est typique des titres très peu tradés et doit être évité.
**TRADEX-AI C2** : GC/HG/CL/ZW sont des futures très liquides — si des gaps apparaissent quasi quotidiennement, investiguer un problème de données NT8 plutôt qu'une réalité de marché.
*Catégorie : volume_liquidite*

### D4143 — Gaps sur timeframes multiples
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les up et down gaps peuvent se former sur des graphiques journaliers, hebdomadaires ou mensuels.
🟡 **SYNTHÈSE** : Un gap sur timeframe mensuel ou hebdomadaire a plus de poids qu'un gap journalier — confluence multi-timeframe augmente la fiabilité du signal.
**TRADEX-AI C1** : Croiser la détection de gap NT8 range bars avec le graphique journalier/hebdomadaire pour hiérarchiser l'importance du gap sur GC/ZW.
*Catégorie : structure_marche*

### D4144 — Synthèse des 4 types de gaps et leur usage opérationnel
🟡 **SYNTHÈSE** (Source : ta_101_part_15.md) : Les 4 types de gaps ont des implications différentes : breakaway (changement de tendance), common (bruit), continuation (mesure de cible), exhaustion (fin de tendance). La classification correcte est essentielle avant toute décision.
⚫ **HYPOTHÈSE PROJET** : La méthode Belkhayate utilise les gaps comme confirmation structurelle de C1 (Prix) — un gap aligné avec BGC/Direction renforce le score TRADEX.
**TRADEX-AI C1** : Intégrer la classification du gap dans le prompt Claude API : préciser le type pour affiner le signal ACHETER/VENDRE/ATTENDRE sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D4145 — Volume : critère discriminant entre gap significatif et bruit
🟡 **SYNTHÈSE** (Source : ta_101_part_15.md) : Le volume supérieur à la moyenne est le critère qui distingue un gap significatif (breakaway, continuation, exhaustion) d'un gap commun ou intraday sans valeur.
**TRADEX-AI C2** : Dans ATAS, vérifier le delta et les big trades au moment du gap — si institutionnels absents (volume faible), qualifier le gap de "commun" et ne pas l'intégrer dans le score.
*Catégorie : volume_liquidite*

### D4146 — Breakaway gap haussier : conditions de formation
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Un bullish breakaway gap se forme après un déclin prolongé, une base étendue ou une période de consolidation — les trois contextes contextuels sont distincts.
🟡 **SYNTHÈSE** : Base étendue = accumulation (Wyckoff) ; consolidation = énergie comprimée ; déclin prolongé = possible capitulation.
**TRADEX-AI C1/C3** : GC après accumulation longue + breakaway gap haussier + COT commercials longs (C3) = confluences maximales pour ACHETER.
*Catégorie : gestion_risque_entree*

### D4147 — Gap commun dans un trading range : exemple $20-$30
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Si un trading range se développe entre $20 et $30 et qu'un gap se forme au milieu, c'est probablement un common gap.
**TRADEX-AI C1** : Sur GC/HG : un gap dans le corps d'une consolidation latérale sans breakout confirmé = common gap à ignorer pour le scoring TRADEX.
*Catégorie : structure_marche*

### D4148 — Exhaustion gap : condition de validation par comblement rapide
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Pour qu'un exhaustion gap soit considéré valide, les prix doivent inverser peu après le gap ET combler le gap.
**TRADEX-AI C1** : Sur CL/ZW : surveiller le comblement du gap dans les 1-3 sessions suivantes — si comblé rapidement, activer alerte d'inversion de tendance dans le moteur TRADEX.
*Catégorie : gestion_risque_entree*

### D4149 — Continuation gap : déclencheur par événements d'actualité
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_15.md) : Les continuation gaps peuvent être déclenchés par des événements d'actualité qui attirent davantage l'attention du marché sur un titre.
**TRADEX-AI C6** : CL/GC : un gap de continuation déclenché par une news géopolitique (C6) ou un rapport macro (NFP/FOMC — C4) valide une entrée en tendance si le news gate TRADEX est passé.
*Catégorie : macro_evenements*

### D4150 — Gaps et psychologie de marché collective
🟡 **SYNTHÈSE** (Source : ta_101_part_15.md) : Les breakaway gaps signalent spécifiquement un changement de psychologie de marché ; les common gaps n'en reflètent aucun. Identifier le type de gap revient à lire l'état émotionnel du marché.
**TRADEX-AI C5** : Croiser la classification du gap avec VIX (C5) — un breakaway gap baissier sur GC avec spike VIX = panique collective confirmée, score d'urgence élevé.
*Catégorie : psychologie*
