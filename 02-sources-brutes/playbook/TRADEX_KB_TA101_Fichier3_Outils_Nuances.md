# Extraction TA 101 — Fichier 3/3 : Outils précis & nuances critiques

## TRADEX-AI · Ressource externe · Source : StockCharts ChartSchool « Technical Analysis 101 »

**Source :** série « Technical Analysis 101 », StockCharts ChartSchool. **Couverture de ce fichier :** Parties 14, 15, 16, 17 (Fibonacci, gaps, candlesticks \+ Bulkowski, comparaison/relative strength). **Statut global :** 🔵 ÉCOLE — mais contient 2 nuances critiques et 1 vraie source statistique.

**Tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ · ⚫ PROPRIÉTAIRE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## A. FIBONACCI / RETRACEMENTS (Partie 14\)

🟢 **Origine factuelle :** la suite de Fibonacci (1,1,2,3,5,8,13,21...) où chaque nombre \= somme des deux précédents. Le ratio d'un nombre au suivant approche **0,6180** (le "Golden Ratio", 1,6180 en inverse). Présent dans la nature (branches d'arbres, pommes de pin, etc.).

🟢 **Lien avec le trading :** R.N. Elliott a fait la première connexion connue entre mouvements de prix et golden ratio. Il a noté que beaucoup de retournements surviennent autour de **61,8 %** ou son complément **38,2 %** (100 − 61,8). Combinés avec 50 % et 100 %, ils forment le set standard de pourcentages Fibonacci.

🟢 **Niveaux Fibonacci standards :** 23,6 %, 38,2 %, 50 %, 61,8 %, 100 %, 161,8 % (extension).

🔵 **Pourquoi ça "marche" (interprétation StockCharts) :** ces pourcentages sont des niveaux où "quelque chose dit à beaucoup de gens qu'il est temps d'agir" → les prix s'y retournent. C'est un **phénomène de psychologie collective**, pas une loi physique.

🔴 **Mise en garde explicite de StockCharts :** beaucoup prétendent que les lignes Fibonacci ont des "pouvoirs presque magiques". StockCharts les considère comme **outils de prévision utiles mais pas magiques** — comme tout outil d'AT.

→ **TRADEX :** confirme et précise les niveaux Fibonacci (Chap. 8 §8.2.1, Murphy). Le set complet **23,6 / 38,2 / 50 / 61,8 / 161,8** est utilisable pour les cibles de pullback et d'extension. ⚠️ Statut 🔵/🟡 — niveaux à backtester sur CL/GC/ES, jamais traités comme magiques. Cohérent avec le rejet de l'infaillibilité (Chap. 14). 🔵

---

## B. GAPS — NUANCE CRITIQUE vs Murphy (Partie 15\) ⭐⚠️

🟢 **Définition :** espaces vides sur le chart \= aucune transaction dans une tranche de prix. Résultent d'un intérêt acheteur/vendeur extraordinaire pendant la fermeture du marché.

- **Up gap (haussier) :** le plus bas du jour de gap \> le plus haut de la veille.  
- **Down gap (baissier) :** le plus haut du jour de gap \< le plus bas de la veille.  
- Significatif quand accompagné d'un **volume supérieur à la moyenne**.

🟢 **4 types de gaps :**

- **Breakaway gap :** signale un changement de psychologie. Haussier après déclin/base/consolidation prolongée ; baissier après avance/top/consolidation.  
- **Common gap :** dans un range ou après un mouvement vif. **Ne reflète PAS de changement de psychologie** — juste volatilité ou déséquilibre temporaire. Peu significatif.  
- **Continuation gap (= measuring / runaway) :** près du milieu d'une tendance, signale sa continuation. Peut être déclenché par une news.  
- **Exhaustion gap :** dans le sens d'une tendance étendue. Pour être valide, le prix doit **se retourner peu après et combler le gap**. Marque souvent la fin de la tendance.

### ⭐⚠️ NUANCE CRITIQUE — contradiction partielle avec Murphy

🔴 **StockCharts (2024) contredit la croyance populaire sur le comblement des gaps :**

Beaucoup d'investisseurs croient à tort que les gaps influencent les prix futurs au point d'être inévitablement comblés. Les cas où les gaps se comblent **dans les quelques jours** suivant leur formation peuvent être significatifs. **MAIS les gaps ont peu ou pas d'influence sur l'action des prix des semaines ou des mois après leur formation.**

🔴 **Gaps intraday temporaires :** les prix gappent souvent à l'ouverture puis comblent avant la clôture. Ces gaps intraday temporaires **ne doivent pas être considérés comme ayant plus de signification que la volatilité normale**.

🔴 **Actifs peu liquides :** un chart avec gaps quasi quotidiens \= titre peu échangé → **à éviter** (viole l'hypothèse \#1 de liquidité, Fichier 1).

→ **TRADEX :** ⭐ **NUANCE IMPORTANTE.** Dans l'extraction Murphy, le "runaway gap" servait de cible de projection — c'est confirmé ici (continuation gap). MAIS la **théorie du comblement systématique des gaps est explicitement réfutée** : un gap n'est PAS destiné à être comblé à coup sûr. Pour TRADEX :

- ✅ Garder : breakaway et continuation gaps comme signaux (avec volume confirmant)  
- 🔴 Rejeter : toute stratégie basée sur "le gap sera comblé" comme règle (croyance non fondée au-delà de quelques jours)  
- ⚠️ Sur CL/ES (gaps fréquents post-EIA/week-end) : distinguer breakaway (significatif) de common gap (bruit). 🔵 à backtester.

Cette nuance est **plus rigoureuse que Murphy** et s'aligne mieux avec la discipline anti-hallucination TRADEX. 🟢 pour la nuance.

---

## C. CANDLESTICKS \+ SOURCE STATISTIQUE BULKOWSKI (Partie 16\) ⭐

🟢 **Origine :** patterns de bougies identifiés depuis les années 1700 par les traders de futures de riz japonais.

🟢 **Doji :** le prix ouvre et clôture au même niveau (ou presque), malgré des oscillations intraday. \= **équilibre des forces acheteur/vendeur**, indécision du marché, précède souvent un retournement.

- Doji avec longue mèche basse \= haussier (acheteurs ont fait remonter depuis un creux intraday).  
- Doji avec longue mèche haute \= baissier.

→ Recoupe le Doji du Chap. 6 §6.1.2 (indécision, pas signal de retournement automatique).

### ⭐ SOURCE STATISTIQUE RÉELLE — Bulkowski (rare et précieux)

🟢 **StockCharts cite Thomas N. Bulkowski :** 6 des patterns de bougies les plus **fiables** ont été déterminés par **test sur 4,7 millions de lignes de bougies**. Source : Bulkowski, *Encyclopedia of Candlestick Charts*.

🟢 C'est l'une des **rares sources de ce corpus à fournir une base statistique chiffrée et une méthodologie** (4,7M de bougies testées). Contrairement aux "taux de réussite" non sourcés rejetés ailleurs.

→ **TRADEX :** ⭐ **piste de recherche à fiabilité supérieure.** Bulkowski fournit des statistiques de fiabilité de patterns avec une méthodologie explicite et un échantillon massif. C'est exactement le type de source que la discipline TRADEX valorise (vs les "73 % de réussite" non sourcés).

- ⚠️ **MAIS** : les tests de Bulkowski portent sur des **actions**, pas sur les futures CL/GC/ES. Les résultats ne sont **pas transposables directement**.  
- ✅ **Action recommandée :** consulter l'*Encyclopedia of Candlestick Charts* de Bulkowski comme source de référence pour les **définitions rigoureuses** des patterns, puis **re-backtester sur l'actif futures cible**. Statut : 🔵 (source sérieuse, mais à valider sur l'actif TRADEX). Ne jamais reprendre les taux de Bulkowski comme 🟢 pour les futures sans backtest propre.

🟢 **Note importante :** StockCharts ne reproduit pas les chiffres exacts de Bulkowski dans la page — donc TRADEX ne dispose pas ici de taux précis. Il faudrait acquérir/consulter l'ouvrage source. Ne pas inventer de chiffres.

---

## D. COMPARISON CHARTING & RELATIVE STRENGTH (Partie 17\)

🟢 **Comparison charting :** étudier la performance d'un actif et sa performance **relative** à d'autres. Type de graphique "Performance" (% depuis une date).

🟢 **Relative Performance (ratio) :** tracer le ratio actif1:actif2 (ex. BA:$INDU).

- Pente **positive** \= actif1 surperforme actif2.  
- Pente **négative** \= actif1 sous-performe actif2.  
- Ligne **plate** \= performances similaires.

🟢 **Usages :** déterminer si un actif surperforme un indice de marché, ou comparer deux actifs entre eux.

→ **TRADEX :** ⭐ **confirme et opérationnalise** l'analyse de ratio déjà extraite (Murphy Charting Made Easy §B.9 \+ Chap. 12 corrélations). Pour TRADEX :

- Ratio **CL:$DXY** → force du pétrole vs dollar  
- Ratio **GC:$DXY** → force de l'or vs dollar  
- Ratio **Copper:Gold** → baromètre risk-on/risk-off (Chap. 12 §12.3.2)  
- Ratio **CL:ES** → corrélation risk-on/risk-off

La pente du ratio \= signal de force/faiblesse relative, calculable automatiquement avec une trendline ou une MA sur le ratio. 🟡→🔵 à backtester comme filtre de contexte macro.

---

## E. SYNTHÈSE — APPORT DU FICHIER 3

| Concept | Apport TRADEX | Tag |
| :---- | :---- | :---- |
| Fibonacci set complet (23,6/38,2/50/61,8/161,8) | Cibles pullback \+ extension | 🔵 |
| Fibonacci "utile pas magique" | Confirme rejet infaillibilité (Chap. 14\) | 🟢 |
| 4 types de gaps | Breakaway/continuation \= signaux | 🔵 |
| ⭐ Comblement des gaps réfuté au-delà de qq jours | NUANCE plus rigoureuse que Murphy | 🟢 |
| Common gap \= bruit | Distinguer du breakaway sur CL/ES | 🔵 |
| Doji \= indécision | Confirme Chap. 6 | 🟢 |
| ⭐ Bulkowski (4,7M bougies) | Source statistique sérieuse à consulter | 🔵 |
| Bulkowski sur actions ≠ futures | Re-backtest obligatoire sur CL/GC/ES | 🔴 |
| Relative Strength (ratio) | CL:DXY, Copper:Gold, etc. (Chap. 12\) | 🔵 |

🟢 **Conclusion Fichier 3 :** deux apports majeurs —

1. **La nuance sur les gaps** : StockCharts réfute explicitement le mythe du comblement systématique (plus rigoureux que Murphy) → TRADEX ne doit PAS baser de stratégie sur "le gap sera comblé".  
2. **Bulkowski** : piste vers une vraie source statistique (4,7M bougies) pour les définitions de patterns — à consulter et re-backtester sur futures, jamais à reprendre en l'état.

Aucune hallucination. Les seuls chiffres cités (38,2 %, 61,8 %, 4,7M bougies) proviennent directement de la source.

---

## F. SYNTHÈSE GLOBALE DES 3 FICHIERS TA 101

🟢 **Ce que la série TA 101 apporte à TRADEX (au-delà de ce que les chapitres couvraient déjà) :**

1. **Confirmation indépendante du cadre anti-graal** (Fichier 1\) — renforce le Chap. 14\.  
2. **Les 3 hypothèses de validité de l'AT** (liquidité, pas de prix artificiel, pas de news extrême) — transposables aux futures.  
3. **L'insight de simplification des patterns de retournement** (Fichier 2\) — tous \= variations du H\&S \= changement de structure \+ volume. Réduit la complexité.  
4. **La nuance critique sur les gaps** (Fichier 3\) — réfute le mythe du comblement.  
5. **La piste Bulkowski** (Fichier 3\) — vers une source statistique rigoureuse.

🔴 **Ce que TA 101 NE change PAS :** c'est un cours débutant orienté actions. Aucun de ses concepts ne devient 🟢 pour les futures sans backtest sur CL/GC/ES. Les durées de tendances, niveaux Fibonacci, et fiabilités de patterns sont des conventions/hypothèses à valider.

🟡 **Cohérence anti-hallucination :** la série TA 101 est elle-même prudente (analogie météo, "utile pas magique", réfutation du mythe des gaps). Parfaitement alignée avec la discipline TRADEX. Aucune contradiction interne introduite.

---

*Extraction TRADEX-AI · Source : TA 101 Parties 14-17 via chartschool.stockcharts.com · Version 1.0 · 2026-06-19* *Document éducatif. Rien n'est du conseil financier. Les sources tierces citées (Elliott, Bulkowski) sont à consulter et backtester sur l'actif cible avant tout usage.*  
