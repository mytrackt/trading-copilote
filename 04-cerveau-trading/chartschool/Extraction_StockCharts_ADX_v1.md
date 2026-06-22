# Extraction_StockCharts_ADX_v1.md
**Source :** StockCharts ChartSchool — Average Directional Index (ADX)  
**URL :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx  
**Décisions :** D62 → D77  
**Images certifiées :** 9/9 (double ancrage v3.1 · section-fallback ARCH-15)  
**Date extraction :** 23/06/2026  

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — DÉFINITION ET ORIGINE

### D62 — ADX / +DI / -DI : définition et créateur

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §What Is the Average Directional Index) : L'Average Directional Index (ADX), le Minus Directional Indicator (-DI) et le Plus Directional Indicator (+DI) forment un groupe d'indicateurs de mouvement directionnel constituant un système de trading développé par **Welles Wilder**. Wilder a conçu son Directional Movement System pour les **matières premières et les prix journaliers**, mais ces indicateurs s'appliquent aussi aux actions.

🔵 **ÉCOLE** (Wilder) : Wilder présente ces indicateurs dans son livre de 1978 *New Concepts in Technical Trading Systems* — le même ouvrage qui introduit l'ATR, le Parabolic SAR et le RSI.

**TRADEX-AI C0/C1** : ADX = brique de la Couche 0 NinjaScript (export `ADX`, `+DI`, `-DI`). Mesure la force de tendance pour C1 (NQ/ES/Gold) — futures = instruments proches des matières premières visées par Wilder.

---

### D63 — Système directionnel : direction (+DI/-DI) vs force (ADX) (image_01)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §What Is the Average Directional Index + image_01 · label certifié : What Is the Average Directional Index (ADX)? [SECTION-FALLBACK]) :

- **+DI** (vert) et **-DI** (rouge) sont dérivés de moyennes lissées des différences de mouvement directionnel et mesurent la **direction** de la tendance. Quand +DI est *au-dessus* de -DI → tendance haussière · quand +DI est *en dessous* de -DI → tendance baissière. Ensemble, +DI et -DI sont appelés **DMI** (Directional Movement Indicator).
- **ADX** (noir) est dérivé des moyennes lissées de la différence entre +DI et -DI ; il mesure la **force** de la tendance, indépendamment de sa direction.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §What Is the Average Directional Index) : Le mouvement directionnel positif et négatif forme l'ossature du système. Wilder détermine le mouvement directionnel en comparant la différence entre deux plus bas consécutifs avec la différence entre leurs plus hauts respectifs.

**TRADEX-AI C1** : Combiner les deux dimensions — **direction** (+DI vs -DI) ET **force** (ADX) — pour qualifier une tendance avant tout signal d'entrée sur NQ/ES/Gold.

---

## BLOC 2 — CALCUL

### D64 — Mouvement directionnel +DM / -DM (image_02)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Directional Movement Calculation + image_02 · label certifié : Directional Movement Calculation [SECTION-FALLBACK]) :

- Mouvement directionnel **positif** (+DM) quand : (plus haut actuel − plus haut précédent) > (plus bas précédent − plus bas actuel). +DM = plus haut actuel − plus haut précédent, s'il est positif (sinon 0).
- Mouvement directionnel **négatif** (-DM) quand : (plus bas précédent − plus bas actuel) > (plus haut actuel − plus haut précédent). -DM = plus bas précédent − plus bas actuel, s'il est positif (sinon 0).

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Directional Movement Calculation · image_02) : Quatre cas illustrés — forte +DM (grand écart de plus hauts) · outside day favorable -DM · forte -DM (grand écart de plus bas) · **inside day = aucun mouvement directionnel (zéro)**. Tous les inside days ont un mouvement directionnel nul.

**TRADEX-AI C0** : Logique à exporter en NinjaScript — calcul de +DM/-DM par barre, avec règle inside-day → 0.

---

### D65 — Calcul ADX pas à pas (14 périodes) (image_03)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Step by Step ADX Calculation + image_03 · label certifié : Step by Step ADX Calculation [SECTION-FALLBACK]) : Calcul basé sur un réglage **14 périodes** recommandé par Wilder :

```
1. Calculer TR, +DM, -DM pour chaque période
2. Lisser ces valeurs (technique de lissage Wilder)
3. +DI14 = (+DM lissé 14j / TR lissé 14j) × 100   → ligne verte
4. -DI14 = (-DM lissé 14j / TR lissé 14j) × 100   → ligne rouge
5. DX    = ( |+DI14 − -DI14| / (+DI14 + -DI14) ) × 100
6. ADX   = moyenne 14j de DX, puis lissée : ((ADX précédent × 13) + DX actuel) / 14
```

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Step by Step ADX Calculation) : Wilder décrit la « True Range » (TR) dans ses formules — méthode de calcul **identique à l'ATR**. Environ 150 périodes sont nécessaires pour absorber les lissages (écart de calcul de 119 jours dans l'exemple tableur).

**TRADEX-AI C0** : Export NinjaScript `ADX(14)` + `+DI(14)` + `-DI(14)` sur clôtures/H-L-C. Dépendance directe à l'ATR (à extraire ensuite).

---

### D66 — Techniques de lissage Wilder

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Wilder's Smoothing Techniques) : Il faut **environ 150 périodes** de données pour obtenir de vraies valeurs ADX. Une ADX sur 30 périodes ne correspond PAS à une ADX sur 150 périodes ; au-delà de 150 jours, les valeurs restent cohérentes.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Wilder's Smoothing Techniques) — lissage des TR1/+DM1/-DM1 sur 14 périodes :

```
First TR14      = somme des 14 premières TR1
Second TR14     = First TR14 − (First TR14 / 14) + TR1 actuel
Subsequent TR14 = Prior TR14 − (Prior TR14 / 14) + TR1 actuel
```

**TRADEX-AI C0** : Prévoir un **warm-up ≥ 150 barres** avant de considérer l'ADX comme valide dans le moteur — sinon valeur biaisée → ne pas générer de signal.

---

## BLOC 3 — INTERPRÉTATION ET FORCE DE TENDANCE

### D67 — ADX mesure la force, pas la direction

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Interpreting the Average Directional Index) : L'ADX mesure la **force ou la faiblesse d'une tendance, pas sa direction**. La direction est définie par +DI et -DI : les acheteurs ont l'avantage quand +DI > -DI · les vendeurs quand -DI > +DI. Les croisements directionnels peuvent être combinés à l'ADX pour un système complet.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Interpreting the Average Directional Index) : Wilder était trader de matières premières et devises — ses exemples portent sur ces instruments, pas sur les actions. Les actions à faible volatilité peuvent ne pas générer de signaux avec les paramètres de Wilder ; il faut alors ajuster les réglages.

**TRADEX-AI C1** : Sur NQ/ES/Gold (futures volatils, proches des matières premières), les paramètres Wilder standard sont a priori adaptés — à valider en Phase C sur range bars NT8.

---

### D68 — Seuils de force de tendance (image_04)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Measuring Trend Strength + image_04 · label certifié : Measuring Trend Strength [SECTION-FALLBACK]) : Selon Wilder :

- **ADX > 25** → tendance forte présente
- **ADX < 20** → pas de tendance
- **20–25** → zone grise
- De nombreux analystes utilisent **20** comme niveau clé.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Measuring Trend Strength) : L'ADX comporte un **retard (lag)** important à cause des lissages. Exemple Nordstrom (JWN) avec SMA 50j : la tendance forte a maintenu l'ADX au-dessus de 20 même lors du retournement haussier→baissier ; deux périodes sans tendance (formations de creux).

**TRADEX-AI C1** : Filtre de régime — signal de tendance valide seulement si **ADX > 25** (ou ≥ 20 selon calibrage). En dessous de 20 → marché en range → privilégier un système non-trend. *(Confirme la règle de filtrage évoquée en D49 MACD.)*

---

## BLOC 4 — SIGNAUX +DI / -DI (SYSTÈME WILDER)

### D69 — Système de Wilder : signal d'achat (image_05)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Identifying Trend Direction and +DI/-DI Trading Signals + image_05 · label certifié : Identifying Trend Direction and +DI/-DI Trading Signals [SECTION-FALLBACK] · exemple Medco Health Solutions) :

- **Pré-requis** : ADX au-dessus de **25** (beaucoup utilisent 20) → assure que les prix sont en tendance.
- **Signal d'achat** : +DI croise **au-dessus** de -DI.
- **Stop initial** : sur le **plus bas du jour du signal**. Le signal reste valide tant que ce plus bas tient, même si +DI repasse sous -DI. Attendre la pénétration de ce plus bas avant d'abandonner le signal.
- Signal renforcé si l'ADX remonte (tendance se renforce). Une fois le trade profitable → intégrer stop-loss et trailing stop.

**TRADEX-AI C3/gestion_risque_entree** : Croisement +DI > -DI + ADX > 20/25 = signal LONG candidat sur NQ/ES/Gold · stop initial = plus bas de la barre de signal.

---

### D70 — Système de Wilder : signal de vente et whipsaws (image_05)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Identifying Trend Direction and +DI/-DI Trading Signals · exemple Medco) :

- **Signal de vente** : -DI croise **au-dessus** de +DI. Stop initial = **plus haut du jour du signal de vente**.
- Les croisements +DI/-DI sont **fréquents** : certains se produisent avec ADX > 20 (signaux validés), d'autres l'invalident. Il y a des **whipsaws**, de bons et de mauvais signaux.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Identifying Trend Direction…) : La clé est d'intégrer d'autres aspects de l'analyse technique. Exemples cités : ignorer les signaux baissiers pendant un drapeau haussier (consolidation, sept. 2009) ; ignorer un signal d'achat trop près d'une zone de résistance (retracement 50-62 %, juin 2010).

**TRADEX-AI C3** : Filtrer les croisements +DI/-DI par le contexte prix (C1 : support/résistance, patterns) avant exécution — ne jamais trader le croisement seul.

---

### D71 — Confirmation par le seuil ADX : exemple AT&T (image_06)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Identifying Trend Direction and +DI/-DI Trading Signals + image_06 · label certifié : Identifying Trend Direction and +DI/-DI Trading Signals [SECTION-FALLBACK] · exemple AT&T (T)) : Trois signaux sur 12 mois, plutôt bons à condition de prendre les profits et d'utiliser des trailing stops (le Parabolic SAR de Wilder peut servir de trailing stop). **Aucun signal de vente** entre les achats de mars et juillet : parce que **l'ADX n'était pas au-dessus de 20** quand -DI a croisé au-dessus de +DI fin avril.

**TRADEX-AI C3** : Règle de filtrage confirmée — un croisement directionnel **sans ADX > 20** ne déclenche PAS de signal. Le seuil ADX agit comme gate sur la validité du croisement.

---

## BLOC 5 — LIMITES ET BONNES PRATIQUES

### D72 — The Bottom Line : filtrer les croisements directionnels

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §The Bottom Line) : Le calcul du Directional Movement System est complexe, mais l'interprétation est simple. Les croisements +DI/-DI sont **très fréquents** et doivent être filtrés par une analyse complémentaire. Exiger une condition ADX réduit les signaux, mais cet indicateur sur-lissé filtre autant de bons que de mauvais signaux.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §The Bottom Line) : Suggestion — mettre l'ADX au second plan et se concentrer sur +DI/-DI pour générer les signaux, puis chercher confirmation ailleurs : indicateurs de volume, analyse de tendance de base, **chart patterns**. Exemple : privilégier les achats +DI quand la tendance majeure est haussière · les ventes -DI quand elle est baissière.

**TRADEX-AI C1/C3** : Hiérarchie TRADEX — biais de tendance majeur (C1) → croisement +DI/-DI dans le sens du biais → confirmation volume/pattern. ADX = filtre de régime, pas générateur de signal seul.

---

## BLOC 6 — CONFIGURATION ET SCANS

### D73 — Configuration SharpCharts (images_07/08)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Using with SharpCharts + image_07 · label certifié Pattern A : Using ADX and supporting overlays on a SharpChart + image_08 · label certifié Pattern A : ADX settings on the SharpCharts Workbench, along with supporting overlays) : Sélectionner **ADX Line (w/+DI and -DI)** dans la liste des indicateurs (option ADX seule disponible aussi). Par défaut : ADX en noir, +DI en vert, -DI en rouge. Recommandé de tracer l'ADX au-dessus ou en dessous du prix (trois lignes). Une ligne horizontale aide à repérer les mouvements de l'ADX.

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Using with SharpCharts) : Exemple combinant SMA 50j (filtre : n'acheter qu'au-dessus de la SMA 50j) et Parabolic SAR (réglage des stops une fois le trade initié).

**TRADEX-AI C0** : Export NinjaScript en trois séries distinctes — `ADX`, `+DI`, `-DI` — pour filtrage indépendant en C1/C3.

---

### D74 — Configuration StockChartsACP (image_09)

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Using with StockChartsACP + image_09 · label certifié : Using with StockChartsACP [SECTION-FALLBACK]) : L'indicateur ADX (avec ou sans +DI/-DI) s'ajoute via le panneau Chart Settings ; il peut être positionné au-dessus, en dessous ou derrière le prix. Calcul par défaut sur **14 périodes**, paramètre ajustable.

**TRADEX-AI C0** : Confirme le réglage par défaut `14` — paramètre de référence pour l'export NinjaScript.

---

### D75 — Scan tendance haussière : +DI croise au-dessus de -DI

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Overall Uptrend with +DI Crossing above -DI) : Critères du scan StockCharts :

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily ADX Line(14) > 20]
AND [Daily Plus DI(14) crosses Daily Minus DI(14)]
AND [Daily Close > Daily SMA(50,Daily Close)]
```

Tendance haussière = au-dessus de la SMA 50j · achat possible quand ADX > 20 et +DI croise au-dessus de -DI.

**TRADEX-AI C3** : Transposable NQ/ES/Gold — LONG candidat = `ADX(14) > 20` ET `+DI croise au-dessus -DI` ET `clôture > SMA(50)`.

---

### D76 — Scan tendance baissière : -DI croise au-dessus de +DI

🟢 **FAIT VÉRIFIÉ** (Source : adx.md §Overall Downtrend with -DI Crossing above +DI) : Critères du scan StockCharts :

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily ADX Line(14) > 20]
AND [Daily Minus DI(14) crosses Daily Plus DI(14)]
AND [Daily Close < Daily SMA(50,Daily Close)]
```

Tendance baissière = sous la SMA 50j · vente possible quand ADX > 20 et -DI croise au-dessus de +DI.

**TRADEX-AI C3** : Transposable NQ/ES/Gold — SHORT candidat = `ADX(14) > 20` ET `-DI croise au-dessus +DI` ET `clôture < SMA(50)`.

---

### D77 — Synthèse opérationnelle ADX/DMI pour TRADEX

🟡 **CONVENTION** (synthèse des sections §Interpreting + §The Bottom Line, adx.md) : Ordre d'utilisation du système directionnel :

1. **ADX** → filtre de régime (tendance présente si > 20/25, absente si < 20).
2. **+DI vs -DI** → direction et signal (croisement dans le sens du biais majeur).
3. **Confirmation** → volume, structure prix, chart patterns.

**TRADEX-AI C1/C3** : ADX = porte d'entrée du régime de tendance dans la grille de score /10. Sans tendance confirmée (ADX < seuil), les signaux de croisement directionnel ne sont pas comptabilisés. Cohérent avec D49 (filtrer les croisements MACD centerline par ADX > 25).

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D62
Dernière décision session  : D77
Prochaine décision         : D78
Total décisions ADX        : 16
Total KB cumulé            : D1 → D77
```

---

*Extraction_StockCharts_ADX_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
