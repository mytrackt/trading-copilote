# Extraction AdamGrimes — When Percents Fail
**Source :** `bundles/adamgrimes/when_percents_fail.md` (HTTP 200) + 0 images certifiées
**Méthode images :** pas d'images dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7511 → D7525 · **Page :** https://www.adamhgrimes.com/when-percents-fail/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 353 — la supériorité des mesures volatilité-ajustées (ATR/sigma) sur les seuils en pourcentage est DIRECTEMENT applicable à la détection de grands mouvements sur GC/HG/CL/ZW dont la volatilité varie énormément selon les régimes de marché.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

---

## DÉCISIONS

### D7511 — Question fondamentale du backtesting : "Que se passe-t-il après X ?"
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Quand on teste quelque chose dans le marché, on cherche une réponse à 'Que se passe-t-il après _____ se produit ?' C'est l'essence de tout backtesting et développement de système, du chartreading casual au machine learning."
**TRADEX-AI C1** : Chaque règle de la KB Belkhayate doit être formulée sous la forme "Après [condition], l'action recommandée est [X]" — c'est la structure de base d'une décision valide dans KNOWLEDGE_BASE_MASTER.json.
*Catégorie : structure_marche*

### D7512 — Prix brut comme mesure : inutile en multi-marchés
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Le prix brut est évident et intuitif, et aussi quasi inutile sauf sur une tranche très étroite de données sur un seul marché. Un mouvement de $10 sur une action à $500 et un mouvement de $1,23 sur une devise auront évidemment des significations très différentes."
**TRADEX-AI C1/C7** : Dans le moteur de corrélations (correlations.py), les comparaisons inter-marchés entre GC, HG, CL et ZW ne doivent JAMAIS utiliser des variations en valeur absolue (dollars/points). Utiliser uniquement des variations normalisées (% ou sigma).
*Catégorie : correlations*

### D7513 — Mesures en pourcentage : supérieures au prix brut mais biaisées par les régimes de volatilité
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Les pourcentages sont meilleurs, mais le problème est que la volatilité change dans un marché. Il y aura des périodes où les mouvements de 2% sont très communs, puis peut-être des années sans un seul mouvement de 2%."
**TRADEX-AI C1** : Les seuils de détection de grands mouvements dans le moteur TRADEX ne doivent pas être fixes en pourcentage. Un seuil adaptatif basé sur la volatilité récente (ATR rolling 14 périodes) est obligatoire pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D7514 — Mesures volatilité-ajustées (ATR/sigma) : supérieures pour la généralisation
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Dans la plupart des cas, je trouve les mesures ajustées à la volatilité supérieures. Elles ajustent exactement pour le niveau courant de volatilité du marché. Deux façons simples : ATR (commun en analyse technique) ou une mesure qui considère les mouvements moyens close-to-close. Les Sigma Spikes ont été très utiles dans une grande partie de mon travail."
**TRADEX-AI C1/C5** : Pour détecter les mouvements anormaux sur GC/HG/CL/ZW (potentiellement liés à news ou manipulation), utiliser un seuil en multiple d'ATR (ex : mouvement > 2 ATR en 1 barre = anomalie) plutôt qu'un seuil en pourcentage.
*Catégorie : indicateurs_momentum*

### D7515 — Distribution homogène des signaux : avantage clé des mesures sigma
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "L'un des bénéfices d'une mesure volatilité-ajustée est que les signaux seront distribués beaucoup plus uniformément sur la timeline. [Avec des pourcentages], il y a de grandes périodes sans signaux — parfois une année complète. Avec les sigma spikes, les mouvements sont assez uniformément distribués."
**TRADEX-AI C5** : Le VX (VIX) utilisé comme filtre Cercle 5 doit être interprété en termes relatifs (sigma du VIX par rapport à sa moyenne 30j) et non en valeur absolue. Un VIX à 18 en régime de basse volatilité est plus significatif qu'un VIX à 18 en régime de haute volatilité.
*Catégorie : indicateurs_momentum*

### D7516 — Lookback bias : exclure les données futures des seuils historiques
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Faites attention au lookback. Par exemple, si l'on prend l'ensemble des plus grands mouvements en pourcentage sur les 20 dernières années, cela inclut des informations qui n'auraient pas été disponibles au moment du trade."
**TRADEX-AI C1** : Les paramètres ATR et sigma du moteur TRADEX doivent être calculés uniquement sur des données passées disponibles à l'instant T. Interdiction d'utiliser des moyennes calculées sur une fenêtre qui inclut des données futures (look-ahead bias).
*Catégorie : gestion_risque_entree*

### D7517 — Sigma spikes : détection de signaux d'alerte non évidents sur le chart
🟡 **SYNTHÈSE** (Source : when_percents_fail.md) : "Le 4/10/2018 sur le S&P 500 était un spike de -2,4 sigma, le plus grand déclin ajusté à la volatilité depuis mars 2018. Vous l'auriez vu sur le chart ? Peut-être ou peut-être pas. Il a donné un avertissement de ce qui est arrivé quelques jours plus tard."
**TRADEX-AI C1/C5** : Un module de détection sigma pourrait alerter sur GC/CL avant les grands mouvements directionnels — un spike de volatilité anormale sur ces actifs précède souvent les cassures de range et est capturé par l'analyse Belkhayate (Énergie).
*Catégorie : indicateurs_momentum*

### D7518 — Comprendre les compromis de chaque mesure avant de l'utiliser
🟢 **FAIT VÉRIFIÉ** (Source : when_percents_fail.md) : "Comme pour toute mesure, comprendre les compromis, ce que le mouvement mesure, et où sont ses forces et faiblesses."
**TRADEX-AI C1** : La documentation de chaque indicateur dans settings.py doit mentionner explicitement ses limites (ex : "ATR 14 périodes — lissé, réagit avec retard aux chocs de volatilité — préférer ATR 5 pour signaux court terme").
*Catégorie : indicateurs_tendance*
