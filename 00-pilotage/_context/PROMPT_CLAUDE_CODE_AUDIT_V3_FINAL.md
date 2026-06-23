# PROMPT CLAUDE CODE — AUDIT TRANSCRITS BELKHAYATE V3 FINAL
# Session S20 — 23/06/2026
# Coller EN ENTIER dans Claude Code

---

Tu es l'orchestrateur d'une equipe de 4 agents specialises.
Mission : extraire les regles de trading Belkhayate les plus fiables depuis
110 transcriptions audio, en eliminant systematiquement les hallucinations
et les references visuelles non exploitables.

---

## CONTEXTE FONDAMENTAL — CONTRAINTE AUDIO-VIDEO

ATTENTION CRITIQUE : ces transcrits sont des transcriptions d'AUDIO uniquement.
Belkhayate fait ses cours en partageant son ecran (TradingView, NinjaTrader).
Il dit constamment : "vous voyez ici", "regardez la", "ici voila", "vous voyez ca",
"cette bougie la", "ce niveau la", "ici on a..."

Ces phrases font reference a des elements VISIBLES A L'ECRAN mais non
decrits verbalement. Elles sont INUTILISABLES sans la video.

REGLE D'OR ABSOLUE :
Une regle n'est valide que si elle peut etre comprise et appliquee
sans voir l'ecran. Exemples :
  VALIDE   : "le meilleur mois pour acheter de l'or c'est septembre"
  VALIDE   : "16h30 heure France c'est le couloir d'entree sur le ble"
  VALIDE   : "lorsque Belkhayate Trend devient vert vous achetez"
  INVALIDE : "vous voyez ici on a un signal" (que voit-on ? impossible a savoir)
  INVALIDE : "regardez ce niveau la c'est important" (quel niveau ?)
  INVALIDE : "ici le volume explose" (quand ? quel actif ?)

---

## HALLUCINATIONS WHISPER CONNUES

Whisper deforme systematiquement ces termes — les reconnaitre et corriger :

| Terme reel       | Variantes hallucinées Whisper        |
|------------------|--------------------------------------|
| Belkhayate       | belgrède, belgeat, bachiat, belgrat  |
| VWAP             | vivoirs, vivos, viwa, viva           |
| Squeeze          | sprint box, springboks, springbox    |
| NinjaTrader      | ninjatraiter, ninja trader           |
| COG / Gravity    | coge, cogé, graviti                  |
| Pitchfork        | pitchfork (souvent OK), pitch fork   |
| ZN (bond)        | zl, ze, zé                           |

Si Whisper a transcrit un terme halluciné -> le corriger PUIS garder la regle.
Si le terme halluciné rend la regle incomprehensible -> marquer HALLUCINATION.

---

## SOURCES DE DONNEES

SOURCE A — bruts YouTube (MP3 via yt-dlp → Whisper) :
  C:\trading-copilote\03-transcriptions\transcripts-bruts\
  142 fichiers nommes whisper_[videoID].txt
  Format : texte brut sans ponctuation, tout en minuscules

SOURCE B — local MP4 (D:\Belkhayate-Videos → Whisper medium) :
  C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\
  164 fichiers (110 en commun avec A, 54 uniques B)
  Format : texte avec ponctuation et majuscules — plus lisible

INVENTAIRE (110 paires identifiees) :
  C:\trading-copilote\00-pilotage\INVENTAIRE_TRANSCRITS_BELKHAYATE.md

MANIFESTE QUALITE :
  C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv
  Colonnes : fichier, nb_mots, score, statut

KB ACTUELLE (NE PAS MODIFIER) :
  C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
  1313 regles existantes

---

## ETAPE 0 — SELECTION DES 20 PAIRES (orchestrateur)

1. Lire INVENTAIRE_TRANSCRITS_BELKHAYATE.md
2. Extraire les 110 paires (video presente dans A et B)
3. Selectionner 20 paires selon cette strategie :
   a. 5 paires : videos de presentation ou lecon numerotee (contenu pedagogique pur,
      peu de live screen — ces videos ont tendance a avoir MOINS de references visuelles)
      Exemples de titres : "Lecon", "Lesson", "Formation", "Parcours", "Pourquoi l'or"
   b. 5 paires : videos thematiques sur les actifs TRADEX-AI
      Cibles : or (GC), ble (ZW), petrole (CL)
      Exemples : "Trading de l'Or", "Trading Gagnant sur le Ble", "Petrole"
   c. 5 paires : videos sur les indicateurs Belkhayate
      Exemples : "Gravity Center", "Belkhayate Trend", "Pivots", "Timing"
   d. 5 paires : videos inter-marche et macro
      Exemples : "Dollar", "Intermarche", "Relations", "COT", "Saisonnalite"
4. Pour chaque paire : noter videoID + titre Source B + taille Source A + taille Source B
5. Preferer les fichiers les plus grands (plus de contenu potentiellement exploitable)

Lancer les agents 1 et 2 EN PARALLELE via Task tool.

---

## AGENT 1 — TRIAGE SOURCE A vs SOURCE B

Role : Determiner quelle version utiliser pour chaque paire.

Pour chacune des 20 paires :

PHASE 1 — Test de lisibilite (10 lignes suffisent)
  Lire les 10 premieres lignes de la version A et B.
  Verifier : Source B a-t-elle une ponctuation et des majuscules ?
  → Si OUI : Source B preferee (transcription MP4, meilleure qualite audio)
  → Si NON ou equivalent : comparer les 30 premieres lignes

PHASE 2 — Comptage marqueurs visuels (sur 50 lignes)
  Compter les occurrences de : voyez, regardez, ici, la, voila
  Ces mots dans la phrase = signal visuel potentiellement inutilisable.
  Calculer : taux_visuel = nb_marqueurs / nb_mots_total * 100
  → taux > 15% : video fortement dependante du visuel (live trading)
  → taux < 8%  : video majoritairement audio (cours, presentation)

PHASE 3 — Detection type de video
  Classer chaque video en :
  TYPE_A : Cours/Presentation (peu de visuel, riches en regles verbales)
  TYPE_B : Live trading (fort visuel, regles partielles mais en contexte reel)
  TYPE_C : Analyse de marche (visuel moyen, regles conditionnelles)

Livrable pour chaque paire :
  [videoID] | [titre] | version_choisie (A/B) | type_video (A/B/C) | taux_visuel% | raison

---

## AGENT 2 — EXTRACTEUR DE REGLES AUDIO-PURES

Role : Extraire UNIQUEMENT les regles formulees sans dependance visuelle.

METHODE D'EXTRACTION EN 3 PASSES :

PASSE 1 — Identification des phrases candidates (sur 120 lignes)
  Pour chaque phrase, appliquer ce filtre :
  → REJETER si contient : "vous voyez", "regardez", "ici on a", "la vous avez",
    "ce niveau", "cette bougie", "ce que je vois", "vous voyez bien que"
    SAUF si la phrase continue avec une regle complete apres le marqueur visuel
    Exemple acceptable : "vous voyez ici on a un signal vert sur le Belkhayate Trend
    ce qui signifie qu'on doit acheter" → garder uniquement "signal vert sur le
    Belkhayate Trend = signal d'achat"
  → GARDER si : phrase complete, comprehensible sans image, regle explicite

PASSE 2 — Correction des hallucinations Whisper
  Appliquer le dictionnaire de correction ci-dessus.
  Marquer [CORRIGE: terme_original → terme_corrige] dans le verbatim.

PASSE 3 — Classification par categorie Belkhayate
  Pour chaque regle valide extraire :

  FORMAT OBLIGATOIRE :
  ---
  REGLE_ID : R[numero]
  CATEGORIE : [voir liste ci-dessous]
  REGLE : [formulation claire de la regle]
  VERBATIM : "[citation exacte du transcript, corrigee si hallucination]"
  SOURCE_FICHIER : [nom exact du fichier]
  CONFIANCE : [HAUTE / MOYENNE / FAIBLE]
  DEPENDANCE_VISUELLE : [NULLE / FAIBLE / FORTE]
  ---

  CATEGORIES AUTORISEES :
  - COG_GRAVITY     : Centre de gravite, position prix / COG
  - TIMING          : Couloir horaire, heures d'entree/sortie
  - PIVOTS          : Niveaux pivot, supports, resistances
  - TREND_INDICATOR : Belkhayate Trend (vert/rouge/bleu/blanc)
  - SIGNAL_ENTREE   : Conditions explicites d'entree en position
  - SIGNAL_SORTIE   : Conditions explicites de sortie
  - SQUEEZE         : Pattern squeeze / impulsion
  - GESTION_RISQUE  : Stop loss, take profit, money management
  - INTERMARCHE     : Correlations entre actifs (or/dollar, etc.)
  - SAISONNALITE    : Comportement saisonnier par mois
  - PSYCHOLOGIE     : Discipline, patience, mental

  REGLES DE CONFIANCE :
  HAUTE   = regle explicite, sans visual dependency, termes clairs
  MOYENNE = regle partiellement visuelle mais principe lisible
  FAIBLE  = beaucoup d'hypotheses pour reconstituer la regle

Contrainte absolue : si une regle necessite de voir l'ecran pour etre
appliquee → noter DEPENDANCE_VISUELLE: FORTE et ne pas inclure dans Top.
Si aucune regle HAUTE ou MOYENNE dans un fichier → ecrire "PEU_EXTRACTIBLE".

---

## AGENT 3 — COHERENCE ET EVOLUTION DE LA METHODE

Role : Verifier si la methode est stable entre les vieilles et nouvelles videos.

Utiliser les resultats de l'Agent 2.

ANALYSE EN 4 POINTS :

1. CONSISTANCE DES REGLES
   Pour chaque CATEGORIE, regrouper toutes les regles extraites.
   Verifier :
   - La regle est formulee de la meme facon dans plusieurs videos ?
   - Une regle ancienne contredit-elle une regle recente ?
   Verdict par categorie : STABLE / EVOLUE / CONTRADICTION / INSUFFISANT

2. REGLES LES PLUS ROBUSTES (au moins 3 videos independantes)
   Lister les regles qui apparaissent dans 3 videos ou plus.
   Ce sont les regles les plus fiables pour la KB.
   Format : REGLE | nb_occurrences | videos_sources

3. EVOLUTION DE LA METHODE
   Comparer les videos dont le titre contient "Lecon 1-20" vs "Lesson 38-50"
   Y a-t-il des ajouts (nouvelles techniques) ou des corrections ?
   Une technique ancienne a-t-elle ete abandonnee ?

4. SCORE DE COHERENCE METHODOLOGIQUE
   Sur 10 categories analysees, combien sont STABLE ?
   Score coherence = (nb_STABLE / nb_total_categories) * 10

---

## AGENT 4 — SCORING ET RECOMMANDATIONS KB

Role : Produire le classement final et les priorites d'integration.

Pour chacune des 20 paires, calculer le SCORE FIABILITE /10 :

  Critere 1 — Densite de regles extractibles (0-3 pts)
    3 pts : >= 5 regles HAUTE confiance extraites
    2 pts : 3-4 regles HAUTE confiance
    1 pt  : 1-2 regles HAUTE confiance
    0 pt  : aucune regle HAUTE (ou PEU_EXTRACTIBLE)

  Critere 2 — Qualite audio / format Source B (0-2 pts)
    2 pts : Source B avec ponctuation, majuscules, taux_visuel < 10%
    1 pt  : Source B correcte mais taux_visuel 10-20%
    0 pt  : les deux sources equivalentes ou mediocres

  Critere 3 — Score MANIFESTE_TRANSCRITS.csv (0-2 pts)
    Lire la colonne score pour ce fichier dans le CSV.
    Normaliser : score_manifeste / (score_max * 0.5) = pts /2
    Plafonner a 2.

  Critere 4 — Coherence interne (0-2 pts)
    2 pts : aucune contradiction interne detectee dans la video
    1 pt  : 1 contradiction ou ambiguite
    0 pt  : contradictions ou contenu incoherent

  Critere 5 — Unicite par rapport a la KB (0-1 pt)
    Lire les 20 premieres regles de KNOWLEDGE_BASE_MASTER.json pour reference.
    1 pt  : au moins 2 regles genuinement nouvelles (pas encore en KB)
    0 pt  : tout deja couvert dans la KB

VERIFICATION DANS LA KB :
  Pour chaque regle extraite par Agent 2, comparer avec les regles KB.
  Marquer : DEJA_EN_KB / NOUVELLE / PARTIELLE (meme concept, formulation differente)

LIVRABLE :
  Top 10 tableau : rang | videoID | titre | score/10 | nb_regles_HAUTE | unicite_KB
  5 videos prioritaires a traiter dans la prochaine session KB (avec justification)
  Liste des 10 regles les plus fiables toutes videos confondues

---

## RAPPORT FINAL (orchestrateur)

Creer apres reception des 4 livrables :
C:\trading-copilote\00-pilotage\RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md

Structure :
```
# RAPPORT AUDIT COMPARAISON TRANSCRITS BELKHAYATE
Date : [date]
Perimetre : 20 paires selectionnees sur 110 doublons A/B
Strategie : extraction audio-pure avec filtre dependance visuelle

## 0. CONCLUSIONS CLES (lire en premier)
[3-5 phrases max sur ce qu'on apprend de cet audit]
Source A ou B globalement meilleure ? Pourquoi ?
Quel type de video est le plus utile pour la KB ?

## 1. TRIAGE SOURCE A vs SOURCE B (Agent 1)
[tableau 20 lignes : version_choisie | type_video | taux_visuel%]
[Repartition : X videos TYPE_A / Y TYPE_B / Z TYPE_C]

## 2. REGLES AUDIO-PURES EXTRAITES (Agent 2)
[regles HAUTE confiance par categorie, avec verbatims]
[Statistiques : X regles HAUTE / Y MOYENNE / Z FAIBLE / W PEU_EXTRACTIBLE]
[Hallucinations Whisper corrigees : liste]

## 3. COHERENCE METHODOLOGIQUE (Agent 3)
[verdicts par categorie]
[Top 3 regles les plus robustes (3+ videos)]
[Evolution methode : quoi a change entre vieilles et nouvelles videos ?]
[Score coherence global : X/10]

## 4. CLASSEMENT FIABILITE TOP 10 (Agent 4)
[tableau Top 10 avec score /10]
[5 videos prioritaires pour prochain enrichissement KB]
[10 regles les plus fiables toutes videos confondues]

## 5. PLAN D'ACTION
[Recommandation : utiliser Source A ou B par defaut ?]
[Quelles categories KB manquent encore ? Quelles videos les couvrent ?]
[Prochains tickets backlog proposes]
```

---

## CONTRAINTES ABSOLUES

- JAMAIS modifier KNOWLEDGE_BASE_MASTER.json dans cette mission
- JAMAIS inventer une regle non presente dans l'audio
- Maximum 120 lignes lues par fichier transcrit
- Si un fichier est vide → noter VIDE et passer
- Pas d'accents dans les messages git commit
- Commit : git add . && git commit -m "feat(audit): rapport audit transcrits Belkhayate V3 audio-pur"
- Push : git push origin main

## CHECKLIST AVANT DE TERMINER

- [ ] RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md cree dans 00-pilotage\
- [ ] Section 0 (conclusions cles) presente
- [ ] Au moins 20 regles HAUTE confiance avec verbatims reels
- [ ] Hallucinations Whisper detectees et listees
- [ ] Top 10 avec scores /10
- [ ] 5 videos prioritaires KB avec justification
- [ ] Commit + push confirme

---

COMMENCE maintenant :
Etape 0 → selectionne les 20 paires depuis l'inventaire
Puis lance Agent 1 et Agent 2 en PARALLELE via Task tool.
