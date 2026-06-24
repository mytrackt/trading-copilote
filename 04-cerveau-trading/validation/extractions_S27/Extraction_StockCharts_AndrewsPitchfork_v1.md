# Extraction StockCharts — Andrews' Pitchfork
**Source :** `bundles/stockcharts/andrews_pitchfork.md` (HTTP 200 · ~6 500 car.) + 8 images certifiées
**Méthode images :** double ancrage · 8/8 certifiées
**Décisions :** D591 → D602 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/andrews-pitchfork
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | An example of how to apply Andrews' Pitchfork in a stock's price chart | Applying Andrews' Pitchfork | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a downward-sloping Andrews' Pitchfork | Applying Andrews' Pitchfork | CERTIFIE (accord .md + HTML) |
| image_03.png | Flexibility with Point 1 of Andrews' Pitchfork | Flexibility with Point 1 [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | An example of a chart with two possible Andrews' Pitchforks | Flexibility with Point 1 | CERTIFIE (accord .md + HTML) |
| image_05.png | An example of Andrews' Pitchfork acting as support or resistance levels | Support, Resistance, and Reversal | CERTIFIE (accord .md + HTML) |
| image_06.png | Here, you see two Andrews' Pitchforks that formed after sharp advances | Support, Resistance, and Reversal | CERTIFIE (accord .md + HTML) |
| image_07.png | The lower and upper trigger lines are trendlines that extend from point 1 | Trigger Lines | CERTIFIE (accord .md + HTML) |
| image_08.png | Draw Andrews' Pitchfork lines on a chart by selecting the three points | Using Andrews' Pitchfork With SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D591 — Définition de l'Andrews' Pitchfork (3 lignes)
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_01) : Andrews' Pitchfork est un outil de canal de tendance composé de trois lignes — une ligne médiane centrale et deux lignes de tendance parallèles équidistantes de part et d'autre. Elles sont tracées en sélectionnant trois points, basés sur des plus-hauts/plus-bas de réaction (pivot points) de gauche à droite.
**TRADEX-AI C1** : Outil de structure de marché : canal de tendance à trois lignes ; les lignes externes balisent support/résistance potentiels, la médiane sert d'axe de tendance.
*Catégorie : structure_marche*

---

### D592 — Construction de la ligne médiane et de la pente
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_01) : Le point 1 marque le départ de la ligne médiane ; les points 2 et 3 définissent la largeur du canal. La médiane part du point 1 et bissecte le segment entre les points 2 et 3, ce qui contrôle la pente (steepness). Les lignes externes sont prolongées parallèlement à la médiane.
**TRADEX-AI C1** : Géométrie de tracé déterministe : médiane = point 1 → milieu(point 2, point 3) ; lignes externes parallèles. Implémentable une fois les pivots Belkhayate identifiés.
*Catégorie : structure_marche*

---

### D593 — Le point 1 détermine la pente du canal
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_01) : La pente de la Pitchfork dépend du placement du point 1. Un point 1 plus tardif/haut (ex. le plus-bas de juillet plutôt que de juin) produit une médiane plus raide tout en continuant à bissecter le segment points 2-3.
**TRADEX-AI C1** : Paramètre de sensibilité : le choix du pivot 1 module la pente ; à exposer comme variable d'analyse, pas comme constante figée.
*Catégorie : structure_marche*

---

### D594 — Canal descendant (downward-sloping)
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_02) : La Pitchfork s'applique aussi en tendance baissière : la médiane part du point 1, bissecte le segment points 2-3, et les lignes externes restent parallèles et équidistantes. Un point 1 plus tardif rend la médiane plus raide.
**TRADEX-AI C1** : Outil symétrique haussier/baissier — applicable aux deux directions de tendance sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D595 — Réalisme de la pente : ni trop raide ni trop plate
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_03) : La médiane doit parfois être ajustée pour une pente réaliste : une Pitchfork trop raide sera facilement cassée, une trop plate ne capturera pas la tendance.
**TRADEX-AI C1** : Garde-fou de validité : rejeter les canaux dont la pente est extrême (trop raide → faux breakouts ; trop plate → non significatif).
*Catégorie : structure_marche*

---

### D596 — Validation d'une Pitchfork par contact répété des lignes
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_04) : Sur Intuit (INTU), la Pitchfork rouge trop raide n'a pas inversé la tendance lors d'un passage sous la ligne basse ; la Pitchfork bleue plus plate a été confirmée quand le prix a trouvé résistance sur la ligne haute et support sur la ligne basse.
**TRADEX-AI C1** : Critère de confirmation : un canal n'est jugé valide qu'après contacts confirmés support haut/résistance bas ; les pentes raides sont plus facilement cassées (analogie trend lines).
*Catégorie : signal*

---

### D597 — Rôles support/résistance en tendance haussière
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_05) : En uptrend, la ligne basse agit comme support définissant la tendance globale, la ligne haute comme résistance, et la médiane définit la force de la tendance.
**TRADEX-AI C1** : Cartographie des niveaux : ligne basse = S de tendance, ligne haute = R, médiane = jauge de force.
*Catégorie : structure_marche*

---

### D598 — La médiane comme jauge de force et signal de faiblesse
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_05) : Le prix doit atteindre régulièrement la médiane pendant un uptrend. L'incapacité à atteindre cette ligne révèle une faiblesse sous-jacente pouvant préfigurer un retournement (cas Ciena/CIEN : médiane = résistance, atteinte quelques fois pour confirmer la tendance).
**TRADEX-AI C3** : Indicateur de confirmation de tendance : le non-retour à la médiane = signal d'affaiblissement à intégrer comme alerte de retournement potentiel.
*Catégorie : signal*

---

### D599 — Cassure de ligne devenant résistance/support inversé
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_05) : CIEN a cassé la ligne basse par un fort déclin en novembre ; cette cassure a tenu, la ligne de tendance se transformant ensuite en résistance.
**TRADEX-AI C1** : Principe de polarité : après cassure, l'ancien support devient résistance (et inversement) — règle de retest classique.
*Catégorie : structure_marche*

---

### D600 — Identification de corrections après fortes avancées
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_06) : Sur CSX Corp, deux corrections après fortes avancées ont été identifiées par la Pitchfork. Le maintien du prix au-dessus de la médiane (en août) a montré de la force menant à un breakout ; un passage sous la médiane suivi d'une récupération a précédé une cassure de résistance.
**TRADEX-AI C1** : La Pitchfork sert à encadrer les phases de correction post-impulsion ; tenue au-dessus de la médiane = force, breakout probable.
*Catégorie : structure_marche*

---

### D601 — Trigger lines : signaux d'achat/vente
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_07) : Les trigger lines partent du point 1. La trigger line haute descend du point 1 à travers le pic (point 3) : une cassure au-dessus est un signal d'achat. La trigger line basse monte du point 1 à travers le creux (point 2) : une cassure en-dessous est un signal de vente. Les signaux Pitchfork arrivent plus tôt que ceux des trend lines normales.
**TRADEX-AI C1** : Mécanisme de déclenchement directionnel : cassure trigger haute = signal long, cassure trigger basse = signal short — plus précoce que trend lines classiques (à soumettre à la grille /10, jamais ordre auto).
*Catégorie : signal*

---

### D602 — Nature subjective du tracé : jugement requis
🟢 **FAIT VÉRIFIÉ** (Source : andrews_pitchfork.md, image_08) : Il n'existe pas de règles strictes pour le placement des points ; le chartiste doit utiliser jugement et expérience. La pente dépend surtout du point 1, parfois ajusté pour un canal réaliste. Sur SharpCharts : Annotate → Line Studies → Andrews' Pitchfork → sélectionner les trois points.
**TRADEX-AI C1** : ⚫🔴 Limite d'automatisation : le tracé est subjectif (pas de règle dure de placement) — l'outil reste une aide d'analyse semi-manuelle, jamais une source de signal automatique.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D591 → D602 (12 décisions) |
| Images certifiées | 8/8 |
| Cercles touchés | C1 (structure/S-R), C3 (confirmation médiane) |
| Catégories | structure_marche (9), signal (3) |
| Lien Belkhayate | ⚫🔴 thème proche (lignes médianes/canaux) — non affirmé |
| Actifs | GC · HG · CL · ZW (applicable, non spécifique source) |
| Cas « à vérifier » | Aucun (8/8 images certifiées, faits littéraux) |

> ⚠️ Extraction BRUTE éducative. Andrews' Pitchfork = outil d'analyse de structure/canaux. Tracé subjectif (D602) : aide semi-manuelle uniquement, jamais signal automatique. Aucune exécution d'ordre. Lien Belkhayate non affirmé.
