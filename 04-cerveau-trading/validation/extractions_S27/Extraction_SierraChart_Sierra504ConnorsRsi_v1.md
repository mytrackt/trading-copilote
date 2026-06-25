# Extraction SierraChart — RSI Connors (ID 504)
**Source :** `bundles/sierrachart/sierra_504_connors_rsi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** pas d'images dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9431 → D9450 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=504
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 449 (Connors RSI) — indicateur momentum composite tri-couche utilisable comme filtre directionnel C1 sur GC/CL/HG/ZW ; seuils suracheté/survendu configurables.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image présente dans le bundle) | — | — | — |

## DÉCISIONS

### D9431 — Connors RSI : définition et composantes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : Le Connors RSI est un oscillateur composite à 3 composantes : (1) RSI standard sur la série de prix (longueur configurable, par défaut Wilder MA), (2) RSI à 2 périodes sur la série Up-Down Length (nombre de barres consécutives en hausse ou en baisse), (3) Rate of Change exprimé en percentile sur `n_ROC` barres passées. La formule finale est la moyenne arithmétique de ces 3 termes.
**TRADEX-AI C1** : Indicateur directement utilisable dans le moteur Python comme filtre momentum sur actifs TRADING (GC, HG, CL, ZW) ; sa nature composite réduit les faux signaux par rapport à un RSI simple.
*Catégorie : indicateurs_momentum*

### D9432 — Paramètre RSI Length (n_RSI)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : `RSI Length` est le paramètre `n_RSI` contrôlant la longueur du RSI classique calculé sur l'Input Data. Par défaut Sierra Chart utilise la Wilders Moving Average, modifiable via `RSI Average Type`.
**TRADEX-AI C1** : Paramètre configurable dans `settings.py` — valeur suggérée à tester sur range bars NT8 : 3 (recommandation Connors Research originale) ou 14 (alignement méthode Belkhayate classique). À valider par backtest Phase C.
*Catégorie : indicateurs_momentum*

### D9433 — Paramètre Rate of Change Length (n_ROC)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : `Rate of Change Length` est `n_ROC`, le nombre de barres passées sur lequel le percentile de variation de prix est calculé. Ce percentile mesure quelle fraction des `n_ROC` barres précédentes avait une variation barre-à-barre inférieure à la variation courante.
**TRADEX-AI C1** : Paramètre à configurer dans `settings.py`. Valeur par défaut Connors : 100 barres. Plus n_ROC est long, plus le signal est lissé et moins réactif aux pointes de volatilité — pertinent pour GC (Or) qui a des gaps de session.
*Catégorie : indicateurs_momentum*

### D9434 — Up-Down Length (UDL) : comptage de tendance courte
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : L'Up-Down Length est une série dérivée qui compte, à chaque barre, le nombre de barres consécutives pendant lesquelles le prix monte (valeur positive) ou descend (valeur négative). Sur cette série, un RSI à 2 périodes est calculé, produisant un signal de persistance de tendance très court terme.
**TRADEX-AI C1** : Le RSI(UDL, 2) agit comme détecteur de retournement immédiat. Dans TRADEX-AI, cette composante permet de détecter les fins de micro-tendances intra-session sur CL (Pétrole) et GC (Or), renforçant ou inhibant un signal Belkhayate.
*Catégorie : indicateurs_momentum*

### D9435 — Ligne 1 Value et Ligne 2 Value : seuils de signal
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : Le Connors RSI affiche deux lignes horizontales configurables via `Line 1 Value` et `Line 2 Value`. Ces seuils délimitent les zones de surachat et de survente. Les niveaux classiques Connors Research sont 90 (surachat) et 10 (survente), mais ils peuvent être ajustés selon l'actif.
**TRADEX-AI C1** : Intégrer dans `settings.py` sous `CONNORS_RSI_OVERBOUGHT` et `CONNORS_RSI_OVERSOLD`. Valeurs de départ recommandées : 90/10 pour GC et CL, à calibrer. Un signal Belkhayate valide avec Connors RSI < 10 renforce la conviction ACHAT ; > 90 renforce VENTE.
*Catégorie : indicateurs_momentum*

### D9436 — RSI Average Type : choix de la MA sous-jacente
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : L'input `RSI Average Type` contrôle la méthode de lissage utilisée dans le calcul du RSI standard (composante 1). Par défaut : Wilder Moving Average (EMA avec alpha = 1/n). D'autres types de MA peuvent être sélectionnés via cet input.
**TRADEX-AI C1** : Conserver Wilder MA par défaut pour rester fidèle à la méthode Connors originale et faciliter la comparaison avec la littérature. Tout changement doit être documenté dans `settings.py` avec justification.
*Catégorie : indicateurs_momentum*

### D9437 — Composite Connors RSI : formule de calcul finale
🟢 **FAIT VÉRIFIÉ** (Source : sierra_504_connors_rsi.md) : La valeur finale est : `RSI_C = (RSI(X, n_RSI) + RSI(UDL(X), 2) + ROC_percentile(X, n_ROC)) / 3`. Chaque composante est normalisée entre 0 et 100, donc la valeur composite oscille aussi entre 0 et 100.
**TRADEX-AI C1** : La normalisation 0-100 facilite l'intégration dans la grille de scoring TRADEX-AI /10. Une lecture Connors RSI entre 20 et 80 est neutre ; en dehors de ces bornes, le signal contribue positivement à la grille Cercle C1.
*Catégorie : indicateurs_momentum*

### D9438 — Indépendance vis-à-vis d'autres études sur TPO
🔵 **ÉCOLE** (Source : sierra_504_connors_rsi.md) : Le Connors RSI (ID 504) est une étude standard Sierra Chart applicable sur tout type de chart (OHLC, Volume Bars, Range Bars). Il n'est pas lié au TPO Profile Chart et peut être ajouté à n'importe quel chart Sierra Chart classique.
**TRADEX-AI C1** : Applicable directement sur les Range Bars NT8 qui alimentent TRADEX-AI. Pas de dépendance TPO ni de contrainte de timeframe spécifique.
*Catégorie : indicateurs_momentum*

### D9439 — Spreadsheet disponible pour vérification des formules
🔵 **ÉCOLE** (Source : sierra_504_connors_rsi.md) : Sierra Chart propose une feuille de calcul `Momentum_Trend.62.scss` (pour l'étude connexe Momentum Trend) permettant de vérifier les formules en dehors de la plateforme. La documentation Connors RSI (ID 504) renvoie au fichier spreadsheet dédié.
**TRADEX-AI C1** : Utile pour valider l'implémentation Python indépendante du Connors RSI dans le moteur TRADEX-AI. Référence pour audit de fidélité des calculs.
*Catégorie : indicateurs_momentum*

### D9440 — Interprétation opérationnelle : signal de retournement court terme
🟡 **SYNTHÈSE** (Source : sierra_504_connors_rsi.md) : Connors RSI < 10 = survente extrême → contexte favorable à une entrée LONG. Connors RSI > 90 = surachat extrême → contexte favorable à une entrée SHORT ou sortie LONG. La robustesse est supérieure au RSI simple car trois mesures indépendantes convergent.
**TRADEX-AI C1** : Dans TRADEX-AI, utiliser comme filtre de timing d'entrée C1 : un signal Belkhayate valide (score ≥ 7.0/10) + Connors RSI en zone extrême = confiance rehaussée. Ne jamais utiliser seul — toujours en conjonction avec la règle 3/4 + 2/3.
*Catégorie : gestion_risque_entree*
