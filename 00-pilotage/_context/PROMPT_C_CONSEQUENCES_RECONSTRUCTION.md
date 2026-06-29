# PROMPT C — CONSÉQUENCES DE LA RECONSTRUCTION KB
> Cowork → Claude Code | S39 | 29/06/2026
> Étape 3/3 — À lancer UNIQUEMENT après validation des Rapports A et B par Abdelkrim

---

## PRÉ-REQUIS

Avant de commencer, confirmer :
- Rapport A validé par Abdelkrim (état des lieux complet)
- Rapport B validé par Abdelkrim (audit 10 phases sans bloquant)
- Aucun bloquant GO/NO-GO en suspens

---

## TA MISSION UNIQUE

Répondre à une seule question : **Que se passe-t-il exactement quand on reconstruit la KB ?**

Tu bases tes réponses UNIQUEMENT sur :
- Les mesures du Rapport A (chiffres réels)
- Les conclusions du Rapport B (code validé)
- Le code que tu peux lire maintenant

Aucune supposition. Aucun chiffre inventé. DONNÉES INSUFFISANTES si non mesurable.

---

## SECTION A — CE QUI SERA DÉTRUIT

### A1 — KNOWLEDGE_BASE_MASTER.json

Depuis le Rapport A :
- Nombre de règles qui seront écrasées : [reprendre M1]
- Détail par catégorie : [reprendre M1]
- Récupérabilité depuis git :

```powershell
git -C "C:\trading-copilote" log --oneline -- "04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json" | Select-Object -First 10
```

→ Combien de commits contiennent la KB ? La version actuelle (1398 règles) est-elle commitée ?
→ Si oui → récupérable via `git checkout {commit} -- 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json`

### A2 — Règles chapitres (id_brique + format id/contenu)

- Nombre de règles chapitres : [depuis Rapport A M1 = 62 règles, pas 14]
  - 14 règles format `id_brique`
  - 48 règles format `id`/`contenu`/`source_origine`
- Le script extract_chapter_rules.py corrigé (filtre `source_video_id not in e`) capture-t-il les 62 ? (réponse Phase 0 Rapport B)
- Sans la Phase 0 (backup), ces 62 règles sont-elles récupérables depuis git ? (réponse A1)
- Avec la Phase 0 (backup JSON) → récupérables à 100% ?

### A3 — Transcripts Whisper

- Nombre de fichiers Whisper : [depuis Rapport A M3]
- Si archivés dans `_archive\whisper-lessons-elimine\` → récupérables en les déplaçant de retour ?
- Ces transcripts sont-ils déjà commitées dans git ?

```powershell
git -C "C:\trading-copilote" ls-files "03-transcriptions/nouvelles-sources/belkhayate-youtube/transcripts/" | Measure-Object | Select-Object Count
```

### A4 — MANIFESTE_TRANSCRITS.csv

```python
import csv
with open(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print(f"Colonnes : {reader.fieldnames}")
    print(f"Lignes   : {len(rows)}")
    print(f"Exemple  : {rows[0] if rows else 'vide'}")
```

→ Sera-t-il encore valide après reconstruction ? (il pointe sur les transcripts Whisper → à adapter)

---

## SECTION B — CE QUI VA CASSER IMMÉDIATEMENT

### B5 — claude_brain.py au chargement de la KB

Lire la fonction de chargement de la KB dans `claude_brain.py` :

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" `
  -Pattern "def load|def get_kb|aggregated_rules|json.load|KB_FILE|KB_PATH" |
  Select-Object LineNumber, Line
```

→ Y a-t-il une validation JSON au chargement ? Un try/except ?
→ Si la KB est vide ou mal formée → exception levée ou valeur par défaut ?
→ Citer le code exact de la fonction de chargement.

### B6 — SHA256_KB_MASTER.md oublié

- Si on ne met pas à jour `SHA256_KB_MASTER.md` après reconstruction →
  TRADEX démarre-t-il quand même ? (Réponse attendue : OUI — c'est manuel)
- Quel est le seul impact ? (documentation désynchronisée)

### B7 — Tests potentiellement cassés

Lire `test_claude_brain.py` en entier et identifier :
- Les assertions sur le nombre de règles (recherche de `assert`, `assertEqual`, `>=`, chiffres)
- Les assertions sur la structure de la KB
- Les assertions qui supposent un seuil minimum de règles

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\test_claude_brain.py" `
  -Pattern "assert|assertEqual|>=|rules|count|total|1398|1300|minimum" -CaseInsensitive |
  Select-Object LineNumber, Line
```

→ Ces tests vont-ils échouer si le nombre de règles change ?
→ Ces tests vont-ils échouer si la structure JSON change ?

### B8 — transcript_processor.py : MANIFESTE et rebuild_aggregated

Lire la fonction qui lit le manifeste dans `transcript_processor.py` (lignes autour de MANIFEST_FILE) :

```powershell
Get-Content "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py" |
  Select-Object -Skip 170 -First 30
```

→ Que se passe-t-il exactement si MANIFESTE_TRANSCRITS.csv est absent ou vide ?
  (FileNotFoundError ? 0 règles silencieusement ? Exception bloquante ?)
→ Citer le code exact du try/except ou de la condition.

⚠️ RISQUE D17 : `rebuild_aggregated()` est-elle appelée dans cette même fonction ?
  Si oui → les 62 règles chapitres sont effacées à chaque vidéo traitée.
  → Citer le code de `rebuild_aggregated()` [l.282-294 environ].

---

## SECTION C — CE QUI VA CHANGER

### C9 — Nombre de règles

- Règles actuelles : [depuis Rapport A]
- Y a-t-il un seuil minimum de règles dans le code ?

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py", `
                    "C:\trading-copilote\05-saas\engine\test_claude_brain.py" `
  -Pattern "minimum|min_rules|seuil|threshold|800|1000|1300" -CaseInsensitive |
  Select-Object Filename, LineNumber, Line
```

→ Si aucun seuil → le moteur fonctionne avec N'IMPORTE quel nombre de règles, même 1 ?

### C10 — Qualité des signaux

Lire la fonction de génération de signal dans `claude_brain.py` :

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" `
  -Pattern "def.*signal|def.*analyze|def.*generate|aggregated_rules|inject|prompt" |
  Select-Object LineNumber, Line
```

→ Comment les règles KB sont-elles utilisées ? (injection dans prompt Claude ? RAG ? filtrage ?)
→ Si les règles changent de contenu → les signaux changent-ils de manière prévisible ?

### C11 — Les 11 catégories

- Si une catégorie disparaît ou change de nom dans la KB reconstruite :

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" `
  -Pattern "saisonnalite|correlations|timing|indicateurs_tendance|indicateurs_momentum|gestion_risque|gestion_position|structure_marche|macro_evenements|volume_liquidite|psychologie" |
  Select-Object LineNumber, Line
```

→ Ces catégories sont-elles hardcodées dans `claude_brain.py` ?
→ Si oui → quel module casse si une catégorie est absente ou renommée ?

### C12 — Mode Manuel vs Mode Auto

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" `
  -Pattern "AUTO_MODE|mode_auto|manuel|auto" -CaseInsensitive |
  Select-Object LineNumber, Line
```

→ La reconstruction KB affecte-t-elle les deux modes de la même façon ?
→ Le mode Auto reste-t-il BLOQUÉ indépendamment de la KB ?

---

## SECTION D — RISQUES CACHÉS

### D13 — Tous les lecteurs KB

(depuis Rapport A M4 — liste des 8 fichiers)

Pour chaque fichier de la liste :
- Lit-il seulement la KB (lecture) ou peut-il aussi la MODIFIER ?
- `purge_kb.py` : que fait-il exactement ? Peut-il effacer des règles Gemini si lancé pendant la reconstruction ?

```python
# Résumé pour chaque lecteur KB
fichiers_a_analyser = [
    r"C:\trading-copilote\05-saas\knowledge_base\audit_kb.py",
    r"C:\trading-copilote\05-saas\knowledge_base\purge_kb.py",
    r"C:\trading-copilote\05-saas\knowledge_base\validate_douteux.py",
    r"C:\trading-copilote\05-saas\knowledge_base\b05_lift_provisoire.py",
    r"C:\trading-copilote\05-saas\knowledge_base\b06_add_video10.py",
]
import re
for path in fichiers_a_analyser:
    try:
        with open(path) as f:
            content = f.read()
        writes = re.findall(r'(json\.dump|open.*"w"|replace|atomic)', content)
        print(f"{path.split(chr(92))[-1]}: LECTURE SEULE={'non' if writes else 'oui'} | écritures: {writes[:3]}")
    except FileNotFoundError:
        print(f"{path.split(chr(92))[-1]}: MANQUANT")
```

### D14 — Cache KB

```powershell
Get-ChildItem "C:\trading-copilote" -Recurse -Include "*.pkl","*.cache","*.pickle","*.joblib" -ErrorAction SilentlyContinue | Select-Object FullName
```

→ Y a-t-il un cache à invalider après reconstruction ?

### D15 — Clés API (FRED, EIA, FINNHUB)

⚠️ Rapport A M9 confirme : les 5 clés sont PRÉSENTES (dette soldée).
→ Vérifier seulement si transcript_processor.py les lit au démarrage (risque crash si absentes dans un autre env) :

```powershell
Select-String -Path "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py" `
  -Pattern "FRED|EIA|FINNHUB|FRED_API|EIA_API|FINNHUB_API" |
  Select-Object LineNumber, Line
```

→ Ces clés sont-elles utilisées dans transcript_processor.py ou seulement dans le moteur live ?

### D16 — Migration google-generativeai (depuis Rapport A M8)

→ Rapport A M8 : `google-genai` déjà utilisé dans `gemini_transcriber.py` (`from google import genai`) — NON bloquant.
→ `google-generativeai` 0.8.4 reste installé mais deprecated → FutureWarning, non bloquant.

### D17 — ⚠️ RISQUE CRITIQUE découvert en Rapport B : rebuild_aggregated() détruit les chapitres

Rapport B Risque #1 :

```python
# transcript_processor.py l.282-294 — vérifier
Select-String -Path "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py" `
  -Pattern "rebuild_aggregated|aggregated_rules|kb\[.videos.\]" |
  Select-Object LineNumber, Line
```

→ `rebuild_aggregated()` recrée `aggregated_rules` UNIQUEMENT depuis `kb["videos"][].rules`.
→ Les 62 règles chapitres vivent SEULEMENT dans `aggregated_rules` — jamais dans `videos[]`.
→ Conséquence : tout `save_kb_atomic()` après reconstruction efface définitivement les 62 règles.

Questions :
1. `rebuild_aggregated()` est-elle appelée automatiquement par le processeur après chaque vidéo ?
   Citer l'appel exact (ligne et contexte).
2. Peut-on patcher le processeur pour qu'il préserve les règles non-vidéo avant de reconstruire ?
   Citer le code de `rebuild_aggregated()` en entier.
3. ⚠️ Fragilité permanente : si on relance le processeur après Phase 8 → les chapitres disparaissent.
   Quelle est la parade ? (backup JSON toujours disponible → relancer inject uniquement)

---

## SECTION E — TABLEAU AVANT/APRÈS

Compléter avec les valeurs réelles des Rapports A et B :

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVANT RECONSTRUCTION              APRÈS RECONSTRUCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KB source      : Whisper           KB source      : Gemini multimodal
Règles totales : 1398               Règles totales : [INCONNU — estimé]
Règles vidéo   : 1336               Règles vidéo   : [INCONNU]
Règles chap.   : 62 (14+48)         Règles chap.   : 62 (si Ph.0+8 OK)
SHA256 actif   : bcaaaeed...        SHA256 actif   : [NOUVEAU — manuel]
Tests baseline : 69/69 PASS         Tests           : [À CONFIRMER après]
TRADEX démarre : OUI               TRADEX démarre  : OUI (SHA256=manuel)
Mode Auto      : BLOQUÉ            Mode Auto       : BLOQUÉ (inchangé)
Modules lisant KB : [M4 Rapport A] Modules lisant KB : [N] (inchangé)
Modules modifiant KB : [D13]       Modules à désactiver : [liste D13]
Cache KB       : [D14]             Cache à invalider : [D14]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SECTION F — VERDICT RISQUE

```
RISQUE GLOBAL       : [FAIBLE / MOYEN / ÉLEVÉ / CRITIQUE]

POINT DE NON-RETOUR : Phase [X]
  → Avant cette phase : rollback possible via git checkout
  → Après cette phase : rollback possible mais manuel (KB_BACKUP_WHISPER_1398.json)

BACKUP SUFFISANT    : [OUI / NON]
  → git tag KB-WHISPER-1398 : [présent / absent]
  → KB_BACKUP_WHISPER_1398.json : [présent / absent]
  → KB_CHAPTER_RULES_BACKUP.json : [sera créé en Phase 0]

MODULES À DÉSACTIVER pendant la reconstruction :
  → purge_kb.py (writer confirmé D13)
  → b05_lift_provisoire.py (writer confirmé D13)
  → b06_add_video10.py (writer confirmé D13)
  → apply_ambigu_verdicts.py (writer confirmé Rapport B Q10.5 : json.dump + os.replace)
  → ⚠️ transcript_processor.py lui-même après Phase 8 (rebuild_aggregated efface chapitres)

RECOMMANDATION : [GO / GO CONDITIONNEL / NO-GO]
  → Condition précise si GO CONDITIONNEL :
```

---

## FORMAT DU RAPPORT C

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPPORT C — CONSÉQUENCES RECONSTRUCTION KB — TRADEX-AI S39
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A — CE QUI SERA DÉTRUIT
[Réponses A1-A4]

B — CE QUI VA CASSER
[Réponses B5-B8 avec lignes de code exactes]

C — CE QUI VA CHANGER
[Réponses C9-C12]

D — RISQUES CACHÉS
[Réponses D13-D16]

E — TABLEAU AVANT/APRÈS
[Tableau complété avec valeurs réelles]

F — VERDICT RISQUE
RISQUE GLOBAL       :
POINT DE NON-RETOUR :
BACKUP SUFFISANT    :
MODULES À DÉSACTIVER:
RECOMMANDATION      :

━━━ PREMIÈRE COMMANDE POUR ABDELKRIM ━━━
[La toute première commande PowerShell à exécuter dans C:\trading-copilote\]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## RÈGLES ABSOLUES

- Baser TOUTES les réponses sur le code réel et les Rapports A et B
- DONNÉES INSUFFISANTES pour tout chiffre non mesurable (ex: nombre de règles après reconstruction)
- Ne jamais modifier un fichier dans ce prompt
- Ne pas relire les fichiers déjà cités dans les Rapports A et B sauf si nécessaire

---

*Prompt C — 3/3 — Cowork S39 — 29/06/2026*
*Pré-requis : Rapports A et B validés par Abdelkrim*
