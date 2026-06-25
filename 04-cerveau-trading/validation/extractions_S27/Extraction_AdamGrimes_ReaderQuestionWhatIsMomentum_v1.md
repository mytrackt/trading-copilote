# Extraction AdamGrimes — Reader Question: What is Momentum?
**Source :** `bundles/adamgrimes/reader_question_what_is_momentum.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6531 → D6544 · **Page :** https://www.adamhgrimes.com/reader-question-what-is-momentum/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le momentum (vitesse prix/temps) est un signal de force directionnelle utilisable en C1/C5 pour qualifier la validité d'un signal Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6531 — Momentum : définition unifiée (3 usages)
🔵 **ÉCOLE** (Source : reader_question_what_is_momentum.md) : Le mot "momentum" désigne trois choses distinctes en trading — (1) l'indicateur technique (variation % sur N périodes), (2) le facteur académique de sélection de portefeuille (performance relative), (3) la description comportementale de la force d'un mouvement de prix (vitesse × amplitude).
**TRADEX-AI C1** : Lors de l'analyse de signaux, distinguer clairement si "momentum" désigne un indicateur calculé, un rang relatif, ou une observation comportementale de la bougie/range bar NT8.
*Catégorie : indicateurs_momentum*

### D6532 — Indicateur Momentum = variation % sur N périodes
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_what_is_momentum.md) : L'indicateur Momentum est calculé : `prix_today / prix_(N_périodes_avant) − 1`, multiplié par 100. Un résultat de 10 = +10%. C'est une mesure de taux de changement (ROC) pure, sans lissage.
**TRADEX-AI C1** : Dans le moteur Python, un ROC simple sur les données NT8 (JSON) peut servir de filtre de momentum rapide avant d'appeler Claude API. Aucune bibliothèque externe requise.
*Catégorie : indicateurs_momentum*

### D6533 — Facteur momentum académique = performance relative inter-actifs
🔵 **ÉCOLE** (Source : reader_question_what_is_momentum.md) : Le facteur momentum académique classe tous les actifs d'un univers selon leur performance sur une période identique, puis sélectionne les N% les plus forts. Hypothèse validée historiquement : les gagnants d'un groupe tendent à continuer à surperformer.
**TRADEX-AI C7** : La matrice de corrélations live 30j (GC/HG/CL/ZW/ES/VX) peut intégrer un classement de performance relative pour identifier l'actif le plus fort à l'instant t, en appui de la règle 3/4 tradables alignés.
*Catégorie : correlations*

### D6534 — Momentum comportemental : force derrière un mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_what_is_momentum.md) : Adam Grimes définit le momentum comportemental comme "la quantité de déplacement du marché par unité de temps". Un mouvement de prix fort est soutenu par une psychologie sous-jacente forte. Les mouvements sans momentum (pas de toucher des Keltner Channels) ne génèrent pas de suivi.
**TRADEX-AI C1** : La règle Belkhayate "3/4 actifs trading alignés" doit s'appuyer sur des mouvements avec momentum réel. Un signal où le prix n'a pas touché ses canaux de volatilité équivalents (ATR, Keltner) est à pondérer en baisse dans le score /10.
*Catégorie : indicateurs_momentum*

### D6535 — Keltner Channels comme proxy de momentum fort
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_what_is_momentum.md) : L'incapacité d'un prix à toucher les Keltner Channels signale l'absence de momentum. À l'inverse, un toucher des canaux confirme un momentum fort derrière le mouvement. Ce test est applicable à tout timeframe.
**TRADEX-AI C1** : Intégrer un test Keltner (ou bandes ATR équivalentes sur range bars NT8) dans la validation de signal : toucher de bande supérieure/inférieure = momentum confirmé → poids +0,5 dans grille /10. Absence de toucher = poids -0,5.
*Catégorie : indicateurs_momentum*

### D6536 — MACD ligne rapide comme mesure directe du momentum
🔵 **ÉCOLE** (Source : reader_question_what_is_momentum.md) : La ligne rapide (bleue) du MACD est un indicateur "quick-and-dirty" du momentum. Un nouveau plus-haut ou plus-bas significatif de cette ligne par rapport à son historique récent confirme un momentum directionnel.
**TRADEX-AI C1** : La ligne rapide MACD peut servir de filtre secondaire de confirmation en Couche 1 (analyse Python pure, coût 0$). Si MACD fast line ne confirme pas le mouvement de prix → signal downgraded.
*Catégorie : indicateurs_momentum*

### D6537 — Spikes de sigma (±2σ) pour mesurer la direction du momentum
🟢 **FAIT VÉRIFIÉ** (Source : reader_question_what_is_momentum.md) : L'analyse des spikes journaliers ajustés à la volatilité (±2 sigma) révèle la direction dominante du momentum : une asymétrie vers les spikes baissiers après un point de rupture indique un momentum vendeur installé.
**TRADEX-AI C1** : Dans le moteur de surveillance Python (cycle 2s), un compteur de spikes σ sur la fenêtre glissante des N dernières barres peut qualifier la direction dominante du momentum sans appel Claude API. Asymétrie >2:1 = signal directionnel renforcé.
*Catégorie : indicateurs_momentum*

### D6538 — Momentum = relation prix/temps : vélocité et force
🟡 **SYNTHÈSE** (Source : reader_question_what_is_momentum.md) : Toutes les définitions du momentum convergent vers un concept unique — la relation entre la variation de prix et le temps (vitesse, vélocité, force). Comprendre cette relation donne des insights sur la psychologie du marché, le comportement des prix, et les opportunités de trading.
**TRADEX-AI C1+C5** : Le prompt Claude (Niveau 3) doit demander explicitement au cerveau d'évaluer la vélocité du mouvement en cours pour GC/HG/CL/ZW avant de rendre un verdict ACHETER/VENDRE/ATTENDRE. La vélocité insuffisante = signal ATTENDRE automatique.
*Catégorie : structure_marche*

### D6539 — Risque de mean reversion du momentum : toujours acheter les plus forts expose au snapback
⚠️ **Risque identifié** — 🟡 **SYNTHÈSE** (Source : reader_question_what_is_momentum.md) : La stratégie d'achat du momentum (toujours acheter les plus forts actifs) expose au mean reversion et au snapback violent. L'edge historique existe sur portefeuille diversifié, mais pas nécessairement sur actifs individuels à court terme.
**TRADEX-AI C1** : La règle garde-fou : un actif qui a déjà réalisé un spike de momentum extrême (±3σ) ne doit pas être tradé dans la direction du spike — risque de retour à la moyenne. Filtrer dans la grille /10 : score -1 si spike extrême récent.
*Catégorie : gestion_risque_entree*
