# DETTE TECHNIQUE — TRADEX-AI

> Bugs CONSTATÉS et NOTÉS lors de la réorganisation du 11/06/2026 — **volontairement non corrigés**
> (décision actée : la mission de réorganisation range, elle ne répare pas le SaaS).
> À traiter dans une mission dédiée avant la mise en route des modules SaaS (Phases C+).
> Tous les modules ne tournent pas encore en production : aucun de ces bugs n'est bloquant aujourd'hui.

---

## 1. Bug `code\code\` — chemins doublés (hérité de la migration vers `code\`, aggravé par le renommage en `05-saas\`)

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

## 3. Import inter-modules cassé — `claude_brain.py:25`

```python
from code.engine.circuit_breaker import CB_CLAUDE   # paquet "code" renommé en "05-saas"
```
L'import échoue silencieusement (`except ImportError`) → `CB_CLAUDE = None` : **le circuit breaker est
désactivé en mode dégradé sans bruit**. Constaté à l'import le 11/06/2026 (« circuit_breaker non disponible »).
Bug antérieur à la réorganisation (l'import en style paquet `code.engine.*` ne fonctionnait que dans
des conditions précises de lancement) ; il est désormais cassé en permanence.

**Correctif futur** : import relatif (`from .circuit_breaker import CB_CLAUDE`) ou restructuration en
paquet propre. Attention : `05-saas` n'est pas un nom de paquet Python valide (tiret + chiffre initial) —
les imports doivent rester relatifs au dossier `05-saas\` ajouté au `sys.path`, jamais en style `O5саas.engine.*`.

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
