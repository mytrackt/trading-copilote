# BACKLOG ENRICHISSEMENTS — TRADEX-AI
> Eléments à intégrer dans les phases futures.
> Source : documents "solo founder" + "SaaS description" (session S05 — 11/06/2026)
> NE PAS modifier la FEUILLE_DE_ROUTE.md existante — ce fichier est le complément.

## États : 📥 À TRAITER · 🔍 PLAN PROPOSÉ · ⚙️ EN EXÉCUTION · ✅ AUDIT AUTO · 🔀 À FUSIONNER · 🟢 INTÉGRÉ
## Priorité : P1 (haute) → P3 (basse). Cowork traite P1 d'abord, 1 ticket par interstice.

---

## 0. [S15 · 16/06/2026] CHAP01_Metier_Trader_Senior_v2_technique — P2 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\playbook\CHAP01_Metier_Trader_Senior_v2_technique.md`
**Source :** Google Docs (Abdelkrim) — contenu réel archivé (260 lignes, Markdown propre)
**Action à l'interstice :** pipeline KB étapes 3-7 (transcript_processor.py → validate → fusionner KB_VALIDEE.json)
**Catégories KB candidates :**
- `gestion_risque_entree` : stop-loss pré-entrée, risque 1% par trade, calcul ticks×valeur×contrats
- `psychologie` : processus écrit/répétable, discipline vs humeur, sur-trading, mythes débutant
- `gestion_position_active` : limite perte journalière, journal de trading, 90% attente / 10% action
- `indicateurs_tendance` : structure sommets/creux (Dow), multi-timeframe, support/résistance, fakeout/retest
- `indicateurs_momentum` : RSI — limites, piège "suracheté = va baisser", indicateur lagging vs leading
**Note :** Document éducatif général (pas Belkhayate-spécifique). Filtrer strictement les règles compatibles méthode Belkhayate lors du pipeline. Chiffres marqués *(illustratif)* = exemples → NE PAS intégrer comme règles KB chiffrées.

---

## 0.f [S16 · 17/06/2026] TRADEX_KB_Chap6_Approches_Universelles — P1 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap6_Approches_Universelles.md`
**Source :** Abdelkrim (document interne) — Chapitre 6 "Approches universelles complémentaires", cours Mentor Trader Senior
**Action à l'interstice :** pipeline KB étapes 3-7
**Catégories KB candidates :** `correlations`, `structure_marche`, `indicateurs_tendance`, `macro_evenements`
**Note :** Approches complémentaires à la méthode Belkhayate (VWAP, SMC, Wyckoff, inter-marchés probable). P1 car complète la série TRADEX KB et enrichit les 7 cercles d'intelligence.

---

## 0.e [S16 · 17/06/2026] TRADEX_KB_Chap3_Brokers_Plateformes — P2 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\playbook\TRADEX_KB_Chap3_Brokers_Plateformes.md`
**Source :** Abdelkrim (document interne) — Chapitre 3 "Brokers & plateformes : l'interaction concrète", version technique enrichie
**Action à l'interstice :** pipeline KB étapes 3-7
**Catégories KB candidates :** `gestion_risque_entree` (types d'ordres, slippage, marge), `macro_evenements` (heures de marché), `psychologie` (discipline d'exécution)
**Note :** Contenu opérationnel broker/plateforme (NinjaTrader, Rithmic). Filtrer ce qui est utile au moteur TRADEX (types d'ordres, règles ATI) vs ce qui est purement éducatif/débutant. P2 car moins Belkhayate-spécifique que Chap4/Chap5.

---

## 0.c [S16 · 17/06/2026] TRADEX_KB_Chap4_Analyse_Technique — P1 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap4_Analyse_Technique.md`
**Source :** Abdelkrim (document interne) — Chapitre 4 "Lire le prix : analyse technique", version technique enrichie avec légende fiabilité (🟢/🟡/🔵/🔴)
**Action à l'interstice :** pipeline KB étapes 3-7
**Catégories KB candidates :** `indicateurs_tendance` (VWAP, support/résistance, structure), `indicateurs_momentum`, `structure_marche`, `volume_liquidite`
**Note :** Série TRADEX KB — complémentaire Chap5 Belkhayate. Priorité P1 car directement lié à la lecture du prix dans TRADEX.

---

## 0.d [S16 · 17/06/2026] CHAP02_Fondamentaux_Futures — P2 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\playbook\CHAP02_Fondamentaux_Futures_v2_technique.md`
**Source :** Abdelkrim (document interne) — Chapitre 2 "Fondamentaux des marchés futures", version technique enrichie
**Action à l'interstice :** pipeline KB étapes 3-7
**Catégories KB candidates :** `gestion_risque_entree` (tick/point/marge CME), `structure_marche`, `macro_evenements`
**Note :** Fondamentaux généraux futures (GC/HG/CL/ZW). Filtrer strictement ce qui est Belkhayate-compatible. Les specs de contrat (tick/point) = vérifier CME officiel avant intégration KB.

---

## 0.b [S16 · 17/06/2026] TRADEX_KB_Chap5_Methode_Belkhayate — P1 · 📥 À TRAITER

**Fichier archivé :** `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap5_Methode_Belkhayate.md`
**Source :** Abdelkrim (document interne) — Chapitre 5 méthode Belkhayate, version technique enrichie avec légende fiabilité (🟢 FAIT / 🟡 CONVENTION / 🔵 ÉCOLE / 🔴 NON VÉRIFIÉ)
**Action à l'interstice :** pipeline KB étapes 3-7 (transcript_processor.py → validate → fusionner KB_VALIDEE.json)
**Catégories KB candidates :** `indicateurs_tendance` (COG, pivots, Direction), `structure_marche`, `timing`, `gestion_risque_entree`, `indicateurs_momentum`
**Note :** Document déjà annoté avec niveaux de fiabilité — filtrer strictement les 🔴 NON VÉRIFIÉ (claims marketing, formules propriétaires non confirmées). Les 🟢 FAIT et 🔵 ÉCOLE sont intégrables directement. Priorité P1 car Belkhayate-spécifique.

---

## 1. JOURNAL DE TRADING IA COMPLET (à intégrer Phase I ou Phase I.4)

Chaque trade doit avoir une fiche complète dans SQLite :

| Champ | Description |
|-------|-------------|
| date | Horodatage exact |
| actif | GC / HG / CL / ZW |
| prix_entree | Prix d'entrée réel |
| prix_sortie | Prix de sortie réel |
| taille | Nombre de contrats |
| stop_loss | SL défini |
| take_profit | TP défini |
| frais | Commissions broker |
| resultat_pnl | PnL réalisé |
| decision_claude | Résumé raisonnement IA |
| validation_risk | OK / REFUSE + raison |
| score_7_cercles | Score /10 au moment du signal |
| contexte_marche | Snapshot indicateurs Belkhayate |
| raison_entree | Pourquoi le trade a été pris |
| raison_sortie | Pourquoi le trade a été fermé |
| erreurs | Anomalies détectées |
| lecon | Note manuelle Abdelkrim |

**Phase cible** : I.4 (après composants dashboard)
**Pourquoi** : audit complet de chaque décision IA — essentiel pour améliorer la stratégie

---

## 2. PROFIL DE RISQUE UTILISATEUR (à intégrer Phase H ou I)

Formulaire simple sauvegardé dans SQLite / settings :

- capital_total (MAD ou USD)
- perte_max_par_jour (% ou montant)
- perte_max_par_trade (% ou montant)
- nb_positions_max_ouvertes
- levier_max_autorise
- horaires_trading (ex: 09h-17h ET)
- validation_manuelle_obligatoire (bool)

**Phase cible** : H (FastAPI route /profile) + I (composant ProfileRisk)
**Pourquoi** : personnalise le moteur de risque selon les préférences réelles

---

## 3. MÉTRIQUES BACKTESTING COMPLÈTES (enrichir Phase E)

En plus du win rate et drawdown déjà prévus, ajouter :

- Profit Factor (gain total / perte totale — doit être > 1.5)
- Ratio Sharpe (rendement / volatilité — doit être > 1.0)
- Courbe de capital (graphique visuel)
- Pire drawdown consécutif
- Nombre de trades perdants consécutifs max
- Périodes difficiles identifiées

**Phase cible** : E (signal_scorer.py — enrichir walk_forward_validate)
**Pourquoi** : éviter overfitting et sélection artificielle des bonnes périodes

---

## 4. MODES DE TRADING EXPLICITES (enrichir Phase I)

Les 6 modes à afficher clairement dans le dashboard :

| Mode | Nom | Comportement |
|------|-----|-------------|
| 1 | Observation | Claude analyse, aucun signal |
| 2 | Signal uniquement | Affiche signaux, pas d'exécution |
| 3 | Validation manuelle | Abdelkrim confirme chaque trade |
| 4 | Semi-automatique | Exécute seulement trades pré-validés |
| 5 | Automatique contrôlé | Mode AUTO dans limites strictes |
| 6 | Emergency Lock | TOUT bloqué, positions fermées |

**Phase cible** : I (composant ModeExecution — déjà prévu, enrichir avec ces 6 niveaux)
**Actuellement** : seulement MANUEL / AUTO — ajouter les niveaux intermédiaires

---

## 5. SÉCURITÉ AVANCÉE (à intégrer Phase H)

Items manquants dans la roadmap actuelle :

- Protection contre injection de prompt (valider sortie JSON Claude avant usage)
- Rotation des secrets (renouveler ANTHROPIC_API_KEY tous les 90 jours — rappel automatique)
- Logs immuables (append-only, jamais de delete sur signal_history.json)
- Rate limiting renforcé sur FastAPI (max 10 req/s)
- Détection activité anormale (> 5 signaux/heure = alerte + lock)

**Phase cible** : H (FastAPI) + F (trade_validator)

---

## 6. CHECKLIST DE VALIDATION PAR PHASE (méthodologie)

À la fin de chaque phase, vérifier avant de passer à la suivante :

```
[ ] Le code compile sans erreur (py_compile)
[ ] Les données s'affichent correctement
[ ] Aucun ordre réel envoyé (si pas encore Phase G)
[ ] Les logs sont lisibles
[ ] Le système peut être arrêté proprement
[ ] Git commit fait avec message conventionnel
[ ] README_TRANSITION généré
```

**Application** : systématique à partir de Phase C-02

---

## 7. AVERTISSEMENTS OBLIGATOIRES (Phase I — Dashboard)

Afficher en permanence (non fermables) :

- "⚠️ Ce système est un outil d'analyse personnel. Il ne constitue pas un conseil financier."
- "⚠️ Le trading comporte des risques. Vous pouvez perdre tout votre capital."
- "⚠️ Usage strictement personnel — non distribué à des tiers (conformité AMMC Maroc)."
- Statut MODE AUTO (BLOQUÉ en rouge / ACTIF en orange avec countdown)

---

## 8. PROGRESSION OBLIGATOIRE AVANT MODE AUTO (rappel)

Ne pas brûler les étapes :

```
1. Données fictives (CSV statique)   ← on est ici (Phase C-01 terminée)
2. Signaux fictifs (KB + test)       ← Phase D
3. Journal manuel                    ← Phase I.4
4. Paper trading                     ← Phase J (30 jours)
5. Lecture seule broker              ← Phase G (validation)
6. Exécution manuelle                ← Phase G + K
7. Semi-automatique                  ← Phase K (après 6 conditions)
8. Automatisation limitée            ← Phase K (validée)
```

---

*BACKLOG_ENRICHISSEMENTS.md — créé S05 11/06/2026*
*Source : documents "solo founder guidelines" + "SaaS description exhaustive"*
*À consulter lors de la conception de chaque phase*
