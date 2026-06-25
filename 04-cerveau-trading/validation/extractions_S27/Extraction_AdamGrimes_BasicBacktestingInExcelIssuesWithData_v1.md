# Extraction AdamGrimes — Basic Backtesting In Excel: Issues With Data
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_issues_with_data.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5291 → D5305 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-issues-with-data/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Identification des pièges de qualité des données multi-instruments — critique pour la fiabilité de `data_reader.py` et `correlations.py`.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5291 — Les instruments n'ont pas tous les mêmes jours de trading
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Différents marchés ont des jours fériés différents. Une devise peut avoir tradé un jour où la bourse américaine était fermée. Aligner deux séries par simple collage génère des décalages de dates — la jointure par date exacte (VLOOKUP / équivalent) est obligatoire.
**TRADEX-AI C7** : Dans `correlations.py`, l'alignement des séries GC/HG/CL/ZW/ES/VX/MBT/6J doit utiliser une jointure par timestamp exact, pas une simple concaténation. Les jours sans donnée pour un actif doivent être marqués comme `NaN` et exclus du calcul de corrélation, pas remplis arbitrairement.
*Catégorie : correlations*

### D5292 — Le trading asynchrone crée des corrélations illusoires entre marchés
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Des données portant le même horodatage peuvent ne pas représenter le même instant réel. Exemple : clôture Brent (Londres) vs WTI (New York) — heures de fermeture différentes. Comparer une action US (clôture 16h EDT) avec une action européenne (clôture plusieurs heures plus tôt) crée une relation non-exécutable en spread.
**TRADEX-AI C7** : Pour la matrice de corrélations 30j, utiliser uniquement des données horaires ou range-bars NT8 avec timestamps identiques. Le DX (Dollar Index) proxifié via DXY Alpha Vantage doit être aligné sur le même fuseau horaire que les futures CME avant tout calcul de corrélation.
*Catégorie : correlations*

### D5293 — Les données intraday ont des problèmes d'horodatage début/fin de barre
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Certains fournisseurs horodatent les barres au début, d'autres à la fin. Mixer des sources sans vérifier cette convention crée des décalages d'une période. Un actif peu liquide affichera le même prix pendant plusieurs minutes tandis qu'un actif actif évolue — créant une fausse relation de spread.
**TRADEX-AI C2** : Les données ATAS (Footprint, Delta) et NT8 doivent partager la même convention d'horodatage dans `data_reader.py`. Documenter explicitement la convention (début ou fin de barre) pour chaque source dans `settings.py`.
*Catégorie : volume_liquidite*

### D5294 — Le back-adjustment des contrats futures est complexe et souvent mal fait
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Les séries de prix futures nécessitent un ajustement pour les rollovers de contrats. Les méthodologies existent mais doivent être appliquées correctement. Les analystes techniques naïfs ignorent souvent ces ajustements — ce qui rend les niveaux de prix historiques et de nombreuses formations chartistes peu fiables sur futures.
**TRADEX-AI C1** : Les actifs tradables TRADEX (GC, HG, CL, ZW) sont tous des futures. Toute règle Belkhayate citant des niveaux de prix absolus historiques doit préciser si les données sont back-adjustées. Les règles basées sur des patterns relatifs (structure, dynamique) sont plus robustes que les niveaux absolus.
*Catégorie : structure_marche*

### D5295 — Les erreurs de données courantes : entrées manquantes et prix identiques
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Erreurs fréquentes dans les flux de données : (1) barres manquantes, (2) série de barres avec exactement le même OHLC (prix figé), (3) H=L=C dans un marché actif (anormal), (4) H < L ou L > H (logiquement impossible), (5) décimales manquantes ou mal placées générant des variations de +/-1000%, (6) données de volume/open interest erronées.
**TRADEX-AI C1** : `data_reader.py` et `staleness_monitor.py` doivent implémenter des validations de sanité : vérifier H >= L, détecter les prix figés (N barres consécutives identiques), détecter les sauts de prix aberrants (>X% en une barre). Résultat = BLOCKED si anomalie détectée.
*Catégorie : volume_liquidite*

### D5296 — 85% du temps des chercheurs en finance est consacré aux données
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Certains chercheurs académiques estiment que 85% de leur temps est consacré à des tâches liées aux données (nettoyage, alignement, validation, mise à jour). La qualité des données est le facteur le plus sous-estimé dans la rigueur d'un backtest.
**TRADEX-AI C1** : Cette réalité justifie la priorité accordée à `staleness_monitor.py` et au `data\` dossier (dette technique point 3) avant toute expansion de la KB. Des données NT8 fiables et validées précèdent tout signal Claude.
*Catégorie : configuration*

### D5297 — Les données payantes contiennent aussi des erreurs
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Même les données achetées auprès de fournisseurs commerciaux contiennent des erreurs. Payer pour les données ne garantit pas leur qualité. Une validation systématique reste nécessaire quelle que soit la source.
**TRADEX-AI C1** : Les données Rithmic via NT8/ATAS (flux payant via broker NTB) doivent faire l'objet des mêmes contrôles de sanité que tout flux gratuit. Ne jamais supposer la qualité des données du seul fait qu'elles proviennent d'un feed professionnel.
*Catégorie : gestion_risque_entree*

### D5298 — La jointure par date exacte est obligatoire pour les séries multi-actifs
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_issues_with_data.md) : Pour combiner deux séries temporelles (ex. SPY + TLT), une jointure par date exacte est indispensable car les deux séries peuvent avoir des dates manquantes différentes. Un simple alignement de colonnes introduit des erreurs silencieuses où une date de l'une correspond à une date différente de l'autre.
**TRADEX-AI C7** : La matrice de corrélations `correlations.py` doit implémenter une jointure inner/outer explicite sur timestamp, avec journalisation des dates manquantes par actif. Tout calcul de corrélation doit indiquer le nombre de points communs effectivement utilisés.
*Catégorie : correlations*
