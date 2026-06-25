# Extraction AdamGrimes — Basic Backtesting In Excel: How To Keep Learning
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_how_to_keep_learning.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5251 → D5261 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-how-to-keep-learning/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Principes de validation statistique et d'évitement des biais dans le backtesting — essentiels pour fiabiliser la KB Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5251 — Contamination par données futures (look-ahead bias)
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : La contamination par des données futures est l'une des pires erreurs de backtesting. Elle peut se produire de façon subtile — ex. : utiliser la clôture du jour J pour calculer une MM qui inclut ce même J, puis décider d'acheter avant de connaître cette clôture. Un test infecté paraît toujours fantastique mais est inexploitable en temps réel.
**TRADEX-AI C1** : Tout indicateur Belkhayate (COG, BGC, etc.) calculé dans les scripts Python doit utiliser exclusivement des données antérieures au bar en cours. Valider systématiquement que `data_reader.py` ne transmet pas la clôture courante à un calcul qui l'utiliserait pour un signal de la même bougie.
*Catégorie : gestion_risque_entree*

### D5252 — La moyenne mobile ne peut pas servir d'entrée sur son propre prix
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Le prix de la moyenne mobile change au fur et à mesure que la clôture du jour évolue (il inclut cette même clôture). Il est donc impossible d'acheter « sur la MM » le jour J car le niveau exact de la MM n'est connu qu'à la clôture — moment où il est trop tard pour entrer au même prix.
**TRADEX-AI C1** : Pour les stratégies Belkhayate utilisant la MM comme soutien/résistance, le signal doit être validé à la clôture du bar précédent (J-1), jamais sur le bar en cours. Documenter cette contrainte dans `claude_brain.py`.
*Catégorie : gestion_risque_entree*

### D5253 — La randomité du marché est l'ennemi principal du backtesting
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Si un signal est aléatoire, il ne peut pas être monetisé. Il n'existe aucun moyen de prouver avec une certitude absolue qu'une pattern n'est pas aléatoire, mais des outils statistiques permettent d'établir une probabilité raisonnée. La plupart des statistiques de marché publiées souffrent d'un biais quelconque.
**TRADEX-AI C1** : Chaque règle intégrée dans `KNOWLEDGE_BASE_MASTER.json` doit avoir un seuil de confiance et une source primaire. Les règles sans validation statistique doivent être marquées `confiance: HYPOTHESE`. Le score /10 Belkhayate est la synthèse déterministe — non une intuition.
*Catégorie : configuration*

### D5254 — Tests de robustesse recommandés : séries de jours + VIX + saisonnalité
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Adam Grimes recommande comme exercices de backtesting : (1) N jours consécutifs haussiers/baissiers, (2) niveaux VIX élevés/bas vs rendements actions futurs, (3) changements importants du VIX vs rendements, (4) divergence VIX vs volatilité historique calculée, (5) saisonnalité par jour/semaine/mois selon les classes d'actifs.
**TRADEX-AI C5** : Les tests VIX sont directement pertinents pour le cercle C5 (Sentiment). La relation VIX vs GC/ES doit être testée sur données historiques avant d'être intégrée comme règle de confirmation dans `correlations.py`.
*Catégorie : indicateurs_momentum*

### D5255 — La saisonnalité nécessite une rigueur statistique maximale
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Tester la saisonnalité (jours, semaines, mois de l'année par classe d'actifs) est décrit comme un « mini masterclass en tests de significativité ». Le risque de sur-ajustement est élevé ; la significativité statistique doit être démontrée rigoureusement.
**TRADEX-AI C1** : Toute règle saisonnière Belkhayate introduite dans la KB doit indiquer la période de test, la taille d'échantillon et le niveau de confiance. Les assertions saisonnières sans ces éléments restent dans `A_VERIFIER_HUMAIN.md`.
*Catégorie : saisonnalite*

### D5256 — Excel insuffisant dès que les règles deviennent complexes → Python requis
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Dès que les règles de trading impliquent des conditions combinées (ex. : être long sur l'actif à la meilleure force relative parmi N actifs avec rotation selon critères), Excel devient inadapté. VBA est une étape intermédiaire ; Python ou R sont les outils adaptés pour des tests sérieux.
**TRADEX-AI C7** : L'architecture Python de TRADEX-AI (`05-saas/engine/`) est le choix correct. `correlations.py` qui calcule la matrice live 30j GC/HG/CL/ZW/ES/VX/MBT/6J est architecturalement justifié par cette contrainte — ne jamais régresser vers des calculs Excel manuels pour valider la KB.
*Catégorie : correlations*

### D5257 — Un résultat « trop beau » indique presque toujours un biais
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_how_to_keep_learning.md) : Les tests contaminés par du look-ahead bias produisent systématiquement des statistiques « homerun » (performances irréalistes). Cette apparence de perfection est elle-même un signal d'alerte. La vigilance doit être maximale sur les tests aux résultats spectaculaires.
**TRADEX-AI C1** : Dans le cadre du backtest COG (e45a0fe), les résultats non validés sur daily (timeframe incorrect) sont cohérents avec cette règle. Avant d'intégrer tout backtest dans la KB, vérifier : (a) absence de look-ahead, (b) timeframe correct (range bars NT8, pas daily), (c) résultat non aberrant.
*Catégorie : configuration*
