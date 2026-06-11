# DETTE TECHNIQUE — TRADEX-AI

> Bugs CONSTATÉS et NOTÉS lors de la réorganisation du 11/06/2026 — **volontairement non corrigés**
> (décision actée : la mission de réorganisation range, elle ne répare pas le SaaS).
> À traiter dans une mission dédiée avant la mise en route des modules SaaS (Phases C+).
> Tous les modules ne tournent pas encore en production : aucun de ces bugs n'est bloquant aujourd'hui.

---

## 1. ✅ PARTIELLEMENT RÉPARÉ (11/06/2026 — commit 75a517e) — Bug `code\code\` — chemins doublés

Les modules calculent `BASE_DIR` = "2 crans au-dessus du fichier" (= `05-saas\` depuis la réorganisation),
puis y ajoutent encore `code\` — un segment qui n'existe plus.

| Fichier | Ligne | Chemin calculé (constaté le 11/06/2026) | Existe ? |
|---|---|---|---|
| `05-saas\engine\claude_brain.py` | 177 | `05-saas\code\knowledge_base\KNOWLEDGE_BASE_MASTER.json` | ❌ |
| `05-saas\config\settings.py` | 69 (`KB_DIR`) | `05-saas\code\knowledge_base\` | ❌ |
| `05-saas\config\settings.py` | 72 (`KB_PATH`) | `05-saas\code\knowledge_base\KNOWLEDGE_BASE_MASTER.json` | ❌ |

**Correctif futur** : pointer vers `C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json`
(emplacement réel de la KB depuis la Phase 7 — `transcript_processor.py` montre le pattern correct :
`PROJECT_ROOT / "04-cerveau-trading"`).

## 2. Dossier `data\` inexistant

| Fichier | Ligne | Chemin codé en dur | Existe ? |
|---|---|---|---|
| `05-saas\engine\staleness_monitor.py` | 16 | `C:/trading-copilote/data` | ❌ |
| `05-saas\engine\data_reader.py` | 4 | `C:/trading-copilote/data` | ❌ |
| `05-saas\config\settings.py` | 68 (`DATA_DIR`) | `05-saas\data` | ❌ |
| `05-saas\config\settings.py` | 70 (`LOGS_DIR`) | `05-saas\logs` | ❌ |

**Correctif futur** : le dossier `data\` (flux JSON NT8/ATAS) sera créé par les collecteurs en Phase C —
décider alors de son emplacement définitif et harmoniser les 4 références ci-dessus.

## 3. ✅ RÉPARÉ (11/06/2026 — commit 75a517e) — Import inter-modules cassé

```python
# AVANT (cassé) :
from code.engine.circuit_breaker import CB_CLAUDE
from code.engine.prompt_builder import build_god_mode_prompt

# APRÈS (corrigé) :
from .circuit_breaker import CB_CLAUDE
from .prompt_builder import build_god_mode_prompt
```
Chemin KB dans `load_kb_rules()` également corrigé :
`dirname(BASE_DIR) / "04-cerveau-trading" / "KNOWLEDGE_BASE_MASTER.json"` — KB existe et est chargeable.

## 4. Hypothèse « 1 transcript vide » — INFIRMÉE (vérifiée le 11/06/2026)

Comptage réel dans `03-transcriptions\transcripts-bruts\` : **142 fichiers `whisper_*.txt`, 0 vide**.
L'écart apparent (143 fichiers déplacés vs 142 lus) vient de `status.json` — le journal de l'ancien
pipeline whisper, qui n'est pas un transcript. Cohérence confirmée par la KB : 142 vidéos traitées.
**Aucune action requise.**

---

## Rappels d'état (réorganisation du 11/06/2026)

- KB vivante : `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` (142 vidéos, 11 catégories de règles)
- Seul script SaaS aux chemins corrects : `05-saas\knowledge_base\transcript_processor.py` (corrigé Phases 6-7)
- Moteur TRANSVIDEO : `01-moteur-transvideo\` — sorties vers `03-transcriptions\nouvelles-sources\`
- Docstring obsolète (cosmétique) : `01-moteur-transvideo\scripts\chunk_fuse.py:1178` mentionne encore
  « 07-nouvelles sources » et déclenche un `SyntaxWarning` (`\[` non échappé) — à nettoyer à l'occasion
