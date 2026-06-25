# Extraction StockCharts — Vortex Indicator
**Source :** `bundles/stockcharts/vortex_indicator.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D4831 → D4850 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/vortex-indicator

**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : indicateur directionnel basé sur True Range utile pour GC/HG/CL/ZW comme confirmateur de tendance dans le Cercle C1, notamment pour identifier le début de tendances et les signaux de retournement.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/yd8Rj4RvICKtfHEqYrvE | Chart 1 — Formule VTX (spreadsheet illustration) | Calculation | D4831 |
| /files/G3EeYwTN5eab6LFHYGlM | Spreadsheet — Calcul VTX détaillé | Calculation | D4831 |
| /files/5DIah7gvCSW7RZz0QzHQ | Chart 2 — QQQ weekly 26-period VTX crossovers | VM Crossovers | D4834 |
| /files/GWzh60s9PEQLY0ij2MoZ | Chart 3 — BAX daily 23-period VTX consolidation | VM Crossovers | D4835 |
| /files/6bwwc7DWWPtVJgFX2TYl | Chart 4 — MCHP daily 23-period VTX threshold signals | VM Thresholds | D4837 |
| /files/25gWKdbwb50mwgJcEptQ | Chart 6 — COMPQ SharpCharts Vortex setup | SharpCharts | D4843 |

---

## DÉCISIONS

### D4831 — Formule complète du Vortex Indicator (VTX)
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md, /files/yd8Rj4RvICKtfHEqYrvE, /files/G3EeYwTN5eab6LFHYGlM) : VTX = deux oscillateurs +VI et -VI. Calcul : +VM = |High courant − Low précédent| ; -VM = |Low courant − High précédent| ; +VM14 = somme 14 périodes de +VM ; -VM14 = somme 14 périodes de -VM. TR14 = somme 14 périodes du True Range (max de : |H-L|, |H-Close_prec|, |L-Close_prec|). +VI14 = +VM14/TR14 ; -VI14 = -VM14/TR14. Les deux oscillateurs oscillent au-dessus/en dessous de 1.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW sur range bars NT8, calculer +VI14 et -VI14 comme indicateurs directionnels normalisés par la volatilité (True Range) — supérieur à un RSI directionnel car corrigé de la volatilité de l'actif.
*Catégorie : indicateurs_tendance*

### D4832 — Développeurs et fondement théorique du VTX
🔵 **ÉCOLE** (Source : vortex_indicator.md) : Développé par Etienne Botes et Douglas Siepman, le VTX s'appuie sur les travaux de Welles Wilder (True Range, concept fondamental) et Viktor Schauberger (considéré comme le père de la technologie d'implosion). L'indicateur capture les mouvements de tendance positifs et négatifs malgré une formule complexe, mais reste facile à interpréter.
**TRADEX-AI C1** : La base True Range de Wilder est commune à l'ATR Belkhayate (proxy Énergie) — le VTX et l'Énergie Belkhayate partagent la même fondation conceptuelle, ce qui en fait des indicateurs complémentaires naturels sur GC/CL.
*Catégorie : indicateurs_tendance*

### D4833 — Interprétation : +VI > -VI = haussier ; -VI > +VI = baissier
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md) : Interprétation directe : quand +VI est au-dessus de -VI, la tendance est haussière. Quand -VI est supérieur à +VI, la tendance est baissière. L'indicateur est soit haussier soit baissier de façon binaire et permanente (pas de zone neutre) — il a toujours un biais clair.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, utiliser +VI > -VI comme condition binaire de tendance haussière confirmée. Ce biais directionnel permanent est idéal comme filtre dans la grille de score TRADEX /10 — +1 point si +VI > -VI pour un signal long.
*Catégorie : indicateurs_tendance*

### D4834 — Crossovers VTX : signal de début de tendance et whipsaws
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md, /files/5DIah7gvCSW7RZz0QzHQ) : Le crossover +VI/-VI signal le début d'une tendance. Sur QQQ weekly 26-period sur 6,5 ans : plus d'une douzaine de crossovers, avec des zones haussières durables > 6 mois. Les zones en bleu montrent des périodes d'indécision (consolidation, les deux indicateurs autour de 1). Les whipsaws sont une réalité inhérente.
**TRADEX-AI C1** : Sur GC weekly (ZW aussi), utiliser VTX(26) sur weekly comme filtre de tendance de fond. Si +VI > -VI sur weekly, ne trader que les signaux longs sur daily. Pendant les consolidations (les deux autour de 1), réduire la taille de position ou s'abstenir.
*Catégorie : indicateurs_tendance*

### D4835 — Consolidation : VTX en range autour de 1 = éviter les trades
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md, /files/GWzh60s9PEQLY0ij2MoZ) : Quand le VTX trade dans un range étroit autour de 1 (comme BAX d'octobre à début novembre), cela marque une phase de consolidation avec formation d'un triangle. Les whipsaws augmentent en début de signaux car la tendance n'est pas encore établie.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW : si +VI et -VI oscillent tous deux entre 0.95 et 1.05, BLOQUER les signaux automatiques TRADEX-AI — l'actif est en consolidation et les signaux seront non fiables. Afficher "Marché en consolidation — attendre" en mode Manuel.
*Catégorie : structure_marche*

### D4836 — Validation par confirmation au-dessus de 1 après crossover
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md) : Pour qualifier un signal de crossover et réduire les whipsaws, attendre une confirmation : le bullish crossover est validé quand +VM monte au-dessus de 1, et un bearish crossover est validé quand -VM monte au-dessus de 1. Cette attente de confirmation filtre les faux signaux de consolidation.
**TRADEX-AI C1** : Sur GC/CL, requérir +VI > 1.0 après un crossover haussier avant de comptabiliser ce signal dans la grille de score TRADEX /10. Crossover sans confirmation > 1.0 = signal non validé.
*Catégorie : gestion_risque_entree*

### D4837 — Seuils de signal : -VI < 0.90 puis +VI > 1.10 = signal haussier robuste
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md, /files/6bwwc7DWWPtVJgFX2TYl) : Méthode des seuils pour réduire les whipsaws : signal haussier en deux temps — (1) tendance baissière s'affaiblit (-VI descend sous 0.90), puis (2) tendance haussière se renforce (+VI monte au-dessus de 1.10). Signal baissier symétrique : (1) +VI < 0.90, puis (2) -VI > 1.10. Cette méthode génère moins de signaux mais plus fiables.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW : utiliser les seuils 0.90/1.10 comme filtres de qualité VTX. Un signal haussier VTX "threshold" (-VI < 0.90 → +VI > 1.10) doit ajouter +1.5 points dans la grille /10 (vs +1 pour un simple crossover) car plus robuste.
*Catégorie : gestion_risque_entree*

### D4838 — Période de lookback 23 (≈ 1 mois) pour daily charts
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md) : Sur graphiques journaliers, une période de 23 couvre approximativement un mois de trading. Un lookback de 14 périodes sur daily sera beaucoup plus sensible (volatile) qu'une période 23. Raccourcir la période augmente la sensibilité et génère plus de crossovers de seuils.
**TRADEX-AI C1** : Sur range bars NT8 pour GC/CL : tester VTX(14) comme période standard (compromis sensibilité/fiabilité). Si trop de whipsaws, passer à VTX(23). Documenter dans settings.py le paramètre retenu après validation.
*Catégorie : configuration*

### D4839 — Multi-timeframe VTX : weekly pour tendance, daily pour signaux
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md) : Le VTX peut être appliqué sur weekly et mensuel pour définir la tendance majeure, puis sur daily pour générer des signaux dans le sens de cette tendance. Les chartists se concentrent sur les signaux haussiers (daily) uniquement quand le VTX weekly indique une tendance haussière.
**TRADEX-AI C1** : Architecture TRADEX recommandée pour GC/CL : VTX(26) weekly = filtre de tendance macro (C3/C4) ; VTX(14) sur range bars = signal d'entrée (C1). Seuls les signaux daily alignés avec le biais weekly sont comptabilisés dans la grille /10.
*Catégorie : configuration*

### D4840 — VTX confirmé par patterns chartistes : wedge breakout
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md) : Le VTX n'est pas conçu comme indicateur standalone. L'exemple montre : signal VTX haussier début janvier confirmé par un wedge breakout ; signal VTX baissier en avril confirmé par un rising wedge suivi de la cassure sous le support wedge. VTX donne l'alerte, le graphique des prix fournit les signaux.
**TRADEX-AI C1** : Dans TRADEX-AI, VTX = alerteur de début de tendance (Cercle C1), patterns chartistes NT8 = confirmateurs. Signal TRADEX valide si : VTX threshold signal + cassure de structure de prix (support/résistance) + alignement 3/4 actifs trading.
*Catégorie : structure_marche*

### D4841 — Positive Trend Movement (+VM) : mesure distance High-Low précédent
🔵 **ÉCOLE** (Source : vortex_indicator.md) : Le mouvement de tendance positif (+VM) = distance du High courant au Low précédent (valeur absolue). Plus le High courant est éloigné du Low précédent, plus le mouvement de tendance positif est fort. Le négatif (-VM) = distance du Low courant au High précédent.
**TRADEX-AI C1** : Sur GC/CL, un +VM élevé signifie que le prix courant a fortement progressé par rapport au range précédent — indicateur de pression directionnelle pure, complémentaire au Delta ATAS (Cercle C2) qui mesure la pression d'order flow.
*Catégorie : indicateurs_tendance*

### D4842 — Normalisation par True Range : correction de volatilité
🔵 **ÉCOLE** (Source : vortex_indicator.md) : La normalisation des mouvements de tendance par le True Range (TR) produit un indicateur ajusté à la volatilité. Cela permet de comparer des signaux VTX entre actifs à volatilités différentes (ex. GC vs ZW). Sans cette normalisation, les actifs volatils auraient mécaniquement des valeurs +VM/-VM plus élevées.
**TRADEX-AI C7** : Sur GC/HG/CL/ZW, les valeurs +VI et -VI sont directement comparables entre actifs grâce à la normalisation TR — utile dans le Cercle C7 (Corrélations) pour calculer la "force directionnelle relative" de chaque actif trading.
*Catégorie : correlations*

### D4843 — Signaux VTX dans un contexte de tendance forte (uptrend)
🟢 **FAIT VÉRIFIÉ** (Source : vortex_indicator.md, /files/6bwwc7DWWPtVJgFX2TYl) : Sur Microchip Technology (MCHP) en 12 mois avec VTX(23) : malgré de nombreux crossovers, seuls 3 signaux "threshold" robustes ont émergé. Le signal haussier de septembre est resté actif malgré des mouvements de +VM sous 0.90, car -VI n'a jamais confirmé la réversion avec un move > 1.10. Signal resté bullish jusqu'à confirmation baissière complète.
**TRADEX-AI C1** : Un signal VTX haussier "threshold" reste actif jusqu'à ce qu'un signal baissier complet soit déclenché (-VI < 0.90 puis -VI > 1.10). Ne pas invalider un signal VTX haussier sur simple crossover sans confirmation de seuil sur GC/HG/CL/ZW.
*Catégorie : gestion_position_active*

