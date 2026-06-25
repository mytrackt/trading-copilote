# Extraction StockCharts — EquiVolume
**Source :** `bundles/stockcharts/equivolume.md` (HTTP 200 · ~6 600 car.) + 11 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D1691 → D1704 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/equivolume
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Illustrations of different types of EquiVolume boxes. | Calculation EquiVolume | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a high-low-close bar chart with volume. | Calculation EquiVolume | CERTIFIE (accord .md + HTML) |
| image_03.png | (EquiVolume boxes, même période) | Calculation EquiVolume [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | After breaking out of a falling wedge, CAT broke out... wide EquiVolume box | Support/Resistance Breaks | CERTIFIE (accord .md + HTML) |
| image_05.png | EquiVolume chart showing a downside support level break. | Support/Resistance Breaks | CERTIFIE (accord .md + HTML) |
| image_06.png | EquiVolume chart identifying a trend reversal. | Reversals | CERTIFIE (accord .md + HTML) |
| image_07.png | EquiVolume chart identifying a reversal of an uptrend with three boxes. | Reversals | CERTIFIE (accord .md + HTML) |
| image_08.png | The EquiVolume chart identifies support just above $9, followed by advance. | Volume Climax | CERTIFIE (accord .md + HTML) |
| image_09.png | The wide EquiVolume box represents support at around $16. | Volume Climax | CERTIFIE (accord .md + HTML) |
| image_10.png | SharpCharts chart settings for EquiVolume charts. | EquiVolume and SharpCharts | CERTIFIE (accord .md + HTML) |
| image_11.png | EquiVolume chart of SPY | EquiVolume and SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1691 — Définition : type de graphique intégrant le volume dans chaque période
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md) : Développé par Richard W. Arms Jr., l'EquiVolume est un tracé de prix incorporant le volume dans chaque période. Ressemble aux chandeliers, mais les bougies sont remplacées par des « boîtes » EquiVolume carrées ou rectangulaires. Les figures classiques (triangles, wedges, double tops) restent visibles, avec le bonus du volume intégré.
**TRADEX-AI C2** : Type de graphe volume (école Arms) ; candidat comme représentation order-flow visuelle, jamais comme déclencheur d'ordre. Non disponible nativement côté NT8/ATAS — à évaluer comme reconstruction ou simple inspiration de lecture volume.
*Catégorie : structure_marche*

---

### D1692 — Construction de la boîte : high = haut, low = bas, volume = largeur
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_01) : Une boîte EquiVolume a trois composantes — price high (borne haute), price low (borne basse), volume (largeur). Les boîtes sont noires quand la clôture est au-dessus de la clôture précédente, rouges quand en-dessous.
**TRADEX-AI C2** : Mapping déterministe (range vertical = amplitude prix ; largeur = volume ; couleur = sens clôture) ; codable comme rendu, mais reste une visualisation, pas un signal autonome.
*Catégorie : structure_marche*

---

### D1693 — Normalisation du volume en pourcentage de la période d'observation
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md) : Le volume est normalisé en pourcentage de la période look-back. Pour un graphe daily sur 4 mois, le volume de chaque jour est divisé par le volume total de la période ; la largeur de chaque boîte = % du volume total. Les jours à gros volume occupent plus d'espace horizontal que les jours à faible volume.
**TRADEX-AI C2** : Formule de normalisation déterministe (volume_jour / volume_période) ; calculable, mais dépend de la fenêtre look-back choisie (paramètre).
*Catégorie : indicateurs_tendance*

---

### D1694 — Axe des dates non uniforme (conséquence des largeurs variables)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_02, image_03) : À cause des largeurs variables, l'axe des dates n'est généralement pas uniforme. Certaines semaines s'étendent plus (boîtes larges), d'autres sont plus courtes (boîtes étroites). La page compare un bar chart high-low-close à axe normal puis la même période en boîtes EquiVolume.
**TRADEX-AI C2** : Propriété structurelle (axe temps déformé par le volume) ; impact sur tout alignement temporel avec d'autres séries — limite d'interopérabilité à noter.
*Catégorie : structure_marche*

---

### D1695 — Boîtes larges = volume élevé ; boîtes fines = volume faible
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_03) : « The wide boxes show relatively high-volume days, while the thin boxes show relatively low-volume days. »
**TRADEX-AI C2** : Lecture de base (largeur ∝ volume) ; primitive de lecture order flow réutilisable comme heuristique de pondération.
*Catégorie : structure_marche*

---

### D1696 — Validation des cassures : break sur fort volume > break sur faible volume
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md) : Le volume est important pour valider un mouvement, en particulier les cassures de support/résistance. « A break on low volume is not as convincing as a break on high volume. » Faible volume = intérêt tiède, pression faible ; fort volume = intérêt élevé, pression forte.
**TRADEX-AI C2** : Principe de confirmation par volume des cassures = filtre order flow directement transposable (cohérent avec la confirmation volume des figures chartistes du projet).
*Catégorie : signal*

---

### D1697 — Cassure de résistance confirmée par boîtes larges (exemple CAT / falling wedge)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_04) : Caterpillar (CAT) a formé un falling wedge début juillet et cassé la trend line avec la boîte EquiVolume la plus large depuis plus d'un mois. Une cassure au-dessus du plus haut de fin juin a été suivie d'un gap et d'une autre boîte large. La cassure finale (la plus large des deux mois, au-dessus de $38) a confirmé la plus forte pression acheteuse en deux mois. « Volume confirmed these breakouts. »
**TRADEX-AI C2** : Cas illustratif liant largeur de boîte et conviction de cassure ; valeur pédagogique, recoupe l'extraction Falling Wedge (D1711+). Aucun paramètre nouveau.
*Catégorie : signal*

---

### D1698 — Cassure de support confirmée par boîte large (exemple INTU)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_05) : Intuit (INTU) cassant le support avec une boîte EquiVolume large, montrant une forte pression vendeuse qui a brisé les plus bas de septembre.
**TRADEX-AI C2** : Cas symétrique (cassure baissière sur fort volume) ; confirme la lecture pression vendeuse via largeur de boîte.
*Catégorie : signal*

---

### D1699 — Retournement haussier signalé par une boîte large (exemple AA)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_06) : Les mouvements à fort volume peuvent signaler le début d'une tendance. Alcoa (AA) en repli de janvier à mars 2009 a touché un fond au-dessus de $5 puis cassé avec une boîte large (la plus large depuis des mois). « Strong buying pressure confirmed the reversal and foreshadowed a rally back to the January highs. »
**TRADEX-AI C2** : Heuristique de retournement (boîte exceptionnellement large au creux = entrée d'acheteurs) ; signal de structure, à confirmer par d'autres outils.
*Catégorie : signal*

---

### D1700 — Retournement baissier d'un uptrend par trois boîtes rouges larges (exemple GS)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_07) : Goldman Sachs (GS) — retournement d'un uptrend avec trois boîtes EquiVolume rouges, larges et longues, cassant le support à $210 ; pression vendeuse s'intensifiant. Le rebond ultérieur s'est fait sur boîtes plus étroites (volume plus faible) : volume haussier du rebond < volume baissier de la cassure → rebond sans conviction qui a échoué.
**TRADEX-AI C2** : Lecture comparative (volume up rebond vs volume down cassure) = primitive d'asymétrie order flow exploitable pour jauger la conviction d'un rebond.
*Catégorie : signal*

---

### D1701 — Volume climax : boîte exceptionnellement large (souvent plus large que haute)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md) : Les boîtes EquiVolume identifient les périodes de très fort volume = volume climax. Un selling climax typique = nouveau plus bas, plongeon intraday, forte reprise intraday avec bon volume. Un climax EquiVolume = boîte exceptionnellement large, souvent plus large que haute : faible variation de prix avec fort volume → indécision pouvant précéder un mouvement significatif.
**TRADEX-AI C2** : Définition opérationnelle du climax (largeur >> hauteur = beaucoup de volume / peu de prix) ; condition codable comme alerte d'indécision/épuisement.
*Catégorie : signal*

---

### D1702 — Boîte climax renforçant un support puis breakouts (exemple WFT)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_08) : Weatherford (WFT) trouvant support juste au-dessus de $9 (mi-janvier à début mars) ; boîte exceptionnellement large le 25 février renforçant le support et agissant comme volume climax. Les cassures suivantes à $11 et $13 ont ouvert la voie à une avance prolongée.
**TRADEX-AI C2** : Cas confirmant le rôle du climax dans la validation d'un support ; illustratif, aucun paramètre nouveau.
*Catégorie : signal*

---

### D1703 — Boîte large comme zone de support + falling channel (exemple AKAM)
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_09) : Akamai (AKAM) — gros gap baissier et boîte EquiVolume exceptionnellement large (plus carrée que rectangulaire) marquant un support à $16-$17. AKAM s'est stabilisé puis a gappé plus haut avec bon volume ; retour tester le support, formation d'un falling channel, test réussi du support et cassure de la résistance du canal. La cassure manquait de boîte large pour confirmation mais a tenu après test à $10.
**TRADEX-AI C2** : Nuance importante — une cassure SANS boîte large (sans confirmation volume) peut quand même tenir : la confirmation volume est forte mais non absolue. À pondérer, pas à ériger en critère éliminatoire.
*Catégorie : signal*

---

### D1704 — Synthèse d'usage et accès SharpCharts / scans
🟢 **FAIT VÉRIFIÉ** (Source : equivolume.md, image_10, image_11) : Les boîtes EquiVolume associent prix (high-low pour la longueur) et volume (largeur) : boîtes fines = faible volume, larges = fort volume, carrées/larges = fort volume avec faible variation de prix. Permettent de repérer figures, cassures S/R et retournements. Accès via Chart Type dans les Attributes (volume « off », « separate » ou « overlay »). EquiVolume n'est PAS disponible comme indicateur de scan ; l'idée peut être approchée en scannant certaines relations prix/volume.
**TRADEX-AI C2** : Récapitulatif des primitives de lecture ; limite outillage (pas scannable nativement) → toute implémentation côté TRADEX serait une reconstruction approximative.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1691 | Définition : graphe volume intégré (Arms) | 🟢 | C2 | structure_marche |
| D1692 | Boîte : high/low + largeur=volume + couleur=clôture | 🟢 | C2 | structure_marche |
| D1693 | Normalisation volume en % de la période | 🟢 | C2 | indicateurs_tendance |
| D1694 | Axe des dates non uniforme | 🟢 | C2 | structure_marche |
| D1695 | Largeur ∝ volume | 🟢 | C2 | structure_marche |
| D1696 | Cassure : fort volume > faible volume | 🟢 | C2 | signal |
| D1697 | Cassure résistance confirmée (CAT/falling wedge) | 🟢 | C2 | signal |
| D1698 | Cassure support confirmée (INTU) | 🟢 | C2 | signal |
| D1699 | Retournement haussier (AA) | 🟢 | C2 | signal |
| D1700 | Retournement baissier 3 boîtes rouges (GS) | 🟢 | C2 | signal |
| D1701 | Volume climax : largeur >> hauteur | 🟢 | C2 | signal |
| D1702 | Climax renforçant support (WFT) | 🟢 | C2 | signal |
| D1703 | Cassure sans boîte large peut tenir (AKAM) | 🟢 | C2 | signal |
| D1704 | Synthèse usage + accès SharpCharts/scans | 🟢 | C2 | structure_marche |

**Liens Belkhayate :** L'EquiVolume est un type de graphique de Richard Arms (StockCharts), PAS un élément de la méthode Belkhayate (⚫ — NON CONCERNÉ). Rapprochement indirect possible : la lecture volume/cassure recoupe la confirmation order flow (ATAS) du projet, mais l'attribuer à Belkhayate serait une hypothèse non affirmée par la source (⚫🔴).

**À vérifier (humain) :**
- Disponibilité outil : EquiVolume n'existe pas nativement dans NT8/ATAS ; toute implémentation = reconstruction (carbox + normalisation volume) → décider si pertinent vs Footprint/Delta déjà câblés (C2).
- D1693 — la normalisation dépend de la fenêtre look-back (paramètre non fixé par la source).
- D1703 — la source admet qu'une cassure SANS confirmation volume peut tenir : ne PAS ériger la confirmation volume en critère éliminatoire dur.
- Chiffres des exemples (CAT $38, INTU, AA $5, GS $210/$235/$345, WFT $9/$11/$13, AKAM $16-$17/$10) = valeurs historiques illustratives, non transposables en paramètres.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
