# Extraction AdamGrimes — Basic Backtesting In Excel: Introduction
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_introduction.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5271 → D5282 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-introduction/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Fondements méthodologiques du backtesting et compréhension des indicateurs — base épistémologique pour valider les règles Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5271 — Comprendre un indicateur jusqu'au calcul interne est obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_introduction.md) : Un trader doit pouvoir calculer lui-même tout indicateur qu'il utilise (stochastics, MACD, etc.). Reconstruire le calcul étape par étape force à comprendre ce qui est mesuré et comment. Les traders qui traitent les indicateurs comme des « lignes magiques » sans comprendre leur logique manquent du niveau de scepticisme nécessaire.
**TRADEX-AI C1** : Les formules COG Belkhayate (période 180, ordre 3, coefficients 0.618/1.618) sont verrouillées mais marquées `[RECONSTRUCTION]` car non validées. Cette décision confirme que la validation mathématique complète des formules doit précéder toute utilisation en production — en Phase C avec range bars NT8.
*Catégorie : indicateurs_tendance*

### D5272 — Excel permet une visualisation intuitive des relations entre données
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_introduction.md) : La disposition en lignes et colonnes alignées avec des calculs référençant d'autres cellules aide à construire une intuition solide sur le flux données → calculs → résultats statistiques. C'est particulièrement utile pour les débutants en analyse quantitative.
**TRADEX-AI C1** : Pour Abdelkrim (profil débutant technique), les exports CSV des données NT8 vers un format lisible en tableur peuvent faciliter la compréhension des sorties de `data_reader.py` avant qu'un dashboard React soit disponible. À envisager pour la phase de tests.
*Catégorie : psychologie*

### D5273 — Le look-ahead bias invalide complètement un test même en petite quantité
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_introduction.md) : « Even the tiniest amount of data leakage like this will completely invalidate your test. » Un système qui achète aujourd'hui si le marché sera plus haut dans une semaine est valide techniquement dans Excel — mais impossible à exécuter en réel. La première ligne de défense est de reconnaître que des résultats « trop beaux » indiquent un biais.
**TRADEX-AI C1** : Règle de validation KB : toute décision ajoutée doit mentionner si elle a été testée out-of-sample. Les résultats basés sur optimisation en-sample uniquement sont flaggés `HYPOTHESE`.
*Catégorie : gestion_risque_entree*

### D5274 — Les règles de trading complexes dépassent rapidement les capacités d'Excel
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_introduction.md) : Calculer des signaux d'achat/vente simples est faisable dans Excel, mais des règles complexes (conditions multiples, gestion de position, rotation d'actifs) deviennent très difficiles à maintenir. Python est le pas naturel suivant pour des tests rigoureux.
**TRADEX-AI C1** : Architecture TRADEX-AI justifiée : la règle `3/4 trading + 2/3 confirmation alignés = signal valide` avec 7 cercles d'intelligence et score /10 est trop complexe pour Excel. Le moteur Python (`05-saas/engine/`) est la seule architecture correcte.
*Catégorie : configuration*

### D5275 — La gestion de données historiques nécessite une vraie base de données
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_introduction.md) : Maintenir des séries de prix historiques mises à jour, avec jointures entre instruments, dépasse les capacités d'Excel. Une vraie base de données est nécessaire dès qu'on veut mettre à jour les séries et les interroger efficacement.
**TRADEX-AI C1** : SQLite (stack technique TRADEX-AI) est le choix correct pour stocker les données NT8/ATAS. Le dossier `data\` (actuellement inexistant — dette technique point 3) est la prochaine priorité à créer en Phase C.
*Catégorie : configuration*

### D5276 — Le backtesting doit couvrir : données, calculs, signaux, statistiques
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_introduction.md) : Un cycle de backtesting complet comprend 4 étapes : (1) obtenir et ingérer les données, (2) calculer les mesures dérivées (MM, relations entre marchés), (3) déclencher les règles de trading (signaux achat/vente), (4) calculer les statistiques de résultat et chercher un edge.
**TRADEX-AI C1** : Ce cadre 4 étapes correspond exactement à l'architecture événementielle TRADEX-AI (Niveaux 1→3). Niveau 1 = données NT8 + calculs. Niveau 2 = filtres. Niveau 3 = signal Claude. La boucle est correctement structurée.
*Catégorie : configuration*

### D5277 — La compréhension profonde d'un outil évite les erreurs silencieuses
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_introduction.md) : Forcer un indicateur à être recalculé manuellement oblige à comprendre ses paramètres internes, ses dépendances temporelles et ses biais. Cette compréhension génère un scepticisme sain sur les résultats.
**TRADEX-AI C1** : Avant d'utiliser l'Énergie Belkhayate (stub non codé), résoudre le conflit `MFI vs proxy ATR` par une compréhension du calcul exact utilisé par Belkhayate — puis coder et valider. Ne jamais intégrer un stub non compris dans la production.
*Catégorie : indicateurs_momentum*
