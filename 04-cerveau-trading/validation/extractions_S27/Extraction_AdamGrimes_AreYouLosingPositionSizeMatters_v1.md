# Extraction AdamGrimes — Are You Losing Position Size Matters
**Source :** `bundles/adamgrimes/are_you_losing_position_size_matters.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5151 → D5165 · **Page :** https://www.adamhgrimes.com/are-you-losing-position-size-matters/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Position sizing quantitatif — règles de risque par trade directement applicables au risk_manager.py pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5151 — Le sizing de position est le facteur le plus négligé et le plus critique
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : La plupart des traders se concentrent sur les entrées/sorties et la discipline, mais négligent la taille des positions. Le sizing est le facteur qui peut transformer des gagnants en perdants. Trop petit = P&L insuffisant. Trop grand = risque de ruine.
**TRADEX-AI C1** : Le risk_manager.py est un composant critique non optionnel. Chaque signal TRADEX doit inclure la taille de position calculée, pas seulement la direction. Mode Manuel : afficher la taille recommandée à Abdelkrim.
*Catégorie : gestion_risque_entree*

### D5152 — Système à espérance positive peut produire des ruines avec un trop grand risque par trade
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Simulation documentée — système à espérance positive (+0.1, 50% de réussite, gains 1,2× les pertes) : à $8 000 de risque par trade (8% de $100k), 11% des comptes font faillite sur 250 trades. À $25 000 de risque (25%), près de 50% font faillite. Un système gagnant peut ruiner un compte si le sizing est trop élevé.
**TRADEX-AI C1** : Le risk_manager.py doit imposer un plafond dur de risque par trade. Même si le signal a un score /10 élevé, le risque en % d'équité ne peut pas dépasser le maximum défini dans settings.py. Ce plafond est non contournable, même en mode Auto.
*Catégorie : gestion_risque_entree*

### D5153 — Plus le risque par trade est élevé, plus les résultats sont variables et extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Sur la même séquence de trades d'un système à espérance positive, augmenter le risque par trade augmente la moyenne des gains, mais augmente exponentiellement la variance et la probabilité de ruine. Le risque élevé ne compense pas statistiquement.
**TRADEX-AI C1** : La variabilité des résultats est une raison supplémentaire de maintenir un risque par trade stable. En mode Auto, le risk_manager.py doit utiliser un risque fixe en pourcentage (pas un montant fixe en dollars) pour que le système soit robuste quelle que soit la taille du compte.
*Catégorie : gestion_risque_entree*

### D5154 — Risque fixe en pourcentage (fixed fractional) préférable au montant fixe en dollars
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Risquer un montant fixe en dollars est acceptable mais sous-optimal. Risquer un pourcentage fixe de l'équité (fixed fractional) est meilleur : quand le compte grossit, les positions grossissent proportionnellement et tout s'adapte automatiquement.
**TRADEX-AI C1** : Le risk_manager.py doit implémenter le risque en % d'équité (fixed fractional), pas en montant absolu. La taille de position est recalculée à chaque trade sur la base de l'équité courante du compte, lue depuis l'API NT8.
*Catégorie : gestion_risque_entree*

### D5155 — Zone de risque par trade recommandée : 1% à 4% de l'équité
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Fourchette recommandée par Grimes : risquer entre 1% et 4% de l'équité par trade. La valeur exacte dépend de la psychologie du trader, des objectifs de trading, et des caractéristiques de la méthode. C'est une règle empirique validée.
**TRADEX-AI C1** : settings.py doit définir RISK_PER_TRADE_PCT avec une valeur par défaut de 1.0% (conservateur pour démarrage) et un maximum configurable de 4.0%. Toute valeur > 4.0% doit être rejetée par le risk_manager.py avec un avertissement explicite.
*Catégorie : gestion_risque_entree*

### D5156 — Le Kelly Criterion et l'optimal f peuvent produire des drawdowns inacceptables
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Les approches optimisées de sizing (Kelly Criterion de Kelly, optimal f de Ralph Vince) peuvent être très agressives et produire des drawdowns inacceptables pour la plupart des investisseurs, malgré leur optimalité mathématique à long terme.
**TRADEX-AI C1** : TRADEX-AI n'utilisera PAS le Kelly Criterion ni l'optimal f. Le fixed fractional conservateur (1%-4%) est le choix retenu, conformément à la recommandation Grimes et à la priorité de préservation du capital Belkhayate.
*Catégorie : gestion_risque_entree*

### D5157 — Trader trop petit rend le trading non rentable malgré une méthode correcte
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Un sizing trop conservateur (risque trop faible par trade) produit des gains insuffisants pour justifier le temps et l'effort consacrés au trading, même avec une méthode correcte et disciplinée.
**TRADEX-AI C5** : Le dashboard doit afficher un indicateur de sizing : si RISK_PER_TRADE_PCT < 0.5%, afficher un avertissement "Position trop petite — gains potentiels insuffisants pour le temps investi."
*Catégorie : gestion_risque_entree*

### D5158 — Les traders sous-estiment la variabilité des résultats sur un système gagnant
🟢 **FAIT VÉRIFIÉ** (Source : are_you_losing_position_size_matters.md) : Simulation documentée : sur 50 traders aléatoires utilisant le même système à espérance positive sur 250 trades, un trader a perdu de l'argent et plusieurs ont eu des difficultés significatives. La variabilité réelle est beaucoup plus grande qu'attendu intuitvement.
**TRADEX-AI C5** : En mode Manuel, lors des périodes de perte consécutives (3 pertes d'affilée), afficher : "Variance normale sur système positif — Ne pas modifier la méthode, ne pas augmenter la taille."
*Catégorie : psychologie*

### D5159 — Focus sur le risque d'abord, pas sur le gain potentiel
🔵 **ÉCOLE** (Source : are_you_losing_position_size_matters.md) : Les traders axés sur le gain potentiel (espoir du home run) avec trop de risque transforment leur compte en billet de loterie. Les traders professionnels se concentrent d'abord sur le risque, le gèrent, et maintiennent un sizing cohérent.
**TRADEX-AI C5** : L'interface TRADEX doit afficher le risque en premier (montant à risque en $, % du compte) AVANT le gain potentiel. Ordre d'affichage : Risque → Stop → R/R → Cible. Jamais la cible en premier.
*Catégorie : psychologie*
