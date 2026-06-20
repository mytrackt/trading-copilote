# Extraction KB — ChartSchool : John Murphy's "Charting Made Easy" eBook
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/john-murphys-charting-made-easy-ebook  
**Version :** v1 enrichie (31 charts analysés visuellement)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Auteur source :** John Murphy — StockCharts.com  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Pertinence TRADEX :** 🔴 MAXIMALE — Couvre les 6 piliers visuels de l'AT : types de charts, S/R, trendlines, patterns, gaps, oscillateurs, volume.  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS
| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart analysé |
| 🔵 | Règle générale Murphy/ChartSchool |
| 🟡 | Application TRADEX déduite |
| ⏳ | À implémenter |
| 🔴 | Risqué si mal appliqué |

---

## SECTION 1 — TYPES DE GRAPHIQUES

### 1.1 Graphique en Ligne (Line Chart)

🟢 **Chart INTC Daily (27-Mar-2000) — version longue (Nov 1998→Mar 2000) :**
- Ligne continue reliant les **prix de clôture** uniquement
- Uptrend visible : ~$18 (nov 1998) → ~$55 (mars 2000) = +205%
- La ligne masque l'amplitude journalière (range intraday invisible)

🟢 **Chart INTC Daily (27-Mar-2000) — version courte (Aug 1999→Mar 2000) :**
- Même actif, même tendance : ~$65 → ~$145 (+123% en 8 mois)
- Prix le 27-Mar-2000 : 142.69 (Open: 139.62, High: 143.75, Low: 139.06, Close: 142.69, Volume: 17.9M)

🔵 **Avantage Line Chart :** simplicité, idéal pour visualiser la tendance globale et les niveaux de clôture. Perd l'information intraday (Open, High, Low).

### 1.2 Graphique en Bougies (Candlestick Chart)

🟢 **Chart INTC Daily Candlestick (29-Mar-2000) :**
- Annotation officielle : *"Area between open and close. Open candles are positive. Darker candles are negative."*
- Annotation : *"Day's Range"* → la mèche complète (wick) = range total de la journée (High-Low)
- Prix 29-Mar-2000 : Open 136.50, High 137.69, Low 131.50, Close 131.88 (-3.81, -2.81%)
- **Bougie baissière (sombre/noire) :** Close < Open = corps plein = pression vendeuse
- **Bougie haussière (vide/blanche) :** Close > Open = corps vide = pression acheteuse

🔵 **Règle lecture bougie :**
- Corps large = forte conviction directionnelle
- Mèche longue = rejet du niveau extrême (rejet haussier ou baissier)
- Doji (corps quasi nul) = indécision du marché

### 1.3 Graphique en Barres (Bar Chart / OHLC)

🟢 **Chart IBM Daily (22-Mar-2000) — Bar Chart avec labels :**
- Labels visuels : **Open** (trait gauche), **High** (sommet de la barre), **Low** (bas de la barre), **Close** (trait droit)
- Prix IBM : Open 114.50, High 115.38, Low 113.88, Close 114.25 (+0.75, +0.66%)
- Annotation : **"Volume Bars"** → panneau inférieur, volumes IBM : 2M→10M selon les jours
- Downtrend visible de fév 2000 (~$120) vers creux ~$100 puis rebond vers $114

🔵 **Avantage Bar Chart :** montre Open + High + Low + Close = information complète. Moins lisible que les bougies mais identique en contenu.

---

## SECTION 2 — SUPPORT ET RÉSISTANCE

### 2.1 Support et Résistance Horizontaux

🟢 **Chart HAL (Halliburton) Daily (28-Apr-2000) — 5 niveaux annotés :**

| Niveau | Type | Prix approx. | Période |
|--------|------|-------------|---------|
| Résistance 1 | Résistance | ~$43-44 | Déc 1999 |
| Support 1 | Support | ~$34-35 | Déc 1999→Jan 2000 |
| Résistance 2 | Résistance | ~$43-44 | Fév 2000 |
| Support 2 | Support | ~$34-35 | Mars 2000 |
| Résistance 3 | Résistance | ~$45-46 | Avr 2000 |

🟢 **Observation :** les mêmes niveaux (~$34-35 support, ~$43-46 résistance) sont testés plusieurs fois sur plusieurs mois → **les niveaux S/R se renforcent à chaque nouveau test**.

🔵 **Règle S/R multiple :** plus un niveau est testé sans être cassé, plus il est fort. Un support testé 3× est plus significatif qu'un support testé 1×.

### 2.2 Inversion Support/Résistance (Murphy Loi 3)

🟢 **Chart XOM (Exxon Mobil) Daily (31-Oct-2006) — L'exemple classique :**
- **Annotation gauche :** *"Prior Resistance Level...."* → niveau horizontal ~$55, testé comme résistance en sept-oct 2005
- **Annotation droite :** *"....becomes new support level"* → même niveau ~$55, devient support en août-sept 2006
- Chronologie : XOM oscille sous $55 (2005), casse à la hausse, revient tester $55 par le bas → rebond confirmé

🔵 **Règle d'inversion (fondamentale TRADEX) :**
- Résistance cassée → **nouveau support** sur les pullbacks
- Support cassé → **nouvelle résistance** sur les rebonds
- Le niveau reste pertinent même après la cassure — il change juste de rôle

🟡 **Application TRADEX :** le COG Belkhayate est un niveau S/R dynamique. Après cassure haussière du COG, le COG devient support. Après cassure baissière, le COG devient résistance. Cette règle doit être codée dans Couche 4 (vision Claude).

### 2.3 Double Breakout de Résistance

🟢 **Chart AMD Daily (28-Apr-2000) :**
- **"1st upside breakout"** : cassure de la résistance ~$16 (1999) après un long consolidation 1997-1998
- **"2nd upside breakout"** : cassure de la résistance ~$24 (2000) après accumulation
- Après le 2ème breakout : AMD s'envole vers ~$44 rapidement

🔵 **Règle double breakout :** chaque résistance cassée devient support. Deux cassures successives = signal d'accélération. Le 2ème breakout valide la force du momentum.

---

## SECTION 3 — TRENDLINES ET CANAUX

### 3.1 Uptrend Line — 4 touches (MSFT)

🟢 **Chart MSFT Daily (3-Mar-2000) — Trendline montante avec 4 touches numérotées :**
- Touch 1 : avr 1999 (~$29) — point de départ
- Touch 2 : juin 1999 (~$29-30)
- Touch 3 : oct 1999 (~$32)
- Touch 4 : fév 2000 (~$33-34)
- Trendline tracée sous les creux → valid car **≥ 3 touches** (Murphy Loi 5)

🔵 **Règle validité trendline :** minimum 3 touches. Ici 4 touches = trendline très fiable. Prix le 3-Mar-2000 : Close 35.79 (Volume: 132.7M = très élevé).

### 3.2 Canal de Tendance Haussier (Rising Channel)

🟢 **Chart CSCO Daily (31-Dec-1999) :**
- **Rising Trendline (bas du canal) :** tracée sous les creux successifs depuis jan 1999
- **Channel Line (haut du canal) :** tracée parallèle, au-dessus des sommets successifs
- Le prix oscille entre les deux lignes tout au long de 1999
- Prix au 31-Dec-1999 : ~$50 (sommet du canal visible)
- Breakout à la hausse visible en nov-déc 1999 → accélération au-dessus de la Channel Line

🔵 **Règle canal haussier :**
- Acheter près de la trendline support (bas du canal)
- Prendre profit près de la channel line (haut du canal)
- Cassure haussière de la channel line = **accélération de la tendance**
- Cassure baissière de la trendline = **fin de la tendance**

### 3.3 Trendline Long Terme ($NYA Weekly)

🟢 **Chart $NYA (NYSE Composite) Weekly (31-Jan-2000) :**
- Trendline montante depuis 1996 (~3600) → jan 2000 (~6574)
- Valeur au 31-Jan-2000 : 6574.01 (Volume: 968.1M)
- Le prix reste au-dessus de la trendline tout au long de 1996-2000 sans la casser
- **Trendline = support majeur long terme de tout le bull market 1996-2000**

### 3.4 Rupture de Trendline ($SOX)

🟢 **Chart $SOX (Philadelphia Semiconductor Index) Daily (28-Apr-2000) :**
- Trendline montante depuis déc 1999 (~$600) jusqu'à janv 2000 (~$950)
- **Rupture baissière de la trendline** : prix casse sous la trendline brutalement en mars-avr 2000
- Post-rupture : $SOX chute de ~$1350 (jan 2000) vers ~$900 (-33%)
- Prix au 28-Apr-2000 : 1171.60

🔵 **Règle rupture trendline :** la cassure d'une trendline valide (≥3 touches) = signal de changement de tendance. Plus la trendline est ancienne et testée, plus la rupture est significative.

### 3.5 Trendline avec Accélération (INTC)

🟢 **Chart INTC Daily (7-Apr-2000) :**
- Trendline montante depuis nov 1999 (~$75) → avr 2000 (~$120)
- Prix breakout au-dessus de la trendline en jan 2000 → **accélération**
- INTC monte de ~$120 (jan) → ~$145 (mars) en parabole
- Prix 7-Apr-2000 : 136.81 (Open: 131.38, High: 137.00, Volume: 25.7M)

### 3.6 Triangle Symétrique (Citigroup)

🟢 **Chart C (Citigroup) Daily (31-Mar-2000) :**
- **"Declining Upper Line"** : ligne de résistance descendante (sommets décroissants)
- **"Rising Lower Line"** : ligne de support montante (creux croissants)
- Les deux lignes convergent → triangle symétrique (fév→oct 1999)
- **Breakout haussier en nov 1999** : prix sort par le haut → C monte de ~$250 → ~$330
- Prix 31-Mar-2000 : 322.75

🔵 **Règle Triangle Symétrique :** pattern de continuation neutre (direction du breakout = direction du trade). La cible théorique = hauteur du triangle projetée depuis le point de cassure.

### 3.7 Triangle Ascendant (Walgreen)

🟢 **Chart WAG (Walgreen) Daily (14-Jul-2000) :**
- **"Flat Upper Line"** : résistance horizontale ~$25.5 (testée plusieurs fois)
- **"Rising Lower Line"** : support montant depuis mars 2000
- Compression progressive → breakout haussier début juil 2000
- WAG s'envole de ~$25.5 → ~$29 post-breakout

🔵 **Règle Triangle Ascendant :** pattern **haussier** par nature (acheteurs plus agressifs = creux qui montent, vendeurs statiques = résistance plate). Probabilité de breakout haussier > 50%.

---

## SECTION 4 — PATTERNS DE RETOURNEMENT

### 4.1 Head & Shoulders Inversé (ALK)

🟢 **Chart ALK (Alaska Air) Daily (26-Feb-1999) :**

| Composant | Période | Prix approx. |
|-----------|---------|-------------|
| Left Shoulder (Épaule gauche) | Août-sept 1998 | Creux ~$16 |
| Head (Tête) | Oct 1998 | Creux ~$13 (plus bas) |
| Right Shoulder (Épaule droite) | Nov-déc 1998 | Creux ~$16 |
| Neckline (Ligne de cou) | Descendante (~$21→$19) | Linie tracée sur les sommets entre les creux |

- **Breakout haussier au-dessus de la neckline :** jan 1999 → ALK monte jusqu'à ~$29
- Prix 26-Feb-1999 : 25.20

🔵 **Règle H&S Inversé :** pattern de retournement **haussier**. Valide quand : 3 creux avec le central plus bas, neckline clairement identifiable, cassure avec volume. Cible = hauteur de la tête projetée au-dessus de la neckline.

### 4.2 Rectangle de Consolidation (GE)

🟢 **Chart GE Daily (31-Mar-2000) :**
- Consolidation horizontale ~fév→mars 2000 entre ~$127 et ~$140
- Niveau "1" marqué au bas = point de départ de la compression
- Résistance horizontale ~$140-141 testée plusieurs fois
- **Breakout haussier en mars-avr 2000** : GE monte vers ~$163
- Prix 31-Mar-2000 : 155.62

🔵 **Règle Rectangle :** pattern de consolidation (continuation). Breakout dans la direction de la tendance précédente. Cible = hauteur du rectangle projetée depuis le breakout.

### 4.3 Spike Top / Spike Bottom (ISLE)

🟢 **Chart ISLE (Isle of Capris Casinos) Daily (28-Mar-2013) — Line Chart :**
- **"Spike Top" :** cerclé en haut — sommet en pointe très aiguë (~juil 2012, ~$7.40) suivi d'une chute rapide
- **"Spike Bottom" :** cerclé en bas — creux en pointe (~déc 2012, ~$5.10) suivi d'une remontée rapide
- Prix 28-Mar-2013 : 6.29

🔵 **Règle Spike (V-Pattern) :**
- Spike Top = retournement baissier brutal, souvent sur fort volume
- Spike Bottom = retournement haussier brutal, épuisement des vendeurs
- Pas de zone de consolidation → retournement le plus rapide et le plus difficile à trader (peu de temps pour réagir)

### 4.4 Saucer Bottom / Rounded Bottom (AMD)

🟢 **Chart AMD Daily (28-Apr-2000) :**
- **"Saucer Bottom" :** courbe arrondie visible sur le bas du graphique (~nov1999→jan2000)
- La courbe est tracée sous les prix comme une assiette renversée
- Post-saucer : AMD monte de ~$20 → ~$87 en 3 mois
- Prix 28-Apr-2000 : 87.50

🔵 **Règle Saucer Bottom :**
- Pattern de retournement haussier lent (semaines à mois)
- Volume généralement faible pendant la formation, croissant à la sortie
- Plus fiable que le V-Bottom car donne le temps de positionner

### 4.5 Double Top Breakdown (LMT)

🟢 **Chart LMT (Lockheed Martin) Daily (1-Jul-2010) :**
- Deux sommets ~$69.5-70 (mars et avr 2010) au même niveau → Double Top
- Ligne horizontale tracée entre les deux sommets
- **Cassure baissière sous le support intermédiaire (~$68)** en mai 2010
- LMT chute vers ~$63 post-cassure

🔵 **Règle Double Top :** (voir aussi extraction Fundamental Analysis — cas Citigroup -94%)
- Deux sommets identiques → résistance très forte
- Cassure sous le neckline (creux entre les deux sommets) = signal de vente
- Plus le temps entre les deux sommets est long, plus le pattern est significatif

### 4.6 Neckline Cassée avec Volume (ADM)

🟢 **Chart ADM (Archer Daniels Midland) Daily (31-Aug-1999) :**
- **"Broken Neckline"** : ligne horizontale ~$15, neckline d'un double top
- ADM oscille sous $15-17 (1997-1998), forme double top autour de $17
- **Cassure baissière de la neckline ~$15** en mai-juin 1998 avec gap baissier
- Volume panel bas : **"Heavy Volume During the Price Breakdown"** — pic visible au moment de la cassure
- Post-cassure : ADM descend de ~$15 → ~$10.35 (-31%)

🔵 **Règle critique :** une cassure de neckline AVEC pic de volume = **confirmation forte**. Une cassure sans volume = potentiellement un faux signal. Murphy Loi 10 s'applique ici directement.

---

## SECTION 5 — PATTERNS DE CONTINUATION

### 5.1 Bullish Pennant (AAPL)

🟢 **Chart AAPL Daily (31-Dec-1999) :**
- **"Bullish Pennant"** : triangle convergent court (~2 semaines) formé après une forte hausse
- Contexte : AAPL monte de ~$60 (oct) → ~$88 (nov), puis consolide en triangle symétrique court
- **Breakout haussier** : déc 1999, AAPL monte vers ~$117
- Prix 31-Dec-1999 : 102.81

🔵 **Règle Pennant :**
- Pattern de continuation court terme (quelques jours à 2 semaines)
- Précédé d'une "mât" (flagpole) = mouvement fort et rapide
- Cible = longueur du mât projetée depuis le breakout du pennant
- Volume : diminue pendant le pennant, explose au breakout

### 5.2 Bull Flag (DIA)

🟢 **Chart DIA (Dow ETF) Daily (23-Jan-2014) :**
- **"Bull Flag"** : petit canal descendant (quelques semaines) après une forte hausse
- Contexte : DIA monte de ~$148 (oct) → ~$160 (nov), puis consolide en flag descendant
- Cassure haussière du flag en déc 2013 → DIA monte vers ~$165
- Prix 23-Jan-2014 : 161.51 (-1.96, -1.20%)

🔵 **Règle Bull Flag vs Bull Pennant :**
- **Flag :** canal parallèle (deux lignes parallèles descendantes) = correction modeste
- **Pennant :** triangle convergent = compression de volatilité
- Les deux sont des patterns de continuation haussiers
- Volume : décline pendant la formation, monte au breakout

### 5.3 Gaps sur $NDX 60 Minutes

🟢 **Chart $NDX 60-min (28-Sep-2007) — 3 types de gaps annotés :**

| Gap | Position | Caractéristique | Signification |
|-----|----------|-----------------|---------------|
| **Upside Breakaway Gap** | 18-19 sept 2007 | Gap haussier sortant d'une zone de consolidation | Début de tendance haussière forte |
| **Runway Gap** | 25-26 sept 2007 | Gap haussier au milieu d'une tendance | Accélération, indique la mi-parcours |
| **Exhaustion Gap** | 27-28 sept 2007 | Gap haussier suivi d'une consolidation/retournement | Fin de tendance imminente |

🔵 **Règles des 3 types de gaps :**
- **Breakaway Gap :** ne se comble pas rapidement. Volume élevé. Signal fort de début de tendance.
- **Runway Gap :** (aussi appelé "Continuation Gap") au milieu du mouvement. Sert à mesurer la cible (mi-parcours).
- **Exhaustion Gap :** dernier gap avant retournement. Volume élevé mais épuisement des acheteurs. Se comble souvent rapidement.

🟡 **Application TRADEX :** les gaps sur les futures (ex: gap d'ouverture sur Gold ou NQ) doivent être classifiés avant décision. Un Exhaustion Gap sur Gold = signal de méfiance même si haussier. ⏳ À inclure dans Couche 4 (vision Claude).

### 5.4 Patterns Combinés sur SPY 60-Min

🟢 **Chart SPY 60-min (3-Oct-2013) — 4 éléments annotés :**
- **"Upside Gap"** : gap haussier visible en sept 2013 (~$167→$168)
- **"Gap Support"** : le gap devient support lors du pullback suivant (~$168)
- **"Trendline Broken"** : ligne de résistance descendante cassée à la hausse
- **"Pennant Completed"** : mini-triangle convergent complété en bas (~oct 2013)

🔵 **Règle Gap Support :** un gap haussier non comblé devient zone de support. Si le prix revient tester le gap et rebondit = confirmation haussière. Si le prix comble le gap = signal d'affaiblissement.

---

## SECTION 6 — VOLUME ET INDICATEURS DE VOLUME

### 6.1 Downside Reversal Day avec Volume (IBM)

🟢 **Chart IBM Daily (31-Jan-2000) :**
- **"Downside Reversal Day" (1ère occurrence) :** déc 1999, IBM fait nouveau High (~$122) mais clôture sous l'Open = inversion baissière
- **"Heavy Volume" (1)** : volume panneau inférieur ~15M+ ce jour-là → confirmation
- **"Downside Reversal Day" (2ème occurrence) :** jan 2000, même pattern au sommet ~$125
- **"Heavy Volume" (2)** : autre pic de volume ~15M+ → confirmation
- Post-événements : IBM chute de $122→$112, puis $125→$112

🔵 **Règle Downside Reversal Day :**
- Prix fait nouveau sommet en intraday
- Clôture sous l'ouverture (ou sous le Close précédent)
- Volume élevé = confirmation que les vendeurs ont pris le contrôle
- Signal baissier de retournement à court terme

### 6.2 OBV Bearish Divergence (JDSU)

🟢 **Chart JDSU Daily (31-May-2000) — OBV Divergence BAISSIÈRE :**
- **Panneau prix :** "Rise in Price" → JDSU monte de ~$400 (nov 1999) → ~$1150 (mars 2000)
- **Panneau OBV :** "Flat OBV Line" → l'OBV reste plat ou légèrement décroissant pendant toute la hausse
- **Divergence : prix monte MAIS OBV plat = distribution déguisée**
- Post-divergence : JDSU chute de $1150 → $700 en mai 2000

🔵 **Règle OBV Bearish Divergence :**
- Prix fait nouveaux sommets
- OBV reste plat ou baisse
- Signification : les institutionnels vendent en silence pendant que le prix monte (distribution)
- Signal de retournement baissier imminent

### 6.3 OBV Bullish Divergence (GE)

🟢 **Chart GE Daily (31-May-2000) — OBV Divergence HAUSSIÈRE :**
- **Panneau prix :** "Decline in Price" → GE descend de ~$39 (nov 1999) → ~$30 (mars 2000)
- **Panneau OBV :** "Rising OBV Line" → l'OBV monte pendant que le prix baisse
- **Divergence : prix baisse MAIS OBV monte = accumulation silencieuse**
- Post-divergence : GE remonte vers ~$39 en avr-mai 2000

🔵 **Règle OBV Bullish Divergence :**
- Prix fait nouveaux creux
- OBV monte ou reste stable
- Signification : les institutionnels achètent pendant la baisse (accumulation)
- Signal de retournement haussier imminent

🟡 **Application TRADEX CRITIQUE :** l'OBV est l'indicateur de divergence volume/prix le plus simple. Pour les futures Gold/NQ, calculer l'OBV sur 20 bougies. Si prix baisse et OBV monte → signal long COG renforcé. ⏳ À ajouter dans Couche 2 (algo Python).

### 6.4 Volume et Patterns sur JDSU (Bull Flags)

🟢 **Chart JDSU Daily (9-Mar-2000) — 2 bull flags avec volume :**
- Prix : deux consolidations en flag visible (jan et fév 2000) sur fond de forte tendance haussière
- Volume inférieur : diminue pendant chaque flag, puis pic au breakout
- Confirmation visuelle de la règle : "Volume decreases in the flag, explodes at the breakout"

---

## SECTION 7 — OSCILLATEURS

### 7.1 RSI(9) sur $INDU — Overbought/Oversold

🟢 **Chart $INDU Daily + RSI(9) (31-May-2000) :**
- Panneau supérieur : $INDU oscille entre ~$9800 et ~$11600 (mai 1999→mai 2000)
- Panneau inférieur : **RSI(9)** avec niveaux annotés
  - **"Overbought"** : ligne horizontale à **70**
  - **"Oversold"** : ligne horizontale à **30** (en rouge, deux occurrences visibles)
- Les zones oversold (oct 1999, mars 2000) correspondent à des creux importants du INDU
- Divergences RSI/prix visibles sur plusieurs tops

🔵 **Paramètres Murphy RSI pour TRADEX :**
- Période : **9** (court terme, plus réactif) ou 14 (standard)
- Suracheté : **> 70**
- Survendu : **< 30**
- Sur les futures intraday : RSI(9) sur 5-15 min peut être utilisé pour le timing d'entrée

### 7.2 Stochastics sur $SPX — Overbought/Oversold

🟢 **Chart $SPX Daily + Stochastics (31-May-2000) :**
- Panneau supérieur : $SPX entre ~$1260 et ~$1520 (mai 1999→mai 2000)
- Panneau inférieur : **Stochastics** avec niveaux annotés
  - **"Overbought"** : **80** (ligne haute)
  - **"Oversold"** : **20** (ligne basse)
- Oscillations rapides et fréquentes du stochastics entre 20 et 80
- Le stochastics dépasse 80 souvent (marché en forte tendance haussière) → **en tendance forte, le stochastics peut rester suracheté longtemps**

🔵 **Règle Murphy Stochastics :**
- Période : 14 jours/semaines
- Suracheté : > 80 ; Survendu : < 20
- En **marché range** : signaux fiables
- En **forte tendance** : peut rester suracheté/survendu longtemps → filtrer avec ADX

### 7.3 Relative Strength Intermarché ($COMPQ/$SPX)

🟢 **Chart $COMPQ/$SPX Daily (10-Apr-2000) — Ratio de Relative Strength :**
- Le ratio COMPQ/SPX mesure la surperformance du Nasdaq vs S&P 500
- Valeur au 10-Apr-2000 : 2.78 (-0.15, -5.06%)
- **Trendline montante** tracée depuis oct 1999 (~2.2) → mars 2000 (~3.5)
- **Cassure baissière de la trendline** en mars-avr 2000 → COMPQ commence à sous-performer SPX
- Post-cassure : ratio chute de 3.5 → 2.78 rapidement = signal précoce de rotation

🔵 **Règle Relative Strength (ratio chart) :**
- Ratio monte = premier actif surperforme le second
- Ratio baisse = premier actif sous-performe le second
- Cassure d'une trendline sur le ratio = **rotation de leadership de marché** imminente

🟡 **Application TRADEX :** surveiller le ratio Gold/$DXY (or vs dollar) ou NQ/SPX. Cassure baissière du ratio Gold/DXY = or commence à sous-performer le dollar = vent contraire pour les longs or. ⏳ À intégrer dans Couche 1 comme filtre contextuel.

---

## SECTION 8 — TABLEAU DE SYNTHÈSE : PATTERNS KB TRADEX

### 8.1 Patterns de Retournement (Couche 4 Vision Claude)

| Pattern | Biais | Signal d'entrée | Confirmation |
|---------|-------|----------------|--------------|
| H&S Inversé | Haussier | Cassure neckline | Volume au breakout |
| Double Top | Baissier | Cassure neckline | Volume au breakdown |
| Saucer Bottom | Haussier | Sortie de la courbe | Volume croissant |
| Spike Bottom | Haussier | Clôture au-dessus du spike | Immédiat |
| Spike Top | Baissier | Clôture sous le spike | Immédiat |
| Rectangle breakout | Direction tendance | Cassure du range | Volume |

### 8.2 Patterns de Continuation

| Pattern | Biais | Durée | Cible |
|---------|-------|-------|-------|
| Bull Flag | Haussier | Jours-semaines | Longueur du mât |
| Bear Flag | Baissier | Jours-semaines | Longueur du mât |
| Bull Pennant | Haussier | Jours | Longueur du mât |
| Triangle Ascendant | Haussier | Semaines | Hauteur triangle |
| Triangle Symétrique | Neutre | Semaines | Hauteur triangle |

### 8.3 Gaps (Couche 4 Vision Claude)

| Gap | Signal | Volume | Comblé rapidement ? |
|-----|--------|--------|---------------------|
| Breakaway | Début tendance | Élevé | Non |
| Runway | Mi-tendance | Modéré | Non |
| Exhaustion | Fin tendance | Élevé | Oui (souvent) |

### 8.4 Oscillateurs — Paramètres de Référence

| Indicateur | Période | Suracheté | Survendu | Usage optimal |
|------------|---------|-----------|----------|---------------|
| RSI | 9 ou 14 | > 70 | < 30 | Range + divergences |
| Stochastics | 14 | > 80 | < 20 | Range |
| OBV | Cumulatif | Hausse = bullish | Baisse = bearish | Divergence prix/volume |

---

## SECTION 9 — RÈGLES GÉNÉRALES CLÉS (SYNTHÈSE MURPHY)

🔵 **R1 — Volume précède le prix (OBV) :** OBV monte = accumulation institutionnelle. OBV plat/baisse sur hausse de prix = distribution = signal baissier.

🔵 **R2 — Trendline = 3 touches minimum :** 2 points = trendline provisoire. 3 points = trendline valide. 4+ points = très fiable.

🔵 **R3 — Gap support :** un gap non comblé = zone de support (haussier) ou résistance (baissier). Le prix qui revient tester le gap est une opportunité d'entrée.

🔵 **R4 — Reversal Day + Volume = signal fort :** nouveau sommet intraday + clôture baissière + volume élevé = alerte de retournement immédiate.

🔵 **R5 — Oscillateurs en range, MA en tendance :** RSI/Stochastics en range (ADX < 20). Moving averages en tendance (ADX > 25). Ne jamais utiliser les oscillateurs seuls en forte tendance.

🔵 **R6 — Pattern + Volume + Convergence = haute confiance :** un pattern seul = signal moyen. Pattern + volume confirmant + oscillateur aligné = signal haute confiance. Pour TRADEX : COG Belkhayate + pattern visuel + volume + ADX en tendance = confiance maximale.

---

## SECTION 10 — CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Calcul exact de l'OBV → formule : OBV(t) = OBV(t-1) + Volume si Close > Close(t-1), -Volume si Close < Close(t-1)
⏳ Paramètres Stochastics exacts (%K, %D, lissage) → non détaillés ici
⏳ Cibles de prix des patterns (mesure exacte) → partiellement couvert
⏳ Intermarché avancé (or/dollar, taux/actions) → voir extraction Asset Allocation

---

*Fin d'extraction — John Murphy's Charting Made Easy — v1 enrichie visuellement (31 charts)*  
*Auteur source : John Murphy, StockCharts.com. Document éducatif uniquement.*  
*Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
