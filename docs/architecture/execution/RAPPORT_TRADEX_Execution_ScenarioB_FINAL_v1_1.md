# RAPPORT FINAL — TRADEX-AI · Couche d'exécution (Scénario B) — v1.1

> **Version finale post-audit.** Le code joint `execution_guardrails_v1_1.py` est la **seule** version valide. L'ancien code v1.0 est **obsolète** (corrigé après audit 12 passes).

---

## INSTRUCTIONS POUR COWORK

**À classer et à intégrer obligatoirement à la feuille de route TRADEX-AI.**

| Champ | Valeur |
|---|---|
| Projet | TRADEX-AI (`C:\trading-copilote`) |
| Type de document | Spécification d'architecture — couche d'exécution |
| Périmètre | Loop 4 « Exécution » (Loop Engineering) |
| Impact KB | **AUCUN** (KB Belkhayate figée, sans vectorisation) |
| Impact stack | **AUCUN** (Python natif, stdlib only) |
| Priorité | P1 (sécurité d'exécution) |
| Classement proposé | `C:\trading-copilote\docs\architecture\execution\` |

**2 fichiers fournis ensemble :**
1. **Ce rapport** (`.md`) → la spec : schéma JSON, instruction CLAUDE.md, roadmap.
2. **`execution_guardrails_v1_1.py`** → le **code final** (à placer comme module importé par `claude_brain.py`).

**Actions Cowork :**
1. Classer les 2 fichiers dans `docs/architecture/execution/` (et le `.py` près de `claude_brain.py`).
2. Créer `confirmation_card_schema_v1.json` à partir du schéma §2 ci-dessous.
3. **Ne PAS recréer le code depuis ce rapport** → utiliser le fichier `.py` v1.1 joint.
4. Ajouter le bloc CLAUDE.md (§4) au `CLAUDE.md` du projet.
5. Inscrire la ligne de roadmap (§5).

---

## 1. CONTEXTE

Couche d'exécution inspirée des patterns Co-Invest (carte de confirmation, garde-fous chiffrés, verdict NO-TRADE, séparation STAGED/SENT), **sans dépendance** au tiers et **sans toucher à la KB**. Co-Invest n'exécutant pas de futures CME, seuls ses *patterns* sont réutilisés dans le code propre de TRADEX-AI.

**Règles verrouillées respectées** : COG = seul signal TREND · corrélation NQ/ES · filtre inverse Gold/DXY · échelle semi-log · **interdiction absolue d'averaging down**.

---

## 2. Schéma JSON figé de la carte de confirmation (v1.0)

Structure unique et obligatoire pour toute sortie d'ordre du Checker.

```json
{
  "schema_version": "1.0",
  "card_id": "string (uuid v4)",
  "timestamp_utc": "string (ISO-8601, UTC)",
  "instrument": "NQ | ES",
  "verdict": "STAGED | NO_TRADE | REJECTED",
  "direction": "LONG | SHORT | FLAT",
  "size_contracts": "integer (>= 1)",
  "size_pct_account": "number (% du solde réel)",
  "entry_price": "number",
  "invalidation_level": "number (stop OBLIGATOIRE si verdict=STAGED)",
  "take_profit": "number | null",
  "exit_rule": "string",
  "risk": { "max_loss_usd": "number", "rr_ratio": "number" },
  "worst_case_loss_usd": "number (rempli par le code v1.1 : gap+slippage+commissions)",
  "signal": { "cog_reason": "string", "trend": "UP | DOWN | NEUTRAL" },
  "filters": {
    "nq_es_correlation_ok": "boolean",
    "gold_dxy_filter_ok": "boolean",
    "semi_log_scale_ok": "boolean",
    "no_averaging_down_ok": "boolean"
  },
  "maker": { "agent": "string", "proposed_at_utc": "string" },
  "checker": { "agent": "string", "validated_at_utc": "string", "verdict_reason": "string" },
  "state": "STAGED | SENT | CANCELLED | EXPIRED | DUPLICATE",
  "human_approval_required": true,
  "expires_at_utc": "string (ISO-8601)"
}
```

---

## 3. CODE — garde-fous chiffrés

> **Le code est dans le fichier joint `execution_guardrails_v1_1.py`.**
> Ne pas le recopier d'ici. Résumé de ce qu'il fait (v1.1, post-audit) :

- `validate_order()` : 12 contrôles → verdict `STAGED | NO_TRADE | REJECTED | CONFIG_NON_VALIDEE`. **Ne renvoie jamais SENT.**
- `send_order()` : fonction **séparée** STAGED → SENT (exige approbation humaine + non-expiré + idempotency).
- Contrôles : allowlist NQ/ES · marge/notional · **exposition corrélée NQ+ES** · stop obligatoire · no-averaging-down · news blackout · risque **pire cas** (gap+slippage+commissions) · RR min · coupe-circuit journalier.
- Sécurité technique : compteur atomique, idempotency `card_id`, expiry vérifié à l'envoi.
- **Garde-fou de démarrage** : tant que `config_validated = False`, **tout ordre est bloqué**.

**Score audit** : v1.0 = 63/100 (À CORRIGER) → v1.1 corrige les 10 points P0.

---

## 4. INSTRUCTION À AJOUTER DANS `CLAUDE.md`

```markdown
## [EXÉCUTION] Carte de confirmation & garde-fous chiffrés (Scénario B — v1.1)

- Toute sortie d'ordre du Checker DOIT respecter le schéma JSON figé confirmation_card v1.0.
- Aucun ordre ne passe en SENT sans : stop présent + execution_guardrails.validate_order() OK
  + approbation humaine explicite (tap).
- validate_order() ne renvoie JAMAIS SENT. STAGED -> SENT = send_order() uniquement, déclenché par l'humain.
- Verdict NO_TRADE obligatoire si COG ambigu OU filtre Belkhayate non passé. Jamais de trade forcé.
- Interdiction averaging down maintenue (décision verrouillée).
- Coupe-circuit journalier + news blackout actifs.
- Instruments : NQ, ES uniquement.
- Tant que GUARDRAILS["config_validated"] = False : tout ordre est bloqué (volontaire).
```

---

## 5. LIGNE DE ROADMAP

```
[Loop 4 — Exécution] D###  Couche d'exécution Scénario B v1.1
  - Schéma JSON figé carte de confirmation v1.0 ............ SPÉCIFIÉ
  - Module execution_guardrails_v1_1.py .................... CODÉ (post-audit)
  - Brancher broker_send_fn sur pont NinjaTrader ........... À FAIRE
  - Tests unitaires garde-fous ............................. À FAIRE
  - Valider GUARDRAILS + passer config_validated = True .... À FAIRE (Abdelkrim)
  KB : non impactée | Stack : non impactée | Tiers : aucun
```

---

## 6. À FAIRE PAR ABDELKRIM AVANT TOUT ORDRE RÉEL
1. Régler les valeurs `GUARDRAILS` (`# AJUSTER`) puis mettre `config_validated = True`.
2. Renseigner `margin_per_contract` réelle du broker.
3. Reconfirmer les multiplicateurs CME (NQ 20$/pt, ES 50$/pt) auprès du broker.
4. Brancher `broker_send_fn` sur le pont NinjaTrader.

---

*Rapport FINAL v1.1 — TRADEX-AI · Scénario B · remise unique à Cowork.*
