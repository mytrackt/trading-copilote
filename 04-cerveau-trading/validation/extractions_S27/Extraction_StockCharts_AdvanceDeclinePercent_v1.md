# Extraction StockCharts — Advance-Decline Percent

**Source :** `bundles/stockcharts/advance_decline_percent.md` (HTTP 200 · ~7 200 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D511 → D521 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-percent
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

⚫🔴 **PERTINENCE LIMITÉE FUTURES** : indicateur de BREADTH (largeur de marché) actions — il agrège advances/declines des composants d'un ETF sectoriel/indiciel (XLK, XLI, SPDRs). NON applicable directement à un future individuel (GC/HG/CL/ZW), qui n'a pas de « composants ». Pertinence indirecte uniquement via ES (S&P 500) comme actif de CONFIRMATION (C5 sentiment / C7 corrélations). Belkhayate NON CONCERNÉ.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | AD Percent - Chart 1 | How Do You Calculate Advance-Decline Percent? | CERTIFIE (accord .md + HTML) |
| image_02.png | AD Percent - Chart 2 | AD Line | CERTIFIE (accord .md + HTML) |
| image_03.png | AD Percent - Chart 3 | Moving Averages | CERTIFIE (accord .md + HTML) |
| image_04.png | AD Percent - Chart 4 | AD Percent Using SharpCharts | CERTIFIE (accord .md + HTML) |
| image_05.png | AD Percent - Chart 5 | AD Percent Using SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D511 — Définition AD Percent (breadth)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md) : « The Advance-Decline Percent is a breadth indicator that measures the percentage of net advances. » Calculé après clôture par StockCharts pour les neuf sector SPDRs et plusieurs ETF indiciels.
**TRADEX-AI C5/C7** : indicateur de participation interne d'un groupe d'actions. Pertinence limitée futures — exploitable seulement sur ES (proxy S&P 500) en CONFIRMATION, jamais sur GC/HG/CL/ZW directement.
*Catégorie : indicateurs_tendance*

---

### D512 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md) : `AD Percent = (Advances Less Declines) / Total Issues`. Exemples littéraux : (70 − 7) / 77 = +81,81 % ; (12 − 65) / 77 = −68,83 %.
**TRADEX-AI C5** : formule déterministe et reproductible. Note pertinence limitée futures : nécessite un panier de composants (Total Issues), inexistant pour un contrat future isolé. Réservé à l'analyse ES.
*Catégorie : indicateurs_tendance*

---

### D513 — Bornes et ligne médiane
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_01) : AD Percent fluctue entre −100 % et +100 % avec zéro comme ligne médiane. +100 % = toutes les valeurs montent ; −100 % = toutes baissent. « Extreme readings are the exception rather than the norm. »
**TRADEX-AI C5** : oscillateur borné, lecture intuitive du sentiment d'un secteur. Pertinence limitée futures — sert au mieux de contexte macro/sentiment via ES.
*Catégorie : indicateurs_tendance*

---

### D514 — Seuils de participation ±70 %
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md) : un avance avec AD Percent > +70 % reflète une force étendue (la plupart des titres participent) ; un déclin avec AD Percent < −70 % reflète une faiblesse étendue.
**TRADEX-AI C5** : seuils littéraux de confirmation de participation. Note futures : applicable uniquement comme jauge de conviction sur ES, pas comme déclencheur d'ordre sur les actifs tradables.
*Catégorie : signal*

---

### D515 — AD Line (cumul)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_02) : l'AD Line est la mesure cumulative de l'AD Percent (ex. $XLIADP). Les valeurs de l'échelle de droite « are not important » (dépendent de la date de départ) ; se concentrer sur les mouvements de la ligne et appliquer l'analyse technique de base.
**TRADEX-AI C7** : ligne de tendance cumulative pour repérer trend et divergences. Pertinence limitée futures — outil de structure interne actions, transposable uniquement à ES.
*Catégorie : indicateurs_tendance*

---

### D516 — Divergences haussières AD Line
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_02) : deux divergences haussières décrites sur XLI — l'indice fait un plus-bas plus bas tandis que l'AD Line tient et forme un plus-bas plus haut (moindre participation à la baisse) ; le breakout suivant déclenche le signal haussier.
**TRADEX-AI C7** : la divergence breadth précède le retournement de prix. Note futures : concept transposable conceptuellement à ES, non à un future isolé (pas d'AD Line possible).
*Catégorie : signal*

---

### D517 — Oscillateur par moyenne mobile + whipsaws
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_03) : une moyenne mobile (ex. SMA 21 jours) appliquée à l'AD Percent crée un oscillateur autour de zéro. Avertissement littéral : « Be careful with oscillator divergences because they occur quite often and don't always produce good trading signals. »
**TRADEX-AI C5** : garde-fou anti-faux-signaux explicite. Pertinence limitée futures — vaut comme principe de prudence général, applicable à tout oscillateur du moteur.
*Catégorie : indicateurs_tendance*

---

### D518 — Seuils ±5 % vs croisements de zéro
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_03) : SMA 21 jours du $XLKADP, lignes à −5 %, 0 % et +5 %. Les croisements de la ligne zéro sont « quite susceptible to whipsaws and bad signals » ; mieux vaut des seuils au-dessus/en-dessous de zéro — ici > +5 % = haussier, < −5 % = baissier.
**TRADEX-AI C5** : convention de filtrage par bande morte autour de zéro pour réduire les faux signaux.
*Catégorie : signal*

---

### D519 — Breadth anticipe le prix (« inside first »)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md) : « Changes sometimes occur on the inside first - using breadth indicators can help chartists anticipate these changes. » Le prix du sous-jacent reflète l'extérieur ; l'AD Percent reflète ce qui se passe sous la surface.
**TRADEX-AI C7** : justification de l'usage des indicateurs de largeur comme signaux avancés. Pertinence limitée futures — l'avance ne vaut que pour des indices/ETF, donc ES côté CONFIRMATION.
*Catégorie : structure_marche*

---

### D520 — Réglages SharpCharts (histogram / invisible / cumulative)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md, image_04, image_05) : données brutes affichées en « histogram » (rouge) ; oscillateur de largeur en mettant le type sur « invisible » puis en ajoutant une moyenne mobile en Overlays ; AD Line via type « cumulative » (noir).
**TRADEX-AI C5** : note d'implémentation propre à l'outil StockCharts. Pertinence limitée futures et plateforme — non transposable tel quel à NT8/ATAS ; valeur documentaire uniquement.
*Catégorie : indicateurs_tendance*

---

### D521 — Instabilité des données long terme
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_percent.md) : les calculs reposent sur la liste des titres alors en vigueur dans le sous-jacent/indice, qui change ; la breadth d'il y a deux ans repose sur les avoirs d'alors. À considérer pour les graphiques long terme.
**TRADEX-AI C7** : mise en garde sur la non-stationnarité de l'historique breadth. Note futures : renforce le caractère indirect/contextuel — ne pas backtester un signal AD Percent sur historique long sans précaution.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D511 → D521 (11) |
| Images certifiées | 5/5 |
| Cercles | C5 (sentiment/participation) · C7 (corrélations/structure) |
| Catégories | indicateurs_tendance · signal · structure_marche |
| Actif applicable | ES uniquement (CONFIRMATION) — JAMAIS GC/HG/CL/ZW directement |
| Belkhayate | NON CONCERNÉ |
| Pertinence futures | LIMITÉE — breadth actions, transposable seulement à ES en contexte macro/sentiment |
| Cas « à vérifier » | Aucun (5/5 images certifiées, tous faits littéraux 🟢) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Indicateur de largeur de marché actions : valeur indirecte pour TRADEX-AI, jamais déclencheur d'ordre sur les actifs tradables.
