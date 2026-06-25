# Extraction StockCharts — Linear Regression Forecast (LRF)

**Source :** `bundles/stockcharts/linear_regression_forecast.md` (HTTP 200 · ~5 475 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D2431 → D2440 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/linear-regression-forecast
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | How to add the Linear Regression Forecast overlay | Chart LRF With StockChartsACP | CERTIFIÉ |
| image_02.png | Changing Linear Regression Forecast parameters | Chart LRF With StockChartsACP | CERTIFIÉ |
| image_03.png | The Linear Regression Forecast overlay in action | Chart LRF With StockChartsACP | CERTIFIÉ |

## DÉCISIONS

### D2431 — Définition et objet du LRF
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md) : Le Linear Regression Forecast (LRF) repose sur la régression linéaire, outil statistique pour prévoir des valeurs de prix à partir de valeurs passées. Le LRF sert à déterminer la tendance sous-jacente et à repérer quand les prix sont sur-étendus à la hausse ou à la baisse.
**TRADEX-AI C1** : Overlay de projection statistique de tendance + détection de sur-extension ; candidat comme indicateur de tendance/extrême sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D2432 — Méthode des moindres carrés (least squares)
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md) : Le LRF utilise la méthode des moindres carrés : une droite tracée à travers les prix qui s'ajuste au mieux aux données, minimisant la distance entre prix et trendline résultante.
**TRADEX-AI C1** : Fondement statistique déterministe (régression OLS) ; calcul reproductible.
*Catégorie : indicateurs_tendance*

---

### D2433 — LRF est une série mobile, pas une droite fixe
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md) : Au lieu d'être tracé en droite fixe, le LRF est une série mobile qui trace, pour chaque point, la valeur prévue de la trendline dérivée. Il suit donc le marché comme une moyenne mobile. Le dernier point de la trendline est la valeur prévue.
**TRADEX-AI C1** : Comportement de type moyenne mobile (série glissante) ; le dernier point = projection à exploiter comme signal directionnel.
*Catégorie : indicateurs_tendance*

---

### D2434 — Formule : équation de droite y = mx + b
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md) : La formule du LRF se base sur la pente d'une droite : `y = mx + b`. La pente (m) et l'ordonnée à l'origine (b) déterminent la droite de meilleur ajustement. (StockCharts ne détaille pas davantage la formule.)
**TRADEX-AI C1** : Squelette calculatoire (pente + intercept) ; renvoie à l'indicateur Slope pour le détail.
*Catégorie : indicateurs_tendance*

---

### D2435 — Ajout de l'overlay dans StockChartsACP
🟡 **CONVENTION** (Source : linear_regression_forecast.md, image_01) : Ajout dans StockChartsACP : (1) saisir le symbole de l'actif/indice/ETF ; (2) dans Chart Settings, dérouler la liste des Standard Indicators ; (3) sélectionner Linear Regression Forecast. L'icône de réglages permet de changer couleur, style et autres paramètres.
**TRADEX-AI C1** : Procédure outil StockCharts ; informationnel, non porté NT8.
*Catégorie : configuration*

---

### D2436 — Paramètre Periods (défaut 14)
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md, image_02) : Periods — le réglage par défaut est 14, modifiable à tout nombre de barres souhaité pour calculer le LRF.
**TRADEX-AI C1** : Période par défaut = 14 barres ; valeur de référence si LRF intégré.
*Catégorie : configuration*

---

### D2437 — Paramètre « Calculated From » (champ de prix)
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md, image_02) : « Calculated From » sélectionne la valeur source du calcul : open, high, low, close, (H+L)/2, (H+L+C)/3, (H+L+2C)/4, (O+H+L+C)/4.
**TRADEX-AI C1** : Choix du champ de prix (incl. typical price) ; paramètre d'entrée du calcul.
*Catégorie : configuration*

---

### D2438 — Paramètres d'affichage (Line Style, Opacity, Colors, Add Overlays)
🟡 **CONVENTION** (Source : linear_regression_forecast.md, image_02) : Réglages visuels : Line Style (solid, thin, thick, dashed…), Opacity (slider de transparence), Colors (couleur du LRF), et « Add Overlays » (menu d'overlays additionnels pour aider à confirmer la direction de tendance).
**TRADEX-AI C1** : Options cosmétiques/d'overlay StockCharts ; informationnel, non porté NT8.
*Catégorie : configuration*

---

### D2439 — Usage : le dernier point prévoit la direction
🟢 **FAIT VÉRIFIÉ** (Source : linear_regression_forecast.md, image_03) : « The last point forecasts price direction. » Dans l'exemple, la tendance court terme est haussière ; si le prix continue de monter, on peut ajouter d'autres indicateurs/overlays (ex. moyennes mobiles) pour confirmer force et/ou momentum, ce qui aide à décider d'acheter, conserver ou vendre.
**TRADEX-AI C1** : Signal directionnel = dernier point du LRF, à confirmer par d'autres indicateurs ; cohérent avec confirmation multi-cercles.
*Catégorie : signal*

---

### D2440 — Lien Belkhayate (régression / projection)
⚫🔴 **NON VÉRIFIÉ — Belkhayate** (Source : aucune dans linear_regression_forecast.md) : Le document ne mentionne ni Belkhayate ni l'Énergie/MFI. Aucun lien direct entre le LRF et la méthode Belkhayate n'est attesté. Toute assimilation LRF ↔ médiane/canal de régression Belkhayate serait une inférence non sourcée.
**TRADEX-AI C1/⚫** : Ne PAS rattacher le LRF à un élément Belkhayate sans validation humaine ; statut bloquant tant que non tranché.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2431 → D2440 (10) — plage cible D2431..2450 non remplie : page courte (~5 475 car.), pas de padding |
| Images | 3/3 certifiées |
| Tags dominants | 🟢 littéral (7) · 🟡 convention (2) · ⚫🔴 Belkhayate non vérifié (1) |
| Cercle | C1 (projection de tendance par régression linéaire, type moyenne mobile) |
| Belkhayate | ⚫🔴 D2440 : aucun lien attesté, ne rien inférer |
| Actifs | Aucun exemple chiffré ; page générique ; aucun GC/HG/CL/ZW |
| Cas à vérifier | D2440 (lien Belkhayate à trancher humainement). Source mince : StockCharts ne divulgue pas la formule complète (renvoie à Slope) — formule détaillée à compléter via la page Slope si LRF intégré. |

> ⚠️ Extraction BRUT, zone validation/, NON fusionnée. Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
