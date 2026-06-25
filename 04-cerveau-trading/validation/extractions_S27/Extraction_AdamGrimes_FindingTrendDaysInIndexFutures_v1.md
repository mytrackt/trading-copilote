# Extraction AdamGrimes — Finding Trend Days In Index Futures
**Source :** `bundles/adamgrimes/finding_trend_days_in_index_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** N/A · 0/0 certifiées · 0 à vérifier
**Décisions :** D5811 → D5830 · **Page :** https://www.adamhgrimes.com/finding-trend-days-in-index-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Identification anticipée des jours de tendance forte via compression de volatilité multi-timeframe, applicable ES/GC.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

## DÉCISIONS

### D5811 — Profits intraday concentrés sur 1-2 jours de tendance par mois
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : En trading intraday, la majorité des profits mensuels provient de 1 à 2 journées de tendance exceptionnelles. Identifier ces jours à l'avance permet une application plus agressive du risque.
**TRADEX-AI C1** : Sur ES (confirmation), filtrer les jours à fort potentiel de tendance pour moduler la taille de position sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D5812 — Compression de volatilité = setup tendance jour suivant
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : La compression de volatilité (range journalier serré, inside days successifs) est l'un des meilleurs setups pour anticiper un jour de tendance le lendemain. Plus la compression est prolongée, plus le setup est fort.
**TRADEX-AI C1** : Intégrer la détection de compression de volatilité multi-jours dans le moteur Python comme pré-filtre niveau 1 (0$) avant appel Claude API.
*Catégorie : structure_marche*

### D5813 — Double inside day = signal fort de trend day imminent
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : Deux inside days consécutifs constituent un signal de haute probabilité de jour de tendance le lendemain. Chaque journée de compression supplémentaire renforce la probabilité.
**TRADEX-AI C1** : Ajouter règle : si 2+ inside days consécutifs sur ES → probabilité trend day élevée → alerter en mode Manuel.
*Catégorie : configuration*

### D5814 — Les outils de probabilité donnent un léger avantage, pas une certitude
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : Aucun outil de prédiction des jours de tendance n'est parfait. Tous ces outils ne font que décaler légèrement les probabilités en faveur du trader. Des setups solides échouent fréquemment et des tendances émergent sans setup apparent.
**TRADEX-AI C1** : Le score /10 de TRADEX-AI représente une probabilité biaisée, jamais une certitude ; le seuil ≥7,0 est un filtre probabiliste, pas une garantie.
*Catégorie : psychologie*

### D5815 — Combiner approche discrétionnaire et outils quantitatifs
🔵 **ÉCOLE** (Source : finding_trend_days_in_index_futures.md) : La meilleure approche combine l'intuition humaine avec la rigueur quantitative. Les outils statistiques structurent et informent le jugement discrétionnaire plutôt que de le remplacer.
**TRADEX-AI C1** : Architecture TRADEX-AI (Python filtre → Claude analyse) matérialise exactement ce principe : quant en niveau 1-2, discrétionnaire/IA en niveau 3.
*Catégorie : psychologie*

### D5816 — Lire la structure journalière avant la séance
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : Évaluer le setup de tendance en regardant le graphique journalier à la clôture de la veille permet de se préparer avant l'ouverture. Le contexte journalier précède et conditionne la lecture intraday.
**TRADEX-AI C1** : Le moteur doit intégrer une lecture daily close sur ES/GC avant la session pour calibrer le biais directionnel.
*Catégorie : timing*

### D5817 — Compression de volatilité valable sur plusieurs timeframes simultanément
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : Lorsque la compression de volatilité est visible simultanément sur plusieurs timeframes (daily + intraday), le setup de trend day est renforcé. La confluence multi-timeframe augmente la probabilité.
**TRADEX-AI C1** : Vérifier la compression de volatilité sur au moins 2 timeframes (daily + 60min) pour valider le setup pré-session.
*Catégorie : indicateurs_tendance*

### D5818 — Premier quart d'heure révèle la direction potentielle
🔵 **ÉCOLE** (Source : finding_trend_days_in_index_futures.md) : Si le marché montre un setup de trend day, le premier quart d'heure (ou première heure) révèle souvent la direction par un premier mouvement directionnel. Attendre ce signal avant de s'engager.
**TRADEX-AI C1** : En mode Manuel, le signal TRADEX-AI pré-session doit être confirmé par la dynamique de la première heure avant d'engager une position.
*Catégorie : timing*

### D5819 — Journées sans setup peuvent devenir de forts jours de tendance
🟢 **FAIT VÉRIFIÉ** (Source : finding_trend_days_in_index_futures.md) : De nombreuses journées de tendance puissante (40+ points sur ES) surviennent sans setup préalable clair. L'absence de setup ne garantit pas l'absence de tendance.
**TRADEX-AI C5** : Le VIX et les événements macro (FOMC, NFP) peuvent déclencher des trend days sans compression préalable ; ces cas sont couverts par le News Gate.
*Catégorie : macro_evenements*

### D5820 — La compression de volatilité fonctionne aussi pour le trade management long terme
🔵 **ÉCOLE** (Source : finding_trend_days_in_index_futures.md) : Même pour les traders long terme, la compression de volatilité fournit des informations utiles pour les décisions d'entrée et de gestion de position, pas seulement pour le trading intraday.
**TRADEX-AI C1** : Les actifs TRADING (GC/HG/CL/ZW) peuvent bénéficier de la détection de compression de volatilité pour optimiser les points d'entrée et ajustement de stops.
*Catégorie : gestion_position_active*
