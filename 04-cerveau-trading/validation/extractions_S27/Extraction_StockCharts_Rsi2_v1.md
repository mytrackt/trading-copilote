# Extraction StockCharts — RSI(2) (stratégie Connors)
**Source :** `bundles/stockcharts/rsi_2.md` (HTTP 200 · ~8 200 car.) + 4 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D3511 → D3525 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔵 Stratégie d'ÉCOLE Larry Connors (mean-reversion court terme) — distincte de la méthode Belkhayate. À traiter comme variante d'école, JAMAIS comme règle Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - RSI(2) | Strategy | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 - RSI(2) | Trading Examples | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 - RSI(2) | Trading Examples | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 - RSI(2) | Tweaking the 2-Period RSI Strategy | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3511 — Nature de la stratégie RSI(2)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Larry Connors a développé la stratégie RSI 2-périodes, une stratégie de retour à la moyenne (mean-reversion) relativement simple, conçue pour acheter ou vendre des titres après une période corrective. C'est une stratégie court terme plutôt agressive, conçue pour participer à une tendance en cours — PAS pour identifier les sommets ou creux majeurs.
**TRADEX-AI C1** : Stratégie de mean-reversion d'école Connors, court terme et agressive. Logique « contre-tendance dans la tendance » — à confronter à la logique Belkhayate, pas à fusionner d'office. Cohérence avec modes Rapide / Scalping TRADEX à évaluer.
*Catégorie : signal*

---

### D3512 — Avertissement éducatif explicite de la source
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : La source précise que l'article est conçu pour éduquer sur des stratégies possibles et NE présente PAS une stratégie clé en main utilisable telle quelle. Il vise à enrichir le développement et le raffinement de stratégie.
**TRADEX-AI C1** : Garde-fou source : ne pas coder cette stratégie telle quelle en production. Matériau pédagogique uniquement. Cohérent avec le statut BRUT/validation TRADEX.
*Catégorie : signal*

---

### D3513 — Étape 1 : tendance majeure via SMA 200
🔵 **ÉCOLE Connors** (Source : rsi_2.md, image_01) : Première étape — identifier la tendance majeure via une moyenne mobile long terme ; Connors recommande la SMA 200 jours. Tendance haussière quand le titre est au-dessus de sa SMA 200, baissière en dessous. Chercher des achats au-dessus de la SMA 200, des ventes à découvert en dessous.
**TRADEX-AI C1** : Filtre directionnel : SMA 200 = juge de la tendance majeure. Achats seulement au-dessus, ventes shorts seulement en dessous. Paramètre quantitatif net (période 200) — à transposer/valider sur l'unité de temps TRADEX.
*Catégorie : indicateurs_momentum*

---

### D3514 — Étape 2 : seuils RS(2) d'entrée (5/95 plus performants que 10/90)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Deuxième étape — choisir un niveau RSI. Connors a testé 0-10 pour l'achat et 90-100 pour la vente (sur clôtures). Les rendements étaient plus élevés en achetant sur un repli du RSI sous 5 plutôt que sous 10 ; plus le RSI plonge bas, plus les rendements ultérieurs sont élevés. Pour les shorts, rendements plus élevés en vendant au-dessus de 95 plutôt que 90.
**TRADEX-AI C1** : Paramètres quantitatifs : seuils achat RSI(2) < 5 (préféré à < 10), short RSI(2) > 95 (préféré à > 90), basés sur clôtures. Codables, mais résultats issus de backtests actions/indices — non transférables d'office aux futures.
*Catégorie : indicateurs_momentum*

---

### D3515 — Étape 3 : timing de l'ordre (avant clôture vs ouverture suivante)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Troisième étape — l'ordre et son timing. On peut entrer juste avant la clôture ou à l'ouverture suivante. Connors préconise l'approche avant-clôture. Mais entrer avant la clôture expose au gap de l'ouverture suivante (bénéfique ou défavorable). Attendre l'ouverture donne plus de flexibilité et peut améliorer le niveau d'entrée.
**TRADEX-AI C1** : Choix de timing d'exécution : avant clôture (préconisé Connors, risque de gap) ou ouverture suivante (plus flexible). Décision d'exécution à arbitrer selon l'actif/mode — pertinent pour le module d'exécution.
*Catégorie : gestion_risque_entree*

---

### D3516 — Étape 4 : sortie via SMA 5 (ou trailing stop / SAR)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Quatrième étape — point de sortie. Sur l'exemple S&P 500, Connors préconise de sortir les longs sur passage au-dessus de la SMA 5 jours et les shorts sous la SMA 5 jours — sorties rapides (stratégie court terme). À envisager aussi : trailing stop ou Parabolic SAR pour laisser courir une tendance forte.
**TRADEX-AI C1** : Règle de sortie : longs fermés au-dessus SMA 5, shorts sous SMA 5 ; alternatives trailing stop / Parabolic SAR. Logique de sortie codable (SMA 5), à recalibrer hors actions journalières.
*Catégorie : gestion_risque_entree*

---

### D3517 — Pas de stops (position Connors) — risque assumé
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Connors ne préconise PAS l'usage de stops. Ses tests quantitatifs (centaines de milliers de trades) ont montré que les stops « nuisent » à la performance sur actions et indices. Bien que le marché ait une dérive haussière, ne pas utiliser de stops peut entraîner de lourdes pertes et de larges drawdowns — proposition risquée ; au trader de décider.
**TRADEX-AI C1** : ⚠️ Point de DIVERGENCE FORTE avec les garde-fous TRADEX : « pas de stops » est INCOMPATIBLE avec les sécurités obligatoires (gestion du risque, R/R ≥ 1:2, drawdown). NE PAS reprendre cette recommandation. À noter comme contre-exemple de risque.
*Catégorie : gestion_risque_entree*

---

### D3518 — Exemple DIA : sept signaux (4 haussiers / 3 baissiers)
🔵 **ÉCOLE Connors** (Source : rsi_2.md, image_02) : Sur le SPDR Dow (DIA) avec SMA 200 (rouge), SMA 5 (rose) et RSI(2) : signal haussier quand DIA > SMA 200 ET RSI(2) ≤ 5 ; signal baissier quand DIA < SMA 200 ET RSI(2) ≥ 95. Sur 12 mois : sept signaux (4 haussiers, 3 baissiers). Sur les 4 haussiers, DIA a monté 3 fois sur 4 (potentiellement profitables) ; sur les 3 baissiers, DIA n'a baissé qu'une seule fois.
**TRADEX-AI C1** : Illustration des conditions composées (filtre SMA 200 + seuil RSI 5/95). Performance illustrative non garantie. Confirme la mécanique D3513/D3514.
*Catégorie : signal*

---

### D3519 — Exemple AAPL : signaux précoces (limites de la stratégie)
🔵 **ÉCOLE Connors** (Source : rsi_2.md, image_03) : Sur Apple (AAPL) au-dessus de sa SMA 200 la plupart du temps : au moins dix signaux d'achat. Les cinq premiers auraient été difficiles à éviter en perte (AAPL en zigzag baissier fév→juin 2011) ; les cinq suivants bien meilleurs (zigzag haussier août→janvier). Beaucoup de signaux étaient précoces : AAPL faisait de nouveaux plus bas après le signal d'achat initial avant de rebondir.
**TRADEX-AI C1** : Limite documentée : signaux souvent PRÉCOCES (le mouvement continue après le signal). Filtre anti-faux-signal nécessaire (cf. D3521). Confirme le caractère agressif/contre-tendance.
*Catégorie : signal*

---

### D3520 — Curve fitting : risque à éviter
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Comme pour toute stratégie, il faut étudier les signaux et chercher à améliorer les résultats, MAIS la clé est d'éviter le curve fitting (surajustement), qui réduit les chances de succès futur.
**TRADEX-AI C1** : Garde-fou méthodologique : éviter le curve fitting lors du tuning. Cohérent avec les exigences de robustesse / walk-forward déjà en KB (sources arXiv). Principe transversal validation.
*Catégorie : signal*

---

### D3521 — Filtre par retour à la médiane (centerline 50)
🔵 **ÉCOLE Connors** (Source : rsi_2.md, image_04) : Pour remédier aux signaux précoces, chercher un indice que les prix se sont retournés après l'extrême du RSI(2) : analyse en chandeliers, figures intraday, autres oscillateurs, ou tweaks du RSI(2). Concrètement : filtrer un short en attendant que RSI(2) repasse SOUS sa médiane (50) ; filtrer un achat (titre > SMA 200, RSI(2) < 5) en attendant que RSI(2) repasse AU-DESSUS de 50 — signalant un retournement court terme effectif. Exemple Google : signaux filtrés par croisement de la médiane (50), bons et mauvais signaux.
**TRADEX-AI C1** : Amélioration codable : filtre de confirmation par croisement de la médiane RSI(2)=50 (réduit les entrées précoces). Attention : les gaps (saisons de résultats) peuvent perturber les trades. Paramètre net (50) intégrable au détecteur.
*Catégorie : indicateurs_momentum*

---

### D3522 — Philosophie Connors : acheter les pullbacks, vendre les rebonds
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : La stratégie permet de participer à une tendance en cours. Connors affirme qu'il faut acheter les replis (pullbacks), pas les cassures (breakouts) ; et inversement, vendre les rebonds de survente (oversold bounces), pas les cassures de support. La stratégie épouse cette philosophie.
**TRADEX-AI C1** : Principe directeur d'école : entrée contre-tendance dans le sens de la tendance majeure (pullback long / bounce short). Cadre conceptuel à confronter à la logique de cassure/alignement Belkhayate avant tout usage.
*Catégorie : signal*

---

### D3523 — Recommandation finale : prévoir stop/exit malgré les tests
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Bien que les tests de Connors montrent que les stops nuisent à la performance, la source juge prudent de développer une stratégie de sortie et de stop-loss pour tout système. Sorties possibles : fermer les longs en zone surachetée (ou trailing stop), fermer les shorts en zone survendue. L'article est un point de départ pour développer un système.
**TRADEX-AI C1** : Nuance importante : la source RECOMMANDE finalement un stop-loss/exit (contrairement à D3517). Pour TRADEX, retenir CETTE recommandation (stop obligatoire) et écarter la position « pas de stops ». Aligné garde-fous risque.
*Catégorie : gestion_risque_entree*

---

### D3524 — Scan « Buy Signal » (filtre Ean)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Scan d'achat RSI(2) (syntaxe StockCharts) : type = stock ; SMA(20, volume) > 40000 ; SMA(60, close) > 20 ; close > SMA(200, close) ; et croisement « 5 x today's rsi(2) » (RSI(2) franchissant 5 à la hausse). Conditions de liquidité (volume) et de prix minimal incluses.
**TRADEX-AI C1** : Critères opérationnels de scan : filtre de liquidité (SMA20 volume > 40000), prix minimal (SMA60 close > 20), tendance (close > SMA200), déclencheur RSI(2) franchissant 5. Logique de filtre transposable (hors syntaxe propriétaire).
*Catégorie : signal*

---

### D3525 — Scan « Sell Signal » (filtre short)
🔵 **ÉCOLE Connors** (Source : rsi_2.md) : Scan de vente RSI(2) : type = stock ; SMA(20, volume) > 40000 ; SMA(60, close) > 20 ; close < SMA(200, close) ; et « today's rsi(2) x 95 » (RSI(2) franchissant 95 à la hausse) → signal de vente short.
**TRADEX-AI C1** : Symétrie du scan achat : mêmes filtres liquidité/prix, tendance baissière (close < SMA200), déclencheur RSI(2) > 95. Logique miroir transposable. Réservé analyse — mode AUTO bloqué par défaut.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3511 | Nature mean-reversion court terme | 🔵 ÉCOLE | C1 | signal |
| D3512 | Avertissement éducatif source | 🔵 ÉCOLE | C1 | signal |
| D3513 | Étape 1 : tendance via SMA 200 | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D3514 | Étape 2 : seuils 5/95 (vs 10/90) | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D3515 | Étape 3 : timing (avant clôture/ouverture) | 🔵 ÉCOLE | C1 | gestion_risque_entree |
| D3516 | Étape 4 : sortie SMA 5 / trailing / SAR | 🔵 ÉCOLE | C1 | gestion_risque_entree |
| D3517 | Pas de stops (Connors) — DIVERGENCE | 🔵 ÉCOLE | C1 | gestion_risque_entree |
| D3518 | Exemple DIA (7 signaux) | 🔵 ÉCOLE | C1 | signal |
| D3519 | Exemple AAPL (signaux précoces) | 🔵 ÉCOLE | C1 | signal |
| D3520 | Curve fitting à éviter | 🔵 ÉCOLE | C1 | signal |
| D3521 | Filtre médiane 50 (anti-précoce) | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D3522 | Philosophie : pullbacks / bounces | 🔵 ÉCOLE | C1 | signal |
| D3523 | Reco finale : stop/exit prudent | 🔵 ÉCOLE | C1 | gestion_risque_entree |
| D3524 | Scan Buy Signal | 🔵 ÉCOLE | C1 | signal |
| D3525 | Scan Sell Signal | 🔵 ÉCOLE | C1 | signal |

**Liens Belkhayate :** la stratégie RSI(2) est une stratégie d'ÉCOLE Larry Connors (🔵), SANS aucun lien avec la méthode Belkhayate (⚫). Pertinence projet **modérée et conditionnelle** : c'est une stratégie de mean-reversion court terme aux paramètres quantifiables (SMA 200 filtre directionnel, seuils RSI(2) 5/95, sortie SMA 5, filtre médiane 50) potentiellement cohérente avec les modes Rapide/Scalping TRADEX. MAIS : (1) résultats issus de backtests actions/indices, non transférables d'office aux futures GC/HG/CL/ZW ; (2) la position « pas de stops » (D3517) est INCOMPATIBLE avec les garde-fous risque TRADEX — à écarter au profit de la reco finale stop/exit (D3523) ; (3) à confronter — non substituer — à la logique d'entrée Belkhayate (Pivots/BGC/Direction/Énergie). Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D3514 / D3516 — seuils (RSI(2) 5/95, SMA 200, SMA 5) issus de backtests actions/indices : à re-backtester sur futures GC/HG/CL/ZW et sur les unités de temps TRADEX (Range Bars / 15 min / 15 s) avant tout usage. Validité statistique non établie pour le projet.
- D3517 vs D3523 — CONTRADICTION interne de la source (pas de stops vs stop prudent). Décision projet : conserver stop-loss obligatoire (garde-fous). Tracer cette divergence.
- D3515 — risque de gap sur entrée avant-clôture : pertinent surtout actions ; à ré-évaluer pour futures (24h) où le gap a un profil différent.
- D3521 / D3524 / D3525 — syntaxe de scan propriétaire StockCharts : seule la LOGIQUE est transposable, pas le code. Filtre liquidité (volume) à adapter aux contrats futures.
- Cohérence projet : une stratégie mean-reversion contre-tendance peut entrer en conflit avec une logique d'alignement/cassure Belkhayate — arbitrage humain requis avant toute fusion.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
