# Extraction StockCharts — Arms Index (TRIN)
**Source :** `bundles/stockcharts/arms_index_trin.md` (HTTP 200 · ~8 900 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D631 → D642 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/arms-index-trin
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label / Section | Statut |
|-------|-----------------|--------|
| image_01.png | How Do You Calculate the TRIN? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | How Do You Interpret the TRIN? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart Scaling [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Overbought/Oversold [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | Overbought/Oversold [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Charting the Arms Index on SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | Charting the Arms Index on SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D631 — Définition du TRIN (Arms Index)
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md) : Le Arms Index, aussi appelé TRIN (Short-Term TRading INdex), est un indicateur de breadth (largeur de marché) développé par Richard W. Arms en 1967. Il identifie les situations de court terme suracheté/survendu.
**TRADEX-AI C5** : Indicateur de sentiment/breadth basé sur les actions (NYSE/Nasdaq). Pertinence pour GC/HG/CL/ZW : INDIRECTE — sert de proxy du sentiment marché actions, pas un signal direct sur futures matières premières. Utilisable comme contexte C5 corroborant ES/VX.
*Catégorie : structure_marche*

---

### D632 — Formule de calcul du TRIN
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_01) : TRIN = (advances / declines) / (advancing volume / declining volume). Advances = nombre d'actions clôturant en hausse ; Declines = nombre clôturant en baisse ; Advancing/Declining Volume = volume total des hausses/baisses.
**TRADEX-AI C5** : Formule déterministe codable SI flux breadth NYSE/Nasdaq disponible. Note pertinence futures : NON applicable directement à GC/HG/CL/ZW (pas de breadth interne) — calcul réservé à l'indice actions de référence (ES/S&P 500) en C5.
*Catégorie : signal*

---

### D633 — Lecture inverse du TRIN vs marché
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md) : Les fortes hausses du marché s'accompagnent de TRIN relativement bas (le volume haussier écrase le volume baissier). Le TRIN évolue donc « à l'inverse » du marché : une forte journée haussière pousse le TRIN vers le bas, une forte journée baissière le pousse vers le haut.
**TRADEX-AI C5** : Règle d'interprétation inverse essentielle. En C5, un TRIN très bas = pression acheteuse actions (risk-on) ; un TRIN très haut = pression vendeuse (risk-off). Note futures : sert d'indice risk-on/risk-off pour pondérer le sentiment, pas un déclencheur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D634 — Seuil pivot à 1 (AD Ratio vs AD Volume Ratio)
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md) : Le TRIN est inférieur à 1 quand le AD Volume Ratio est supérieur au AD Ratio (force relative du volume), et supérieur à 1 quand le AD Volume Ratio est inférieur au AD Ratio (faiblesse relative). Lectures basses (<1) = force ; lectures hautes (>1) = faiblesse.
**TRADEX-AI C5** : Seuil pivot déterministe = 1,0. Note futures : utilisable comme bascule binaire force/faiblesse du marché actions dans le contexte C5, jamais comme signal d'ordre sur matières premières.
*Catégorie : signal*

---

### D635 — Exemple chiffré extrême (0,42 et 3,00)
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_02) : Quand le AD Volume Ratio a bondi à 7,17 (up-volume >> down-volume), le TRIN est tombé à 0,42 (bien sous 1). À l'inverse, quand le AD Volume Ratio a chuté à 0,05, le TRIN est monté à 3,00 (bien au-dessus de 1). Les lectures extrêmes du AD Volume Ratio produisent des TRIN extrêmes.
**TRADEX-AI C5** : Calibrage empirique des extrêmes. Note futures : repères 0,42 / 3,00 documentent l'amplitude possible du sentiment actions — contexte C5, sans transposition directe aux futures.
*Catégorie : signal*

---

### D636 — Échelle log vs arithmétique
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_03) : Le TRIN peut s'afficher en échelle semi-log ou arithmétique. En log, un mouvement de 0,50 à 1 (+100 %) occupe la même distance que de 1 à 2 (+100 %). L'échelle log lisse les fluctuations ; il n'y a pas de bon ou mauvais choix, c'est une préférence.
**TRADEX-AI C5** : Détail de représentation graphique. Note futures : sans impact sur le calcul du signal C5 — préférer l'échelle log pour symétriser hausses/baisses lors d'une visualisation éventuelle.
*Catégorie : structure_marche*

---

### D637 — Seuils suracheté/survendu (TRIN brut, échelle log)
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_04) : Sur le $TRIN NYSE quotidien (échelle log), les surges au-dessus de 3 sont jugées survendues (oversold) et les chutes sous 0,50 surachetées (overbought). Le TRIN brut est plus volatil et requiert une plage plus large.
🔵 **ÉCOLE** (Richard Arms) : Calibrage de l'auteur sur données NYSE.
**TRADEX-AI C5** : Seuils déterministes TRIN brut : oversold > 3 ; overbought < 0,50. Note futures : zones d'extrême de sentiment actions, exploitables en C5 comme alerte risk-on/risk-off, pas comme signal d'entrée GC/HG/CL/ZW.
*Catégorie : signal*

---

### D638 — Filtre de tendance par MM100
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_04) : Le NY Composite est en plus grande tendance haussière car au-dessus de sa MM100 ascendante. Dans ce cas, les niveaux survendus (oversold) sont privilégiés pour générer des signaux haussiers alignés sur la plus grande tendance.
🔵 **ÉCOLE** (Richard Arms / StockCharts) : Trader dans le sens de la tendance dominante.
**TRADEX-AI C5** : Règle de filtre tendanciel (MM100 de l'indice sous-jacent) avant d'exploiter un extrême TRIN. Note futures : cohérent avec la doctrine TRADEX « trader dans le sens de la tendance » — applicable conceptuellement, le TRIN restant un contexte C5.
*Catégorie : timing*

---

### D639 — Version lissée MM10 et seuils resserrés
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_05) : Sur le $TRINQ Nasdaq lissé en moyenne mobile simple 10 jours (SMA 10), la plage est plus étroite : survendu au-dessus de 1,20 et suracheté en dessous de 0,80. Le lissage réduit la plage nécessaire pour générer les signaux.
🔵 **ÉCOLE** (Richard Arms) : Variante medium-terme.
**TRADEX-AI C5** : Variante lissée déterministe : SMA10, oversold > 1,20 / overbought < 0,80. Note futures : signal de sentiment plus stable (medium terme) pour le contexte C5 ; moins de bruit que le TRIN brut.
*Catégorie : signal*

---

### D640 — Applicabilité multi-indices (S&P 500 / Nasdaq 100)
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md) : Bien que typiquement basé sur les données NYSE ou Nasdaq, l'Arms Index peut être calculé à partir des statistiques de breadth d'autres indices comme le S&P 500 ou le Nasdaq 100.
**TRADEX-AI C5** : Pertinent — le TRIN peut être calculé sur le S&P 500, qui est l'actif de CONFIRMATION ES du système. Note futures : permet un TRIN aligné sur ES (catégorie CONFIRMATION), renforçant la cohérence du sentiment C5 vis-à-vis de GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D641 — Caractère volatil et nécessité de confirmation
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md) : L'Arms Index est un indicateur de breadth volatil générant de nombreux signaux ; il est préférable de trader dans le sens de la tendance sous-jacente. Ce n'est qu'un seul indicateur : les chartistes doivent employer d'autres aspects de l'analyse technique pour confirmer ou réfuter les signaux.
🔵 **ÉCOLE** (Richard Arms / StockCharts) : Confirmation multi-indicateurs obligatoire.
**TRADEX-AI C5** : Garde-fou — le TRIN seul ne suffit jamais. Note futures : cohérent avec la grille déterministe /10 multi-cercles ; le TRIN n'est qu'un intrant C5 parmi d'autres, jamais critère unique.
*Catégorie : signal*

---

### D642 — Symboles StockCharts ($TRIN / $TRINQ) et tracé
🟢 **FAIT VÉRIFIÉ** (Source : arms_index_trin.md, image_06, image_07) : Les utilisateurs StockCharts tracent l'Arms Index pour le NYSE ($TRIN) et le Nasdaq ($TRINQ). Pour une échelle log, mettre l'Arms Index comme symbole principal puis cocher « log scale ». Des lignes horizontales (ex. 0,80 ; 1 ; 1,20 en valeurs séparées par virgules) délimitent les zones suracheté/survendu.
🟡 **CONVENTION** (StockCharts) : Tickers et procédure de tracé propres à la plateforme.
**TRADEX-AI C5** : Symboles de référence pour collecte de données ($TRIN NYSE, $TRINQ Nasdaq). Note futures : utile pour câbler une source de sentiment C5 ; non lié directement aux flux NT8/ATAS des futures.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Aspect | Contenu |
|--------|---------|
| Indicateur | Arms Index (TRIN), breadth / sentiment marché actions — Richard W. Arms, 1967 |
| Formule | (advances / declines) / (advancing volume / declining volume) |
| Pivot | 1,0 (au-dessus = faiblesse, en dessous = force ; lecture inverse du marché) |
| Seuils TRIN brut (log) | oversold > 3 · overbought < 0,50 |
| Seuils SMA10 | oversold > 1,20 · overbought < 0,80 |
| Filtre | trader dans le sens de la tendance (MM100 de l'indice sous-jacent) |
| Symboles | $TRIN (NYSE) · $TRINQ (Nasdaq) ; calculable sur S&P 500 (→ lien ES) |
| Cercle TRADEX | **C5 (sentiment/breadth)** uniquement |
| Pertinence futures GC/HG/CL/ZW | INDIRECTE — contexte risk-on/risk-off via marché actions ; jamais signal d'ordre direct |
| Belkhayate | NON CONCERNÉ (méthode prix/pivots, pas de breadth actions) |
| Décisions | D631 → D642 (12 décisions) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Le TRIN est un indicateur de sentiment du marché actions ; sa transposition aux futures matières premières est indirecte et doit rester confinée au cercle C5.
