# AUDIT DE COHÉRENCE & COMPATIBILITÉ — DOCTRINE KB AMÉLIORÉE

> **Date** : 2026-06-16 · **Mode** : LECTURE SEULE — aucun fichier existant modifié.
> **Objet** : valider la cohérence interne des 8 axes proposés ET leur compatibilité avec l'existant TRADEX-AI.
> **Conclusion express** : 🟡 **GO après 4 ajustements bloquants** — le schéma réel des briques ne correspond à AUCUN des schémas proposés.

---

## 0. FAIT DÉCISIF (à lire avant tout)

Le schéma RÉEL d'une brique dans `KNOWLEDGE_BASE_MASTER.json` n'est **pas** un objet riche.
C'est une **chaîne de texte nue**, rangée dans une map `videos → video_id → rules → catégorie → [ ... ]` :

```json
"videos": {
  "-OIGv5rLLV8": {
    "video_id": "-OIGv5rLLV8",
    "transcript_file": "...txt",
    "transcript_chars": 7051,
    "model": "claude-sonnet-4-6",
    "processed_at": "2026-06-14T20:48:43Z",
    "rules": {
      "gestion_risque_entree": [
        "Ne pas entrer sur la première cassure d'un range : attendre...",   // ← UNE brique = CETTE string
        "Entrer un tick en dessous du point de cassure confirmé..."
      ],
      "structure_marche": [ "..." ],
      "psychologie": [ "..." ]
    }
  }
}
```
*(Source : `KNOWLEDGE_BASE_MASTER.json:94-123` — confirmé identique dans `validation\KB_VALIDEE.json:1-45`.)*

**Conséquence** : une brique n'a **AUCUN** champ au niveau règle — pas d'`id`, pas de `type`,
pas de `fiabilite`, pas de `source_origine`, pas de `verbatim`, pas de statut. Les seules
métadonnées vivent au niveau **vidéo** (`video_id`, `transcript_file`, `model`, `processed_at`).
Le **statut** (VALIDE/DOUTEUX/INVALIDE/DOUBLON) est stocké **hors du master**, dans
`AUDIT_KB_RESULTS.json`, repéré par `catégorie + index` (`AUDIT_KB_RESULTS.json:11-60`).

La doctrine proposée (8 axes) décrit un **objet-brique riche** (type, fiabilite, id, source_origine,
audit_score, prerequis, lifecycle…). Elle est donc **compatible avec le schéma DOCUMENTÉ**
(`PIPELINE_ENRICHISSEMENT_KB.md §7`) mais **incompatible avec le JSON RÉELLEMENT en production**.
Tout le reste de l'audit découle de cet écart.

---

## 1. TABLEAU DES CONTRÔLES

| # | Contrôle | Verdict | Preuve (fichier:ligne) |
|---|----------|---------|------------------------|
| **A** | Cohérence interne des 8 axes | ⚠️ à adapter | Axes 1/2/3/4/5/7/8 cohérents entre eux. Tension : axe 6 (cycle draft→validée→active→dépréciée) introduit une **3ᵉ taxonomie de statut** qui chevauche les 6 états de ticket (`PIPELINE…KB.md:46-53`) et les statuts d'audit (`AUDIT_KB_RESULTS.json:5-9`). |
| **B1** | Schéma proposé vs schéma DOCUMENTÉ (`PIPELINE §7`) | ✅ compatible | `type`, `fiabilite`, `regle_associee`, `source_origine`, `mots_cles` existent déjà (`PIPELINE…KB.md:124-138`). La doctrine ré-énonce ce schéma. |
| **B2** | Schéma proposé vs schéma RÉEL (master en prod) | ❌ conflit | Brique = string nue, 0 champ règle (`KNOWLEDGE_BASE_MASTER.json:100-123`). `id`, `type`, `fiabilite`, `source_origine`, `audit_score`, `prerequis` TOUS absents. |
| **B3** | Champ `verbatim` (obligatoire selon STRATEGIE) | ❌ conflit hérité | `STRATEGIE_KB_MASTER.md:67` : « pas de verbatim = règle rejetée ». Or **0 brique du master n'a de verbatim**. La KB en prod viole déjà sa propre règle d'or — la doctrine ne le corrige pas. |
| **B4** | Convention d'ID anti-collision | ⚠️ à adapter | Master réel : **aucun ID** → 0 collision technique. MAIS la convention proposée `domaine-sujet-concept-type` est une **3ᵉ** convention concurrente : `STRATEGIE_KB_MASTER.md:48` impose `BLK-C2-timing-0042`, `PIPELINE…KB.md:126` impose `ordres-stop-limite-piege`. |
| **B5** | Traçabilité (source_origine, date_ajout, audit_score) | ⚠️ à adapter | Traçabilité existe au niveau **vidéo** seulement (`transcript_file`, `processed_at` — `KNOWLEDGE_BASE_MASTER.json:96-99`). `audit_score` numérique par brique n'existe pas : l'audit ne stocke que `statut`+`motif` (`AUDIT_KB_RESULTS.json:15-18`). |
| **C** | Compatibilité processus (interstice / validation\ avant master / 1 ticket) | ✅ compatible (1 réserve) | Doctrine additive, ne contredit pas `CLAUDE.md:329-355` ni `PIPELINE…KB.md:85-98`. Réserve : « REGLE critiques AUSSI dans le system prompt » ouvre une cible d'écriture (`claude_brain.py`) **hors** du chemin audité `validation\`→master. |
| **D** | Compatibilité agents (`AGENTS.md` / A9) | ⚠️ à adapter | A9 tient `REGISTRE_VALIDITE.md` avec vocabulaire VALIDE/DOUTEUX/INVALIDE (`REGISTRE_VALIDITE.md:4`). Le lifecycle de l'axe 6 est une taxonomie parallèle → à mapper. Méta-règle EXPLIQUE/VÉRIFIE/ALERTE = **identique** à `PIPELINE…KB.md:118` ✅. |
| **E** | Dette / contraintes ignorées par le dernier audit | ⚠️ à adapter | Statut stocké par **index positionnel** hors master (`AUDIT_KB_RESULTS.json:11-60`) → fragile à toute insertion/réordonnancement, ce qui casse l'idempotence (axe 2) et le lifecycle (axe 6) qui supposent une identité d'objet stable. |

---

## 2. INCOMPATIBILITÉS CONCRÈTES + CORRECTIFS

### ❌ INC-1 (BLOQUANT) — Schéma objet vs schéma string nue
- **Constat** : la doctrine suppose un objet-brique ; le master stocke des strings (`KNOWLEDGE_BASE_MASTER.json:100-123`).
- **Impact** : aucun des 8 axes (id, type, fiabilite, audit_score, prerequis, lifecycle) n'est applicable en l'état. Adopter la doctrine = **migrer les 1265 briques** string → objet.
- **Correctif proposé** : décider explicitement un **schéma cible v2** et un **script de migration** (1 string → 1 objet `{id, type, fiabilite, contenu, categorie, source_video_id, ...}`), exécuté via `validation\` puis fusion auditée. Versionner : `metadata.schema_version = 2`. Tant que la migration n'est pas faite, la doctrine reste **théorique**.

### ❌ INC-2 (BLOQUANT) — Champ `verbatim` absent en prod
- **Constat** : `STRATEGIE_KB_MASTER.md:67` exige verbatim sous peine de rejet ; les 1265 briques n'en ont aucun.
- **Impact** : règle d'or anti-hallucination déjà violée ; la doctrine (axe 3 traçabilité) ne réintroduit pas le verbatim.
- **Correctif** : soit (a) ajouter `verbatim` aux champs obligatoires de l'axe 1 et l'extraire lors de la migration, soit (b) acter formellement que le master courant est « sans verbatim » et abaisser STRATEGIE de « obligatoire » à « recommandé ». **Choix métier à trancher par Abdelkrim.**

### ⚠️ INC-3 — Trois conventions d'ID concurrentes
- **Constat** : `BLK-C2-timing-0042` (STRATEGIE:48) vs `ordres-stop-limite-piege` (PIPELINE:126) vs `domaine-sujet-concept-type` (doctrine axe 2).
- **Correctif** : choisir **une seule** convention et l'inscrire dans `STRATEGIE_KB_MASTER.md` comme autorité unique. Recommandation : la forme sémantique kebab `domaine-sujet-concept-type` (lisible, anti-collision, compatible idempotence).

### ⚠️ INC-4 — Statut par index positionnel (fragilité idempotence)
- **Constat** : `AUDIT_KB_RESULTS.json` lie statut↔`catégorie+index` ; insérer/supprimer une brique décale tous les index.
- **Correctif** : le contrôle de doublon (axe 2) et le lifecycle (axe 6) **exigent un `id` stable** porté par la brique elle-même, pas un index. → dépend de INC-1.

### ⚠️ INC-5 — Lifecycle (axe 6) vs vocabulaire A9
- **Constat** : draft/validée/active/dépréciée (doctrine) vs VALIDE/DOUTEUX/INVALIDE (A9, `REGISTRE_VALIDITE.md:4`) vs 6 états de ticket source.
- **Correctif** : publier une **table de correspondance** unique (ex. `active`=VALIDE, `dépréciée`=INVALIDE, `draft`=brique en `validation\`, `validée`=audit AUTO réussi). Confier la tenue à A9 pour éviter deux journaux de vérité.

### ⚠️ INC-6 — REGLE critiques dans le system prompt (cible non auditée)
- **Constat** : la doctrine copie les REGLE critiques dans le system prompt (`claude_brain.py`), hors du garde-fou `validation\`→audit→master (`PIPELINE…KB.md:114`).
- **Correctif** : étendre l'interdit « jamais d'écriture directe » au system prompt — toute REGLE promue au prompt doit d'abord être `active` dans le master audité, puis générée/synchronisée automatiquement.

---

## 3. SCORE DE COMPATIBILITÉ : **62 / 100**

| Dimension | Poids | Note | Commentaire |
|-----------|------:|-----:|-------------|
| Cohérence interne des 8 axes | 20 | 16 | Solide ; seule la taxonomie de statut chevauche l'existant. |
| Compat. schéma DOCUMENTÉ | 15 | 13 | La doctrine ré-énonce fidèlement `PIPELINE §7`. |
| Compat. schéma RÉEL (prod) | 30 | 9 | Écart majeur string↔objet ; migration obligatoire. |
| Compat. processus (interstice/validation) | 20 | 17 | Additive, 1 réserve (system prompt). |
| Compat. agents (A9/A4/A5) | 15 | 7 | Lifecycle à réconcilier avec A9. |
| **Total** | **100** | **62** | 🟡 GO conditionnel. |

### 3 RISQUES MAJEURS
1. **Migration silencieuse** : appliquer la doctrine sans migrer les 1265 strings → briques fantômes sans `id`/`type`, audit cassé. (INC-1/INC-4)
2. **Double vérité de statut** : lifecycle doctrine + statuts A9 + index audit + texte CLAUDE.md (`1166 VALIDE`) vs `AUDIT_KB_RESULTS.json` (`VALIDE:40`) déjà désynchronisés → source de confusion. (INC-5, E)
3. **Verbatim perdu** : anti-hallucination affaibli — la KB en prod n'a aucun verbatim alors que STRATEGIE le rend obligatoire. (INC-2)

---

## 4. VERDICT

🟡 **GO APRÈS 4 AJUSTEMENTS BLOQUANTS** (ne pas appliquer la doctrine en l'état) :

1. **Acter un schéma cible v2 + script de migration** string→objet (résout INC-1, INC-4).
2. **Trancher le sort du `verbatim`** : champ obligatoire migré, ou STRATEGIE assouplie (INC-2).
3. **Unifier la convention d'ID** dans `STRATEGIE_KB_MASTER.md` comme autorité unique (INC-3).
4. **Publier la table lifecycle↔statuts A9** et étendre l'interdit d'écriture au system prompt (INC-5, INC-6).

Les 8 axes sont **bons sur le fond** et cohérents avec la *doctrine documentée* ; ils sont
simplement **en avance sur le format réel** de la KB. Une fois la migration v2 décidée, le
passage en 🟢 GO est direct.

---

## 5. FAILLES CRITIQUES DÉTECTÉES PENDANT L'AUDIT (hors doctrine, à déclarer)

> Trouvailles incidentes lors de la lecture du périmètre. Aucune corrigée (lecture seule). À traiter séparément.

| # | Gravité | Faille | Preuve | Risque concret |
|---|---------|--------|--------|----------------|
| **F1** | 🔴 CRITIQUE | `AGENTS.md` est **gravement périmé et contradictoire** avec `CLAUDE.md` : modèle « **Codex-sonnet-4-6** » (nom inexistant), score « **17/21** », code dans `code\` (pas `05-saas\`), KB « 2337 règles ». | `AGENTS.md:51-52, 88, 157, 194` vs `CLAUDE.md:52, 90, 215` | Tout agent Codex qui lit `AGENTS.md` applique le scoring **abandonné /21**, de **mauvais chemins** et un **modèle fantôme** → décisions verrouillées violées. |
| **F2** | 🟠 ÉLEVÉ | **Statut des règles désynchronisé** entre 3 sources. `CLAUDE.md` = `1166 VALIDE`. `AUDIT_KB_RESULTS.json` = `VALIDE:40 / DOUTEUX:1225`. Master = aucun statut par règle. | `CLAUDE.md:258` vs `AUDIT_KB_RESULTS.json:5-9` | Aucune source de vérité unique sur « combien de règles sont fiables » → Mode Auto pourrait s'appuyer sur un compte faux. |
| **F3** | 🟠 ÉLEVÉ | **KB « provisoire » : contradiction**. `REGISTRE_VALIDITE.md` la marque ⚠️ DOUTEUX / PROVISOIRE ; `metadata.kb_provisoire=false` + `CLAUDE.md` la dit CANONIQUE. | `REGISTRE_VALIDITE.md:12, 67` vs `KNOWLEDGE_BASE_MASTER.json:31` | Le flag `kb_provisoire` pilote l'interdiction du Mode Auto (A5). Contradiction = porte d'Auto mal gardée. |
| **F4** | 🟠 ÉLEVÉ | **`verbatim` obligatoire jamais respecté** : 0 des 1265 règles n'a de verbatim, alors que STRATEGIE le rend obligatoire sous peine de rejet. | `STRATEGIE_KB_MASTER.md:67` vs `KNOWLEDGE_BASE_MASTER.json:100-123` | Anti-hallucination de façade : aucune règle n'est traçable à sa phrase-source dans le JSON. |
| **F5** | 🟡 MOYEN | **Cible volumétrique explosée** : STRATEGIE vise 300-600 règles « fiables » ; réalité = 1265. | `STRATEGIE_KB_MASTER.md:213` vs `CLAUDE.md:258` | Le tri qualité prévu (garder le meilleur) n'a pas eu lieu → dilution probable. |
| **F6** | 🟡 MOYEN | **Chemins périmés dans `GARDE_FOUS_PROPOSES.md`** : références `code/engine/...`, `code/config/...` au lieu de `05-saas\`. | `GARDE_FOUS_PROPOSES.md:28-48` | Doc de sécurité pointant des chemins inexistants → implémentation des 10 garde-fous manquants risque de viser le mauvais dossier. |
| **F7** | 🟡 MOYEN | **3 schémas de brique concurrents** documentés, aucun déclaré autorité unique, aucun ne décrit le format réel. | `STRATEGIE…md:46-65` vs `PIPELINE…md:124-138` vs `KNOWLEDGE_BASE_MASTER.json:100` | Toute personne/agent qui « suit la doc » fabrique des briques non fusionnables. |

**Priorité de traitement suggérée** : F1 (immédiat — corriger ou geler `AGENTS.md`) → F3 → F2 → F4 → F7 → F5/F6.

---

## 6. RECOMMANDATIONS AMÉLIORÉES (ma synthèse)

### 6.1 Geler le schéma AVANT d'enrichir
N'ajoutez **aucune** nouvelle brique tant que le schéma cible n'est pas figé. Sinon vous empilez
de la dette sur un format que vous allez devoir migrer. Ordre correct : **schéma v2 → migration → enrichissement**.

### 6.2 Adopter un schéma v2 minimal mais suffisant (proposition)
Plutôt que les 12+ champs de la doctrine d'un coup, viser un noyau **migrable automatiquement** depuis l'existant :
```json
{
  "id": "structure-marche-cassure-range-regle",   // kebab sémantique = convention UNIQUE
  "schema_version": 2,
  "type": "REGLE",                                  // DEFINITION | REGLE | PIEGE
  "fiabilite": "ECOLE_DE_PENSEE",                   // FAIT_STABLE | DEPEND_DU_BROKER | ECOLE_DE_PENSEE
  "statut": "active",                               // draft|validée|active|dépréciée (table mappée A9)
  "categorie": "structure_marche",
  "contenu": "Ne pas entrer sur la première cassure d'un range...",   // ≤ 60 mots
  "verbatim": null,                                 // null assumé pour l'héritage, obligatoire pour le NEUF
  "source_video_id": "-OIGv5rLLV8",                 // déjà présent au niveau vidéo → remonté
  "source_origine": "03-transcriptions/.../-OIGv5rLLV8_*.txt",
  "audit_score": null,                              // rempli par l'audit auto
  "date_ajout": "2026-06-16",
  "prerequis": [], "regle_associee": null, "mots_cles": []
}
```
Les 5 premiers champs sont **dérivables par script** depuis le master actuel (id = catégorie+slug, type/fiabilite par défaut + revue). `verbatim=null` toléré pour l'**hérité**, mais **obligatoire pour toute brique neuve** → l'anti-hallucination redevient vrai sans bloquer la migration.

### 6.3 Une seule source de vérité pour le statut
Migrer le statut **dans la brique** (champ `statut` + `audit_score`) et **supprimer** la dépendance à l'index positionnel d'`AUDIT_KB_RESULTS.json`. `REGISTRE_VALIDITE.md` (A9) reste le **journal**, mais ne duplique plus le compte ; `CLAUDE.md` cite ce journal au lieu d'un chiffre figé.

### 6.4 Idempotence par `id`, pas par texte
Le contrôle de doublon (axe 2) doit hasher l'`id` normalisé, pas la phrase (qui varie). Deux formulations du même concept → même `id` racine + suffixe → liées, jamais fusionnées en silence (cohérent avec `STRATEGIE…md:191-192`).

### 6.5 Verrouiller la cible d'écriture system prompt
Étendre le garde-fou « jamais d'écriture directe » (`PIPELINE…md:114`) : une REGLE n'entre dans le system prompt de `claude_brain.py` **que** si elle est `active` dans le master audité, et par **génération automatique** (pas copier-coller manuel). Sinon le prompt devient une 2ᵉ KB non auditée.

### 6.6 Éval de récupération (axe 8) = porte de fusion, pas décoration
Les 2-3 questions-test par lot doivent **bloquer** la fusion si la KB ne sait pas répondre (intégrer à l'étape 6 « AUDIT AUTO »). Sinon l'axe 8 est cosmétique.

### 6.7 Traiter F1 en priorité absolue
`AGENTS.md` est un piège actif. Deux options : (a) le réaligner sur `CLAUDE.md` (modèle `claude-sonnet-4-6`, /10, `05-saas\`), ou (b) y mettre un bandeau « OBSOLÈTE — autorité = CLAUDE.md » en tête. **Ne pas laisser deux sources de vérité divergentes.**

### 6.8 Décider le sort des 1265 vs cible 300-600
Soit assumer 1265 comme nouveau réel (mettre à jour STRATEGIE), soit lancer une passe de **consolidation qualité** (dédup + dépréciation des DOUTEUX) pour revenir à un corpus dense. À trancher par Abdelkrim — décision **métier**.

---

## 7. FICHIERS LUS (périmètre, lecture seule)
`STRATEGIE_KB_MASTER.md` · `PIPELINE_ENRICHISSEMENT_KB.md` · `GARDE_FOUS_PROPOSES.md` ·
`REGISTRE_VALIDITE.md` · `BACKLOG_ENRICHISSEMENTS.md` · `CLAUDE.md` · `AGENTS.md` ·
`04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` (schéma + métadonnées) ·
`04-cerveau-trading\AUDIT_KB_RESULTS.json` · `04-cerveau-trading\AUDIT_KB_RAPPORT_20260614_2316.md` ·
`04-cerveau-trading\processor_status.json` · `04-cerveau-trading\validation\KB_VALIDEE.json`.

**Note** : `00-pilotage\STRATEGIE_KB_MASTER.md` présent et lu. Aucun fichier du périmètre absent.

*Rapport généré le 2026-06-16 — LECTURE SEULE — aucun fichier existant modifié, aucune fusion lancée.*
