# PROMPT CLAUDE CODE — ÉTAPE 6 PIPELINE KB
# Audit automatique — Ticket 0.b · KB_CHAP5_BELKHAYATE.json · S18 · 2026-06-20

## CONTEXTE

Projet : TRADEX-AI — `C:\trading-copilote\`
Mission : auditer les 14 briques de `04-cerveau-trading\validation\KB_CHAP5_BELKHAYATE.json`.
Source : `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap5_Methode_Belkhayate.md`
Cette source est un **document de synthèse Couche 2** (méthode Belkhayate) — pas une transcription SRT.
Conséquence : le verbatim YouTube direct est impossible → appliquer la grille d'audit "document de synthèse".

**RÈGLE ABSOLUE** : Ne rien écrire dans KNOWLEDGE_BASE_MASTER.json ni KB_VALIDEE.json.
Écrire UNIQUEMENT dans `04-cerveau-trading\validation\REGISTRE_VALIDITE.md`.

---

## ÉTAPES À EXÉCUTER

### 1. Lire les fichiers d'entrée

- `04-cerveau-trading\validation\KB_CHAP5_BELKHAYATE.json` → les 14 briques à auditer
- `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap5_Methode_Belkhayate.md` → la source originale
- `04-cerveau-trading\KB_VALIDEE.json` → pour détecter les doublons (chercher dans `regles` et `ajouts_manuels`)

### 2. Appliquer la grille d'audit sur chaque brique

Pour chaque brique (id, titre, contenu, type, fiabilite) :

**CRITÈRE A — Source tracée** (1 pt)
→ `source_origine` pointe vers un fichier qui existe dans `02-sources-brutes\`
→ ✅ +1 si le fichier existe / ❌ 0 si introuvable

**CRITÈRE B — Cohérence type ↔ contenu** (1 pt)
→ DEFINITION = décrit un concept, ne prescrit pas de comportement
→ REGLE = prescrit une action ou un comportement
→ PIEGE = avertit d'une erreur à éviter
→ ✅ +1 si cohérent / ❌ 0 si type mal assigné

**CRITÈRE C — Fiabilité appropriée** (1 pt)
→ FAIT_STABLE : réservé aux faits documentés par ≥ 2 sources indépendantes OU mathématiquement vérifiables
→ ECOLE_DE_PENSEE : pour les affirmations propres à la méthode Belkhayate non prouvées universellement
→ ✅ +1 si la fiabilite est justifiable / ❌ 0 si incohérente (ex: FAIT_STABLE sur une opinion d'école)

**CRITÈRE D — Absence de chiffres inventés** (1 pt)
→ Tout chiffre dans `contenu` doit être soit vague ("plusieurs", "longtemps"), soit sourcé dans la brique elle-même
→ Les chiffres "80%", "90%", "95%", "3 déviations", "0,618", "1,618" → acceptables car cités avec contexte de source
→ ❌ 0 si un chiffre précis est affirmé sans contexte de source
→ ✅ +1 si tous les chiffres sont correctement contextualisés ou absents

**CRITÈRE E — Titre = reflet exact du contenu** (1 pt)
→ Le titre ne doit pas promettre plus que le contenu ne dit
→ ✅ +1 si le titre est un résumé honnête / ❌ 0 si dérive

**CRITÈRE F — Pas de doublon évident dans KB_VALIDEE.json** (1 pt)
→ Chercher si une règle IDENTIQUE (même concept, même sens) existe déjà
→ Des formulations différentes du même concept = doublon → signaler mais ne pas bloquer
→ ✅ +1 si aucun doublon exact / ❌ 0 si doublon exact trouvé

**Score max par brique : 6 pts**
**Seuil d'acceptation par brique : ≥ 4 / 6**
**Seuil global d'acceptation : ≥ 80% des briques ≥ 4 / 6**

### 3. Calculer le score global et décider

```
Total briques : 14
Briques ≥ 4/6 : [calculer]
Pourcentage : [x/14 × 100]%
Verdict : VALIDE (≥ 80%) ou BLOQUÉ (< 80%)
```

### 4. Vérifier aussi : doublons entre les 14 briques elles-mêmes

Si deux briques dans KB_CHAP5_BELKHAYATE.json couvrent le même concept → signaler les IDs concernés.

### 5. Mettre à jour REGISTRE_VALIDITE.md

Ajouter après l'entrée existante du 2026-06-20 :

```markdown
### AUDIT AUTOMATIQUE — [2026-06-20]

**Fichier audité :** 04-cerveau-trading/validation/KB_CHAP5_BELKHAYATE.json
**Grille appliquée :** document-de-synthese-couche2 (pas verbatim SRT — source = TRADEX_KB_Chap5.md)

| id | A | B | C | D | E | F | Score | Verdict |
|----|---|---|---|---|---|---|-------|---------|
| cog-structure-visuelle | | | | | | | /6 | |
| cog-bandes-nombre-or | | | | | | | /6 | |
| cog-logique-mean-reversion | | | | | | | /6 | |
| timing-structure-zones | | | | | | | /6 | |
| timing-biais-directionnel | | | | | | | /6 | |
| setup-type-confluence | | | | | | | /6 | |
| objectifs-sortie-cog | | | | | | | /6 | |
| filtre-tendance-htf | | | | | | | /6 | |
| confluence-cog-timing-vwap-volume | | | | | | | /6 | |
| piege-repainting-cog | | | | | | | /6 | |
| piege-biais-reversion-tendance-forte | | | | | | | /6 | |
| piege-versions-tierces-divergentes | | | | | | | /6 | |
| piege-formule-proprietaire | | | | | | | /6 | |
| piege-claims-performance-non-prouves | | | | | | | /6 | |

**Score global :** X/14 briques ≥ 4/6 → X%
**Verdict final :** [VALIDE → passer Étape 7] ou [BLOQUÉ → raison en 1 ligne]

**Doublons détectés entre briques :** [aucun / liste]
**Doublons avec KB_VALIDEE.json :** [aucun / liste]
**Briques sous le seuil (< 4/6) :** [aucune / liste avec raison]
```

### 6. Si verdict VALIDE → mettre le ticket à jour dans BACKLOG

Fichier : `00-pilotage\BACKLOG_ENRICHISSEMENTS.md`
Changer `⚙️ EN EXÉCUTION` → `🔀 À FUSIONNER` pour le ticket 0.b

### 7. Si verdict VALIDE → annoncer à Cowork

```
✅ AUDIT TERMINÉ — Ticket 0.b
Score : X/14 briques valides (X%)
Verdict : VALIDE
Ticket 0.b → 🔀 À FUSIONNER
Prêt pour Étape 7 (fusion dans KB_VALIDEE.json + KB MASTER)
```

### 8. Si verdict BLOQUÉ → NE PAS passer à l'Étape 7

```
❌ AUDIT BLOQUÉ — Ticket 0.b
Score : X/14 briques valides (X% < seuil 80%)
Briques bloquantes : [IDs]
Raison : [1 ligne par brique bloquante]
Action requise : correction des briques concernées avant fusion
```

### 9. Commit

```powershell
cd C:\trading-copilote
git add 04-cerveau-trading/validation/REGISTRE_VALIDITE.md 00-pilotage/BACKLOG_ENRICHISSEMENTS.md
git commit -m "feat(KB): audit ticket 0.b Chap5 - verdict [VALIDE/BLOQUE]"
```

---

## RÈGLES ANTI-HALLUCINATION POUR L'AUDIT

1. Ne pas inventer des scores — remplir la grille brique par brique, critère par critère
2. Si tu ne peux pas vérifier un critère (ex: fichier source introuvable) → noter ❌ et expliquer pourquoi
3. Ne pas arrondir à la hausse un score pour forcer un verdict VALIDE
4. Les PIEGE avec FAIT_STABLE sont intentionnels : le repainting est un fait documenté, la formule propriétaire est un fait documenté → ne pas les déclasser
5. Les DEFINITION/REGLE avec ECOLE_DE_PENSEE sont intentionnels : les affirmations Belkhayate ne sont pas universellement prouvées → correct

---

*Généré par Cowork — Session S18 · 2026-06-20 · Pipeline Enrichissement KB Étape 6*
