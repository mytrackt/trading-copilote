# Extraction AdamGrimes — Spikes In The VIX
**Source :** `bundles/adamgrimes/spikes_in_the_vix.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image présente dans ce bundle
**Décisions :** D6711 → D6726 · **Page :** https://www.adamhgrimes.com/spikes-in-the-vix/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 313 (VIX spikes) — DIRECTEMENT pertinent pour C5 (Sentiment/VIX) : démystification du VIX comme "crash predictor", comportement post-spike, saisonnalité VIX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6711 — Le VIX n'est pas un indicateur de crash imminent
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Le VIX est une mesure du prix des options sur le S&P 500 (racine carrée de la variance forward annualisée à 30 jours), pas un prédicteur de crash. L'affirmation "VIX élevé = crash imminent" est démystifiée par les données historiques.
**TRADEX-AI C5** : Le circuit de confirmation VX (actif Catégorie 2) ne doit PAS être utilisé comme signal de crash directionnel ; un VIX élevé n'est pas un critère éliminatoire de signal à lui seul. Seul le niveau absolu de VIX (seuil critique configuré dans risk_manager.py) déclenche la suspension Auto.
*Catégorie : indicateurs_momentum*

### D6712 — Calcul VIX : de-annualisation obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Pour interpréter le VIX correctement, diviser la valeur par √12 pour obtenir la variation mensuelle attendue du S&P 500. Exemple : VIX=17.03 → 17.03/√12 = 4.92% de variation mensuelle attendue.
**TRADEX-AI C5** : Implémenter la formule de de-annualisation (VIX/√12) dans le module d'interprétation VX pour afficher la volatilité mensuelle ES attendue plutôt que la valeur brute VIX dans le dashboard TRADEX.
*Catégorie : indicateurs_momentum*

### D6713 — Saisonnalité VIX : bas en juillet, hausse vers octobre
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Sur 10 ans de données historiques, le VIX a tendance à atteindre un creux vers juillet puis à augmenter jusqu'en octobre. Ce schéma saisonnier est robuste mais sujet à distorsions.
**TRADEX-AI C5** : Intégrer ce schéma saisonnier VIX dans le module C5 : entre août et octobre, le niveau absolu de VIX sera interprété avec une tolérance plus élevée (hausse saisonnière attendue) ; entre janvier et juillet, un VIX élevé est plus anormal. Pondération saisonnière à appliquer dans le scoring /10.
*Catégorie : saisonnalite*

### D6714 — Relation VIX/S&P quotidienne : stable et prévisible
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Les variations journalières du VIX sont quasi-entièrement prédites par les variations journalières du S&P 500. La relation est si stable que les mouvements VIX au jour le jour n'apportent quasi aucune information additionnelle par rapport au mouvement du S&P.
**TRADEX-AI C5** : Ne pas analyser les mouvements journaliers du VIX de façon isolée ; leur information est redondante avec le mouvement ES. Le VX est utile comme filtre de niveau (VIX > seuil critique) et comme signal de spike exceptionnel, pas comme indicateur de direction quotidien.
*Catégorie : indicateurs_momentum*

### D6715 — Niveaux historiques VIX : bas prolongés ne précèdent pas systématiquement les crises
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Des niveaux bas de VIX peuvent durer 3 ans sans crash (exemple : boom dot com des années 90). Les niveaux bas ont précédé à la fois la crise 2007-2009 ET la hausse boursière des années 90. Aucune valeur prédictive directionnelle des bas de VIX.
**TRADEX-AI C5** : Un VIX bas n'est PAS un signal de prudence à lui seul dans le filtre C5. Le seuil critique de suspension Auto (défini dans risk_manager.py) doit cibler les niveaux ÉLEVÉS anormaux (spikes), pas les bas prolongés.
*Catégorie : indicateurs_momentum*

### D6716 — Après un grand spike VIX : sous-performance à 1 mois, sur-performance à 3-12 mois
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Sur données hebdomadaires depuis 1990 (1 283 semaines), un spike de VIX au 94e percentile (variations en points) est suivi d'une légère sous-performance des actions sur le mois suivant, mais d'une surperformance sur 3 mois, 6 mois et 12 mois. Acheter les dips après un grand spike VIX est historiquement gagnant.
**TRADEX-AI C5** : Suite à un spike VIX majeur (>94e percentile), la confirmation ES à court terme (1 mois) sera baissière mais la tendance à moyen terme (3-12 mois) sera haussière. Pour les signaux TRADEX sur GC/HG/CL/ZW, un spike VIX peut être traité comme signal de volatilité temporaire, pas comme inverseur de tendance durable.
*Catégorie : macro_evenements*

### D6717 — Spike VIX = mean reversion des actions probable
🟡 **SYNTHÈSE** (Source : spikes_in_the_vix.md) : L'auteur interprète la surperformance post-spike VIX comme un effet de mean reversion : le VIX monte quand les actions baissent, et les grands mouvements de prix tendent à se reverser. Le VIX peut simplement indiquer un spot où les actions ont baissé fort et sont candidates à une recovery.
**TRADEX-AI C5** : Un spike VIX fort combiné à une chute ES peut être utilisé comme filtre de "dip dans la tendance" pour GC et CL (corrélation négative historique Or/Dollar et pétrole/VIX à valider via C7). Ne pas sur-interpréter le VIX ; la mécanique sous-jacente est la mean reversion de l'ES.
*Catégorie : psychologie*

### D6718 — Volatility clustering : spike VIX précède d'autres pics de volatilité
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Le clustering de volatilité ("volatility clustering") est établi empiriquement : un spike de volatilité tend à être suivi d'une période de volatilité accrue. Après un premier grand spike VIX, le marché reste en état d'alerte volatilité.
**TRADEX-AI C5** : Implementer un flag "post-spike-VIX" dans le moteur TRADEX : après un spike VIX significatif, maintenir un multiplicateur de prudence sur les seuils de signal pendant N jours (à calibrer). Ce flag correspond au mécanisme de suspend_auto_mode existant dans risk_manager.py.
*Catégorie : gestion_risque_entree*

### D6719 — Variations VIX en points (différence) préférables aux variations en pourcentage
🔵 **ÉCOLE** (Source : spikes_in_the_vix.md) : Le VIX étant déjà une mesure en pourcentage, les variations en points absolus (ex : +3 points) sont analytiquement préférables aux variations en % (ex : +20%) car ces dernières induisent des distorsions quand le VIX est à des niveaux bas (ex : VIX=8, variation +1 point = +12.5%).
**TRADEX-AI C5** : Dans le calcul du seuil de spike VIX dans risk_manager.py, utiliser des variations en points absolus plutôt qu'en pourcentage pour éviter les faux positifs en période de VIX bas.
*Catégorie : indicateurs_momentum*

### D6720 — Les grands outliers post-spike VIX (2000, 2007, 2008) ne renversent pas la statistique globale
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Même en incluant les crises 2000 et 2007-2009 (qui ont produit des retours négatifs sur 12 mois post-spike VIX), la statistique globale reste favorable à l'achat post-spike sur l'horizon 3-12 mois.
**TRADEX-AI C5** : La règle post-spike VIX (prudence court terme, opportunité moyen terme) est robuste aux crises systémiques passées. Applicable comme filtre de timing dans TRADEX mais avec gestion de risque stricte sur les outliers (R/R ≥ 1:2 obligatoire).
*Catégorie : gestion_risque_entree*

### D6721 — Le VIX bas de 2017-2018 n'était pas "record absolu"
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Les niveaux bas du VIX dans la période de rédaction de l'article n'étaient pas les plus bas jamais enregistrés ; des niveaux similaires ont existé par le passé pendant plusieurs années consécutives. La narration "VIX à niveaux sans précédent" était incorrecte.
**TRADEX-AI C5** : Calibrer les seuils VIX dans risk_manager.py sur des percentiles historiques longs (20+ ans) plutôt que sur des comparaisons à des "records récents" pour éviter les biais de mémoire courte.
*Catégorie : indicateurs_momentum*

### D6722 — Un spike VIX hebdomadaire au 94e percentile : définition quantitative
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Grimes utilise les données VIX hebdomadaires depuis 1990 (1 283 semaines) pour définir un "grand spike" comme une variation au-delà du 94e percentile des variations hebdomadaires en points. Ce seuil est cohérent avec les mesures mensuelles.
**TRADEX-AI C5** : Pour le risk_manager.py, définir le seuil de spike VIX "majeur" comme une variation hebdomadaire en points > percentile 94 calculé sur les 1 300 dernières semaines. Ce seuil est distinct du seuil "critique" de suspension Auto (lequel cible le niveau absolu de VIX, pas la variation).
*Catégorie : gestion_risque_entree*

### D6723 — Fausse popularité de l'hyperbole VIX dans les médias financiers
🔵 **ÉCOLE** (Source : spikes_in_the_vix.md) : L'auteur note que l'hyperbole médiatique autour du VIX (peur, crash imminent, etc.) est systématiquement non justifiée par les données historiques. La compréhension technique exacte du VIX est rare même chez les professionnels.
**TRADEX-AI C5** : Dans les prompts du cerveau Claude (claude_brain.py), le VIX doit être référencé avec sa définition exacte (prix des options S&P 30 jours, de-annualisé par √12) pour éviter les biais de langage dans les analyses IA.
*Catégorie : psychologie*

### D6724 — Relation VIX/S&P visible sur graphique de dispersion
🟢 **FAIT VÉRIFIÉ** (Source : spikes_in_the_vix.md) : Un graphique de dispersion (S&P return en écarts-types sur 20 jours vs variation VIX en %) montre que la quasi-totalité des points se concentrent dans un corridor prévisible. Les outliers sont rares et extrêmes.
**TRADEX-AI C5** : La corrélation inverse ES/VX est suffisamment stable pour être utilisée comme validation interne : si le VX monte fortement ET l'ES monte aussi (décorrélation), cela signale une anomalie de marché méritant une suspension des signaux Auto sur TRADEX.
*Catégorie : correlations*

### D6725 — Saisonnalité VIX : "distorsion possible" — à utiliser avec prudence
🟡 **SYNTHÈSE** (Source : spikes_in_the_vix.md) : L'auteur qualifie la saisonnalité VIX de "squirrely" (capricieuse), indiquant qu'elle représente au mieux une légère influence sujette à des distorsions sévères. Elle ne doit pas être utilisée comme signal fort.
**TRADEX-AI C5** : La saisonnalité VIX (D6713) est un filtre secondaire de contexte, pas un déclencheur de signal. Dans le scoring /10 TRADEX, lui attribuer un poids faible (0.5 point maximum) dans le cercle C5.
*Catégorie : saisonnalite*

### D6726 — Conclusion : le VIX comme outil de localisation des dips, pas de direction
🟡 **SYNTHÈSE** (Source : spikes_in_the_vix.md) : La conclusion synthétique d'Adam Grimes est que le VIX est utile principalement pour identifier les moments où les actions ont beaucoup baissé (dips) et pourraient rebondir (mean reversion), pas pour prédire la direction future du marché.
**TRADEX-AI C5** : Dans TRADEX, VX (VIX) remplit la fonction de "filtre de stress de marché" : un VIX anormalement élevé identifie une fenêtre de potentielle mean reversion ES, utile pour filtrer les signaux contre-tendance sur GC (refuge) et pour valider les signaux directionnels sur CL (volatilité économique).
*Catégorie : macro_evenements*
