# Extraction StockCharts — Trend Lines
**Source :** `bundles/stockcharts/trend_lines.md` (HTTP 200) + 9 images certifiées
**Méthode images :** double ancrage · 9/9 certifiées · 0 à vérifier
**Décisions :** D4571 → D4590 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/trend-lines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Lignes de tendance comme support/résistance dynamiques sur GC/HG/CL/ZW — validation, angles, espacements, lignes internes pour filtrer les faux signaux.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/Gw26NUaM1LzkXo9O7Uyc | Example of an uptrend line in a stock chart | What Is an Uptrend Line | D4571 |
| /files/pkyrhVAoCLWWc2tykTVr | Example of a downtrend in a stock chart | What Is a Downtrend Line | D4572 |
| /files/fSA2BVn3SOSrsdfBfE49 | Downtrend lines in semi-log vs. arithmetic scale | Scale Settings | D4574 |
| /files/ndVmyjNvTMzBsWQRxU6L | Uptrend lines in semi-log and arithmetic scale | Scale Settings | D4574 |
| /files/gPYQMXXbh2cKTeqgv77i | Example of a valid uptrend line (3 points) | How Do You Validate a Trend Line | D4575 |
| /files/wwyd7t9YBvS89uO0bNvC | Trendline where second high point is too close | Spacing Rules | D4577 |
| /files/wbu1ut2gnbqtkAds7Qdw | Example of a steep trendline | What Are Trend Angles | D4578 |
| /files/cw2BNEEQ5VJQ3RAZPwos | Internal trend line ignoring price spikes | What Are Internal Trend Lines | D4579 |
| /files/Arvm4CLSOIQcVsSXTOUp | Internal trend line using price clusters | What Are Internal Trend Lines | D4580 |
| /files/VcyUqudwZYCTL0MaiLKC | Trendline break that didn't reverse the trend | The Bottom Line | D4582 |

## DÉCISIONS

### D4571 — Définition et rôle de la ligne de tendance haussière
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_Gw26NUaM1LzkXo9O7Uyc) : Une ligne de tendance haussière a une pente positive, formée en reliant deux ou plus points bas (chaque bas supérieur au précédent). Elle agit comme support et indique que la demande nette augmente même quand le prix monte. Tant que les prix restent au-dessus, l'uptrend est intact. Une cassure sous la ligne indique que la demande nette s'affaiblit.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une ligne de tendance haussière valide constitue un support dynamique — une cassure en clôture déclenche un signal d'alerte VENTE dans la grille /10.
*Catégorie : structure_marche*

### D4572 — Définition et rôle de la ligne de tendance baissière
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_pkyrhVAoCLWWc2tykTVr) : Une ligne de tendance baissière a une pente négative, formée en reliant deux ou plus points hauts (chaque haut inférieur au précédent). Elle agit comme résistance et indique que l'offre nette augmente même quand le prix baisse. Tant que les prix restent sous la ligne, le downtrend est intact. Une cassure au-dessus indique que l'offre nette diminue.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une ligne de tendance baissière valide constitue une résistance dynamique — une cassure en clôture déclenche un signal d'alerte ACHAT dans la grille /10.
*Catégorie : structure_marche*

### D4573 — Importance fondamentale des lignes de tendance en analyse technique
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md) : Les lignes de tendance représentent une dépiction visuelle des niveaux de support et résistance dans n'importe quel timeframe. Leur importance réside dans leur capacité à fournir une représentation visuelle claire des tendances de marché et des points de retournement potentiels. Les mêmes principes applicables aux supports/résistances horizontaux s'appliquent aux lignes de tendance.
**TRADEX-AI C1** : Les trendlines sur GC/HG/CL/ZW sont des outils de structure de marché (C1) — équivalentes fonctionnellement aux supports/résistances horizontaux de la méthode Belkhayate.
*Catégorie : structure_marche*

### D4574 — Echelle semi-logarithmique recommandée pour les trendlines long terme
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_fSA2BVn3SOSrsdfBfE49, image_ndVmyjNvTMzBsWQRxU6L) : Les hauts et bas s'alignent mieux pour les lignes de tendance quand les prix sont affichés en échelle semi-log. Particulièrement vrai pour les trendlines long terme ou quand il y a un grand changement de prix. L'échelle arithmétique affiche les incréments de valeur absolue; l'échelle semi-log affiche en termes de pourcentage.
**TRADEX-AI C1** : Pour l'analyse des trendlines sur GC/HG/CL/ZW sur des timeframes hebdomadaires ou mensuels, l'échelle semi-log doit être préférée pour éviter les fausses cassures.
*Catégorie : indicateurs_tendance*

### D4575 — Règle de validation d'une trendline : 3 points minimum
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_gPYQMXXbh2cKTeqgv77i) : Règle générale : 2 points pour dessiner une trendline, le 3ème point confirme sa validité. Plus il y a de points utilisés pour dessiner la ligne de tendance, plus la validité du niveau de support/résistance représenté est solide. 4 touches renforcent encore davantage la solidité du niveau.
**TRADEX-AI C1** : Sur TRADEX, une trendline sur GC/HG/CL/ZW n'est considérée valide (et donc utilisable pour un signal) qu'à partir de 3 points de contact confirmés.
*Catégorie : structure_marche*

### D4576 — Quand les points ne s'alignent pas, ne pas forcer la trendline
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md) : Il peut être difficile de trouver plus de 2 points pour construire une trendline. Bien que les trendlines soient importantes en analyse technique, les dessiner sur chaque graphique n'est pas toujours possible. Parfois les hauts ou bas ne s'alignent pas et il vaut mieux ne pas forcer.
**TRADEX-AI C1** : Sur TRADEX, si une trendline ne peut être construite sur 3 points valides pour GC/HG/CL/ZW, elle est ignorée dans la grille de score — forcer une trendline génère de faux signaux.
*Catégorie : gestion_risque_entree*

### D4577 — Règles d'espacement des points sur une trendline
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_wwyd7t9YBvS89uO0bNvC) : Les bas (pour uptrend) et les hauts (pour downtrend) ne doivent pas être trop éloignés ni trop proches. La distance idéale dépend du timeframe, du degré de mouvement et des préférences personnelles. Trop proches : validité du bas/haut de réaction en question. Trop éloignés : relation suspecte. Idéal : points relativement également espacés.
**TRADEX-AI C1** : Pour les trendlines sur GC/HG/CL/ZW, les points de validation doivent être espacés de façon homogène — un écart trop court (même bougie ou barre suivante) invalide la trendline.
*Catégorie : structure_marche*

### D4578 — Trendlines trop raides : moins fiables comme support/résistance
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_wbu1ut2gnbqtkAds7Qdw) : Plus la pente d'une trendline est raide, moins sa validité comme support/résistance est grande. Une trendline raide résulte d'une avancée ou d'un déclin rapide sur une courte période. Même formée avec 3 points apparemment valides, elle offre rarement un niveau support/résistance significatif.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, les trendlines à forte pente (angle > 45°) sont considérées comme instables — elles sont à pondérer moins dans la grille /10 que les trendlines à pente modérée.
*Catégorie : structure_marche*

### D4579 — Lignes de tendance internes : ignorer les spikes de prix
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_cw2BNEEQ5VJQ3RAZPwos) : Quand les hauts ou bas ne s'alignent pas proprement (angle trop raide, points trop proches), on peut dessiner une trendline interne qui ignore les spikes de prix dans une mesure raisonnable. Ces spikes représentent des surréactions extrêmes. La ligne interne passe à travers les bas pour donner un angle raisonnable avec les autres bas correspondants.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, lors d'événements macro (NFP, FOMC), des spikes de prix peuvent fausser les trendlines — utiliser les lignes internes pour filtrer ces distorsions temporaires.
*Catégorie : macro_evenements*

### D4580 — Lignes de tendance internes via clusters de prix
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_Arvm4CLSOIQcVsSXTOUp) : Un cluster de prix est un groupe de prix dans une plage serrée sur une période. On peut ignorer les spikes en utilisant le cluster de prix pour dessiner la trendline. Cette approche produit une trendline interne basée sur 3 touches solides qui prédit précisément les niveaux de résistance futurs.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en période de consolidation (range tight), utiliser les clusters de prix plutôt que les pointes extrêmes pour tracer les trendlines — améliore la fiabilité des niveaux de support/résistance.
*Catégorie : structure_marche*

### D4581 — Confirmer la cassure de trendline avec d'autres outils
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md) : Pour valider les cassures de trendline, d'autres outils doivent être employés — supports/résistances horizontaux ou analyse pic-et-creux. Les trendlines sont populaires mais ne sont qu'un outil parmi d'autres pour établir, analyser et confirmer une tendance.
**TRADEX-AI C1** : Sur TRADEX, une cassure de trendline sur GC/HG/CL/ZW ne constitue un signal valide que si elle est confirmée par au moins un autre indicateur (support horizontal, analyse des hauts/bas Belkhayate).
*Catégorie : gestion_risque_entree*

### D4582 — Cassure de trendline sans inversion de trend : avertissement, pas verdict
🟢 **FAIT VÉRIFIÉ** (Source : trend_lines.md, image_VcyUqudwZYCTL0MaiLKC) : Les cassures de trendline ne doivent pas être l'arbitre final mais servent simplement d'avertissement qu'un changement de tendance peut être imminent. En utilisant les cassures comme avertissements, les investisseurs et traders peuvent porter plus d'attention aux autres signaux de confirmation pour un changement de tendance potentiel.
**TRADEX-AI C1** : Dans TRADEX, une cassure de trendline sur GC/HG/CL/ZW est un signal de niveau "alerte" dans la grille /10 — elle doit être confirmée par les autres cercles (C2 à C7) avant de générer un signal d'exécution.
*Catégorie : gestion_risque_entree*
