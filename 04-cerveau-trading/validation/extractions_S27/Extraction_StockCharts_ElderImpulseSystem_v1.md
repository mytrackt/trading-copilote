# Extraction StockCharts — Elder Impulse System
**Source :** `bundles/stockcharts/elder_impulse_system.md` (HTTP 200 · ~6 100 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D1651 → D1664 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of an Elder Impulse System chart showing when bulls (and bears are in control) | Calculating the Elder Impulse System | CERTIFIE (accord .md + HTML) |
| image_02.png | Daily bars with the Elder Impulse System with an EMA overlay (and MACD) | Timeframe | CERTIFIE (accord .md + HTML) |
| image_03.png | Elder Impulse System chart displaying bullish and bearish signals | Entries and Exits | CERTIFIE (accord .md + HTML) |
| image_04.png | Elder Impulse System SharpChart | Using Elder Impulse System With SharpCharts | CERTIFIE (accord .md + HTML) |
| image_05.png | How to access Elder Impulse System chart type in SharpCharts | Using Elder Impulse System With SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1651 — Définition : système de coloration de barres combinant tendance + momentum
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : Conçu par Alexander Elder (livre *Come Into My Trading Room*). Selon Elder, « the system identifies inflection points where a trend speeds up or slows down ». Le système repose sur deux indicateurs : une EMA 13 jours (identifie la tendance) et le MACD-Histogram (mesure le momentum). Il combine suivi de tendance et momentum pour identifier des « impulsions » tradables, codées en couleur dans les barres de prix.
**TRADEX-AI C1** : Outil composite tendance+momentum (école Elder, non Belkhayate) ; candidat comme module de coloration/diagnostic visuel, jamais comme déclencheur d'ordre.
*Catégorie : indicateurs_tendance*

---

### D1652 — Barre verte : EMA 13 montante ET MACD-H montant (contrôle haussier)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_01) : « Green Price Bar: (13-period EMA > previous 13-period EMA) and (MACD-Histogram > previous period's MACD-Histogram). » Les barres vertes montrent que les bulls contrôlent tendance ET momentum, l'EMA 13 et le MACD-H montant tous deux.
**TRADEX-AI C1** : Condition booléenne déterministe (double pente positive EMA13 + MACD-H) codable directement comme état « plein régime haussier ».
*Catégorie : signal*

---

### D1653 — Barre rouge : EMA 13 descendante ET MACD-H descendant (contrôle baissier)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : « Red Price Bar: (13-period EMA < previous 13-period EMA) and (MACD-Histogram < previous period's MACD-Histogram). » La barre rouge indique que les bears ont pris le contrôle car l'EMA 13 et le MACD-H baissent tous deux.
**TRADEX-AI C1** : Condition booléenne symétrique (double pente négative) codable comme état « plein régime baissier ».
*Catégorie : signal*

---

### D1654 — Barre bleue : signaux mixtes (aucune des deux conditions remplie)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : « Price bars are colored blue when conditions for a Red Price Bar or Green Price Bar is not met. » La barre bleue indique des signaux techniques mixtes — ni pression acheteuse ni pression vendeuse ne prédomine.
**TRADEX-AI C1** : Troisième état neutre/indécis exploitable comme zone d'attente (cohérent avec biais ATTENDRE par défaut du projet).
*Catégorie : signal*

---

### D1655 — Paramètres figés : EMA 13 jours + MACD-Histogram(12,26,9)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : « The MACD-Histogram is based on MACD(12,26,9). » La moyenne mobile utilisée est une EMA 13 périodes.
**TRADEX-AI C1** : Paramètres canoniques (EMA 13 ; MACD 12/26/9) à fixer si le module est implémenté ; aucune ambiguïté de réglage côté source.
*Catégorie : indicateurs_tendance*

---

### D1656 — Multi-timeframe : trading en harmonie avec la tendance majeure (règle du ×5)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : Le système s'utilise sur différents timeframes mais « trading should be in harmony with the bigger trend ». Elder recommande de fixer son timeframe de trading (« intermédiaire ») puis de le multiplier par cinq pour obtenir le timeframe long terme.
**TRADEX-AI C1** : Règle multi-timeframe déterministe (×5) ; cadre la logique d'alignement tendance majeure / tendance d'entrée du moteur.
*Catégorie : configuration*

---

### D1657 — Exemples de couples de timeframes (daily/weekly, 10min/60min, weekly/monthly)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : Daily (intermédiaire) → weekly (long terme). 10-minute → 60-minute. Weekly → monthly. « A little judgment is required » pour les très petits ou très grands timeframes.
**TRADEX-AI C1** : Tableau de correspondances de timeframes ; valeur de référence pour paramétrer l'alignement multi-échelle.
*Catégorie : configuration*

---

### D1658 — Proxy de tendance long terme : EMA 65 (= 5 × EMA 13) ou MACD(1,65,1)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_02) : Tendance long terme jugée haussière quand le prix est au-dessus de l'EMA 65 jours (cinq fois l'EMA 13) ou quand MACD(1,65,1) est positif. La page applique le MACD pour simplifier ; d'autres méthodes existent.
**TRADEX-AI C1** : Deux proxys quantitatifs de la tendance hebdomadaire sur un seul graphe (EMA 65 ou MACD 1/65/1) ; codables comme filtre directionnel macro de la figure.
*Catégorie : indicateurs_tendance*

---

### D1659 — Signal d'achat : tendance LT haussière + Impulse intermédiaire devenu haussier
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_03) : « A buy signal occurs when the long-term trend is deemed bullish, and the Elder Impulse System turns bullish on the intermediate-term trend. » Le weekly doit montrer un uptrend clair pour qu'un buy daily soit valide ; sinon le buy daily est ignoré.
**TRADEX-AI C1** : Règle d'entrée à double condition (filtre LT + bascule intermédiaire) ; codable comme garde-fou évitant les signaux contre-tendance.
*Catégorie : signal*

---

### D1660 — Signal de vente : tendance LT baissière + Impulse intermédiaire devenu baissier
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : « A sell signal occurs when the long-term trend is deemed bearish, and the Elder Impulse System turns bearish on the intermediate-term trend. » Le weekly doit montrer un downtrend clair pour qu'un sell daily soit valide ; sinon ignoré.
**TRADEX-AI C1** : Règle de sortie/vente symétrique à double condition ; codable comme filtre directionnel.
*Catégorie : signal*

---

### D1661 — Filtre opérationnel : MACD(1,65,1) > 0 = weekly up ; < 0 = weekly down
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_03) : Le daily ajoute MACD(1,65,1) pour matérialiser la tendance weekly. « If the MACD is above zero, the weekly trend is up. If it is below zero, the weekly trend is down. »
**TRADEX-AI C1** : Critère de bascule déterministe (signe du MACD 1/65/1) pour autoriser/bloquer les signaux ; test booléen direct.
*Catégorie : signal*

---

### D1662 — Lecture des clusters : grappes de barres vertes = buys valides ; rouges après bascule weekly = sells valides
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_03) : Sur l'exemple, les trois premières flèches vertes = buys daily valides (nouveaux clusters de barres vertes). Les premières barres rouges ne sont PAS des sells valides tant que le weekly reste positif (MACD) ; ce n'est qu'après bascule baissière du weekly que la première vente est valide. Symétriquement le weekly doit redevenir positif avant tout nouvel achat valide.
**TRADEX-AI C1** : Confirme que le filtre tendance majeure prime sur la couleur locale ; logique anti faux-signal codable.
*Catégorie : signal*

---

### D1663 — Philosophie : entrer prudemment, sortir vite (catch des mouvements courts)
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md) : Système conçu pour capter des mouvements de prix relativement courts. Elder : « The Impulse System encourages you to enter cautiously but exit fast... the total opposite of the amateur's style. »
**TRADEX-AI C5** : Cadre psychologique/gestion (entrée prudente, sortie rapide) ; aligné avec la prudence du projet, mais reste une recommandation, pas un paramètre.
*Catégorie : gestion_risque_entree*

---

### D1664 — Usage en filtre de confirmation et anticipation de figures/retournements
🔵 **ÉCOLE (Elder)** (Source : elder_impulse_system.md, image_04, image_05) : Au-delà des setups, le système peut prévenir de mauvais trades en confirmant les setups : ignorer un setup haussier si le système n'est pas en plein régime vert ; ignorer un signal baissier s'il n'est pas en plein régime rouge. Il peut aussi anticiper figures/retournements (ex. bull flag pressenti ou retracement Fibonacci proche → l'Impulse confirme un retournement court terme). Accès via Chart Type « Elder Impulse System » dans SharpCharts.
**TRADEX-AI C1** : Mode d'emploi « filtre de confirmation » (vert plein / rouge plein) directement transposable comme pondération de score ; aucun paramètre neuf.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1651 | Définition système couleur tendance+momentum | 🔵 | C1 | indicateurs_tendance |
| D1652 | Barre verte : EMA13↑ ET MACD-H↑ | 🔵 | C1 | signal |
| D1653 | Barre rouge : EMA13↓ ET MACD-H↓ | 🔵 | C1 | signal |
| D1654 | Barre bleue : signaux mixtes | 🔵 | C1 | signal |
| D1655 | Paramètres EMA 13 + MACD(12,26,9) | 🔵 | C1 | indicateurs_tendance |
| D1656 | Multi-timeframe : règle du ×5 | 🔵 | C1 | configuration |
| D1657 | Couples de timeframes types | 🔵 | C1 | configuration |
| D1658 | Proxy LT : EMA 65 ou MACD(1,65,1) | 🔵 | C1 | indicateurs_tendance |
| D1659 | Buy : LT haussière + Impulse intermédiaire haussier | 🔵 | C1 | signal |
| D1660 | Sell : LT baissière + Impulse intermédiaire baissier | 🔵 | C1 | signal |
| D1661 | Filtre MACD(1,65,1) ≷ 0 | 🔵 | C1 | signal |
| D1662 | Lecture clusters (filtre weekly prime) | 🔵 | C1 | signal |
| D1663 | Entrer prudemment, sortir vite | 🔵 | C5 | gestion_risque_entree |
| D1664 | Filtre de confirmation / anticipation figures | 🔵 | C1 | configuration |

**Liens Belkhayate :** Le Elder Impulse System est un système Alexander Elder (🔵 école), PAS un élément de la méthode Belkhayate. Aucune correspondance directe affirmée par la source (NON CONCERNÉ). Rapprochement possible mais NON affirmé : la combinaison tendance (EMA) + momentum recoupe l'esprit « Direction + Énergie » de Belkhayate ; l'attribuer à Belkhayate serait une hypothèse projet (⚫🔴), non soutenue par StockCharts.

**À vérifier (humain) :**
- Conflit d'indicateurs : le moteur Belkhayate utilise le MFI pour l'« Énergie » (mémoire projet) tandis qu'Elder utilise MACD-Histogram pour le momentum — ne pas fusionner les deux sans arbitrage explicite.
- Paramètre EMA 65 / MACD(1,65,1) : proxy hebdomadaire propre à l'exemple SPY/INDU ; à revalider sur range bars NT8 (GC/HG/CL/ZW) car les timeframes Belkhayate diffèrent (Standard 15min / Range Bar 4-5t).
- Couleur des barres : module purement visuel/diagnostic — décider s'il alimente le score /10 ou reste indicatif.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
