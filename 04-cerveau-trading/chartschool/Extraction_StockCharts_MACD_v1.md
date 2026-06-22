# Extraction_StockCharts_MACD_v1.md
**Source :** StockCharts ChartSchool — MACD (Moving Average Convergence/Divergence) Oscillator  
**URL :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator  
**Décisions :** D40 → D61  
**Images certifiées :** 11/11 (double ancrage v3 · section-fallback ARCH-15)  
**Date extraction :** 22/06/2026  

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — DÉFINITION ET ORIGINE

### D40 — MACD : définition et créateur

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §What Is the MACD) : Le MACD (Moving Average Convergence/Divergence) est un oscillateur de momentum développé par Gerald Appel à la fin des années 1970. Il transforme deux moyennes mobiles trend-following en oscillateur de momentum en soustrayant la MA longue de la MA courte.

🟡 **CONVENTION** : Le MACD combine les deux mondes — suivi de tendance ET momentum — dans un seul indicateur.

**TRADEX-AI C3** : Indicateur de confirmation multi-couche pour NQ/ES/Gold. Confirme la direction de tendance (C1) avant entrée.

---

### D41 — MACD : formule officielle

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §How Do You Calculate the MACD) :

```
Ligne MACD    = EMA(12) - EMA(26)
Ligne Signal  = EMA(9) de la Ligne MACD
Histogramme   = Ligne MACD - Ligne Signal
```

Les moyennes mobiles sont calculées sur les **prix de clôture**.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §How Do You Calculate the MACD) : Les paramètres standard sont **12, 26 et 9**. D'autres valeurs peuvent être substituées selon le style de trading.

**TRADEX-AI C0** : Paramètres à exporter depuis NinjaScript : `MACD(12, 26, 9)` sur clôtures. Trois séries : MACDLine, SignalLine, Histogram.

---

### D42 — MACD : composants et rôles

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §How Do You Calculate the MACD) :

- **Ligne MACD** : EMA 12j − EMA 26j. L'EMA 12j est plus rapide et responsable de la majorité des mouvements MACD.
- **Ligne Signal** : EMA 9j de la ligne MACD. Agit comme filtre pour identifier les retournements.
- **Histogramme MACD** : Différence entre ligne MACD et ligne Signal. Positif quand MACD > Signal · Négatif quand MACD < Signal.

**TRADEX-AI C3** : L'histogramme mesure l'accélération du momentum — signal d'alerte précoce avant le croisement des lignes.

---

## BLOC 2 — INTERPRÉTATION DU MACD

### D43 — MACD : convergence et divergence des MAs

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Convergence/Divergence) :

- **Convergence** : les deux MAs se rapprochent → momentum ralentit.
- **Divergence** : les deux MAs s'éloignent → momentum s'accélère.
- L'EMA 12j (rapide) est responsable de la majorité des mouvements MACD.
- L'EMA 26j (lente) est moins réactive aux variations de prix.

**TRADEX-AI C3** : Surveiller la vitesse de divergence sur NQ/ES — une divergence rapide indique une impulsion directionnelle forte.

---

### D44 — MACD : oscillateur et ligne zéro (image_02)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Oscillator + image_02 · label : StockCharts MACD interpretation) : La ligne MACD oscille au-dessus et en dessous de la **ligne zéro** (centerline).

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Oscillator) :
- **MACD positif** → EMA 12j > EMA 26j → momentum haussier croissant.
- **MACD négatif** → EMA 12j < EMA 26j → momentum baissier croissant.
- Plus les EMAs divergent, plus la valeur absolue du MACD augmente.

🟢 **FAIT VÉRIFIÉ** (Source : image_02 · label certifié : StockCharts MACD interpretation) : La zone dorée illustre le MACD en territoire négatif (EMA 12j < EMA 26j) · la zone rouge illustre les valeurs positives (EMA 12j > EMA 26j).

**TRADEX-AI C3** : Le signe du MACD (positif/négatif) filtre le biais directionnel — LONG seulement si MACD > 0 sur NQ/ES · SHORT seulement si MACD < 0.

---

### D45 — MACD : limites — pas d'overbought/oversold

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §What Is the MACD + §The Bottom Line) : Le MACD est **non borné** — il n'a pas de limites supérieure ou inférieure. Il n'est donc **pas** particulièrement utile pour identifier les niveaux de surachat/survente. Durant des mouvements brusques, le MACD peut continuer à s'étendre au-delà de ses extrêmes historiques.

🟡 **CONVENTION** : Pour comparer le momentum entre plusieurs actifs avec des prix différents, utiliser le **PPO (Percentage Price Oscillator)** plutôt que le MACD.

**TRADEX-AI C3** : Ne jamais utiliser le MACD seul pour définir un niveau d'entrée en survente/surachat. Toujours combiner avec RSI (borné 0–100) pour ce rôle (D18–D39).

---

## BLOC 3 — SIGNAUX MACD

### D46 — Signal Line Crossover : définition (image_03)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Signal Line Crossovers + image_03 · label : Signal Line Crossovers [SECTION-FALLBACK]) : Les croisements de ligne signal sont les signaux MACD **les plus fréquents**.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Signal Line Crossovers) :
- **Croisement haussier** : MACD monte et croise AU-DESSUS de la ligne Signal.
- **Croisement baissier** : MACD descend et croise EN DESSOUS de la ligne Signal.
- La durée d'un croisement varie de quelques jours à quelques semaines selon la force du mouvement.

**TRADEX-AI C3** : Croisement haussier = signal d'entrée LONG candidat · croisement baissier = signal d'entrée SHORT candidat. Toujours confirmer avec contexte prix (C1) et RSI (C3).

---

### D47 — Signal Line Crossover : précautions aux extrêmes

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Signal Line Crossovers) : Les croisements de ligne signal aux **extrêmes positifs ou négatifs** doivent être traités avec prudence. Un mouvement fort dans l'actif sous-jacent pousse le momentum à un extrême — même si le mouvement continue, le momentum ralentit et génère souvent un croisement aux extrémités. La volatilité de l'actif peut aussi augmenter le nombre de croisements (faux signaux).

**TRADEX-AI C3** : Sur NQ/ES/Gold — filtrer les croisements signal quand l'histogramme est à un extrême historique. Signal valide seulement si histogramme revient vers zéro depuis un niveau modéré.

---

### D48 — Centerline Crossover haussier et baissier (images_04/05/06)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Centerline Crossovers + images_04/05/06 · label : Centerline Crossovers [SECTION-FALLBACK]) :

- **Croisement centerline haussier** : MACD passe AU-DESSUS de zéro → EMA 12j vient de croiser AU-DESSUS EMA 26j.
- **Croisement centerline baissier** : MACD passe EN DESSOUS de zéro → EMA 12j vient de croiser EN DESSOUS EMA 26j.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Centerline Crossovers) : Les croisements centerline peuvent durer quelques jours ou quelques mois selon la force de la tendance. Le MACD reste positif tant qu'une tendance haussière soutenue est en place · négatif tant qu'une tendance baissière soutenue persiste.

**TRADEX-AI C1/C3** : Le passage du MACD au-dessus de zéro confirme un changement de biais directionnel — signal de tendance long terme sur NQ/ES/Gold. Plus fiable que le croisement signal pour les trades de tendance.

---

### D49 — Centerline Crossover : qualité selon contexte de tendance

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Centerline Crossovers) : Les croisements centerline fonctionnent bien quand une **tendance forte émerge** après le croisement (exemple : Pulte Homes PHM, 4 croisements en 9 mois avec tendances fortes). En revanche, sans tendance forte, ils génèrent de nombreux **whipsaws** (exemple : Cummins CMI, 7 croisements en 5 mois sans tendances claires). Un signal centerline peut durer jusqu'à 10 mois dans une tendance forte (exemple 3M MMM).

**TRADEX-AI C1** : Filtrer les croisements centerline MACD avec ADX > 25 pour confirmer la présence d'une tendance avant de trader le signal.

---

## BLOC 4 — DIVERGENCES MACD

### D50 — Divergence haussière MACD : définition

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Une **divergence haussière** se forme quand l'actif enregistre un **plus bas inférieur** ET que le MACD forme un **plus bas supérieur**.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Le plus bas inférieur de l'actif confirme la tendance baissière en cours, MAIS le plus bas supérieur du MACD indique une réduction du momentum baissier. Tant que le MACD reste en territoire négatif, le momentum baissier domine encore — c'est un signal d'alerte précoce, pas de renversement confirmé.

**TRADEX-AI C3** : Divergence haussière MACD sur NQ/ES/Gold = signal de vigilance pour réduction d'exposition SHORT ou préparation d'entrée LONG — jamais signal d'entrée seul.

---

### D51 — Divergence haussière MACD : exemple Google (image_07)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences + image_07 · label : Divergences [SECTION-FALLBACK]) : Exemple Google (GOOG) octobre-novembre 2008 : Google forme un plus bas inférieur en novembre · le MACD forme un plus bas supérieur → divergence haussière. Le MACD remonte avec un croisement signal en décembre · Google confirme le retournement avec un breakout de résistance.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Les divergences MACD utilisent les **prix de clôture** (pas les intraday highs/lows) pour l'identification.

**TRADEX-AI C3** : Sur Gold — les divergences haussières MACD en fin de tendance baissière sont des alertes de retournement à surveiller, confirmées par breakout de résistance.

---

### D52 — Divergence baissière MACD : définition

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Une **divergence baissière** se forme quand l'actif enregistre un **plus haut supérieur** ET que le MACD forme un **plus haut inférieur**.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Le plus haut supérieur de l'actif est normal dans une tendance haussière, MAIS le plus haut inférieur du MACD indique une réduction du momentum haussier. Tant que le MACD reste positif, le momentum haussier domine encore malgré son affaiblissement.

**TRADEX-AI C3** : Divergence baissière MACD = momentum s'essouffle → réduire exposition LONG ou préparer entrée SHORT — jamais signal d'entrée seul.

---

### D53 — Divergence baissière MACD : exemple GameStop (image_08)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences + image_08 · label : Divergences [SECTION-FALLBACK]) : Exemple GameStop (GME) août-octobre : GME forge un plus haut au-dessus de 28 · le MACD forme un plus haut inférieur → divergence baissière. Le croisement signal baissier suivant et le cassage de support MACD confirment. Le support cassé devient résistance sur le rebond de novembre (ligne rouge pointillée) — deuxième opportunité de vente.

**TRADEX-AI C3** : Le support cassé qui devient résistance est un pattern de confirmation post-divergence applicable sur NQ/ES/Gold.

---

### D54 — Divergences MACD : mise en garde critique

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) : Les divergences doivent être traitées avec **prudence**.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences) :
- Les **divergences baissières sont fréquentes dans les tendances haussières fortes** — elles n'indiquent pas nécessairement un retournement.
- Les **divergences haussières sont fréquentes dans les tendances baissières fortes** — idem.
- Une tendance forte débute souvent par une avancée puissante qui génère un pic de momentum MACD. Même si la tendance continue à un rythme plus lent, le MACD décline depuis ses sommets → divergence mécanique, pas de signal de retournement.

**TRADEX-AI C3** : Ne jamais trader une divergence MACD seule. Exiger confirmation : croisement signal + contexte prix (support/résistance) + volume.

---

### D55 — Divergences baissières multiples en tendance haussière forte (image_09)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Divergences + image_09 · label : Divergences [SECTION-FALLBACK]) : Exemple S&P 500 ETF (SPY) août-novembre 2009 — quatre divergences baissières successives, mais le SPY continue de monter car la tendance haussière est forte. Le MACD reste positif malgré son déclin → momentum haussier toujours dominant. Leçon : momentum positif = momentum haussier > baissier, même si en déclin.

**TRADEX-AI C3** : Sur ES — des divergences baissières MACD multiples en tendance haussière forte (MACD > 0) ne justifient PAS un SHORT. Attendre passage MACD sous zéro.

---

## BLOC 5 — PARAMÈTRES ET CONFIGURATIONS

### D56 — MACD : sensibilité et paramètres alternatifs

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §The Bottom Line) :
- **Plus sensible** : raccourcir l'EMA courte ET allonger l'EMA longue. Exemple : `MACD(5, 35, 5)` — mieux adapté aux graphiques hebdomadaires.
- **Moins sensible** : allonger les deux EMAs → croisements centerline et signal moins fréquents.
- Le MACD standard `(12, 26, 9)` est calibré pour les graphiques **journaliers**.

**TRADEX-AI C0** : Pour NQ/ES/Gold sur timeframe journalier → `MACD(12, 26, 9)` standard. Pour timeframe hebdomadaire → tester `MACD(5, 35, 5)`.

---

### D57 — MACD : dépendance au prix absolu de l'actif

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §The Bottom Line) : Les valeurs MACD dépendent du **prix absolu** de l'actif sous-jacent. Exemple : un actif à 20$ aura des valeurs MACD entre -1,5 et +1,5 · un actif à 100$ aura des valeurs entre -10 et +10. Il est **impossible de comparer** les valeurs MACD entre actifs de prix différents.

🟡 **CONVENTION** : Pour comparer le momentum entre actifs, utiliser le **PPO (Percentage Price Oscillator)** — exprimé en pourcentage, comparable entre actifs.

**TRADEX-AI C3** : Sur TRADEX — NQ (~20 000 pts), ES (~5 000 pts), Gold (~3 000 $/oz) ont des valeurs MACD absolues très différentes. Ne jamais comparer directement les niveaux MACD entre ces trois actifs.

---

## BLOC 6 — CONFIGURATION SHARPCHARTS

### D58 — MACD : configuration plateforme (images_10/11)

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Using MACD With SharpCharts + images_10/11 · label : Using MACD With SharpCharts [SECTION-FALLBACK]) : Le MACD peut être positionné au-dessus, en dessous ou derrière le graphique prix. Le positionnement **"derrière"** le prix facilite la comparaison visuelle momentum/prix. Paramètres par défaut à l'activation : `(12, 26, 9)`.

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §Using MACD With SharpCharts) : Pour supprimer l'histogramme et la ligne signal → paramétrer `(12, 26, 1)` ou `(12, 26)`. Pour ajouter une ligne signal séparée sans histogramme → utiliser "Exp. Moving Avg" dans les options avancées.

**TRADEX-AI C0** : Sur NinjaScript — exporter séparément : `MACDLine`, `SignalLine`, `MACDHistogram` comme trois séries distinctes pour permettre le filtrage indépendant en C3.

---

## BLOC 7 — SIGNAUX SCAN ET FAQ

### D59 — MACD : scan bullish signal line cross

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §MACD Bullish Signal Line Cross) : Critères du scan StockCharts pour croisement signal haussier :
- Prix > SMA(200) — tendance haussière confirmée
- Jour précédent : MACD < Signal
- Jour actuel : MACD > Signal (croisement haussier)
- MACD < 0 — le retournement se produit après un pullback

**TRADEX-AI C3** : Logique applicable sur NQ/ES/Gold : croisement signal haussier AVEC MACD négatif = signal de pullback dans tendance haussière — qualité supérieure au croisement en territoire positif.

---

### D60 — MACD : scan bearish signal line cross

🟢 **FAIT VÉRIFIÉ** (Source : macd.md §MACD Bearish Signal Line Cross) : Critères du scan StockCharts pour croisement signal baissier :
- Prix < SMA(200) — tendance baissière confirmée
- Jour précédent : MACD > Signal
- Jour actuel : MACD < Signal (croisement baissier)
- MACD > 0 — le retournement se produit après un rebond

**TRADEX-AI C3** : Sur NQ/ES/Gold : croisement signal baissier AVEC MACD positif = signal de rebond dans tendance baissière — qualité supérieure au croisement en territoire négatif.

---

### D61 — MACD : résumé des trois signaux principaux

🟡 **CONVENTION** (Source : macd.md §What does the MACD indicate) : Les trois familles de signaux MACD par ordre de fréquence :

1. **Croisements de ligne signal** — les plus fréquents · signaux tactiques
2. **Croisements de centerline (zéro)** — moins fréquents · signaux de tendance
3. **Divergences prix/MACD** — les plus rares · signaux de retournement potentiel

**TRADEX-AI C3** : Hiérarchie d'utilisation TRADEX — centerline (biais directionnel C1) → signal line (entrée C3) → divergence (alerte retournement C3). Jamais utiliser seul.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D40
Dernière décision session  : D61
Prochaine décision         : D62
Total décisions MACD       : 22
Total KB cumulé            : D1 → D61
```

---

*Extraction_StockCharts_MACD_v1.md · TRADEX-AI · 22/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
