# 🧠 PIPELINE D'ENRICHISSEMENT DU CERVEAU — TRADEX-AI

> **Emplacement de ce fichier :** `C:\trading-copilote\00-pilotage\`
> **But :** transformer n'importe quelle source (chapitre mentor, PDF, note Belkhayate, transcription…) en briques de connaissance validées dans `KNOWLEDGE_BASE_MASTER.json`, **sans jamais perturber la feuille de route**.

---

## 1. PRINCIPE (à lire une fois)

Deux voies **parallèles** qui ne se mélangent jamais :
- **Voie BUILD** = `FEUILLE_DE_ROUTE.md` → construire l'app (phases séquentielles).
- **Voie CERVEAU** = `BACKLOG_ENRICHISSEMENTS.md` → nourrir le cerveau (file d'attente continue).

Image : un **tapis à bagages**. Tu déposes une valise (source) quand tu veux ; le tapis (Cowork) ne la traite **qu'aux moments sûrs** (les interstices). **Déposer ≠ traiter.**

L'**interstice** = le moment entre la fin d'une mission de la roadmap et le début de la suivante. C'est **là**, et seulement là, que l'enrichissement se glisse.

```
Mission roadmap N terminée
        │
        ▼
   [INTERSTICE]  ←── Cowork lit le backlog ici. 1 source 📥 → il la traite.
        │
        ▼
Mission roadmap N+1
```

---

## 2. QUEL FICHIER BOUGE, LEQUEL NE BOUGE JAMAIS

| Fichier | Rôle | Bouge ? |
|---|---|---|
| `FEUILLE_DE_ROUTE.md` | les phases de l'app | ❌ **JAMAIS** touchée par l'enrichissement |
| `CLAUDE.md` (racine) | comportement permanent de Cowork | ⚠️ modifié **UNE seule fois** (la règle interstice), puis plus jamais |
| `BACKLOG_ENRICHISSEMENTS.md` | la file des sources | ✅ +1 ligne par source |
| `02-sources-brutes\` | archive des sources | ✅ reçoit chaque source |
| `04-cerveau-trading\validation\` | zone tampon des briques | ✅ briques fabriquées ici d'abord |
| `KNOWLEDGE_BASE_MASTER.json` | le cerveau (cible finale) | ✅ grossit à chaque fusion validée |
| `REGISTRE_VALIDITE.md` | journal d'audit | ✅ écrit **tout seul** par Claude Code |

👉 Valider un plan **ne change PAS** la feuille de route. La fusion entre dans le **cerveau**, pas dans la roadmap.

---

## 3. LES 6 ÉTATS D'UN TICKET SOURCE

1. 📥 **À TRAITER** — déposée, en attente.
2. 🔍 **PLAN PROPOSÉ** — Cowork a analysé, attend ton OK.
3. ⚙️ **EN EXÉCUTION** — Claude Code fabrique les briques.
4. ✅ **AUDIT AUTO** — Claude Code a lancé l'audit et écrit le verdict.
5. 🔀 **À FUSIONNER** — score OK, prête à entrer.
6. 🟢 **INTÉGRÉ** — fusionnée + commit Git fait.

---

## 4. LE FLUX COMPLET — ÉTAPE PAR ÉTAPE (avec les bons rôles)

### Étape 1 — DÉPÔT · *TOI (dans le chat Cowork)*
Tu colles / uploades la source **directement dans la discussion Cowork** et tu écris :
> « Nouvelle source pour le cerveau. »

Tu ne ranges aucun fichier. Tu ne touches à rien d'autre.

### Étape 1bis — ARCHIVAGE IMMÉDIAT · *COWORK → CLAUDE CODE (auto, instantané)*
Dès le dépôt, Cowork écrit un **petit prompt** → Claude Code :
- enregistre la source dans `02-sources-brutes\` (bon sous-dossier),
- ajoute **1 ligne** au `BACKLOG_ENRICHISSEMENTS.md` à l'état 📥 À TRAITER.

→ La source est **en sécurité dans le projet**, même si tu fermes le chat. (L'archivage est trivial : il ne dérange pas la mission en cours.)

### Étape 2 — DÉCLENCHEMENT · *automatique (à l'interstice)*
À la fin de sa mission roadmap en cours, **avant** la suivante, Cowork lit le backlog (règle dans `CLAUDE.md`), voit le ticket 📥 le plus prioritaire, et le traite **maintenant**. La mission en cours n'est **jamais** coupée.

### Étape 3 — PLAN · *COWORK (prompt uniquement)*
Cowork lit la source + `STRATEGIE_KB_MASTER.md` et te propose :
> « Cette source donne **N briques**, voici leurs `type` et leur `fiabilite`. »

Il **n'écrit aucun fichier**. Ticket → 🔍 PLAN PROPOSÉ.

### Étape 4 — TON SEUL GESTE · *TOI (1 mot)*
Tu réponds **« OK »** (ou « ajuste »). C'est une décision **métier**, pas technique.
⚠️ « OK » = *lance la fabrication*, **pas** *fusionne tout de suite*.

### Étape 5 — EXÉCUTION · *COWORK écrit le prompt → CLAUDE CODE exécute*
Claude Code fabrique les briques JSON dans `04-cerveau-trading\validation\`.
**JAMAIS** directement dans le master. Ticket → ⚙️ EN EXÉCUTION.

### Étape 6 — AUDIT AUTOMATIQUE · *CLAUDE CODE (toi = 0, rien à cocher)*
Claude Code lance **tout seul** l'audit KB sur `validation\`, calcule le **score**, et **écrit le verdict** dans `REGISTRE_VALIDITE.md` (journal automatique).
- Score **≥ seuil** → passe à l'étape 7.
- Score **< seuil** → **STOP**, rien n'est fusionné, il t'écrit la raison en une ligne. Ticket reste bloqué. Ticket → ✅ AUDIT AUTO.

### Étape 7 — FUSION + SAUVEGARDE · *CLAUDE CODE*
1. Sauvegarde d'abord le master (réflexe `.bak`).
2. Fusionne les briques validées dans `KNOWLEDGE_BASE_MASTER.json`.
3. Ticket → 🟢 INTÉGRÉ.
4. `git add . && git commit -m "KB: integration source [nom]"`.

---

## 5. CE QUE TU VOIS, TOI (résumé ultra-simple)

1. Tu colles une source dans le chat → « Nouvelle source pour le cerveau ».
2. Plus tard, Cowork te dit : « N briques proposées, OK ? » → tu réponds **OK**.
3. Cowork te dit : **« 🟢 fusionné »** ou **« ❌ bloqué — raison : … »**.

C'est tout. Aucune case à cocher, aucune mémoire requise.

---

## 6. GARDE-FOUS NON NÉGOCIABLES

- ❌ Jamais d'écriture directe dans `KNOWLEDGE_BASE_MASTER.json` sans passer par `validation\` + audit.
- ❌ Jamais fusionner une source qui n'a pas été archivée dans `02-sources-brutes\` (sinon brique sans origine = non auditable).
- ❌ Jamais interrompre une mission roadmap en cours.
- ✅ Un seul ticket traité par interstice.
- ✅ Le cerveau **explique / vérifie / alerte** — il **ne prédit pas** et n'émet aucun signal certain. Chiffres broker/marge/commission = `DEPEND_DU_BROKER`, jamais inventés.

---

## 7. SCHÉMA D'UNE BRIQUE (rappel — autorité = `STRATEGIE_KB_MASTER.md`)

```json
{
  "id": "ordres-stop-limite-piege",
  "type": "PIEGE",                 // DEFINITION | REGLE | PIEGE
  "fiabilite": "FAIT_STABLE",      // FAIT_STABLE | DEPEND_DU_BROKER | ECOLE_DE_PENSEE
  "domaine": "futures",
  "sujet": "types-ordres",
  "niveau": "debutant",
  "langue": "FR",
  "titre": "Ne jamais utiliser un stop-limite comme stop-loss",
  "contenu": "Un stop-limite devient un ordre limite une fois déclenché : exécution non garantie. Dans une chute rapide, le prix peut sauter par-dessus la limite sans remplir l'ordre.",
  "regle_associee": "Un stop-loss doit être un stop-AU-MARCHÉ.",
  "source_origine": "02-sources-brutes/playbook/PROMPT_Mentor_Trader_Senior_Futures.md",
  "mots_cles": ["stop", "stop-limit", "stop-market", "stop-loss"]
}
```
