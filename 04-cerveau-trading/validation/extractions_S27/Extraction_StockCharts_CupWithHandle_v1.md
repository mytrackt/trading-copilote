# Extraction StockCharts — Cup With Handle
**Source :** `bundles/stockcharts/cup_with_handle.md` (HTTP 200 · ~5 800 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1411 → D1424 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/cup-with-handle
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Cup With Handle pattern. | What Is the Cup With Handle Pattern? | CERTIFIE (accord .md + HTML) |
| image_02.png | A Cup With Handle pattern in EMC. | What Is the Cup With Handle Pattern? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1411 — Nature et origine du Cup With Handle
🔵 **ÉCOLE (O'Neil)** (Source : cup_with_handle.md) : Le Cup With Handle est une figure de continuation **haussière** qui marque une période de consolidation suivie d'un breakout. Développé par William O'Neil, introduit dans son livre de 1988 *How to Make Money in Stocks*. La figure a deux parties — la coupe (cup) et l'anse (handle).
**TRADEX-AI structure_marche** : Figure de continuation haussière candidate pour qualifier une reprise de tendance sur GC/HG/CL/ZW ; à traiter comme couche analytique structurelle, jamais comme déclencheur d'ordre automatique.
*Catégorie : structure_marche*

---

### D1412 — Anatomie de la figure (cup + handle)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md, image_01) : La coupe se forme après une avance et ressemble à un bol ou à un rounding bottom (creux arrondi). Lorsque la coupe est complétée, un trading range se développe sur le côté droit, formant l'anse. Un breakout subséquent hors du trading range de l'anse signale une continuation de l'avance précédente.
**TRADEX-AI structure_marche** : Séquence à 3 temps (avance → coupe arrondie → anse → cassure) ; détectable comme enchaînement géométrique sur graphique.
*Catégorie : structure_marche*

---

### D1413 — Condition de tendance préalable
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Pour qualifier comme figure de continuation, une tendance préalable doit exister. Idéalement la tendance devrait avoir quelques mois. Si la tendance est trop mature, moins de chances que la figure marque une continuation (moins de potentiel haussier restant).
**TRADEX-AI structure_marche** : Pré-requis de contexte directionnel ; filtre à appliquer avant de valider une coupe — ne pas chercher la figure hors tendance établie.
*Catégorie : configuration*

---

### D1414 — Forme de la coupe (U et non V)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : La coupe doit être en forme de U et ressembler à un bol / rounding bottom. Un creux en V serait considéré comme un retournement trop brutal pour qualifier. La forme « U » plus douce garantit que la coupe est une figure de consolidation avec un support valide au fond du « U ». La figure parfaite aurait des sommets égaux des deux côtés, mais ce n'est pas toujours le cas.
**TRADEX-AI structure_marche** : Critère de qualité géométrique (U vs V) ; mesurable via la courbure / durée du creux pour rejeter les rebonds trop brusques.
*Catégorie : configuration*

---

### D1415 — Profondeur de la coupe (retracement)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Idéalement, la profondeur de la coupe devrait retracer 1/3 ou moins de l'avance précédente. Le retracement peut toutefois aller de 1/3 à 1/2 sur des marchés volatils et des sur-réactions. Dans des situations extrêmes, le retracement maximal pourrait être de 2/3, ce qui est conforme à la théorie de Dow.
**TRADEX-AI structure_marche** : Bande de retracement quantifiée (33 % idéal, 50 % toléré, 67 % extrême) ; paramétrable comme seuil de validation/rejet de la coupe.
*Catégorie : configuration*

---

### D1416 — Caractéristiques de l'anse (handle)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Après le sommet du côté droit de la coupe, un pullback forme l'anse. Parfois l'anse ressemble à un drapeau (flag) ou un fanion (pennant) en pente descendante ; d'autres fois c'est juste un court pullback. L'anse représente la dernière consolidation avant le grand breakout et peut retracer jusqu'à 1/3 de l'avance de la coupe, mais généralement pas plus. Plus le retracement est petit, plus la formation est haussière et plus le breakout est significatif.
**TRADEX-AI configuration** : L'anse = phase finale de consolidation ; profondeur ≤ 1/3 de l'avance de la coupe comme critère de qualité — anse peu profonde = signal plus fort.
*Catégorie : configuration*

---

### D1417 — Durée de la figure
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : La coupe peut durer d'un à six mois, parfois plus sur graphiques hebdomadaires. L'anse peut durer d'une à plusieurs semaines et est idéalement complétée en une à quatre semaines.
**TRADEX-AI structure_marche** : Bornes temporelles indicatives ; à transposer/échelonner selon le timeframe Belkhayate (15min / Range Bar) plutôt que de copier les durées en jours.
*Catégorie : configuration*

---

### D1418 — Confirmation par le volume au breakout
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Il devrait y avoir une augmentation substantielle du volume lors du breakout au-dessus de la résistance de l'anse.
**TRADEX-AI structure_marche** : Le volume expansif au franchissement est le critère de confirmation ; mappable sur les données order-flow (ATAS) plutôt que sur le seul prix.
*Catégorie : signal*

---

### D1419 — Calcul de l'objectif de prix (target)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : L'avance projetée après le breakout peut être estimée en mesurant la distance entre le sommet droit de la coupe et le fond de la coupe.
**TRADEX-AI structure_marche** : Règle de projection déterministe (hauteur de la coupe reportée depuis le breakout) ; utilisable pour pré-calculer un take-profit théorique et le R/R.
*Catégorie : gestion_risque_entree*

---

### D1420 — Primauté de l'essence sur les détails
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Comme pour la plupart des figures, capturer l'essence de la figure est plus important que les particularités. La coupe est une consolidation en bol et l'anse est un court pullback suivi d'un breakout avec volume en expansion. Un retracement de coupe de 62 % peut ne pas remplir les exigences mais peut tout de même capturer l'essence de la figure.
**TRADEX-AI structure_marche** : Avertissement contre la rigidité paramétrique ; impose une logique de score graduée plutôt qu'un test booléen strict des seuils.
*Catégorie : configuration*

---

### D1421 — Exemple EMC : tendance et coupe
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md, image_02) : EMC a établi sa tendance haussière en avançant d'environ 10 $ à plus de 30 $ en cinq mois, puis a entamé un pullback/consolidation. Le déclin d'avril fut net mais les plus bas se sont étendus sur deux mois pour former le bol marquant la consolidation ; le support a été trouvé sur les plus bas de février 1999.
**TRADEX-AI structure_marche** : Illustration empirique d'une coupe valide (durée multi-mois, support historique réutilisé) ; sert d'exemple de calibration visuelle.
*Catégorie : configuration*

---

### D1422 — Exemple EMC : profondeur et anse réelle
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md, image_02) : Le plus bas de la coupe a retracé 42 % de l'avance précédente ; le titre a culminé à 32,69 $ pour compléter la coupe. L'anse a démarré en juillet ; un déclin brutal en août a fait retracer l'anse de plus de 1/3 de l'avance de la coupe, mais une reprise rapide a ramené le titre dans les limites normales de l'anse en une semaine — l'essence de la formation restait valide malgré ce déclin brutal.
**TRADEX-AI configuration** : Cas réel où un dépassement temporaire de seuil (anse > 1/3) n'invalide pas la figure si l'essence est préservée — argument pour une validation tolérante.
*Catégorie : configuration*

---

### D1423 — Exemple EMC : breakout et confluence CMF
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Début septembre 2000, le titre a cassé la résistance de l'anse avec un gap up et une expansion de volume. De plus, le Chaikin Money Flow a bondi au-dessus de +20 %. La cible projetée (~9 points depuis le breakout vers 32 $) a été facilement atteinte les mois suivants.
**TRADEX-AI structure_marche** : Confluence gap + volume + flux monétaire (CMF > +20 %) comme faisceau de confirmation ; modèle de multi-confirmation transposable à la grille /10.
*Catégorie : signal*

---

### D1424 — Protocole de trading (FAQ)
🟢 **FAIT VÉRIFIÉ** (Source : cup_with_handle.md) : Une fois la figure repérée, il est préférable d'attendre que le prix casse hors de l'anse avant d'entrer en position longue. Avant cela, s'assurer que le volume de trading est fort — cela confirme que le prix suivra à la hausse. (FAQ : figure haussière de continuation ; la tendance préalable ne devrait avoir que quelques mois.)
**TRADEX-AI structure_marche** : Règle d'entrée explicite (attendre la cassure confirmée + volume fort) ; aucune entrée anticipée — cohérent avec l'exigence projet de confirmation avant signal.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1411 → D1424 (14 décisions) |
| Images certifiées | 2/2 |
| Catégories couvertes | structure_marche · configuration · signal · gestion_risque_entree |
| Cercle dominant | structure_marche (figure chartiste) |
| Lien Belkhayate | NON CONCERNÉ (figure O'Neil, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Figure issue de la méthode O'Neil (CANSLIM), aucun rapport affirmé avec la méthode Belkhayate.
