# Extraction AdamGrimes — Does the 200 Day Moving Average "Work"?
**Source :** `bundles/adamgrimes/200_day_moving_average_work.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5011 → D5022 · **Page :** https://www.adamhgrimes.com/200-day-moving-average-work/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Remet en cause les filtres de tendance MA200 couramment utilisés sur GC/HG/CL/ZW/ES — justifie l'utilisation d'outils alternatifs (Belkhayate COG, GER) plutôt que des moyennes mobiles classiques.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D5011 — Absence d'effet statistiquement significatif de la MA200 sur le S&P 500
🟢 **FAIT VÉRIFIÉ** (Source : 200_day_moving_average_work.md) : Le S&P 500 au-dessus de la MA200 produit un rendement annualisé de 11,0% vs 2,1% en dessous, soit un écart de 8,9 pts, mais cet effet n'est PAS statistiquement significatif selon les tests de significativité appliqués par Grimes. L'effet s'évanouit quasi totalement sur la dernière décennie de données.
**TRADEX-AI C1** : Ne pas utiliser la MA200 comme filtre de tendance pour GC/HG/CL/ZW. Les pivots Belkhayate et le COG sont des outils de tendance plus robustes empiriquement.
*Catégorie : indicateurs_tendance*

### D5012 — Aucune moyenne mobile n'est "spéciale" — toutes sont équivalentes
🟢 **FAIT VÉRIFIÉ** (Source : 200_day_moving_average_work.md) : Les travaux quantitatifs de Grimes montrent qu'il n'existe aucune moyenne mobile "spéciale" : la MA200 n'est pas statistiquement différente de la MA193 ou MA204. Les croisements, pentes et touches de moyennes mobiles (50, 100, 200) n'ont aucun pouvoir prédictif sur la direction future du marché.
**TRADEX-AI C1** : Valide le rejet des moyennes mobiles classiques dans le moteur TRADEX. Le cerveau Claude ne doit PAS intégrer de signal basé sur des croisements MA200 pour GC/HG/CL/ZW/ES.
*Catégorie : indicateurs_tendance*

### D5013 — Dégradation progressive de l'efficacité des systèmes MA depuis les années 1990
🟢 **FAIT VÉRIFIÉ** (Source : 200_day_moving_average_work.md) : La réplication du test Brock-Lakonishok-LeBaron (croisement MA50) montre une courbe des profits régulière pendant les décennies 1926-1990 (Grande Dépression, WWII, récessions), puis une dégradation nette sur la période post-1990. Les systèmes de croisement MA qui "fonctionnaient" historiquement ont perdu leur efficacité dans l'ère moderne.
**TRADEX-AI C1** : Renforce la décision de baser TRADEX sur des indicateurs propriétaires Belkhayate (COG, Timing, Énergie) plutôt que sur des systèmes MA classiques. Stationnarité des signaux = critère d'évaluation obligatoire.
*Catégorie : indicateurs_tendance*

### D5014 — Erreur statistique fréquente : comptage du jour de croisement dans la mauvaise catégorie
🟡 **SYNTHÈSE** (Source : 200_day_moving_average_work.md) : Grimes identifie une erreur méthodologique courante dans les études sur MA : comptabiliser le jour du croisement (qui est presque toujours haussier pour le passage au-dessus et baissier pour le passage en dessous) dans la catégorie "après croisement" fausse massivement les statistiques. Des chiffres comme "S&P +23,5% au-dessus et -19,5% en dessous" sont des artefacts de cette erreur.
**TRADEX-AI C1** : Règle méthodologique pour les backtests TRADEX : exclure le jour du signal du calcul de performance. Appliquer à tout backtest COG/Timing.
*Catégorie : gestion_risque_entree*

### D5015 — Pente d'une moyenne mobile : indicateur de tendance non fiable
🟢 **FAIT VÉRIFIÉ** (Source : 200_day_moving_average_work.md) : La pente d'une moyenne mobile (croissante vs décroissante) n'est PAS un indicateur fiable de la tendance du marché selon les tests quantitatifs de Grimes. Même conclusion pour les indicateurs dérivés des moyennes mobiles (MACD, etc.).
**TRADEX-AI C1** : Ne pas utiliser la pente de MA comme proxy de tendance dans le moteur TRADEX. Utiliser Direction Belkhayate (NT8) comme indicateur de tendance pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D5016 — DJIA : données 1925-présent confirment l'absence d'effet MA200 statistiquement solide
🟢 **FAIT VÉRIFIÉ** (Source : 200_day_moving_average_work.md) : Sur le DJIA depuis 1925, le rendement au-dessus de la MA200 est de 4,1% (p=0.16, non significatif) et -7,7% en dessous (p=0.13, non significatif). Les deux p-values sont supérieures au seuil de 0,05 : l'effet n'est pas statistiquement démontré.
**TRADEX-AI C4** : Sur les actifs de confirmation ES/DX, ne pas intégrer la position relative à la MA200 comme signal macro. Les niveaux de support/résistance Belkhayate sont à privilégier.
*Catégorie : indicateurs_tendance*
