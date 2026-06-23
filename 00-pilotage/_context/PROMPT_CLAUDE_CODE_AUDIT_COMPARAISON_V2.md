# PROMPT CLAUDE CODE — AUDIT COMPARAISON TRANSCRITS BELKHAYATE V2
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code

---

Tu es l'orchestrateur d'une equipe de 4 agents specialises.
Mission : comparer les 110 videos Belkhayate presentes dans les 2 sources,
evaluer la fiabilite de chaque transcription, et identifier les regles trading
les plus solides pour la KB TRADEX-AI.

## CONTEXTE EXACT (verifie par inventaire dff89f1)

SOURCE A — bruts YouTube (MP3 via yt-dlp → Whisper) :
  C:\trading-copilote\03-transcriptions\transcripts-bruts\
  142 fichiers nommes whisper_[videoID].txt

SOURCE B — local MP4 (D:\Belkhayate-Videos → Whisper) :
  C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\
  164 fichiers (dont 110 correspondances avec SOURCE A, 54 uniques)

INVENTAIRE DISPONIBLE :
  C:\trading-copilote\00-pilotage\INVENTAIRE_TRANSCRITS_BELKHAYATE.md
  (contient les listes completes et les 110 paires de doublons)

MANIFESTE QUALITE :
  C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv
  109 VALIDE / 1 HORS_PERIMETRE

KB ACTUELLE :
  C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
  (1313 regles — NE PAS MODIFIER)

---

## ETAPE 0 — LECTURE INVENTAIRE (toi, avant de lancer les agents)

Avant tout, lire :
  C:\trading-copilote\00-pilotage\INVENTAIRE_TRANSCRITS_BELKHAYATE.md

Extraire la liste des 110 paires (videoID present dans A et B).
Selectionner un echantillon de 20 paires representatif :
  - 5 paires parmi les lecons numerotees (Lecon 1-30)
  - 5 paires parmi les lecons avancees (Lecon 31-50 ou Lesson 38-50)
  - 5 paires parmi les videos thematiques (or, ble, petrole, psychologie)
  - 5 paires parmi les videos de trading live

Lance ensuite les 4 agents avec ces 20 paires comme perimetre.

---

## AGENT 1 — COMPARATEUR QUALITE TRANSCRIPTION

Role : Pour chaque paire, comparer la qualite brute des 2 versions.

Pour chacune des 20 paires selectionnees :
1. Lire les 80 premieres lignes de la version SOURCE A (whisper_[ID].txt)
2. Lire les 80 premieres lignes de la version SOURCE B ([nom lisible].txt)
3. Evaluer pour chaque version :
   - Clarte du texte (lisible ou charabia ?)
   - Presence du nom "Belkhayate" ou termes methode
   - Densite d'information trading (beaucoup de contenu utile ou bavardage ?)
4. Pour chaque paire, conclure : A meilleure / B meilleure / equivalentes

Livrable : tableau 20 lignes [videoID | titre | A_score | B_score | meilleure_version]

---

## AGENT 2 — EXTRACTEUR DE REGLES TRADING

Role : Extraire les regles et techniques Belkhayate explicites de la meilleure version de chaque paire.

Pour chacune des 20 paires :
1. Prendre la version jugee meilleure par Agent 1 (ou B par defaut si equivalentes)
2. Lire jusqu'a 150 lignes
3. Extraire UNIQUEMENT les regles formulees explicitement :
   - Centre de Gravite (COG / Gravity Center) : position prix par rapport au COG
   - Timing : signaux de timing, couloir horaire
   - Pivots : utilisation des niveaux pivot
   - Energie / Direction : interpretation des indicateurs
   - Entree / Sortie : conditions exactes d'entree et de sortie
   - Stop Loss / Take Profit : placement et gestion
   - Inter-marches : correlations or/petrole/indices
   - Psychologie : discipline, patience, gestion emotionnelle

Format pour chaque regle :
  REGLE : [texte de la regle]
  SOURCE : [nom fichier exact]
  VERBATIM : "[citation courte entre guillemets]"
  CATEGORIE : [COG | Timing | Pivots | Energie | Entree | SL_TP | Inter-marches | Psychologie]

Contrainte absolue : JAMAIS inventer une regle. Si aucune regle claire dans 150 lignes → noter "PEU DE CONTENU TRADING".

Livrable : liste structuree des regles par video

---

## AGENT 3 — DETECTEUR DE COHERENCE ET EVOLUTION

Role : Analyser si la methode Belkhayate est coherente entre les anciennes et nouvelles videos.

Instructions (utiliser les resultats de l'Agent 2) :
1. Grouper les regles par CATEGORIE
2. Pour chaque categorie, verifier :
   - Les regles des vieilles videos (Lecon 1-20) sont-elles identiques aux nouvelles (Lesson 38-50) ?
   - Y a-t-il des contradictions (regle A dit "acheter quand X" et regle B dit "ne pas acheter quand X") ?
   - Y a-t-il des evolutions normales (methode affinee avec le temps) ?
3. Produire un verdict par categorie :
   COHERENT / EVOLUE / CONTRADICTION / INSUFFISANT (pas assez de donnees)
4. Conclusion generale : la methode Belkhayate est-elle stable ? A-t-elle evolue ?
5. Identifier les 3 regles les plus constantes (mentionnees dans plusieurs videos differentes)
6. Identifier les 3 sujets ou la comparaison est impossible (videos trop differentes pour comparer)

Livrable : section coherence avec verdicts par categorie + conclusion

---

## AGENT 4 — CLASSEMENT FIABILITE ET RECOMMANDATIONS KB

Role : Classer les 20 paires par fiabilite et recommander les meilleures pour la KB.

Pour chaque paire :
1. Score fiabilite /10 :
   - Clarte des regles exprimees (0-3 pts)
   - Presence de verbatims Belkhayate identifiables (0-2 pts)
   - Score MANIFESTE_TRANSCRITS.csv — lire colonne score pour ce fichier (0-2 pts, normalise)
   - Coherence interne du transcript (pas de contradiction dans le meme fichier) (0-2 pts)
   - Unicite (apporte quelque chose que les autres videos ne couvrent pas) (0-1 pt)
2. Verifier si les regles du transcript sont deja dans la KB :
   - Lire les 50 premieres regles de KNOWLEDGE_BASE_MASTER.json pour reference
   - Marquer chaque regle : DEJA_EN_KB / NOUVELLE / PARTIELLE
3. Produire Top 10 des transcrits les plus fiables avec score /10
4. Recommander 5 transcrits a integrer en priorite dans la prochaine session KB

Livrable : tableau Top 10 + liste 5 recommandations prioritaires

---

## RAPPORT FINAL (toi, orchestrateur)

Apres reception des 4 livrables, creer :
C:\trading-copilote\00-pilotage\RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md

```
# RAPPORT AUDIT COMPARAISON TRANSCRITS BELKHAYATE
Date : [date]
Perimetre : 20 paires selectionnees sur 110 doublons A/B

## 1. QUALITE COMPAREE SOURCE A vs SOURCE B (Agent 1)
[tableau 20 lignes avec verdict par paire]
Conclusion : quelle source est globalement meilleure ?

## 2. REGLES ET TECHNIQUES EXTRAITES (Agent 2)
[liste par categorie avec verbatims]
Total : X regles extraites

## 3. COHERENCE METHODOLOGIQUE (Agent 3)
[verdict par categorie]
[3 regles les plus constantes]
[conclusion stabilite methode]

## 4. CLASSEMENT FIABILITE TOP 10 (Agent 4)
[tableau score /10]
[5 transcrits prioritaires pour la KB]

## 5. RECOMMANDATIONS FINALES
- Quelle source utiliser pour la KB (A ou B) ?
- Quelles categories de regles sont les mieux couvertes ?
- Quelles categories manquent encore dans les transcrits disponibles ?
- Prochains tickets backlog suggeres
```

## CONTRAINTES ABSOLUES

- JAMAIS modifier KNOWLEDGE_BASE_MASTER.json — rapport uniquement
- JAMAIS inventer une regle ou citation
- Maximum 150 lignes lues par fichier transcrit
- Si un fichier est vide ou illisible → noter "ILLISIBLE" et passer au suivant
- Pas d'accents dans les messages git commit
- Commit final : git add . && git commit -m "feat(audit): rapport comparaison 20 paires transcrits Belkhayate A vs B"
- Push : git push origin main

## VERIFICATION FINALE AVANT DE TERMINER

- [ ] RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md existe dans 00-pilotage\
- [ ] Contient les 5 sections
- [ ] Au moins 15 verbatims reels cites entre guillemets avec nom de fichier
- [ ] Tableau Top 10 present avec scores /10
- [ ] 5 recommandations prioritaires KB presentes
- [ ] Commit + push fait

COMMENCE par lire INVENTAIRE_TRANSCRITS_BELKHAYATE.md, selectionne les 20 paires,
puis lance les agents 1 et 2 en PARALLELE via le tool Task.
