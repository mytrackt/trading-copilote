# Extraction AdamGrimes — Bad Statistics Lead Bad Decisions
**Source :** `bundles/adamgrimes/bad_statistics_lead_bad_decisions.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5171 → D5185 · **Page :** https://www.adamhgrimes.com/bad-statistics-lead-bad-decisions/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthode de validation statistique des edges — comment éviter les faux signaux et les biais de sélection dans les règles Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5171 — Les statistiques faciles sont souvent trompeuses
🟢 **FAIT VÉRIFIÉ** (Source : bad_statistics_lead_bad_decisions.md) : Une statistique facile à calculer est souvent une statistique fausse ou trompeuse. Prendre des décisions de trading sur la base de statistiques incorrectes est directement néfaste pour le capital. L'absence d'information serait préférable à une mauvaise information.
**TRADEX-AI C1** : Toute règle extraite de la KB Belkhayate doit être validée par une méthodologie rigoureuse avant intégration ; une règle non vérifiée est plus dangereuse qu'une absence de règle.
*Catégorie : gestion_risque_entree*

### D5172 — Biais de confirmation statistique : l'effet « premier jour du mois »
🟢 **FAIT VÉRIFIÉ** (Source : bad_statistics_lead_bad_decisions.md) : Le test « premier jour du mois » sur le S&P 500 (1961–) semblait montrer un edge fort (64,9% positif si J1 haussier vs 51,2% si J1 baissier), mais le même résultat apparaît pour n'importe quel autre jour du mois (J2, J3… J17). Un résultat valide pour tous les jours est invalide comme edge — il n'existe aucune relation causale, seulement un artefact mathématique.
**TRADEX-AI C7** : Les corrélations inter-marchés testées dans la matrice 30j (GC/HG/CL/ZW/ES/VX) doivent être vérifiées contre ce même piège : si la corrélation est vraie pour toutes les conditions, elle n'a pas de valeur prédictive.
*Catégorie : correlations*

### D5173 — L'artefact de la corrélation interne : le retour mensuel comme variable confondue
🟡 **SYNTHÈSE** (Source : bad_statistics_lead_bad_decisions.md) : L'erreur méthodologique centrale est une variable confondue (confounding variable) : le retour mensuel cumulé inclut le jour testé. Tester si « J1 est haussier → le mois est haussier » est circulaire car J1 fait partie du mois. La solution est de mesurer séparément : retour de J2 à J_fin, conditionné au signe de J1.
**TRADEX-AI C1** : Lors du backtest des signaux Belkhayate, ne jamais inclure la bougie de signal dans la mesure de performance ; le retour doit être calculé à partir de la clôture du signal (J0) vers la cible (J+N), sans recouvrement.
*Catégorie : configuration*

### D5174 — Coût réel des erreurs statistiques pour un trader
🟢 **FAIT VÉRIFIÉ** (Source : bad_statistics_lead_bad_decisions.md) : Un trader professionnel a opéré un système pendant une décennie sur la base de statistiques apparemment solides (validées sous toutes les permutations de paramètres) et a perdu plusieurs millions de dollars (« high seven figures »). Le système semblait robuste à toutes les analyses sauf la bonne. Les statistiques pour un trader ne sont pas académiques — ce sont un outil de survie.
**TRADEX-AI C1** : Le moteur de scoring sur /10 ne doit accepter une règle KB que si elle passe un test out-of-sample ; les règles qui « marchent partout » doivent être marquées AMBIGU et envoyées dans A_VERIFIER_HUMAIN.md.
*Catégorie : psychologie*

### D5175 — Principe de vérification : chercher l'absurde
🔵 **ÉCOLE** (Source : bad_statistics_lead_bad_decisions.md) : La première vérification d'une statistique de marché est la cohérence logique. Demander « est-ce que ce résultat a un sens ? ». Si un test donne le même résultat quel que soit le paramètre utilisé (J1, J7, J17), le résultat est probablement un artefact, pas un edge. Le momentum mensuel de J17 est absurde → l'ensemble des résultats est suspect.
**TRADEX-AI C1** : Avant d'intégrer une règle dans la KB, appliquer le test de l'absurde : si la règle reste vraie quand on change arbitrairement ses paramètres de ±50%, c'est un signal d'artefact.
*Catégorie : gestion_risque_entree*

### D5176 — Résultat correct : absence d'effet premier jour
🟢 **FAIT VÉRIFIÉ** (Source : bad_statistics_lead_bad_decisions.md) : Avec une méthodologie correcte (retour mesuré de J2 à fin du mois, sans inclure J1 dans la mesure), il n'existe aucun effet statistiquement significatif du premier jour du mois sur la direction du reste du mois. Il n'y a aucun edge tradable ici.
**TRADEX-AI C4** : Les biais calendaires (début de mois, expiration options, FOMC…) ne doivent pas être utilisés comme déclencheurs de signal si leur validation croise le même biais qu'ils prétendent mesurer. Le News Gate (blocage 30min avant NFP/FOMC) reste une règle de sécurité, pas un signal directionnel.
*Catégorie : macro_evenements*

### D5177 — Règle de la séparation signal / retour dans tout backtest
🟡 **SYNTHÈSE** (Source : bad_statistics_lead_bad_decisions.md) : L'erreur fondamentale détectée est le chevauchement entre la période de signal et la période de mesure du retour. La correction universelle est : (1) définir la condition de signal sur une période fermée, (2) mesurer le retour sur une période strictement postérieure et non chevauchante.
**TRADEX-AI C1** : Pour les backtests COG/Timing Belkhayate (Phase C), la règle de non-chevauchement est absolue : le score /10 est calculé à T=0 (clôture bougie signal), la performance est mesurée de T+1 à T+N (cible ou stop).
*Catégorie : configuration*

### D5178 — Humilité épistémique dans l'analyse statistique
🔵 **ÉCOLE** (Source : bad_statistics_lead_bad_decisions.md) : Même une analyse correcte peut rater quelque chose. La posture correcte après un test négatif est « nous ne voyons pas d'effet, sauf si notre test a raté quelque chose — restons humbles ». Cette humilité est une protection contre la sur-confiance et les faux positifs.
**TRADEX-AI C1** : Le moteur TRADEX-AI doit afficher le niveau de confiance (%) avec chaque signal, et le fallback local est plafonné à 65% — jamais 100%. L'humilité statistique est câblée dans l'architecture.
*Catégorie : psychologie*

### D5179 — Producteurs ET consommateurs de statistiques sont responsables
🔵 **ÉCOLE** (Source : bad_statistics_lead_bad_decisions.md) : La responsabilité de la qualité statistique est partagée entre ceux qui produisent les chiffres (traders, analystes, vendeurs de systèmes) et ceux qui les consomment (décideurs, traders exécutants). Chaque partie doit être en garde contre les erreurs.
**TRADEX-AI C1** : Les règles KB extraites par le pipeline TRANSVIDEO (Gemini → extraction → audit → fusion) passent par 3 couches de validation avant intégration dans KNOWLEDGE_BASE_MASTER.json. Ce pipeline incarne la co-responsabilité producteur/consommateur.
*Catégorie : psychologie*

### D5180 — Statistiques comme outil de survie pour le trader
🟢 **FAIT VÉRIFIÉ** (Source : bad_statistics_lead_bad_decisions.md) : « Pour les traders, les statistiques sont une question de vie ou de mort » — ce sont l'outil principal de compréhension du mouvement des marchés. Les mauvaises statistiques produisent de mauvaises décisions, et les mauvaises décisions coûtent de l'argent.
**TRADEX-AI C1** : La KB Belkhayate (~1313 règles au 25/06/2026) est le substrat statistique de TRADEX-AI. Sa qualité détermine directement la qualité des signaux. Les 45 règles AMBIGU dans A_VERIFIER_HUMAIN.md représentent un risque actif à traiter en priorité.
*Catégorie : gestion_risque_entree*
