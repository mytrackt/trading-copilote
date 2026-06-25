# Extraction StockCharts — Six-Month Cycle MACD
**Source :** `bundles/stockcharts/six_month_cycle_macd.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D3591 → D3610 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/six-month-cycle-macd
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Cycle saisonnier 6 mois directement applicable à ES (confirmation), biais directionnel saisonnier pour GC/CL/HG/ZW qui corrèlent avec l'appétit au risque.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Chart 1 — Six Month Cycle MACD (S&P 500 avec cycle 6 mois, flèches rouge mai / vert novembre) | Six-Month Cycle | D3591 |
| image_02 | Chart 2 — Six Month Cycle MACD (SPX avec MACD, cycles avril 2011 → février 2012) | Strategy | D3595 |
| image_03 | Chart 4 — Six Month Cycle MACD (SPY février 2010 → février 2011) | Tweaks | D3603 |
| image_04 | Chart 14 — Six Month Cycle MACD (DIA weekly MACD, cycles jaune/blanc) | Tweaks | D3606 |

## DÉCISIONS

### D3591 — Cycle saisonnier 6 mois : période haussière novembre–avril, baissière mai–octobre
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md, image_01) : « The six-month cycle defines a bullish cycle running from November to April and a bearish cycle running from May to October. This is where the phrase "sell in May and go away" comes from. »
🔵 **ÉCOLE** : Découvert par Yale Hirsch, fondateur du *Stock Trader's Almanac*.
**TRADEX-AI C4** : Biais saisonnier sur ES : haussier nov–avr, baissier mai–oct. Les commodités GC/CL/HG/ZW corrèlent partiellement avec l'appétit au risque — à intégrer comme filtre saisonnier dans la grille C4.
*Catégorie : saisonnalite*

### D3592 — Performance historique 50 ans : gain moyen Dow < 1% mai–oct vs > 7% nov–avr
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Over the past 50 years, the average gain for the Dow was less than 1% from May to October. In contrast, the average gain was more than 7% from November to April. »
⏳ **VOLATILE** : Statistique sur 50 ans à partir de 1999 (date du livre) — chiffre à mettre à jour avec données récentes.
**TRADEX-AI C4** : Différentiel de performance 7:1 entre la période haussière et baissière sur 50 ans — biais saisonnier statistiquement robuste pour ES, utile comme filtre C4.
*Catégorie : saisonnalite*

### D3593 — Ajustement Harding : cycle haussier démarre le 16 octobre (2 semaines plus tôt)
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Harding started the bullish cycle on October 16th, which is two weeks earlier. Starting the cycle a little earlier makes sense because there have been several October bottoms in the S&P 500. »
🔵 **ÉCOLE** : Sy Harding, *Riding the Bear* (1999).
**TRADEX-AI C4** : Date d'activation du biais haussier = 16 octobre (non 1er novembre) — plusieurs bottoms historiques d'octobre sur ES justifient cette anticipation.
*Catégorie : saisonnalite*

### D3594 — Ajustement Harding : cycle baissier démarre le 20 avril (3 semaines plus tard)
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Harding started the bearish cycle on April 20th, which is almost three weeks later. »
**TRADEX-AI C4** : Date d'activation du biais baissier = 20 avril (non 1er mai) — anticipation de la fin du cycle haussier.
*Catégorie : saisonnalite*

### D3595 — Signal d'achat : MACD haussier au démarrage du cycle haussier (16 oct) OU MACD devient haussier après le 16 oct
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md, image_02) : « A buy signal is triggered when the bullish cycle starts and MACD is on a bullish signal or, alternately, when MACD turns bullish after the bullish cycle starts. »
**TRADEX-AI C1/C4** : Règle d'entrée hybride cycle + momentum : 1) 16 oct + MACD haussier → buy immédiat ; 2) après 16 oct → attendre MACD haussier. Applicable sur ES en C4.
*Catégorie : indicateurs_momentum*

### D3596 — Signal de vente : MACD baissier au démarrage du cycle baissier (20 avr) OU MACD devient baissier après le 20 avr
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « A sell signal is triggered when the bearish cycle starts and MACD is on a bearish signal or when MACD turns bearish after the bearish cycle starts. »
**TRADEX-AI C1/C4** : Règle de sortie : 1) 20 avr + MACD baissier → sell immédiat ; 2) après 20 avr → attendre MACD baissier sur ES.
*Catégorie : indicateurs_momentum*

### D3597 — MACD devient haussier : quand il passe au-dessus de sa signal line OU entre en territoire positif (le premier des deux)
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « MACD turns bullish when it moves above its signal line or into positive territory, whichever comes first. »
**TRADEX-AI C1** : Définition opérationnelle MACD haussier : croisement signal line au-dessus OU passage en territoire positif — utiliser le premier signal qui se produit.
*Catégorie : indicateurs_momentum*

### D3598 — MACD devient baissier : quand il passe sous sa signal line OU entre en territoire négatif (le premier des deux)
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « MACD turns bearish when it moves below its signal line or into negative territory. »
**TRADEX-AI C1** : Définition opérationnelle MACD baissier : croisement signal line en dessous OU passage en territoire négatif — utiliser le premier signal qui se produit.
*Catégorie : indicateurs_momentum*

### D3599 — Récapitulatif signal achat : buy le 16 oct si MACD haussier ; sinon attendre signal MACD haussier
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Buy Signal Recap: 1. Buy on October 16th if MACD is bullish. 2. Wait for bullish MACD signal if MACD is not bullish on October 16th. »
**TRADEX-AI C1/C4** : Règle opérationnelle claire pour timing d'entrée saisonnière sur ES — adaptable comme filtre de timing pour GC/HG/CL/ZW en C4.
*Catégorie : timing*

### D3600 — Récapitulatif signal vente : sell le 20 avr si MACD baissier ; sinon attendre signal MACD baissier
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Sell Signal Recap: 1. Sell on April 20th if MACD is bearish. 2. Wait for a bearish MACD signal if MACD is not bearish on April 20th. »
**TRADEX-AI C1/C4** : Règle opérationnelle pour timing de sortie saisonnière — à utiliser comme filtre de biais directionnel pour TRADEX.
*Catégorie : timing*

### D3601 — MACD améliore significativement la profitabilité du système saisonnier et réduit le risque
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « According to the Stock Trader's Almanac, using MACD greatly increased the profitability of the seasonal system and reduced risk. »
🔵 **ÉCOLE** : *Stock Trader's Almanac* (Yale Hirsch).
**TRADEX-AI C1** : Valeur ajoutée de MACD comme confirmation du timing saisonnier est empiriquement validée sur >50 ans de données — renforce l'intérêt de combiner cycle et momentum.
*Catégorie : indicateurs_momentum*

### D3602 — Anticipation possible : tout avril pour anticiper le signal de vente, tout octobre pour anticiper le signal d'achat
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Knowing that the six-month cycle will turn bearish in May, traders can use the whole month of April to anticipate a sell signal in MACD. Similarly, traders can use the whole month of October to anticipate a buy signal. »
**TRADEX-AI C4** : En avril et octobre, surveiller les signaux MACD de manière proactive — ne pas attendre les dates exactes du 20 avr / 16 oct.
*Catégorie : timing*

### D3603 — Exemple 2010 : signal MACD en avance sur le cycle saisonnier — marché trop suracheté pour attendre octobre
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md, image_03) : « MACD moved above its signal line in early September and broke resistance in mid-September. These signals were well before the bullish six-month cycle started, but traders would have faced an overbought market if they had waited until October. Speculation requires anticipation. »
**TRADEX-AI C1** : Quand les conditions sont claires, anticiper le signal plutôt qu'attendre la date du cycle — la rigidité calendaire peut coûter des points d'entrée.
*Catégorie : timing*

### D3604 — Période saisonnière baissière 2009 (mai–oct) : MACD ne s'est pas retourné à la baisse
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « For example, MACD did not turn down during the bearish cycle period from May 2009 until October 2009. »
**TRADEX-AI C1** : Garde-fou : le cycle saisonnier peut échouer (non-signal) — si MACD ne confirme pas, ne pas forcer le trade de cycle.
*Catégorie : gestion_risque_entree*

### D3605 — Weekly charts + MACD weekly : uniquement les croisements de signal line fonctionnent (centerline trop rare)
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « only the signal line crossovers would work because the centerline crosses are too infrequent. »
**TRADEX-AI C1** : En timeframe hebdomadaire, utiliser uniquement le croisement de la signal line MACD — les croisements de la ligne zéro sont trop rares pour être opérationnels.
*Catégorie : indicateurs_momentum*

### D3606 — MACD weekly sur DIA : bons signaux, mauvais signaux et non-signaux coexistent
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md, image_04) : « There were some good signals, some bad signals, and some non-signals. »
**TRADEX-AI C1** : Le système cycle + MACD weekly n'est pas fiable à 100% — intégrer la gestion du risque (stop loss, R/R ≥ 1:2) pour chaque trade.
*Catégorie : gestion_risque_entree*

### D3607 — Le système génère >100 signaux sur 50 ans ; les gains des meilleurs signaux compensent les pertes des mauvais
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « The overall results are based on over 50 years of trading, which means over 100 signals. Most likely, the gains in some of the great signals made up for the losses in the bad signals to produce a positive result overall. »
**TRADEX-AI C4** : Profitabilité du système basée sur la distribution statistique — fonctionne en expectancy positive sur le long terme, pas sur chaque trade individuel.
*Catégorie : psychologie*

### D3608 — Si 20 avril ou 16 octobre tombe un weekend : avancer au prochain jour de trading
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « Chartists can move ahead to the next trading date should April 20th or October 16th fall on a weekend. »
**TRADEX-AI C4** : Règle pratique opérationnelle pour l'implémentation du calendrier saisonnier dans TRADEX.
*Catégorie : timing*

### D3609 — Article est un point de départ pour le développement d'un système de trading — augmenter avec le style et préférences personnelles
🟢 **FAIT VÉRIFIÉ** (Source : six_month_cycle_macd.md) : « this article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments. »
**TRADEX-AI C1** : Le cycle saisonnier est un filtre de biais directionnel — à combiner avec les indicateurs Belkhayate (BGC, Direction, Énergie) pour validation des signaux TRADEX.
*Catégorie : configuration*

### D3610 — Combinaison cycle 6 mois + MACD introduite par Sy Harding dans *Riding the Bear* (1999)
🔵 **ÉCOLE** (Source : six_month_cycle_macd.md) : « Sy Harding introduced his seasonal MACD strategy in his 1999 book, Riding the Bear. The strategy combines the six-month seasonal cycle from the Stock Trader's Almanac and momentum using MACD, which was developed by Gerald Appel. »
**TRADEX-AI C4** : Traçabilité académique de la stratégie : Hirsch (cycle) + Appel (MACD) + Harding (combinaison) — cadre éprouvé depuis 1999.
*Catégorie : indicateurs_tendance*
