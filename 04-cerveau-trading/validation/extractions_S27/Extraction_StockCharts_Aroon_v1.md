# Extraction StockCharts — Aroon
**Source :** `bundles/stockcharts/aroon.md` (HTTP 200 · ~7 800 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D651 → D662 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/aroon
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Aroon - Chart 1 | How To Calculate the Aroon Indicators | CERTIFIE (accord .md + HTML) |
| image_02.png | Aroon - Chart 1 | How To Calculate the Aroon Indicators | CERTIFIE (accord .md + HTML) |
| image_03.png | Aroon - Chart 2 | New Trend Emerging | CERTIFIE (accord .md + HTML) |
| image_04.png | Aroon - Chart 3 | Consolidation Period | CERTIFIE (accord .md + HTML) |
| image_05.png | Aroon - Chart 4 | Consolidation Period | CERTIFIE (accord .md + HTML) |
| image_06.png | Aroon - Chart 5 | Using Aroon With SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D651 — Nature et origine de l'indicateur Aroon
🔵 **ÉCOLE (Chande)** (Source : aroon.md) : Développé par Tushar Chande en 1995, Aroon est un système d'indicateurs qui détermine si un actif est en tendance ou non et la force de cette tendance. « Aroon » signifie « Première lumière de l'aube » en sanskrit. Les indicateurs Aroon mesurent le nombre de périodes écoulées depuis qu'un plus haut (high) ou plus bas (low) sur x jours a été enregistré. Aroon mesure le **temps relatif au prix** (et non le prix relatif au temps comme les oscillateurs de momentum classiques).
**TRADEX-AI C1** : Indicateur de tendance candidat pour qualifier l'état (tendance vs range) de GC/HG/CL/ZW ; à traiter comme couche analytique, jamais comme déclencheur d'ordre.
*Catégorie : indicateurs_tendance*

---

### D652 — Formules de calcul Aroon-Up et Aroon-Down
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_01) : Les indicateurs sont exprimés en pourcentage et fluctuent entre 0 et 100. Aroon-Up repose sur les plus hauts, Aroon-Down sur les plus bas.
`Aroon-Up = ((25 - Jours depuis le plus haut sur 25 jours) / 25) x 100`
`Aroon-Down = ((25 - Jours depuis le plus bas sur 25 jours) / 25) x 100`
Le paramètre par défaut dans SharpCharts est 25.
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; paramètre 25 par défaut, à reparamétrer selon le timeframe Belkhayate utilisé (15min / Range Bar).
*Catégorie : indicateurs_tendance*

---

### D653 — Décroissance temporelle et borne 0-100
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md) : Aroon décroît à mesure que le temps écoulé depuis un nouveau plus haut/bas augmente. Les valeurs sont bornées entre 0 et 100. Une valeur élevée signifie qu'un plus haut/bas a été enregistré récemment ; une valeur faible signifie qu'aucun plus haut/bas récent n'a été atteint.
**TRADEX-AI C1** : Lecture directe de la « fraîcheur » d'un extrême de prix ; utile comme feature continue normalisée 0-100.
*Catégorie : indicateurs_tendance*

---

### D654 — Centre 50 et impossibilité d'une valeur exacte 50 en journalier
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_02) : 50 est le point de coupure. Comme 12,5 jours marque le milieu exact, une valeur d'exactement 50 est impossible sur un graphique journalier (possible sur d'autres timeframes). Aroon est soit sous 50 (ex. 48) soit au-dessus de 50 (ex. 52) en journalier. Au-dessus de 50 = un nouvel extrême enregistré dans les 12 derniers jours ou moins ; sous 50 = un nouvel extrême enregistré dans les 13 jours ou plus {(25-13)/25 x 100 = 48}.
**TRADEX-AI C1** : Le seuil 50 sert de bascule binaire haussier/baissier ; ne pas coder de test d'égalité stricte à 50 en daily (jamais atteint).
*Catégorie : signal*

---

### D655 — Biais de tendance via position relative à 50
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md) : Les haussiers ont l'avantage quand Aroon-Up est au-dessus de 50 ET Aroon-Down sous 50 (plus grande propension aux nouveaux plus hauts sur x jours). Inversement, les baissiers ont l'avantage quand Aroon-Up est sous 50 ET Aroon-Down au-dessus de 50.
**TRADEX-AI C3** : Règle de confirmation de biais directionnel ; combinable avec la BGC/Direction Belkhayate comme filtre de cohérence tendance.
*Catégorie : signal*

---

### D656 — Lectures extrêmes (surge 100, plages persistantes)
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md) : Une poussée (surge) à 100 indique qu'une tendance pourrait émerger, confirmable par un déclin de l'autre indicateur (ex. Aroon-Up à 100 + Aroon-Down sous 30 = force haussière). Des lectures constamment élevées signifient que les prix font régulièrement de nouveaux extrêmes. Prix en hausse soutenue quand Aroon-Up reste dans la plage 70-100 sur une période prolongée. Aroon-Down restant dans 0-30 signifie que les prix ne baissent PAS (mais cela n'implique pas qu'ils montent — vérifier Aroon-Up).
**TRADEX-AI C1** : Plages 70-100 / 0-30 exploitables comme zones de force de tendance ; attention à l'asymétrie logique (faible Aroon-Down ≠ hausse).
*Catégorie : signal*

---

### D657 — Signal de nouvelle tendance émergente en 3 stages
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_03) : Pour un signal de tendance haussière : (1) Aroon-Up passe au-dessus d'Aroon-Down (nouveaux plus hauts plus récents que nouveaux plus bas) ; (2) Aroon-Up passe au-dessus de 50 et Aroon-Down sous 50 ; (3) Aroon-Up atteint 100 tandis qu'Aroon-Down reste à des niveaux relativement bas. Les stages 1 et 2 ne surviennent pas toujours dans cet ordre. Pour un signal baissier, les positions sont inversées : Aroon-Down passe au-dessus d'Aroon-Up, dépasse 50, atteint 100.
**TRADEX-AI C1** : Séquence de croisement + franchissement codable en machine à états (stage 1/2/3) pour détecter l'émergence de tendance sur GC/HG/CL/ZW.
*Catégorie : configuration*

---

### D658 — Exemple historique CSX (illustration multi-tendances)
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_03) : Sur CSX Corp en barres hebdomadaires avec Aroon 25 semaines : le 1er stage d'uptrend signalé quand Aroon-Up passe au-dessus d'Aroon-Down début 2008, puis Aroon-Up dépasse 50 et atteint 100 pendant qu'Aroon-Down reste bas. L'uptrend a duré jusqu'en septembre 2008 où Aroon-Down a franchi Aroon-Up, dépassé 50 et atteint 100 (downtrend).
**TRADEX-AI C1** : Cas pédagogique confirmant la persistance d'Aroon près de 100 pendant une tendance soutenue ; pas de paramètre nouveau, valeur illustrative.
*Catégorie : configuration*

---

### D659 — Détection de consolidation (range)
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_04, image_05) : Les indicateurs signalent une consolidation quand les deux sont sous 50 et/ou quand les deux baissent en parallèle avec un faible écart entre les lignes. Pour Aroon 25 jours, des lectures sous 50 signifient qu'aucun plus haut/bas sur 25 jours n'a été enregistré depuis 13 jours ou plus. Un déclin parallèle resserré indique la formation d'un range. Le premier indicateur à franchir 50 et atteindre 100 déclenchera le signal suivant.
**TRADEX-AI C1** : Détecteur de range exploitable comme garde-fou (ne pas générer de signal directionnel en consolidation) ; cohérent avec la logique « pas de trade en range » Belkhayate.
*Catégorie : structure_marche*

---

### D660 — Exemples de consolidation OMC et LPNT
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md, image_04, image_05) : Sur Omnicom (OMC), Aroon-Up et Aroon-Down sous 50 en déclin parallèle (zone jaune) puis Aroon-Up surge à 100 = fin de consolidation / début d'avance. Sur Lifepoint Hospitals (LPNT) avec Aroon 25 jours, les deux lignes baissent en mai (écart ~25 points), s'aplatissent en juin sous 50 environ deux semaines (triangle), puis Aroon-Down franchit 50 avant la cassure du triangle et atteint 100 = continuation baissière.
**TRADEX-AI C1** : Illustration de sortie de range par franchissement de 50 ; renforce la règle « premier à 50/100 donne la direction ».
*Catégorie : configuration*

---

### D661 — Synthèse opératoire (The Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md) : Aroon-Up et Aroon-Down sont complémentaires et mesurent le temps écoulé entre nouveaux plus hauts/bas sur x jours. Une poussée d'Aroon-Up + déclin d'Aroon-Down signale l'émergence d'un **uptrend** ; l'inverse signale un **downtrend**. Une consolidation est présente quand les deux baissent en parallèle ou restent à de bas niveaux (sous 30). Aroon sert à déterminer si l'actif est en tendance ou plat, puis on utilise d'autres indicateurs pour générer les signaux appropriés.
**TRADEX-AI C3** : Aroon positionné comme filtre d'état de marché (tendance/plat) en amont des déclencheurs ; ne génère pas seul l'ordre — rôle de confirmation.
*Catégorie : signal*

---

### D662 — Scan suggéré « Aroon-Up et Aroon-Down < 20 »
🟢 **FAIT VÉRIFIÉ** (Source : aroon.md) : Scan StockCharts repérant les actifs où Aroon-Up et Aroon-Down sont sous 20 (consolidation fréquente à ces niveaux bas ; le premier à franchir 50 donne l'indice directionnel suivant) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily Aroon Up(25) < 20]
AND [Daily Aroon Down(25) < 20]
```
**TRADEX-AI C1** : Logique de filtre « double Aroon bas = consolidation » transposable en condition Python ; syntaxe de scan propre à StockCharts (non réutilisable telle quelle), seule la logique compte.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D651 | Nature et origine Aroon | 🔵 ÉCOLE | C1 | indicateurs_tendance |
| D652 | Formules Aroon-Up / Aroon-Down | 🟢 | C1 | indicateurs_tendance |
| D653 | Décroissance temporelle / borne 0-100 | 🟢 | C1 | indicateurs_tendance |
| D654 | Centre 50 / 50 impossible en daily | 🟢 | C1 | signal |
| D655 | Biais de tendance via 50 | 🟢 | C3 | signal |
| D656 | Lectures extrêmes (100, 70-100, 0-30) | 🟢 | C1 | signal |
| D657 | Tendance émergente en 3 stages | 🟢 | C1 | configuration |
| D658 | Exemple historique CSX | 🟢 | C1 | configuration |
| D659 | Détection de consolidation | 🟢 | C1 | structure_marche |
| D660 | Exemples consolidation OMC / LPNT | 🟢 | C1 | configuration |
| D661 | Synthèse opératoire | 🟢 | C3 | signal |
| D662 | Scan « double Aroon < 20 » | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** Aroon n'est PAS un indicateur Belkhayate (⚫). Lien indirect possible : son rôle de détecteur de tendance/range recoupe la logique « ne pas trader en range » et peut servir de filtre de cohérence avec la BGC/Direction Belkhayate, sans jamais s'y substituer.

**À vérifier (humain) :**
- D654 — exemples numériques 48 / 52 et {(25-13)/25 x 100 = 48} : la valeur 52 n'est pas explicitement détaillée par un calcul dans la source (déduite par symétrie). À confirmer avant codage d'un seuil dur.
- D662 — la syntaxe de scan est propre à StockCharts ; seule la **logique** (double Aroon < 20 = consolidation) est transposable, pas le code.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
