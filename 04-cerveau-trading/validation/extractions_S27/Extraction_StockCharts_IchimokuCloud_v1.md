# Extraction StockCharts — Ichimoku Cloud

**Source :** `bundles/stockcharts/ichimoku_cloud.md` (HTTP 200 · ~11 200 car.) + 11 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D2151 → D2170 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/ichimoku-cloud
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🔵 **PERTINENCE FUTURES : OUI (C1/C3) — ÉCOLE Ichimoku** — overlay de tendance/support-résistance directement transposable aux futures (GC/HG/CL/ZW), périodes à recalibrer sur le timeframe TRADEX (15min / Range Bar). Méthode externe (école Ichimoku / Hosoda), NON Belkhayate → tag 🔵 ÉCOLE. Belkhayate NON CONCERNÉ (Ichimoku n'est pas un outil de la méthode ⚫).

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Décision |
|-------|-------|---------|----------|
| image_01.png | What Is an Ichimoku Cloud? | What Is an Ichimoku Cloud? [SECTION-FALLBACK] | D2151 |
| image_02.png | Comparing Ichimoku Cloud plots | Interpreting Ichimoku Clouds | D2158 |
| image_03.png | Ichimoku Cloud in an Uptrend | Identifying Trends | D2161 |
| image_04.png | Ichimoku Cloud in a Downtrend | Identifying Trends | D2162 |
| image_05.png | Conversion-Base Line Crossover Signal in an Uptrend | Conversion-Base Line Crossovers | D2164 |
| image_06.png | Conversion-Base Line Crossover Signal in a Downtrend | Conversion-Base Line Crossovers | D2164 |
| image_07.png | Price-Base Line Crossover Signal in an Uptrend | Price-Base Line Crossovers | D2165 |
| image_08.png | Price-Base Line Crossover Signal in a Downtrend | Price-Base Line Crossovers | D2165 |
| image_09.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | D2169 |
| image_10.png | SharpCharts settings for the Ichimoku Cloud overlay | Using with SharpCharts | D2169 |
| image_11.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | D2169 |

## DÉCISIONS

### D2151 — Nature multi-fonction de l'Ichimoku Cloud
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_01) : « The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a multi-functional tool that provides various insights into market dynamics. It helps in identifying levels of support and resistance, figuring out the direction of the market trend, measuring momentum, and producing trading signals. Ichimoku Kinko Hyo translates into "one look equilibrium chart." »
**TRADEX-AI C1/C3** : Ichimoku = système complet support/résistance + direction de tendance + momentum + signaux en un coup d'œil. Brique de tendance (C1) avec composante S/R structurelle (C3).
*Catégorie : indicateurs_tendance*

---

### D2152 — Origine et lisibilité de l'indicateur
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « The indicator was developed by journalist Goichi Hosoda and published in his 1969 book. Even though the Ichimoku Cloud may seem complicated (...) it's a rather straightforward indicator; the concepts are easy to understand and the signals are well-defined. »
**TRADEX-AI C1** : provenance école japonaise (Hosoda, 1969), signaux « bien définis » donc codables de façon déterministe. Note documentaire d'attribution.
*Catégorie : configuration*

---

### D2153 — Cinq tracés basés sur la moyenne haut-bas
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « Four of the five plots within the Ichimoku Cloud are based on the average of the high and low over a given period of time. (...) The Ichimoku Cloud consists of five plots. »
**TRADEX-AI C1** : 4 des 5 tracés = milieu du range haut-bas (≠ moyenne mobile de clôtures). Architecture de calcul à reproduire exactement (midpoint, pas SMA).
*Catégorie : indicateurs_tendance*

---

### D2154 — Conversion Line (Tenkan-sen) = (9h + 9b)/2
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : `Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2`. Défaut 9 périodes, ajustable ; sur daily = milieu du range 9 jours (~2 semaines).
**TRADEX-AI C1** : formule littérale ligne de conversion. Période 9 = défaut (exemple daily), à recalibrer sur timeframe TRADEX.
*Catégorie : indicateurs_tendance*

---

### D2155 — Base Line (Kijun-sen) = (26h + 26b)/2
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : `Kijun-sen (Base Line): (26-period high + 26-period low)/2`. Défaut 26 périodes, ajustable ; sur daily = milieu du range 26 jours (~1 mois).
**TRADEX-AI C1** : formule littérale ligne de base. Période 26 = défaut, à recalibrer.
*Catégorie : indicateurs_tendance*

---

### D2156 — Leading Span A/B et projection +26 périodes
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : `Senkou Span A: (Conversion Line + Base Line)/2` (frontière rapide, tracée 26 périodes dans le futur) ; `Senkou Span B: (52-period high + 52-period low)/2` (frontière lente, tracée 26 périodes dans le futur). Lagging Span (Chikou) = clôture tracée 26 jours dans le passé.
**TRADEX-AI C1/C3** : les deux frontières du nuage sont **décalées +26 dans le futur** → S/R projetée. Span B sur 52 périodes. Détail critique : le décalage temporel doit être codé (le nuage anticipe la S/R future).
*Catégorie : indicateurs_tendance*

---

### D2157 — Formation et couleur du nuage (Kumo)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « the "clouds" (...) are formed when the faster Leading Span A plot crosses the slower Leading Span B. (...) If the faster Leading Span A line is on top, that is bullish and the area (...) is shaded in green. If the slower Leading Span B is on top, that is bearish and (...) shaded in red. »
**TRADEX-AI C1** : règle de couleur du nuage — Span A > Span B = vert (haussier) ; Span A < Span B = rouge (baissier). Codable comme état binaire de biais de tendance.
*Catégorie : indicateurs_tendance*

---

### D2158 — Les 5 tracés s'utilisent comme des moyennes mobiles (9/26 = MACD)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_02) : « The five plots (...) can be used very much like moving averages. (...) The Conversion Line (blue) is the fastest (...) The Base Line (red) trails the faster Conversion Line (...). Incidentally, notice that 9 and 26 are the same periods used to calculate the MACD. »
**TRADEX-AI C1** : analogie pédagogique — Conversion/Base se comportent comme MM rapide/lente (9 et 26 = périodes du MACD). Utile pour relier Ichimoku à des features déjà connues du moteur.
*Catégorie : indicateurs_tendance*

---

### D2159 — Identifier la tendance : prix vs nuage
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « the trend is up when prices are above the cloud, down when prices are below the cloud, and flat when prices are in the cloud. This is a very straightforward signal to spot on a chart. »
**TRADEX-AI C1** : règle de tendance n°1 — prix au-dessus du nuage = up, sous = down, dans = plat. Filtre de tendance déterministe et codable directement.
*Catégorie : indicateurs_tendance*

---

### D2160 — Renforcement de tendance par couleur + S/R future
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « the uptrend is strengthened when the Leading Span A (...) rises above the Leading Span B (...) (green cloud). Conversely, a downtrend is reinforced when (...) Span A falls below Span B (red cloud). Because the cloud is shifted forward 26 days, it also provides a glimpse of future support or resistance. »
**TRADEX-AI C1/C3** : règle de tendance n°2 — couleur du nuage = confirmation de force ; nuage projeté +26 = S/R anticipée. Double lecture tendance + S/R.
*Catégorie : indicateurs_tendance*

---

### D2161 — Le nuage comme support en tendance haussière
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_03) : exemple IBM — uptrend tant que le prix trade au-dessus du nuage ; le nuage a offert un support ; « Remember, the entire cloud is shifted forward 26 days. This means it is plotted 26 days ahead of the last price point to indicate future support or resistance. »
**TRADEX-AI C3** : en uptrend, le nuage agit comme zone de support dynamique (projetée). Confluence S/R exploitable pour les entrées sur pullback.
*Catégorie : structure_marche*

---

### D2162 — Changement de tendance : cassure + changement de couleur (downtrend)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_04) : exemple Boeing — « The trend changed when Boeing broke below cloud support (...). The cloud changed from green to red when the Leading Span A moved below the Leading Span B (...). The cloud break represented the first trend change signal, while the color change represented the second trend change signal. (...) the cloud then acted as resistance. »
**TRADEX-AI C1/C3** : deux signaux séquentiels de retournement — (1) cassure du nuage, (2) changement de couleur. Puis le nuage devient résistance. Logique d'inversion codable en 2 étapes.
*Catégorie : signal*

---

### D2163 — Trader dans le sens de la tendance majeure
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « bullish signals are reinforced when prices are above the cloud, and the cloud is green. Bearish signals are reinforced when prices are below the cloud, and the cloud is red. (...) Signals counter to the existing trend are deemed weaker. »
**TRADEX-AI C1** : garde-fou directionnel — ne prendre les signaux que dans le sens du biais nuage (prix+couleur). Signaux contra-tendance = plus faibles → cohérent avec la logique de score multi-cercles.
*Catégorie : signal*

---

### D2164 — Signal Conversion/Base Line Crossover
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_05, image_06) : « During an uptrend, a bullish signal is triggered when the Conversion Line crosses above the Base Line. Similarly, the Conversion Line crossing below the Base Line during a downtrend is a bearish signal. » Exemples KMB (haussier) et AT&T (baissier).
**TRADEX-AI C1** : signal de momentum — croisement Conversion×Base, valide uniquement dans le sens de la tendance nuage. Équivalent fonctionnel d'un croisement MM rapide/lente.
*Catégorie : signal*

---

### D2165 — Signal Price/Base Line Crossover
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_07, image_08) : « During an uptrend, a bullish signal is triggered when price crosses above the Base Line. Similarly, price crossing below the Base Line during a downtrend is a bearish signal. » Exemples Disney (haussier, pullback oversold) et DR Horton (baissier, bounce overbought).
**TRADEX-AI C1** : signal plus fréquent que le croisement Conversion/Base — prix franchit la Base Line après un pullback/bounce dans le sens de la tendance. Plus de signaux que la version classique.
*Catégorie : signal*

---

### D2166 — Récapitulatif des 4 signaux haussiers
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : Bullish — (1) Price moves above cloud (trend), (2) Cloud turns from red to green (ebb-flow), (3) Price moves above the Base Line (momentum), (4) Conversion Line moves above Base Line (momentum).
**TRADEX-AI C1** : grille des 4 conditions haussières (2 tendance + 2 momentum). Directement transposable en checklist de scoring.
*Catégorie : signal*

---

### D2167 — Récapitulatif des 4 signaux baissiers
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : Bearish — (1) Price moves below cloud (trend), (2) Cloud turns from green to red (ebb-flow), (3) Price moves below Base Line (momentum), (4) Conversion Line moves below Base Line (momentum).
**TRADEX-AI C1** : grille symétrique des 4 conditions baissières. Checklist de scoring miroir.
*Catégorie : signal*

---

### D2168 — Synthèse d'usage + confluence avec d'autres indicateurs
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : « Chartists can first determine the trend by using the cloud. Once the trend is established, appropriate signals can be determined using the price plot, Conversion Line, and Base Line. (...) The Ichimoku Cloud can also be used in conjunction with other indicators. Traders can identify the trend using the cloud and then use classic momentum oscillators to identify overbought or oversold conditions. »
**TRADEX-AI C1** : garde-fou de confluence — Ichimoku définit la tendance, puis combiner avec des oscillateurs de momentum pour OB/OS. Jamais signal isolé ; cohérent score multi-cercles.
*Catégorie : signal*

---

### D2169 — Paramètres par défaut et affichage (SharpCharts / ACP)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md, image_09, image_10, image_11) : « Default settings are 9 for the Conversion Line, 26 for the Base Line and 52 for the Leading Span B. (...) The number for the Base Line (26) is also used to move the cloud forward (26 days). These numbers can be adjusted (...). » Choix « Ichimoku Cloud » (nuage seul) ou « Ichimoku Cloud (Full) » (toutes les lignes).
**TRADEX-AI C1** : paramètres défaut 9/26/52 + décalage 26. Implication config — coder la valeur de décalage = celle de la Base Line ; périodes ajustables, à recalibrer pour TRADEX.
*Catégorie : configuration*

---

### D2170 — Scans Ichimoku uptrend/downtrend (Span A/B + Base Line)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud.md) : scan uptrend — `Close > Span B(9,26,52)` ET `Span A > Span B` ET `Close x Base Line(9,26,52)` (breakout). Scan downtrend — `Close < Span A(9,26,52)` ET `Span A < Span B` ET `Base Line(9,26,52) x Close`. Filtres : SMA(60,Volume) > 100000, SMA(60,Close) > 10.
**TRADEX-AI C1** : logique de screening déterministe — biais (Close vs Span B + Span A/B) + déclencheur (croisement Close/Base Line). Périodes/filtres = exemples actions US daily, NE PAS coder tels quels ; recalibrer sur les futures.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2151 | Nature multi-fonction Ichimoku | 🔵 | C1/C3 | indicateurs_tendance |
| D2152 | Origine Hosoda 1969 | 🔵 | C1 | configuration |
| D2153 | 5 tracés = midpoint haut-bas | 🔵 | C1 | indicateurs_tendance |
| D2154 | Conversion Line (9) | 🔵 | C1 | indicateurs_tendance |
| D2155 | Base Line (26) | 🔵 | C1 | indicateurs_tendance |
| D2156 | Span A/B + décalage +26 | 🔵 | C1/C3 | indicateurs_tendance |
| D2157 | Couleur du nuage (Kumo) | 🔵 | C1 | indicateurs_tendance |
| D2158 | Tracés ~ MM (9/26 = MACD) | 🔵 | C1 | indicateurs_tendance |
| D2159 | Tendance : prix vs nuage | 🔵 | C1 | indicateurs_tendance |
| D2160 | Renforcement couleur + S/R future | 🔵 | C1/C3 | indicateurs_tendance |
| D2161 | Nuage = support en uptrend | 🔵 | C3 | structure_marche |
| D2162 | Retournement : cassure + couleur | 🔵 | C1/C3 | signal |
| D2163 | Trader dans le sens de la tendance | 🔵 | C1 | signal |
| D2164 | Croisement Conversion/Base | 🔵 | C1 | signal |
| D2165 | Croisement Price/Base | 🔵 | C1 | signal |
| D2166 | 4 signaux haussiers | 🔵 | C1 | signal |
| D2167 | 4 signaux baissiers | 🔵 | C1 | signal |
| D2168 | Synthèse + confluence oscillateurs | 🔵 | C1 | signal |
| D2169 | Paramètres défaut 9/26/52 | 🔵 | C1 | configuration |
| D2170 | Scans uptrend/downtrend | 🔵 | C1 | signal |

| Élément | Valeur |
|---------|--------|
| Décisions | D2151 → D2170 (20) |
| Images certifiées | 11/11 |
| Cercles | C1 (tendance/signal, dominant) + C3 (S/R nuage projeté) |
| Catégories | indicateurs_tendance · structure_marche · signal · configuration |
| Actif applicable | GC/HG/CL/ZW (TRADING) + ES — overlay transposable, périodes 9/26/52 à recalibrer |
| Belkhayate | NON CONCERNÉ (Ichimoku = école externe, pas un outil Belkhayate ⚫) |
| Pertinence futures | OUI (C1/C3) — école Ichimoku, brique tendance + S/R projetée |
| Cas « à vérifier » | (1) Tag 🔵 ÉCOLE (Ichimoku/Hosoda), méthode externe NON Belkhayate. (2) Périodes 9/26/52 et décalage 26 = défauts daily actions ; NE PAS coder tels quels — recalibrer sur timeframe TRADEX (15min/Range Bar). (3) Scans (D2170) = exemples actions US (filtres volume/prix actions), inapplicables tels quels aux futures. (4) Le décalage +26 dans le futur des Span A/B est un point d'implémentation critique (S/R anticipée) à ne pas oublier. |

**Liens Belkhayate :** Aucun lien direct — l'Ichimoku Cloud n'est PAS un indicateur de la méthode Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
