# BACKLOG ENRICHISSEMENTS — TRADEX-AI
> Eléments à intégrer dans les phases futures.
> Source : documents "solo founder" + "SaaS description" (session S05 — 11/06/2026)
> NE PAS modifier la FEUILLE_DE_ROUTE.md existante — ce fichier est le complément.

## États : 📥 À TRAITER · 🔍 PLAN PROPOSÉ · ⚙️ EN EXÉCUTION · ✅ AUDIT AUTO · 🔀 À FUSIONNER · 🟢 INTÉGRÉ
## Priorité : P1 (haute) → P3 (basse). Cowork traite P1 d'abord, 1 ticket par interstice.

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
