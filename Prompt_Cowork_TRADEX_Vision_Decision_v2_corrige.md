MISSION : Ajouter à la feuille de route TRADEX-AI la Phase "Vision-Décision Temps Réel" — architecture hybride 5 couches connectant NinjaTrader 8 à TRADEX-AI, avec garde-fous trading complets.

═══════════════════════════════════════════════════
CONTEXTE
═══════════════════════════════════════════════════
TRADEX-AI est un copilote de trading DÉCISIONNEL (méthode Belkhayate) basé à C:\trading-copilote\.
La KB locale (ChromaDB + Ollama + nomic-embed-text + Mistral) est en cours de construction.
Le COG Belkhayate est déjà porté en C# (NinjaTrader) et en Python.

RÈGLE ABSOLUE NON CONTOURNABLE :
TRADEX est un outil d'aide à la décision UNIQUEMENT. AUCUNE exécution automatique d'ordre.
La sortie finale n'est jamais un ordre, toujours une recommandation soumise à validation humaine.

PROBLÈME RÉSOLU PAR CETTE PHASE :
Mistral local lit du texte, pas les charts NinjaTrader. Objectif : permettre à TRADEX
de "voir" les graphiques en quasi temps réel SANS screenshot manuel, de façon automatique.

INSIGHT ARCHITECTURAL CLÉ :
Ne pas photographier l'écran. Se brancher sur le FLUX DE DONNÉES NUMÉRIQUE de NinjaTrader.
NinjaTrader connaît déjà les valeurs exactes (OHLCV, COG, ADX). Lire les nombres, pas les pixels.

═══════════════════════════════════════════════════
ARCHITECTURE CIBLE — 5 COUCHES (assignation par rôle)
═══════════════════════════════════════════════════

COUCHE 0 — SOURCE (NinjaTrader 8, C# / NinjaScript)
- Add-on NinjaScript qui lit en direct OHLCV + COG Belkhayate + ADX à chaque bougie (OnBarUpdate)
- Pousse les données en JSON sur un canal local (WebSocket ou HTTP localhost)
- DÉMARRAGE PROGRESSIF : d'abord export CSV simple, puis socket temps réel une fois validé

COUCHE 1 — INGESTION (FastAPI local, Python)
- Reçoit le flux de bougies en temps réel depuis NinjaTrader
- Latence cible < 50 ms (à mesurer et valider, pas supposée)
- Stocke un buffer glissant des N dernières bougies
- CIRCUIT BREAKER intégré : si dernière donnée reçue > X secondes (paramétrable) OU Internet coupé
  → état forcé NO_TRADE. Aucune décision produite tant que le feed n'est pas rétabli.

COUCHE 2 — DÉTECTION ALGORITHMIQUE (Python pur)
- Détecte les patterns sur les NOMBRES (pas l'image) via règles géométriques :
  swing highs/lows, triangles, flags, double top/bottom, H&S, S/R, trendlines
- Utilise les 20 patterns ChartSchool extraits comme RÈGLES DE VALIDATION
- Produit un SCORE DE CONFIANCE chiffré (0-100%) pour chaque pattern détecté
- 0 €, instantané, déterministe. Couvre ~80% des cas sans LLM.
- SEUIL DE BASCULE VERS VISION : si score de confiance < 70% (paramétrable) → déclenche Couche 4 vision.
  Si score ≥ 70% → pattern considéré comme clair, pas d'appel vision nécessaire.

COUCHE 3 — RAG / KB BELKHAYATE (Mistral local via Ollama + ChromaDB)
- Interroge la KB : critères de validité d'un pattern, règles Belkhayate, Donchian, Rhodes, biais cognitifs
- Contient déjà les règles psychologie/discipline : anti-revenge (Rhodes R13), Hot-Hand (série +3 → réduction taille), anti-FOMO
- 100% local, gratuit, illimité, privé
- Répond aux questions de connaissance pure (ex : "critères d'un flag valide ?")

COUCHE 4 — VISION + DÉCISION FINALE (Claude API, claude-sonnet-4-6)
- DÉCLENCHÉE, JAMAIS EN CONTINU. Appelée uniquement quand :
  * la détection algo (couche 2) a un score de confiance < 70%
  * un signal est généré et nécessite confirmation visuelle avant validation
- Volume estimé : 5-20 appels/jour (cohérent avec 5-20 signaux/jour)
- Budget cible : 20-50 $/mois
- RATE LIMITER + CIRCUIT BREAKER COÛT : hard stop à N appels Claude/jour (paramétrable, ex : 30/jour).
  Au-delà → état NO_TRADE, alerte à l'utilisateur. Protège le budget mensuel.

  AVANT toute décision, la couche 4 applique OBLIGATOIREMENT dans cet ordre :

  1. NEWS GATE (obligatoire)
     - Vérifier événement macro imminent sur CL/GC/ES : EIA/API (pétrole), FOMC/Fed/CPI/PCE/NFP (or/indices), OPEP+ (pétrole), géopolitique majeure
     - News critique imminente → NO_TRADE
     - Réaction post-news non digérée → WAIT
     - News moyenne → REDUCE_RISK
     - Circuit breaker marché (SPX -7/-13/-20%) → NO_TRADE immédiat

  2. CONTEXTE INTERMARCHÉ + COT (qualification, pas trigger)
     - COT = CONTEXTE HEBDOMADAIRE UNIQUEMENT. Décalage CFTC ~3 jours ouvrés.
       INTERDIT comme déclencheur intraday. Sert uniquement à qualifier le biais de fond.
     - Qualifier le régime (risk-on / risk-off / stress) à partir des données fournies, sinon marquer NON VÉRIFIABLE

  3. CROISEMENT DÉCISIONNEL
     - Pattern détecté (couche 2) + COG Belkhayate + KB (couche 3) + contexte macro/COT
     - Imposer : niveau d'invalidation défini, stop-loss défini AVANT entrée, taille calculée selon le stop,
       R/R minimum ≥ 1.5, scénario opposé étudié

  4. COÛTS RÉELS (intégrés au format de sortie)
     - Spread (XAUUSD/GC élargi à 3h UTC), slippage estimé, commissions, gap weekend (réouverture dimanche soir CL/GC/ES),
       dates de rollover futures (GC/CL/ES — préciser par contrat actif)

  5. EXECUTION GATEKEEPER (sortie obligatoire)
     - État par défaut = NO_TRADE. Le système ne propose TRADE_ALLOWED que si TOUTES les conditions ci-dessus sont réunies.
     - Sortie standardisée : NO_TRADE / WAIT / REDUCE_RISK / TRADE_ALLOWED
     - Si TRADE_ALLOWED : direction + sizing + stop + R/R + scénario d'invalidation + coûts estimés
     - La vision est une CONFIRMATION, jamais sur le chemin critique du tick (incompatible scalping sinon)

COUCHE TRANSVERSALE — AUDIT & MONITORING
- AUDIT LOG : historiser chaque décision IA (entrées des 4 couches + sortie gatekeeper + timestamp)
- MONITORING / ALERTING : health check des 5 couches, alerte si un module tombe
- MODEL VERSION CONTROL : versions Mistral + Claude gelées et loguées

═══════════════════════════════════════════════════
RÈGLE DE RÉPARTITION DES MODÈLES (à documenter dans la feuille de route)
═══════════════════════════════════════════════════
- Détection patterns (nombres)  → Python algo      (0 €, local, score de confiance)
- KB Belkhayate (texte)         → Mistral local    (0 €, local)
- Vision charts (image)         → Claude API       (payant, déclenché si confiance < 70%)
- Décision finale (croisement)  → Claude API       (payant, 1 appel/signal validé)

═══════════════════════════════════════════════════
FICHIERS À CRÉER (à lister dans la roadmap)
═══════════════════════════════════════════════════
1. Add-on NinjaScript C# : export données NinjaTrader → canal local
2. Service FastAPI d'ingestion du flux + circuit breaker feed
3. Module Python de détection algorithmique de patterns + score de confiance
4. Connecteur Mistral local (requête KB ChromaDB)
5. Connecteur Claude API (vision + décision) + rate limiter + circuit breaker coût
6. Module News Gate (calendrier événements CL/GC/ES)
7. Module Execution Gatekeeper (NO_TRADE/WAIT/REDUCE_RISK/TRADE_ALLOWED)
8. Module Audit Log + Monitoring
9. Prompt système couche vision (lecture chart structurée)
10. Prompt système couche décision (croisement multi-facteurs Belkhayate + garde-fous)
11. Format JSON standardisé d'échange entre les 5 couches

═══════════════════════════════════════════════════
PLAN DE VALIDATION (tests de fiabilité)
═══════════════════════════════════════════════════
1. Détection algo : tourner sur 50 bougies historiques CL → vérifier swing points + patterns + score de confiance
2. Circuit breaker : couper le feed → vérifier passage automatique en NO_TRADE
3. RAG Mistral : 10 questions Belkhayate → vérifier récupération des bons passages KB
4. Vision Claude : 5 screenshots → comparer identification vs détection algo (divergences = zones ambiguës)
5. News Gate : simuler un FOMC imminent → vérifier sortie NO_TRADE
6. Gatekeeper : 1 signal avec stop manquant → vérifier refus (NO_TRADE par défaut)
7. Décision complète : 1 signal réel passé dans les 5 couches → vérifier cohérence + présence des coûts réels
8. Rate limiter : simuler 31 appels → vérifier hard stop au seuil

═══════════════════════════════════════════════════
OBSTACLES ANTICIPÉS + PARADES
═══════════════════════════════════════════════════
- Add-on C# à développer       → commencer par export CSV avant socket temps réel
- Détection algo rate des cas  → Claude vision en filet de sécurité si confiance < 70%
- Coût API Claude monte        → rate limiter hard stop N appels/jour + cache décisions similaires
- Internet tombe               → circuit breaker → NO_TRADE ; Mistral + algo local en mode dégradé
- Latence vision vs scalping   → vision = confirmation uniquement, hors chemin critique du tick
- News surprise (event surprise)→ news gate + état NO_TRADE par défaut si event non digéré
- COT mal utilisé              → contrainte explicite : contexte hebdo uniquement, jamais trigger intraday

═══════════════════════════════════════════════════
DÉPENDANCES (ordre obligatoire)
═══════════════════════════════════════════════════
- La KB TRADEX-AI doit être COMPLÈTE avant d'implémenter les couches 3 et 4
  (la décision n'a de valeur que si la connaissance Belkhayate est solide)
- Couche 0 (NinjaScript) et Couche 2 (détection algo) peuvent démarrer en parallèle
- News Gate et Execution Gatekeeper doivent être opérationnels AVANT le premier test de décision réelle
- Ordre d'implémentation : Couche 0 → 1 (+ circuit breaker) → 2 → 3 → 6 (news gate) → 7 (gatekeeper) → 4 → 8 (audit/monitoring)

═══════════════════════════════════════════════════
ACTION DEMANDÉE
═══════════════════════════════════════════════════
1. Ajouter cette Phase "Vision-Décision Temps Réel" (5 couches + couche transversale) à la feuille de route TRADEX-AI
2. Documenter la règle de répartition des modèles (tableau ci-dessus)
3. Lister les 11 fichiers à créer comme sous-tâches
4. Marquer les dépendances : KB complète AVANT couches 3-4 ; News Gate + Gatekeeper AVANT test décision réelle
5. Confirme l'ajout et affiche la feuille de route mise à jour
