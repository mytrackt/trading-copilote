RAPPORT DE SESSION — VEILLE TECHNOLOGIQUE IA TRADING
Date : 29 juin 2026 | Session : Veille techno autonome
Projets concernés : TRADEX-AI + Écosystème Claude Code

---

## 1. RÉSUMÉ EXÉCUTIF

Session de veille technologique couvrant 3 outils majeurs découverts en juin 2026 :
- **OpenAlice** : agent IA de trading autonome (open-source)
- **GStack** (Garry Tan / YC CEO) : setup Claude Code en équipe virtuelle
- **Loop Engineering** : nouvelle philosophie de workflow IA (Boris Cherny / Anthropic)

Aucune installation réalisée. Aucun code produit. Session 100% exploration et stratégie.

---

## 2. OUTIL 1 — OPENALICE

### Qu'est-ce que c'est ?
Agent IA de trading autonome open-source. Couvre le cycle de vie complet du trade :
recherche → dimensionnement position → surveillance → gestion risque → sortie.

### Architecture
- Tourne en local (Node.js)
- Interface : Web UI + bot Telegram + serveur MCP
- Basé fichiers uniquement (pas de base de données)
- Données crypto gratuites : Binance, OKX, Bybit (read-only sans clé API)
- Brokers supportés : Alpaca, Interactive Brokers, CCXT

### Guards de risque intégrés
```json
{
  "guards": [
    { "type": "max-position-size", "options": { "maxPercentOfEquity": 10 } },
    { "type": "cooldown", "options": { "minutes": 15 } },
    { "type": "symbol-whitelist", "options": { "symbols": ["NQ", "ES", "GC"] } }
  ]
}
```

### Moteur IA configuré
```json
{
  "profiles": {
    "default": {
      "backend": "agent-sdk",
      "model": "claude-opus-4-7",
      "loginMethod": "claudeai"
    }
  }
}
```
→ Utilise Claude Code login (abonnement Pro/Max) — pas de clé API séparée.

### Installation prévue (non encore exécutée)
```powershell
# Option A — Desktop (recommandée)
# Télécharger .exe depuis https://github.com/TraderAlice/OpenAlice/releases

# Option B — Sources
git clone https://github.com/TraderAlice/OpenAlice.git C:\OpenAlice
cd C:\OpenAlice
pnpm install && pnpm build
pnpm dev
```

### ⚠️ Statut
Logiciel expérimental — NE PAS utiliser avec de vrais fonds sans période de test paper trading.

### Lien avec TRADEX-AI
OpenAlice peut servir de **couche d'exécution** pendant que TRADEX-AI reste la couche
d'analyse Belkhayate. Les deux coexistent. Même paradigme : fichiers locaux + Claude.

---

## 3. OUTIL 2 — GSTACK (Garry Tan / CEO Y Combinator)

### Qu'est-ce que c'est ?
Setup Claude Code open-source de Garry Tan (CEO YC). Transforme Claude Code en équipe
d'ingénierie virtuelle avec 23 outils spécialisés.

- GitHub : https://github.com/garrytan/gstack
- 117k+ stars | MIT License

### Philosophie
> "Planning is not review. Review is not shipping."
L'IA doit avoir des **engrenages cognitifs explicites**, pas un mode unique générique.

### Skills disponibles
| Commande | Rôle |
|---|---|
| `/plan-ceo-review` | Pense comme un fondateur avant d'écrire du code |
| `/plan-eng-review` | Revue technique comme un staff engineer paranoid |
| `/review` | Code review structurée smart-routée |
| `/ship` | Livraison en 1 commande (tests + docs + deploy) |
| `/browse` | Vrai navigateur Chromium (stealth, screenshots) |
| `/retro` | Rétrospective hebdomadaire par développeur |

### Installation prévue (Étape 1 faite, pas confirmée)
```powershell
# Étape 1 — Cloner dans skills Claude
git clone https://github.com/garrytan/gstack.git C:\Users\mytra\.claude\skills\gstack

# Étape 2 — Setup
cd C:\Users\mytra\.claude\skills\gstack
./setup
```

### Application possible pour mytrackt
Utiliser `/plan-ceo-review` avant chaque nouvelle feature DIFAI/TRADEX/CARIO.
Utiliser `/ship` pour automatiser les livraisons avec tests + docs.

---

## 4. OUTIL 3 — LOOP ENGINEERING

### Concept fondateur
> "Je ne prompts plus Claude. J'ai des boucles qui promptent Claude à ma place.
> Mon job c'est d'écrire des boucles." — Boris Cherny, créateur de Claude Code

### Définition
Concevoir des systèmes IA qui **agissent → observent → décident → répètent**
jusqu'à ce qu'un objectif soit réellement atteint. Remplace le prompting manuel.

### Les 5 blocs d'une boucle

| Bloc | Rôle | Dans Claude Code |
|---|---|---|
| Schedule | Déclenche la boucle | Automation / cron / `/loop` |
| Memory | Fichier d'état persistant | `progress.md` ou `STATE.md` |
| Worktree | Zone isolée par agent | `--worktree` flag |
| Sub-agents | Maker (produit) + Checker (valide) | Sous-agents Claude Code |
| Human Gate | Décisions irréversibles | Approbation manuelle |

### Les 4 types de boucles
1. **Heartbeat** — check-in périodique (ex: toutes les 30 min)
2. **Cron** — tâche programmée fixe (ex: tous les matins à 9h)
3. **Hook** — déclenché par un événement (ex: nouveau commit)
4. **Goal-based** — tourne jusqu'à ce qu'une condition soit vraie (la plus puissante)

### Commandes natives Claude Code
```bash
# Goal-based loop (v2.1.139+)
/goal Tous les tests passent et lint retourne 0 erreur

# Boucle récurrente
/loop every 30m — Vérifie les nouveaux signaux NQ dans SIGNAL_LOG.md

# Auto-approbation (mode headless)
claude --dangerously-skip-permissions
```

### Règle maker + checker (ANTI-BIAIS)
Un seul agent = biais de confirmation (il valide son propre travail).
Solution : 2 sub-agents séparés :
- **MAKER** : produit le code/signal/analyse
- **CHECKER** : valide contre specs/tests/règles — modèle différent

### Fichier mémoire persistant (progress.md)
```markdown
## Done
- 2026-06-29 : Signal NQ détecté, COG à 21450, band sup touchée

## In progress
- Validation volume en cours

## Open / needs human
- Signal Gold ambigu — décision position manuelle requise
```

### ⚠️ Dangers à éviter
- Sans `/goal` précis → boucle infinie → facture API explosive
- Toujours mettre `max_turns` (ex: 10)
- Toujours un human gate pour ordres réels

---

## 5. ARCHITECTURE INTÉGRATION TRADEX-AI × OPENALICE × LOOPS

```
BOUCLE 1 — SURVEILLANCE (toutes les 15 min)
  /loop every 15m
  → Lis prix NQ/ES/Gold
  → Calcule COG Belkhayate
  → Écrit dans MARKET_STATE.md

BOUCLE 2 — ANALYSE (déclenchée par Boucle 1 si signal potentiel)
  /goal : SIGNAL_LOG.md contient signal avec score > 70%
         ET validation Belkhayate complète (COG + band + volume)
  [MAKER] claude_brain.py analyse
  [CHECKER] sous-agent valide règles Belkhayate

BOUCLE 3 — HUMAN GATE (toi)
  → Notification Telegram/Inbox OpenAlice
  → Tu approuves manuellement

BOUCLE 4 — EXÉCUTION (OpenAlice)
  → Ordre transmis au broker via Guards (max 10% equity, cooldown 15min)
  → Snapshot toutes les 15min
```

---

## 6. QUESTIONS EN SUSPENS (à trancher en session Cowork)

1. **Broker pour NQ/ES/Gold** : Interactive Brokers ou NinjaTrader ?
   → OpenAlice supporte IB nativement. NinjaTrader = intégration custom.

2. **TRADEX-AI génère-t-il des signaux aujourd'hui ?**
   → Si non, Boucle 2 ne peut pas être activée.

3. **Paper trading d'abord** : combien de semaines de test avant live ?

4. **GStack installation** : compléter l'étape `./setup` (Étape 1 clonée, non confirmée).

5. **Loop Engineering** : quel est le premier loop à construire pour TRADEX-AI ?
   Proposition : commencer par Boucle 1 (surveillance) uniquement.

---

## 7. DÉCISIONS PRISES

| # | Décision | Statut |
|---|---|---|
| D1 | OpenAlice = couche exécution, TRADEX-AI = couche analyse Belkhayate | ✅ Validé |
| D2 | RAG/KB stack maintenu : Claude API + claude_brain.py + prompt caching | ✅ Confirmé |
| D3 | Architecture Maker+Checker pour tous les loops TRADEX-AI | ✅ Décidé |
| D4 | Human gate OBLIGATOIRE avant tout ordre réel | ✅ Non négociable |
| D5 | Commencer en paper trading uniquement | ✅ Validé |

---

## 8. RESSOURCES CLÉS

| Outil | URL |
|---|---|
| OpenAlice | https://github.com/TraderAlice/OpenAlice |
| GStack | https://github.com/garrytan/gstack |
| Loop Engineering (essay) | https://www.the-ai-corner.com/p/loop-engineering-coding-agents-2026 |
| Claude Code Agent Loop docs | https://code.claude.com/docs/en/agent-sdk/agent-loop |
| Loop Engineering GitHub | https://github.com/cobusgreyling/loop-engineering |

---

## 9. PHRASE D'AMORÇAGE POUR COWORK

Colle ce bloc en début de session Cowork :

```
Contexte de session : j'ai fait une veille technologique sur claude.ai
couvrant 3 outils : OpenAlice (agent trading IA autonome), GStack (Garry Tan / YC),
et Loop Engineering (Boris Cherny / Anthropic).

Mon projet principal est TRADEX-AI (C:\trading-copilote) — copilote de trading
basé sur la méthode Belkhayate, stack gelée : claude_brain.py + Claude API +
prompt caching. NinjaTrader pour NQ/ES/Gold.

Le rapport complet de la session précédente est joint (RAPPORT_SESSION_VEILLE_TECHNO_20260629.md).

Je veux continuer sur : [CHOISIS UNE OPTION]
A) Installer GStack dans mon Claude Code
B) Installer OpenAlice et le configurer en paper trading
C) Construire la Boucle 1 (surveillance 15min) pour TRADEX-AI
D) Définir l'architecture complète d'intégration TRADEX × OpenAlice × Loops
```

---

*Rapport généré le 29/06/2026 — Session veille techno claude.ai*
*Projet : TRADEX-AI + Écosystème Claude Code*