# Extraction TA 101 — Fichier 2/3 : Structure de marché & price action
## TRADEX-AI · Ressource externe · Source : StockCharts ChartSchool « Technical Analysis 101 »

> **Source :** série « Technical Analysis 101 », StockCharts ChartSchool.
> **Couverture de ce fichier :** Parties 7, 8, 9, 10, 11, 12, 13 (support/résistance, tendances, channels, volume, patterns).
> **Statut global :** 🔵 ÉCOLE.
>
> **Tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ · ⚫ PROPRIÉTAIRE
> **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## A. SUPPORT ET RÉSISTANCE — mécanisme psychologique (Partie 7)

🟢 **Support :** niveau de prix où des acheteurs "avides" (greedy) entrent pour empêcher le prix de baisser davantage. Peut être un prix précis ou, plus souvent, une **zone de prix**. Peut durer plusieurs mois.

🟢 **Résistance :** niveau où des vendeurs "craintifs" (fearful) entrent et empêchent le prix de monter davantage. Même logique de zone.

🟢 **Mécanisme du role-reversal (psychologie expliquée) :**
- Après cassure d'un support → il devient résistance. Les traders qui ont acheté dans la zone de support sont maintenant en perte et veulent **vendre dès que le prix revient à leur prix d'achat** (pour rentrer dans leurs fonds).
- Après cassure d'une résistance → elle devient support. Les vendeurs qui ont vendu dans la zone de résistance **regrettent** et veulent racheter dès que le prix revient à leur niveau de vente.

→ **TRADEX :** ⭐ **explication psychologique du role-reversal** (déjà extrait de Murphy). L'outil **Volume by Price** (volume échangé par tranche de prix) permet d'identifier les zones où beaucoup de positions ont été prises = futurs S/R puissants. Concept proche du POC Market Profile (Chap. 6 §6.5) et des niveaux COG. 🟢 mécanisme / 🔵 application.

🟢 **S/R = zone, pas ligne précise.** Confirme que les bandes COG sont des **zones** de réaction, pas des niveaux exacts.

---

## B. TENDANCES ET TRENDLINES (Partie 8)

🟢 **Trend = mouvement directionnel soutenu.** Peut être vu comme une "**zone de support/résistance inclinée**". Continue tant que fear ou greed domine ; change quand l'équilibre fear/greed change.

🟢 **Définition structurelle (confirme Chap. 6 §6.1.3) :**
- Uptrend = pics et creux montants (HH/HL)
- Downtrend = pics et creux descendants (LH/LL)
- Trading range = pics et creux horizontaux

🟢 **Classification des tendances (différente de Murphy — noter la divergence) :**
- Majeure : > 6 mois
- Intermédiaire : 1 à 6 mois
- Mineure : < 1 mois

⚠️ **Note de cohérence :** Murphy (Charting Made Easy) donnait majeure > 1 an, secondaire 1-3 mois, mineure < quelques semaines. TA 101 donne des bornes différentes. → **Conclusion : ces bornes sont des CONVENTIONS variables selon les auteurs (🟡), pas des faits.** Pour TRADEX, définir ses propres bornes selon le TF tradé et les fixer avant backtest. Ne jamais traiter ces durées comme 🟢.

🟢 **Trendline :** ligne reliant 2+ points de prix bas (uptrend, agit comme support) ou hauts (downtrend, agit comme résistance). Les 2 premiers points établissent la ligne, les points additionnels la **valident**. Cassure de la trendline = changement de tendance possible.

→ **TRADEX :** confirme la règle des 3 touches (Murphy) — 2 points établissent, le 3e valide. 🟡

---

## C. PRICE CHANNELS ET CHANGEMENTS DE TENDANCE (Partie 9)

🟢 **Price channel :** prix borné par 2 trendlines parallèles. Signaux de faiblesse :
- En uptrend, si le prix **ne touche plus la ligne supérieure** du canal → l'uptrend faiblit, possible retournement.
- Si le prix **casse au-dessus** de la ligne supérieure → soit épuisement et retournement, soit nouvelle tendance plus raide.

→ **TRADEX :** ⭐ point exploitable. Le **non-touché de la borne du canal** = signal avancé de faiblesse de tendance. Transposable aux bandes COG : si en tendance le prix ne touche plus la bande externe dans le sens du mouvement, la tendance faiblit. 🔵 à backtester.

🟢 **Changements de tendance (confirme Chap. 6 §6.1.3 — BoS) :**
Un prix en tendance ne peut aller que dans 3 directions : continuer, passer en range, ou se retourner.
- Changement d'uptrend = un nouveau pic similaire ou **inférieur** au pic précédent. **Confirmé** quand le creux suivant est similaire ou inférieur au dernier creux.
- Logique identique pour downtrends et ranges.

→ **TRADEX :** ⭐ **définition mécanique du changement de tendance** = Break of Structure (Chap. 6). Confirme et précise : il faut un pic ET un creux pour confirmer, pas juste un pic. Critère objectif intégrable. 🟢

🟢 **Ajustement données dividendes :** sur StockCharts, préfixe underscore (_TSLA) pour données non ajustées, ou décocher "Adjust For Dividends". Les analystes utilisent généralement les **données ajustées**. → Confirme l'hypothèse #2 (Fichier 1) : données back-adjusted nécessaires. 🟢

---

## D. CONFIRMATION PAR LE VOLUME (Partie 10) ⭐

🟢 **Règle de confirmation volume (confirme Chap. 6 VSA + Murphy Loi 10) :**
- **Uptrend sain :** volume **s'étend** quand le prix monte, **se contracte** sur les replis.
- **Downtrend sain :** volume s'étend quand le prix baisse, se contracte sur les rebonds.

🟢 **Divergences volume = signaux avancés :**
- **Divergence négative :** nouveaux plus hauts en uptrend sur **volume déclinant** → pression acheteuse diminuant. Si le volume augmente sur les replis → possible consolidation ou retournement baissier.
- **Divergence positive :** nouveaux plus bas en downtrend sur volume contractant, mais volume s'étendant sur les rebonds → possible retournement haussier.

→ **TRADEX :** ⭐ confirme directement le rôle du volume (Chap. 6, Chap. 8 critère volume). La **divergence prix/volume** est un signal exploitable et calculable (recoupe l'OBV extrait de Murphy + le VSA). Candidat solide pour le scoring. 🟢 principe / 🔵 paramétrage du seuil.

---

## E. PATTERNS DE CONTINUATION (Parties 11-12)

🟢 **Nature des patterns :** "restes visuels d'une bataille entre bulls et bears". La plupart des patterns sont des **combinaisons de trendlines**. ⚠️ Les patterns indiquent **souvent mais pas toujours** les mouvements futurs (analogie météo).

### Rectangle Pattern
🟢 Prix entre 2 lignes horizontales S/R. Chaque ligne doit être touchée **au moins 2 fois**. Dure de jours à mois. Se termine à la cassure d'une ligne.
🟢 **Anticipation de cassure haussière :** volume s'étend quand le prix monte et se contracte quand il baisse dans le rectangle ; ou si le prix ne redescend pas au support avant de remonter.
🟢 **Plus le prix reste longtemps dans le pattern, plus le breakout sera grand** et la nouvelle ligne S/R significative.

### Triangle Pattern (= "coil")
🟢 Comme le rectangle mais avec lignes inclinées :
- **Triangle descendant :** résistance inclinée vers le bas, support horizontal → sentiment baissier croissant → casse souvent vers le bas.
- **Triangle ascendant :** support incliné vers le haut, résistance horizontale → sentiment haussier croissant → casse souvent vers le haut.
- **Triangle symétrique :** les 2 lignes inclinées → la "bataille" s'intensifie comme un ressort.

🟢 **Indices de direction du breakout :**
- La tendance **précédant** le triangle indique souvent la direction (continuation).
- Triangles ascendants → cassent souvent vers le haut ; descendants → vers le bas.
- Triangle symétrique souvent pas vraiment symétrique : casse dans la direction où il "pointe".
- Le breakout survient généralement **avant l'apex**.

🟢 **Confirmation volume (Partie 12) :** volume **décroissant** pendant la formation du pattern (rectangle ou triangle), puis **pic de volume** au breakout. Exemple réel : les mini-pics de volume pendant le coil doivent être **chacun plus petit que le précédent** ; un gros pic au-dessus de cette tendance décroissante signale le breakout.

→ **TRADEX :** confirme les patterns de continuation (Chap. 8 §8.2). Le critère **"chaque mini-pic de volume plus petit que le précédent"** est une précision utile pour valider un coil. 🟡 convention / 🔵 à backtester sur futures.

🟢 **Distinction continuation vs reversal :** rectangles et triangles = **patterns de consolidation/continuation** (le prix reprend généralement la tendance préalable). Ce sont des "escarmouches" ; les patterns de retournement sont les "grandes batailles".

---

## F. PATTERNS DE RETOURNEMENT — Head & Shoulders (Partie 13) ⭐

🟢 **H&S top :** 3 pics successifs, le central (tête) plus haut, les 2 externes (épaules) plus bas. Les creux de réaction reliés forment la **neckline**. Pattern complété quand le prix **clôture sous la neckline**.

🟢 **Psychologie temps réel (précision utile) :** jusqu'au moment où le prix repasse sous le niveau de l'épaule gauche, **ça ressemble à un uptrend normal**. Ce n'est qu'à la violation du niveau de l'épaule gauche que les bulls deviennent craintifs. L'épaule droite se forme quand les bulls tentent de rétablir l'uptrend et **échouent**.

🟢 **Confirmation volume :** le volume d'achat (jours up) se transforme progressivement en volume de vente (jours down) à mesure que le pattern se développe.

🟢 **Cible de projection :** à la cassure de neckline, le prix chute souvent **au moins de la distance entre la neckline et le sommet de la tête**. (Confirme Murphy.)

🟢 **Variantes :** plusieurs épaules gauches ou droites peuvent se former avant la vraie neckline.

### ⭐ Trade secret de StockCharts (insight important)

🟢 **La plupart des autres patterns de retournement (rounding bottom, V-reversal, double top, triple bottom) sont juste des variations du H&S qui ne se sont pas formées "parfaitement".** Exemple : le Triple Top est un H&S où la tête ne dépasse pas l'épaule gauche.

🟢 **Recommandation StockCharts :** ne pas se préoccuper du **type** exact de retournement. Savoir que c'est un Triple Top plutôt qu'un H&S ne rapporte pas plus d'argent. Se concentrer sur ce que le graphique dit : **le ratio fear/greed change** — et réagir en conséquence.

→ **TRADEX :** ⭐ **insight de simplification majeur.** Plutôt que de coder 15 patterns de retournement distincts (Chap. 8 §8.3), TRADEX peut se concentrer sur **un seul concept générique : le changement de structure (BoS) + confirmation volume**. Cela réduit la complexité (parcimonie, Chap. 9 §9.7.1) et le risque d'over-fitting. Tous les patterns de retournement = variations d'un même phénomène (épuisement de la tendance + bascule fear/greed). 🟢 principe / 🔵 implémentation.

---

## G. SYNTHÈSE — APPORT DU FICHIER 2

| Concept | Apport TRADEX | Tag |
|---|---|---|
| S/R = zones (psychologie role-reversal) | Confirme bandes COG comme zones | 🟢 |
| Volume by Price | = POC Market Profile, identifie S/R puissants | 🔵 |
| Classification tendances (durées) | ⚠️ Convention variable, ne pas figer en 🟢 | 🟡 |
| Trendline 2 points + validation | Confirme règle 3 touches | 🟡 |
| Non-touché borne canal | Signal avancé faiblesse tendance | 🔵 |
| Changement tendance = pic ET creux | Précise le BoS (Chap. 6) | 🟢 |
| Divergence prix/volume | Signal avancé (recoupe OBV/VSA) | 🟢 |
| Rectangle/Triangle continuation | Confirme Chap. 8 §8.2 | 🟡 |
| Volume décroissant dans coil | Critère de validation pattern | 🔵 |
| H&S + psychologie épaule gauche | Précise le timing de confirmation | 🟢 |
| ⭐ Tous reversals = variations du H&S | Simplification : 1 concept BoS+volume | 🟢 |

🟢 **Conclusion Fichier 2 :** apport majeur = **l'insight de simplification** (tous les patterns de retournement = un seul phénomène de changement de structure). Cela permet à TRADEX de réduire la complexité au lieu de multiplier les détecteurs de patterns. Le reste confirme les Chap. 6 et 8. Aucune hallucination.

---

*Extraction TRADEX-AI · Source : TA 101 Parties 7-13 via chartschool.stockcharts.com · Version 1.0 · 2026-06-19*
*Document éducatif. Rien n'est du conseil financier.*
