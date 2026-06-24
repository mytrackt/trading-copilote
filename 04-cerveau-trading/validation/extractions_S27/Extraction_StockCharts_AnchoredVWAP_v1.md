# Extraction StockCharts — Anchored VWAP

**Source :** `bundles/stockcharts/anchored_vwap.md` (HTTP 200) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 3/3 certifiées · 0 à vérifier
**Décisions :** D219 → D228 · **Page :** chartschool.stockcharts.com/.../technical-overlays/anchored-vwap
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page PRIORITAIRE. L'Anchored VWAP ancre la moyenne prix×volume sur un **événement** (plus haut/bas, earnings, gap, news) — clé d'order flow (C2) et de support/résistance dynamique (C1). Anchored VWAP s'applique aux actifs TRADING **GC/HG/CL/ZW**. Aucun rattachement Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | What Is the Anchored VWAP? (section-fallback) | What Is the Anchored VWAP? | D219 |
| image_02 | How Do You Interpret the Anchored VWAP? (section-fallback) | How Do You Interpret the Anchored VWAP? | D223 |
| image_03 | Charting with Anchored VWAP (section-fallback) | Charting with Anchored VWAP | D227 |

---

## DÉCISIONS

### D219 — Anchored VWAP : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md, image_01) : L'Anchored Volume Weighted Average Price (Anchored VWAP) est un indicateur de trading qui fournit le **prix moyen** d'un actif depuis un **point de départ précis** (« l'ancre »), en intégrant **prix ET volume**. Il sert à confirmer les tendances et à identifier les zones de support et de résistance sur le graphique.
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : L'indicateur lie les calculs VWAP à une barre de prix précise choisie par le trader ; comme le VWAP traditionnel, il combine prix et volume dans une moyenne pondérée.
**TRADEX-AI C1/C2** : Anchored VWAP = niveau prix×volume dynamique servant de support/résistance et de confirmation de tendance sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D220 — Anchored VWAP vs VWAP traditionnel : point de départ flexible
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : Le VWAP traditionnel se **réinitialise chaque jour** (première barre du jour → dernière barre du jour) et ne donne que le prix moyen intraday. L'Anchored VWAP permet de **fixer le point d'ancrage** d'où commence le calcul, offrant une vue plus flexible.
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : Avec l'Anchored VWAP, le chartiste choisit la première barre du calcul (« ancrage »), et la dernière barre est **toujours la plus récente disponible**. Grâce à ces points de départ/fin flexibles, l'Anchored VWAP **n'est pas limité aux graphiques intraday** (contrairement au VWAP traditionnel, limité à une seule journée).
**TRADEX-AI C1** : Côté moteur, l'Anchored VWAP doit accepter une barre d'ancrage paramétrable et recalculer jusqu'à la barre courante ; utilisable sur tout timeframe NT8 (range bars incluses) sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D221 — Choix de l'ancre : un événement marquant un changement de psychologie
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : La barre de départ choisie marque généralement un **changement de psychologie de marché** : un plus haut ou plus bas significatif, une annonce de résultats (earnings), un gap, une news ou autre annonce. La ligne Anchored VWAP est tracée à partir de cet événement marquant.
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : Anchored VWAP permet de voir si les **acheteurs ou les vendeurs** dominent depuis ce moment précis.
**TRADEX-AI C2/C4** : Ancrer le VWAP sur événements identifiables — plus haut/bas de structure (C1), gap, ou catalyseur macro/news (C4) — pour lire la domination acheteur/vendeur sur GC/HG/CL/ZW depuis l'événement.
*Catégorie : structure_marche*

---

### D222 — Calcul : même formule que VWAP, seules les barres incluses changent
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : L'Anchored VWAP utilise **la même formule** que le VWAP traditionnel ; la seule différence réside dans les **barres incluses** dans le calcul. VWAP traditionnel = première à dernière barre du jour (donc intraday uniquement) ; Anchored VWAP = barre d'ancrage choisie → barre la plus récente.
🟡 **CONVENTION** : La formule détaillée du VWAP standard est renvoyée à l'article VWAP dédié de ChartSchool (non incluse dans cette page).
**TRADEX-AI C0/C1** : Réutiliser l'implémentation VWAP existante en ne modifiant que la fenêtre de barres (ancre → barre courante) ; besoin OHLCV + volume. Formule exacte à reprendre de l'article VWAP source (cf. à vérifier).
*Catégorie : indicateurs_tendance*

---

### D223 — Interprétation : confirmer tendances + support/résistance, données pertinentes seulement
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md, image_02) : Comme le VWAP traditionnel, l'Anchored VWAP confirme les tendances et identifie les zones de support/résistance. L'avantage est de pouvoir fixer le point de départ pour **n'inclure que les données pertinentes**. Le price action **avant** le changement de psychologie doit être exclu car il ne reflète pas la même psychologie de marché.
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md, image_02) : Exemple TSLA — la ligne VWAP (bleue, ancrée sur la barre d'ouverture) inclut une hausse vive puis une forte chute et ne reflète pas le price action de mi-séance ; la ligne Anchored VWAP (rouge, ancrée au plus bas du matin) ne contient que les données depuis ce plus bas et reflète mieux la psychologie de mi-séance.
**TRADEX-AI C1** : Préférer l'Anchored VWAP au VWAP réinitialisé quand le contexte récent (post-événement) est plus pertinent que la journée entière, sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D224 — Lignes multiples : convergence = zone de support/résistance renforcée
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : Plusieurs lignes Anchored VWAP peuvent être utilisées sur un même graphique, chacune ancrée à un point de départ différent. **Là où plusieurs lignes Anchored VWAP convergent**, cela peut indiquer une zone de support ou de résistance **particulièrement forte**.
**TRADEX-AI C1/C3** : Calculer plusieurs Anchored VWAP (ancres = plusieurs swings/événements) et détecter leurs **confluences** comme zones S/R prioritaires sur GC/HG/CL/ZW ; pondérer la confiance d'un niveau par le nombre de lignes convergentes.
*Catégorie : structure_marche*

---

### D225 — Bottom line : avantage = fenêtre d'étude précise, exclure l'ancienne psychologie
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : L'Anchored VWAP offre les mêmes bénéfices que le VWAP traditionnel pour définir support et résistance, avec l'avantage de **cibler précisément la fenêtre temporelle** à étudier. Démarrer le calcul à un point de retournement significatif permet d'**exclure** le price action piloté par une psychologie de marché différente.
**TRADEX-AI C1** : Règle d'usage — choisir l'ancre au dernier point de retournement pertinent pour neutraliser l'historique non représentatif sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D226 — Garde : ne jamais utiliser l'Anchored VWAP seul
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : Comme pour tout indicateur technique, les traders doivent utiliser l'Anchored VWAP **avec d'autres indicateurs et techniques d'analyse**.
**TRADEX-AI C3** : Guard permanent — un signal Anchored VWAP (rejet/franchissement de la ligne, confluence) exige confirmation multi-outil (price action, structure, volume/order flow) ; jamais de décision sur la seule ligne VWAP sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

---

### D227 — Paramétrage : ancre par défaut + ajustement par clic (StockChartsACP)
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md, image_03) : L'overlay s'ajoute depuis le panneau Chart Settings d'un graphique StockChartsACP. À l'ajout, une **date et heure d'ancrage par défaut** sont choisies automatiquement, modifiables ensuite. Les champs Anchor Date et Anchor Time peuvent être édités manuellement, mais le plus rapide est de **survoler le graphique, placer le viseur sur la barre voulue et cliquer** pour fixer la nouvelle ancre.
**TRADEX-AI C0** : Référence UI — exposer dans l'interface un champ « Anchor Date/Time » + une sélection d'ancre par clic sur la barre pour GC/HG/CL/ZW.
*Catégorie : configuration*

---

### D228 — FAQ : synthèse des points clés (différence, signification de l'ancre, lignes multiples)
🟢 **FAIT VÉRIFIÉ** (Source : anchored_vwap.md) : FAQ officielle — (1) différence principale = point de départ (VWAP traditionnel toujours à la première barre du jour, Anchored VWAP à une barre choisie, donc non limité à l'intraday) ; (2) la barre d'ancrage marque un changement de psychologie (plus haut/bas, earnings, news) et révèle qui domine depuis ; (3) plusieurs lignes possibles, leur convergence = zone S/R particulièrement forte.
🟡 **CONVENTION** : La FAQ ne fait que récapituler D220, D221 et D224 — aucune information neuve, conservée pour traçabilité.
**TRADEX-AI C1/C2** : Confirme les règles d'usage déjà extraites ; pas de logique additionnelle.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D219 → D228 (10) |
| Images certifiées citées | 3/3 |
| Catégories utilisées | indicateurs_tendance · structure_marche · configuration · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🟡 CONVENTION |
| Belkhayate | **NON CONCERNÉ** — aucun rattachement affirmé par la source ; ne rien inventer |

### CAS « À VÉRIFIER »
- **Formule VWAP détaillée (D222)** : cette page ne donne PAS la formule de calcul, elle renvoie à l'article VWAP dédié de ChartSchool (`volume-weighted-average-price-vwap.md`). À scraper séparément si la formule littérale est requise pour l'implémentation NinjaScript.
- **Aucune image douteuse** : 3/3 certifiées par accord .md + HTML (toutes section-fallback, figcaptions vides à la source — c'est normal sur cette page).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
