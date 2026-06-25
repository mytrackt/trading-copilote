# Extraction StockCharts — Cognitive Biases (psychologie / behavioral finance)

**Source :** `bundles/stockcharts/cognitive_biases.md` (HTTP 200 · ~23 986 car.) + 3 images certifiées
**Méthode images :** double ancrage (accord .md + HTML) · 3/3 certifiées
**Décisions :** D1311 → D1324 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/cognitive-biases
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

> **NATURE DE LA PAGE :** article de fond (Grayson Roze) sur 11 biais cognitifs en behavioral finance. Contenu riche → extraction substantielle (14 décisions). Cercle dominant **C5 (psychologie / sentiment)**. Auteur cité : Grayson Roze (StockCharts).

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Cognitive Biases | Cognitive Biases [SECTION-FALLBACK] | CERTIFIÉ (accord .md + HTML) |
| image_02.png | Illustration of Loss Aversion | Loss Aversion and the Endowment Effect | CERTIFIÉ (accord .md + HTML) |
| image_03.png | Table illustrating Framing Bias | The Framing Effect | CERTIFIÉ (accord .md + HTML) |

## DÉCISIONS

### D1311 — Définition des biais cognitifs (cadre général)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md, image_01) : « cognitive biases describe the innate tendencies of the human mind to think, judge, and behave in irrational ways that often violate sensible logic… The average human – and the average investor – is largely unaware of these inherent psychological inefficiencies. »
**TRADEX-AI C5** : Cadre fondateur du cercle psychologie : le trader (mode Manuel = Abdelkrim décide) est exposé à des biais inconscients. Justifie une couche de garde-fous comportementaux dans l'interface (rappels, journalisation des décisions).
*Catégorie : psychologie*

---

### D1312 — Anchoring (ancrage / focalisme)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « anchoring is the tendency to be over-influenced by the earliest information presented to us… subsequent decisions are made not on their own, but rather by adjusting away from the anchor. » Exemple marché : un price target d'analyste Wall Street à 200 $ biaise tes propres estimations.
**TRADEX-AI C5** : Risque que le prix d'entrée, un objectif annoncé ou un niveau récent ancre le jugement. Garde-fou : le moteur fournit des niveaux dérivés de la méthode (pivots Belkhayate, R/R) et non d'objectifs externes, pour limiter l'ancrage.
*Catégorie : psychologie*

---

### D1313 — Loss Aversion (aversion à la perte) + Prospect Theory
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md, image_02) : « loss aversion refers to the human tendency to strongly prefer decisions that allow us to avoid losses over those that allow us to acquire gains… the human perception of loss is twice as powerful as that of gain » (Tversky & Kahneman, base de la Prospect Theory).
**TRADEX-AI C5** : L'aversion à la perte pousse à couper les gains trop tôt et laisser courir les pertes. Garde-fou direct : R/R minimum 1:2 imposé par la grille de signal et stops obligatoires — contrecarre le biais par une règle déterministe.
*Catégorie : gestion_risque_entree*

---

### D1314 — Endowment Effect (effet de dotation)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « the endowment effect describes the human tendency to place greater value on a good that we own than… an identical good that we do not own. » Études : mug (≈2×), tickets Final Four (≈14× le prix d'achat hypothétique).
**TRADEX-AI C5** : Le simple fait de détenir une position GC·HG·CL·ZW gonfle sa valeur perçue → attachement émotionnel au moment de vendre. Garde-fou : sortie pilotée par règle (stop/target) et non par sentiment de propriété.
*Catégorie : psychologie*

---

### D1315 — Loss aversion + endowment → déni des positions perdantes
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « our tendency to steer away from loss can lead to denial as losses build in a poor position… causing us to ignore weakening positions in an attempt to diminish their emotional impact. »
**TRADEX-AI C5** : Mécanisme du déni des positions faiblissantes. Le Staleness Monitor + stops automatiques et l'affichage neutre du signal (ATTENDRE/sortie) contrent la tendance à ignorer une position qui se dégrade.
*Catégorie : gestion_risque_entree*

---

### D1316 — Framing Effect (effet de cadrage)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md, image_03) : « the framing effect describes our tendency to react to, judge, or interpret the exact same information in distinctly different ways depending on how it is presented… people tend to avoid risk when information is presented in a positive frame but seek risk when… in a negative frame. » Étude Tversky-Kahneman 1981 (traitements A/B, maladie 600 personnes) : 72 % choisissent A en cadrage positif vs 22 % en cadrage négatif.
**TRADEX-AI C5** : Le cadrage d'une news (haussière vs baissière) biaise l'interprétation. Garde-fou : le cercle géopolitique/news (C6) doit présenter l'information de façon neutre et factuelle, sans cadrage directionnel imposé au décideur.
*Catégorie : psychologie*

---

### D1317 — Confirmation Bias (biais de confirmation)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « confirmation bias is the tendency to overweight, favor, seek out… information… that confirms our preconceived beliefs… while… undervaluing, ignoring… information that does not… leading to overconfidence in our opinions and our decisions even in the face of strong contrary evidence. » Effet renforcé sur sujets émotionnels.
**TRADEX-AI C5** : Risque de ne retenir que les signaux confirmant son biais directionnel. Contre-mesure : règle d'alignement multi-cercles (3/4 trading + 2/3 confirmation) et critères éliminatoires — force la prise en compte de signaux contradictoires avant tout signal.
*Catégorie : signal*

---

### D1318 — Hindsight Bias (biais rétrospectif)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « hindsight bias describes our inclination, after an event has occurred, to see the event as having been predictable, even if there had been little to no objective basis for predicting it » (le fameux « I knew it all along »).
**TRADEX-AI C5** : Après coup, on surestime sa capacité de prédiction → surconfiance future. Garde-fou : journaliser le signal et sa confiance AU MOMENT de la décision (horodaté) pour évaluer la performance sans réécriture rétrospective.
*Catégorie : psychologie*

---

### D1319 — Availability Heuristic (heuristique de disponibilité)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « the availability heuristic, a common mental shortcut that causes individuals to rely on immediate information or examples that come to mind first… individuals tend to more heavily weight recent or immediately-recalled information, creating a bias towards the latest news, events, experiences or memories. »
**TRADEX-AI C5** : Surpondération des news/événements récents. Garde-fou : la grille de signal /10 est déterministe et pondère des sources structurées, réduisant le poids émotionnel de la dernière news.
*Catégorie : psychologie*

---

### D1320 — Sunk Cost Fallacy (coûts irrécupérables)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « sunk cost fallacy… our irrational belief that sunk costs should be considered a legitimate factor in our forward decision making. » Exemple marché : « I've already lost $XXX, it's too late to sell now » → escalade de l'engagement à mesure que les pertes grossissent.
**TRADEX-AI C5** : Pousse à conserver une position perdante par refus d'acter la perte déjà subie. Contre-mesure forte : stop automatique non négociable et suspension Auto après perte — la décision de sortie ignore le coût déjà encouru.
*Catégorie : gestion_risque_entree*

---

### D1321 — Gambler's Fallacy (Monte Carlo)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « the mistaken tendency to believe that, if something happens more frequently than “normal”… it must happen less frequently in the future. » Marché : après une série de pertes, croire à tort que la probabilité de gain augmente — « the probability of his or her next trade being profitable is unaffected by previous losses. »
**TRADEX-AI C5** : Chaque trade est indépendant ; une série de pertes n'augmente PAS la probabilité du gain suivant. Garde-fou : pas d'augmentation de taille de position pour « se refaire » ; le risk_manager dimensionne indépendamment de l'historique récent.
*Catégorie : gestion_risque_entree*

---

### D1322 — Hot-Hand Fallacy (main chaude)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « the mistaken belief that an individual who has experienced success with a random event has a greater chance of continuing that success… a series of winning trades can induce risky overconfidence… leading to errors in judgment and poor decision making. »
**TRADEX-AI C5** : Une série de gains induit une surconfiance dangereuse (risque sur-pris). Garde-fou symétrique de D1321 : le dimensionnement et les seuils de signal restent constants après une série gagnante ; la suspension Auto et les limites de risque ne se relâchent jamais sur un « hot streak ».
*Catégorie : gestion_risque_entree*

---

### D1323 — Money Illusion (illusion monétaire)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md) : « the money illusion describes the tendency to think of currency in nominal terms rather than in real terms… many average investors commonly ignore the real value of their currency when valuing their investments… leading to incorrect perceptions of value and past performance. »
**TRADEX-AI C4/C5** : Évaluer P&L en valeur nominale ignore le pouvoir d'achat réel (inflation). Pertinent pour le cercle macro (C4) — lecture du contexte inflation/DX — et l'évaluation honnête de la performance.
*Catégorie : psychologie*

---

### D1324 — Auteur et finalité éducative (provenance)
🟢 **FAIT VÉRIFIÉ** (Source : cognitive_biases.md, section About the Author) : article rédigé par **Grayson Roze** (Business Manager StockCharts.com, auteur « Tensile Trading » et « Trading for Dummies »). But déclaré : « educate you on these psychological predispositions so that you can better recognize and overcome them in your own decision making. »
**TRADEX-AI C5** : Provenance et finalité = éducation comportementale du décideur, alignée sur le mode Manuel du projet. Source secondaire (vulgarisation), pas une étude primaire — fiabilité conceptuelle bonne, pas de calibration chiffrée pour le moteur.
*Catégorie : psychologie*

---

## SYNTHÈSE

| D### | Biais | Cercle | Catégorie | Tag | Garde-fou TRADEX |
|------|-------|--------|-----------|-----|------------------|
| D1311 | Cadre général biais | C5 | psychologie | 🟢 | journalisation décisions |
| D1312 | Anchoring | C5 | psychologie | 🟢 | niveaux méthode, pas externes |
| D1313 | Loss Aversion / Prospect Th. | C5 | gestion_risque_entree | 🟢 | R/R ≥ 1:2 + stops |
| D1314 | Endowment Effect | C5 | psychologie | 🟢 | sortie par règle |
| D1315 | Déni positions perdantes | C5 | gestion_risque_entree | 🟢 | stops auto + staleness |
| D1316 | Framing Effect | C5 | psychologie | 🟢 | news neutres (C6) |
| D1317 | Confirmation Bias | C5 | signal | 🟢 | alignement 3/4+2/3 |
| D1318 | Hindsight Bias | C5 | psychologie | 🟢 | log horodaté du signal |
| D1319 | Availability Heuristic | C5 | psychologie | 🟢 | grille déterministe /10 |
| D1320 | Sunk Cost Fallacy | C5 | gestion_risque_entree | 🟢 | stop non négociable |
| D1321 | Gambler's Fallacy | C5 | gestion_risque_entree | 🟢 | taille indépendante histo |
| D1322 | Hot-Hand Fallacy | C5 | gestion_risque_entree | 🟢 | seuils constants post-gains |
| D1323 | Money Illusion | C4/C5 | psychologie | 🟢 | lecture réelle vs nominale |
| D1324 | Auteur / finalité | C5 | psychologie | 🟢 | provenance vulgarisation |

**Lien Belkhayate :** NON CONCERNÉ (psychologie générique behavioral finance ; aucun lien Belkhayate dans la source — ne rien inventer). Apport pour le cercle C5 du projet, transversal à tous les actifs GC·HG·CL·ZW.
**Images :** 3/3 certifiées (image_01 illustration générale, image_02 courbe Prospect Theory/loss aversion, image_03 table cadrage). **Cas à vérifier :** aucun (les 3 images sont CERTIFIÉES par accord .md+HTML ; image_01 via SECTION-FALLBACK, figcaption vide mais alignée — fiabilité OK).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
