# Extraction AdamGrimes — A Roadmap for the Trading Day
**Source :** `bundles/adamgrimes/a_roadmap_for_the_trading_day.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle (graphique des 6 patterns référencé mais non inclus) · 0/0 certifiées · 0 à vérifier
**Décisions :** D5071 → D5086 · **Page :** https://www.adamhgrimes.com/a-roadmap-for-the-trading-day/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Taxonomie des 6 patterns de journée intraday (ES/S&P) — fournit un cadre de contexte journalier applicable pour filtrer ou qualifier les signaux TRADEX sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Graphique des 6 patterns de journée référencé dans le texte mais non inclus dans le bundle | — | — |

## DÉCISIONS

### D5071 — Structure temporelle de la journée de trading : 3 grandes phases
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : La journée de trading se divise en 3 phases distinctes : (1) Ouverture/Matin — volatilité élevée, volume fort, mouvement de prix ; (2) Midi — volume et intérêt en baisse, pause du marché, débute souvent vers 12h00 EDT mais peut commencer plus tôt ; (3) Après-midi — reprise d'activité, souvent entre 13h30 et 14h30 EDT. Ce schéma s'applique aux indices boursiers et actions individuelles. Devises et matières premières nécessitent ajustement selon les sessions.
**TRADEX-AI C4** : Applicable directement pour qualifier le contexte temporel des signaux TRADEX. GC/CL ont leurs propres sessions (COMEX 8h20-13h30 ET pour GC) — adapter les phases. Bloc timing dans `settings.py`.
*Catégorie : timing*

### D5072 — Taxonomie des 6 patterns de journée intraday
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Grimes identifie 6 patterns récurrents de journée intraday : (1) Trend Day, (2) Range Day, (3) Trend and Reversal, (4) Trend-Range-Trend, (5) Trend qui échoue en Range, (6) Morning Range puis Trend Day. Ces patterns s'appliquent aux indices boursiers (ES/S&P) et actions. L'auteur précise que direction (hausse/baisse) n'est pas le critère discriminant — c'est la séquence trend/range qui compte.
**TRADEX-AI C1** : Cette taxonomie de 6 patterns peut structurer le contexte journalier ES comme signal de confirmation C2/C5 avant d'activer un signal TRADEX sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D5073 — Pattern Trend Day : définition et risque pour les traders contre-tendance
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Un Trend Day peut être un mouvement fort et dramatique ou un mouvement calme à pression persistante vers un extrême. Caractéristique clé : peu de retracements contre la tendance. Risque documenté : les traders qui fadent un Trend Day fort peuvent effacer plusieurs mois de profits en une seule journée.
**TRADEX-AI C1** : Règle de protection TRADEX : si le pattern journalier ES identifié est "Trend Day", ne pas aller contre la tendance dominante sur GC/HG/CL/ZW même si un signal contrarian apparaît. Le mode Auto doit bloquer les signaux à contre-tendance en Trend Day.
*Catégorie : gestion_risque_entree*

### D5074 — Pattern Range Day : tests multiples des extrêmes sans direction claire
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Un Range Day se caractérise par des tests répétés des highs ET des lows sans direction nette. Il peut contenir de bons micro-trends internes, le range peut être serré ou large, mais le facteur distinctif est les tentatives multiples et les faux breakouts aux extrêmes. Les Range Days sont les plus fréquents dans la plupart des marchés et environnements.
**TRADEX-AI C1** : Signal TRADEX en Range Day = risque accru de faux signal. Appliquer un filtre de confirmation supplémentaire (score ≥ 8,0/10 au lieu de 7,0) avant exécution en mode Auto sur GC/HG/CL/ZW identifiés en Range Day.
*Catégorie : gestion_risque_entree*

### D5075 — Pattern Trend and Reversal : risque de restitution totale des gains matinaux
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Les journées "Trend and Reversal" (trend matin suivi d'un trend inverse fort) sont rares mais représentent un risque psychologique et financier majeur. Un trader en position dans le sens du trend matin peut restituer bien plus que ses gains si le reversal est plus fort que le trend initial. Grimes qualifie ces journées de "significant risk" pour la plupart des traders.
**TRADEX-AI C1** : Règle TRADEX mode Auto : après un trend fort en première session GC/HG/CL/ZW, réduire la taille de position en session après-midi si aucun retracement normal n'a été observé. Risque de reversal extrême = réduire exposition.
*Catégorie : gestion_position_active*

### D5076 — Pattern Trend-Range-Trend : le "classic trend day" en 3 actes
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Le pattern Trend-Range-Trend est décrit par Grimes comme le "classic trend day pattern" : trend matin, consolidation midday, puis reprise du trend en après-midi. Mise en garde spécifique : ne pas shorter les breakouts de l'après-midi après un fort trend matinal. La pause midday peut donner l'impression d'un retournement qui ne vient pas.
**TRADEX-AI C1** : Règle TRADEX : en mode Trend-Range-Trend identifié sur ES, ne pas émettre de signal CONTRE la direction du trend matin lors du breakout après-midi sur GC/HG/CL/ZW. Attendre confirmation d'un vrai reversal.
*Catégorie : timing*

### D5077 — Pattern Trend qui échoue en Range : setup pour la journée suivante
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Lorsqu'un trend fort du matin se dissout en un range qui ne va nulle part (pattern "Trend that fails into a range"), cette configuration est souvent un bon setup pour la journée de trading SUIVANTE. L'énergie non libérée du trend échoué crée une tension potentielle pour le lendemain.
**TRADEX-AI C1** : Règle TRADEX inter-journée : si ES montre un "failed trend to range" aujourd'hui, augmenter la vigilance des signaux pour le lendemain sur GC/HG/CL/ZW. Contexte favorable à une reprise directionnelle.
*Catégorie : configuration*

### D5078 — Pattern Morning Range / Afternoon Trend : breakout qui surprend
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Lorsque la matinée est calme (tight range), le breakout en trend peut arriver plus tôt que prévu, avant la fenêtre normale de 13h30-14h30 EDT. Ce pattern suit souvent plusieurs jours de consolidation préalable. La surprise liée au timing peut piéger les traders qui attendent la fenêtre habituelle d'après-midi.
**TRADEX-AI C4** : Règle TRADEX : après 2-3 jours de consolidation sur GC/HG/CL/ZW + morning range serré, activer la surveillance renforcée dès 11h00 ET (pas uniquement la fenêtre 13h30-14h30 ET). Pertinent pour la détection de breakouts surprise.
*Catégorie : timing*

### D5079 — Probabilité et préparation : travailler avec le scénario "le plus probable" sans exclure les autres
🟢 **FAIT VÉRIFIÉ** (Source : a_roadmap_for_the_trading_day.md) : Grimes insiste : le roadmap journalier n'est PAS une prédiction. C'est un scénario "le plus probable" avec une conscience explicite que n'importe quoi peut arriver. La psychologie requise est "avoir un plan mais rester flexible" et "toujours répondre au message du marché en développement". Les scénarios improbables qui se réalisent sont eux-mêmes une information précieuse.
**TRADEX-AI C1** : Principe TRADEX fondamental : le mode Manuel d'Abdelkrim suit cette philosophie — le signal TRADEX propose le scénario le plus probable, mais Abdelkrim décide en intégrant le contexte temps réel. Le signal ≠ certitude.
*Catégorie : psychologie*
