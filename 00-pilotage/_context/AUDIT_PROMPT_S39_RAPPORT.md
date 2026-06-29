# AUDIT PROMPT — RAPPORT 12 PASSES
> Prompt audité : PROMPT_CLAUDE_CODE_S39_AUDIT_STRATEGIE.md
> Auditeur : Cowork (basé sur lecture code réel) | S39 | 29/06/2026

---

## 1. VERDICT EXÉCUTIF

```
Score global      : 65/100
Statut            : À CORRIGER
Niveau de danger  : MOYEN
Utilisable tel quel ? NON — 6 erreurs factuelles bloquantes
Décision          : CORRIGER avant envoi à Claude Code
```

---

## 2. RÉSUMÉ DES PROBLÈMES MAJEURS

| Gravité | Problème | Impact | Correction |
|---------|----------|--------|------------|
| 🔴 CRITIQUE | `KB_HASH.txt` n'existe pas | Claude Code va chercher un fichier absent → rapport faux sur Phase 9 | Remplacer par `SHA256_KB_MASTER.md` |
| 🔴 CRITIQUE | `05-saas\tests\` n'existe pas | `py -m pytest 05-saas\tests\` va ÉCHOUER | Les tests sont dans `05-saas\engine\` et `05-saas\api\` |
| 🔴 CRITIQUE | SHA256 NON vérifié par le code | claude_brain.py ne contient aucun check SHA256 → Phase 9 repose sur un mécanisme fantôme | SHA256_KB_MASTER.md est un REGISTRE MANUEL, pas un garde-fou automatique |
| 🔴 CRITIQUE | 8 fichiers lisent la KB (pas 1) | Cowork dit "seul claude_brain.py lit la KB" → FAUX | audit_kb.py, purge_kb.py, validate_douteux.py, b05, b06, settings.py lisent tous la KB |
| 🟠 ÉLEVÉ | `extract_chapter_rules.py` absent | Claude Code ne peut pas valider "le code est-il correct ?" sans code à lire | Fournir le code dans le prompt |
| 🟠 ÉLEVÉ | `inject_chapter_rules.py` absent | Idem Phase 8 | Fournir le code dans le prompt |
| 🟡 MOYEN | Ordre Étape 4 avant Étape 5 | Format défini avant le contenu → confusion structurelle | Inverser ou fusionner |
| 🟡 MOYEN | SHA256 actif ≠ "bcaaaeed" | Le tableau avant/après dit `bcaaaeed` mais le vrai hash actif est `4cc9f77a...` | Corriger la valeur dans le tableau |
| 🟡 MOYEN | Phase 7 : coût tokens invitable | Les MP4 n'existent pas encore → impossible à mesurer → hallucination garantie | Ajouter "→ DONNÉES INSUFFISANTES si non mesurable" |
| 🟡 MOYEN | Grep D13 sans commande | "grep KNOWLEDGE_BASE_MASTER" sans commande PowerShell → résultat variable | Fournir la commande exacte |

---

## 3. AUDIT DÉTAILLÉ — 12 PASSES

### P1 — PÉRIMÈTRE & OBJECTIF : À CORRIGER (4/6)
- ✅ Mission claire : auditer la stratégie + rapport conséquences
- ✅ Ordre de lecture des fichiers référence bien défini
- ❌ Étape 4 (FORMAT RAPPORT) placée AVANT Étape 5 (CONTENU CONSÉQUENCES). Étape 4 référence des sections A-F qui ne sont définies qu'en Étape 5 → Claude Code risque de produire un rapport incomplet
- ❌ "Aucune politesse. Aucun résumé." puis "Améliorations suggérées" dans le format : contradiction de ton

### P2 — ANTI-HALLUCINATION : À CORRIGER (7/14)
- ✅ "Ne jamais inventer un chiffre" est bien là
- ❌ `KB_HASH.txt` n'existe PAS → Claude Code va répondre "fichier manquant" alors qu'il doit pointer sur `SHA256_KB_MASTER.md`
- ❌ Phase 9 : "Faut-il mettre à jour 1 ou 2 fichiers ?" → la réponse attendue suppose que claude_brain.py vérifie le hash. FAUX. Aucun check automatique dans le code. Claude Code va inventer un mécanisme.
- ❌ Phase 7 : "Coût estimé : X tokens × 110 vidéos" → les vidéos n'existent pas encore, calcul impossible, hallucination garantie
- ❌ "37 tests" présenté comme un fait alors que le dossier `05-saas\tests\` n'existe pas. Les tests sont dispersés dans `05-saas\engine\` et `05-saas\api\`

### P3 — VALIDITÉ STATISTIQUE/BACKTEST : N/A
Prompt technique, pas de signal de trading. Passe non applicable.

### P4 — LOGIQUE DE TRADING : N/A
Pas de logique de signal dans ce prompt. Passe non applicable.

### P5 — INTERMARCHÉ : N/A

### P6 — VOLUME/OI/COT : N/A

### P7 — NEWS/MACRO/MIGRATION BLOQUANTE : DONNÉES PARTIELLES (6/8)
- ✅ Question D16 sur migration `google-generativeai → google-genai` est posée (DETTE §5)
- ❌ Pas de plan d'action si D16 = "OUI bloquant". Le prompt demande de signaler mais ne dit pas : "Si bloquant → STOP, ne pas continuer, reporter à Cowork immédiatement"
- ❌ La migration est listée dans "risques cachés" alors que c'est un BLOQUANT POTENTIEL pour Phase 4 (transcription Gemini)

### P8 — RISQUE/EXÉCUTION : À CORRIGER (8/11)
- ✅ Rate-limiting YouTube mentionné (sleep-interval 5s)
- ✅ `--continue` pour reprendre les téléchargements
- ❌ Espace disque D:\ non vérifié. 110 MP4 ≈ 5-30 Go selon durée. Le prompt ne demande pas `Get-PSDrive D` avant téléchargement
- ❌ Si yt-dlp bloque sur YouTube (403/429), le prompt dit "STOP sur Phase 2" mais ne donne pas de commande de fallback ni de seuil (5 vidéos bloquées = STOP ? 50 ?)

### P9 — PSYCHOLOGIE : N/A

### P10 — SAAS/ARCHITECTURE IA : À CORRIGER (8/15)
- ✅ Le prompt demande de lire les 3 fichiers Python clés
- ✅ Scripts Python fournis pour vérifier la KB
- ❌ **ERREUR CRITIQUE** : `05-saas\tests\` n'existe pas → la commande pytest dans le format de rapport va échouer
  - Tests réels : `05-saas\engine\test_*.py` + `05-saas\api\test_api.py`
  - Commande correcte : `py -m pytest 05-saas\engine\ 05-saas\api\ -v`
- ❌ **ERREUR CRITIQUE** : 8 fichiers lisent `KNOWLEDGE_BASE_MASTER.json`, pas 1 seul :
  - `claude_brain.py`, `audit_kb.py`, `b05_lift_provisoire.py`, `b06_add_video10.py`, `purge_kb.py`, `transcript_processor.py`, `validate_douteux.py`, `settings.py`
  - Conséquence : la reconstruction KB affecte 8 modules, pas 1
- ❌ `extract_chapter_rules.py` et `inject_chapter_rules.py` n'existent pas → Claude Code devra les inventer sans modèle de référence
- ❌ Pas de checkpoint STOP entre les étapes → Claude Code peut faire tout l'audit en une passe sans signaler les blocages au fur et à mesure

### P11 — RÉGLEMENTAIRE : VALIDÉ (6/6)
- ✅ Usage personnel confirmé
- ✅ ANTHROPIC_API_KEY via os.getenv (jamais dans le code)
- ✅ Disclaimer légal TRADEX non affecté par la reconstruction KB

### P12 — SCORE GLOBAL : 65/100 → MOYEN

---

## 4. CONTRADICTIONS INTERNES

| Contradiction | Emplacement | Impact |
|---|---|---|
| SHA256 = "bcaaaeed" dans tableau E vs hash actif = "4cc9f77a..." dans SHA256_KB_MASTER.md | Étape 5 tableau E | Claude Code va signaler une incohérence et perdre du temps |
| "Ne jamais inventer" + "Coût estimé tokens×110" | Règles absolues vs Phase 7 | L'invitation à estimer contredit la règle anti-hallucination |
| Étape 4 référence sections A-F définis seulement en Étape 5 | Structure du prompt | Claude Code peut produire Étape 4 avec des sections vides |
| "37 tests" comme fait acquis vs dossier `05-saas\tests\` inexistant | Phase 10 + Étape 4 | Claude Code obtiendra 0 résultats et sera confus |

---

## 5. HALLUCINATIONS / AFFIRMATIONS NON PROUVÉES

| Affirmation dans le prompt | Type de risque | Réalité vérifiée |
|---|---|---|
| "KB_HASH.txt" à vérifier | Fichier fantôme | N'existe pas. Fichier réel : `SHA256_KB_MASTER.md` |
| "py -m pytest 05-saas\tests\ -v" | Commande qui va échouer | Dossier `tests\` absent. Vrais tests dans `engine\` et `api\` |
| "SHA256 non mis à jour → TRADEX refuse de démarrer" | Mécanisme fantôme | `claude_brain.py` ne contient aucune vérification SHA256 automatique |
| "seul claude_brain.py lit la KB" (implicite) | Sous-estimation | 8 fichiers lisent KNOWLEDGE_BASE_MASTER.json |
| SHA256 actif = "bcaaaeed" | Valeur incorrecte | Valeur réelle : `4cc9f77a0fe18887...` |

---

## 6. VALIDITÉ STATISTIQUE/BACKTEST : N/A

---

## 7. RISQUES NON COUVERTS

| Risque | Gravité | Pourquoi l'ajouter |
|---|---|---|
| 8 fichiers KB → 8 modules à valider après reconstruction | 🔴 CRITIQUE | purge_kb.py peut écraser la KB reconstruite si lancé par erreur |
| `b05_lift_provisoire.py` et `b06_add_video10.py` dans `knowledge_base/` | 🟠 ÉLEVÉ | Ces scripts modifient la KB — doivent-ils être désactivés pendant la reconstruction ? |
| Espace disque D:\ avant téléchargement 110 MP4 | 🟡 MOYEN | 110 vidéos YouTube ≈ 5-30 Go selon durée |
| SHA256_KB_MASTER.md est un REGISTRE MANUEL | 🟡 MOYEN | Si on oublie de le mettre à jour, aucun système ne bloque — c'est juste de la documentation |
| Migration google-generativeai → google-genai (DETTE §5) | 🟠 ÉLEVÉ | Bloquant pour Phase 4 si lib non installée — traité comme "risque caché" alors que c'est un PRÉ-REQUIS |

---

## 8. RISQUES SAAS/IA NON COUVERTS

| Module manquant | Impact | Recommandation |
|---|---|---|
| `purge_kb.py` — peut effacer des règles pendant la reconstruction | Perte de règles Gemini si lancé accidentellement | Demander à Claude Code de vérifier si ce script est en mode automatique ou manuel |
| `audit_kb.py` — audit de la KB qui lit la KB | Si lancé sur KB en cours de reconstruction → rapport faux | Désactiver pendant la reconstruction |
| `settings.py` → `KB_PATH` — la config lit la KB | Si le chemin change → tous les modules cassent | Confirmer que KB_PATH reste identique après reconstruction |

---

## 9. CHECKLIST DE CORRECTION DU PROMPT

```
[ ] 1. Remplacer "KB_HASH.txt" par "SHA256_KB_MASTER.md" PARTOUT dans le prompt
[ ] 2. Corriger les chemins des tests : "05-saas\engine\ + 05-saas\api\" (pas 05-saas\tests\)
[ ] 3. Ajouter la commande pytest correcte : py -m pytest 05-saas\engine\ 05-saas\api\ -v
[ ] 4. Retirer "SHA256 non mis à jour → TRADEX refuse de démarrer" — FAUX
[ ] 5. Ajouter : "SHA256_KB_MASTER.md est un registre MANUEL — mettre à jour la ligne 'Hash actif'"
[ ] 6. Ajouter grep D13 avec commande exacte :
       Select-String -Path "C:\trading-copilote\**\*.py" -Pattern "KNOWLEDGE_BASE_MASTER" -Recurse
[ ] 7. Mentionner les 8 fichiers qui lisent la KB (pas seulement claude_brain.py)
[ ] 8. Fournir le code de extract_chapter_rules.py dans le prompt (il n'existe pas)
[ ] 9. Fournir le code de inject_chapter_rules.py dans le prompt (il n'existe pas)
[ ] 10. Corriger SHA256 dans tableau E : "4cc9f77a..." (pas "bcaaaeed")
[ ] 11. Déplacer Étape 5 AVANT Étape 4, ou ajouter "→ voir Étape 5 pour le contenu"
[ ] 12. Ajouter vérification espace disque D:\ : Get-PSDrive D
[ ] 13. Si D16 (migration) = bloquant → STOP immédiat, ne pas continuer
[ ] 14. Phase 7 : "Coût estimé" → ajouter "→ DONNÉES INSUFFISANTES si MP4 non encore téléchargés"
[ ] 15. Corriger "37 tests" → "Compter les tests dans 05-saas\engine\ et 05-saas\api\"
```

---

## 10. VERSION CORRIGÉE DU PROMPT — DIFF MINIMAL

### Correction 1 — KB_HASH.txt → SHA256_KB_MASTER.md
```
# REMPLACER partout "KB_HASH.txt" par :
# → SHA256_KB_MASTER.md (section "## Hash actif")

# Phase 9 — AVANT (FAUX) :
"claude_brain.py vérifie le hash → TRADEX refuse de démarrer"

# Phase 9 — APRÈS (CORRECT) :
"SHA256_KB_MASTER.md est un REGISTRE MANUEL.
Aucun code ne vérifie ce hash automatiquement.
Après reconstruction → mettre à jour la ligne '## Hash actif' dans SHA256_KB_MASTER.md
avec le nouveau SHA256 calculé via PowerShell :
(Get-FileHash 'C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json' -Algorithm SHA256).Hash"
```

### Correction 2 — Tests dans le bon dossier
```
# REMPLACER :
py -m pytest 05-saas\tests\ -v

# PAR :
py -m pytest 05-saas\engine\test_claude_brain.py 05-saas\engine\test_signal_engine.py 05-saas\engine\test_risk_guardrails.py 05-saas\engine\test_belkhayate_formulas.py 05-saas\api\test_api.py -v
```

### Correction 3 — Grep D13
```
# AJOUTER commande exacte pour D13 :
Select-String -Path "C:\trading-copilote\05-saas\**\*.py" -Pattern "KNOWLEDGE_BASE_MASTER" -Recurse

# Résultat attendu (8 fichiers) :
# claude_brain.py, audit_kb.py, b05_lift_provisoire.py, b06_add_video10.py,
# purge_kb.py, transcript_processor.py, validate_douteux.py, settings.py
```

### Correction 4 — Scripts manquants
```
# AJOUTER en Phase 0 et Phase 8 — Code exact à créer :

# === extract_chapter_rules.py ===
import json, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")

with open(KB_FILE, encoding="utf-8") as f:
    kb = json.load(f)

chapters = {}
count = 0
for cat, entries in kb.get("aggregated_rules", {}).items():
    for e in entries:
        if "id_brique" in e:
            if cat not in chapters:
                chapters[cat] = []
            chapters[cat].append(e)
            count += 1

with open(BACKUP_FILE, "w", encoding="utf-8") as f:
    json.dump({"chapter_rules": chapters, "total": count}, f, ensure_ascii=False, indent=2)
print(f"Sauvegardé : {count} règles chapitres dans {BACKUP_FILE}")
```

### Correction 5 — Migration bloquante
```
# MODIFIER D16 :
# AVANT : "est-elle bloquante pour lancer gemini_transcriber.py aujourd'hui ?"
# APRÈS :
"est-elle bloquante pour lancer gemini_transcriber.py aujourd'hui ?
→ Vérifier : py -c 'import google.generativeai; print(google.generativeai.__version__)'
→ Si ImportError OU version < 0.8 → STOP IMMÉDIAT. Reporter à Cowork. Ne pas continuer.
→ Solution : pip install google-generativeai --upgrade --break-system-packages"
```

---

## VERDICT FINAL

```
SCORE           : 65/100 → MOYEN
STATUT          : À CORRIGER — 15 corrections à appliquer
ERREURS FATALES : 4 (KB_HASH.txt fantôme, tests mauvais dossier, SHA256 non vérifié, 8 lecteurs KB)
RISQUE SI ENVOYÉ TEL QUEL : Claude Code va produire un rapport avec des informations fausses
                            sur Phase 9 (SHA256) et Phase 10 (tests) — deux phases critiques

RECOMMANDATION  : Appliquer les 15 corrections → score estimé 90/100 → envoi possible
TEMPS CORRECTION : 20 min
```

---

*Audit réalisé sur code réel — S39 — 29/06/2026*
*Fichiers lus : gemini_transcriber.py · claude_brain.py · transcript_processor.py · SHA256_KB_MASTER.md · structure projet*
