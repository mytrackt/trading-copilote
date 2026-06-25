# Extraction AdamGrimes — Understanding Returns
**Source :** `bundles/adamgrimes/understanding_returns.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7251 → D7262 · **Page :** https://www.adamhgrimes.com/understanding-returns/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Mathématiques des rendements composés — fondamental pour évaluer drawdowns et volatilité du compte de trading.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7251 — Définition : un retour = un pourcentage de variation
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : En finance et analyse technique, un "return" (retour/rendement) est un pourcentage de variation. Le retour brut = retour net + 1,0. Exemple : +10% net → 1,10 brut.
**TRADEX-AI C4** : Toute mesure de performance du système TRADEX doit distinguer retour net et retour brut ; les rapports de backtest doivent afficher les deux.
*Catégorie : gestion_risque_entree*

### D7252 — Règle : on ne peut pas additionner les retours simples
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : On ne peut PAS additionner des rendements en pourcentage. Démonstration : -50% puis +50% → (1 - 0,50) × (1 + 0,50) = 0,75 → perte nette de -25%, pas retour à zéro.
**TRADEX-AI C4** : La grille de score /10 de TRADEX ne doit jamais additionner des P&L en % bruts ; le calcul de performance cumulée doit multiplier les retours bruts.
*Catégorie : gestion_risque_entree*

### D7253 — Formule : retour total = produit des retours bruts
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Retour brut total = Retour brut période 1 × Retour brut période 2 × … Cette formule se généralise à n'importe quel nombre de périodes.
**TRADEX-AI C4** : Le module de reporting TRADEX doit implémenter cette multiplication pour tout calcul de performance multi-trades.
*Catégorie : gestion_risque_entree*

### D7254 — Formule : capitalisation sur N périodes
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Retour net composé = ((1 + retour net) ^ N périodes) − 1. Exemple : 2% par jour pendant 5 jours → ((1,02)^5) − 1 = 10,408%.
**TRADEX-AI C4** : Le backtesting de TRADEX doit utiliser cette formule pour projeter les performances sur des horizons multi-jours, et non une simple multiplication linéaire.
*Catégorie : gestion_risque_entree*

### D7255 — Règle d'annualisation des retours
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Pour annualiser un retour journalier : ^ 252 (252 jours de trading/an). Pour un retour hebdomadaire : ^ 52. Pour un retour mensuel : ^ 12. Exemple : 1%/jour → 1127,4%/an ; 1%/semaine → 67,8%/an ; 1%/mois → 12,7%/an.
**TRADEX-AI C4** : Si TRADEX affiche un taux de gain annualisé, appliquer ces facteurs exacts selon la granularité des données NT8 utilisées.
*Catégorie : gestion_risque_entree*

### D7256 — Alerte : les drawdowns sont asymétriques et plus dangereux qu'ils n'y paraissent
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Un drawdown de -50% nécessite un gain de +100% pour revenir au breakeven (et non +50%). Cette asymétrie mathématique rend les pertes exponentiellement plus coûteuses que les gains équivalents.
**TRADEX-AI C1/C5** : Le risk_manager.py de TRADEX doit calibrer les seuils de suspension du mode Auto en tenant compte de cette asymétrie — une perte de 20% exige +25% pour récupérer, pas +20%.
*Catégorie : gestion_risque_entree*

### D7257 — Méthode : test TLAR (Too Large A Return) comme premier filtre
🟡 **SYNTHÈSE** (Source : understanding_returns.md) : Avant toute analyse statistique d'un pattern de marché, appliquer le test TLAR : "ce retour est-il trop beau pour être vrai ?" Un retour sur 20 jours qui semble anormalement élevé doit déclencher un examen de stabilité du pattern.
**TRADEX-AI C4** : Tout signal TRADEX avec un R/R affiché > 5:1 doit être marqué "TLAR_WARNING" et soumis à validation humaine avant exécution en mode Auto.
*Catégorie : configuration*

### D7258 — Concept : stabilité temporelle d'un pattern de marché
🟡 **SYNTHÈSE** (Source : understanding_returns.md) : La question clé n'est pas seulement "ce pattern marche-t-il ?" mais "ce pattern reste-t-il stable dans le temps ?" Un pattern peut fonctionner sur une période passée et devenir inexploitable par la suite.
**TRADEX-AI C4** : La KB de TRADEX doit inclure pour chaque règle Belkhayate une métadonnée de "stabilité_temporelle" (confirmée sur plusieurs périodes vs observée une seule fois).
*Catégorie : configuration*

### D7259 — Erreur commune : confondre retour net et retour brut dans les publications
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Même des analystes certifiés (CMT) commettent des erreurs sur la distinction retour net / retour brut, notamment en croyant qu'un gain de +10% après une perte de -10% ramène au breakeven. Cette confusion est répandue dans les forums et publications.
**TRADEX-AI C4** : Le dashboard TRADEX doit afficher TOUJOURS les deux métriques (net et brut) avec des libellés clairs pour éviter cette confusion chez Abdelkrim.
*Catégorie : psychologie*

### D7260 — Règle : comprendre les mathématiques de base est critique pour évaluer la volatilité
🟡 **SYNTHÈSE** (Source : understanding_returns.md) : La maîtrise des mathématiques de rendement (compounding, annualisation) permet d'identifier des erreurs dans les analyses publiées et de développer un respect approprié pour les drawdowns et la volatilité.
**TRADEX-AI C5** : Le mode éducatif du dashboard TRADEX doit inclure une section "Mathématiques de base" expliquant ces concepts à Abdelkrim avec des exemples concrets sur GC/HG/CL/ZW.
*Catégorie : psychologie*

### D7261 — Alerte : la volatilité amplifie l'asymétrie des pertes/gains
🟡 **SYNTHÈSE** (Source : understanding_returns.md) : La compréhension du compounding montre que la volatilité (fluctuations autour d'un retour moyen) réduit systématiquement la performance réelle par rapport au retour moyen arithmétique. Plus la volatilité est élevée, plus la performance réelle est inférieure à la moyenne.
**TRADEX-AI C5** : Le staleness_monitor.py doit signaler non seulement les données périmées mais aussi les périodes de volatilité anormale susceptibles de fausser les calculs de performance.
*Catégorie : gestion_position_active*

### D7262 — Principe fondamental : ne pas ignorer les coûts de transaction dans les retours
🟢 **FAIT VÉRIFIÉ** (Source : understanding_returns.md) : Les retours mentionnés dans l'exemple de la question initiale sont des retours "all-in, including transaction costs" (net de frais). Les coûts de transaction doivent être intégrés dans tout calcul de performance réelle.
**TRADEX-AI C4** : TRADEX doit intégrer les frais de commission NT8/Rithmic dans tous les calculs de P&L affichés — jamais de P&L brut sans déduction des frais.
*Catégorie : gestion_risque_entree*
