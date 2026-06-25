# Extraction StockCharts — Ease of Movement (EMV)

**Source :** `bundles/stockcharts/ease_of_movement_emv.md` (HTTP 200 · ~11 100 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 7/7 certifiées · 0 à vérifier
**Décisions :** D1611 → D1621 · **Page :** chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ease-of-movement-emv
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **NATURE** : EMV est un **oscillateur basé sur le volume (C2)** développé par Richard Arms, qui quantifie la relation prix/volume (« facilité » du mouvement). Calculable sur tout instrument disposant de volume — donc applicable aux futures TRADING (GC·HG·CL·ZW) sur les données NT8/ATAS. Outil de **confirmation**, non autonome. Aucun lien Belkhayate affirmé par la source (mais l'idée « facilité du mouvement » est proche de la notion d'Énergie Belkhayate ⚫ — non tranché côté projet).

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | Spreadsheet | Calculating the EMV | D1613 |
| image_02 | Chart 1 | Interpreting the EMV | D1614 |
| image_03 | Chart 2 | Interpreting the EMV | D1615 |
| image_04 | Chart 3 | Confirming Other Signals | D1617 |
| image_05 | Chart 4 | Confirming Other Signals | D1617 |
| image_06 | Chart 5 | Using with SharpCharts | D1620 |
| image_07 | Chart 6 | Using with SharpCharts | D1620 |

---

## DÉCISIONS

### D1611 — Définition et origine de l'EMV
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md) : Ease of Movement (EMV) est un **oscillateur basé sur le volume** fluctuant **au-dessus et en dessous de la ligne zéro**, développé par **Richard Arms** pour mesurer la « facilité » du mouvement de prix. Il prolonge les graphiques **EquiVolume** d'Arms en quantifiant la relation prix/volume. Le prix avance avec relative facilité quand l'oscillateur est en **territoire positif**, et décline avec relative facilité quand il est en **territoire négatif**.
**TRADEX-AI C2** : Brique volume/momentum — lecture binaire au-dessus/en dessous de zéro pour la facilité directionnelle du mouvement.
*Catégorie : indicateurs_tendance*

---

### D1612 — Formule EMV (distance, box ratio, lissage 14)
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md) : Trois composantes — distance parcourue, volume, range haut-bas.
`Distance Moved = ((H + L)/2 - (Prior H + Prior L)/2)`
`Box Ratio = ((V/100 000 000)/(H - L))`
`1-Period EMV = Distance Moved / Box Ratio`
`14-Period EMV = moyenne mobile simple 14 périodes du 1-period EMV`
La **Distance Moved** (numérateur) compare le point médian (H+L)/2 courant à celui de la période précédente : positive si le médian monte, négative s'il descend. Le **Box Ratio** (dénominateur) divise le volume par 100 000 000 pour rester homogène avec les autres nombres.
**TRADEX-AI C2** : Formule déterministe codable sur données NT8/ATAS (H, L, V par période).
*Catégorie : indicateurs_tendance*

---

### D1613 — Sémantique du Box Ratio (range vs volume)
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md, image_01) : Volume relativement **faible** + range haut-bas **large** → dénominateur (Box ratio) plus petit → **EMV plus grand** : large range à faible volume implique un mouvement de prix **facile** (peu de volume a suffi à bouger le prix). Inversement, range **étroit** sur **fort** volume → dénominateur plus grand → **EMV plus petit** : mouvement **difficile** (beaucoup de volume pour peu de range).
**TRADEX-AI C2** : Cœur interprétatif — l'EMV mesure le ratio « amplitude de prix obtenue par unité de volume ».
*Catégorie : indicateurs_tendance*

---

### D1614 — Interprétation : petites valeurs EMV (mouvement difficile)
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md, image_02) : Exemple QQQ (1-period EMV) : deux petites valeurs EMV (une légèrement positive, une légèrement négative) avec volume **au-dessus de la moyenne** mais range **modeste/faible** → le prix a eu du **mal à bouger** malgré un volume relativement élevé.
**TRADEX-AI C2** : Brique de lecture — valeur EMV proche de zéro à fort volume = absence de progression, signal d'épuisement potentiel.
*Catégorie : signal*

---

### D1615 — Interprétation : valeurs extrêmes (~±3, mouvement facile)
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md, image_02, image_03) : EMV proche de **-3** (très négatif) = volume faible + large range → prix décline avec **facilité**, peu/pas de pression acheteuse. EMV proche de **+3** = volume faible + large range → prix avance avec facilité, peu/pas de pression vendeuse. Le graphique Jabil Circuit (JBL) illustre l'**EMV 14 périodes** (moyenne mobile simple 14 de chaque EMV période).
**TRADEX-AI C2** : Valeurs extrêmes = mouvement directionnel facile ; le lissage 14 périodes réduit le bruit.
*Catégorie : signal*

---

### D1616 — EMV n'est pas autonome : confirmation uniquement
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md) : EMV est **mieux utilisé pour confirmer** d'autres indicateurs ou l'analyse graphique — **ce n'est PAS un indicateur autonome**. La composante « Distance Moved » est le moteur positif/négatif : EMV est généralement positif quand le médian monte, négatif quand il descend, donc l'EMV **suit globalement le prix** ; l'ampleur dépend du Box ratio. On peut l'utiliser pour confirmer un breakout haussier (territoire positif) ou un breakdown baissier (territoire négatif).
**TRADEX-AI C2** : Garde-fou — n'utiliser EMV qu'en confirmation d'un signal de prix/structure, jamais seul pour générer un ordre.
*Catégorie : gestion_risque_entree*

---

### D1617 — Exemples de confirmation (MOS, VLO)
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md, image_04, image_05) : Mosaic (MOS) : EMV s'est détérioré pendant deux mois et est passé en négatif en mars, confirmant le breakdown de support début avril ; puis amélioration fin mai→début juin vers le positif, accompagnant un inverse head-and-shoulders et une cassure de résistance à 50 $. Valero Energy (VLO) : signaux EMV **confirmés par le RSI** et le prix — EMV a cassé son plus-bas de fin février et plongé en négatif fin mars (RSI au plus bas depuis début janvier) ; à la cassure de résistance de mi-juillet, EMV était fermement positif et le RSI a confirmé.
**TRADEX-AI C2** : Illustration de l'usage combiné EMV + structure de prix + RSI pour valider breakout/breakdown.
*Catégorie : configuration*

---

### D1618 — Bottom line : oscillateur momentum lié au prix
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md) : EMV combine **direction du prix** et **volume** en un oscillateur de momentum basé sur le volume. Étroitement lié aux variations de prix, il **suit de près** le prix du sous-jacent. Il sert surtout à **confirmer** les signaux du prix ou d'autres indicateurs. Un EMV plus lisse s'obtient en **allongeant la période** de look-back.
**TRADEX-AI C2** : Réglage — augmenter la période pour lisser ; rappel que EMV reste confirmatoire.
*Catégorie : indicateurs_tendance*

---

### D1619 — Paramétrage SharpCharts (positionnement, moyenne mobile)
🟡 **CONVENTION** (Source : ease_of_movement_emv.md, image_06, image_07) : Dans SharpCharts, EMV est dans la section « indicators » ; les réglages se changent dans « parameters ». L'indicateur peut être positionné « behind price », « above » ou « below » la fenêtre principale ; on peut ajouter une moyenne mobile via les options « advanced ».
**TRADEX-AI** : Détail spécifique à l'outil StockCharts — non transposable tel quel ; informatif seulement.
*Catégorie : configuration*

---

### D1620 — Scans EMV (croisement de zéro) et garde-fou volume
🟢 **FAIT VÉRIFIÉ** (Source : ease_of_movement_emv.md) : Deux scans fournis — « EMV Crosses above Zero » (`[Daily EMV(14) crosses 0]`, négatif→positif) et « EMV Crosses below Zero » (`[0 crosses Daily EMV(14)]`, positif→négatif), avec filtres `SMA(20,Volume) > 100000` et `SMA(60,Close) > 20`. **Garde-fou** : le volume quotidien étant incomplet en séance, baser les scans d'indicateurs basés volume (EMV, Accumulation/Distribution, OBV, PVO) sur le « **Last Market Close** ».
**TRADEX-AI C2** : Signaux codables (croisement de la ligne zéro) ; garde-fou de fraîcheur des données aligné avec le Staleness Monitor — ne pas calculer EMV sur du volume intraséance incomplet.
*Catégorie : signal*

---

### D1621 — Rattachement Belkhayate (Énergie) — non tranché
⚫🔴 **NON VÉRIFIÉ / BELKHAYATE** (Source : aucune mention explicite dans ease_of_movement_emv.md) : La notion de « facilité du mouvement » (prix obtenu par unité de volume) évoque conceptuellement l'**Énergie Belkhayate**. Or côté projet l'Énergie = **MFI standard** (mémoire projet), et l'arbitrage MFI vs proxy n'est **pas tranché**. La source **ne mentionne PAS Belkhayate** : aucun rattachement affirmé.
**TRADEX-AI** : NE PAS assimiler EMV à l'Énergie Belkhayate sans validation humaine. Brique candidate à verser dans A_VERIFIER_HUMAIN si un rapprochement est envisagé.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie | Actifs |
|---|----------|-----|--------|-----------|--------|
| D1611 | Définition / origine Arms | 🟢 | C2 | indicateurs_tendance | GC·HG·CL·ZW |
| D1612 | Formule (distance/box/14) | 🟢 | C2 | indicateurs_tendance | GC·HG·CL·ZW |
| D1613 | Sémantique Box Ratio | 🟢 | C2 | indicateurs_tendance | GC·HG·CL·ZW |
| D1614 | Petites valeurs = difficile | 🟢 | C2 | signal | GC·HG·CL·ZW |
| D1615 | Valeurs ±3 = facile | 🟢 | C2 | signal | GC·HG·CL·ZW |
| D1616 | Non autonome / confirmation | 🟢 | C2 | gestion_risque_entree | GC·HG·CL·ZW |
| D1617 | Exemples MOS / VLO | 🟢 | C2 | configuration | GC·HG·CL·ZW |
| D1618 | Bottom line momentum | 🟢 | C2 | indicateurs_tendance | GC·HG·CL·ZW |
| D1619 | Paramétrage SharpCharts | 🟡 | — | configuration | — |
| D1620 | Scans + garde-fou volume | 🟢 | C2 | signal | GC·HG·CL·ZW |
| D1621 | Lien Belkhayate non tranché | ⚫🔴 | C2 | indicateurs_tendance | GC·HG·CL·ZW |

**Total : 11 décisions (D1611→D1621) · 7/7 images certifiées · 0 cas à vérifier.**
Lien Belkhayate : **⚫🔴 À VÉRIFIER** (D1621) — rapprochement Énergie/EMV non affirmé par la source, à arbitrer humainement.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
