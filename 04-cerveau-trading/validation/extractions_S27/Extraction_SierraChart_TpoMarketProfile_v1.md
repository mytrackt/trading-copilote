# Extraction SierraChart — TPO Market Profile (Time Price Opportunity Charts)
**Source :** `bundles/sierrachart/tpo_market_profile.md` (HTTP 200) + 0 images certifiées
**Méthode images :** pas d'images dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9471 → D9490 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference/TimePriceOpportunityCharts.html
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 451 (TPO Market Profile) — très pertinent pour TRADEX-AI : le POC, la Value Area et l'Initial Balance sont des niveaux de structure journalière clés en C2 (Order Flow) et C1 (structure marché) pour GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image présente dans le bundle) | — | — | — |

## DÉCISIONS

### D9471 — TPO / Market Profile : définition et principe fondamental
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Un chart TPO (Time Price Opportunity) représente la distribution temporelle des prix : chaque lettre ou bloc indique qu'un prix a été atteint pendant un sous-période de temps donné. Le TPO Profile Chart identifie le **Point of Control** (prix avec le plus grand nombre de TPOs = zone de plus forte activité temporelle) et la **Value Area** (zone englobant 70% des TPOs autour du POC par défaut).
**TRADEX-AI C2** : Le POC et la VA sont des niveaux de structure clés pour TRADEX-AI. Ils indiquent les zones de prix où le marché a passé le plus de temps — zones d'équilibre potentielles pour GC, CL, HG, ZW. À intégrer comme niveaux de référence dans `data_reader.py`.
*Catégorie : structure_marche*

### D9472 — Point of Control (POC) TPO : calcul exact
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Le POC TPO est le niveau de prix avec le **plus grand nombre de TPOs** (lettres/blocs). En cas d'égalité, Sierra Chart sélectionne le niveau le plus proche du centre du profil. Si deux niveaux sont équidistants du centre, c'est le **niveau inférieur** qui est retenu.
**TRADEX-AI C1/C2** : Règle de tie-break documentée et à reproduire exactement dans l'implémentation Python si TRADEX-AI calcule son propre POC depuis les données NT8. Le biais vers le bas en cas d'égalité est intentionnel et doit être conservé.
*Catégorie : structure_marche*

### D9473 — Value Area (VA) : calcul et paramètre TPO Value Area %
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : La Value Area englobe les niveaux de prix totalisant le pourcentage de TPOs défini par `TPO Value Area %`. Valeur par défaut : **70%**. Le calcul part du POC et s'étend vers le haut et le bas en comparant chaque paire de niveaux adjacents (celui avec le plus de TPOs est inclus en premier). Deux niveaux à égalité sont inclus simultanément.
**TRADEX-AI C1** : La VA à 70% est la valeur standard du Market Profile (méthode Dalton). Dans TRADEX-AI, exposer ce paramètre dans `settings.py` sous `TPO_VALUE_AREA_PCT = 0.70`. La VA High et VA Low sont des niveaux de support/résistance dynamiques journaliers pertinents pour GC et CL.
*Catégorie : structure_marche*

### D9474 — Initial Balance Range (IBR) : définition et paramètre
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : L'Initial Balance Range est la plage de prix couverte par les **N premières sous-périodes** d'un profil, défini par l'input `Initial Balance Range` (en nombre de sous-périodes). Avec des sous-périodes de 30 minutes et IBR = 2, l'Initial Balance est la range de la **première heure** de trading.
**TRADEX-AI C1/C4** : L'IBR de la première heure est un contexte macro journalier fondamental. Un prix GC ou CL en dehors de l'IBR en début de session indique une extension — signal de force directionnelle. À calculer dans `data_reader.py` depuis les données NT8 intraday.
*Catégorie : structure_marche*

### D9475 — IBR Extensions : niveaux de projection au-delà de l'Initial Balance
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Sierra Chart supporte jusqu'à **4 extensions de l'IBR** configurables via `IBR 1-4 Extension Percentage`. Ces extensions projettent des niveaux au-dessus et en dessous de l'IBR sous forme de lignes horizontales. L'extension est désactivée quand le pourcentage est mis à 0.
**TRADEX-AI C1** : Les extensions IBR sont des objectifs de prix potentiels une fois l'IBR cassé. Dans TRADEX-AI, l'IBR Extension 1 (ex : 100% de l'IBR) peut servir de premier objectif de prix (TP1) dans le calcul R/R pour les actifs TRADING.
*Catégorie : gestion_position_active*

### D9476 — Singles : définition et signal de déséquilibre
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Les **Singles** sont les premiers TPOs d'une sous-période qui dépassent le high ou low de toutes les sous-périodes précédentes, à condition que tous les TPOs de la sous-période suivante restent au-delà de ce niveau. Un single est confirmé uniquement après la clôture de la sous-période suivante. Les singles représentent des zones de prix visitées une seule fois — zones de déséquilibre.
**TRADEX-AI C1** : Les zones de singles sont des zones de déséquilibre non remplies — le marché tend à y retourner. Dans TRADEX-AI, identifier les singles proches du prix courant sur GC/CL comme zones à risque ou cibles potentielles. Signal C1 de structure marché.
*Catégorie : structure_marche*

### D9477 — Poor High / Poor Low : signal de fragilité des extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Un **Poor High** se produit quand le high d'un profil TPO est égal au high d'un profil précédent (comparaison entre sous-périodes et entre profils). Un **Poor Low** est symétrique. La tolérance est configurable via `Price Increments For Poor High/Poor Low Comparison`. Les Poor Highs/Lows indiquent que le marché n'a pas rejeté fortement les extrêmes — zones potentiellement revisitables.
**TRADEX-AI C1** : Un Poor High sur GC signifie que le marché n'a pas confirmé le rejet de résistance — risk de cassure à la hausse. Intégrer ce concept dans le filtre de structure marché C1 : ne pas vendre un Poor High, ne pas acheter un Poor Low sans confirmation supplémentaire.
*Catégorie : structure_marche*

### D9478 — Volume Point of Control (Volume POC) vs TPO POC
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Le **Volume POC** est calculé différemment du TPO POC : c'est le niveau de prix avec le **volume le plus élevé** (et non le plus grand nombre de sous-périodes). Les deux POC peuvent diverger. Le Volume POC est calculé quand `Volume by Price` est ajouté au chart TPO.
**TRADEX-AI C2** : La divergence TPO POC vs Volume POC est un signal d'ordre flow important. Si le Volume POC est plus bas que le TPO POC sur GC, les institutionnels ont accumulé en dessous du niveau temporel dominant — signal C2/C3. À noter comme information contextuelle dans les données NT8.
*Catégorie : volume_liquidite*

### D9479 — TPO Value Area % vs Volume Value Area % : deux paramètres distincts
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : `TPO Value Area %` (défaut 70%) s'applique quand `Value Area Highlight Based on Volume` = No. `Volume Value Area %` (défaut 70%) s'applique quand `Value Area Highlight Based on Volume` = Yes. Les deux paramètres sont indépendants et configurables séparément.
**TRADEX-AI C2** : Dans TRADEX-AI, utiliser la **Volume Value Area** en priorité (basée sur le volume réel) pour définir les zones de support/résistance. La TPO VA reste utile comme référence temporelle complémentaire. Exposer les deux dans `settings.py`.
*Catégorie : volume_liquidite*

### D9480 — Rotation Factor : indicateur de bias directionnel intra-journalier
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Le **Rotation Factor** est un entier incrémenté/décrémenté pour chaque sous-période en fonction des mouvements du high et du low : `+1` si High sous-période > High précédent, `+1` si Low sous-période > Low précédent, `-1` si High < précédent, `-1` si Low < précédent. Valeur positive = bias haussier, négative = bias baissier.
**TRADEX-AI C1/C2** : Le Rotation Factor journalier sur GC/CL est un indicateur de momentum intra-journalier simple et robuste. Dans TRADEX-AI, un Rotation Factor > 0 combiné à un signal Belkhayate ACHAT renforce la conviction. Calculable depuis les données NT8 JSON sans recours à Sierra Chart.
*Catégorie : indicateurs_tendance*

### D9481 — TPO Profile Time Period Length : granularité du profil
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : `Profile Time Period Length` + `Profile Time Period Length Unit` définissent la durée de chaque profil (ex : 1 Day, 1 Week, 1 Month). Pour les charts intraday, la durée par défaut est **1 Day**. Le paramètre `TPO Letter/Block Time Period Length` (défaut 30 minutes) définit la durée de chaque sous-période (lettre/bloc).
**TRADEX-AI C1** : Pour TRADEX-AI, utiliser des profils **1 Day** avec des sous-périodes de **30 minutes** (configuration standard Market Profile). Cela produit 32 sous-périodes pour une session CME standard (16h de trading). Paramètres à documenter dans `settings.py`.
*Catégorie : structure_marche*

### D9482 — Tick Size obligatoire : précision du profil
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Sierra Chart exige que le `Tick Size` soit **correctement configuré** dans `Chart >> Chart Settings` avant d'utiliser le TPO Profile Chart. Un Tick Size incorrect provoque des profils mal formés ou très lents à calculer. Pour les marchés Forex, éviter `Letter/Block Price Increment in Ticks = 1`.
**TRADEX-AI C1** : Tick Sizes pour les actifs TRADEX : GC = 0.10 (10 cents/oz), CL = 0.01 (1 cent/baril), HG = 0.0005 (0.05 cent/lb), ZW = 0.25 (1/4 cent/boisseau). Ces valeurs doivent être configurées dans `settings.py` pour tout calcul de profil.
*Catégorie : indicateurs_tendance*

### D9483 — Peaks and Valleys TPO : niveaux de liquidité concentrée
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Les **Peaks** TPO sont des niveaux de prix ayant plus de TPOs que les N niveaux au-dessus et en dessous (N = `Peaks and Valleys Sensitivity`). Les **Valleys** ont moins de TPOs. Ces niveaux représentent des concentrations et raréfactions de temps passé — analogues aux POC locaux et zones de liquidité faible.
**TRADEX-AI C1** : Les Peaks TPO sont des zones de forte attraction de prix (return-to-value). Les Valleys sont des zones de transition rapide (peu de temps passé = faible liquidité). Dans TRADEX-AI, utiliser les Peaks comme niveaux de support/résistance secondaires pour le calcul du R/R.
*Catégorie : structure_marche*

### D9484 — Compatibilité études sur TPO Chart : restriction importante
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Seules 3 études sont compatibles avec le TPO Profile Chart : **Volume by Price**, **Countdown Timer**, et **Current Price Line**. Toute autre étude ajoutée à un chart TPO produira des résultats incorrects. L'étude `TPO Value Area Lines` ajoutée à un chart TPO ne correspond pas aux valeurs réelles du profil.
**TRADEX-AI C1** : TRADEX-AI ne doit pas calculer des indicateurs classiques (RSI, MA, Momentum) directement sur les données brutes d'un chart TPO Sierra Chart. Tous ces calculs doivent être effectués sur un chart standard séparé ou directement depuis les données NT8 JSON.
*Catégorie : structure_marche*

### D9485 — POC et VA : sources de divergence entre plateformes
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Les valeurs de POC et VA peuvent diverger entre plateformes à cause de : session times différents, données manquantes, paramétrage `Value Area %` différent, méthode de calcul (Count 2 Levels at a Time = Yes/No), `Letter/Block Price Increment in Ticks` différent.
**TRADEX-AI C1** : Pour reproductibilité, documenter **tous** les paramètres TPO dans `settings.py` : VA% = 70, session times CME exacts, Price Increment en ticks par actif, Count 2 Levels = No (défaut). Tout écart par rapport à ces paramètres doit être tracé dans `DETTE_TECHNIQUE.md`.
*Catégorie : structure_marche*

### D9486 — Session Times et Evening Session : impact sur le profil journalier
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Quand l'Evening Session est activée, le profil 1 Day **commence à l'heure de début de la session du soir** (ex : 17:00 ET pour CME). L'input `New Period at Day Session Start When Using Evening Session` = Yes crée deux profils séparés (jour + soir). L'input `Exclude Evening Session Profiles Except For Last Day` filtre les sessions du soir historiques.
**TRADEX-AI C4** : Pour GC et CL (marchés CME avec session électronique 23h/24h), définir clairement les heures de session dans `settings.py` : session principale = 08:30-15:15 ET, session électronique = 17:00-08:30 ET (lendemain). Impact direct sur le calcul des niveaux VA/POC utilisés dans TRADEX-AI.
*Catégorie : macro_evenements*

### D9487 — Opening Range : signal d'orientation de session
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : L'`Opening Range Time Length in Minutes` définit la durée de l'**Opening Range** (range de la première N minutes de session). Ce range est affiché comme barre verticale à gauche du profil quand `Highlight Opening Range on TPO Profiles` = Yes. Distinct de l'Initial Balance qui couvre les premières sous-périodes définies.
**TRADEX-AI C1/C4** : L'Opening Range des 30 premières minutes est un niveau structurel clé pour GC et CL. Un break de l'Opening Range High = biais haussier de session. Break de l'OR Low = biais baissier. Paramètre `OPENING_RANGE_MINUTES = 30` à ajouter dans `settings.py`.
*Catégorie : timing*

### D9488 — Closing Range : contexte de fin de session
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : L'`Closing Range Time Length in Minutes` définit la durée du **Closing Range** (range des dernières N minutes de session). Affiché comme barre verticale à droite du profil quand `Highlight Closing Range on TPO Profiles` = Yes.
**TRADEX-AI C4** : Le Closing Range sur GC (Or) est pertinent pour la corrélation avec le fixing PM LBMA (15:00 LDN = 10:00 ET). Un close fort dans la moitié haute du Closing Range confirme la force du mouvement journalier — signal de continuation pour la session suivante.
*Catégorie : timing*

### D9489 — Méthodes de calcul du Midpoint TPO : deux approches
🟢 **FAIT VÉRIFIÉ** (Source : tpo_market_profile.md) : Deux méthodes disponibles : (1) **Midpoint of TPO High and TPO Low** = (High + Low) / 2 du profil entier (équivalent au milieu du range) ; (2) **TPO Letter/Block Midpoint** = niveau de prix où le nombre de lettres/blocs au-dessus est égal ou presque égal au nombre en dessous (médiane pondérée par temps).
**TRADEX-AI C1** : La méthode 2 (TPO Letter/Block Midpoint) est plus informative car elle représente le prix médian pondéré par le temps passé — proche du concept Belkhayate de prix d'équilibre. Utiliser la méthode 2 dans les calculs TRADEX-AI. Paramètre `TPO_MIDPOINT_METHOD = 2` dans `settings.py`.
*Catégorie : structure_marche*

### D9490 — Rotation Factor : interprétation trading et seuils opérationnels
🟡 **SYNTHÈSE** (Source : tpo_market_profile.md) : Un Rotation Factor **positif et croissant** en cours de session = marché en tendance haussière avec extension des highs et lows. **Négatif et décroissant** = tendance baissière. **Proche de 0** = marché en balance / range. La valeur absolue reflète l'amplitude de la tendance.
**TRADEX-AI C1** : Règles opérationnelles pour TRADEX-AI : RF > +4 = tendance haussière confirmée → favoriser les entrées LONG sur signaux Belkhayate ; RF < -4 = tendance baissière confirmée → favoriser les entrées SHORT ; -3 ≤ RF ≤ +3 = marché en balance → appliquer les seuils de confirmation stricter (score ≥ 8.0/10 au lieu de 7.0). Seuils à calibrer par backtest Phase C.
*Catégorie : structure_marche*
