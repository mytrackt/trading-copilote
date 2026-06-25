# Extraction StockCharts — Why and How To Use Correlation
**Source :** `bundles/stockcharts/why_and_how_to_use_correlation.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 images présentes dans le bundle · 0 à vérifier
**Décisions :** D4871 → D4890 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/why-and-how-to-use-correlation
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Corrélations inter-marchés directement applicables à la matrice live 30j GC/HG/CL/ZW/ES/VX/DX (Cercle C7) — fondements théoriques du module corrélations.py.

---

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| *(aucune image dans le bundle)* | — | — | — |

---

## DÉCISIONS

### D4871 — Définition statistique de la corrélation
🟢 **FAIT VÉRIFIÉ** (Source : why_and_how_to_use_correlation.md) : La corrélation mesure le degré auquel deux variables (ou plus) se meuvent ensemble. Valeurs positives = mouvement dans le même sens. Valeurs négatives = mouvement en sens opposé. Plage : -1,0 à +1,0. Une valeur de 0 indique l'absence de relation entre les variables.
**TRADEX-AI C7** : La matrice de corrélations live 30j de TRADEX-AI (`correlations.py`) mesure exactement ce coefficient entre GC/HG/CL/ZW/ES/VX/DX — une corrélation proche de 0 invalide l'utilisation d'un actif comme confirmation pour un autre.
*Catégorie : correlations*

---

### D4872 — Corrélation dans les marchés financiers
🟢 **FAIT VÉRIFIÉ** (Source : why_and_how_to_use_correlation.md) : En finance, la corrélation mesure la relation entre deux instruments (actions, obligations, ETF, fonds, indices) et leur degré de co-mouvement. Corrélation positive forte → même direction. Corrélation négative forte → directions opposées. Corrélation proche de 0 → non liés en termes de direction.
**TRADEX-AI C7** : Dans TRADEX-AI, GC (Or) et DX (Dollar Index) ont typiquement une corrélation négative forte — cette relation est un signal de confirmation C4 (macro) quand elle se maintient. Si la corrélation se rapproche de 0, ce signal de confirmation perd sa valeur.
*Catégorie : correlations*

---

### D4873 — Utilité de la corrélation : diversification et réduction du risque
🟢 **FAIT VÉRIFIÉ** (Source : why_and_how_to_use_correlation.md) : Les valeurs de corrélation peuvent être utilisées pour construire un portefeuille bien diversifié, réduisant le risque tout en améliorant les rendements. Un ensemble d'actifs avec des valeurs de corrélation faibles entre eux (diversifiés) limite l'exposition aux chocs de marché singuliers.
**TRADEX-AI C7** : Le choix des 4 actifs tradables de TRADEX-AI (GC/HG/CL/ZW) repose implicitement sur cette logique — les commodités ont des corrélations partielles mais non totales, offrant des signaux indépendants ; la règle 3/4 tradables alignés exploite la convergence de signaux non corrélés à 1,0.
*Catégorie : correlations*

---

### D4874 — Comment utiliser la corrélation : équilibrer un portefeuille
🟢 **FAIT VÉRIFIÉ** (Source : why_and_how_to_use_correlation.md) : Pour utiliser la corrélation à son avantage, équilibrer les actifs du portefeuille selon leurs valeurs de corrélation, en veillant à ce que les corrélations vs un benchmark commun (ex. S&P 500) ne soient pas toutes clustérisées dans la même plage. Exemple : 10 actifs tous avec corrélation vs S&P 500 entre +0,87 et +0,98 → risque concentré. Si les corrélations vont de -0,79 à +0,95 → plus diversifié, moins exposé aux chocs.
**TRADEX-AI C7** : Dans TRADEX-AI, la matrice 30j doit surveiller ce clustering — si GC/HG/CL/ZW ont tous une corrélation > +0,80 avec ES un jour donné (risk-on total), les signaux de confirmation de 3/4 actifs pourraient être factices (tous montent/descendent pour la même raison macro). Dans ce cas, élever le seuil de confiance requis.
*Catégorie : correlations*

---

### D4875 — Corrélation positive vs négative : implications pour la confirmation
🟡 **SYNTHÈSE** (Source : why_and_how_to_use_correlation.md) : Une corrélation positive forte entre deux actifs signifie que l'un peut confirmer l'autre. Une corrélation négative forte signifie que la hausse d'un prédit la baisse de l'autre — utile comme signal inverse. Une corrélation nulle annule la valeur de confirmation.
**TRADEX-AI C7** : Pour les actifs de confirmation (DX/ES/VX) dans TRADEX-AI : DX corrélation négative avec GC → hausse DX = signal bearish GC. ES corrélation positive avec CL → force ES confirme tendance CL. VX corrélation négative avec ES → VIX élevé = marché craintif = invalide signaux haussiers ES/CL. Ces relations doivent être surveillées en live sur 30j.
*Catégorie : correlations*

---

### D4876 — Corrélation plage -1.0 à +1.0 : seuils pratiques
🔵 **ÉCOLE** (Source : why_and_how_to_use_correlation.md) : La plage de corrélation est strictement bornée entre -1,0 (parfaitement opposé) et +1,0 (parfaitement identique), avec 0 = aucune relation. Cette borne est mathématiquement garantie quelle que soit la volatilité des actifs.
**TRADEX-AI C7** : Dans `correlations.py`, le calcul rolling 30j produira toujours des valeurs dans cette plage — pas besoin de normalisation supplémentaire. Les seuils d'alerte pratiques recommandés : |r| > 0,7 = relation forte, 0,4 < |r| < 0,7 = relation modérée, |r| < 0,4 = relation faible (confirmation peu fiable).
*Catégorie : correlations*

---

### D4877 — Diversification par classe d'actifs et valeurs de corrélation
🔵 **ÉCOLE** (Source : why_and_how_to_use_correlation.md) : La diversification efficace requiert des actifs de classes différentes avec des corrélations faibles entre eux. Un portefeuille avec des corrélations allant de -0,79 à +0,95 est considéré plus largement diversifié qu'un portefeuille avec corrélations clustérisées entre +0,87 et +0,98.
**TRADEX-AI C7** : Les 4 actifs TRADEX tradables (GC/HG/CL/ZW) appartiennent tous aux commodités — en période de stress global, leurs corrélations peuvent se rapprocher simultanément de +1,0 (flight-to-safety ou sell-off généralisé). Le module corrélations doit détecter ce cas et émettre un warning "corrélations convergentes" qui augmente le seuil de signal requis.
*Catégorie : gestion_risque_entree*
