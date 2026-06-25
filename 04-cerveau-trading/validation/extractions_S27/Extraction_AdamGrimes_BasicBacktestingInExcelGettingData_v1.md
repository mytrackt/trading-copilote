# Extraction AdamGrimes — Basic Backtesting in Excel: Getting Data
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_getting_data.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5211 → D5225 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-getting-data/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Qualité des données de marché comme prérequis absolu pour tout backtest — directement applicable au pipeline de données NT8/ATAS de TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5211 — La qualité des données conditionne la valeur de tout backtest
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_getting_data.md) : Sans données de qualité, toute analyse est probablement une perte de temps. La décision sur la source et la qualité des données est la plus importante à prendre avant tout travail quantitatif. « If you don't have good data, everything else you do is likely to be a waste of time. »
**TRADEX-AI C1** : Le staleness_monitor.py est le gardien de la qualité des données en temps réel. Si les données NT8/ATAS dépassent leur seuil de fraîcheur, le système passe en BLOCKED — aucun signal ne peut être généré sur données périmées. Cette règle est non négociable.
*Catégorie : volume_liquidite*

### D5212 — Données statiques vs données dynamiques : le choix initial
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_getting_data.md) : Pour débuter, les données historiques statiques sont suffisantes. La mise à jour automatique des données est nécessaire à terme mais complexe à mettre en place. La priorité initiale est de maîtriser les mécaniques d'analyse, pas l'infrastructure de mise à jour.
**TRADEX-AI C1** : Le dossier `data\` (Phase C) devra être créé pour accueillir les collecteurs NT8/ATAS. Selon la dette technique (dette #3), ce dossier n'existe pas encore. Les analyses de développement peuvent s'appuyer sur des JSONs statiques en attendant la Phase C.
*Catégorie : configuration*

### D5213 — Limitation Excel pour les données intraday (tick data)
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_getting_data.md) : Excel est limité à environ 1 million de points de données. 1 an de données 1-minute pour une session New York = ~98 280 barres. Excel devient très lent et instable avec de grands datasets. Les données tick sont encore plus volumineuses.
**TRADEX-AI C1** : Le moteur TRADEX-AI utilise des range bars NT8 (pas des barres 1-minute). Les range bars réduisent considérablement le volume de données tout en préservant les structures de prix importantes. Ce choix architectural est cohérent avec les limites de traitement temps réel.
*Catégorie : configuration*

### D5214 — Ajustement en arrière des contrats futures : une question critique
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_getting_data.md) : Pour les futures (GC, CL, HG, ZW), l'ajustement en arrière (back-adjustment) des données à la rotation de contrat est une décision méthodologique majeure avec plusieurs approches valides. Ce problème est souvent ignoré par les traders qui utilisent des données non ajustées — source d'erreurs de backtest importantes.
**TRADEX-AI C1** : Les données NT8 pour GC, HG, CL, ZW doivent utiliser des symboles de continuation (ex : GC 09-26) avec une méthode d'ajustement définie (généralement Panama ou ratio). Cette décision doit être documentée dans settings.py avant la Phase C. Une erreur ici invalide tous les backtests historiques.
*Catégorie : configuration*

### D5215 — Actions corporatives et ajustement des données actions
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_getting_data.md) : Pour les actions, les splits, dividendes, et autres événements corporatifs modifient les prix historiques et doivent être ajustés pour des comparaisons valides. ES (S&P 500 futures) comme actif de confirmation dans TRADEX-AI n'est pas affecté par ce problème, mais le principe reste valide pour tout actif.
**TRADEX-AI C2** : Les données ATAS (order flow) pour ES/VX utilisées comme actifs de confirmation ne nécessitent pas d'ajustement historique car ce sont des données de flux en temps réel. Seules les données de prix historiques pour backtest sont concernées.
*Catégorie : configuration*

### D5216 — Les données fondamentales sont souvent révisées
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_getting_data.md) : Les données économiques et fondamentales (GDP, emploi, COT…) sont régulièrement révisées après leur première publication. Backtester sur des données révisées (point-in-time problem) donne des résultats optimistes qui ne peuvent pas être répliqués en trading réel.
**TRADEX-AI C3** : Les données COT (CFTC hebdomadaire) pour le Cercle C3 (Institutionnels) doivent utiliser les données au moment de publication (pas les données révisées). Le pipeline COT doit stocker la version initiale de chaque rapport, pas uniquement la version la plus récente.
*Catégorie : macro_evenements*

### D5217 — Ignorer les problèmes complexes au début pour maîtriser les mécaniques
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_getting_data.md) : La recommandation d'Adam Grimes pour les débutants est d'ignorer d'abord les problèmes complexes (ajustements, devises, révisions) pour se concentrer sur les mécaniques fondamentales. Revenir ensuite aux problèmes complexes avec une bonne compréhension des bases.
**TRADEX-AI C1** : La Phase C (collecteurs NT8/ATAS) doit d'abord fonctionner avec des JSONs simples de données de clôture avant d'intégrer les données tick, order flow, et COT. La complexité doit être ajoutée progressivement pour éviter les bugs non détectables.
*Catégorie : configuration*

### D5218 — Les devises étrangères introduisent un biais caché dans les backtest
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_getting_data.md) : Pour les instruments libellés en devises non-USD, le retour en devise locale peut diverger significativement du retour en USD. Ce biais doit être géré explicitement dans les analyses multi-marchés.
**TRADEX-AI C4** : Le Dollar Index (DX) est un actif de confirmation dans TRADEX-AI précisément pour capturer ce biais macroéconomique. Une hausse du DX impacte différemment GC (négatif), CL (négatif), HG (négatif) et ZW (mixte). Le Cercle C4 (Macro) intègre ce facteur de correction.
*Catégorie : macro_evenements*

### D5219 — Sources de données gratuites et leurs limites
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_getting_data.md) : Yahoo! Finance et Quandl sont des sources de données gratuites pour les données journalières. Pour les données intraday, un abonnement à un fournisseur de données payant est nécessaire. La Fed de St. Louis (FRED) est la référence pour les données économiques.
**TRADEX-AI C4** : Alpha Vantage est utilisé dans TRADEX-AI comme proxy pour le DX (Dollar Index) — conforme à la liste des sources de données identifiées. La gratuité d'Alpha Vantage avec une clé API est cohérente avec l'architecture locale Windows.
*Catégorie : macro_evenements*

### D5220 — L'ordre chronologique des données : convention down-is-newer
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_getting_data.md) : Adam Grimes recommande que les nouvelles données soient en bas du fichier (ordre chronologique ascendant). Yahoo! Finance exporte en ordre inverse — un tri est nécessaire. Cette convention est importante pour la cohérence des formules d'index temporel.
**TRADEX-AI C1** : Les fichiers JSON produits par data_reader.py pour NT8/ATAS doivent utiliser un ordre chronologique ascendant (timestamp croissant) pour être cohérents avec le calcul des MAs et indicateurs Belkhayate. Cette convention doit être documentée dans settings.py.
*Catégorie : configuration*
