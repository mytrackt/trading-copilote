# Extraction StockCharts — CVR3 VIX Market Timing
**Source :** `bundles/stockcharts/cvr3_vix_market_timing.md` (HTTP 200 · ~6 400 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D1431 → D1444 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/cvr3-vix-market-timing
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - CVR3 VIX Market Timing | VIX Defined | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 - CVR3 VIX Market Timing | Buy Example | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 - CVR3 VIX Market Timing | Sell Example | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 - CVR3 VIX Market Timing | Adjusting | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 5 - CVR3 VIX Market Timing | Adjusting | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1431 — Nature de la stratégie CVR3
🔵 **ÉCOLE (Connors & Landry)** (Source : cvr3_vix_market_timing.md) : CVR3 est une stratégie de trading court-terme utilisant le Cboe Volatility Index ($VIX) pour timer le S&P 500. Développée par Larry Connors et Dave Landry, elle cherche des lectures VIX surextendues signalant une peur ou une avidité excessive. La peur excessive génère des signaux d'achat (stratégie de retour à la moyenne) ; l'avidité excessive génère des signaux de vente.
**TRADEX-AI C5** : Stratégie de timing fondée sur le sentiment (VIX) ; candidate comme couche C5 (sentiment) pour moduler le biais des actifs trading — jamais comme déclencheur d'ordre. NB : indice/actif source = S&P 500, hors actifs tradables GC/HG/CL/ZW.
*Catégorie : timing*

---

### D1432 — Définition du VIX
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md, image_01) : Le Cboe Volatility Index ($VIX) mesure la volatilité implicite d'un panier d'options put et call sur le S&P 500. Spécifiquement, le VIX mesure la volatilité attendue à 30 jours pour le S&P 500. La volatilité est une mesure du risque : une volatilité relativement élevée reflète un risque plus élevé sur le marché actions ; une volatilité faible suggère un risque faible.
**TRADEX-AI C5** : Définition canonique du VIX comme proxy de risque/sentiment ; cohérent avec l'usage projet de VX (VIX) comme actif de confirmation.
*Catégorie : timing*

---

### D1433 — VIX comme indice de la peur
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Le VIX est aussi appelé « indice de la peur ». Volatilité et VIX explosent quand la peur frappe le marché — surge de volatilité implicite sur les puts, donc surge des prix des puts. La complaisance est l'opposé de la peur : le VIX baisse quand la peur s'estompe, et les traders sont jugés complaisants quand le VIX atteint des niveaux excessivement bas.
**TRADEX-AI C5** : Axe sémantique peur↔complaisance directement exploitable comme feature de sentiment ; les extrêmes (haut=peur, bas=complaisance) sont les zones d'intérêt.
*Catégorie : timing*

---

### D1434 — Règle 1 du signal d'achat
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Signal d'achat, règle 1 — le plus bas journalier du VIX est au-dessus de sa moyenne mobile à 10 jours. Cela signifie que la barre/chandelier entier doit être au-dessus de la MM10.
**TRADEX-AI C5** : Condition booléenne déterministe sur le VIX (low > MM10) ; implémentable telle quelle comme première brique du signal d'achat composite.
*Catégorie : signal*

---

### D1435 — Règle 2 du signal d'achat (PPO)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Signal d'achat, règle 2 — la clôture journalière est au moins 10 % au-dessus de sa MM10. Dans SharpCharts, le Percent Price Oscillator (PPO) sert à définir cette règle (avec une EMA10). PPO(1,10,1) montre l'écart pourcentage entre l'EMA-1-jour (close) et l'EMA-10-jours ; un PPO ≥ 10 indique que la clôture est au moins 10 % au-dessus de l'EMA10.
**TRADEX-AI C5** : Seuil quantifié (PPO ≥ +10) ; formule de normalisation de l'écart à la MM, réutilisable comme détecteur de surextension VIX.
*Catégorie : signal*

---

### D1436 — Règle 3 du signal d'achat (chandelier)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Signal d'achat, règle 3 — la clôture est en dessous de l'ouverture (le chandelier doit être noir/plein). Un chandelier plein = clôture sous l'ouverture ; un chandelier blanc/creux = clôture au-dessus de l'ouverture.
**TRADEX-AI C5** : Condition de couleur du chandelier VIX (close < open) ; troisième brique booléenne du signal d'achat composite (3 règles ET).
*Catégorie : signal*

---

### D1437 — Convergence des règles et fenêtre (buy example)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md, image_02) : Exemple avec VIX (fenêtre haute), PPO(1,10,1) (fenêtre médiane), S&P 500 (fenêtre basse). Obtenir les trois règles alignées le même jour n'arrive pas aussi souvent qu'on le penserait. Quatre signaux d'achat de fin juillet à fin septembre 2011. Les chartistes peuvent considérer des « fenêtres » de règles en cherchant le déclenchement des 3 règles dans un délai de 3 jours, ce qui augmenterait le nombre de signaux.
**TRADEX-AI C5** : Notion de « fenêtre de 3 jours » assouplissant l'alignement strict ; choix de conception (alignement strict vs fenêtré) impactant la fréquence de signaux.
*Catégorie : configuration*

---

### D1438 — Règle 1 du signal de vente
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Signal de vente, règle 1 — le plus haut du VIX est en dessous de sa MM10 (la barre/chandelier entier doit être sous la MM10).
**TRADEX-AI C5** : Miroir baissier de la règle d'achat (high < MM10) ; brique booléenne du signal de vente composite.
*Catégorie : signal*

---

### D1439 — Règle 2 du signal de vente (PPO négatif)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Signal de vente, règle 2 — la clôture journalière est au moins 10 % en dessous de la MM10. Le PPO(1,10,1) peut le mesurer : une valeur de -10 signifie que la clôture est 10 % sous l'EMA10.
**TRADEX-AI C5** : Seuil symétrique (PPO ≤ -10) ; détecteur de complaisance/surextension basse du VIX.
*Catégorie : signal*

---

### D1440 — Règle 3 du signal de vente (chandelier)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md, image_03) : Signal de vente, règle 3 — la clôture est au-dessus de l'ouverture (chandelier blanc/creux). Exemple : un seul signal de vente sur la seconde moitié 2011 ; le PPO(1,10,1) est passé sous -10 plusieurs fois et il y avait quelques chandeliers blancs sous la MM10, mais les 3 règles ne se sont alignées qu'une fois.
**TRADEX-AI C5** : Troisième brique du signal de vente (close > open) ; illustre la rareté de l'alignement strict des 3 conditions.
*Catégorie : signal*

---

### D1441 — Gestion des stop-loss
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : Connors et Landry suggèrent des stops relativement serrés. Sur positions longues, le stop est déclenché quand le VIX passe sous la MM10 de la veille (en intraday). Les positions courtes sont fermées quand le VIX passe au-dessus de la MM10 de la veille. Alternativement, ils suggèrent de sortir en 2 à 4 jours — système très court-terme. On peut aussi appliquer un stop directement au S&P 500 via le Parabolic SAR.
**TRADEX-AI gestion_risque_entree** : Logique de sortie déterministe (stop sur croisement VIX/MM10 veille ou sortie temporelle 2-4 j) ; transposable comme règle de gestion mais sur indice S&P, pas sur GC/HG/CL/ZW directement.
*Catégorie : gestion_risque_entree*

---

### D1442 — Adaptabilité de la stratégie
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md, image_04) : L'article ne promeut pas une stratégie clé-en-main mais montre une stratégie d'un professionnel à adapter. CVR3 utilise exclusivement le VIX, ce qui en fait un excellent complément aux autres stratégies sur les indices majeurs. On peut allonger les look-back des moyennes et du PPO pour la rendre plus moyen-terme, ou l'utiliser sur graphiques hebdomadaires.
**TRADEX-AI C5** : Avertissement explicite : stratégie à calibrer, complémentaire et non autonome ; argument pour traiter CVR3 comme une feature de sentiment parmi d'autres, pas comme un système de décision isolé.
*Catégorie : configuration*

---

### D1443 — Indices de volatilité par actif (extension)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md, image_05) : Le CBOE calcule des indices de volatilité pour plusieurs ETF/indices : Gold SPDR, US Oil Fund, Euro Currency Trust, Dow Industrials, Nasdaq 100. Les chartistes peuvent utiliser ces indices pour développer des stratégies sur le Dow, le Nasdaq 100, le pétrole, l'or et l'euro.
**TRADEX-AI C5** : Existence d'indices de volatilité dédiés Or (GVZ) et Pétrole (OVX) — piste directement pertinente pour appliquer une logique CVR3 aux actifs trading GC et CL via leur propre VIX sectoriel. ⏳ VOLATILE : disponibilité/feed de ces indices à confirmer côté data NT8/ATAS.
*Catégorie : timing*

---

### D1444 — Synthèse méthodologique (Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : cvr3_vix_market_timing.md) : CVR3 est une stratégie classique de retour à la moyenne tirant parti des conditions surextendues ; le VIX mesure la peur et la complaisance excessives ; une fois surextendu, un retour à la moyenne est attendu. Comme le VIX est le seul indicateur, les chartistes doivent aussi analyser le price action et les indicateurs du S&P 500 : les signaux d'achat CVR3 doivent être appariés à des indications haussières du S&P, et inversement pour les ventes.
**TRADEX-AI C5** : Exigence de confluence (signal VIX + confirmation price action du sous-jacent) ; cohérent avec l'architecture projet où le sentiment (C5) module mais ne décide jamais seul.
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1431 → D1444 (14 décisions) |
| Images certifiées | 5/5 |
| Catégories couvertes | timing · signal · configuration · gestion_risque_entree |
| Cercle dominant | C5 (sentiment / VIX) |
| Lien Belkhayate | NON CONCERNÉ (stratégie Connors & Landry, hors méthode Belkhayate) |
| Cas à vérifier | D1443 ⏳ VOLATILE — disponibilité des indices de volatilité Or (GVZ) / Pétrole (OVX) à confirmer côté feed ; stratégie centrée S&P 500, applicabilité directe à GC/HG/CL/ZW à valider (transposition VIX→GVZ/OVX) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs trading concernés : GC · HG · CL · ZW uniquement (VIX/VX = actif de confirmation C5). Stratégie issue de Connors & Landry, aucun rapport affirmé avec la méthode Belkhayate.
