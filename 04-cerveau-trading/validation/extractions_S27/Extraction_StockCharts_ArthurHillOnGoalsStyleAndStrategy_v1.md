# Extraction StockCharts — Arthur Hill on Goals, Style and Strategy
**Source :** `bundles/stockcharts/arthur_hill_on_goals_style_and_strategy.md` (HTTP 200 · ~6 200 car.) + 0 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 0/0 certifiées (page sans figure)
**Décisions :** D691 → D699 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/arthur-hill-on-goals-style-and-strategy
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (manifest : .md=0 figures vs HTML=0 images — page purement textuelle).

## DÉCISIONS

### D691 — Définir une stratégie cohérente avec objectifs et style avant de trader
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : « Before investing or trading, it is important to develop a strategy or game plan that is consistent with your goals and style. » Le but ultime est de gagner de l'argent, mais il existe de nombreuses méthodes pour y parvenir. Investisseurs et traders bénéficient à garder à l'esprit leurs objectifs et leur style avant de développer une stratégie (analogie sportive : une équipe connaît son objectif et son style avant son plan de jeu).
**TRADEX-AI C1** : Principe de gouvernance amont — la grille de signal /10 doit s'inscrire dans un cadre objectifs/style figé ; ne change rien au moteur, sert de garde-fou méthodologique.
*Catégorie : gestion_risque_entree*

---

### D692 — Risque et rendement sont hautement corrélés (spectre Treasury → croissance)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : « One cannot consider return without weighing risk… Risk and return are highly correlated. The higher the potential return, the higher the potential risk. » À une extrémité du spectre, les obligations du Trésor US offrent le risque le plus bas (taux dit sans risque) et un rendement garanti ; à l'autre, les actions de croissance à forte volatilité et hauts multiples offrent les rendements potentiels (et risques) les plus élevés.
**TRADEX-AI C1** : Rappel que tout objectif de rendement implique un budget de risque correspondant ; cohérent avec le dimensionnement de position et le R/R ≥ 1:2 du projet.
*Catégorie : gestion_risque_entree*

---

### D693 — Le style découle des objectifs (rendement attendu et risque désiré)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : « After your goals have been established, it is time to develop or choose a style that is consistent with achieving those goals. » Si l'objectif est revenu et sécurité, acheter/vendre aux niveaux extrêmes (surachat/survente) est un style improbable ; si l'objectif est profits rapides, hauts rendements et haut risque, alors le bottom-picking et le gap trading peuvent être le style adopté.
**TRADEX-AI C1** : Le style choisi détermine les seuils opératoires ; à mapper sur les modes Belkhayate (Standard 15min / Rapide Range Bar / Scalping 15s) sans s'y substituer.
*Catégorie : gestion_risque_entree*

---

### D694 — Spectre des styles et horizons de détention associés
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : Les styles vont du day trader agressif cherchant à scalper des gains d'un quart à un demi-point, jusqu'à l'investisseur visant des tendances macroéconomiques de long terme. Entre les deux : swing traders (trades de 1-5 jours), position traders (1-8 semaines), value investors (1-2 ans), aggressive growth investors et contrarians.
**TRADEX-AI C1** : Taxonomie des horizons utile pour cadrer le périmètre TRADEX (intraday/position) ; aucune valeur d'ordre, contexte pédagogique.
*Catégorie : timing*

---

### D695 — Le style dépend aussi du niveau d'engagement (commitment)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : « Your style will depend not only on your goals, but also on your level of commitment. » Les day traders adoptent un style agressif à forte activité (trades rapides, petits profits, stop-loss très serrés, graphiques intraday, fort engagement). Les position traders utilisent des graphiques journaliers de fin de séance pour des mouvements de 1-8 semaines, avec un engagement moindre. « Make sure your level of commitment jibes with your trading style. The more trading involved, the higher the level of commitment. »
**TRADEX-AI C1** : Le niveau d'activité doit rester compatible avec le rate limiting (max 1 analyse/10s) et le mode Manuel ; rappelle que le scalping exige plus d'engagement humain.
*Catégorie : timing*

---

### D696 — Exemple chiffré : objectif 20-30 % annuel et allocation 5-10 % du portefeuille
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : Dans la stratégie hypothétique exposée, l'objectif est un rendement annuel de 20-30 %, relativement élevé donc impliquant un niveau de risque correspondant élevé. À cause de ce risque, seule une petite part (5-10 %) du portefeuille est allouée à cette stratégie, le reste allant à une approche plus conservatrice.
**TRADEX-AI C1** : Cadre d'allocation prudent (capital de trading = fraction minoritaire du capital total) ; cohérent avec la philosophie de préservation du capital.
*Catégorie : gestion_risque_entree*

---

### D697 — Règle de money management : 5 % max par trade + exit défini avant l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : Le style décrit impose un money management strict limitant les pertes par un stop-loss placé immédiatement après l'initiation du trade. « An exit strategy must be in place before the trade is initiated. » Si le trade devient gagnant, la stratégie de sortie est révisée pour verrouiller les gains. Le maximum autorisé par trade est de 5 % du capital de trading total (exemple : portefeuille 300 000 → 21 000 (7 %) alloués au trading → max 1 050 par trade = 21 000 × 5 %).
**TRADEX-AI C7** : Règle de gestion du risque par trade (stop défini AVANT entrée, plafond % du capital) directement transposable en garde-fou de dimensionnement ; valeur 5 % à confronter aux 32/42 garde-fous existants avant tout codage.
*Catégorie : gestion_risque_entree*

---

### D698 — Stratégie type : long près des supports / short près des résistances, filtrée par tendance long terme
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : La stratégie de trading consiste à acheter (long) les actions proches des niveaux de support et vendre (short) celles proches des résistances. Par prudence, l'auteur ne prend des longs que sur des actions en tendance haussière hebdomadaire (long terme) et des shorts sur des actions en tendance baissière hebdomadaire. Il recherche en plus des divergences positives/négatives naissantes sur des indicateurs de momentum clés et des signes d'accumulation/distribution.
**TRADEX-AI C1** : Logique de confluence support/résistance + filtre de tendance supérieure + divergence ; recoupe la logique multi-timeframe et l'usage des pivots Belkhayate comme zones, sans s'y substituer.
*Catégorie : configuration*

---

### D699 — Arsenal d'indicateurs limité à 3 + déclencheurs (chandeliers, retournements, gaps)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_goals_style_and_strategy.md) : Le style limite les indicateurs à trois, le price action (chandeliers) et les figures graphiques ayant le plus d'influence. L'arsenal : deux indicateurs de momentum (PPO orienté direction du momentum, et Slow Stochastic Oscillator orienté surachat/survente) et un indicateur de volume (Accumulation/Distribution Line). Comme déclencheurs : figures en chandeliers clés, retournements de prix et gaps. L'auteur conseille aussi des portefeuilles séparés pour différencier activités de trading (agressif, ~5-10 %) et d'investissement (conservateur, ~90-95 %).
**TRADEX-AI C1** : Principe de parcimonie (peu d'indicateurs, déclencheurs price-action) cohérent avec une grille déterministe ; PPO/Stochastic/ADL sont des candidats indicateurs, jamais des ordres automatiques.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D691 | Stratégie cohérente avec objectifs/style | 🟢 | C1 | gestion_risque_entree |
| D692 | Risque/rendement hautement corrélés | 🟢 | C1 | gestion_risque_entree |
| D693 | Le style découle des objectifs | 🟢 | C1 | gestion_risque_entree |
| D694 | Spectre des styles et horizons | 🟢 | C1 | timing |
| D695 | Style dépend du niveau d'engagement | 🟢 | C1 | timing |
| D696 | Objectif 20-30 % + allocation 5-10 % | 🟢 | C1 | gestion_risque_entree |
| D697 | 5 % max/trade + exit avant entrée | 🟢 | C7 | gestion_risque_entree |
| D698 | Long support/short résistance + filtre tendance | 🟢 | C1 | configuration |
| D699 | Arsenal 3 indicateurs + déclencheurs | 🟢 | C1 | signal |

**Liens Belkhayate :** Aucun lien direct. La méthode décrite est un cadre générique de gouvernance objectifs/style/stratégie (Arthur Hill / StockCharts), NON CONCERNÉ par la méthode Belkhayate propriétaire (⚫ Belkhayate seul). Les principes de money management (stop avant entrée, % max par trade) recoupent les garde-fous TRADEX mais ne proviennent pas de Belkhayate ; toute assimilation serait « hypothèse projet, non affirmée par la source » (⚫🔴).

**À vérifier (humain) :**
- D696/D697 — chiffres (20-30 %, 5-10 %, 5 % par trade, exemple 300 000/21 000/1 050) : ce sont des exemples pédagogiques d'une stratégie HYPOTHÉTIQUE de l'auteur, PAS des recommandations universelles. Ne pas coder ces valeurs comme seuils TRADEX sans arbitrage humain vs garde-fous existants.
- Page sans aucune image (0/0) — rien à certifier côté visuel.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
