# Extraction AdamGrimes — A New Look at Measuring Trend Days
**Source :** `bundles/adamgrimes/a_new_look_at_measuring_trend_days.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5031 → D5044 · **Page :** https://www.adamhgrimes.com/a-new-look-at-measuring-trend-days/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthode objective de détection des "trend days" intraday sur ES — directement applicable pour qualifier le contexte de marché avant d'émettre un signal GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle (images ES bars référencées dans le texte mais non incluses) | — | — |

## DÉCISIONS

### D5031 — Définition quantitative d'un "trend day" : 4 caractéristiques observables
🟢 **FAIT VÉRIFIÉ** (Source : a_new_look_at_measuring_trend_days.md) : Un "trend day" présente 4 caractéristiques mesurables : (1) open et close aux extrémités opposées du range journalier, (2) peu de reversals majeurs intraday, (3) range plus large que la moyenne, (4) fréquence d'environ une fois par mois. Ces critères s'appliquent aux futures S&P (ES).
**TRADEX-AI C1** : Adapter ces 4 critères pour qualifier le contexte journalier ES avant d'activer le signal TRADEX sur GC/HG/CL/ZW. Un trend day ES valide peut confirmer un alignement directionnel C2/C7.
*Catégorie : structure_marche*

### D5032 — Méthode SignedTrend : compter les nouveaux highs/lows intraday sur barres 1 minute
🔵 **ÉCOLE** (Source : a_new_look_at_measuring_trend_days.md) : Grimes propose de compter le nombre de barres 1-minute de l'ES qui établissent de nouveaux highs (NH) et nouveaux lows (NL) sur la journée. La métrique SignedTrend = NH - NL. Une valeur fortement positive indique un trend day haussier, fortement négative un trend day baissier. La variable Trend = |SignedTrend| mesure l'intensité directionnelle sans considération de direction.
**TRADEX-AI C2** : Cette logique est analogique au Delta cumulé ATAS — NH dominants = pression acheteuse persistante. Peut enrichir le filtre C2 (Order Flow) dans le moteur TRADEX pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D5033 — Seuils percentiles pour classifier la force de tendance intraday
🔵 **ÉCOLE** (Source : a_new_look_at_measuring_trend_days.md) : Sur 5 ans de données ES 1-minute, la variable Trend (|SignedTrend|) varie de 0 à 64. Grimes propose une classification percentile : >99e percentile = "strongest trend", >95e = "strong trend", >90e = "trend", >75e = "possible trend". Les jours en dessous du 75e percentile ne sont pas qualifiés comme trend days.
**TRADEX-AI C1** : Principe de percentile applicable pour calibrer les seuils de force de tendance dans TRADEX. Utiliser une approche percentile rolling sur les données NT8 pour éviter des seuils absolus non adaptatifs.
*Catégorie : indicateurs_tendance*

### D5034 — Profits mensuels intraday concentrés sur 1-2 trend days
🟢 **FAIT VÉRIFIÉ** (Source : a_new_look_at_measuring_trend_days.md) : Pour certains styles de trading intraday, l'essentiel des profits mensuels (voire tous) provient de 1 à 2 trend days par mois. Les autres jours montrent de petits gains et pertes qui s'équilibrent. Ce phénomène est documenté empiriquement par Grimes sur ES.
**TRADEX-AI C1** : Justifie la sélectivité du moteur TRADEX (score ≥ 7,0/10 + R/R ≥ 1:2) : concentrer le capital sur les opportunités de qualité, ne pas trader chaque signal marginal. Applicable GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D5035 — Réduction ou arrêt du trading sur les jours non-trend améliore la performance
🟢 **FAIT VÉRIFIÉ** (Source : a_new_look_at_measuring_trend_days.md) : Grimes indique que beaucoup de traders obtiennent de meilleurs résultats en réduisant (voire en stoppant) leur activité lors des jours non-trend. L'identification préalable du type de jour (trend vs range) est donc une composante critique de la gestion de risque intraday.
**TRADEX-AI C1** : Valide la règle TRADEX de bloquer les signaux en mode "range day" détecté. Le contexte journalier ES/GC doit être évalué avant tout signal.
*Catégorie : gestion_risque_entree*

### D5036 — Fréquence des trend days : environ 1 fois par mois (environ 5% des séances)
🟢 **FAIT VÉRIFIÉ** (Source : a_new_look_at_measuring_trend_days.md) : Les trend days se produisent approximativement une fois par mois sur l'ES, soit environ 1/20 séances. La classification percentile (>75e = "possible trend") implique que ~25% des séances peuvent être des candidats trend day selon le seuil choisi. Le top 1% représente les journées de trend exceptionnel.
**TRADEX-AI C1** : Calibrage de la fréquence attendue pour les signaux TRADEX en mode intraday sur GC/HG/CL/ZW. Une fréquence de signal trop élevée (>25% des séances) suggère un seuil trop bas.
*Catégorie : timing*

### D5037 — Alerte audio sur nouveaux highs/lows : méthode de monitoring continu du marché
🔵 **ÉCOLE** (Source : a_new_look_at_measuring_trend_days.md) : Grimes décrit l'utilisation d'alertes audio déclenchées à chaque nouveau high/low du jour sur barres 1-minute ES. La fréquence et le type (high vs low) des alertes donnent une lecture intuitive du marché sans consultation visuelle constante de l'écran. Principe : si l'alerte "S&P High" se déclenche fréquemment → journée haussière forte.
**TRADEX-AI C1** : Concept applicable dans le dashboard TRADEX : compteur temps réel NH/NL (données NT8) visible dans l'interface pour qualifier le contexte de marché en un coup d'oeil.
*Catégorie : structure_marche*
