# Extraction AdamGrimes — How to Calculate SigmaSpikes
**Source :** `bundles/adamgrimes/how_to_calculate_sigmaspikes.md` (HTTP 200) + 0 images certifiées
**Méthode images :** sans image · 0/0 certifiées · 0 à vérifier
**Décisions :** D6051 → D6060 · **Page :** https://www.adamhgrimes.com/how-to-calculate-sigmaspikes/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Mesure de volatilité normalisée (SigmaSpike) applicable à GC/HG/CL/ZW pour détecter les jours extrêmes et filtrer les signaux.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6051 — SigmaSpike : définition et formule
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : Le SigmaSpike mesure le retour journalier d'un actif en multiple de l'écart-type glissant 20 jours, décalé d'un jour pour éviter le look-ahead bias. Formule exacte : `return = close_today / close_yesterday - 1` → `stdev = stdev(returns, 20)` → `SigmaSpike = return_today / stdev_yesterday`.
**TRADEX-AI C1** : Implémenter SigmaSpike sur GC, HG, CL, ZW pour détecter les jours de volatilité anormale (|SigmaSpike| > 2 ou > 3) et bloquer ou filtrer les signaux d'entrée sur ces jours.
*Catégorie : indicateurs_momentum*

### D6052 — Fenêtre 20 jours : compromis réactivité/stabilité
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : Une fenêtre de 20 jours de bourse est choisie comme équilibre optimal : une fenêtre plus courte est trop instable, une fenêtre plus longue répond trop lentement aux changements de régime de volatilité.
**TRADEX-AI C1** : Utiliser strictement `stdev_window = 20` (jours de bourse) dans le calcul SigmaSpike pour tous les actifs TRADEX. Ne pas confondre avec des jours calendaires.
*Catégorie : indicateurs_momentum*

### D6053 — Décalage d'un jour : protection contre le look-ahead bias
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : On divise le retour d'aujourd'hui par l'écart-type d'HIER (et non celui d'aujourd'hui), car l'ATR/stdev du jour en cours n'est connu qu'à la clôture. Utiliser l'écart-type du jour même gonflerait artificiellement la baseline pour les jours extrêmes, les rendant moins marquants.
**TRADEX-AI C1** : Dans `staleness_monitor.py` et `data_reader.py`, s'assurer que le calcul SigmaSpike utilise toujours `stdev[t-1]` et non `stdev[t]`. Règle absolue de time-leakage.
*Catégorie : gestion_risque_entree*

### D6054 — True Range vs Range simple : supériorité pour les gaps overnight
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : Le True Range (ATR) est supérieur au Range simple car il intègre les gaps overnight et peut être appliqué à des séries "close-only" (données économiques sans high/low). Ceci améliore la qualité du baseline de volatilité.
**TRADEX-AI C4** : Pour les actifs de confirmation DX et ES, utiliser ATR-based stdev plutôt que range simple, car ces marchés peuvent subir des gaps overnight significatifs lors d'événements macro (NFP, FOMC).
*Catégorie : macro_evenements*

### D6055 — Universalité de la mesure : comparaison cross-actifs
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : La normalisation par l'écart-type permet de comparer la volatilité entre actifs de niveaux de prix et volatilités absolues très différents (ex : GC à 2000$ vs ZW à 5$). Un SigmaSpike de +3 a la même signification sur l'Or que sur le Blé.
**TRADEX-AI C7** : Le SigmaSpike est l'outil recommandé pour comparer les mouvements cross-actifs dans la matrice de corrélations live (C7). Remplace avantageusement le % de variation brut pour les alertes de divergence.
*Catégorie : correlations*

### D6056 — Adoption industrielle : standard risk management et options
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_sigmaspikes.md) : Le calcul SigmaSpike est utilisé par pratiquement tous les traders d'options et systèmes de gestion du risque professionnels. Ce n'est pas une idiosyncrasie de Grimes mais un standard de l'industrie financière.
**TRADEX-AI C5** : La mesure SigmaSpike est institutionnellement validée. Son intégration dans le scoring /10 de TRADEX (Cercle C5 sentiment) renforce la crédibilité systémique de l'approche.
*Catégorie : gestion_risque_entree*

### D6057 — Dépersonnalisation des grands mouvements de prix
🔵 **ÉCOLE** (Source : how_to_calculate_sigmaspikes.md) : Le SigmaSpike permet de "dépersonnaliser" les grandes variations de prix. Un mouvement de 50$/oz sur l'Or peut sembler dramatique mais n'être qu'un SigmaSpike de 1,2 si la volatilité récente est élevée, ou être un signal d'alarme de 4,0 si la volatilité récente est faible.
**TRADEX-AI C5** : Intégrer le SigmaSpike dans le dashboard TRADEX pour afficher les mouvements en "sigmas" plutôt qu'en valeur absolue — aide Abdelkrim à calibrer sa réaction émotionnelle face aux mouvements de marché.
*Catégorie : psychologie*

### D6058 — Retour comme pourcentage : définition standard finance
🔵 **ÉCOLE** (Source : how_to_calculate_sigmaspikes.md) : En finance académique, "return" signifie simplement variation en pourcentage (close_today / close_yesterday - 1). Ce n'est PAS un "rendement" ou "profit" au sens commun. L'analyse technique utilise parfois à tort "risk/reward" quand elle veut dire "reward/risk".
**TRADEX-AI C1** : Dans `claude_brain.py` et les prompts KB, utiliser systématiquement "retour journalier" = `(close_t / close_t-1) - 1`, jamais une différence absolue de prix.
*Catégorie : structure_marche*

### D6059 — Stdev 20j vs ATR 20j : équivalence pratique
🟡 **SYNTHÈSE** (Source : how_to_calculate_sigmaspikes.md) : Grimes a évolué de ATR/range moyen vers l'écart-type des retours, ces deux approches sont "légèrement différentes" mais comparables en pratique. La stdev des retours est préférable car elle s'applique à toute série temporelle (y compris données économiques sans OHLC).
**TRADEX-AI C4** : Pour les indicateurs macro C4 (DX proxy, taux Fed) qui n'ont que des données "close-only", utiliser obligatoirement stdev des retours et non ATR pour le calcul SigmaSpike.
*Catégorie : macro_evenements*

### D6060 — Application pratique : Excel / Python
🔵 **ÉCOLE** (Source : how_to_calculate_sigmaspikes.md) : Le calcul SigmaSpike est trivial à implémenter. En pseudo-Excel : col A = close, col B = `A/A[-1]-1` (returns), col C = `stdev(B, 20)` (stdev glissante), col D = `B / C[-1]` (SigmaSpike). En Python : `df['ss'] = df['ret'] / df['stdev'].shift(1)`.
**TRADEX-AI C1** : Template d'implémentation Python pour `data_reader.py` : `sigma_spike = daily_return / returns.rolling(20).std().shift(1)`. Valider avec `python -m py_compile` avant usage.
*Catégorie : indicateurs_momentum*
