# Extraction StockCharts — Market Indicator Dictionary

**Source :** `bundles/stockcharts/market_indicator_dictionary.md` (HTTP 200 · ~9 500 car.) + 0 image certifiée
**Méthode images :** double ancrage v3 · 0/0 certifiées (manifest : .md=0 figures vs HTML=0 images → aucune image dans la page)
**Décisions :** D2531 → D2543 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/introduction-to-market-indicators/market-indicator-dictionary
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (page sans figure — glossaire de symboles uniquement).

## DÉCISIONS

> Page = glossaire dense de symboles de breadth (NYSE/Nasdaq/Amex/Toronto/TSX Venture). Synthèse par FAMILLES d'indicateurs (max 14), pas symbole-par-symbole. Pertinence futures limitée : tous ces indices mesurent la santé d'un panier d'actions (NYSE/Nasdaq), donc usage TRADEX = sentiment/confirmation marché actions via ES (C5), jamais ordre sur GC/HG/CL/ZW.

### D2531 — Définition « Market Indicator » (≠ indicateur technique)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : « Market Indicators (as opposed to "technical" indicators) are index symbols that contain calculated values which measure the health of a specified group of stocks. » Exemple donné : $NYHGH = totaux quotidiens d'actions NYSE ayant établi un nouveau plus-haut 52 semaines.
**TRADEX-AI C5** : un indicateur de marché mesure la santé d'un GROUPE d'actions (panier indiciel), pas un titre isolé — à traiter comme contexte sentiment/confirmation, non comme signal d'entrée sur futures matières premières.
*Catégorie : structure_marche*

---

### D2532 — Famille « Stocks Above Moving Average » (50/150/200 jours)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : la page liste, pour NYSE/Nasdaq/Toronto, les symboles de comptage absolu ($NYA50, $NYA150, $NYA200) et de pourcentage ($NYA50R, $NYA150R, $NYA200R) = « Stocks / Percent of Stocks Above 50/150/200-Day Moving Average », fréquence EOD, historique depuis 2002.
**TRADEX-AI C5** : breadth de tendance (part des actions au-dessus de leur MA) = mesure de largeur de marché actions ; pertinence futures indirecte via confirmation ES.
*Catégorie : indicateurs_tendance*

---

### D2533 — Famille « Advance-Decline Issues » (avances/déclins)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : symboles $NYAD (Advance-Decline Issues), $NYADV (Issues Advancing), $NYDEC (Issues Declining), $NYADU (Issues Unchanged) — fréquence Intraday, historique 1992.
**TRADEX-AI C5** : la dynamique avances-déclins est la brique de base du breadth (alimente McClellan & Summation) ; signal de participation, non transposable directement aux futures.
*Catégorie : structure_marche*

---

### D2534 — Famille « Advance-Decline Volume » (volume avances/déclins)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : symboles $NYUD (Advance-Decline Volume), $NYUPV (Volume Advancing), $NYDNV (Volume Declining), $NYUDU (Volume Unchanged) — Intraday ; certains à reset quotidien (Daily Reset = Yes pour $NYDNV, $NYUPV).
**TRADEX-AI C5** : breadth pondéré par le volume (où va le flux) ; alimente le TRIN / Arms Index. Contexte sentiment marché actions.
*Catégorie : structure_marche*

---

### D2535 — Famille « New Highs / New Lows » (52 semaines)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $NYHGH (New 52-Week Highs), $NYLOW (New 52-Week Lows), $NYHL (New Highs-New Lows), $NYHLR (New High/Low Ratio) — Intraday/EOD, historique 1992.
**TRADEX-AI C5** : indicateur de leadership/épuisement du marché actions (expansion ou contraction des extrêmes 52 sem.) ; usage confirmation de régime.
*Catégorie : structure_marche*

---

### D2536 — « 10-Day MA of Record High Percent Index »
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $NYHILO (et $NAHILO, $AMHILO, $TSXHILO) = « 10-Day MA of Record High Percent Index », fréquence EOD.
**TRADEX-AI C5** : version lissée (MA 10 j) du Record High Percent ; réduit le bruit des extrêmes quotidiens pour le suivi de tendance breadth.
*Catégorie : indicateurs_tendance*

---

### D2537 — McClellan Oscillator (Ratio-Adjusted vs Traditional)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $NYMO = « McClellan Oscillator (Ratio-Adjusted) », $NYMOT = « McClellan Oscillator (Traditional) » — EOD, historique depuis Jun 1998 ; équivalents Nasdaq $NAMO / $NAMOT.
**TRADEX-AI C5** : deux variantes du McClellan ; StockCharts privilégie la version ratio-ajustée (comparable dans le temps) — détaillée dans l'extraction dédiée mcclellan_oscillator.
*Catégorie : signal*

---

### D2538 — McClellan Summation Index (Ratio-Adjusted vs Traditional)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $NYSI = « Summation Index (Ratio-Adjusted) », $NYSIT = « Summation Index (Traditional) » — EOD, historique Jun 1998 ; équivalents Nasdaq $NASI / $NASIT.
**TRADEX-AI C5** : cumul du McClellan Oscillator → vision moyen/long terme du breadth ; détaillé dans l'extraction dédiée mcclellan_summation_index.
*Catégorie : signal*

---

### D2539 — $TICK (Tick) et $TRIN / Arms Index
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $TICK = « Tick » (Intraday, depuis 1999) ; $TRIN = « Short-Term Trading Arms Index » (Intraday, 1992) ; équivalents Nasdaq $TICKQ / $TRINQ.
**TRADEX-AI C5** : indicateurs de breadth intraday court terme (pression acheteuse/vendeuse instantanée et ratio Arms) ; outils de timing sentiment marché actions.
*Catégorie : timing*

---

### D2540 — Familles de volume total et symboles actifs
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : $NYTOT (Total Active Symbols), $NYTV (Primary Market Total Volume) — Intraday, 1992 ; équivalents par place ($NATOT/$NATV, $AMTOT/$AMTV, $TOTOT/$TOTV…).
**TRADEX-AI C5** : compteurs de participation (nombre de titres actifs, volume total) servant de dénominateur aux ratios de breadth ; usage contextuel.
*Catégorie : structure_marche*

---

### D2541 — Couverture multi-places (NYSE, Nasdaq, Amex, Toronto, TSX Venture)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : la même grille d'indicateurs (above-MA, AD issues, AD volume, new highs/lows, McClellan…) est répliquée par préfixe : $NY* (NYSE), $NA* (Nasdaq), $AM* (Amex/NYSE Mkt), $TO*/$TSX* (Toronto), $CD* (TSX Venture).
**TRADEX-AI C5** : les indicateurs de marché sont segmentés par place boursière ; pour TRADEX, seuls NYSE/Nasdaq (proxy ES/marché US) ont une pertinence de confirmation — Canada hors périmètre.
*Catégorie : structure_marche*

---

### D2542 — Attribut « Daily Reset » des indicateurs intraday
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : la colonne « Daily Reset » distingue les symboles cumulés sur la journée puis remis à zéro (ex. $NYDNV, $NYUPV = Yes) des symboles non réinitialisés (la majorité = No).
**TRADEX-AI C5** : métadonnée technique de lecture des données breadth — un indicateur « reset = Yes » ne doit pas être lu comme une série continue intraday. Garde-fou d'interprétation si jamais intégré.
*Catégorie : structure_marche*

---

### D2543 — Fréquence et profondeur d'historique (EOD vs Intraday, depuis 1992/1998/2002)
🟢 **FAIT VÉRIFIÉ** (Source : market_indicator_dictionary.md) : chaque symbole porte une fréquence (EOD ou Intraday) et un début d'historique (AD issues 1992 ; McClellan/Summation Jun 1998 ; above-MA 2002).
**TRADEX-AI C5** : métadonnées de disponibilité ; les indicateurs de breadth les plus longs (AD depuis 1992) permettent l'étude de régimes historiques, les McClellan/Summation seulement depuis 1998.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| # | Famille / Décision | Symboles repères | Cercle | Catégorie | Pertinence futures |
|---|--------------------|------------------|--------|-----------|--------------------|
| D2531 | Définition Market Indicator | — | C5 | structure_marche | Contexte uniquement |
| D2532 | Stocks Above MA 50/150/200 | $NYA50/150/200(R) | C5 | indicateurs_tendance | Indirecte (via ES) |
| D2533 | Advance-Decline Issues | $NYAD/$NYADV/$NYDEC | C5 | structure_marche | Indirecte |
| D2534 | Advance-Decline Volume | $NYUD/$NYUPV/$NYDNV | C5 | structure_marche | Indirecte |
| D2535 | New Highs / New Lows | $NYHGH/$NYLOW/$NYHL | C5 | structure_marche | Indirecte |
| D2536 | 10-Day MA Record High % | $NYHILO | C5 | indicateurs_tendance | Indirecte |
| D2537 | McClellan Oscillator | $NYMO/$NYMOT | C5 | signal | Indirecte |
| D2538 | McClellan Summation Index | $NYSI/$NYSIT | C5 | signal | Indirecte |
| D2539 | $TICK + $TRIN/Arms | $TICK/$TRIN | C5 | timing | Indirecte |
| D2540 | Volume total / actifs | $NYTOT/$NYTV | C5 | structure_marche | Contexte |
| D2541 | Couverture multi-places | $NY/$NA/$AM/$TO/$CD | C5 | structure_marche | NYSE/Nasdaq seuls |
| D2542 | Attribut Daily Reset | — | C5 | structure_marche | Garde-fou lecture |
| D2543 | Fréquence / historique | — | C5 | structure_marche | Métadonnée |

**Note de portée :** glossaire de breadth ACTIONS (NYSE/Nasdaq). Pour TRADEX-AI (futures GC/HG/CL/ZW), valeur = sentiment/confirmation marché actions US via ES (C5) ; aucun lien direct avec les actifs tradables ni avec la méthode Belkhayate (⚫ NON CONCERNÉ). 13 décisions, 0 image.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
