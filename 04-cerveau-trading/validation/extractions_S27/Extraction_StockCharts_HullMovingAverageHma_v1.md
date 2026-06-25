# Extraction StockCharts — Hull Moving Average (HMA)

**Source :** `bundles/stockcharts/hull_moving_average_hma.md` (HTTP 200 · ~5 800 car.) + 1 image certifiée (1 décorative ignorée)
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 1/2 certifiée (1 décorative IGNORÉE)
**Décisions :** D2111 → D2127 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/hull-moving-average-hma
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🟢 **PERTINENCE FUTURES : OUI (C1)** — la Hull Moving Average est un overlay de tendance directement transposable aux actifs tradables (GC/HG/CL/ZW) comme feature de tendance/retournement, sous réserve de recalibrer la période sur le timeframe TRADEX (15min / Range Bar). Belkhayate NON CONCERNÉ (la HMA n'est pas un outil de la méthode).

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| (décorative) | — (rang 1, alt/figcaption vide) | Introduction | IGNORÉE (décorative) |
| image_01.png | Charting with the Hull Moving Average (HMA) | Charting with the Hull Moving Average (HMA) [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2111 — Objectif de la HMA : réduire le lag en gardant le lissage
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « The Hull Moving Average (HMA) attempts to minimize the lag of a traditional moving average while retaining the smoothness of the moving average line. Developed by Alan Hull in 2005, this indicator makes use of weighted moving averages to prioritize more recent values and greatly reduce lag. The resulting average is more responsive and well-suited for identifying entry points. »
**TRADEX-AI C1** : HMA = MM réactive et lissée, conçue pour repérer les points d'entrée. Pertinente comme feature de tendance peu retardée sur les futures.
*Catégorie : indicateurs_tendance*

---

### D2112 — Réactivité supérieure à la SMA (illustration)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « Notice in the example below that the HMA line (in red) turns more quickly and decisively than the corresponding SMA (in blue). » (image d'introduction décorative, ignorée car alt/figcaption vide).
**TRADEX-AI C1** : la HMA tourne plus vite que la SMA → détection de retournement plus précoce. Avantage de réactivité à intégrer comme feature.
*Catégorie : indicateurs_tendance*

---

### D2113 — Structure de calcul en trois WMA
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « The formula for the Hull Moving Average uses two different weighted moving averages (WMAs) of price, plus a third WMA to smooth the raw moving average. There are three parts to the calculation. (...) "n" indicates the number of periods. »
**TRADEX-AI C1** : la HMA repose sur 3 WMA (deux de prix + une de lissage). Architecture de calcul déterministe et codable.
*Catégorie : indicateurs_tendance*

---

### D2114 — Étape 1 : deux WMA (n et n/2)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : `WMA1 = WMA(n/2) of price` ; `WMA2 = WMA(n) of price`. Première étape : calculer une WMA sur le nombre de périodes spécifié et une sur la moitié.
**TRADEX-AI C1** : formule littérale étape 1. Reproductible exactement.
*Catégorie : indicateurs_tendance*

---

### D2115 — Étape 2 : Raw HMA
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : `Raw HMA = (2 * WMA1) - WMA2`. Calcul de la Hull Moving Average brute (non lissée).
**TRADEX-AI C1** : formule littérale étape 2. Le décalage (2·WMA(n/2) − WMA(n)) est ce qui concentre le poids sur les valeurs récentes.
*Catégorie : indicateurs_tendance*

---

### D2116 — Étape 3 : lissage final sur sqrt(n)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : `HMA = WMA(sqrt(n)) of Raw HMA`. Troisième étape : lisser le Raw HMA avec une WMA dont la période est la racine carrée du nombre de périodes spécifié.
**TRADEX-AI C1** : formule littérale étape 3. Complète la chaîne de calcul de la HMA.
*Catégorie : indicateurs_tendance*

---

### D2117 — Arrondi des périodes non entières (exemple n=11)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : quand n/2 ou sqrt(n) n'est pas entier, on arrondit au plus proche. Exemple HMA 11 jours : 11/2 = 5,5 arrondi à 6 ; sqrt(11) = 3,317 arrondi à 3 pour la WMA de lissage finale.
**TRADEX-AI C1** : règle d'arrondi à implémenter pour reproduire exactement la HMA de StockCharts. Détail de précision codable.
*Catégorie : configuration*

---

### D2118 — Mécanisme de réduction du lag
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « Weighted moving averages inherently reduce lag by placing additional weight on more recent values. Lag is further reduced by offsetting one WMA with another (...) the most recent half (...). The final smoothing uses another WMA with even fewer periods (the square root...). The end result is a smooth moving average line that stays very close to the price bars. »
**TRADEX-AI C1** : explication du triple mécanisme de réduction du lag (WMA + offset moitié + lissage sqrt). Justifie l'usage de la HMA comme MM peu retardée collée au prix.
*Catégorie : indicateurs_tendance*

---

### D2119 — Interprétation : confirmer/repérer un changement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « The Hull Moving Average can be interpreted in a similar way to traditional moving averages, but it responds more quickly. Like other moving averages, it can be used to confirm a trend or spot a change in the trend. »
**TRADEX-AI C1** : usage double — confirmation de tendance et détection de retournement, plus rapide qu'une MM classique.
*Catégorie : indicateurs_tendance*

---

### D2120 — Signal d'entrée par turning point (HMA courte)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « HMAs with shorter periods are often used to identify entry points. When the overall trend is up and the HMA turns up, this is a signal to buy long. Conversely, when the overall trend is down and the HMA turns down, this is a signal to buy short. »
**TRADEX-AI C1** : règle de signal — retournement de la HMA courte DANS LE SENS de la tendance dominante = entrée (long si uptrend, short si downtrend). Filtre par tendance majeure intégré.
*Catégorie : signal*

---

### D2121 — Alan Hull déconseille les croisements de HMA
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « HMA creator Alan Hull does not recommend using crossovers with HMAs, because that technique depends on looking at differences in lag between the two moving averages, and the lag has already been greatly reduced in Hull Moving Averages. Instead, he recommends looking at turning points to identify entries and exits. »
**TRADEX-AI C1** : garde-fou explicite — NE PAS appliquer la logique de croisement à la HMA ; utiliser les turning points. Distinction importante vs la stratégie de croisement classique (cf. extraction MA crossovers).
*Catégorie : signal*

---

### D2122 — HMA longue (ex. 200) pour la tendance globale
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « HMAs with longer periods (e.g. 200-period HMA) can be used to identify the current overall trend. If the HMA is rising, the overall trend is up; if the HMA is falling, the overall trend is down. »
**TRADEX-AI C1** : HMA longue = filtre de tendance de fond (pente montante/descendante). Combinable avec HMA courte (D2120) pour le timing. Période 200 = exemple, à recalibrer.
*Catégorie : indicateurs_tendance*

---

### D2123 — Conclusion : jamais en stand-alone
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « Short-term traders can look for turning points in the average to identify entry/exit points. Longer-term HMAs can be used to identify or confirm the overall trend. As with all technical indicators, traders should use the HMA in conjunction with other indicators and analysis techniques. »
**TRADEX-AI C1** : garde-fou de confluence — brique de tendance/timing, jamais signal isolé. Cohérent avec la logique de score multi-cercles.
*Catégorie : signal*

---

### D2124 — Disponibilité via Advanced Indicator Pack (StockChartsACP)
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md, image_01) : « The HMA overlay can be charted on StockChartsACP after installing our free Advanced Indicator Pack (...). HMA can be overlaid on the security's price plot or on an indicator panel. »
**TRADEX-AI C1** : note d'implémentation plateforme StockCharts. La HMA n'est pas native partout — à coder soi-même pour NT8/ATAS. Valeur documentaire.
*Catégorie : configuration*

---

### D2125 — Période par défaut 20, ajustable
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : « By default, the moving average is calculated with 20 periods, but the number of periods can be adjusted to meet your technical analysis needs. »
**TRADEX-AI C1** : période par défaut 20 (paramétrable). Point de départ à recalibrer sur le timeframe TRADEX, jamais coder « 20 jours » tel quel pour les futures.
*Catégorie : configuration*

---

### D2126 — Scan « uptrend + prix croise au-dessus HMA »
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : scan littéral — uptrend présent quand `HullMA(50,Close) > Daily SMA(50,HullMA(50,Close))` ; signal d'achat quand `Daily Close crosses HullMA(20,Close)` (filtres : volume SMA(20) > 100000, SMA(60,Close) > 10).
**TRADEX-AI C1** : combinaison HMA 50 (tendance) + croisement prix/HMA 20 (signal). Logique de screening transposable comme condition de signal ; périodes 20/50 = exemples actions à recalibrer.
*Catégorie : signal*

---

### D2127 — Scan « downtrend + prix croise sous HMA »
🟢 **FAIT VÉRIFIÉ** (Source : hull_moving_average_hma.md) : scan littéral symétrique — downtrend quand `HullMA(50,Close) < Daily SMA(50,HullMA(50,Close))` ; signal de vente quand `HullMA(20,Close) crosses Daily Close`. Syntaxe identique pour les alertes.
**TRADEX-AI C1** : version baissière du screening HMA 50 + croisement HMA 20. Note : ce scan utilise un croisement prix/HMA pour le déclenchement, alors que D2121 déconseille les croisements ENTRE deux HMA — les deux ne se contredisent pas (prix vs HMA ≠ HMA vs HMA).
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2111 | Objectif HMA : réduire le lag | 🟢 | C1 | indicateurs_tendance |
| D2112 | Réactivité > SMA | 🟢 | C1 | indicateurs_tendance |
| D2113 | Structure 3 WMA | 🟢 | C1 | indicateurs_tendance |
| D2114 | Étape 1 : WMA(n/2) et WMA(n) | 🟢 | C1 | indicateurs_tendance |
| D2115 | Étape 2 : Raw HMA | 🟢 | C1 | indicateurs_tendance |
| D2116 | Étape 3 : lissage sqrt(n) | 🟢 | C1 | indicateurs_tendance |
| D2117 | Arrondi des périodes (n=11) | 🟢 | C1 | configuration |
| D2118 | Mécanisme de réduction du lag | 🟢 | C1 | indicateurs_tendance |
| D2119 | Confirmer / repérer changement de tendance | 🟢 | C1 | indicateurs_tendance |
| D2120 | Entrée par turning point (HMA courte) | 🟢 | C1 | signal |
| D2121 | Hull déconseille les croisements de HMA | 🟢 | C1 | signal |
| D2122 | HMA longue (200) = tendance globale | 🟢 | C1 | indicateurs_tendance |
| D2123 | Jamais en stand-alone | 🟢 | C1 | signal |
| D2124 | Advanced Indicator Pack (ACP) | 🟢 | C1 | configuration |
| D2125 | Période par défaut 20 ajustable | 🟢 | C1 | configuration |
| D2126 | Scan uptrend + prix croise HMA | 🟢 | C1 | signal |
| D2127 | Scan downtrend + prix croise HMA | 🟢 | C1 | signal |

| Élément | Valeur |
|---------|--------|
| Décisions | D2111 → D2127 (17) |
| Images certifiées | 1/2 (1 décorative IGNORÉE) |
| Cercles | C1 (tendance/signal, exclusif) |
| Catégories | indicateurs_tendance · signal · configuration |
| Actif applicable | GC/HG/CL/ZW (TRADING) + ES — overlay transposable, période à recalibrer |
| Belkhayate | NON CONCERNÉ (HMA ≠ outil Belkhayate) |
| Pertinence futures | OUI (C1) — overlay de tendance/retournement directement utile au moteur |
| Cas « à vérifier » | (1) Périodes 20/50/200 et scans HullMA(20)/HullMA(50) : exemples actions US daily, NE PAS coder tels quels — recalibrer sur timeframe TRADEX. (2) Distinction clé : D2121 déconseille les croisements ENTRE deux HMA, mais D2126/D2127 utilisent un croisement PRIX/HMA (non contradictoire) — à expliciter avant implémentation. (3) image d'intro = décorative ignorée (alt/figcaption vide), conforme au manifest. |

**Liens Belkhayate :** Aucun lien direct — la Hull Moving Average n'est PAS un indicateur Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
