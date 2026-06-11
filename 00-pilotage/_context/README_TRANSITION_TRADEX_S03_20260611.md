# README DE TRANSITION — TRADING-COPILOTE

**Date :** 11/06/2026 · **Session :** S03 — Alignement des sources de vérité (CLAUDE.md + Instructions Cowork) sur la nouvelle structure 00→06.

---

## 1. ÉTAT ACTUEL

La réorganisation pro 00→06 (session S02) est **poussée sur GitHub** (`960fe88`). Cette session a corrigé les **deux cartes périmées** qui décrivaient encore l'ancienne structure : `CLAUDE.md` (disque) et les Instructions du projet Cowork. Les deux sont désormais alignées, avec garde-fous trading cohérents et dette technique signalée. La dette technique reste **documentée mais non réparée**.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Détail | Commit | Statut |
|---|---|---|---|
| Vérif git push S02 | Push confirmé `960fe88` + ZIP de sauvegarde supprimé | — | ✅ |
| Réécriture `CLAUDE.md` | Structure 00→06 réelle + dette technique + décisions verrouillées conservées | `30d59a1` | ✅ |
| Réécriture Instructions Cowork | Alignées 00→06 ; correction contradiction `5/8`→`3/4+2/3` ; Bitcoin/Yen no-trade ; RÈGLE 11 garde-fous runtime ajoutée | (Cowork, hors Git) | ✅ |
| Audit skill `/audit-trading-saas-prompts` | Instructions Cowork auditées : 74→~90/100 après corrections (comptage KB 10→11, garde-fous runtime, disclaimer) | — | ✅ |

---

## 3. MISSION SUIVANTE (par priorité)

1. **🔴 Réparer la dette technique** (`00-pilotage\DETTE_TECHNIQUE.md`) — surtout le **circuit breaker inactif en silence** (`claude_brain.py` importe l'ancien paquet `code.engine.circuit_breaker`). Garde-fou de sécurité trading KO. → **À faire dans Cowork** (travail code + tests).
2. Corriger chemins doublés `code\code\` et dossier `data\` inexistant (claude_brain, settings, staleness_monitor, data_reader).
3. Valider la **fiabilité réelle du moteur** (objectif > 90/95 %, jamais prouvé — dernier test = `success_partial`).
4. Distiller le cerveau trading → CDC du SaaS.

---

## 4. DÉCISIONS PRISES CETTE SESSION

- **`CLAUDE.md` = source de vérité disque**, Instructions Cowork = source de vérité gouvernance. Les deux doivent rester synchronisées avec la structure 00→06.
- **Migration recommandée vers Cowork** pour la dette technique (modif fichiers + exécution tests sur disque). Claude.ai réservé à la réflexion/audit/rédaction.
- Ancien `CLAUDE.md` conservé en `CLAUDE.md.old` (filet de sécurité, non commité).

---

## 5. DÉCISIONS TEMPORAIRES

| # | Décision | Condition de levée | Action |
|---|---|---|---|
| 1 | `CLAUDE.md.old` conservé | Quand tout est validé stable | `Remove-Item C:\trading-copilote\CLAUDE.md.old` |
| 2 | `_temp\temp_audio\` (121 Mo) conservé | Confirmer ne plus en avoir besoin | Supprimer `_temp\` |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

- **🔴 Circuit breaker inactif en silence** — critique, à réparer avant tout usage trading réel.
- **Bugs chemins** (`code\code\`, `data\` absent) — modules pas en service → pas urgent mais bloque le lancement du SaaS.
- **Fiabilité moteur non validée** (> 95 % NON prouvé).

---

## 7. ÉTAT DU REPO

- Dernier commit poussé : `30d59a1` "docs(claude): mise a jour structure 00-06 + dette technique".
- Précédent : `960fe88` (réorganisation pro).
- `git push` : ✅ confirmé.

---

## 8. COMMANDES UTILES (PowerShell — lignes séparées, jamais &&)

```powershell
cd C:\trading-copilote
git log --oneline -3
```

Nettoyage (uniquement quand validé stable) :
```powershell
Remove-Item C:\trading-copilote\CLAUDE.md.old
```

---

## 9. PHRASE D'AMORÇAGE SESSION SUIVANTE (à coller dans Cowork)

> « Reprise du projet trading-copilote dans Cowork. Lis d'abord C:\trading-copilote\CLAUDE.md EN ENTIER, puis le dernier README dans 00-pilotage\_context\, puis 00-pilotage\DETTE_TECHNIQUE.md. Mission du jour : réparer la dette technique, en priorité le circuit breaker inactif (claude_brain.py importe l'ancien paquet code.engine.circuit_breaker). Procède phase par phase, je valide chaque étape, et explique chaque commande comme à un débutant. »
