# DETTE TECHNIQUE — TRADEX-AI

> Bugs CONSTATÉS et NOTÉS lors de la réorganisation du 11/06/2026 — **volontairement non corrigés**
> (décision actée : la mission de réorganisation range, elle ne répare pas le SaaS).
> À traiter dans une mission dédiée avant la mise en route des modules SaaS (Phases C+).
> Tous les modules ne tournent pas encore en production : aucun de ces bugs n'est bloquant aujourd'hui.

---

## 1. ✅ RÉPARÉ COMPLET (S35, commit c8ffb0f) — Chemins KB + `load_kb_rules`

Chemins `KB_DIR`/`KB_PATH` dans `settings.py` corrigés en S35 → pointent vers
`C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` (emplacement réel).

`load_kb_rules()` dans `claude_brain.py` réparé S35 : lit la clé `aggregated_rules`
(au lieu de `rules` inexistante) et gère 2 formats KB coexistants (vidéo + chapitre).
Résultat : 1398 règles chargées correctement · SHA256 = `bcaaaeed...`

**Aucune action requise.**

## 2. ✅ RÉSOLU (S36) — Dossier `data\` — existant confirmé

Vérifié en S36 lors de l'exécution de C0B : `DATA_DIR = C:\trading-copilote\data` **existe**.
Le dossier a été créé entre S11 et S36 (probablement lors d'une session de test).
Les 3 collecteurs Phase C (cot_collector, macro_collector, news_collector) écriront dans ce dossier.

**Aucune action requise.** Harmonisation des chemins : voir Phase C Track A.

## 3. ✅ RÉPARÉ (S03, commit 75a517e + S35, commit c8ffb0f) — Import inter-modules + load_kb_rules

Imports relatifs corrigés S03 (`from .circuit_breaker import CB_CLAUDE`).
`load_kb_rules()` réparé S35 : chemin KB correct + lecture `aggregated_rules` + 2 formats KB.
**Aucune action requise.**

## 4. Hypothèse « 1 transcript vide » — INFIRMÉE (vérifiée le 11/06/2026)

Comptage réel dans `03-transcriptions\transcripts-bruts\` : **142 fichiers `whisper_*.txt`, 0 vide**.
L'écart apparent (143 fichiers déplacés vs 142 lus) vient de `status.json` — le journal de l'ancien
pipeline whisper, qui n'est pas un transcript. Cohérence confirmée par la KB : 142 vidéos traitées.
**Aucune action requise.**

## ⏳ 5. Migration google.generativeai → google.genai
- Package actuel : google-generativeai (déprécié, FutureWarning)
- Action : pip install google-genai + adapter imports + API dans gemini_transcriber.py
- Fichiers concernés : 05-saas\utils\gemini_transcriber.py
- Priorité : P2 — à faire AVANT mise en prod, après validation pipeline complet
- Risque si ignoré : rupture future sans préavis lors d'une mise à jour pip

---

## 6. ✅ RÉPARÉ (S36) — Circuit Breaker INACTIF

### Problème
`protected_call()` (timeout 15s + retry 2x + fallback ATTENDRE) implémentée dans
`circuit_breaker.py` mais jamais appelée en production.
`claude_brain.py` et `data_reader.py` utilisaient `CB.call()` directement → 0 timeout.
Un appel Claude API ou lecture JSON bloqué gelait le thread moteur indéfiniment.

### Correctif appliqué (S36)
- `claude_brain.py` : `CB_CLAUDE.call(_call)` → `protected_call(CB_CLAUDE, _call, timeout_sec=15, retry_max=2)`
- `data_reader.py` : `CB_NT8.call()` / `CB_ATAS.call()` → `protected_call(..., timeout_sec=5, retry_max=1)`
- Détection fallback dict CB_FALLBACK → comportement correct dans get_signal() et data_reader

### Validation
Tests `test_risk_guardrails.py` : 21/21 PASS (tests CB préexistants couvrent tous les cas).
Lint `py_compile` : 0 erreur sur les 3 fichiers. KB inchangée : 1398 règles.

### Mode AUTO
Toujours BLOQUÉ (`AUTO_MODE = False`). La réparation du circuit breaker est un prérequis
**nécessaire mais pas suffisant** pour envisager le mode AUTO.

---

## 7. ⏳ Phase C — points OPÉRATIONNELS collecteurs (S36, pas des bugs de code)

> Les 3 collecteurs Phase C (`cot_collector`, `macro_collector`, `news_collector`) compilent
> et fonctionnent. Les 2 points ci-dessous sont opérationnels (clé API / quota), pas du code.

### 7.1 ✅ RÉSOLU (S38) — Clé Finnhub régénérée
- Clé révoquée régénérée sur finnhub.io (S38, 28/06/2026) → remplacée dans `.env`.
- Validation : `collect_news()` → `finnhub_disponible=True` · `count=2` · pas de 401.
- **Aucune action requise.**

### 7.2 ⏳ GDELT rate-limit (`news_collector.py`)
- API GDELT : **429** « limit requests to one every 5 seconds » sur la requête large multi-OR.
- Transitoire : une requête simple a bien renvoyé 200 (endpoint + format OK). Le 429 prolongé en S36
  venait des sondes de diagnostic rapprochées. En prod (1 cycle / 5 min) GDELT répond.
- Le code gère déjà le 429 (retourne `[]`). **Aucune action bloquante.**
- Amélioration possible (non faite) : en-tête `User-Agent` + léger backoff si throttling récurrent.

### 7.3 Correctifs de fond appliqués pendant Track A (rappel)
- `cot_collector` : filtrage COT par **code contrat exact** (`cftc_contract_market_code`) au lieu de
  `contains(nom)` — évitait MICRO GOLD / MICRO COPPER / WTI ICE Europe / mauvais blé. API CFTC OData **v4**, table `jun7-fc8e`, encodage `%20`.
- `macro_collector` : série EIA **`WCESTUS1`** (stocks crude hors SPR, ~412M) au lieu de `WCRSTUS1`
  (total SPR incluse, ~743M) que renvoyaient les facets initiales. Dataset `petroleum/stoc/wstk`.

---

## Rappels d'état (réorganisation du 11/06/2026)

- KB vivante : `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` (142 vidéos, 11 catégories de règles)
- Seul script SaaS aux chemins corrects : `05-saas\knowledge_base\transcript_processor.py` (corrigé Phases 6-7)
- Moteur TRANSVIDEO : `01-moteur-transvideo\` — sorties vers `03-transcriptions\nouvelles-sources\`
- Docstring obsolète (cosmétique) : `01-moteur-transvideo\scripts\chunk_fuse.py:1178` mentionne encore
  « 07-nouvelles sources » et déclenche un `SyntaxWarning` (`\[` non échappé) — à nettoyer à l'occasion
