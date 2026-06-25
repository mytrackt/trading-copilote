# Extraction AdamGrimes — Trailing Stops 9 Ideas You Can Use Today
**Source :** `bundles/adamgrimes/trailing_stops_9_ideas_you_can_use_today.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7131 → D7145 · **Page :** https://www.adamhgrimes.com/trailing-stops-9-ideas-you-can-use-today/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Gestion de position active directement applicable sur GC/CL/HG/ZW — trailing stops après entrée signal Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

---

## DÉCISIONS

### D7131 — Gestion de trade au moins aussi importante que l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : La gestion de trade (trade management) est au moins aussi importante que l'entrée, probablement davantage. Les deux outils principaux sont les profit targets et les stops. Avant de trader, avoir une réponse solide à chaque question de gestion : placement initial, déplacement, annulation, sortie partielle, time stop.
**TRADEX-AI C1** : Le plan de gestion de chaque signal TRADEX doit définir avant exécution : stop initial, niveau de trailing, target partielle à 1R — applicable Mode Manuel (affichage) et Mode Auto (exécution).
*Catégorie : gestion_position_active*

### D7132 — Trailing stop : réduire le risque ouvert quand le trade progresse
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Règle générale : quand le trade évolue favorablement, déplacer le stop pour réduire le risque ouvert dans la trade. C'est le principe fondamental du trailing stop — protéger progressivement les gains latents.
**TRADEX-AI C1** : En Mode Auto sur GC/CL/HG/ZW, dès que le profit atteint 0,5R, déplacer le stop vers breakeven. Dès 1R atteint, stop au-delà du dernier pivot bas (long) ou haut (short).
*Catégorie : gestion_position_active*

### D7133 — Time stop alternatif : déplacer le stop si pas de mouvement
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Si le trade ne bouge pas et stagne autour du point d'entrée, déplacer quand même le stop progressivement. Cette tactique sert d'alternative au time stop classique (sortir après N barres sans profit). Le résultat probable est le stop-out, ce qui est l'objectif : libérer le capital d'un trade inactif.
**TRADEX-AI C1** : En Mode Auto, activer un time stop implicite : si aucun mouvement de ±0,3R après N barres définies dans settings.py, resserrer le stop progressivement vers l'entrée.
*Catégorie : gestion_position_active*

### D7134 — Structure de marché : pivots hauts/bas pour localiser les stops
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Utiliser la structure de marché — spécifiquement les pivots hauts et bas précédents — pour positionner les trailing stops. Cette approche est la plus alignée avec la lecture technique car elle reflète les niveaux de décision réels du marché.
**TRADEX-AI C1** : Sur NT8, les pivots Belkhayate (hauts/bas de swings identifiés par NT8 indicator) constituent les niveaux naturels pour les trailing stops sur GC/CL/HG/ZW.
*Catégorie : gestion_position_active*

### D7135 — Stop à l'intérieur vs l'extérieur des pivots : question de philosophie
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Choix délibéré entre placer le stop à l'intérieur, au niveau, ou juste au-delà des supports/résistances pivot. La majorité des traders choisit l'extérieur pour éviter d'être stoppés sur des trades encore valides. Mais aucune règle universelle — le choix impacte le taux de stop-out et la taille du recul autorisé.
**TRADEX-AI C1** : Règle TRADEX par défaut : stop 1 tick au-delà du pivot (extérieur). Option à exposer dans le dashboard pour paramétrage manuel par Abdelkrim.
*Catégorie : gestion_risque_entree*

### D7136 — Trailing N-day lowest low / highest high : uniquement en trend fort
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Tracer le stop au plus bas des N derniers jours (long) ou plus haut des N derniers jours (short) est une approche valide — mais uniquement dans un marché en tendance forte. Cette méthode échoue dans les marchés en range ou tendance faible.
**TRADEX-AI C1** : Applicable sur GC en super-tendance (trend Belkhayate confirmé + DX aligné). Valeur N à définir selon timeframe de trading — exclure cette méthode si score tendance < 7,0.
*Catégorie : gestion_position_active*

### D7137 — Barre forte dans le sens du trade : serrer le stop dans le range de la barre suivante
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Après un mouvement exceptionnel sur une seule barre dans le sens du trade (windfall), déplacer le stop dans le range de cette barre sur la barre suivante. Cette approche est généralement trop serrée mais l'objectif est de protéger le maximum du gain exceptionnel.
**TRADEX-AI C1** : Sur GC/CL lors de barres impulsives post-signal (gap overnight, réaction NFP), resserrer le stop dans le range de la barre impulsive le lendemain.
*Catégorie : gestion_position_active*

### D7138 — Parabolic SAR et Chandelier Stops : outils de trailing à comprendre avant usage
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Parabolic SAR et Chandelier Stops sont des indicateurs conçus pour servir de trailing stops. Ils peuvent être utilisés mais nécessitent une compréhension des nuances de chaque outil avant intégration dans un système.
**TRADEX-AI C1** : Ces indicateurs sont disponibles dans NT8. Utilisation possible mais uniquement après validation quantitative sur GC/HG/CL/ZW — ne pas intégrer par défaut sans backtest.
*Catégorie : indicateurs_tendance*

### D7139 — Canaux de Donchian (N-day high/low) comme stops structurels
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Le plus haut/plus bas des N derniers jours (canaux Donchian) constitue une approche de stop basée sur la structure du marché. La valeur de N doit être calibrée selon le type d'entrée et la durée de détention prévue.
**TRADEX-AI C1** : Pour les trades de swing (multi-sessions) sur GC/CL, un Donchian 5-10 jours peut servir de stop structurel complémentaire aux pivots Belkhayate.
*Catégorie : gestion_position_active*

### D7140 — Moyenne mobile comme stop : simple mais non validé quantitativement
🟢 **FAIT VÉRIFIÉ** (Source : trailing_stops_9_ideas_you_can_use_today.md) : Utiliser une moyenne mobile comme trailing stop est une option simple et claire. Cependant, Grimes note que les MM ne testent pas bien dans les analyses quantitatives pour cet usage. Avoir un plan clair — même imparfait — est supérieur à n'avoir aucun plan.
**TRADEX-AI C1** : Les MM ne sont pas le premier choix pour les trailing stops TRADEX. Utiliser en dernier recours si aucun pivot structurel n'est disponible sur GC/HG/CL/ZW.
*Catégorie : gestion_position_active*

### D7141 — Avoir un plan de gestion défini avant le trade
🟡 **SYNTHÈSE** (Source : trailing_stops_9_ideas_you_can_use_today.md) : L'ensemble des 9 idées converge vers un principe : avoir un plan de gestion complet avant de trader est indispensable. Le type de plan (stop structure, N-day, MM, indicator) importe moins que d'en avoir un et de le respecter.
**TRADEX-AI C1** : Le signal TRADEX doit systématiquement inclure dans sa réponse API : stop initial, niveau trailing cible, target 1R — avant tout affichage en Mode Manuel ou exécution en Mode Auto.
*Catégorie : gestion_position_active*
