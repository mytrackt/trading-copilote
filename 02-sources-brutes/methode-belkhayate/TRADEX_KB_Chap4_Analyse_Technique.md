# TRADEX-AI · BASE DE CONNAISSANCES

# Chapitre 4 — Lire le prix : analyse technique (version technique enrichie)

**Statut du document :** ressource de connaissance interne pour le cerveau IA de TRADEX. **Règle anti-hallucination :** ce document ne contient aucun taux de réussite inventé, aucune promesse de gain, aucune statistique non vérifiable. Chaque affirmation est taguée par son **niveau de fiabilité** (voir légende). Tout ce qui dépend du contexte est explicitement signalé. **Avertissement :** contenu éducatif. Ce n'est ni un conseil financier, ni un signal d'achat/vente. La majorité des débutants perdent de l'argent en trading.

---

## 🏷️ LÉGENDE DES NIVEAUX DE FIABILITÉ

| Tag | Signification | Exemple |
| :---- | :---- | :---- |
| 🟢 **FAIT** | Définition ou formule mathématique stable et vérifiable. Vrai par construction. | La formule du RSI. |
| 🟡 **CONVENTION** | Réglage ou usage standard par défaut, mais modifiable. Largement adopté, pas obligatoire. | RSI période 14\. |
| 🔵 **ÉCOLE** | Interprétation propre à un courant d'analyse (price action, SMC, Wyckoff…). Opinion, pas vérité. | « Prix au-dessus du VWAP \= biais acheteur. » |

**Pour l'IA TRADEX :** ne jamais présenter un 🔵 ÉCOLE comme un 🟢 FAIT. Toujours dire « selon telle approche » pour un 🔵.

---

## 4.0 — Cadre épistémique de l'analyse technique

🟢 **FAIT.** L'analyse technique (AT) étudie l'historique du **prix** et du **volume** pour estimer les scénarios futurs les plus *probables*. Elle ne traite ni des fondamentaux économiques, ni des bilans d'entreprise.

🔵 **ÉCOLE.** Le postulat « le prix intègre déjà toute l'information disponible » vient de la tradition technique (proche de l'hypothèse d'efficience faible). C'est une hypothèse de travail, pas une loi prouvée.

🟢 **FAIT.** L'AT est **probabiliste**, jamais déterministe. Aucun outil ne « prédit » le prix. Un outil ne fait que déplacer une probabilité.

**Analogie pédagogique :** lire les traces de pas dans la neige. On ne voit pas l'animal, mais les traces indiquent une direction probable.

---

## 4.1 — Structure de marché et tendances

### Définitions de base (🟢 FAIT)

- **Swing high (sommet pivot)** : une bougie dont le *plus haut* est supérieur à celui des bougies immédiatement à sa gauche et à sa droite (souvent N bougies de chaque côté ; N=2 ou 3 est un réglage 🟡).  
- **Swing low (creux pivot)** : symétrique — un *plus bas* inférieur aux bougies voisines.

Ces points pivots sont les briques qui définissent une tendance. On ne lit pas une tendance « à l'œil » : on lit la **séquence des pivots**.

### Les 4 codes de structure (🟢 FAIT, vocabulaire issu de la théorie de Dow)

- **HH** \= *Higher High* \= sommet plus haut que le précédent.  
- **HL** \= *Higher Low* \= creux plus haut que le précédent.  
- **LH** \= *Lower High* \= sommet plus bas que le précédent.  
- **LL** \= *Lower Low* \= creux plus bas que le précédent.

### Les 3 régimes de marché (🟢 FAIT)

1. **Tendance haussière** : séquence de **HH \+ HL**. Le prix monte en escalier.  
2. **Tendance baissière** : séquence de **LH \+ LL**. Le prix descend en escalier.  
3. **Range (latéral)** : pivots qui oscillent entre une borne haute et une borne basse, sans nouvelle direction nette.

HAUSSIÈRE                BAISSIÈRE               RANGE

        HH                 LH                  ┌──plafond──┐

      /                      \\                 │  /\\  /\\   │

   HL                          LH              │ /  \\/  \\  │

   /                             \\             └──plancher─┘

 (HL \> creux précédent)        (LL \< ...)

### Changement de structure (🔵 ÉCOLE — price action / Smart Money Concepts)

- **BOS** (*Break of Structure*) : cassure d'un pivot dans le **sens** de la tendance → continuation probable.  
- **CHoCH** (*Change of Character*) : cassure d'un pivot **contre** la tendance → premier signal d'un possible retournement.

Ces deux notions sont des grilles de lecture d'école. Utiles, mais à présenter comme telles, pas comme des certitudes.

**Adage 🔵 :** « la tendance est ton amie » — convention culturelle des traders, pas une garantie. Toute tendance finit par s'inverser.

---

## 4.2 — Supports et résistances (S/R)

### Définition (🟢 FAIT)

- **Support** : zone de prix où la **demande** (acheteurs) a historiquement dépassé l'offre → le prix peine à descendre plus bas. Un plancher.  
- **Résistance** : zone où l'**offre** (vendeurs) a dépassé la demande → le prix peine à monter plus haut. Un plafond.

### Règles techniques

1. 🟢 **Ce sont des zones, pas des lignes.** Un niveau se définit par une fourchette de prix (ex. 5 798–5 802), pas par un tick exact.  
2. 🟡 **Validation par le nombre de touches** : un niveau touché et respecté plusieurs fois est considéré comme « plus fort » par convention. Aucun seuil officiel n'existe.  
3. 🟢 **Polarité (inversion des rôles, *role reversal*)** : une résistance franchie devient fréquemment un support, et inversement. C'est une observation structurelle robuste, mais pas systématique.  
4. 🟡 **Niveaux psychologiques** : les chiffres ronds (ex. 6 000 sur l'ES, 20 000 sur le NQ) attirent souvent les ordres. Convention de marché observée, pas une loi.

### Types de S/R (🟢 FAIT)

- **Horizontaux** : niveau de prix fixe (ancien sommet/creux, plus haut/bas de séance, clôture précédente).  
- **Dynamiques** : niveau qui se déplace dans le temps (moyenne mobile, VWAP — voir 4.5 et 4.6).  
- **Obliques** : lignes de tendance reliant plusieurs pivots.

---

## 4.3 — Chandeliers japonais (candlesticks)

🟢 **FAIT (origine).** Technique de représentation née au Japon (négoce du riz, XVIIIᵉ s., attribuée à Munehisa Homma), popularisée en Occident par Steve Nison (1991).

### Anatomie (🟢 FAIT)

Une bougie résume **une** unité de temps avec 4 valeurs : **OHLC** \= Open (ouverture), High (plus haut), Low (plus bas), Close (clôture).

   │        ← mèche haute  \= High

 ┌─┴─┐

 │   │      ← CORPS \= |Open − Close|

 └─┬─┘

   │        ← mèche basse  \= Low

Amplitude totale (range) \= High − Low

- **Corps** \= distance ouverture↔clôture. Mesure le **résultat net** de la période.  
- **Mèches (ombres)** \= zones testées puis rejetées. Mesurent l'**indécision / le rejet**.  
- Bougie **haussière** : Close \> Open. Bougie **baissière** : Close \< Open.

### Classification fonctionnelle (🟢 FAIT)

| Type | Forme | Lecture brute |
| :---- | :---- | :---- |
| **Momentum** | grand corps, petites mèches | un camp domine nettement |
| **Indécision** | petit corps, mèches longues | équilibre / hésitation |
| **Rejet** | longue mèche d'un seul côté | un niveau a été défendu |

### Figures à 1 bougie (🟡 CONVENTION — seuils indicatifs)

- **Doji** : Open ≈ Close (corps quasi nul) → indécision.  
- **Marteau (*hammer*)** : petit corps en haut, mèche basse ≥ \~2× le corps → rejet du bas.  
- **Étoile filante (*shooting star*)** : petit corps en bas, longue mèche haute → rejet du haut.  
- **Marubozu** : corps plein, mèches quasi absentes → momentum fort.  
- **Dragonfly / Gravestone doji** : doji avec une seule longue mèche (basse / haute respectivement).

### Figures à 2 bougies (🟡 CONVENTION)

- **Englobante (*engulfing*)** : la 2ᵉ bougie a un corps qui recouvre entièrement celui de la 1ʳᵉ → bascule du rapport de force.  
- **Harami** : petite 2ᵉ bougie contenue dans le corps de la 1ʳᵉ → essoufflement.  
- **Piercing / Dark cloud cover** : pénétration de la clôture dans le corps opposé précédent.

### Figures à 3 bougies (🟡 CONVENTION)

- **Étoile du matin (*morning star*)** : baissière → doji/indécision → haussière. Signal de retournement haussier potentiel.  
- **Étoile du soir (*evening star*)** : symétrique baissier.

### Règles d'usage critiques (🟢 FAIT / 🔵 ÉCOLE)

1. 🔵 **Le contexte prime sur le motif.** Un marteau sur un support majeur \> un marteau au milieu de nulle part.  
2. 🟢 **Attendre la clôture.** Une bougie change de forme tant qu'elle n'est pas clôturée (*repainting* visuel intra-bougie). Une figure n'est confirmée qu'à la clôture de l'unité de temps.  
3. 🔵 **Une bougie seule ne décide de rien** — c'est sa position et sa confluence qui font sens (voir 4.8 et Chapitre 7).

---

## 4.4 — Volume

🟢 **FAIT.** Le volume \= nombre de contrats échangés sur une période.

### Spécificité futures (🟢 FAIT — important)

Les futures CME (ES, NQ, CL, GC…) se négocient sur un **marché centralisé** : le volume affiché est le **volume réel** consolidé par la bourse. C'est une différence majeure avec le Forex au comptant (décentralisé), où les plateformes n'affichent qu'un **tick volume** (nombre de changements de prix), un simple substitut. Sur futures, le volume est donc une donnée de qualité.

### Lecture (🔵 ÉCOLE — analyse classique du volume / VSA)

- Mouvement **avec volume élevé** \= participation large → mouvement plus crédible.  
- Mouvement **avec volume faible** \= peu de participants → mouvement plus fragile.  
- **Climax de volume** : pic de volume anormal, souvent près d'un extrême → possible épuisement.  
- **Divergence prix/volume** : prix fait un nouveau sommet mais volume décroît → essoufflement possible.

Ces lectures sont des grilles d'école, pas des certitudes. Le volume confirme ou questionne ; il ne tranche pas seul.

---

## 4.5 — VWAP (Volume Weighted Average Price)

🟢 **FAIT (définition).** Le VWAP est le **prix moyen pondéré par le volume**, cumulé depuis le début de la séance.

### Formule exacte (🟢 FAIT)

Prix typique(i) \= ( High(i) \+ Low(i) \+ Close(i) ) / 3        \[🟡 variante la plus courante\]

VWAP(t) \= Σ \[ Prix typique(i) × Volume(i) \]  /  Σ \[ Volume(i) \]

          (somme cumulée de i \= début de séance jusqu'à t)

- 🟡 Le « prix typique » `(H+L+C)/3` est la convention la plus répandue ; certaines plateformes utilisent la clôture seule ou `(H+L)/2`.  
- 🟢 Le VWAP est **cumulatif intra-séance** et se **réinitialise** à chaque nouvelle séance.

### Bandes de VWAP (🟢 FAIT / 🟡 CONVENTION)

Bande sup \= VWAP \+ k × σ      (σ \= écart-type pondéré par le volume)

Bande inf \= VWAP − k × σ      (k \= 1, 2, 3 selon réglage 🟡)

### Usages (🔵 ÉCOLE — day trading / exécution institutionnelle)

- Prix **\> VWAP** → biais acheteur de séance ; **\< VWAP** → biais vendeur.  
- Le VWAP agit souvent comme **support/résistance dynamique** (aimant à prix).  
- 🟢 **Fait sous-jacent réel :** de nombreux desks institutionnels utilisent le VWAP comme **référence d'exécution** (benchmark pour acheter/vendre « au prix moyen »). C'est ce qui rend le niveau auto-réalisateur : beaucoup d'acteurs y réagissent.  
- **Anchored VWAP** : VWAP démarré à une date/événement précis (ex. depuis un plus bas majeur) plutôt qu'au début de séance — variante utile en day trading.

---

## 4.6 — Moyennes mobiles (MM / MA)

🟢 **FAIT.** Une moyenne mobile lisse le prix en calculant sa moyenne sur N périodes glissantes. C'est un indicateur **retardé (*lagging*)** : il réagit après le prix, par construction.

### Moyenne mobile simple — SMA (🟢 FAIT)

SMA(t) \= \[ P(t) \+ P(t−1) \+ … \+ P(t−N+1) \] / N

Toutes les bougies ont le même poids.

### Moyenne mobile exponentielle — EMA (🟢 FAIT)

k \= 2 / (N \+ 1\)                              ← facteur de lissage

EMA(t) \= P(t) × k \+ EMA(t−1) × (1 − k)

Initialisation : EMA de départ ≈ SMA des N premières valeurs

L'EMA donne **plus de poids aux bougies récentes** → réagit plus vite que la SMA (mais génère plus de faux signaux). *Exemple :* EMA 20 → k \= 2/21 ≈ 0,0952.

### Réglages courants (🟡 CONVENTION)

Périodes fréquentes : **9, 20, 50, 200**. Aucune n'est « magique » ; ce sont des usages.

### Lectures (🔵 ÉCOLE)

- Prix au-dessus de la MM \= biais haussier ; en dessous \= baissier.  
- **Croisement (*crossover*)** : une MM rapide qui croise une MM lente est lue comme un signal de momentum. Souvent en retard sur les marchés rapides (scalping).

---

## 4.7 — RSI (Relative Strength Index)

🟢 **FAIT (origine).** Oscillateur créé par **J. Welles Wilder** (*New Concepts in Technical Trading Systems*, 1978). Borné entre **0 et 100**.

### Formule exacte (🟢 FAIT)

Variation(t)  \= Close(t) − Close(t−1)

Gain(t)       \= Variation si \> 0, sinon 0

Perte(t)      \= |Variation| si \< 0, sinon 0

1ʳᵉ moyenne (sur N=14) \= moyenne arithmétique des gains / des pertes

Lissage de Wilder (périodes suivantes) :

  MoyGain(t)  \= \[ MoyGain(t−1) × (N−1) \+ Gain(t) \] / N

  MoyPerte(t) \= \[ MoyPerte(t−1) × (N−1) \+ Perte(t) \] / N

RS  \= MoyGain / MoyPerte

RSI \= 100 − \[ 100 / (1 \+ RS) \]

### Réglages et seuils (🟡 CONVENTION)

- Période standard : **14** (Wilder). Variantes : 9 (plus réactif), 21/25 (plus lisse).  
- Seuils : **\> 70 suracheté**, **\< 30 survendu** (Wilder). Variante stricte : 80/20.

### Lectures et pièges

- 🔵 **Divergence RSI/prix** : prix fait un HH mais RSI fait un LH → essoufflement haussier possible (et inversement). Grille d'école, à confirmer.  
- 🟢 **PIÈGE MAJEUR :** « suracheté » **n'égale pas** « il faut vendre ». En forte tendance, le RSI peut rester \> 70 longtemps pendant que le prix continue de monter. Le RSI est une **information**, jamais un ordre.

---

## 4.8 — Analyse multi-unités de temps (multi-timeframe)

🟢 **FAIT.** Une unité de temps (*timeframe*, TF) \= la durée résumée par chaque bougie (1 min, 5 min, 1 h, journalier…).

### Principe top-down (🔵 ÉCOLE, très répandu)

1. **Grande TF** \= contexte (tendance \+ S/R majeurs). La « vue d'avion ».  
2. **Petite TF** \= timing d'entrée, dans le sens du contexte. La « rue où l'on marche ».

🟡 **CONVENTION de ratio :** on espace les TF d'un facteur \~**4 à 6×** (ex. 1 h pour le contexte → \~15 min ou 5 min pour l'entrée) pour qu'elles apportent une information complémentaire et non redondante.

### Confluence (🟢 FAIT conceptuel)

La **confluence** \= plusieurs éléments indépendants pointant vers la même idée (ex. support horizontal \+ VWAP \+ marteau \+ volume). Plus de confluence ≠ certitude, mais probabilité jugée plus favorable (🔵).

### Exemple chiffré (illustratif, contrat ES)

Valeurs d'illustration — pas des données de marché réelles.

- En **1 h** : structure HH/HL (haussière), support marqué vers **5 800**.  
- Le prix redescend vers **5 800**.  
- Passage en **5 min** : on attend une bougie de **rejet** (marteau / englobante haussière) sur 5 800, idéalement avec volume, au-dessus du VWAP.  
- Contexte (grande TF) \+ déclencheur (petite TF) dans le **même sens** \= confluence.

🟢 **Erreur classique :** entrer sur un signal de petite TF qui va **contre** la grande TF.

---

## 4.9 — Limites et garde-fous de l'AT (anti-hallucination)

🟢 **FAIT.** À intégrer dans tout raisonnement de l'IA TRADEX :

1. L'AT est **probabiliste** : raisonner en scénarios \+ invalidation, jamais en prédiction certaine.  
2. **Aucun indicateur magique** n'existe. Tout indicateur dérive du prix et est en retard sur lui.  
3. **Le prix prime sur l'indicateur.** En cas de contradiction, la structure de prix gagne.  
4. **Surcharge \= paralysie.** 2–3 outils maîtrisés \> 8 outils empilés.  
5. **Sur-optimisation (*overfitting*)** : un réglage parfait sur le passé ne garantit rien sur le futur.  
6. **Ne jamais inventer** un taux de réussite, une probabilité chiffrée ou une statistique. Si non mesuré → dire « non mesuré / dépend du contexte ».

---

## 📒 MINI-GLOSSAIRE

- **Swing high / low** : sommet / creux pivot validé par ses voisins.  
- **HH / HL / LH / LL** : codes de structure (sommets/creux plus hauts ou plus bas).  
- **BOS / CHoCH** : cassure de structure dans le sens / contre le sens (🔵 SMC).  
- **Support / Résistance** : zone-plancher (demande) / zone-plafond (offre).  
- **Polarité** : résistance cassée → support, et inversement.  
- **OHLC** : Open, High, Low, Close d'une bougie.  
- **Corps / mèche** : résultat net / zone testée puis rejetée.  
- **Doji, marteau, englobante, étoile filante/matin/soir, marubozu** : figures de bougies.  
- **Volume** : contrats échangés ; réel et centralisé sur futures CME.  
- **Tick volume** : substitut du volume sur marchés décentralisés (≠ volume réel).  
- **VWAP** : prix moyen pondéré par le volume, cumulé sur la séance.  
- **Anchored VWAP** : VWAP ancré à un événement précis.  
- **SMA / EMA** : moyenne mobile simple / exponentielle (k \= 2/(N+1)).  
- **RSI** : oscillateur 0–100 de Wilder ; 70/30 par convention.  
- **Divergence** : prix et indicateur pointent dans des sens opposés.  
- **Timeframe (TF)** : durée résumée par une bougie.  
- **Top-down** : contexte grande TF → entrée petite TF.  
- **Confluence** : alignement de plusieurs signaux indépendants.  
- **Lagging** : indicateur en retard sur le prix.  
- **Overfitting** : sur-optimisation sur données passées.

## 🎯 3 POINTS CLÉS

1. **Structure d'abord** : lire la séquence de pivots (HH/HL ou LH/LL) avant tout indicateur. Le contexte multi-TF gouverne.  
2. **Les outils suivent le prix** : RSI, MM et VWAP dérivent du prix et sont en retard. Suracheté ≠ vendre.  
3. **Confluence, pas certitude** : empiler des signaux *indépendants* augmente la probabilité, jamais à 100 %.

## 🏋️ EXERCICE (compte démo, sans argent réel)

Sur simulateur (ES ou NQ) :

1. En **1 h** : marque les pivots (HH/HL/LH/LL), déduis le régime (haussier / baissier / range), trace 2 supports \+ 2 résistances.  
2. Ajoute **VWAP** \+ **une seule** MM (EMA 20).  
3. Descends en **5 min** : observe la réaction du prix à chaque niveau (rejet ? cassure ? volume ?).  
4. Annote 3 séances. **Aucun trade.** Objectif : entraîner l'œil à lire structure \+ confluence.

---

*Fin du Chapitre 4 — version technique enrichie pour TRADEX-AI. Rappel : éducation, pas conseil financier.*  
