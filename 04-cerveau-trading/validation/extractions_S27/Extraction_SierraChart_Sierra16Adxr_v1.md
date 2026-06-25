# Extraction SierraChart — ADXR
**Source :** `bundles/sierrachart/sierra_16_adxr.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8991 → D9010 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=16
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : ADXR (Average Directional Movement Index Rating) de Welles Wilder — mesure de la force de tendance lissée, utilisable comme filtre de confirmation de tendance pour les actifs TRADEX (GC/HG/CL/ZW).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D8991 — Définition ADXR : Average Directional Movement Index Rating
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : L'ADXR est l'Average Directional Movement Index Rating de Welles Wilder. Il est basé sur des calculs similaires à l'ADX (Average Directional Movement Index), mais avec un lissage supplémentaire via le paramètre ADXR Interval.
**TRADEX-AI C1** : L'ADXR est une version lissée de l'ADX — moins réactif aux faux signaux mais plus retardé. Pour TRADEX-AI, utile comme filtre de tendance "stable" sur GC/HG/CL/ZW pour éviter les entrées en marché sans tendance.
*Catégorie : indicateurs_tendance*

### D8992 — Formule ADXR : lissage de l'ADX courant et passé
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : L'ADXR est calculé à l'index t en combinant la valeur ADX courante et la valeur ADX retardée de n_ADXR périodes en arrière. La formule est : ADXR_t = (ADX_t + ADX_{t-n_ADXR}) / 2. Le calcul commence à t ≥ n_DX + n_ADX + n_ADXR - 2.
**TRADEX-AI C1** : Cette moyenne de deux ADX espacés de n_ADXR périodes rend l'ADXR plus stable que l'ADX simple. Pour TRADEX-AI, cela réduit le risque d'entrer en tendance sur un pic ADX isolé (faux signal de tendance forte).
*Catégorie : indicateurs_tendance*

### D8993 — Paramètre DX Length (n_DX)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : Le paramètre DX Length (noté n_DX) définit la période utilisée pour calculer le DX (Directional Movement Index), qui est la base des calculs ADX et ADXR. C'est la période de smoothing des +DI et -DI de Wilder.
**TRADEX-AI C1** : DX Length standard = 14 périodes (valeur Wilder originale). Sur range bars NT8 pour GC ou CL, tester DX Length=14 comme point de départ. Une valeur inférieure (10) augmente la réactivité; supérieure (20) augmente la stabilité.
*Catégorie : indicateurs_tendance*

### D8994 — Paramètre DX Mov Avg Length (n_ADX)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : Le paramètre DX Mov Avg Length (noté n_ADX) définit la période de la moving average appliquée au DX pour calculer l'ADX intermédiaire, lui-même utilisé dans le calcul de l'ADXR.
**TRADEX-AI C1** : DX Mov Avg Length standard = 14 périodes (valeur Wilder). En pratique, DX Length et DX Mov Avg Length sont souvent fixés à la même valeur. Pour TRADEX-AI, conserver n_ADX = n_DX = 14 par défaut.
*Catégorie : indicateurs_tendance*

### D8995 — Paramètre ADXR Interval (n_ADXR)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : Le paramètre ADXR Interval (noté n_ADXR) définit l'espacement temporel entre le ADX courant et le ADX passé utilisés dans la moyenne. La formule est ADXR = (ADX_t + ADX_{t-n_ADXR}) / 2.
**TRADEX-AI C1** : ADXR Interval standard = 14 périodes. Plus n_ADXR est grand, plus l'ADXR est lissé et retardé. Pour TRADEX-AI sur marchés futures rapides (CL pétrole), un n_ADXR=10 peut être plus adapté pour réduire le lag.
*Catégorie : indicateurs_tendance*

### D8996 — Délai de calcul : ADXR nécessite n_DX + n_ADX + n_ADXR - 2 barres minimum
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : L'ADXR commence à être calculé uniquement à partir de l'index t ≥ n_DX + n_ADX + n_ADXR - 2. Avec les valeurs standard (14+14+14-2=40), il faut 40 barres minimum avant d'obtenir une valeur ADXR.
**TRADEX-AI C1** : Au démarrage de TRADEX-AI ou après un redémarrage, attendre au minimum 40 barres (avec paramètres standard) avant d'utiliser le signal ADXR. Implémenter un contrôle de "warmup" dans le moteur Python pour éviter les signaux prématurés.
*Catégorie : gestion_risque_entree*

### D8997 — Relation ADXR / ADX : ADXR = version lissée de l'ADX
🔵 **ÉCOLE** (Source : sierra_16_adxr.md) : L'ADXR est une version plus lissée et donc plus lente que l'ADX. Alors que l'ADX mesure la force de la tendance en cours, l'ADXR confirme si cette tendance est soutenue dans le temps (car la moyenne inclut une valeur passée). Un ADXR montant confirme qu'une tendance s'installe dans la durée.
**TRADEX-AI C1** : Utiliser l'ADXR pour filtrer les entrées en mode Auto : ADXR > 25 = tendance établie (signal fiable), ADXR < 20 = marché sans direction (bloquer entrées en suivi de tendance), ADXR < 15 = range (inverser logique → mean reversion).
*Catégorie : gestion_risque_entree*

### D8998 — Seuils opérationnels ADXR standard
🔵 **ÉCOLE** (Source : sierra_16_adxr.md) : Les seuils ADXR standard hérités de la méthode ADX de Wilder sont : < 20 = tendance faible ou absente, 20-25 = début de tendance, > 25 = tendance établie, > 40 = tendance très forte (potentiellement à bout de souffle).
**TRADEX-AI C1** : Configuration TRADEX-AI recommandée : ADXR < 20 → bloquer signaux TREND FOLLOWING (autoriser uniquement signals mean reversion) · ADXR 20-25 → signaux avec confirmation supplémentaire requise · ADXR > 25 → signaux valides · ADXR > 50 → surveiller retournement.
*Catégorie : gestion_risque_entree*

### D8999 — Disponibilité : Format Spreadsheet Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : Sierra Chart fournit les formules ADXR dans un fichier spreadsheet `ADXR.16.scss` accessible depuis File >> Open Spreadsheet. Ce fichier contient l'implémentation complète avec les formules intermédiaires DX, +DI, -DI, ADX.
**TRADEX-AI C1** : Utiliser ADXR.16.scss comme référence de validation pour l'implémentation Python de l'ADXR dans TRADEX-AI lors de la Phase C (vérifier cohérence calculs avec Sierra Chart).
*Catégorie : indicateurs_tendance*

### D9000 — Comparaison ADXR vs ADX pour TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_16_adxr.md) : L'ADXR offre une mesure de force de tendance plus stable que l'ADX mais avec un délai supplémentaire. L'ADX est plus réactif aux changements de tendance récents. Les deux partagent la même base de calcul (DX de Wilder) mais diffèrent par le lissage final.
**TRADEX-AI C1** : Pour TRADEX-AI, l'ADXR est préférable à l'ADX comme filtre de tendance dans le moteur Python (moins de faux signaux liés à des pics ADX isolés). Implémenter ADXR comme garde-fou C1 dans le circuit breaker de signal.
*Catégorie : indicateurs_tendance*

### D9001 — Application sur actifs TRADING TRADEX (GC/HG/CL/ZW)
🟡 **SYNTHÈSE** (Source : sierra_16_adxr.md) : L'ADXR s'applique uniformément à tout actif avec données OHLC. Les paramètres standard (DX Length=14, DX Mov Avg Length=14, ADXR Interval=14) sont un point de départ. Les marchés des matières premières ont des caractéristiques de tendance différentes : GC tend à avoir des tendances plus soutenues que CL (plus volatile).
**TRADEX-AI C1** : Paramétrage proposé par actif : GC → ADXR(14,14,14) conservateur · HG → ADXR(14,14,10) légèrement plus réactif · CL → ADXR(10,10,10) pour capturer les tendances rapides · ZW → ADXR(14,14,14) standard. À valider Phase C.
*Catégorie : configuration*

### D9002 — Lien ADXR avec méthode Belkhayate : filtre de force directionnelle
🟡 **SYNTHÈSE** (Source : sierra_16_adxr.md) : La méthode Belkhayate utilise la "Direction" (BGC direction) et l'"Énergie" comme indicateurs de force directionnelle. L'ADXR est un indicateur externe complémentaire qui mesure la force de la tendance sans référence à la méthode Belkhayate. Les deux approches peuvent se confirmer mutuellement.
**TRADEX-AI C1** : Dans le cercle C1 (Prix Belkhayate), l'ADXR peut servir de validation externe : BGC Direction haussière + ADXR > 25 = forte confirmation du signal. Discordance BGC haussier + ADXR < 20 = signal ambigu, réduire confiance.
*Catégorie : configuration*

### D9003 — Implémentation Python : calcul ADXR sans bibliothèque externe
🟡 **SYNTHÈSE** (Source : sierra_16_adxr.md) : La formule ADXR = (ADX_t + ADX_{t-n_ADXR}) / 2 est simple à implémenter en Python avec numpy/pandas. Nécessite : (1) calcul du True Range, (2) +DM/-DM de Wilder, (3) lissage Wilder sur n_DX, (4) DX = 100 * |+DI - -DI| / (+DI + -DI), (5) ADX = Wilder MA du DX sur n_ADX, (6) ADXR = moyenne ADX courant et ADX retardé.
**TRADEX-AI C1** : Ajouter ADXR dans `05-saas/engine/correlations.py` ou créer `05-saas/engine/indicators.py` dédié aux indicateurs techniques auxiliaires lors de la Phase C. Utiliser pandas.Series.rolling() pour les calculs vectorisés.
*Catégorie : indicateurs_tendance*

### D9004 — Comportement ADXR en début de données insuffisantes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_16_adxr.md) : L'ADXR ne produit aucune valeur avant t = n_DX + n_ADX + n_ADXR - 2. Pour les paramètres standard (14,14,14) : 40 barres de warmup minimum. Pour des paramètres plus larges (20,20,20) : 58 barres de warmup.
**TRADEX-AI C1** : Dans le moteur Python TRADEX-AI, implémenter une vérification dans `staleness_monitor.py` : si le nombre de barres depuis le démarrage < warmup_adxr, retourner ADXR=None et traiter comme donnée non disponible (pas de blocage du signal, mais pas de confirmation ADXR non plus).
*Catégorie : gestion_risque_entree*

### D9005 — ADXR dans le contexte multi-timeframe TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_16_adxr.md) : L'ADXR calculé sur un timeframe donné reflète la force de tendance à cette échelle temporelle. Un ADXR fort sur le timeframe mensuel indique une tendance de fond, tandis qu'un ADXR sur le timeframe intraday indique la dynamique à court terme.
**TRADEX-AI C1** : Pour TRADEX-AI, calculer l'ADXR sur 2 timeframes minimum : (1) Daily — pour la tendance de fond (C4 Macro context) et (2) Intraday NT8 range bars — pour la confirmation entry timing. Alignement des deux ADXR > 25 = signal haute conviction.
*Catégorie : configuration*
