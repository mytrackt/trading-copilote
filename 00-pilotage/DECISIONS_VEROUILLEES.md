# DECISIONS VERROUILLEES — TRADEX-AI
> Source de vérité pour toutes les décisions stratégiques du projet.
> **RÈGLE** : Décisions prises par Cowork (débat avec Abdelkrim) → Claude Code enregistre sur instruction explicite de Cowork → Claude Code ne modifie jamais une décision de manière autonome.
> Toute modification = nouveau commit daté.

---

## FORMAT D'ENTRÉE

```
ID      : D-SXX-N (session + numéro)
Date    : JJ/MM/AAAA
Session : SXX
Décision: [intitulé court]
Détail  : [description complète]
Raison  : [pourquoi cette décision]
Impact  : [fichiers / modules concernés]
Statut  : VERROUILLÉ / SUSPENDU / REMPLACÉ PAR D-XXX
```

---

## DÉCISIONS FONDATRICES (pré-S30)

### D-F-01 — Méthode Belkhayate
**Date** : origine projet
**Décision** : Méthode Belkhayate exclusivement — intouchable
**Raison** : C'est le cœur de la stratégie d'Abdelkrim. Toute règle doit être compatible ou étiquetée Couche 2/3.
**Impact** : KB, cerveau IA, signaux, prompts
**Statut** : VERROUILLÉ

### D-F-02 — Architecture exécution
**Date** : origine projet
**Décision** : NinjaTrader 8 ATI — TCP/IP local port 36973
**Raison** : Seule plateforme utilisée par Abdelkrim. Pas d'alternative.
**Impact** : MODULE 00, MODULE 06
**Statut** : VERROUILLÉ

### D-F-03 — Règle d'entrée signal
**Date** : S06 — 13/06/2026
**Décision** : 3/4 actifs trading alignés ET 2/3 confirmation alignés = signal valide
**Raison** : Remplace l'ancienne règle 5/8 — plus précise, moins de faux signaux
**Impact** : engine/claude_brain.py, config/settings.py
**Statut** : VERROUILLÉ

### D-F-04 — Grille de scoring
**Date** : S06 — 13/06/2026
**Décision** : Grille déterministe /10. Seuil ≥ 7,0 + aucun critère éliminatoire
**Raison** : Remplace le score /21 — plus lisible, plus calibré Belkhayate
**Impact** : engine/claude_brain.py
**Statut** : VERROUILLÉ

### D-F-05 — Actifs tradables
**Date** : origine projet
**Décision** : TRADING = GC · HG · CL · ZW / CONFIRMATION = DX · ES · VX / RÉFÉRENCE = MBT · 6J (jamais d'ordre)
**Raison** : Classification définitive validée par Abdelkrim
**Impact** : config/settings.py, tous les modules
**Statut** : VERROUILLÉ

### D-F-06 — Modèles IA verrouillés
**Date** : S24 — 24/06/2026
**Décision** : KB + signaux = claude-sonnet-4-6 / Transcription = gemini-2.5-flash (multimodal)
**Raison** : Gemini validé sur 3 vidéos (71Mo / 413Mo chunké / 157Mo) — seule méthode fiable avec synchro image-texte
**Impact** : gemini_transcriber.py, claude_brain.py
**Statut** : VERROUILLÉ

### D-F-07 — Mode AUTO bloqué par défaut
**Date** : origine projet
**Décision** : Mode AUTO strictement interdit tant que toutes les conditions ne sont pas remplies
**Raison** : Sécurité absolue — circuit breaker encore inactif
**Impact** : MODULE 06, tous les modules
**Statut** : VERROUILLÉ

---

## DÉCISIONS SESSION S30 (26/06/2026)

### D-S30-1 — R/R ZW (Blé)
**Date** : 26/06/2026
**Session** : S30
**Décision** : R/R minimum abaissé à 1:1,5 pour ZW uniquement (vs 1:2 pour GC/HG/CL)
**Raison** : ZW moins volatile, mouvements plus courts — exiger 1:2 élimine trop d'opportunités valides
**Impact** : config/settings.py, engine/risk_manager.py
**Statut** : VERROUILLÉ

### D-S30-2 — Structure signal 15 champs
**Date** : 26/06/2026
**Session** : S30
**Décision** : Signal enrichi — 15 champs obligatoires :
Type · Instrument · Timeframe · Contexte · Entrée · Invalidation · SL · TP · R/R · Taille · Score confiance · Score risque · Raisons pour · Raisons contre · Décision système
**Raison** : Remplace le signal basique (ACHETER/VENDRE/ATTENDRE + %). Plus explicable, auditable, journalisable.
**Impact** : engine/claude_brain.py — MODULE 01
**Statut** : VERROUILLÉ

### D-S30-3 — 10 prompts spécialisés
**Date** : 26/06/2026
**Session** : S30
**Décision** : Remplacer le prompt monolithique par 10 prompts ciblés :
1. Analyse marché · 2. Génération scénario · 3. Refus trade · 4. Audit post-trade
5. Psychologie/discipline · 6. Rapport quotidien · 7. Risk check · 8. Amélioration stratégie
9. Décision instantanée frontend · 10. Prompt système général
**Raison** : Moins de tokens, plus précis, plus cheap. Prompt monolithique = gaspillage.
**Impact** : engine/claude_brain.py — MODULE 01
**Statut** : VERROUILLÉ

### D-S30-4 — Mémoire opérationnelle
**Date** : 26/06/2026
**Session** : S30
**Décision** : 10 types de mémoires runtime distinctes de la KB Belkhayate :
marchés observés · signaux générés · trades simulés · décisions humaines · erreurs
stratégies · conditions marché · faux signaux · bons signaux · comportements dangereux
**Raison** : La KB = règles statiques Belkhayate. La mémoire opérationnelle = apprentissage live. Deux choses différentes.
**Impact** : engine/memory_manager.py (à créer) — MODULE 04
**Statut** : VERROUILLÉ

### D-S30-5 — Risque par trade explicite
**Date** : 26/06/2026
**Session** : S30
**Décision** : 0,25% minimum — 0,50% maximum du capital par trade (paper et réel)
**Raison** : Règle absente de CLAUDE.md. Comble un vide critique pour la gestion du risque débutant.
**Impact** : engine/risk_manager.py — MODULE 02
**Statut** : VERROUILLÉ

### D-S30-6 — Strategy Lab
**Date** : 26/06/2026
**Session** : S30
**Décision** : Fiches stratégie avec statuts active/test/suspendue/rejetée + historique versions + critères d'activation stricts
**Raison** : Permet de tester, versionner et suspendre les stratégies sans risque.
**Impact** : MODULE 05 — phase ultérieure
**Statut** : VERROUILLÉ (implémentation différée)

### D-S30-7 — Architecture construction modulaire
**Date** : 26/06/2026
**Session** : S30
**Décision** : 7 modules CDC indépendants (MODULE 00 → 06) + CLAUDE.md allégé + DECISIONS_VEROUILLEES.md séparé
**Raison** : CLAUDE.md trop long → saturation contexte Claude Code. Modules autonomes = sous-agents focalisés.
**Impact** : Tout le projet — gouvernance
**Statut** : VERROUILLÉ

### D-S30-8 — Règles de gouvernance des fichiers
**Date** : 26/06/2026
**Session** : S30
**Décision** :
- DECISIONS_VEROUILLEES.md : Cowork ÉCRIT, Claude Code LIT uniquement
- MODULE_XX.md : max 200 lignes (sinon découper en sous-modules)
- Branching : feature/module-XX → merge vers main après tests
- Sub-agent échec : log obligatoire → rollback → Cowork averti
**Raison** : Éviter la reproduction des problèmes de CLAUDE.md (trop long, tout mélangé)
**Impact** : Processus de développement
**Statut** : VERROUILLÉ

### D-S30-9 — Transcriptions sources
**Date** : 26/06/2026
**Session** : S30
**Décision** : Trading Geek Whisper → archivés (_archive/trading-geek-whisper-elimine/). 203 vidéos → re-transcrire avec Gemini multimodal (batch_gemini.py)
**Raison** : Whisper = audio uniquement, pas de synchro image-texte. Gemini = multimodal, voit les charts.
**Impact** : 03-transcriptions/, MODULE 01 (bloqué jusqu'à fin transcriptions)
**Statut** : VERROUILLÉ — batch en cours

### D-S30-10 — Mémoire opérationnelle enrichie (remplace D-S30-4)
**Date** : 26/06/2026
**Session** : S30
**Décision** : Pour chacun des 10 types de mémoire, spécifier obligatoirement : données à enregistrer · importance · utilisation pour amélioration · erreurs à éviter · durée de conservation · indicateurs à calculer
**Raison** : D-S30-4 définissait les 10 types sans détail — insuffisant pour l'implémentation
**Impact** : engine/memory_manager.py — MODULE 04
**Remplace** : D-S30-4 (enrichissement, pas remplacement de fond)
**Statut** : VERROUILLÉ

### D-S30-11 — Taxonomie 20 erreurs détectables
**Date** : 26/06/2026
**Session** : S30
**Décision** : L'application détecte et gère 20 types d'erreurs :
1. Signal trop tôt · 2. Signal trop tard · 3. Mauvaise tendance · 4. Mauvais range
5. Mauvaise zone entrée · 6. Stop mal placé · 7. TP irréaliste · 8. R/R insuffisant
9. Confiance excessive · 10. Volatilité dangereuse · 11. Contre tendance forte
12. Multi-timeframe ignoré · 13. Sur-trading · 14. Revenge trading · 15. Entrée impulsive
16. Sortie prématurée · 17. Non-respect du plan · 18. Mauvaise taille position
19. Mauvaise gestion série pertes · 20. Répétition stratégie inefficace
Pour chaque erreur : détection + mesure + affichage + prévention + alerte + règle sécurité
**Impact** : engine/error_tracker.py (à créer) — MODULE 04
**Statut** : VERROUILLÉ

### D-S30-12 — Optimisation contrôlée (15 critères)
**Date** : 26/06/2026
**Session** : S30
**Décision** : Toute optimisation doit respecter 10 règles (données suffisantes → backtest → paper trading → comparaison version précédente → explication → versionnement → annulable → validation humaine → règles risque jamais assouplies automatiquement → stratégie instable rejetée) ET analyser 15 critères (win rate · R/R moyen · profit factor · drawdown · nb trades · stabilité périodes · stabilité marchés · comportement volatil · faux signaux · perte max · série pertes · qualité entrées · qualité sorties · respect plan · robustesse hors échantillon)
**Raison** : Empêcher toute auto-modification dangereuse de la stratégie
**Impact** : engine/optimizer.py (à créer) — MODULE 05
**Statut** : VERROUILLÉ

### D-S30-13 — Frontend 7 blocs précis (gate MODULE 03)
**Date** : 26/06/2026
**Session** : S30
**Décision** : Écran "Décision instantanée" composé de 7 blocs obligatoires :
BLOC 1 : Verdict immédiat (ACHAT / VENTE / ATTENDRE / DANGEREUX / REFUSÉ)
BLOC 2 : Score global (confiance · risque · contexte · stratégie · timing)
BLOC 3 : Plan du trade (entrée · SL · TP · R/R · taille · perte max)
BLOC 4 : 3 raisons POUR le signal uniquement
BLOC 5 : 3 raisons CONTRE le signal uniquement
BLOC 6 : Checklist 8 points (tendance · zone · ratio · risque · sur-trading · revenge · confirmation · plan)
BLOC 7 : 5 boutons (Simuler · Journal · Surveillance · Refuser · Analyse détaillée)
Aucun bouton d'ordre réel. Logique couleurs : vert/orange/rouge/gris/bleu/noir.
**Raison** : Décision en moins de 5 secondes sans surcharge cognitive
**Impact** : MODULE 03 — prérequis : Sujet 1 (discussion frontend) doit être validé avant
**Statut** : VERROUILLÉ

### D-S30-14 — Module Anti-Répétition des Erreurs
**Date** : 26/06/2026
**Session** : S30
**Décision** : Nouveau module dédié : identifier erreurs répétées → calculer fréquence → mesurer coût → afficher impact → déclencher alertes → bloquer comportements → forcer pause → proposer règle corrective → vérifier correction → rapport hebdomadaire
**Raison** : Transforme l'app en système apprenant — évite de répéter indéfiniment les mêmes fautes
**Impact** : engine/anti_repetition.py (à créer) — MODULE 05
**Statut** : VERROUILLÉ

### D-S30-15 — 8 types de rapports d'apprentissage
**Date** : 26/06/2026
**Session** : S30
**Décision** : L'application génère 8 types de rapports :
1. Post-trade · 2. Quotidien · 3. Hebdomadaire · 4. Mensuel
5. Par stratégie · 6. Par type de marché · 7. Par erreur · 8. Par niveau de risque
Chaque rapport répond à 10 questions fixes (ce qui a marché · échoué · erreur répétée · stratégie améliorée · stratégie dégradée · comportement dangereux · règle à renforcer · décision à éviter · amélioration à tester · conclusion session)
**Raison** : TRADEX-AI n'avait que le rapport quotidien — couverture insuffisante
**Impact** : engine/report_generator.py (à créer) — MODULE 04 + MODULE 05
**Statut** : VERROUILLÉ

### D-S30-16 — Strategy Lab enrichi (remplace D-S30-6)
**Date** : 26/06/2026
**Session** : S30
**Décision** : Strategy Lab passe à 20 champs par fiche + 18 fonctionnalités :
20 champs : nom · hypothèse · entrée · sortie · SL · TP · R/R min · conditions favorables · conditions dangereuses · win rate · drawdown max · nb trades testés · perf backtest · perf paper trading · stabilité · confiance · date modif · historique versions · raisons améliorations · verdict (active/test/suspendue/rejetée)
18 fonctionnalités : création · description · entrée · sortie · invalidation · marchés · timeframes · indicateurs · contexte idéal · contextes interdits · backtesting · paper trading · comparaison · scoring robustesse · détection surapprentissage · versionnement · validation humaine · désactivation automatique si dégradée
**Raison** : D-S30-6 avait 8 champs — insuffisant pour gérer des stratégies sérieusement
**Impact** : MODULE 05 — Strategy Lab
**Remplace** : D-S30-6
**Amendement S30 (26/06/2026)** : Désactivation automatique = SEULEMENT sur seuil fort validé :
- Drawdown stratégie > seuil configuré dans settings.py (ex: -15%)
- OU série de N pertes consécutives > seuil configuré (ex: 5 trades perdants)
Désactivation automatique → alerte immédiate obligatoire vers Abdelkrim → réactivation manuelle uniquement (jamais automatique).
Activation initiale : validation humaine toujours requise.
**Statut** : VERROUILLÉ

### D-S30-17 — 15 prompts fusionnés (Option B — remplace D-S30-3)
**Date** : 26/06/2026
**Session** : S30
**Décision** : 15 prompts finaux (12 fusionnés doc 1+2 + 3 garde-fous sécurité récupérés de D-S30-3) :
1. Prompt système général
2. Analyse marché (contexte + 7 Cercles)
3. Génération scénario conditionnel
4. Risk check (garde-fous avant signal)
5. Refus de trade (pédagogique)
6. Décision instantanée frontend (5 secondes)
7. Audit post-trade (scénario prévu vs résultat réel)
8. Détection erreurs répétées
9. Amélioration + comparaison versions stratégie
10. Validation avant activation stratégie
11. Suspension stratégie dangereuse
12. Rapport (quotidien / hebdo / mensuel selon paramètre)
13. Fallback local (confiance plafonnée 65% — mode Auto INTERDIT)
14. Discipline 3e trade (alerte sur-trading — blocage si VIX > seuil)
15. Contexte VIX élevé (marché dangereux — réduction taille, signal prudence)
**Raison** : Option B — les prompts 13/14/15 sont des garde-fous de sécurité critiques, jamais des doublons. Coût tokens = 0 (déclenchés uniquement sur condition spécifique).
**Impact** : engine/claude_brain.py — MODULE 01
**Remplace** : D-S30-3
**Statut** : VERROUILLÉ

---

## DÉCISIONS SESSION S31 (26/06/2026)

### D-S31-1 — Signal enrichi 18 champs (remplace D-S30-2)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Signal passe de 15 à 18 champs obligatoires.
15 champs D-S30-2 conservés :
Type · Instrument · Timeframe · Contexte · Entrée · Invalidation · SL · TP · R/R · Taille · Score confiance · Score risque · Raisons pour · Raisons contre · Décision système
3 champs ajoutés (PROMPT MAITRE Section 5) :
16. Probabilité qualitative (faible / moyen / fort — langage humain, pas numérique)
17. Conditions qui annulent le signal (triggers d'invalidation dynamiques post-émission)
18. Message pédagogique débutant (explication simple du signal en 1-2 phrases)
**Raison** : Champ 16 = lisibilité humaine. Champ 17 = gestion dynamique signal actif. Champ 18 = formation en contexte réel.
**Impact** : engine/claude_brain.py — MODULE 01 — MODULE 03 (frontend)
**Remplace** : D-S30-2
**Statut** : VERROUILLÉ

### D-S31-2 — 16 prompts (remplace D-S30-17)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Passer de 15 à 16 prompts. Les 15 de D-S30-17 sont conservés intégralement.
Ajout du Prompt 16 :
16. Formation progressive (explication didactique du concept trading détecté dans le signal — adapte le niveau au débutant, s'enrichit au fil des sessions)
**Raison** : D-S30-17 couvre l'analyse et les garde-fous. Le Prompt 16 couvre la formation en contexte — absent de tous les prompts existants.
**Impact** : engine/claude_brain.py — MODULE 01
**Remplace** : D-S30-17
**Statut** : VERROUILLÉ

### D-S31-3 — Règles de risque journalier, hebdomadaire et comportemental
**Date** : 26/06/2026
**Session** : S31
**Décision** : Compléter D-S30-5 (risque par trade) avec les règles de risque globales suivantes :
1. Risque max par JOUR : configurable settings.py (valeur par défaut proposée : -1% capital)
2. Risque max par SEMAINE : configurable settings.py (valeur par défaut proposée : -2% capital)
3. Nombre max de trades par JOUR : configurable settings.py (valeur par défaut proposée : 3 trades)
4. Kill switch : blocage automatique de la session si perte max/jour atteinte → réactivation manuelle uniquement
5. Mode pause obligatoire : déclenché après N pertes consécutives (N configurable settings.py)
6. Interdiction de martingale : taille de position ne peut JAMAIS être augmentée après une perte
7. Interdiction d'augmenter la taille en cours de trade perdant
**Raison** : D-S30-5 protège le trade individuel. D-S31-3 protège la session, la journée et la semaine. Les deux sont complémentaires et indispensables pour un débutant.
**Impact** : engine/risk_manager.py — config/settings.py — MODULE 02
**Complète** : D-S30-5 (pas de remplacement — extension)
**Statut** : VERROUILLÉ

### D-S31-4 — Critères Go/No-Go formels par phase (A → L)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Chaque phase de la roadmap (A → L) dispose désormais de critères go/no-go formels structurés :
- Tableau de critères GO avec mesure concrète et seuil chiffré
- Conditions NO-GO bloquantes (une seule suffit à bloquer)
- Procédure rollback en cas de NO-GO
- Validation humaine obligatoire (Abdelkrim ✋) avant passage à la phase suivante
Format : voir section "CRITÈRES GO / NO-GO PAR PHASE" dans FEUILLE_DE_ROUTE.md
**Raison** : La roadmap avait des critères informels ou absents — impossible de savoir objectivement quand une phase est terminée. Les critères go/no-go rendent la progression vérifiable et non-contestable.
**Impact** : FEUILLE_DE_ROUTE.md — toutes les phases A → L
**Statut** : VERROUILLÉ

### D-S31-5 — News Gate gradué 3 zones (enrichit D-F-01 garde-fous)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Le News Gate passe de binaire à 3 zones distinctes :
ZONE 1 — 2h avant annonce critique (NFP/FOMC/CPI/EIA/OPEP+) : REDUCE_RISK → taille réduite 50% · signal de prudence affiché · aucun nouveau trade en taille pleine
ZONE 2 — 30 min avant annonce (inchangé) : BLOCAGE TOTAL → aucun signal · aucun ordre · prioritaire sur tout
ZONE 3 — Post-annonce : analyse de la surprise (scoring impact Section E D-S31-7) → si surprise élevée : zone de prudence variable 30–60 min · si surprise faible : retour normal après confirmation
Règle absolue : la Zone 2 (30 min blocage) est intouchable — jamais assouplie.
**Raison** : Le blocage binaire laissait sans protection les 2h précédant l'annonce et ignorait le post-annonce. La zone de surprise post-annonce est aussi dangereuse que l'annonce elle-même.
**Impact** : engine/risk_manager.py · engine/news_gate.py · MODULE 02
**Enrichit** : GARDE_FOUS.md (News Gate existant) — ne le remplace pas
**Statut** : VERROUILLÉ

### D-S31-6 — MODULE 07 "Agent Veille Macro" (4 sous-agents)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Création d'un nouveau module dédié MODULE 07 "Agent IA de Veille Macro & Actualités".
L'agent répond à une unique question : "Le contexte économique, financier ou politique actuel autorise-t-il une décision de trading, impose-t-il la prudence, ou rend-il le marché trop dangereux ?"
4 sous-agents distincts :
1. Collecteur : enrichit news_collector.py + macro_collector.py existants (sources officielles prioritaires : Fed, BCE, FRED, IMF · puis calendriers économiques · puis données marché · puis médias · réseaux sociaux = non fiables, jamais suffisants seuls)
2. Filtre de fiabilité : classe chaque info en 8 catégories (fait confirmé · donnée macro officielle · événement programmé · déclaration importante · rumeur non vérifiée · opinion analyste · signal de risque · bruit marché)
3. Scorer d'impact : 8 dimensions (D-S31-7)
4. Synthétiseur : produit le contexte macro structuré → cerveau IA principal (MODULE 01)
Règle absolue : cet agent ne trade PAS · ne produit PAS d'ordre · n'enrichit QUE le contexte.
8 moments de veille : avant ouverture · après statistiques · avant/après BC · avant séances US/EU/AS · synthèse fin de journée · actualité urgente · avant toute session trading Abdelkrim.
**Raison** : TRADEX avait news_collector.py + macro_collector.py sans intelligence — ils collectent sans filtrer ni scorer. Sans module veille, les signaux Belkhayate manquent du filtre macro essentiel.
**Impact** : MODULE 07 (à créer) · ARCHITECTURE_CONSTRUCTION.md · FEUILLE_DE_ROUTE.md
**Statut** : VERROUILLÉ

### D-S31-7 — Score d'impact macroéconomique 8 dimensions
**Date** : 26/06/2026
**Session** : S31
**Décision** : Chaque information macro reçoit un score sur 8 dimensions :
1. Impact marché : faible / moyen / élevé / critique
2. Fiabilité de la source : faible / moyen / élevé
3. Urgence : faible / moyen / élevé
4. Risque : faible / moyen / élevé
5. Surprise : attendu / légèrement surprenant / très surprenant
6. Direction potentielle : favorable / défavorable / neutre / ambigu
7. Actifs affectés : liste (GC · HG · CL · ZW · DX · ES · VX)
8. Durée probable impact : très court terme / intraday / plusieurs jours / structurel
Ce scoring alimente directement le champ "Score risque" du signal 18 champs (D-S31-1) et déclenche les zones D-S31-5 si impact = élevé ou critique.
L'agent doit pouvoir conclure : impact incertain ou contradictoire.
**Raison** : Le gate binaire actuel ignore la graduation du risque macro. Un CPI légèrement inférieur aux attentes ≠ une surprise FOMC majeure.
**Impact** : engine/macro_scorer.py (à créer) · MODULE 07 · MODULE 02
**Statut** : VERROUILLÉ

### D-S31-8 — Market Risk Alert (mode alerte rouge événements externes)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Mode spécial "Market Risk Alert" distinct du circuit breaker technique.
Se déclenche sur 8 conditions externes (≥ 1 suffit) :
1. Décision majeure banque centrale
2. Donnée économique très différente des attentes (score surprise = très surprenant)
3. Crise politique ou géopolitique
4. Volatilité anormale détectée (VIX spike)
5. Cassure violente d'un niveau majeur sur actif suivi
6. Spreads augmentent fortement
7. Marchés illisibles (corrélations habituelles cassées)
8. Plusieurs sources fiables (niveau 1-2) confirment un événement dangereux
Actions quand activé :
- Alerte rouge affichée sur tous les écrans (UI)
- Score de confiance de tous les signaux actifs réduit automatiquement
- Blocage des trades à risque élevé ou critique
- Recommandation ATTENDRE en langage simple
- Confirmation humaine renforcée obligatoire pour tout signal
- Journalisation de l'événement
- Synthèse post-événement générée automatiquement
Désactivation : manuelle par Abdelkrim uniquement (jamais automatique).
**Raison** : Le circuit breaker couvre les pannes techniques. Ce mode couvre les chocs externes — deux choses distinctes.
**Impact** : engine/market_risk_alert.py (à créer) · MODULE 02 · MODULE 07
**Statut** : VERROUILLÉ

### D-S31-9 — 14 prompts internes Agent Veille Macro (distincts des 16 prompts trading)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Le MODULE 07 dispose de 14 prompts internes DISTINCTS des 16 prompts du cerveau trading (D-S31-2). Total système : 30 prompts (16 trading + 14 veille).
14 prompts veille :
1. Prompt système Agent IA de Veille Macro
2. Prompt de collecte quotidienne
3. Prompt de filtrage des actualités (8 catégories)
4. Prompt de classement par impact (8 dimensions)
5. Prompt de détection des risques politiques/géopolitiques
6. Prompt d'analyse des banques centrales
7. Prompt d'analyse des données économiques (CPI, NFP, PIB, PMI...)
8. Prompt de synthèse pré-marché
9. Prompt d'alerte événement critique (Market Risk Alert)
10. Prompt d'intégration avec le cerveau IA de trading
11. Prompt de rapport post-événement
12. Prompt d'audit anti-hallucination de la veille
13. Prompt d'apprentissage de l'agent de veille
14. Prompt de résumé débutant (vulgarisation pour Abdelkrim)
Règles communes à tous les 14 prompts : jamais inventer une actualité · jamais sans source · toujours afficher date/heure · toujours distinguer fait/interprétation/hypothèse · toujours signaler les contradictions.
**Raison** : Les prompts veille ont une logique différente des prompts trading — ils traitent du contexte externe, pas des signaux techniques.
**Impact** : engine/veille_prompts.py (à créer) · MODULE 07
**Statut** : VERROUILLÉ

### D-S31-10 — Rapport quotidien de veille = 9e type de rapport (enrichit D-S30-15)
**Date** : 26/06/2026
**Session** : S31
**Décision** : D-S30-15 avait 8 types de rapports. Ajout d'un 9e type : "Rapport quotidien de veille macro".
12 éléments obligatoires :
1. Résumé économique du jour
2. Résumé financier du jour
3. Résumé politique/géopolitique du jour
4. Événements programmés importants
5. Événements imprévus importants
6. Actifs à surveiller (GC · HG · CL · ZW)
7. Actifs à éviter (et pourquoi)
8. Périodes horaires dangereuses (avec créneaux précis)
9. Niveau général de risque du marché (favorable / neutre / prudent / dangereux / illisible)
10. Opportunités potentielles (zones de surveillance uniquement — jamais de signal direct)
11. Points d'incertitude
12. Conclusion opérationnelle : marché favorable / prudent / dangereux / illisible
Format : lisible par un débutant + utile pour un trader. Produit chaque jour avant la première session.
**Raison** : Les 8 rapports existants couvrent les trades et la performance. Aucun ne couvre le contexte macro quotidien.
**Impact** : engine/report_generator.py · MODULE 07 · MODULE 04
**Enrichit** : D-S30-15 (passe de 8 à 9 types de rapports)
**Statut** : VERROUILLÉ

---

## DÉCISIONS SESSION S31 — SÉCURITÉ SPÉCIFIQUE TRADEX (26/06/2026)

### D-S31-11 — Validation plausibilité données NT8 (VULN 1 — Data poisoning)
**Date** : 26/06/2026
**Session** : S31
**Décision** : `data_reader.py` doit valider la plausibilité de chaque prix reçu avant de l'envoyer à `claude_brain.py`. Fourchettes par actif (valeurs indicatives — à affiner dans settings.py) :
- GC (Or) : entre 1 000 et 5 000 $/oz
- HG (Cuivre) : entre 1,5 et 8 $/lb
- CL (Pétrole) : entre 10 et 200 $/baril
- ZW (Blé) : entre 200 et 1 500 cents/boisseau
- DX (Dollar) : entre 70 et 130
- ES (SP500) : entre 1 000 et 10 000 points
- VX (VIX) : entre 5 et 90
Si un prix est hors fourchette → état BLOCKED immédiat · aucun signal · alerte Abdelkrim · log obligatoire.
Règle : une donnée hors fourchette n'est jamais ignorée silencieusement — c'est toujours soit une panne, soit une attaque.
**Raison** : staleness_monitor.py détecte les données périmées mais pas les données falsifiées récentes. Un flux NT8 corrompu génère de faux signaux sans déclenchement d'alarme.
**Impact** : engine/data_reader.py · config/settings.py (fourchettes configurables) · MODULE 00
**Statut** : VERROUILLÉ

### D-S31-12 — Intégrité KB : hash SHA256 + restauration + alerte malware (VULN 2)
**Date** : 26/06/2026
**Session** : S31
**Décision** : `claude_brain.py` calcule un hash SHA256 de `KNOWLEDGE_BASE_MASTER.json` à chaque démarrage et compare au hash de référence stocké dans `04-cerveau-trading\KB_HASH.txt` (fichier séparé, git-tracké).
Si hash identique → démarrage normal.
Si hash différent → 3 actions obligatoires dans cet ordre :
1. REFUS DE DÉMARRER — aucun signal possible tant que non résolu
2. RESTAURATION AUTOMATIQUE depuis la dernière version git (`git checkout HEAD -- 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json`)
3. ALERTE MALWARE — log horodaté dans `05-saas/logs/security_alert.log` + message clair à Abdelkrim : "⚠️ KB modifiée de façon non autorisée — restauration effectuée — vérifier présence malware"
Procédure post-alerte : lancer Kaspersky analyse complète avant tout redémarrage de TRADEX.
Hash de référence mis à jour uniquement après commit git validé (jamais automatiquement).
**Raison** : La KB est le cerveau de TRADEX. Une modification silencieuse de règles Belkhayate peut inverser tous les signaux sans alerte visible. La restauration automatique réduit le temps d'arrêt.
**Impact** : engine/claude_brain.py · 04-cerveau-trading/KB_HASH.txt (à créer) · MODULE 01
**Statut** : VERROUILLÉ

### D-S31-13 — Port 36973 NT8 ATI : localhost uniquement (VULN 3)
**Date** : 26/06/2026
**Session** : S31
**Décision** : La connexion NT8 ATI doit écouter exclusivement sur `127.0.0.1` (localhost), jamais sur `0.0.0.0` (toutes interfaces).
Vérification obligatoire dans `nt8_ati_client.py` au démarrage : tenter une connexion sur `127.0.0.1:36973` uniquement. Si NT8 répond sur une autre interface → log d'alerte + BLOCKED.
Test de validation Phase G : scanner les interfaces NT8 avec `netstat -ano | findstr 36973` — vérifier que seul `127.0.0.1:36973` apparaît, jamais `0.0.0.0:36973`.
**Raison** : Un port ouvert sur `0.0.0.0` est accessible depuis tout appareil du réseau local (téléphone, TV connectée, PC tiers). N'importe quel appareil pourrait envoyer de faux ordres à NinjaTrader en imitant TRADEX.
**Impact** : engine/nt8_ati_client.py · MODULE 06 · tests Phase G
**Statut** : VERROUILLÉ

### D-S31-14 — Anti-prompt injection MODULE 07 (VULN 4)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Tout contenu externe collecté par le MODULE 07 (actualités Finnhub, GDELT, Reuters, etc.) doit être désinfecté AVANT insertion dans un prompt Claude.
Filtre obligatoire dans `veille_filter.py` :
1. Supprimer les balises d'instruction : "ignore", "oublie", "nouvelle instruction", "system:", "assistant:", "[INST]" et équivalents
2. Limiter chaque information à 500 caractères maximum
3. Wrapper tout contenu externe dans des balises XML de données : `<external_data>...</external_data>` — jamais dans le corps du prompt d'instruction
4. Logger toute information filtrée (contenu suspect + source + timestamp)
Si une information déclenche 2 filtrages ou plus → source mise en quarantaine pour la session.
**Raison** : Les LLM sont vulnérables aux prompt injections indirectes — un acteur malveillant peut publier une "actualité" contenant des instructions pour manipuler Claude. Documenté et exploité en conditions réelles.
**Impact** : engine/veille_filter.py · MODULE 07
**Statut** : VERROUILLÉ

### D-S31-15 — Synchronisation NTP au démarrage (VULN 5)
**Date** : 26/06/2026
**Session** : S31
**Décision** : TRADEX vérifie la synchronisation de l'heure système via NTP à chaque démarrage, avant toute activation du News Gate.
Implémentation dans `engine/time_guard.py` (à créer) :
- Interroger `pool.ntp.org` (ou `time.windows.com` en fallback)
- Si écart heure système vs NTP > 60 secondes → BLOCKED · aucun signal · alerte Abdelkrim : "⚠️ Heure système désynchronisée — News Gate potentiellement inactif"
- Si NTP inaccessible (pas de réseau) → passer en mode dégradé : News Gate activé en permanence (NO_TRADE forcé) jusqu'à synchronisation confirmée
**Raison** : Le News Gate (D-S31-5) est basé sur `datetime.now()`. Une heure système manipulée ou désynchronisée peut contourner silencieusement le blocage 30 min avant NFP/FOMC/CPI.
**Impact** : engine/time_guard.py (à créer) · engine/risk_manager.py · MODULE 02
**Statut** : VERROUILLÉ

### D-S31-16 — Journal de trading append-only avec chaîne d'intégrité (VULN 6)
**Date** : 26/06/2026
**Session** : S31
**Décision** : Le journal de trading SQLite est en mode append-only avec chaîne d'intégrité.
Implémentation dans le schéma SQLite (table `trades` et table `journal`) :
- Chaque entrée contient un champ `entry_hash` = SHA256(contenu_entrée + hash_entrée_précédente)
- Aucune fonction UPDATE ou DELETE sur les entrées passées — uniquement INSERT
- Fonction de vérification `verify_journal_integrity()` dans `report_generator.py` : recompose la chaîne depuis la première entrée et compare — toute rupture = alerte
- La vérification s'exécute automatiquement à chaque génération de rapport (D-S31-10)
Si rupture de chaîne détectée → log security_alert.log + rapport marqué "⚠️ INTÉGRITÉ COMPROMISE — statistiques non fiables"
**Raison** : Avec de l'argent réel (Phase K), les statistiques de performance doivent être irréfutables. Un journal modifiable rend impossible la confiance dans les données d'apprentissage de TRADEX.
**Impact** : 05-saas/db/schema.sql · engine/report_generator.py · MODULE 04
**Applicable** : à implémenter avant Phase K (argent réel)
**Statut** : VERROUILLÉ

---

## DÉCISIONS EN ATTENTE DE VALIDATION

*(vide — toutes les décisions S31 sont validées)*

---

## DÉCISIONS REMPLACÉES / ABANDONNÉES

| ID ancien | Décision remplacée | Remplacée par | Date |
|---|---|---|---|
| Règle 5/8 | 5 actifs sur 8 alignés | D-F-03 (3/4 + 2/3) | S06 |
| Score /21 | Grille sur 21 points | D-F-04 (grille /10) | S06 |
| Prompt monolithique | 1 seul prompt cerveau | D-S30-3 (10 prompts) | S30 |
| D-S30-3 (10 prompts) | 10 prompts Option A | D-S30-17 (15 prompts Option B) | S30 |
| D-S30-6 Strategy Lab 8 champs | 8 champs fiche stratégie | D-S30-16 (20 champs + désactivation seuil) | S30 |
| D-S30-2 (15 champs signal) | 15 champs signal | D-S31-1 (18 champs) | S31 |
| D-S30-17 (15 prompts) | 15 prompts Option B | D-S31-2 (16 prompts) | S31 |

---

*Dernière mise à jour : 26/06/2026 — Session S31 — 16 décisions (D-S31-1 à D-S31-16)*
*Ce fichier est la mémoire décisionnelle de TRADEX-AI.*
