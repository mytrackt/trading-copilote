# Extraction SierraChart — Laguerre RSI
**Source :** `bundles/sierrachart/sierra_500_laguerre_rsi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9411 → D9420 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=500
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Laguerre RSI = RSI ultra-lissé basé sur le filtre Laguerre (John Ehlers) — réduit le bruit et identifie les zones de surachat/survente avec moins de faux signaux que le RSI standard sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9411 — Définition Laguerre RSI : RSI avec lissage Laguerre Filter
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : Le Laguerre RSI est une implémentation ACSIL de l'indicateur décrit dans les Figures 14.8 et 14.9 du livre "Cybernetic Analysis for Stocks and Futures" de John Ehlers. Il peut être assimilé à un RSI dans lequel le Average Type est un Laguerre Moving Average, composé des éléments du Laguerre Filter.
**TRADEX-AI C1** : Le Laguerre RSI est un indicateur momentum avancé basé sur la théorie des cycles de John Ehlers — adapté pour les marchés à tendance cyclique comme l'or (GC) et le pétrole (CL) qui ont des cycles saisonniers bien documentés.
*Catégorie : indicateurs_momentum*

### D9412 — Source académique : livre "Cybernetic Analysis" de John Ehlers
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : L'implémentation Sierra Chart est basée sur les Figures 14.8 et 14.9 du livre "Cybernetic Analysis for Stocks and Futures" de John Ehlers (auteur reconnu dans le domaine des indicateurs basés sur la théorie des signaux et des filtres numériques).
**TRADEX-AI C1** : Référence académique vérifiable — John Ehlers est l'auteur de MESA (Maximum Entropy Spectral Analysis) et de nombreux indicateurs basés sur les cycles de marché. Cette implémentation Sierra Chart est fidèle à la source originale.
*Catégorie : indicateurs_momentum*

### D9413 — Paramètre Damping Factor (gamma) : pondération des valeurs passées
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : L'input `Damping Factor` (noté γ, lettre grecque gamma) détermine le facteur de pondération donné aux valeurs actuelles et passées de l'Input Data. C'est le paramètre principal contrôlant la réactivité vs lissage de l'indicateur.
**TRADEX-AI C1** : Le Damping Factor est l'équivalent du paramètre "période" d'un RSI standard, mais avec une logique différente : un gamma élevé (proche de 1) donne plus de poids aux valeurs passées (plus lisse), un gamma faible (proche de 0) donne plus de poids aux valeurs récentes (plus réactif). Valeur typique recommandée : 0.5 (selon Ehlers).
*Catégorie : indicateurs_momentum*

### D9414 — Architecture interne : Up Sum et Down Sum par Laguerre Filter
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : Le calcul du Laguerre RSI passe d'abord par le calcul d'un "Up Sum" (U_t) et d'un "Down Sum" (D_t), chacun dérivé du Laguerre Filter appliqué à l'Input Data avec le Damping Factor γ. Le Laguerre RSI final est ensuite calculé comme RSI_L = U_t / (U_t + D_t).
**TRADEX-AI C1** : Cette structure Up/Down Sum est similaire à celle du RSI de Wilder mais avec un filtre Laguerre au lieu d'une Wilder Smoothing — ce qui réduit l'effet de "bande passante" qui crée des faux signaux dans les RSI standards.
*Catégorie : indicateurs_momentum*

### D9415 — Output : valeur entre 0 et 1 (pas 0-100 comme RSI standard)
🟡 **SYNTHÈSE** (Source : sierra_500_laguerre_rsi.md) : La formule RSI_L = U_t / (U_t + D_t) produit une valeur normalisée entre 0 et 1 (et non entre 0 et 100 comme le RSI standard de Wilder). Les niveaux Line 1 Value et Line 2 Value doivent donc être définis dans cette plage.
**TRADEX-AI C1** : Attention critique : si TRADEX-AI compare le Laguerre RSI avec un RSI standard, l'échelle est différente. Niveaux de référence recommandés : Line 1 = 0.8 (surachat, équivalent 80 sur RSI standard), Line 2 = 0.2 (survente, équivalent 20 sur RSI standard), selon la recommandation d'Ehlers.
*Catégorie : indicateurs_momentum*

### D9416 — Paramètre Line 1 Value : niveau de surachat configurable
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : L'input `Line 1 Value` permet de définir un niveau horizontal affiché sur le chart — typiquement utilisé pour marquer le seuil de surachat. La valeur doit être dans la plage 0-1 (échelle du Laguerre RSI).
**TRADEX-AI C1** : Pour TRADEX-AI, Line 1 Value = 0.8 constitue la zone de surachat standard (convention Ehlers). Un Laguerre RSI > 0.8 sur GC (or) avec un signal Belkhayate C1 baissier = confluence signal vente potentiel.
*Catégorie : indicateurs_momentum*

### D9417 — Paramètre Line 2 Value : niveau de survente configurable
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : L'input `Line 2 Value` permet de définir un second niveau horizontal — typiquement utilisé pour marquer le seuil de survente. La valeur doit être dans la plage 0-1 (échelle du Laguerre RSI).
**TRADEX-AI C1** : Pour TRADEX-AI, Line 2 Value = 0.2 constitue la zone de survente standard (convention Ehlers). Un Laguerre RSI < 0.2 sur GC (or) avec un signal Belkhayate C1 haussier = confluence signal achat potentiel.
*Catégorie : indicateurs_momentum*

### D9418 — Avantage vs RSI standard : moins de faux signaux en tendance forte
🟡 **SYNTHÈSE** (Source : sierra_500_laguerre_rsi.md) : Le Laguerre Filter utilisé en base du calcul introduit un lissage adaptatif basé sur les composants du filtre numérique. Selon Ehlers dans "Cybernetic Analysis", cela réduit significativement les faux signaux de surachat/survente en tendance forte par rapport au RSI de Wilder.
**TRADEX-AI C1** : Avantage majeur pour TRADEX-AI : lors de tendances directionnelles fortes sur GC ou CL (Belkhayate Energie élevée), le Laguerre RSI reste moins longtemps en zone de "faux surachat" que le RSI standard — moins de signaux contraires parasites au Niveau 1.
*Catégorie : indicateurs_momentum*

### D9419 — Input Data : applicable à tout type de données de prix
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : L'input `Input Data` détermine sur quelle donnée de prix le Laguerre RSI est calculé. Comme pour toutes les études Sierra Chart, cela peut être Open, High, Low, Close, ou des valeurs issues d'autres études.
**TRADEX-AI C1** : Pour TRADEX-AI, application sur le Close (prix de clôture de la range bar) — cohérent avec la méthode Belkhayate. Une variante sur le prix médian (HL/2) ou typique (HLC/3) est possible pour réduire l'impact des mèches extrêmes sur les marchés volatils.
*Catégorie : indicateurs_momentum*

### D9420 — Spreadsheet disponible + référence livre Ehlers
🟢 **FAIT VÉRIFIÉ** (Source : sierra_500_laguerre_rsi.md) : Sierra Chart fournit un fichier spreadsheet `Laguerre_RSI.500.scss`. La dernière modification date du 24 janvier 2025. La référence primaire est le livre "Cybernetic Analysis for Stocks and Futures" de John Ehlers (Figures 14.8 et 14.9).
**TRADEX-AI C1** : Deux sources de validation indépendantes disponibles : (1) le spreadsheet Sierra Chart pour recalculer les valeurs, (2) le livre Ehlers comme référence académique primaire. Ces ressources permettent de valider une implémentation Python indépendante du Laguerre RSI si nécessaire pour le moteur TRADEX-AI.
*Catégorie : indicateurs_momentum*
