# PROMPT CLAUDE CODE — AUDIT COMPARAISON TRANSCRITS BELKHAYATE
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code

---

Tu es l'orchestrateur d'une equipe de 4 agents specialises. Ta mission est d'auditer et comparer les transcriptions Belkhayate presentes dans le projet TRADEX-AI, d'evaluer leur coherence methodologique et de produire un rapport de fiabilite.

## CONTEXTE

Il existe 2 sources de transcrits dans le projet :

SOURCE A — Anciens transcrits (whisper_*.txt) :
- Dossier : C:\trading-copilote\03-transcriptions\transcripts-bruts\
- 142 fichiers .txt nommes whisper_[videoID].txt
- Generes par Whisper depuis les MP3 YouTube telecharges via yt-dlp

SOURCE B — Nouveaux transcrits (fichiers nommes lisiblement) :
- Dossier : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\
- 164 fichiers .txt generes par Whisper depuis les MP4 locaux (D:\Belkhayate-Videos)
- Manifeste qualite disponible : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv

OBJECTIF : Comparer les deux sources, verifier la coherence des methodes et techniques enseignees par Belkhayate entre ses anciennes et nouvelles videos, et identifier les transcrits les plus fiables et logiques pour alimenter la KB.

## EQUIPE D'AGENTS

Lance les 4 agents via le tool Task en parallele (agents 1+2 simultanement, puis 3+4 apres).

---

### AGENT 1 — INVENTAIRE ET CLASSIFICATION

Role : Cataloguer les deux sources et identifier les correspondances.

Instructions :
1. Lire le fichier MANIFESTE_TRANSCRITS.csv complet
2. Lister les 15 fichiers de SOURCE A avec le score MANIFESTE le plus eleve (colonne score)
3. Lister les 15 fichiers de SOURCE B avec le score MANIFESTE le plus eleve
4. Pour chaque fichier selectionne, noter : nom / nb_mots / score / statut VALIDE ou non
5. Identifier les doublons evidents (meme video presente dans les 2 sources)
6. Produire un tableau Markdown clair

Livrable : section "INVENTAIRE" du rapport final

---

### AGENT 2 — EXTRACTION DES REGLES ET TECHNIQUES

Role : Extraire les regles et techniques de trading mentionnees dans un echantillon representatif.

Instructions :
1. Lire les 10 meilleurs fichiers de SOURCE A (score le plus eleve dans le MANIFESTE)
2. Lire les 10 meilleurs fichiers de SOURCE B (score le plus eleve)
3. Pour chaque fichier, extraire les mentions explicites de :
   - Centre de Gravite (COG / Gravity Center / BGC)
   - Timing Belkhayate
   - Pivots
   - Energie
   - Direction
   - Regles d'entree / sortie
   - Gestion du risque (stop loss, take profit)
   - Inter-marches (or, petrole, indices)
   - Psychologie du trader
   - Couloir horaire
4. Pour chaque technique trouvee, noter : technique / description / fichier source / citation courte (verbatim)
5. Ne jamais inventer une regle non presente dans le texte

Livrable : section "REGLES EXTRAITES" du rapport final

---

### AGENT 3 — ANALYSE DE COHERENCE

Role : Comparer les regles extraites par l'Agent 2 entre les deux sources.

Instructions (a executer APRES reception des resultats Agent 2) :
1. Pour chaque technique identifiee, verifier si elle est :
   - Presente dans les 2 sources avec la meme definition → COHERENT
   - Presente dans les 2 sources avec une definition differente → EVOLUTION ou CONTRADICTION
   - Presente uniquement dans SOURCE A → ANCIEN UNIQUEMENT
   - Presente uniquement dans SOURCE B → NOUVEAU UNIQUEMENT
2. Identifier les 3 principales coherences (elements stables dans la methode)
3. Identifier les 3 principales evolutions ou contradictions entre ancien et nouveau
4. Conclure : la methode Belkhayate est-elle stable ou a-t-elle evolue ?

Livrable : section "COHERENCE METHODOLOGIQUE" du rapport final

---

### AGENT 4 — SCORING DE FIABILITE

Role : Evaluer et classer les transcrits selon leur fiabilite pour la KB.

Instructions (a executer APRES reception des resultats Agent 2) :
1. Pour chaque transcrit analyse par l'Agent 2, attribuer un score de fiabilite /10 selon ces criteres :
   - Presence de verbatims Belkhayate clairs et identificables (0-3 pts)
   - Coherence interne des regles enoncees (0-2 pts)
   - Clarte et precision des techniques decrites (0-2 pts)
   - Score MANIFESTE_TRANSCRITS.csv (0-2 pts, normalise /100 → /2)
   - Absence d'hallucinations ou contradictions internes (0-1 pt)
2. Produire un classement Top 10 des transcrits les plus fiables toutes sources confondues
3. Pour chaque transcrit du Top 10 : indiquer si les regles qu'il contient sont deja dans la KB ou sont nouvelles
4. Recommander les 5 transcrits prioritaires a integrer dans la prochaine session d'enrichissement KB

Livrable : section "CLASSEMENT FIABILITE" du rapport final

---

## SYNTHESE FINALE (toi, l'orchestrateur)

Apres reception des 4 livrables, produire le rapport final :

Fichier de sortie : C:\trading-copilote\00-pilotage\RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md

Structure obligatoire du rapport :
```
# RAPPORT AUDIT COMPARAISON TRANSCRITS BELKHAYATE
Date : [date du jour]
Sources : 142 anciens (transcripts-bruts) + 164 nouveaux (belkhayate-youtube/transcripts)

## 1. INVENTAIRE (Agent 1)
[tableau anciens vs nouveaux, top 15 chaque source]

## 2. REGLES ET TECHNIQUES EXTRAITES (Agent 2)
[liste structuree par technique, avec verbatims]

## 3. COHERENCE METHODOLOGIQUE (Agent 3)
[coherences, evolutions, contradictions, conclusion stabilite methode]

## 4. CLASSEMENT FIABILITE TOP 10 (Agent 4)
[tableau score /10, deja en KB ou nouveau, priorite integration]

## 5. RECOMMANDATIONS
[5 transcrits prioritaires a integrer + 3 regles nouvelles candidates KB]
```

## CONTRAINTES ABSOLUES

- JAMAIS ecrire dans KNOWLEDGE_BASE_MASTER.json — ce rapport est une analyse, pas une integration
- JAMAIS inventer une regle non presente dans les fichiers lus
- Si un fichier depasse 3000 mots, lire les 100 premieres lignes + 100 dernieres lignes
- Rapport = observations factuelles uniquement
- Pas d'accents dans les messages git commit
- Apres creation du rapport : git add . && git commit -m "feat(audit): rapport comparaison transcrits Belkhayate anciens vs nouveaux"

## VERIFICATION FINALE

Avant de terminer, verifier :
- [ ] Le fichier RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md existe dans 00-pilotage\
- [ ] Il contient les 5 sections
- [ ] Au moins 10 verbatims reels cites (entre guillemets, avec nom du fichier source)
- [ ] Le classement Top 10 est present avec scores /10
- [ ] Git commit fait

COMMENCE MAINTENANT par lancer les agents 1 et 2 en parallele.
