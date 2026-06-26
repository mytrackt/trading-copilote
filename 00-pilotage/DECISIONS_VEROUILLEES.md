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

---

## DÉCISIONS EN ATTENTE DE VALIDATION

*(vide — toutes les décisions S30 sont validées)*

---

## DÉCISIONS REMPLACÉES / ABANDONNÉES

| ID ancien | Décision remplacée | Remplacée par | Date |
|---|---|---|---|
| Règle 5/8 | 5 actifs sur 8 alignés | D-F-03 (3/4 + 2/3) | S06 |
| Score /21 | Grille sur 21 points | D-F-04 (grille /10) | S06 |
| Prompt monolithique | 1 seul prompt cerveau | D-S30-3 (10 prompts) | S30 |

---

*Dernière mise à jour : 26/06/2026 — Session S30*
*Ce fichier est la mémoire décisionnelle de TRADEX-AI.*
