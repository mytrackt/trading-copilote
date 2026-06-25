# Extraction StockCharts — Three Line Break Charts
**Source :** `bundles/stockcharts/three_line_break_charts.md` (HTTP 200) + 9 images certifiées
**Méthode images :** double ancrage · 9/9 certifiées · 0 à vérifier
**Décisions :** D4491 → D4510 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/three-line-break-charts.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Three Line Break = type de graphique japonais filtrant le bruit (comme Kagi/Renko), pertinent pour GC/HG/CL/ZW — identifie tendances pures sans distorsion temporelle ; utile pour TRADEX en complément des range bars NT8.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/lyJIaQw1B3Kxwygik9ou | Traditional candlestick chart shows 85 trading days between March 21 and July 20 | Construction | D4491 |
| /files/QubsfeS75o49DljN9WxD | Three Line Break chart condenses the information in a traditional candlestick chart | Construction | D4491 |
| /files/SAkiR6lf3CgnlRo3XTem | Two-line reversals (Dell Inc. DELL) | Two Line Reversals | D4494 |
| /files/3TiX6t9N0urLAZ2CpPa6 | Two-line reversals featuring black and white combinations (United Parcel UPS) | Two Line Reversals | D4495 |
| /files/nDMYICrJZhlzkXX7gMgk | Three Line Break chart showing move from downtrend to uptrend and back (Russell 2000 IWM) | Three Line Reversals | D4497 |
| /files/v6yZJ2n6C78vmvMvLkbd | Support and resistance levels in Three Line Break chart (Constellation Energy CEG) | Support and Resistance | D4499 |
| /files/Ui29PU1rbfLXYetGVqce | Symmetrical triangle support break in Vulcan Materials VMC (Three Line Break) | Classic Patterns | D4500 |
| /files/e9e8w2v9o0pukQGWx96B | Three-Line Break chart using SharpCharts | SharpCharts | D4502 |
| /files/RiMCp5vmZ2u0fR1drw9I | SharpChart settings for Three Line Break chart | SharpCharts | D4502 |

## DÉCISIONS

### D4491 — Three Line Break : graphique japonais ignorant le temps, basé uniquement sur le prix
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, images /files/lyJIaQw1B3Kxwygik9ou, /files/QubsfeS75o49DljN9WxD) : Les Three Line Break Charts sont d'origine japonaise. Ils ignorent le temps et ne changent que quand les prix bougent d'une certaine quantité (similaire aux Point & Figure Charts). Ils montrent une série de lignes verticales blanches (hausse) et noires (baisse). 85 chandeliers japonais → 44 lignes Three Line Break = compression et filtrage du bruit.
**TRADEX-AI C1** : Alternative aux range bars NT8 pour filtrer le bruit de marché sur GC/HG/CL/ZW. Les Three Line Break charts focalisent sur les mouvements de prix significatifs, aligné avec la philosophie Belkhayate (attendre le mouvement clair).
*Catégorie : structure_marche*

### D4492 — Construction : les "lignes" sont basées sur les prix de clôture, pas les hauts/bas
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md) : Trois clarifications de construction importantes : (1) les barres du graphique s'appellent "lignes" ; (2) les changements de ligne sont basés sur les PRIX DE CLÔTURE, pas le range haut-bas ; (3) les Three Line Break charts évoluent selon le PRIX, pas le TEMPS. Un nouveau jour sans mouvement significatif ne génère aucune ligne.
**TRADEX-AI C1** : Pour TRADEX : si implémenté sur GC, les signaux Three Line Break seraient basés sur clôtures, non sur les hauts/bas intraday. Compatible avec la lecture NT8 via data_reader.py qui lit les prix de clôture des barres.
*Catégorie : structure_marche*

### D4493 — Trois possibilités à chaque nouveau prix de clôture
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md) : À chaque nouveau prix de clôture, exactement 3 possibilités : (1) nouvelle ligne de même couleur si le prix s'étend dans la même direction ; (2) nouvelle ligne de couleur opposée si le changement de prix justifie un retournement ; (3) aucune nouvelle ligne si le prix ne s'étend pas ou si le mouvement est insuffisant pour justifier un retournement.
**TRADEX-AI C1** : Logique déterministe simple — 3 cas exhaustifs. Algorithme facilement codable dans le moteur TRADEX pour GC/HG/CL/ZW. Règle objective sans ambiguïté d'interprétation.
*Catégorie : indicateurs_tendance*

### D4494 — Retournement 2 lignes (Two-Line Reversal) : règle précise du point de retournement
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, image /files/SAkiR6lf3CgnlRo3XTem) : Si la ligne la plus récente est noire (baisse), le HAUT des 2 dernières lignes marque le point de retournement. Une clôture AU-DESSUS de ce haut génère une ligne blanche = retournement haussier. La ligne précédant la noire peut être blanche ou noire — seul le haut des 2 lignes compte. Démontré sur Dell Inc. (DELL) avec 3 retournements deux-lignes.
**TRADEX-AI C1** : Règle d'entrée précise et codable : si dernière ligne noire ET clôture > max(2 dernières lignes) → signal achat potentiel. Pour GC/HG/CL/ZW : point de retournement objectif et non subjectif.
*Catégorie : indicateurs_tendance*

### D4495 — Retournement 2 lignes haussier → baissier : règle symétrique
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, image /files/3TiX6t9N0urLAZ2CpPa6) : Si la ligne la plus récente est blanche (hausse), le BAS des 2 dernières lignes marque le point de retournement. Une clôture EN-DESSOUS de ce bas génère une ligne noire = retournement baissier. Démontré sur United Parcel Service (UPS) avec 3 retournements (combinaisons noir/blanc et deux blancs).
**TRADEX-AI C1** : Règle d'entrée short : si dernière ligne blanche ET clôture < min(2 dernières lignes) → signal vente potentiel. Symétrie parfaite haussier/baissier = algorithme simple à implémenter pour les 4 actifs tradables.
*Catégorie : indicateurs_tendance*

### D4496 — Three Line Break (3 lignes) : signal de retournement de tendance majeur
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md) : Le Three Line Break proprement dit = rupture de 3 lignes. Un retournement haussier se produit quand 3 lignes noires forment et qu'une seule ligne blanche brise le HAUT de ces 3 lignes. Un retournement baissier se produit quand 3 lignes blanches forment et qu'une seule ligne noire brise le BAS de ces 3 lignes. Ce signal 3-lignes indique un mouvement plus fort, pouvant signaler un retournement de tendance.
**TRADEX-AI C1** : Signal 3-lignes = signal de tendance majeur, différent du signal 2-lignes (correction/continuation). Pour TRADEX : le 3-Line Break sur GC/HG pourrait servir de filtre de tendance macro (C1) — ne prendre des longs que si le 3-Line Break est blanc, ne prendre des shorts que si noir.
*Catégorie : indicateurs_tendance*

### D4497 — Exemple IWM : cycle complet downtrend → uptrend → downtrend documenté
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, image /files/nDMYICrJZhlzkXX7gMgk) : Sur Russell 2000 ETF (IWM), le Three Line Break montre un cycle complet : (1) downtrend débute 6 juin avec première ligne noire ; (2) pas de nouvelle ligne le 7 juin (mouvement insuffisant) ; (3) nouvelle ligne noire le 8 juin ; (4) le 21 juin, clôture dépasse le haut des 3 lignes noires → signal uptrend ; (5) 28 juin, 5 jours plus tard, nouvelle ligne blanche ; (6) uptrend inverse quand prix passe sous le bas des 3 lignes blanches.
**TRADEX-AI C1** : Démonstration que le graphique Three Line Break filtre efficacement les faux mouvements intermédiaires (le 7 juin n'est pas affiché). Pour GC : utile pour éviter les whipsaws intraday et se concentrer sur les vrais retournements de tendance.
*Catégorie : structure_marche*

### D4498 — Absence de ligne = information : le non-événement est significatif
🟡 **SYNTHÈSE** (Source : three_line_break_charts.md) : Le fait qu'aucune ligne ne soit ajoutée certains jours est en lui-même informatif : le marché est en consolidation ou en mouvement insuffisant. Ce filtrage temporel est une caractéristique distinctive des graphiques Three Line Break vs les graphiques temporels classiques.
**TRADEX-AI C1** : Philosophie alignée avec Belkhayate : attendre le signal clair, ne pas trader la consolidation. Le "silence" du Three Line Break correspond au signal "ATTENDRE" de TRADEX.
*Catégorie : structure_marche*

### D4499 — Supports et résistances : hauts et bas de réaction clairement identifiables
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, image /files/v6yZJ2n6C78vmvMvLkbd) : Les Three Line Break Charts produisent des hauts et bas de réaction clairs pour baser la résistance et le support. L'analyse chartiste s'applique de la même façon qu'en graphique barre ou chandelier. Exemple Constellation Energy (CEG) : zone de résistance claire par 3 hauts de réaction, puis cassure en avril avec forte progression. Un canal/flag descendant visible en février.
**TRADEX-AI C1** : Les niveaux de support/résistance identifiés sur Three Line Break sont objectifs et non subjectifs (basés sur les hauts/bas réels des lignes). Compatible avec les Pivots Belkhayate (C1) pour confirmer des niveaux clés sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4500 — Patterns classiques applicables : Double Bottom, Double Top, H&E, Triangles
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md, image /files/Ui29PU1rbfLXYetGVqce) : Les patterns classiques (Double Bottom, Double Top, Head-and-Shoulders, Triangles) se forment sur les Three Line Break Charts. Exemple Vulcan Materials (VMC) : Symmetrical Triangle janvier→mai, puis rupture du support avec sharp decline en mai.
**TRADEX-AI C1** : Les patterns chartistes universels sont reconnaissables sur Three Line Break. Pour TRADEX : si implémenté, le moteur pourrait détecter des Triangles ou H&E sur Three Line Break pour renforcer la confiance du signal sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D4501 — Avantage principal : filtrage du bruit + identification facilité de la tendance
🟢 **FAIT VÉRIFIÉ** (Source : three_line_break_charts.md) : Contrairement aux Point & Figure (boîte fixe), le Three Line Break utilise un seuil variable basé sur le range des 2 dernières lignes. Ce range variable permet une adaptation au contexte de marché. Le filtrage du bruit facilite : (1) identification de la tendance sous-jacente ; (2) repérage des hauts/bas importants ; (3) classification uptrend (HH+HL) ou downtrend (LL+LH).
**TRADEX-AI C1** : Pour GC (Or), les Three Line Break Charts pourraient servir de référence de tendance macro (timeframe supérieur) pour calibrer le biais directionnel avant d'analyser les signaux intraday Belkhayate.
*Catégorie : indicateurs_tendance*

### D4502 — Implémentation SharpCharts : sélection dans Chart Type → Attributes
🔵 **ÉCOLE** (Source : three_line_break_charts.md, images /files/e9e8w2v9o0pukQGWx96B, /files/RiMCp5vmZ2u0fR1drw9I) : Dans SharpCharts de StockCharts.com, les Three Line Break Charts s'activent en sélectionnant "Three Line Break" dans "Chart Type" dans la section "Attributes" des paramètres du graphique.
**TRADEX-AI C1** : Information d'implémentation spécifique à StockCharts. Pour TRADEX/NinjaTrader : la logique Three Line Break peut être codée directement en Python dans le moteur TRADEX sans dépendance externe.
*Catégorie : configuration*

### D4503 — Référence bibliographique : "Beyond Candlesticks" de Steve Nison (chapitre dédié)
🔵 **ÉCOLE** (Source : three_line_break_charts.md) : Steve Nison couvre les Three Line Break Charts dans un chapitre entier de "Beyond Candlesticks". Il couvre aussi les Renko Charts, Kagi Charts et l'utilisation des moyennes mobiles par les traders japonais. Référence académique validée pour l'approfondissement.
**TRADEX-AI C1** : Source bibliographique à potentiellement intégrer dans la KB via PIPELINE_ENRICHISSEMENT_KB. Nison est une autorité sur les techniques japonaises d'analyse de prix, alignées avec l'approche Belkhayate (méthode également d'inspiration asiatique).
*Catégorie : configuration*

