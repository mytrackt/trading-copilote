# Extraction StockCharts — TTM Squeeze
**Source :** `bundles/stockcharts/ttm_squeeze.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D4731 → D4750 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ttm-squeeze
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : TTM Squeeze identifie les compressions de volatilité précédant des breakouts puissants — directement applicable sur GC/CL/HG qui alternent consolidation et mouvements directionnels forts.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/pRGTtjTRhj5eZksSH7MA | Vue d'ensemble TTM Squeeze indicator | Introduction | D4731 |
| /files/hOUwt96OSR0G00EoXYwK | SharpCharts TTM Squeeze section | Using with SharpCharts | D4748 |
| /files/zwlEP9YGjyG51TBlHm99 | SharpCharts paramètres (20,2.0,20,1.5,20) | Using with SharpCharts | D4748 |
| /files/teyB9kAu9xhr8lBkAs3q | StockChartsACP TTM Squeeze | Using with ACP | D4749 |
| (image supplémentaire non labelisée) | — | — | — |

## DÉCISIONS

### D4731 — Définition TTM Squeeze : volatilité + momentum combinés
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md, image /files/pRGTtjTRhj5eZksSH7MA) : TTM Squeeze est un indicateur combinant volatilité et momentum, développé par John Carter (Trade the Markets / Simpler Trading). Il capitalise sur la tendance des prix à faire des breakouts puissants après une consolidation en range serré.
**TRADEX-AI C1** : Indicateur directement aligné avec la méthode Belkhayate (compression → explosion) — applicable sur GC/HG/CL/ZW pour détecter les coils avant breakout. Pertinence haute C1.
*Catégorie : configuration*

### D4732 — Composante volatilité : Bollinger Bands vs Keltner Channels
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Le composant volatilité du TTM Squeeze compare les Bollinger Bands (BB) aux Keltner Channels (KC). Si BB sont entièrement à l'intérieur des KC → squeeze ON (compression faible volatilité). Si BB sortent des KC → squeeze OFF (volatilité en expansion, breakout probable).
**TRADEX-AI C1** : Cette dualité BB/KC est la mécanique clé — sur GC (Or), les périodes de squeeze prolongé précèdent souvent des mouvements directionnels de 50-100 points. Codable comme détecteur de setup en Niveau 1 Python.
*Catégorie : structure_marche*

### D4733 — Signal visuel : points rouges (squeeze ON) et verts (squeeze OFF)
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Sur la ligne zéro de l'indicateur, des points signalent l'état du squeeze : point rouge = squeeze ON (volatilité comprimée), point vert = squeeze OFF (volatilité en expansion, breakout en cours).
**TRADEX-AI C1** : Dans le dashboard React TRADEX, le passage de point rouge à vert sur GC/CL doit déclencher une alerte visuelle pour Abdelkrim (mode Manuel) ou le Niveau 2 de filtrage (mode Auto).
*Catégorie : configuration*

### D4734 — Paramètres Bollinger Bands par défaut : 20 périodes, 2 écarts-types
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Carter utilise les paramètres BB standards : 20 périodes et 2 écarts-types. Ces valeurs sont ajustables selon les besoins du trader.
**TRADEX-AI C1** : Paramètres de départ pour GC/HG/CL/ZW sur range bars NT8 — à valider par backtest avant de verrouiller pour TRADEX.
*Catégorie : configuration*

### D4735 — Keltner Channels version originale Carter (1960, Keltner)
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Carter utilise la formule originale des Keltner Channels de Chester W. Keltner (1960), avec 20 périodes et multiplicateur ATR 1.5. ATTENTION : différente de la formule Raschke (1980s) utilisée ailleurs sur StockCharts.
**TRADEX-AI C1** : Règle d'implémentation critique : si TRADEX intègre le TTM Squeeze, utiliser la formule Keltner originale (1960) avec ATR×1.5, PAS la version Raschke — sinon le squeeze ne se déclenche pas aux bons niveaux.
*Catégorie : configuration*

### D4736 — Condition squeeze ON : double condition stricte
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Squeeze ON si ET SEULEMENT SI les deux conditions suivantes sont simultanément vraies : (1) Upper BB < Upper KC ET (2) Lower BB > Lower KC. Si une seule condition est fausse → squeeze OFF.
**TRADEX-AI C1** : Logique booléenne claire, directement codable en Python : `squeeze_on = (upper_bb < upper_kc) and (lower_bb > lower_kc)`. Applicable sur tous les actifs TRADEX.
*Catégorie : configuration*

### D4737 — Histogramme momentum : direction du breakout
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Le TTM Squeeze inclut un oscillateur momentum lissé pour indiquer la direction probable du breakout. Histogramme au-dessus de zéro et en hausse (barres bleu clair) = opportunité LONG ; en-dessous de zéro et en baisse (barres rouge foncé) = opportunité SHORT.
**TRADEX-AI C1** : Le squeeze (volatilité) + direction momentum = signal actionnable. Sur GC/CL : squeeze OFF + histogramme haussier = setup ACHETER candidat pour le Niveau 2 TRADEX.
*Catégorie : indicateurs_momentum*

### D4738 — Calcul histogramme momentum : Donchian midline + SMA + régression linéaire
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Calcul en 4 étapes : (1) Donchian midline 20 périodes = (plus haut 20 périodes + plus bas 20 périodes) / 2 ; (2) SMA20 des clôtures ; (3) Delta = Close − (Donchian midline + SMA20) / 2 ; (4) Régression linéaire sur les deltas pour lisser l'histogramme.
**TRADEX-AI C1** : Formule précise pour l'implémentation Python — la régression linéaire finale (non standard) est ce qui distingue cet histogramme d'un simple MACD. Requiert `numpy.polyfit()` ou équivalent.
*Catégorie : indicateurs_momentum*

### D4739 — Code couleur de l'histogramme
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Barres au-dessus de zéro = bleues ; barres en-dessous de zéro = rouges. Barre plus haute que la précédente = couleur claire (bleu clair, rouge clair) ; barre plus basse que la précédente = couleur foncée (bleu foncé, rouge foncé). 4 états visuels distincts.
**TRADEX-AI C1** : Dans le dashboard React TRADEX, reproduire ce code couleur 4 états pour GC/HG/CL/ZW — l'état "bleu clair" (momentum haussier croissant) est le plus actionnable pour entrée LONG.
*Catégorie : configuration*

### D4740 — Recommandation Carter : acheter sur le premier point vert
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Carter recommande explicitement : acheter sur le PREMIER point vert après un ou plusieurs points rouges. C'est le moment où la volatilité se libère pour la première fois après la compression.
**TRADEX-AI C1** : Règle d'entrée concrète pour TRADEX : transition rouge→vert du squeeze + histogramme positif = setup ACHETER prioritaire sur GC/CL. À coder comme condition de Niveau 1 Python.
*Catégorie : gestion_risque_entree*

### D4741 — Durée typique du mouvement post-squeeze : 8-10 barres
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Les mouvements de prix après un squeeze font typiquement 8 à 10 barres. Quand l'histogramme change de direction et revient vers zéro = signal de sortie.
**TRADEX-AI C1** : Règle de gestion de position pour TRADEX : sur GC/CL, après entrée sur premier point vert, prévoir exit quand histogramme TTM retourne vers zéro, typiquement dans les 8-10 barres — à paramétrer dans risk_manager.py.
*Catégorie : gestion_position_active*

### D4742 — Règle d'exit Carter : 2 barres de couleur inversée consécutives
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Carter recommande de vendre quand on observe 2 barres consécutives de la nouvelle couleur. Exemple : après un mouvement haussier (barres bleu clair), vendre à l'apparition de 2 barres bleu foncé consécutives (momentum au-dessus de zéro mais décroissant).
**TRADEX-AI C1** : Règle d'exit quantitative et codable : 2 barres bleu foncé consécutives sur GC/CL = signal de sortie LONG. Plus conservateur que d'attendre le passage sous zéro — préserve plus de profit.
*Catégorie : gestion_position_active*

### D4743 — Confirmation multi-timeframes renforce le signal
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Si un squeeze se déclenche simultanément sur un graphique journalier ET horaire, le signal est plus fort que sur un seul timeframe. Carter recommande explicitement de vérifier plusieurs timeframes pour confirmation.
**TRADEX-AI C1** : Aligne avec la règle TRADEX 3/4 + 2/3 — un squeeze TTM aligné sur daily ET range bars NT8 pour GC constitue une confirmation inter-timeframe, renforçant la conviction du signal.
*Catégorie : gestion_risque_entree*

### D4744 — Utilisation conjointe avec d'autres indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : "Traders should use the TTM Squeeze indicator in conjunction with other indicators and analysis techniques." Avertissement explicite contre l'utilisation isolée.
**TRADEX-AI C1** : Principe fondamental TRADEX confirmé — le TTM Squeeze est un outil parmi les 7 Cercles, jamais un signal autonome.
*Catégorie : gestion_risque_entree*

### D4745 — Paramètres par défaut complets : (20,2.0,20,1.5,20,20)
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : Les paramètres par défaut sur SharpCharts sont (20,2.0,20,1.5,20,20) : BB(20,2.0) + KC original(20,1.5,20) + histogramme momentum 20 périodes.
**TRADEX-AI C1** : Valeurs de départ pour l'implémentation TRADEX sur tous les actifs — à tester sur range bars NT8 spécifiques à chaque actif (GC, HG, CL, ZW peuvent nécessiter des ajustements).
*Catégorie : configuration*

### D4746 — TTM Squeeze applicable sur tous les timeframes
🟢 **FAIT VÉRIFIÉ** (Source : ttm_squeeze.md) : "The TTM Squeeze indicator can be used in many timeframes." Pas de restriction particulière de timeframe.
**TRADEX-AI C1** : Applicable sur les range bars NT8 utilisées par TRADEX — contrairement à certains indicateurs calibrés uniquement pour le daily.
*Catégorie : configuration*

### D4747 — Scan LONG : squeeze vient de se déclencher + histogramme > 0 et en hausse
🔵 **ÉCOLE** (Source : ttm_squeeze.md) : Scan TTM pour aller long : TTM Squeeze = true ET yesterday's TTM Squeeze = false (premier vert) ET TTM Squeeze Hist > 0 ET TTM Squeeze Hist > yesterday's TTM Squeeze Hist. Quadruple condition.
**TRADEX-AI C1** : Logique de scan directement transposable en Python pour Niveau 1 TRADEX : `squeeze_fired and momentum_positive and momentum_rising` sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D4748 — Scan SHORT : squeeze déclenché + histogramme < 0 et en baisse
🔵 **ÉCOLE** (Source : ttm_squeeze.md, images /files/hOUwt96OSR0G00EoXYwK et /files/zwlEP9YGjyG51TBlHm99) : Scan TTM pour shorter : TTM Squeeze = true ET yesterday's false ET Hist < 0 ET Hist < yesterday's Hist. Condition symétrique du scan LONG.
**TRADEX-AI C1** : Condition de SHORT sur GC/HG/CL/ZW : `squeeze_fired and momentum_negative and momentum_falling` — à coder en Niveau 1 Python pour le mode Auto.
*Catégorie : configuration*

### D4749 — Disponible sur SharpCharts et StockChartsACP (plugin)
🔵 **ÉCOLE** (Source : ttm_squeeze.md) : TTM Squeeze disponible nativement sur SharpCharts. Sur StockChartsACP, nécessite l'installation du "Advanced Indicator Pack" (plugin gratuit).
**TRADEX-AI C1** : Information de référence plateforme — pour TRADEX, l'implémentation est Python native, pas dépendante de StockCharts.
*Catégorie : configuration*

### D4750 — Volatilité TTM : mécanique coil/spring typique des marchés matières premières
🟡 **SYNTHÈSE** (Source : ttm_squeeze.md) : La logique du TTM Squeeze (compression → explosion) est particulièrement adaptée aux marchés de matières premières qui alternent entre phases de range (consolidation saisonnière, attente macro) et phases de tendance forte (annonces COT, événements géopolitiques).
**TRADEX-AI C1** : Sur GC (Or) : phases pré-FOMC souvent en squeeze → explosion post-annonce. Sur CL (Pétrole) : accumulation avant rapports EIA → breakout. Le TTM Squeeze est un détecteur de setup prioritaire pour le News Gate TRADEX.
*Catégorie : macro_evenements*
