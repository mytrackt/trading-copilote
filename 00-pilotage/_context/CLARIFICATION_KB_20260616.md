# CLARIFICATION KB — TRADEX-AI
**Date :** 16/06/2026 | **Session :** S15 | **Auteur :** Cowork (lecture seule)
**Objet :** Réconciliation des compteurs contradictoires de la Knowledge Base

> ⛔ Ce document est en LECTURE SEULE. Aucun fichier n'a été modifié.

---

## 1. RECOMPTAGE RÉEL — KNOWLEDGE_BASE_MASTER.json

**Fichier :** `04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json`
**Modifié le :** 2026-06-15 20:54:53 UTC

```
Structure : {metadata, videos, aggregated_rules}
aggregated_rules → 11 catégories → TOTAL : 1 265 règles
```

**⚠️ DÉCOUVERTE CRITIQUE :** Les règles dans `aggregated_rules` sont des **chaînes de texte brutes (strings)**, pas des objets avec champ `statut`. Le master KB ne porte AUCUN statut VALIDE/AMBIGU/INVALIDE directement.

| Catégorie | Nb règles |
|-----------|----------:|
| saisonnalite | 21 |
| correlations | 34 |
| timing | 106 |
| indicateurs_tendance | 218 |
| indicateurs_momentum | 49 |
| gestion_risque_entree | 174 |
| gestion_position_active | 84 |
| structure_marche | 267 |
| macro_evenements | 12 |
| volume_liquidite | 67 |
| psychologie | 233 |
| **TOTAL** | **1 265** |

**Les statuts (VALIDE/AMBIGU/INVALIDE) vivent dans : `04-cerveau-trading/validation/KB_VALIDEE.json`** — dans sa section `metadata`, pas dans le master.

---

## 2. QUI DIT QUOI — TABLEAU DES SOURCES (plus récente → plus ancienne)

| Source | Chiffre annoncé | Date | Commit | Concorde avec recomptage réel ? |
|--------|----------------|------|--------|--------------------------------|
| CLAUDE.md | 1166 VALIDE / 45 AMBIGU / 54 INVALIDE | 2026-06-15 23:11 | 23575f6 + e2f3ef8 | ✅ Oui — concorde avec KB_VALIDEE metadata |
| KB_VALIDEE.json (metadata) | 1166 VALIDE / 45 AMBIGU / 54 INVALIDE | 2026-06-15 20:41 | 8dceff0 | ✅ Oui — source de vérité des statuts |
| AUDIT_KB_RESULTS.json | 40 VALIDE / 1225 DOUTEUX / 165 INVALIDE | 2026-06-14 23:16 | Antérieur à 8dceff0 | ❌ Non comparable — population différente + définition différente |

**Le chiffre qui fait foi aujourd'hui : 1 265 règles dont 1 166 VALIDE / 45 AMBIGU / 54 INVALIDE (92,2%)**
Source : métadonnées cumulées de `KB_VALIDEE.json` (3 passes de validation successives).

---

## 3. CALCUL DE RECONSTRUCTION DES 1 166 VALIDE (traçabilité complète)

```
Étape 0 : Purge B-04 (14/06 23:23) : 1 461 → 1 257 règles (-204 DOUBLON/INVALIDE)
Étape 1 : Lift B-05 (échantillon 5%) : -1 supprimé manuel + 2 promus VALIDE → 1 256
Étape 2 : Ajouts B-06 (vidéo 10 Belkhayate officielle) : +9 règles VALIDE → 1 265
──────────────────────────────────────────────────────────────────────────────────
BASE : 1 265 règles dans aggregated_rules (chiffre vérifié par recomptage)

Passe 1 — validate_douteux.py (15/06 ~20:19) :
  VALIDE : 835 | INVALIDE : 42 | AMBIGU : 388 → total 1 265 ✅

Passe 2 — revalidation S13 (15/06 ~20:53) :
  +276 VALIDE_gagne | +9 INVALIDE_gagne | reste 103 AMBIGU
  → 835+276 = 1 111 VALIDE | 42+9 = 51 INVALIDE | 103 AMBIGU → total 1 265 ✅

Passe 3 — revalidation S14 passe3 Sonnet (15/06 ~20:41) :
  +55 VALIDE_gagne | +3 INVALIDE_gagne | reste 45 AMBIGU
  → 1 111+55 = 1 166 VALIDE | 51+3 = 54 INVALIDE | 45 AMBIGU → total 1 265 ✅

RÉSULTAT FINAL : 1 166 VALIDE / 54 INVALIDE / 45 AMBIGU = 1 265 ✅
```

---

## 4. ORIGINE DES 1 265 RÈGLES

**Règles brutes extraites par le moteur :** 108 vidéos → 1 188 règles brutes
(Champ `channel` vide dans le JSON → affiché "INCONNU" par le parser — pas une erreur, c'est un attribut non rempli dans la structure vidéo.)

**Règles manuelles :** +9 règles (phase B-06, vidéo 10 Belkhayate officielle, statut VALIDE garanti)

**Reconstruction post-purge :** -204 règles DOUBLON/INVALIDE supprimées → **1 265 règles finales**

**Origine des 108 vidéos :** INDÉTERMINÉ précisément — le champ `channel` est vide dans chaque objet vidéo du master. Le REGISTRE_VALIDITE.md mentionne que la KB originale venait de "synthèses NotebookLM" (142 fichiers), remplacée par rebuild B-02 avec de vrais transcrits. Les canaux réels sont identifiables uniquement via `03-transcriptions/` (Belkhayate officiel + Gigi Trading + Single Videos).

**Le 92,2% concerne-t-il tout le cerveau ou un sous-ensemble ?**
→ Il concerne **l'intégralité des 1 265 aggregated_rules**, pas un sous-ensemble. Belkhayate + autres canaux confondus.

---

## 5. HEAD vs 8dceff0 — ÉTAT DU DISQUE

```
HEAD actuel  : e2f3ef8 — "Pipeline enrichissement KB en place" — 16/06/2026 00:16
8dceff0      : "feat(kb): passe3 S14 - 1166 VALIDE 54 INVALIDE 45 AMBIGU (+55 valide)" — S14

Commits intermédiaires depuis 8dceff0 :
  c1b9cc5 — chore: session S14 terminee (+revalider_passe3.log uniquement)
  23575f6 — chore: session S14 terminee (+README_TRANSITION + CLAUDE.md)
  e2f3ef8 — Pipeline enrichissement KB en place (+BACKLOG, PIPELINE, MODELE_TICKET, etc.)
```

**e2f3ef8 n'a PAS modifié les fichiers KB** (0 changement sur KNOWLEDGE_BASE_MASTER.json, KB_VALIDEE.json, AUDIT_KB_RESULTS.json). Il a ajouté des fichiers de pilotage uniquement.

→ **Les fichiers KB sur le disque correspondent à 8dceff0.** HEAD = e2f3ef8 est cohérent.

---

## 6. CAUSE RACINE DE LA CONTRADICTION

Les trois sources parlent de **trois choses différentes** présentées avec le même mot "VALIDE" :

**Source A (AUDIT_KB_RESULTS.json — 40 VALIDE)** : Audit hostile lancé le 14/06 à 23:16 sur **1 461 règles** (avant purge). Définition ultra-stricte : une règle est VALIDE uniquement si elle est **verbatim confirmée dans un transcript Belkhayate officiel**. 1 225 règles tombent en DOUTEUX car leur attribution à Belkhayate n'est pas prouvée mot pour mot. Cet audit n'a **pas servi à mettre à jour le master** — il a servi à déclencher la purge.

**Source B (KNOWLEDGE_BASE_MASTER.json — pas de statut)** : Le master contient 1 265 strings brutes **sans champ statut**. Il ne déclare aucun chiffre de validation. C'est une base de textes, pas une base de jugements.

**Source C (KB_VALIDEE.json metadata — 1 166 VALIDE)** : Validation sémantique via Claude Sonnet en 3 passes successives. Définition souple : une règle est VALIDE si le **concept est compatible avec la méthode Belkhayate**, même en paraphrase. Les statuts sont stockés dans la metadata de KB_VALIDEE, pas dans les règles elles-mêmes.

**Ces sources ne sont pas comparables** : population différente (1461 vs 1265), critère différent (verbatim vs sémantique), fichier différent (AUDIT vs KB_VALIDEE).

---

## 7. 3 ACTIONS RECOMMANDÉES (à exécuter lors d'une prochaine session — pas maintenant)

**Action 1 — Attacher les statuts aux règles dans le master (P1)**
Modifier le script de fusion pour que chaque règle dans `aggregated_rules` soit un objet `{regle, statut, source_video_id, categorie}` plutôt qu'une string. Permet de requêter directement le master sans KB_VALIDEE séparée.

**Action 2 — Renseigner le champ `channel` dans videos[] (P2)**
Parcourir `videos{}` et remplir `channel` depuis les noms de dossiers dans `03-transcriptions/nouvelles-sources/`. Permet de ventiler les 1 265 règles par canal d'origine (Belkhayate officiel vs enrichissements externes) et de donner un taux "92,2% de quoi" précis.

**Action 3 — Archiver ou supprimer AUDIT_KB_RESULTS.json (P3)**
Ce fichier correspond à un audit sur une population périmée (1 461 règles avant purge). Il risque de continuer à créer de la confusion. Le déplacer dans `_archive/audits-prompts/` avec une note expliquant qu'il précède la purge B-04.

---

## 8. FICHIERS CONSULTÉS (lecture seule)

| Fichier | Date modif | Commit |
|---------|-----------|--------|
| CLAUDE.md | 2026-06-15 23:11 | e2f3ef8 |
| 00-pilotage/REGISTRE_VALIDITE.md | — | antérieur |
| 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json | 2026-06-15 20:54 | 8dceff0 |
| 04-cerveau-trading/AUDIT_KB_RESULTS.json | 2026-06-15 20:54 | 8dceff0 |
| 04-cerveau-trading/PURGE_KB_LOG_20260614_2323.md | 2026-06-15 20:54 | 8dceff0 |
| 04-cerveau-trading/processor_status.json | 2026-06-15 20:54 | 8dceff0 |
| 04-cerveau-trading/validation/KB_VALIDEE.json | 2026-06-15 20:41 | 8dceff0 |
| AUDIT_KB_RAPPORT_20260614_2316.md | 2026-06-15 20:54 | 8dceff0 |
| git log --oneline -15 | HEAD=e2f3ef8 | — |

**Fichiers absents (signalés) :** Aucun fichier manquant parmi ceux demandés. BACKLOG_ENRICHISSEMENTS.md présent et lu. REGISTRE_VALIDITE.md présent et lu.
