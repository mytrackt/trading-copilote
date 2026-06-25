# Extraction StockCharts — Dow Theory

**Source :** `bundles/stockcharts/dow_theory.md` (HTTP 200 · ~44 000 car.) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 10/10 certifiées · 0 à vérifier
**Décisions :** D1591 → D1604 · **Page :** chartschool.stockcharts.com/table-of-contents/market-analysis/dow-theory
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **NATURE** : la Dow Theory est le corpus **fondateur** de l'analyse technique (Charles Dow, raffiné par Hamilton et Rhea). Ses énoncés sont des **principes d'ÉCOLE (🔵)** et des **conventions historiques (🟡)**, pas des règles chiffrées universelles. Univers natif = indices ACTIONS (DJIA + DJTA) avec confirmation par deux moyennes. La logique de structure (tendance = série de plus-hauts/plus-bas croissants ou décroissants) est universelle et **applicable aux futures (C1)** ; la confirmation inter-indices et le breadth restent côté CONFIRMATION (ES, C5/C7). Aucun lien Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | Coca Cola Co. (KO) Reaction Rally example chart | Averages Discount Everything | D1593 |
| image_02 | Yahoo Inc. (YHOO) Rumor example chart | Averages Discount Everything | D1593 |
| image_03 | DJIA ($INDU) Market Movement example chart | Secondary Movements | D1596 |
| image_04 | (section-fallback) | Secondary Movements | D1596 |
| image_05 | (section-fallback) | Secondary Movements | D1596 |
| image_06 | DJTA ($TRAN) Trend example chart | Identification of the Trend | D1599 |
| image_07 | DJIA ($INDU) Trend example chart | Identification of the Trend | D1599 |
| image_08 | DJIA ($INDU) Reaction High example chart | Identification of the Trend | D1599 |
| image_09 | DJTA and DJIA Confirmed Averages example chart | How Averages Confirm | D1600 |
| image_10 | DJIA ($INDU) Trading Ranges example chart | Lines (Trading Ranges) | D1603 |

---

## DÉCISIONS

### D1591 — Objet de la Dow Theory : tendance primaire + confirmation par deux moyennes
🔵 **ÉCOLE** (Source : dow_theory.md) : La Dow Theory identifie la **tendance** du marché et fournit des signaux pour trader **avec la tendance primaire**. Elle repose sur l'identification de la tendance du **Dow Jones Rail (aujourd'hui Transports)** et du **Dow Jones Industrial Average**, avec le **volume pour confirmer**. Si les deux moyennes tendent dans le même sens, l'ensemble du marché est dit tendanciel dans ce sens.
**TRADEX-AI C7/C5** : Principe fondateur de confirmation inter-indices. Côté TRADEX-AI : applicable seulement en CONFIRMATION (santé du marché actions via ES), pas un signal direct sur un future isolé.
*Catégorie : structure_marche*

---

### D1592 — Assomption 1 : la tendance primaire ne se manipule pas
🔵 **ÉCOLE** (Source : dow_theory.md) : Première assomption — la **manipulation de la tendance primaire est impossible**. Les mouvements intrajournaliers, jour-à-jour et même secondaires peuvent être manipulés (grandes institutions, spéculateurs, news, rumeurs), mais pas la tendance primaire. Des titres individuels peuvent être manipulés mais retournent ensuite à leur tendance primaire (ex. cités : PairGain via canular, Books-A-Million, argent par les frères Hunt en 1979/80).
**TRADEX-AI C1** : Cadre conceptuel — privilégier la tendance de fond, traiter le bruit court terme comme suspect.
*Catégorie : structure_marche*

---

### D1593 — Assomption 2 : les moyennes escomptent tout (« buy the rumor, sell the news »)
🔵 **ÉCOLE** (Source : dow_theory.md, image_01, image_02) : Deuxième assomption — le **marché reflète toute l'information disponible** ; tout est déjà dans le prix. L'imprévu n'affecte généralement que la tendance court terme ; la primaire reste intacte. Le marché « regarde devant » : d'où l'axiome « **buy the rumor, sell the news** ». Exemples : Coca-Cola (rallye oct./nov. 1998 = mouvement secondaire dans une primaire baissière) ; Yahoo! a chuté ~20 % malgré des résultats dépassant les attentes.
**TRADEX-AI C4/C6** : Rappel macro/news — l'information attendue est déjà escomptée ; à coupler avec la News Gate (NFP/FOMC/CPI) du système.
*Catégorie : structure_marche*

---

### D1594 — Assomption 3 : la théorie n'est pas infaillible
🔵 **ÉCOLE** (Source : dow_theory.md) : Troisième assomption — la Dow Theory **n'est pas infaillible** ; c'est un ensemble de lignes directrices, pas une méthode sûre de battre le marché. Elle aide à retirer l'émotion et exige de l'objectivité (voir ce qui est, pas ce qu'on veut voir). Hamilton notait que ceux qui l'appliquaient bien tradaient rarement plus de 4-5 fois par an.
**TRADEX-AI** : Garde-fou épistémique — pas de surconfiance ; cohérent avec le plafond de confiance fallback et la prudence du mode AUTO.
*Catégorie : gestion_risque_entree*

---

### D1595 — Trois types de mouvements : primaire, secondaire, fluctuations quotidiennes
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md) : Trois types de mouvements de prix. **Primaire** : tendance de fond, de quelques mois à plusieurs années (bull/bear markets) ; reste en vigueur jusqu'à preuve du contraire. **Secondaire (réaction)** : de quelques semaines à quelques mois, **à contre-courant** de la primaire. **Fluctuations quotidiennes** : avec ou contre la primaire, de quelques heures à quelques jours, rarement plus d'une semaine.
**TRADEX-AI C1** : Taxonomie de structure multi-échelles — distinguer primaire (fond) / secondaire (correction) / bruit, base de toute lecture de tendance.
*Catégorie : structure_marche*

---

### D1596 — Caractéristiques des mouvements secondaires (retracement 1/3–2/3)
🟡 **CONVENTION** (Source : dow_theory.md, image_03, image_04, image_05) : Caractéristiques observées par Hamilton (guides, pas règles) : (1) les mouvements secondaires retracent **1/3 à 2/3** de la primaire, **50 %** étant typique (exemple DJIA 1997 : ~42 %) ; (2) ils sont **plus rapides et plus marqués** que la primaire précédente ; (3) ils se terminent par une **période d'apathie** (peu de mouvement, baisse de volume) juste avant le retournement ; (4) les plus-bas s'accompagnent parfois d'un **jour de washout à fort volume** (ex. sept./oct. 1998, volumes records).
**TRADEX-AI C1** : Brique retracement codable côté confirmation (zone 1/3–2/3, médiane 50 %) ; signaux volume (apathie / washout) = brique C2.
*Catégorie : structure_marche*

---

### D1597 — Fluctuations quotidiennes : dangereuses isolément
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md) : Les fluctuations quotidiennes, importantes en groupe, sont **dangereuses et peu fiables individuellement**. Trop d'emphase sur un ou deux jours mène à des erreurs et des pertes. Le prix quotidien n'a de valeur que regroupé avec d'autres jours pour former une structure.
**TRADEX-AI C1** : Garde-fou — ne pas générer de signal sur un mouvement isolé d'un seul jour ; exiger une structure pluri-périodes.
*Catégorie : gestion_risque_entree*

---

### D1598 — Trois stades des bull et bear markets primaires (psychologie)
🔵 **ÉCOLE** (Source : dow_theory.md) : Hamilton identifie trois stades. **Bull market** : (1) Accumulation (« smart money » achète, pessimisme dominant, valorisations basses) ; (2) Big Move (le plus long, plus forte hausse, conditions et bénéfices s'améliorent) ; (3) Excess (spéculation excessive, pressions inflationnistes, public pleinement investi). **Bear market** : (1) Distribution ; (2) Big Move ; (3) Despair (tout espoir perdu, valorisations basses mais vente continue).
**TRADEX-AI C5** : Cadre de sentiment/cycle psychologique — Accumulation/Distribution comme phases ; brique de contexte, pas signal exécutable.
*Catégorie : structure_marche*

---

### D1599 — Identification de la tendance : peak/trough analysis (HH/HL vs LH/LL)
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md, image_06, image_07, image_08) : Hamilton utilise l'analyse **pics/creux**. Une **tendance haussière** = série de **plus-hauts croissants et plus-bas croissants** (higher highs / higher lows) ; une **tendance baissière** = série de **plus-hauts décroissants et plus-bas décroissants** (lower highs / lower lows). Une tendance est valide jusqu'à preuve du contraire : un downtrend reste valide tant qu'un plus-bas plus haut n'est pas formé ET que l'avance suivante ne dépasse pas le plus-haut de réaction précédent (et réciproquement). Hamilton suggérait d'**exclure les mouvements de moins de 3 %** pour éliminer les faux signaux, et évoquait une **moyenne mobile 5 jours** pour lisser.
**TRADEX-AI C1** : Définition opérationnelle de la tendance directement codable (HH/HL vs LH/LL) ; filtre anti-bruit 3 % ; applicable GC·HG·CL·ZW.
*Catégorie : structure_marche*

---

### D1600 — Les deux moyennes doivent se confirmer
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md, image_09) : Pour qu'un signal d'achat/vente de tendance primaire soit valide, l'**Industrial Average ET le Rail Average doivent se confirmer** : si l'un enregistre un nouveau plus-haut (ou plus-bas), l'autre doit suivre rapidement. Une **non-confirmation** (une moyenne sans l'autre) est un **avertissement** sans changer la tendance. Justification historique : l'activité des rails (matières premières transportées) précède celle de l'industrie.
**TRADEX-AI C7** : Principe d'inter-marché/corrélation — confirmation croisée entre deux baromètres ; pour TRADEX-AI relève de la matrice de corrélations (C7) et de la confirmation ES.
*Catégorie : structure_marche*

---

### D1601 — Rôle du volume : confirmation, jamais déterminant ultime
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md) : Le **prix reste le déterminant ultime** ; le volume est **confirmatoire**. Le volume devrait augmenter dans le sens de la tendance primaire (plus lourd sur les avances que sur les corrections en bull market ; inverse en bear market). Un **volume élevé après une longue avance** peut indiquer un retournement imminent.
**TRADEX-AI C2** : Brique volume — confirme la force du mouvement, n'est pas un signal autonome.
*Catégorie : indicateurs_tendance*

---

### D1602 — Lines (trading ranges) : accumulation ou distribution, neutres jusqu'à breakout
🟢 **FAIT VÉRIFIÉ** (Source : dow_theory.md, image_10) : Les « lines » sont des **ranges horizontaux** formés quand les moyennes évoluent latéralement. Elles indiquent soit **accumulation** soit **distribution**, indéterminable jusqu'à une cassure : cassure haussière = accumulation, cassure baissière = distribution. Hamilton considérait le range **neutre** jusqu'au breakout et déconseillait d'anticiper la cassure.
**TRADEX-AI C1** : Brique range/breakout — un range reste neutre ; ne signaler qu'à la cassure confirmée, pas par anticipation.
*Catégorie : configuration*

---

### D1603 — Performance et limites de la Dow Theory
🔵 **ÉCOLE** (Source : dow_theory.md) : Étude (Brown/Goetzmann/Kumar, *Journal of Finance*) sur 1929→sept. 1998 : le système Dow Theory a **surperformé le buy-and-hold d'environ 2 %/an** avec un **risque significativement moindre** ; il sous-performe en bull markets et surperforme en bear markets. Sur les 18 dernières années il a sous-performé de ~2,6 %/an (mais surperformé ajusté du risque).
⏳ **VOLATILE** : chiffres et bornes temporelles datés (rédaction fin années 1990) ; non actualisés.
**TRADEX-AI** : Contexte historique de performance — informatif, non opérationnel ; ne pas extrapoler les chiffres datés.
*Catégorie : gestion_risque_entree*

---

### D1604 — Critiques de la Dow Theory
🔵 **ÉCOLE** (Source : dow_theory.md) : Trois critiques principales : (1) ce n'est **pas vraiment une théorie** (aucun article académique formel, simples éditoriaux du WSJ assemblés par Rhea) ; (2) elle est **trop tardive** (le signal n'arrive qu'après dépassement du plus-haut de réaction précédent, manquant une partie du mouvement) ; (3) elle est **dépassée** car fondée sur DJIA/DJTA (réfuté en partie : le DJTA reste l'un des indices les plus sensibles à l'économie).
**TRADEX-AI** : Garde-fou — accepter le décalage du signal et le caractère retardé inhérent à une approche de suivi de tendance.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie | Actifs |
|---|----------|-----|--------|-----------|--------|
| D1591 | Objet : tendance + 2 moyennes | 🔵 | C7·C5 | structure_marche | ES (confirmation) |
| D1592 | Primaire non manipulable | 🔵 | C1 | structure_marche | — |
| D1593 | Moyennes escomptent tout | 🔵 | C4·C6 | structure_marche | — |
| D1594 | Pas infaillible | 🔵 | — | gestion_risque_entree | — |
| D1595 | 3 types de mouvements | 🟢 | C1 | structure_marche | GC·HG·CL·ZW |
| D1596 | Mouvements secondaires (1/3–2/3) | 🟡 | C1·C2 | structure_marche | GC·HG·CL·ZW |
| D1597 | Fluctuations quotidiennes | 🟢 | C1 | gestion_risque_entree | GC·HG·CL·ZW |
| D1598 | 3 stades bull/bear (psycho) | 🔵 | C5 | structure_marche | — |
| D1599 | Tendance HH/HL vs LH/LL | 🟢 | C1 | structure_marche | GC·HG·CL·ZW |
| D1600 | Confirmation des 2 moyennes | 🟢 | C7 | structure_marche | ES (confirmation) |
| D1601 | Volume = confirmation | 🟢 | C2 | indicateurs_tendance | GC·HG·CL·ZW |
| D1602 | Lines / ranges / breakout | 🟢 | C1 | configuration | GC·HG·CL·ZW |
| D1603 | Performance (datée) | 🔵⏳ | — | gestion_risque_entree | — |
| D1604 | Critiques | 🔵 | — | gestion_risque_entree | — |

**Total : 14 décisions (D1591→D1604) · 10/10 images certifiées · 0 cas à vérifier.**
Lien Belkhayate : **NON CONCERNÉ** (la source ne mentionne pas Belkhayate). La structure HH/HL ⊂ LH/LL (D1599) recoupe la notion de « Direction » Belkhayate mais sans citation explicite de la source → non rattaché.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
