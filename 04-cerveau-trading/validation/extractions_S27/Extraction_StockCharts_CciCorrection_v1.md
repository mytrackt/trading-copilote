# Extraction StockCharts — CCI Correction
**Source :** `bundles/stockcharts/cci_correction.md` (HTTP 200 · ~10 300 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D1131 → D1144 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/cci-correction
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - CCI Corrections | Strategy | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 - CCI Corrections | Strategy | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 - CCI Corrections | Trading Examples | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 - CCI Corrections | Trading Examples | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 5 - CCI Corrections | Trading Examples | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 6 - CCI Corrections | Adjusting | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1131 — Origine et nature du CCI (Lambert)
🔵 **ÉCOLE (Lambert)** (Source : cci_correction.md) : Développé par Donald Lambert, le Commodity Channel Index (CCI) est un oscillateur de momentum servant à identifier une nouvelle tendance ou à avertir de conditions extrêmes. La stratégie CCI Correction utilise un CCI hebdomadaire pour fixer le biais directionnel (surge > +100 ou plunge < -100, niveaux clés de Lambert), puis un CCI quotidien pour générer des signaux aux extrêmes.
**TRADEX-AI C1** : Oscillateur de momentum candidat comme indicateur de biais multi-timeframe ; jamais standalone (cf. D1144).
*Catégorie : indicateurs_momentum*

---

### D1132 — Règle de base de Lambert (+100 / -100)
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : Les règles de Lambert reposent sur les franchissements de +100 et -100. Comme 70 à 80 % des valeurs du CCI sont entre +100 et -100, un signal n'est en force que 20 à 30 % du temps. CCI > +100 = entrée en fort uptrend → signal d'achat ; clôturer quand le CCI repasse sous +100. CCI < -100 = fort downtrend → signal de vente ; clôturer quand le CCI repasse au-dessus de -100.
**TRADEX-AI C1** : Seuils déterministes ±100 implémentables ; mais la sortie « retour sous/au-dessus du seuil » produit beaucoup de signaux courts (limite corrigée en D1133).
*Catégorie : signal*

---

### D1133 — Limite de la stratégie originale et tweak « Correction »
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : En imposant la sortie sur retour sous +100 / au-dessus de -100, la stratégie originale de Lambert produit beaucoup de signaux relativement courts. La CCI Correction propose un ajustement tout en conservant les guidelines générales (surge > +100 ou plunge < -100), en trois étapes.
**TRADEX-AI C1** : Justification du passage à une logique multi-timeframe (réduire le bruit). Pertinent pour limiter le rate de faux signaux.
*Catégorie : signal*

---

### D1134 — Étape 1 : définir le biais via le CCI hebdomadaire
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_01) : Étape 1 — un surge du CCI > +100 sur le graphique HEBDO indique un uptrend émergent → biais haussier adopté, maintenu jusqu'à un plunge < -100. Un plunge < -100 en hebdo → biais baissier, maintenu jusqu'à preuve contraire par un surge > +100.
**TRADEX-AI C1** : Machine à états de biais (bull/bear) pilotée par le timeframe supérieur. Transposable en filtre directionnel persistant ; recoupe l'idée d'analyse top-down.
*Catégorie : structure_marche*

---

### D1135 — Étape 2 : attendre un contre-mouvement sur le timeframe inférieur
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_02) : Étape 2 — sur le graphique quotidien, chercher les pullbacks surachetés/survendus contraires au biais. Biais haussier : un plunge du CCI daily < -100 reflète un pullback dans l'uptrend majeur. Biais baissier : un surge daily > +100 indique un rebond dans le downtrend majeur.
**TRADEX-AI C1** : Logique « acheter le repli dans la tendance » ; le contre-mouvement crée le point d'entrée à meilleur R/R (cf. D1137).
*Catégorie : timing*

---

### D1136 — Étape 3 : entrer sur le retournement du contre-mouvement
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : Étape 3 — biais haussier et CCI daily descendu < -100 : un retour (surge) en territoire positif signale le retournement du pullback et la reprise de l'uptrend. Biais baissier et CCI daily > +100 : un plongeon en territoire négatif signale le retournement du rebond et la reprise du downtrend.
**TRADEX-AI C1** : Déclencheur d'entrée = recroisement (zero line) après pullback, dans le sens du biais. Séquence pullback→reversal codable en machine à états.
*Catégorie : signal*

---

### D1137 — Principe directeur : trader dans le sens de la tendance majeure
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : L'idée générale est de trader dans la direction de la tendance majeure et de raccourcir le timeframe pour chercher les signaux sur la tendance courte. En théorie, toute combinaison de timeframes peut servir (ex. daily pour le biais, 30 minutes pour les signaux). Initier les positions après une correction améliore le ratio risque/récompense.
**TRADEX-AI C1** : Confluence multi-timeframe + entrée post-correction = meilleur R/R (≥ 1:2 projet). Choix des timeframes paramétrable (cohérent avec les timeframes Belkhayate par mode).
*Catégorie : gestion_risque_entree*

---

### D1138 — Choix du 26-week CCI pour le biais (exemple SPY)
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_03) : Le premier graphique montre SPY avec un CCI 26 semaines (≈ 6 mois, bon repère de tendance moyen/long terme). Les zones jaunes = mode bull (dernier signal = surge > +100) ; les zones blanches = mode bear (dernier signal = plunge < -100). Les graphiques suivants utilisent des barres daily et un CCI 26 jours pour générer les signaux 2008/2009/2010.
**TRADEX-AI C1** : Paramètre de référence (26 périodes ≈ 6 mois) pour le biais ; la longueur du look-back fixe l'horizon de tendance.
*Catégorie : configuration*

---

### D1139 — Exemple 2008 : biais bear, n'écouter que les signaux baissiers
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_04) : Le CCI hebdo passe en mode bear en novembre 2007. On aborde alors le daily avec un biais baissier et on ne cherche QUE des signaux baissiers (les haussiers sont ignorés car la tendance majeure est baissière). Rappel : un signal baissier = surge > +100 puis passage sous la ligne zéro. Sur cinq signaux montrés, celui de fin février ne fonctionne pas bien, mais les autres correspondent bien aux pics de SPY.
**TRADEX-AI C1** : Filtrage directionnel strict (un seul sens selon le biais) ; confirme que tous les signaux ne réussissent pas → gestion du risque obligatoire.
*Catégorie : signal*

---

### D1140 — Exemple 2009 : changement de biais et near-signals
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_05) : Le CCI hebdo bascule de bear à bull début mai 2009. Avant ce basculement, le daily a produit un bon signal de vente début janvier. Après le basculement, un signal d'achat en mi-juillet (CCI plongeant < -100 puis repassant au-dessus de zéro) s'avère opportun. Deux « near-signals » : le CCI a touché -97 fin juin et début novembre sans déclencher.
**TRADEX-AI C1** : Notion de « near-signal » (seuil frôlé sans franchissement) → importance d'une règle stricte de franchissement, et zone grise nécessitant jugement humain.
*Catégorie : signal*

---

### D1141 — Exemple 2010 : trois périodes de biais, signaux gagnants et perdants
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : 2010 commence avec un biais haussier, bascule en baissier fin juin, puis revient haussier début octobre — trois périodes distinctes. Le premier signal haussier mi-février précède une belle avance ; le signal haussier mi-juin aurait été perdant après le déclin sous 100. Le signal baissier d'août a eu un certain follow-through mais un bon stop-loss était nécessaire pour verrouiller le profit ou éviter une perte.
**TRADEX-AI C1** : Confirme que la stratégie produit aussi des pertes ; un stop-loss est indispensable. Aligné avec les garde-fous du projet.
*Catégorie : gestion_risque_entree*

---

### D1142 — Adaptation mono-timeframe : émuler l'hebdo via un look-back plus long
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md, image_06) : Utiliser deux timeframes peut être lourd. On peut émuler le CCI hebdo sur le daily avec un look-back plus long : l'exemple utilise un CCI 100 jours (au lieu d'un CCI hebdo) pour le biais — bull après surge > +100 (zones jaunes), bear après plunge < -100 (zones blanches) — et un CCI 20 jours pour les signaux. Exemple : signaux baissiers fin juin et début août, puis biais haussier dès mi-septembre 2010, fort uptrend, CCI 20 jours ne replongeant sous -100 qu'en mars 2011 (six mois plus tard). Un « near-signal » en novembre (CCI à -94) a nécessité du jugement personnel.
**TRADEX-AI C1** : Alternative implémentable sur un seul flux : long look-back (100) = biais, court look-back (20) = signaux. Réduit la complexité multi-source.
*Catégorie : configuration*

---

### D1143 — Recommandation : éviter le curve-fitting, pas de réglage parfait
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : Les exemples montrent qu'il est quasi impossible de trouver le réglage parfait, et les chartistes doivent éviter le curve-fitting en concevant une stratégie. La CCI Correction n'est PAS un système autonome : il faut décider des stop-loss, des prises de profit et adapter la stratégie à ses propres objectifs et style.
**TRADEX-AI C1** : Garde-fou anti-surapprentissage (cohérent avec walk-forward du projet) ; impose stop-loss et prise de profit explicites. Paramètres = points de départ, pas optimaux.
*Catégorie : gestion_risque_entree*

---

### D1144 — Synthèse : trader avec la tendance après correction, jamais en standalone
🟢 **FAIT VÉRIFIÉ** (Source : cci_correction.md) : La CCI Correction combine le « trading avec la tendance » et l'« initiation après une phase corrective ». Traders agressifs : look-back plus court pour des signaux plus rapides ; moins agressifs : un surge > +100 (ou plunge < -100) pour générer les signaux sur le timeframe court. L'article est un point de départ pour développer un système, à augmenter selon style, préférences risque/récompense et jugement personnel.
**TRADEX-AI C1** : Règle architecturale — stratégie paramétrable (agressivité = longueur de look-back) ; toujours encadrée par gestion du risque et jugement. Jamais déclencheur unique.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1131 | Origine et nature du CCI (Lambert) | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D1132 | Règle de base ±100 | 🟢 | C1 | signal |
| D1133 | Limite originale + tweak Correction | 🟢 | C1 | signal |
| D1134 | Étape 1 — biais via CCI hebdo | 🟢 | C1 | structure_marche |
| D1135 | Étape 2 — contre-mouvement (TF inférieur) | 🟢 | C1 | timing |
| D1136 | Étape 3 — entrée sur retournement | 🟢 | C1 | signal |
| D1137 | Trader dans le sens de la tendance majeure | 🟢 | C1 | gestion_risque_entree |
| D1138 | 26-week CCI pour le biais (SPY) | 🟢 | C1 | configuration |
| D1139 | Exemple 2008 — filtrage directionnel | 🟢 | C1 | signal |
| D1140 | Exemple 2009 — near-signals | 🟢 | C1 | signal |
| D1141 | Exemple 2010 — gagnants/perdants + stop | 🟢 | C1 | gestion_risque_entree |
| D1142 | Émuler l'hebdo via long look-back (100/20) | 🟢 | C1 | configuration |
| D1143 | Anti curve-fitting, pas de réglage parfait | 🟢 | C1 | gestion_risque_entree |
| D1144 | Synthèse — avec la tendance, jamais standalone | 🟢 | C1 | signal |

**Liens Belkhayate :** la stratégie CCI Correction et le CCI de Lambert ne font PAS partie de la méthode Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé par Belkhayate) : la logique multi-timeframe « biais sur TF supérieur → entrée sur repli en TF inférieur » recoupe l'esprit de l'analyse Belkhayate par mode/timeframe (Standard 15 min, Rapide Range Bar, Scalping), et la notion de Direction (étape 3 Belkhayate) peut faire écho au biais directionnel. Mais le CCI n'est pas un indicateur Belkhayate et l'Énergie Belkhayate = MFI standard, distinct du CCI. Ne rien inventer.

**À vérifier (humain) :**
- D1138 / D1142 — les look-backs (26 semaines / 100 jours / 20 jours) sont des exemples StockCharts sur actions ; à recalibrer et backtester (walk-forward) sur GC/HG/CL/ZW en Range Bars avant tout codage.
- D1132 / D1136 — la sortie/entrée « retour au-dessus/sous le seuil » génère des signaux courts et des near-signals (-94/-97 frôlant -100) : définir une règle stricte de franchissement + buffer pour le moteur, la source laissant place au jugement humain.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
