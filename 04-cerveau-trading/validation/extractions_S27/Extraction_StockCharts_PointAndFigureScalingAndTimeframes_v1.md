# Extraction StockCharts — Point & Figure Scaling and Timeframes
**Source :** `bundles/stockcharts/point_and_figure_scaling_and_timeframes.md` (HTTP 200 · ~13 500 car.) + 10 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende · section-fallback image_01) · 10/10 certifiées
**Décisions :** D3171 → D3190 · **Page :** chartschool.stockcharts.com/.../point-and-figure-charts/point-and-figure-basics/point-and-figure-scaling-and-timeframes
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

---

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Traditional [section-fallback] | Traditional | D3173 |
| image_02 | P&F Timeframes | Dynamic (ATR) Scaling | D3177 |
| image_03 | P&F chart showing a 1% box size. | Percentage versus User-Defined | D3179 |
| image_04 | P&F chart showing a user-defined 0.20 points box size. | Percentage versus User-Defined | D3179 |
| image_05 | P&F chart with a 1% box size. | Percentage versus User-Defined | D3180 |
| image_06 | P&F chart with a user-defined box size of 5 points. | Percentage versus User-Defined | D3180 |
| image_07 | A P&F chart that extends for 18 months. | 9–24 Month Charts | D3182 |
| image_08 | A P&F chart that extends for nine months. | 9–24 Month Charts | D3182 |
| image_09 | P&F chart based on 60-minute data and 0.5% box size. | 3–9 Month Charts | D3187 |
| image_10 | P&F chart of VFC using 60-minute data and 0.5% box size. | 3–9 Month Charts | D3187 |

---

## DÉCISIONS

### D3171 — Look-back P&F déterminé par les reversals
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : La quantité de données passées affichée sur un chart Point & Figure n'est pas fixe ; le look-back dépend du **nombre de reversals de prix**, lui-même influencé par la **taille de box**, le **reversal amount** et l'**intervalle de données**. C'est cette extension dans le passé qui détermine le timeframe analytique.
**TRADEX-AI C1** : un overlay P&F sur GC/HG/CL/ZW doit exposer (box, reversal, intervalle) comme paramètres pilotant la profondeur d'historique ; aucun « nombre de barres » fixe.
*Catégorie : structure_marche*

### D3172 — Trois horizons d'analyse selon l'extension
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Un chart qui remonte ~1 mois est orienté **court terme** ; plusieurs mois = **moyen terme** ; plus d'un an = **long terme**. Charts à petites box et intervalles courts → look-back courts ; grandes box et intervalles longs → look-back longs.
**TRADEX-AI C1** : règle de cadrage multi-horizon réutilisable pour aligner un signal court terme dans la direction du long terme.
*Catégorie : structure_marche*

### D3173 — Quatre méthodes de scaling
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_01) : Quatre méthodes de scaling P&F sont disponibles : **Traditional, Percentage, Dynamic (ATR), User-Defined**.
**TRADEX-AI C1** : énumération fermée des modes de box-sizing à implémenter ; tag 🟡 sur le choix par défaut (convention).
*Catégorie : indicateurs_tendance*

### D3174 — Traditional scaling (table ChartCraft/Dorsey)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_01) : Le **Traditional scaling** utilise une table prédéfinie de plages de prix pour fixer la box size. Table créée à l'origine par ChartCraft, popularisée par Tom Dorsey (*Point & Figure Charting*), mise à jour par StockCharts pour refléter les prix actuels.
**TRADEX-AI C1** : table déterministe codable en lookup ; tag 🔵 ÉCOLE (méthode Dorsey/ChartCraft, convention propriétaire à la table).
*Catégorie : indicateurs_tendance*

### D3175 — Percentage scaling
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Le **Percentage scaling** utilise une box size égale à un pourcentage fixe du prix. Ex. : scaling 5 % sur un titre à 100 $ → box de 5,00 $.
**TRADEX-AI C1** : formule directe `box = pct × prix`, recalculée par niveau de prix ; codable.
*Catégorie : indicateurs_tendance*

### D3176 — User-Defined scaling
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Le **User-Defined scaling** fixe une box size constante pour tout le chart, indépendante du niveau de prix.
**TRADEX-AI C1** : paramètre scalaire unique ; le plus simple à implémenter.
*Catégorie : indicateurs_tendance*

### D3177 — Dynamic (ATR) scaling
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_02) : Le **Dynamic (ATR) scaling** calcule l'Average True Range sur une période donnée et utilise cette valeur comme box size constante du chart.
**TRADEX-AI C1** : réutilise l'ATR (déjà présent ailleurs dans la KB) comme générateur de box ; pont possible vers le proxy ATR débattu pour l'Énergie. Lien Belkhayate indirect → ⚫🔴 (assemblage non publié).
*Catégorie : indicateurs_tendance*

### D3178 — Effet box-size / intervalle sur le look-back
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Avec Percentage scaling et reversal classique (3) : **petites box + intervalles courts → look-back courts** ; **grandes box + intervalles longs → look-back longs**. L'« interval » désigne les périodes de données (daily, 60 min, 30 min…).
**TRADEX-AI C1** : règle monotone exploitable pour proposer automatiquement un réglage selon l'horizon visé.
*Catégorie : indicateurs_tendance*

### D3179 — Percentage vs User-Defined : nivellement inter-titres
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_03, image_04) : Le Percentage scaling permet un réglage unique pour un groupe de titres aux niveaux de prix très différents (ex. GOOG > 600 $ vs INTC < 25 $). Une box de 1 % vaut ~0,21 $ sur Intel et ~6 $ sur Google → « level the playing field ». Ex. comparé : Intel en 1 % vs user-defined 0,20 $.
**TRADEX-AI C1** : justifie le Percentage scaling pour comparer GC/HG/CL/ZW (niveaux de prix hétérogènes) avec un réglage homogène.
*Catégorie : indicateurs_tendance*

### D3180 — Équivalence pratique Percentage ≈ User-Defined ~1 %
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_05, image_06) : Pour un set box size, viser ~1 % du prix courant (Intel ~21 → box 0,21 ; Google ~592 → box ~6, arrondissable). Une box plus petite (0,50) → plus de reversals et look-back plus court ; box plus grande (1,00) → moins de reversals, look-back plus long. Sur Google, les charts 1 % et 5 points donnent des différences petites et globalement similaires.
**TRADEX-AI C1** : heuristique « box ≈ 1 % du prix » exploitable comme valeur initiale par défaut ; tag 🟡 (convention).
*Catégorie : indicateurs_tendance*

### D3181 — Reversal 3-box ≈ mouvement de 3 % (box 1 %)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Sur un P&F à box 1 %, un reversal 3-box se produit à chaque retournement de ~3 %. Le seuil est **un peu au-dessus de 3 % à la hausse et un peu en dessous à la baisse**, car 3 % de 60 (1,8) > 3 % de 57 (1,71).
**TRADEX-AI C1** : asymétrie hausse/baisse à modéliser fidèlement (le reversal n'est pas symétrique en valeur absolue).
*Catégorie : signal*

### D3182 — Box 1 % / 3-box → 9–24 mois
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_07, image_08) : Un P&F 3-box à box 1 % couvre généralement **9 à 24 mois**. Titres en range (nombreux reversals 3 %) → timeframe plus court ; titres en tendance (peu de reversals) → couvrent plus de temps. Ex. VFC ~18 mois (août 2009→mars 2011) ; Urban Outfitters ~9 mois. Augmenter la box augmente le temps couvert.
**TRADEX-AI C1** : préréglage « vue long terme » documenté pour cadrer la tendance majeure.
*Catégorie : configuration*

### D3183 — Deux méthodes de pricing : High-Low et Close
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Deux méthodes de pricing P&F existent : **High-Low Method** et **Close Method**. Chacune n'utilise qu'**un seul point de prix**. La Close Method n'emploie que la clôture ; la High-Low Method utilise le high **ou** le low, mais pas les deux (parfois aucun).
**TRADEX-AI C1** : choix de pricing explicite à exposer ; impacte la sensibilité du chart.
*Catégorie : structure_marche*

### D3184 — Règles High-Low en colonne de X (hausse)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : En colonne de X : **utiliser le high** quand un X supplémentaire peut être tracé (ignorer le low) ; **utiliser le low** quand un X ne peut plus être tracé et que le low déclenche un reversal 3-box ; **ignorer les deux** si ni high ni low ne justifient une action.
**TRADEX-AI C1** : automate déterministe précis ; codable tel quel.
*Catégorie : signal*

### D3185 — Règles High-Low en colonne de O (baisse)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : En colonne de O : **utiliser le low** quand un O supplémentaire peut être tracé (ignorer le high) ; **utiliser le high** quand un O ne peut plus être tracé et que le high déclenche un reversal 3-box ; **ignorer les deux** sinon.
**TRADEX-AI C1** : symétrique de D3184 ; complète l'automate.
*Catégorie : signal*

### D3186 — Intraday corrige la perte de données du High-Low
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Avec un seul point par période, le High-Low peut laisser des données clés hors chart. Les **données intraday** y remédient : ~6,5 h de séance NYSE/Nasdaq → 7 périodes 60 min, 13 de 30 min, 39 de 10 min. Un chart 60 min utilise 7 points/jour même en High-Low, captant davantage de swings/highs/lows.
**TRADEX-AI C1** : argument pour alimenter le P&F en barres intraday issues de NT8 plutôt qu'en daily, afin de ne pas manquer les swings.
*Catégorie : structure_marche*

### D3187 — 60 min + box 0,50 % → 3–9 mois (moyen terme)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md, image_09, image_10) : Passer de daily→60 min et de box 1 %→0,50 % réduit le temps couvert et augmente la sensibilité ; ces charts s'étendent généralement **3 à 9 mois** (moyen terme). Ex. Urban Outfitters et VFC en 60 min / 0,50 %.
**TRADEX-AI C1** : préréglage « vue moyen terme » documenté.
*Catégorie : configuration*

### D3188 — 15 min + box 0,25 % → ~1 mois (court terme)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Un chart **15 min à box 0,25 %** couvre ~**1 mois** de données pour beaucoup de titres — étape court terme suivant la réduction d'intervalle et de box.
**TRADEX-AI C1** : préréglage « vue court terme » ; complète la grille daily/60 min/15 min.
*Catégorie : configuration*

### D3189 — Daily long terme, intraday moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Les P&F daily conviennent au long terme ; les intervalles intraday sont souvent nécessaires pour un cadrage moyen terme. L'étape court terme suivante consiste à réduire encore intervalle et box.
**TRADEX-AI C1** : confirme la correspondance intervalle ↔ horizon ; synthèse des préréglages D3182/D3187/D3188.
*Catégorie : structure_marche*

### D3190 — Top-down : tendance majeure puis setups alignés
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_scaling_and_timeframes.md) : Commencer par le look-back le plus long permet de définir la tendance majeure. Les résultats s'améliorent en cherchant des **setups bullish court terme quand la tendance long terme est haussière**. Les réglages cités sont des guides généraux à adapter à son style.
**TRADEX-AI C1** : règle d'alignement multi-horizon (filtre directionnel long terme avant entrée court terme) directement transposable à la grille de score. Écho méthodologique à Belkhayate (analyse top-down) → ⚫🔴 (assemblage propriétaire non publié).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D3171 → D3190 (20) |
| Faits vérifiés 🟢 | 20 |
| Tags secondaires | 🔵 ÉCOLE (D3174) · 🟡 CONVENTION (D3173, D3180) · ⚫🔴 Belkhayate indirect (D3177, D3190) |
| Cercle dominant | C1 (Prix / structure marché) |
| Images | 10/10 certifiées |
| Actifs cibles | GC · HG · CL · ZW (Percentage scaling = comparaison homogène) |
| Cas à vérifier | Aucun (10/10 images certifiées ; 0 ambigu) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
