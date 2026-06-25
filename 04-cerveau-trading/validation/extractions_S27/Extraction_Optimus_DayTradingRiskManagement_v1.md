# Extraction Optimus — Day Trading Risk Management
**Source :** `bundles/optimusfutures/day_trading_risk_management.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8391 → D8410 · **Page :** https://optimusfutures.com/blog/day-trading-risk-management/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : règles de gestion du risque day trading (1-2% max, daily loss limit, R:R ratios, psychologie) — directement applicables risk_manager.py et Mode Manuel TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8391 — Règle fondamentale : survivre via contrôle des pertes, pas maximisation des gains
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Les traders professionnels survivent non pas parce qu'ils gagnent tous leurs trades, mais parce qu'ils contrôlent leurs pertes. La gestion du risque est la compétence primaire, non la stratégie de signal.
**TRADEX-AI C1** : Règle Belkhayate confirmée : le risk_manager.py TRADEX-AI est un composant de première classe, pas accessoire. La Sécurité #1-6 du CLAUDE.md (Circuit Breaker, Staleness Monitor, etc.) incarne ce principe.
*Catégorie : gestion_risque_entree*

### D8392 — Règle 1-2% max par trade : calcul de taille de position via stop-loss
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Risquer 1-2% max du compte par trade. Calcul exact : Max Risk = 2% × capital. Taille position = Max Risk ÷ (distance stop × valeur du point). Exemple MES : compte $5,000 → max risk $100 → stop 10 pts × $5/pt = $50/contrat → 2 contrats. Ne jamais estimer à vue, toujours calculer mathématiquement.
**TRADEX-AI C1** : Le risk_manager.py doit implémenter ce calcul automatiquement. Pour GC (Or) : 1 point = $10 (contrat standard), $1 = $100 (Micro MGC = $10). Stop-loss distance fourni par le Signal Belkhayate → taille calculée en temps réel avant tout ordre Mode Auto.
*Catégorie : gestion_risque_entree*

### D8393 — Daily Max Loss Limit : circuit breaker à 5% ou 3 trades perdants consécutifs
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Les traders professionnels fixent une limite de perte journalière pour prévenir les spirales émotionnelles. Règle typique : 5% du compte total ou 3 trades perdants consécutifs. Quand la limite est atteinte → fermer la plateforme immédiatement. Pas de revenge trading.
**TRADEX-AI C1** : Cette règle est DÉJÀ implémentée dans TRADEX-AI via la Sécurité #5 (suspend_auto_mode après pertes). Aligner la valeur dans settings.py avec ce standard professionnel : DAILY_MAX_LOSS = 5% ou MAX_CONSECUTIVE_LOSSES = 3. Vérifier la cohérence avec GARDE_FOUS_PROPOSES.md.
*Catégorie : gestion_risque_entree*

### D8394 — Bracket orders obligatoires : stop et target pré-définis à l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Toujours pré-définir stop-loss et target au moment de l'entrée (bracket orders). Ceci élimine l'émotion du processus de gestion de position. Un trader qui décide de sa sortie en position est beaucoup plus sujet aux erreurs émotionnelles.
**TRADEX-AI C1** : Dans Mode Auto TRADEX-AI via NT8 ATI, tout ordre est envoyé avec bracket (stop + target) automatiquement calculés. En Mode Manuel, l'interface doit afficher les niveaux suggérés stop/target pour qu'Abdelkrim puisse les saisir rapidement. Ne jamais afficher un signal sans ces niveaux.
*Catégorie : gestion_position_active*

### D8395 — Respect de la volatilité : réduire la taille ou s'abstenir pendant CPI/FOMC/NFP
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Pendant les événements à fort impact (CPI, FOMC, Jobs Report), réduire la taille ou s'abstenir de trader jusqu'à ce que la volatilité se stabilise.
**TRADEX-AI C4** : Règle News Gate TRADEX-AI confirmée et renforcée : bloquer signaux 30min avant NFP/FOMC/CPI (déjà dans Sécurité #1 CLAUDE.md). Ajouter : 15min après l'annonce = taille divisée par 2 automatiquement en Mode Auto. Ce délai post-événement est le "calme après la tempête".
*Catégorie : macro_evenements*

### D8396 — Interdire le revenge trading : ne pas doubler après une perte
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Après une perte, ne pas doubler la taille pour "rattraper". Cette tendance (revenge trading) est l'une des causes principales de destruction de compte chez les débutants.
**TRADEX-AI C1** : Dans risk_manager.py, après chaque perte enregistrée, maintenir ou réduire la taille de position calculée. Interdire toute augmentation de taille dans les 3 trades suivant une perte. Paramètre configurable : POST_LOSS_SIZE_LOCK = True par défaut.
*Catégorie : psychologie*

### D8397 — Ratio Risk/Reward : 3 niveaux (1:1 scalp, 2:1 débutant, 3:1 pro)
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Niveaux R/R reconnus : Tight Scalp 1:1 (breakeven après frais), Balanced 2:1 (objectif débutant commun), Aggressive 3:1 (préféré des pros). Avec seulement 40% de win rate, un setup 2:1 peut être rentable à long terme.
**TRADEX-AI C1** : Le seuil TRADEX-AI R/R ≥ 1:2 (STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md, Partie 4) est aligné avec le niveau "Balanced" confirmé par cette source. Pour le Mode Auto, n'exécuter que des setups ≥ 2:1. Le niveau 3:1 est l'objectif optimal pour TRADEX-AI.
*Catégorie : gestion_risque_entree*

### D8398 — Connaitre le calendrier économique : step aside avant événements majeurs
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : Parfois le meilleur trade est de ne pas trader. La liquidité mince, les news à fort impact, et la fatigue émotionnelle créent des pertes évitables. Vérifier le calendrier économique avant de trader et identifier les événements.
**TRADEX-AI C4** : Le News Gate TRADEX-AI (Sécurité #1) implémente ce principe. À renforcer : ajouter une fenêtre "post-événement" de 15min dans le calendrier. Les événements FOMC et NFP sont les plus critiques pour GC, CL (impacts directs).
*Catégorie : macro_evenements*

### D8399 — FOMO : ennemi n°1 des comptes débutants — règle 2-trigger
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Le FOMO pousse à chaser : breakouts déjà terminés, tendances presque finies, spikes de news. La règle 2-Trigger : avant d'entrer, vérifier (1) est-ce que ça correspond à mon setup ? (2) puis-je placer un stop-loss immédiatement ? Si une des réponses est NON → ne pas entrer. "Ne pas trader est une décision de trading."
**TRADEX-AI C5** : La règle 2-Trigger est implémentée structurellement dans TRADEX-AI : la règle d'entrée "3/4 + 2/3 alignés" EST le filtre anti-FOMO. Aucun signal n'est émis sur une opportunité déjà passée. Ajouter dans l'interface un affichage explicite "Setup actif / Pas de setup" pour renforcer la discipline d'Abdelkrim.
*Catégorie : psychologie*

### D8400 — Fear (peur) : sortie prématurée des gagnants + maintien des perdants
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : La peur pousse à : sortir les trades gagnants trop tôt, maintenir les trades perdants trop longtemps, déplacer les stops "juste un peu plus", douter du setup après un seul mauvais trade. Solution : pré-définir TOUT avant l'entrée (entrée, stop, target, risque max) pour que la peur ne puisse pas "pirater" le processus.
**TRADEX-AI C1** : En Mode Manuel TRADEX-AI, l'interface doit afficher en permanence les niveaux pré-calculés (stop/target) même après l'entrée, pour éviter que la peur ne modifie les décisions d'Abdelkrim. Un disclaimer "Respecter le plan" doit être visible pendant la gestion de position.
*Catégorie : psychologie*

### D8401 — Overtrading : 3-Trade Rule pour limiter les trades par session
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Chaque trade doit avoir une raison ancrée dans le plan. Signes d'overtrading : trader par ennui, trader chaque micro-mouvement sur 1min chart, augmenter la taille après une perte, sauter entre marchés. Solution : règle des 3 trades max par session. Si 3 trades pris sans setup de qualité → arrêter la session.
**TRADEX-AI C1** : Implémenter MAX_TRADES_PER_SESSION = 3 dans risk_manager.py. Après 3 trades clôturés dans la session, Mode Auto se bloque automatiquement (même sans perte). Mode Manuel affiche un avertissement. Paramètre configurable par Abdelkrim.
*Catégorie : gestion_risque_entree*

### D8402 — Tilt émotionnel : 90-second reset après grosse perte ou trade manqué
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : Le tilt survient quand le trader arrête de penser clairement et commence à agir comme s'il avait quelque chose à prouver. Déclencheurs : grosse perte, trade manqué, revenge trading, stress ou fatigue. Solution : règle des 90 secondes — respirer lentement, s'éloigner de l'écran, boire de l'eau. Cela interrompt le momentum émotionnel avant qu'il ne s'amplifie.
**TRADEX-AI C1** : Après chaque perte dépassant 1% du capital, l'interface TRADEX-AI doit afficher obligatoirement un écran de pause de 90 secondes avec le message "Pause recommandée — Éloignez-vous de l'écran." Le Mode Auto reste suspendu pendant cette pause.
*Catégorie : psychologie*

### D8403 — Confiance calme vs ego : progression taille uniquement après cohérence
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : L'objectif n'est ni le manque de confiance ni l'ego ("je suis inarrêtable"). L'objectif est la confiance calme — ancrée, disciplinée, reproductible. Se construit via : trader petit, journaliser tout, review hebdomadaire, collecter des données pas des émotions. Augmenter la taille SEULEMENT après cohérence démontrée.
**TRADEX-AI C1** : Dans TRADEX-AI, la règle progression de taille est : Skill → Consistency → Size → Profit. JAMAIS l'inverse. Implémenter un "palier de validation" dans risk_manager.py : augmentation de taille autorisée seulement après X trades consécutifs respectant le plan (win rate + R/R), paramétrable.
*Catégorie : psychologie*

### D8404 — 4 personas de trader : Sniper, Momentum Rider, Mean-Reverter, Patient Trader
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : Les traders les plus efficaces connaissent leur identité de trading : (1) Sniper — attend les setups A+, faible fréquence, haute précision ; (2) Momentum Rider — excelle dans les mouvements rapides, stops serrés ; (3) Mean-Reverter — achète les pullbacks, vend les overextensions ; (4) Patient Trader — approche méthodique et calme. Choisir un persona et construire la stratégie autour.
**TRADEX-AI C1** : La méthode Belkhayate correspond au profil "Sniper" : attendre que 3/4 actifs + 2/3 confirmation + score ≥ 7/10 soient alignés. Abdelkrim est par construction un Sniper dans TRADEX-AI — faible fréquence, haute conviction. Cette source valide l'approche.
*Catégorie : psychologie*

### D8405 — Recovery Blueprint après grosse perte : stop 30min + review + ajuster 1 chose
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : Blueprint de récupération après grosse perte : (1) Arrêter de trader pendant 30 minutes minimum ; (2) Analyser ce qui s'est passé — setup défaillant ? FOMO ? fatigue ? ; (3) Ajuster UNE chose seulement, pas cinq ; (4) Re-entrer uniquement quand le mental est clair.
**TRADEX-AI C1** : La Sécurité #5 TRADEX-AI (suspension Auto 15-60 min après perte) implémente ce principe partiellement. Renforcer : après chaque trade perdant dépassant 1.5%, afficher en Mode Manuel le Recovery Blueprint comme checklist interactive. L'utilisateur coche chaque étape avant de retrouver un accès complet.
*Catégorie : gestion_risque_entree*

### D8406 — Progression en 7 étapes : démo → live micro → consistance → scale
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : Séquence de progression recommandée : (1) Démo avec données temps réel ; (2) Choisir 1 marché + 1 setup ; (3) Ouvrir compte live quand prêt ; (4) Trader 1 micro-contrat (exposition minimale) ; (5) Journaliser toutes les semaines ; (6) Obtenir du support d'experts ; (7) Augmenter la taille seulement après consistance sur 30-50 trades.
**TRADEX-AI C1** : TRADEX-AI suit déjà cette progression : Mode Manuel (équivalent "démo décisionnel") → Mode Auto uniquement après validation Abdelkrim. L'objectif 30-50 trades avant de scale est aligné avec la philosophie TRADEX-AI de prudence opérationnelle.
*Catégorie : gestion_risque_entree*

### D8407 — Choisir un marché selon la personnalité : MES (lisse), MNQ (rapide), MGC (structuré)
🔵 **ÉCOLE** (Source : day_trading_risk_management.md) : Choisir un marché selon sa personnalité : MES (E-mini S&P Micro) — tendances lisses ; MNQ (Nasdaq Micro) — momentum rapide ; MGC (Micro Gold) — mouvements lents et structurés ; MCL (Micro Crude) — volatilité avec catalyseurs clairs.
**TRADEX-AI C1** : Pour TRADEX-AI, les actifs TRADING Belkhayate sont GC/HG/CL/ZW. GC (Or) = marché "structuré et structurel" de type MGC décrit ici. CL (Pétrole) = volatilité avec catalyseurs (catalysts = macro events C4). HG (Cuivre) et ZW (Blé) = marchés à catalyseurs fondamentaux C4.
*Catégorie : configuration*

### D8408 — 2-Trigger Rule comme filtre anti-entrée impulsive
🟡 **SYNTHÈSE** (Source : day_trading_risk_management.md) : La règle 2-Trigger est un filtre structurel simple mais puissant contre l'entrée impulsive : (1) Le setup correspond-il à mon plan ? (2) Puis-je placer un stop immédiatement ? Les deux doivent être OUI. Cette règle disciplinaire évite 80% des entrées émotionnelles.
**TRADEX-AI C1** : Dans l'interface TRADEX-AI Mode Manuel, afficher ces 2 questions en overlay sur chaque signal avant qu'Abdelkrim puisse valider manuellement une entrée. Il doit cliquer "OUI" aux deux avant que le bouton d'entrée s'active. Mécanisme de friction intentionnelle.
*Catégorie : psychologie*

### D8409 — Skill→Consistency→Size→Profit : séquence non négociable
🟢 **FAIT VÉRIFIÉ** (Source : day_trading_risk_management.md) : La séquence de développement d'un trader est non négociable : Skill (compétence) → Consistency (régularité) → Size (taille) → Profit (bénéfice). JAMAIS dans l'autre sens. Augmenter la taille sans consistance préalable = destruction du compte.
**TRADEX-AI C1** : Cette séquence est la philosophie fondamentale de TRADEX-AI. Le Mode Auto n'est activable qu'après validation humaine (Abdelkrim). La progression vers des tailles plus grandes doit être documentée dans un journal de trading intégré à l'interface, non activable avant 30 trades cohérents en Mode Manuel.
*Catégorie : psychologie*

### D8410 — FAQ : 1-2% par trade · 2:1 ratio débutant · 3-Trade Rule · FOMO comme cause principale d'échec
🟡 **SYNTHÈSE** (Source : day_trading_risk_management.md) : Résumé FAQ Optimus Futures : (1) Risque max professionnel = 1-2% par trade ; (2) Ratio R/R débutant = 2:1 (professionnel = 3:1) ; (3) Anti-overtrading = 3-Trade Rule par session ; (4) Cause principale d'échec = FOMO, peur, overtrading, tilt (psychologie) — pas le manque de stratégie ; (5) Recovery Blueprint = stop 30min + review + ajuster 1 chose + re-entrer mental clair.
**TRADEX-AI C1** : Ces 5 points constituent les paramètres minimaux que risk_manager.py doit implémenter : MAX_RISK_PER_TRADE_PCT = 0.02, MIN_RR_RATIO = 2.0, MAX_TRADES_PER_SESSION = 3, RECOVERY_PAUSE_MINUTES = 30. Vérifier la cohérence de ces valeurs avec GARDE_FOUS_PROPOSES.md (42 garde-fous).
*Catégorie : gestion_risque_entree*
