# Extraction AdamGrimes — Reader Question: How To Backtest?
**Source :** `bundles/adamgrimes/reader_question_how_to_backtest.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6471 → D6480 · **Page :** https://www.adamhgrimes.com/reader-question-how-to-backtest/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Protocole rigoureux de backtesting pour valider l'edge Belkhayate avant toute mise en production du mode Auto.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

---

## DÉCISIONS

### D6471 — Formation statistique obligatoire avant tout backtesting sérieux
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_how_to_backtest.md) : Avant d'externaliser ou d'automatiser un backtest, un trader doit maîtriser les statistiques, la probabilité et les méthodes de backtesting. Sans cette base, il est impossible de détecter les nombreux pièges et erreurs fatales que même un backtester bien intentionné peut commettre.
**TRADEX-AI C7** : La validation de l'edge Belkhayate sur GC/HG/CL/ZW (Phase C du projet) doit s'appuyer sur une méthodologie statistique rigoureuse — non pas sur des résultats visuels ou des courbes equity. Documenter la méthode statistique avant tout backtest officiel.
*Catégorie : configuration*

### D6472 — Le backtest bien présenté ne garantit pas la performance future
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_how_to_backtest.md) : Il est facile de produire un backtest visuellement convaincant. L'objectif réel est de produire un système qui fonctionne dans le futur, ce qui est beaucoup plus difficile. Les prestataires de backtesting peuvent dazzler avec Monte Carlo et statistiques non-paramétriques sans garantir la robustesse future.
**TRADEX-AI C7** : Le backtest COG daily invalidé (S11, commit e45a0fe) illustre exactement ce point — un backtest sur mauvais timeframe (daily vs range bars NT8) peut sembler invalide même si la logique est correcte. Toute validation Belkhayate doit spécifier le timeframe exact des range bars NT8 utilisées en production.
*Catégorie : configuration*

### D6473 — Piège d'overfitting : modifier les règles puis retester sur les mêmes données
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_how_to_backtest.md) : Modifier un ensemble de règles en fonction des résultats puis relancer un test sur les mêmes données est une erreur classique qui produit de l'overfitting (surapprentissage). De même, tester un indicateur avec plusieurs paramètres et choisir le meilleur dégrade la fiabilité du test.
**TRADEX-AI C1** : Règle critique pour TRADEX — les paramètres COG (période 180, ordre 3, coeffs 0,618/1,618) sont figés (décision verrouillée S11). Ne jamais modifier ces paramètres après observation des résultats backtesting, sauf revalidation complète sur données out-of-sample.
*Catégorie : configuration*

### D6474 — Excel utile pour premiers backtests : visibilité sur les données
🔵 **ÉCOLE** (Source : reader_question_how_to_backtest.md) : Faire ses premiers backtests en Excel, malgré ses limites, présente un avantage pédagogique majeur : on voit et manipule directement les données, ce qui donne une compréhension que des outils comme Stata, Matlab, Python ou R ne donnent pas aussi facilement au débutant.
**TRADEX-AI C7** : Pour la validation manuelle des signaux Belkhayate historiques sur GC/HG/CL/ZW — commencer par des analyses Excel sur des échantillons de 50-100 trades avant de passer aux backtests Python automatisés.
*Catégorie : configuration*

### D6475 — Outils de backtesting avancés : Python et R recommandés à terme
🔵 **ÉCOLE** (Source : reader_question_how_to_backtest.md) : Python et R sont les environnements à terme pour des backtests rigoureux. Stata et Matlab sont aussi utilisés par des professionnels. La progression naturelle est : Excel (compréhension) → Python/R (robustesse statistique).
**TRADEX-AI C7** : Architecture TRADEX (Python 3.11) est déjà alignée avec cette recommandation — le module de backtest Belkhayate sera développé en Python avec validation statistique formelle.
*Catégorie : configuration*

### D6476 — Démarche : tester d'abord des concepts simples, chercher l'edge avant de construire le système
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_how_to_backtest.md) : La bonne séquence est : (1) maîtriser les statistiques, (2) comprendre les pièges du backtesting, (3) créer des backtests simples de concepts simples, (4) chercher l'edge, (5) puis construire et tester le système. Aller directement à l'étape 5 est une erreur.
**TRADEX-AI C1** : Pour la validation Belkhayate — commencer par tester la règle la plus simple (ex : signal BGC seul sur GC) avant de combiner les 7 cercles. Chaque couche ajoutée doit montrer un gain d'edge statistiquement significatif.
*Catégorie : configuration*

### D6477 — Les services payants de backtesting ne remplacent pas la compréhension personnelle
🟡 **SYNTHÈSE** (Source : reader_question_how_to_backtest.md) : Des prestataires proposent des services de backtesting avec des modèles Monte Carlo et des statistiques avancées, mais sans éducation personnelle préalable, le trader ne peut pas évaluer la qualité du travail ni détecter les pièges. L'auto-formation reste indispensable.
**TRADEX-AI C7** : TRADEX est un système propriétaire — tout audit externe du backtest Belkhayate doit être accompagné d'une compréhension interne suffisante pour valider les hypothèses et détecter l'overfitting.
*Catégorie : psychologie*
