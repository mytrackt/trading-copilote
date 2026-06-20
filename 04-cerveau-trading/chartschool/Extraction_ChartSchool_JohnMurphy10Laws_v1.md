# Extraction KB — ChartSchool : John Murphy's 10 Laws of Technical Trading
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/john-murphys-10-laws-of-technical-trading  
**Version :** v1 complète (texte intégral récupéré + annotations TRADEX)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Auteur :** John Murphy — Chief Technical Analyst StockCharts.com  
**Référence livres :** *Technical Analysis of the Financial Markets* · *Trading with Intermarket Analysis* · *The Visual Investor*  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Pertinence TRADEX :** 🔴 MAXIMALE — Ces 10 lois sont le socle philosophique de l'analyse technique. Chaque loi a une application directe dans l'architecture TRADEX v2.  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur chart/source officielle |
| 🔵 | Règle citée par John Murphy — auteur reconnu |
| 🟡 | Interprétation appliquée à TRADEX |
| ⏳ | À vérifier / implémenter |
| 🔴 | Risqué si mal appliqué |

---

## CONTEXTE AUTEUR

🔵 **John Murphy :** ancien analyste technique CNBC-TV (7 ans, émission "Tech Talk"), 30 ans d'expérience, auteur de 3 best-sellers en analyse technique. Ces 10 lois sont issues de questions reçues après des conférences publiques — elles répondent aux erreurs les plus fréquentes des traders débutants et intermédiaires.

🔵 **Principe central de Murphy :** *"Il est plus important de déterminer où va un marché (haut ou bas) que la raison derrière sa direction."* → Priorité absolue au prix et au graphique, pas aux fondamentaux.

---

## LOI 1 — MAP THE TRENDS (Cartographier les tendances)

🔵 **Règle :** Étudier d'abord les graphiques **mensuels et hebdomadaires** (plusieurs années). Établir la perspective long terme AVANT de consulter les graphiques journaliers et intraday.

🔵 **Citation Murphy :** *"A short-term market view alone can often be deceptive. Even if you only trade the short term, you will do better if you're trading in the same direction as the intermediate- and longer-term trends."*

🟡 **Application TRADEX :**
- Avant tout signal COG Belkhayate sur futures : vérifier le **Weekly** → direction primaire
- Puis Daily → direction intermédiaire
- Puis intraday (5-15 min) → timing d'entrée
- Signal COG contre la tendance Weekly = confiance réduite automatiquement dans Couche 4

⏳ **À implémenter :** Couche 0 NinjaScript exporte OHLCV. La Couche 1 doit calculer la tendance sur 3 timeframes (Weekly/Daily/Intraday) et les comparer avant de valider un signal.

---

## LOI 2 — SPOT THE TREND AND GO WITH IT (Suivre la tendance)

🔵 **Règle :** Déterminer la tendance et la suivre. Ne jamais trader contre elle.
- Tendance haussière → **acheter les replis (buy the dips)**
- Tendance baissière → **vendre les rebonds (sell the rallies)**

🔵 **Sélection du timeframe de trading :**
- Trading intermédiaire → graphiques **Daily et Weekly**
- Day trading → graphiques **Daily et intraday**
- Le graphique long terme définit la direction, le court terme affine le timing

🟡 **Application TRADEX :**
- Un signal COG long dans une tendance **Weekly haussière** = biais confirmé → score augmenté
- Un signal COG long dans une tendance **Weekly baissière** = contra-tendance → score réduit ou NO_TRADE
- "Buy the dip" = signal COG au creux d'un repli dans un uptrend = setup idéal TRADEX

---

## LOI 3 — FIND THE LOW AND HIGH OF IT (Support et Résistance)

🔵 **Règle Support :** Le meilleur endroit pour acheter = **près des niveaux de support** (souvent un creux précédent).

🔵 **Règle Résistance :** Le meilleur endroit pour vendre = **près des niveaux de résistance** (souvent un sommet précédent).

🔵 **Règle d'inversion Support/Résistance (CRITIQUE) :**
- Une **résistance cassée** → devient du **support** sur les pullbacks futurs (l'ancien "haut" devient le nouveau "bas")
- Un **support cassé** → devient de la **résistance** sur les rebonds futurs (l'ancien "bas" devient le nouveau "haut")

🟡 **Application TRADEX :**
- Le COG Belkhayate est lui-même un niveau de support/résistance dynamique
- La Loi 3 justifie l'utilisation des niveaux COG passés comme zones de réaction futures
- Couche 4 (vision Claude) doit identifier les S/R statiques majeurs sur le chart ET les comparer au COG actuel

⏳ À coder : dans Couche 2 (détection algo Python), identifier les S/R statiques des dernières 20 bougies et les intégrer dans le scoring.

---

## LOI 4 — KNOW HOW FAR TO BACKTRACK (Retracements)

🔵 **Règle des retracements :**
- **Retracement le plus fréquent : 50%** d'un mouvement précédent
- **Minimum de retracement : 33%** (un tiers)
- **Maximum de retracement : 67%** (deux tiers)
- **Niveaux Fibonacci : 38% et 62%** → zones de surveillance prioritaires

🔵 **Application pratique :** dans un uptrend, les zones d'achat initiales sont situées dans la zone de **retracement 33-38%** du mouvement précédent.

🔵 **Référence Fibonacci (note Murphy) :** Leonardo Fibonacci, mathématicien du XIIIe siècle, suite : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144... → après les 4 premiers, le ratio d'un nombre sur le suivant tend vers **0.618** ("Golden Mean"). Ratio inversé = **0.382** (1 - 0.618).

🟡 **Application TRADEX :**
- Le COG Belkhayate agit souvent comme niveau de retracement naturel (centre de gravité du mouvement)
- Un signal COG qui coïncide avec un niveau Fibonacci 38% ou 62% = **confluence forte**
- Couche 2 (algo Python) doit calculer les retracements Fibonacci depuis le dernier swing high/low

⏳ Niveaux à calculer automatiquement : 38.2%, 50%, 61.8% du dernier mouvement directionnel identifié.

---

## LOI 5 — DRAW THE LINE (Lignes de tendance)

🔵 **Règle :** Les trendlines sont l'outil graphique le plus simple et le plus efficace. Deux points suffisent pour les tracer.
- **Uptrend line :** tracée sous deux creux successifs **croissants**
- **Downtrend line :** tracée au-dessus de deux sommets successifs **décroissants**

🔵 **Règles de validité d'une trendline :**
- **Minimum 3 touches** pour être considérée valide
- Plus elle est ancienne et testée fréquemment, plus elle est **critique**
- La rupture d'une trendline = **signal de changement de tendance**
- Les prix reviennent souvent sur la trendline avant de reprendre la tendance (pullback sur la ligne)

🟡 **Application TRADEX :**
- La Couche 4 (vision Claude) doit identifier les trendlines majeures sur le chart soumis
- Un signal COG qui coïncide avec un rebond sur une trendline valide = confluence forte
- La rupture d'une trendline par le prix avant le signal = contexte dégradé

⏳ La détection automatique de trendlines peut être ajoutée à la Couche 2 (algo Python) via régression linéaire sur les pivots hauts/bas.

---

## LOI 6 — FOLLOW THAT AVERAGE (Moyennes Mobiles)

🔵 **Règle :** Les moyennes mobiles (MA) fournissent des **signaux objectifs d'achat et de vente**. Elles confirment si la tendance existante est toujours en mouvement.

🔵 **Les 3 MA les plus importantes en trading d'actions :**
- **MA 20 jours** → tendance court terme
- **MA 50 jours** → tendance intermédiaire
- **MA 200 jours** → tendance majeure (long terme)

🔵 **Combinaisons de croisements MA (trending signals) :**
- 5-20 jours → court terme
- 20-50 jours → intermédiaire
- **50-200 jours → long terme (Golden Cross / Death Cross)**

🔵 **EMA recommandées** pour les croisements (Exponential Moving Average) : plus réactives que les MA simples car pondèrent davantage les données récentes.

🔵 **Limite des MA :** elles ne prédisent pas un changement de tendance à l'avance — elles le **confirment après**. Elles sont des indicateurs retardés (lagging).

🟡 **Application TRADEX :**
- La Couche 0 exporte déjà l'ADX. Ajouter MA 20/50/200 sur Daily dans NinjaScript
- Signal COG au-dessus de MA(50) Daily = contexte haussier confirmé
- Signal COG en-dessous de MA(200) Daily = tendance majeure baissière → prudence maximale

⏳ Paramètres à tester sur Gold Futures (GC) : MA(20)/MA(50) sur Daily comme filtres de tendance intermédiaire.

---

## LOI 7 — LEARN THE TURNS (Oscillateurs)

🔵 **Règle :** Les oscillateurs identifient les marchés **surachetés (overbought)** et **survendus (oversold)**. Ils avertissent souvent qu'un marché a été poussé trop loin et va bientôt se retourner.

🔵 **RSI (Relative Strength Index) — paramètres Murphy :**
- Période : **9 ou 14 jours/semaines**
- Suracheté : **> 70** → signal de prudence côté long
- Survendu : **< 30** → opportunité côté long potentielle
- **Divergence RSI / Prix = signal fort de retournement** (prix fait nouveau high, RSI non → bearish divergence)

🔵 **Stochastics Oscillator — paramètres Murphy :**
- Période : **14 jours/semaines**
- Suracheté : **> 80**
- Survendu : **< 20**

🔵 **Règles d'usage des oscillateurs :**
- Fonctionnent **mieux en marché range/trading** (pas en forte tendance)
- Signaux Weekly filtrent les signaux Daily
- Signaux Daily filtrent les signaux intraday

🔵 **Divergence oscillateur/prix = signe d'alerte :**
- Prix fait nouveau sommet → oscillateur fait sommet inférieur = **bearish divergence** → retournement probable
- Prix fait nouveau creux → oscillateur fait creux supérieur = **bullish divergence** → retournement probable

🟡 **Application TRADEX :**
- La Couche 0 exporte ADX. Ajouter RSI(14) dans les données NinjaScript
- RSI > 70 au moment du signal COG long = suracheté → réduire score ou filtrer
- Divergence RSI/prix sur le chart = signal fort à inclure dans l'analyse Couche 4 (vision Claude)

⏳ À inclure dans Couche 2 : calcul RSI(14) sur OHLCV reçus, détection divergences sur N dernières bougies.

---

## LOI 8 — KNOW THE WARNING SIGNS (MACD)

🔵 **Règle :** Le MACD combine un système de croisement de moyennes mobiles avec les éléments surachat/survendu d'un oscillateur.

🔵 **MACD — développé par Gerald Appel. Paramètres standard : (12, 26, 9)**

🔵 **Signaux d'achat/vente MACD (Murphy) :**
- **BUY signal :** la ligne rapide croise **au-dessus** de la ligne lente ET les deux lignes sont **sous zéro**
- **SELL signal :** la ligne rapide croise **en-dessous** de la ligne lente ET les deux lignes sont **au-dessus de zéro**

🔵 **Règle de priorité :** les signaux **Weekly priment sur les signaux Daily**.

🔵 **MACD Histogram :**
- Représente la différence entre la ligne MACD et la ligne signal
- Barre positive = MACD au-dessus de signal (momentum haussier)
- Barre négative = MACD sous signal (momentum baissier)
- **Changement de signe du histogram = premier avertissement précoce de changement de tendance**

🟡 **Application TRADEX :**
- MACD(12,26,9) Daily sur le sous-jacent = filtre de momentum
- Signal COG long + MACD histogram positif et croissant = confluence forte
- Signal COG long + MACD histogram négatif = signal contre le momentum → score réduit

⏳ Ajouter MACD à la Couche 0 NinjaScript pour export dans le flux de données.

---

## LOI 9 — TREND OR NOT A TREND (ADX)

🔵 **Règle :** L'ADX (Average Directional Movement Index) détermine si le marché est en phase de **tendance** ou de **trading range**.

🔵 **Interprétation ADX (Murphy) :**
- **ADX en hausse → tendance forte** (utiliser les moyennes mobiles / trend-following)
- **ADX en baisse → range / absence de tendance** (utiliser les oscillateurs)

🔵 **Règle d'usage conditionnel :**
- ADX montant → favoriser les MA et les stratégies de suivi de tendance
- ADX descendant → favoriser RSI/Stochastics et les stratégies de retour à la moyenne

🔴 **CRITIQUE POUR TRADEX :** cette loi justifie directement le détecteur de régime de l'architecture v2. **L'ADX est déjà planifié dans la Couche 0 NinjaScript.** C'est la validation par Murphy lui-même de ce choix architectural.

🟡 **Seuils recommandés (Murphy implicites, à confirmer) :**
- ADX > 25 = tendance présente → signal COG valide
- ADX < 20 = range → signal COG risqué, réduire le score ou NO_TRADE
- ADX entre 20-25 = zone grise ⏳

⏳ À définir dans Couche 1 : seuil ADX exact pour validation/rejet de signal TRADEX. Murphy ne donne pas de chiffre précis — utiliser les seuils standards du marché (20/25).

---

## LOI 10 — KNOW THE CONFIRMING SIGNS (Volume)

🔵 **Règle :** Le volume est un indicateur de confirmation **essentiel**.

🔵 **Citation Murphy :** *"Volume precedes price."* — **Le volume précède le prix.**

🔵 **Règles volume/tendance :**
- En **uptrend** : volume **plus élevé les jours haussiers** → confirm que de nouveaux capitaux soutiennent la tendance
- Volume **décroissant** en tendance = signe d'alerte que la tendance approche de sa fin
- Un uptrend solide **doit toujours** être accompagné d'un volume croissant

🔵 **Signaux d'alerte volume :**
- Prix monte mais volume baisse = **uptrend faible**, risque de retournement
- Pic de volume sur une bougie de retournement = **signal fort** de changement de tendance
- Volume élevé sur un breakout = **validation du breakout**

🟡 **Application TRADEX :**
- La Couche 0 exporte le Volume → déjà prévu
- Signal COG long + volume croissant sur les bougies haussières = confluence confirmée
- Signal COG long + volume décroissant = signal faible → score réduit

⏳ À coder dans Couche 2 : ratio Volume(bougie actuelle) / Volume(moyenne N bougies précédentes). Si ratio > 1.5 sur bougie directionnelle = confirmation volume.

---

## LOI "11" — KEEP AT IT (Amélioration continue)

🔵 **Citation Murphy :** *"Technical analysis is a skill that improves with experience and study. Always be a student and keep learning."*

🟡 **Application TRADEX :** le système TRADEX lui-même doit évoluer. Les extractions KB, les backtests, les corrections de paramètres = application de cette loi "11" au système IA.

---

## SYNTHÈSE — 10 LOIS MAPPÉES SUR L'ARCHITECTURE TRADEX v2

| Loi Murphy | Couche TRADEX | Statut |
|------------|--------------|--------|
| L1 — Multi-timeframe (Monthly→Daily→Intraday) | Couche 1 (ingestion) | ⏳ À implémenter |
| L2 — Suivre la tendance (biais directionnel) | Couche 1 + Couche 4 | ⏳ Filtre tendance |
| L3 — Support / Résistance | Couche 2 (algo) + Couche 4 (vision) | ⏳ |
| L4 — Retracements Fibonacci (33/38/50/62/67%) | Couche 2 (algo) | ⏳ |
| L5 — Trendlines (3 touches minimum) | Couche 4 (vision Claude) | ⏳ |
| L6 — Moving Averages (20/50/200j) | Couche 0 (NinjaScript) + Couche 1 | ⏳ Ajouter MA |
| L7 — Oscillateurs RSI(14) / Stochastics | Couche 2 (algo) | ⏳ Ajouter RSI |
| L8 — MACD(12,26,9) | Couche 0 + Couche 2 | ⏳ Ajouter MACD |
| L9 — ADX (tendance vs range) | Couche 0 (NinjaScript) | ✅ DÉJÀ PRÉVU |
| L10 — Volume (volume précède le prix) | Couche 0 (NinjaScript) | ✅ DÉJÀ PRÉVU |

**Couche 0 à compléter :** ajouter MA(20/50/200), MACD(12,26,9), RSI(14) aux exports NinjaScript en plus des données OHLCV + COG + ADX déjà prévus.

---

## TABLEAU DE RÉFÉRENCE RAPIDE — PARAMÈTRES MURPHY

| Indicateur | Paramètre | Seuil haussier | Seuil baissier |
|------------|-----------|---------------|----------------|
| RSI | 9 ou 14 périodes | > 70 = suracheté | < 30 = survendu |
| Stochastics | 14 périodes | > 80 = suracheté | < 20 = survendu |
| MACD | (12, 26, 9) | Rapide > Lente + sous 0 | Rapide < Lente + dessus 0 |
| ADX | Standard | Montant = tendance | Descendant = range |
| MA court terme | 20 jours | Prix > MA = haussier | Prix < MA = baissier |
| MA intermédiaire | 50 jours | Prix > MA = haussier | Prix < MA = baissier |
| MA long terme | 200 jours | Prix > MA = bull market | Prix < MA = bear market |
| Fibonacci | — | 38% / 50% / 62% | Retracements clés |
| Volume | — | Croissant en hausse | Décroissant en hausse = alerte |

---

*Fin d'extraction — John Murphy's 10 Laws of Technical Trading — v1 complète (texte intégral + annotations TRADEX)*  
*Source officielle : StockCharts.com ChartSchool. Auteur : John Murphy.*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
