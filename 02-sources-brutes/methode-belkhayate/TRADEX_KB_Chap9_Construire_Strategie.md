# Chapitre 9 — Construire sa stratégie de trading

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 9.0 Pourquoi ce chapitre

🟢 Un trader peut maîtriser tous les outils des chapitres précédents (COG, Wyckoff, Order Flow, gestion du risque, setups) et échouer s'il ne les assemble pas dans un **système cohérent, écrit, et testé**. La stratégie est le cadre qui transforme des outils dispersés en un processus reproductible.

🟢 **Définition opérationnelle :** une stratégie de trading est un ensemble de règles écrites, non ambiguës, qui définissent : quand chercher un trade, quand entrer, quand sortir, combien risquer, et dans quelles conditions ne pas trader. Toute règle qui ne peut pas être écrite de façon non ambiguë n'est pas une règle — c'est du jugement subjectif.

🟡 **Convention de ce chapitre :** on distingue la **stratégie** (le système complet) du **setup** (une configuration d'entrée spécifique, Chap. 8). Une stratégie peut contenir plusieurs setups.

---

## 9.1 Les composantes d'une stratégie complète

### 9.1.1 Les 7 piliers d'une stratégie

🟢 Une stratégie opérationnelle doit répondre à ces 7 questions avant la première exécution :

| Pilier | Question | Exemple TRADEX-AI |
| :---- | :---- | :---- |
| **1\. Univers** | Sur quels actifs ? | Crude Oil Futures (CL), Gold (GC), E-mini S\&P (ES) |
| **2\. Timeframe** | Sur quel(s) TF ? | TF d'analyse : Daily/H4. TF d'entrée : H1/M15 |
| **3\. Filtre de régime** | Dans quelles conditions de marché ? | Range : COG actif. Tendance : structure HH/HL |
| **4\. Setup(s)** | Quelle(s) configuration(s) d'entrée ? | COG bande externe \+ rejet (Chap. 8\) |
| **5\. Gestion du trade** | Comment gérer après l'entrée ? | Scale-out à 1R, trailing sur structure |
| **6\. Gestion du risque** | Combien risquer ? | 1 % par trade, DD max 10 % |
| **7\. Règles de pause** | Quand ne pas trader ? | DD journalier \> 2R, annonce majeure, hors RTH |

🟢 Un pilier manquant \= stratégie incomplète \= décisions prises "en live" sous stress \= biais émotionnel.

### 9.1.2 La hiérarchie temporelle (Multi-Timeframe)

🟢 **Principe MTF (Multi-Timeframe Analysis) :** analyser le marché sur plusieurs échelles de temps pour aligner contexte macro et signal d'entrée micro.

🟢 **Structure classique en 3 TF :**

TF SUPÉRIEUR (contexte)     →  Direction globale, structure HH/HL, régime

TF INTERMÉDIAIRE (signal)   →  Setup, niveau clé, confirmation

TF INFÉRIEUR (entrée)       →  Précision du timing d'entrée, bougie signal

🟡 **Rapport entre TF (convention pratique) :** facteur 4 à 6 entre chaque niveau.

- Exemple : Daily (contexte) → H4 (signal) → H1 (entrée)  
- Exemple : H4 (contexte) → H1 (signal) → M15 (entrée)

🔴 **Erreur fréquente :** chercher un signal d'achat sur H1 quand le Daily est en tendance baissière forte. Le TF supérieur prime toujours sur le TF inférieur pour la direction.

🟢 **Règle MTF TRADEX-AI :** le signal d'entrée doit être aligné avec la direction du TF supérieur. Un signal contra-tendance sur TF inférieur nécessite une confluence exceptionnelle (Spring Wyckoff \+ bande externe COG) et une taille réduite.

---

## 9.2 Le filtre de régime — La décision la plus importante

### 9.2.1 Pourquoi le filtre de régime prime sur le setup

🟢 **Vérité fondamentale :** les stratégies de mean-reversion (retour vers la moyenne — COG Belkhayate) performent en marché de range. Les stratégies de suivi de tendance (pullback sur HL, LPS Wyckoff) performent en marché de tendance. Appliquer la mauvaise stratégie dans le mauvais régime détruit l'edge.

🟢 **Exemple concret :** le COG génère des signaux de retour vers la ligne centrale. En marché de forte tendance, le prix peut rester collé sur une bande externe pendant 10–20 bougies sans revenir. Chaque signal COG "d'achat" devient une perte si la tendance continue.

### 9.2.2 Méthodes de détection de régime

🟢 **Méthode 1 — Structure HH/HL :**

- Série de HH et HL → tendance haussière  
- Série de LH et LL → tendance baissière  
- Alternance sans direction → range

Avantage : simple, visuel, sans paramètre. Inconvénient : réactif (le régime est confirmé après le fait).

🟢 **Méthode 2 — ADX (Average Directional Index, Wilder 1978\) :**

- ADX \< 20 : marché sans tendance (range) → COG pertinent  
- ADX 20–40 : tendance modérée  
- ADX \> 40 : tendance forte → stratégies de suivi de tendance

🟡 Le seuil de 20/40 est une convention Wilder, pas une loi. Il peut être ajusté selon l'actif et le TF. À calibrer en backtest.

🟢 **Méthode 3 — R² (coefficient de détermination d'une régression linéaire) :** Calculer R² d'une régression linéaire sur N bougies. R² proche de 1 \= tendance forte. R² proche de 0 \= marché aléatoire/range.

🟡 N \= 14 est une convention commune. Non optimal universellement.

🔵 **Méthode 4 — Hurst Exponent :** H \> 0,5 : marché avec mémoire (tendance persistante) H \= 0,5 : marché aléatoire (Brownian motion) H \< 0,5 : marché mean-reverting (range, COG pertinent) 🔴 Le calcul du Hurst Exponent sur des séries courtes (\< 512 points) est peu fiable statistiquement. Usage limité en intraday.

### 9.2.3 Implémentation du filtre dans TRADEX-AI

🔵 **Filtre recommandé (à backtester) :**

SI ADX(14) \< 25 ET structure non directionnelle :

    → Activer setups COG mean-reversion (Chap. 8 §8.5.1)

    → Désactiver setups de continuation de tendance

SI ADX(14) \> 25 ET structure directionnelle (HH/HL ou LH/LL) :

    → Activer setups de continuation (pullback HL, LPS Wyckoff)

    → Désactiver setups COG mean-reversion purs (risque de fade la tendance)

    → COG utilisé uniquement pour les niveaux, pas comme signal de retournement

⚠️ Cette logique est une hypothèse de départ — à valider en backtest sur CL, GC, ES séparément. Les régimes varient selon l'actif.

---

## 9.3 Construction de la stratégie — Méthodologie pas à pas

### 9.3.1 Étape 1 : Définir l'edge théorique

🟢 Avant d'écrire une seule règle, répondre à cette question : **Quelle inefficacité de marché la stratégie exploite-t-elle ?**

Exemples d'edges théoriques valides :

- "Le prix revient statistiquement vers la gravité (COG) après un excès sur les bandes externes" → mean-reversion  
- "Les breakouts de range accompagnés de volume significatif ont une probabilité de continuation supérieure au hasard" → momentum  
- "Les Springs Wyckoff précédent statistiquement une phase de markup" → structure de marché

🔴 **Edge invalide :** "les prix montent souvent le lundi matin" — corrélation sans mécanisme explicatif. Ce type d'observation disparaît dès qu'il est connu et arbitré.

🟢 L'edge doit être basé sur un **mécanisme logique et défendable** (offre/demande, comportement des participants, liquidité) — pas uniquement sur une corrélation historique.

### 9.3.2 Étape 2 : Écrire les règles en langage pseudo-code

🟢 Objectif : rendre chaque règle testable et exécutable sans ambiguïté.

**Exemple — Setup COG Bande Externe (version pseudo-code) :**

CONDITION 1 (Régime) :

  ADX(14, H4) \< 25

  ET les 3 derniers HH/HL sur Daily ne forment pas de tendance directionnelle

CONDITION 2 (Niveau) :

  Prix actuel \>= COG\_Bande\_Haute(période=50, k=2.0)

  OU Prix actuel \<= COG\_Bande\_Basse(période=50, k=2.0)

CONDITION 3 (Signal) :

  Bougie H1 courante \= Pin Bar (mèche \>= 2/3 longueur totale, clôture dans 1/3 opposé)

  ET clôture de la bougie signal dépasse l'ouverture de la bougie précédente

CONDITION 4 (Confirmation volume) :

  Volume bougie signal \> Moyenne\_Volume(20 bougies précédentes) × 1.2

ENTRÉE :

  Prix d'entrée \= clôture de la bougie signal

  Stop \= extrême de la mèche \+ 2 ticks (buffer)

  Cible 1 \= COG\_Ligne\_Centrale

  Cible 2 \= COG\_Bande\_Opposée

GESTION :

  À Cible 1 atteinte : fermer 50 % de la position, déplacer stop au break-even

  Reste : trailing stop sur structure (sous dernier HL en haussier)

INVALIDER SI :

  DD journalier \>= 2R

  OU annonce économique dans les 30 min suivantes

  OU ADX(14) \> 30 au moment du signal

🔵 Ce pseudo-code est une hypothèse de travail — non validé. Chaque paramètre (50, 2.0, 1.2, 30 min) est à calibrer en backtest.

### 9.3.3 Étape 3 : Backtest in-sample

🟢 Appliquer les règles écrites sur une période historique représentative (minimum 2 ans, minimum 100 trades).

🟢 **Métriques à mesurer en in-sample :**

- Taux de gain  
- RR moyen réalisé  
- Espérance (en R)  
- Profit Factor  
- Maximum Drawdown  
- Nombre de trades par mois (fréquence)  
- Performance par type de marché (range vs. tendance)

🔴 Ne modifier aucun paramètre pendant l'in-sample pour "améliorer" les résultats. Toute modification \= nouveau backtest depuis le début.

### 9.3.4 Étape 4 : Validation out-of-sample (walk-forward)

🟢 Appliquer exactement les mêmes règles sur une période postérieure à l'in-sample, non consultée pendant l'optimisation.

🟢 **Critère de validation (conventions pratiques) :**

- Profit Factor out-of-sample ≥ 1,3 (dégradation acceptable vs. in-sample)  
- Maximum Drawdown out-of-sample ≤ 1,5 × Maximum Drawdown in-sample  
- Taux de gain out-of-sample ≥ taux de gain in-sample − 10 points

🔴 Si les résultats out-of-sample sont fortement dégradés : la stratégie est sur-optimisée. Revenir à l'étape 2 avec moins de paramètres.

### 9.3.5 Étape 5 : Simulation en temps réel (Paper Trading)

🟢 Avant d'engager du capital réel, exécuter la stratégie en simulation sur données en temps réel pendant minimum 30 trades ou 1 mois.

🟢 Objectifs du paper trading :

1. Vérifier que les règles sont applicables en temps réel (pas uniquement sur chart passé)  
2. Identifier les ambiguïtés de règles non détectées en backtest  
3. Construire la discipline d'exécution avant les enjeux financiers réels

🟡 Le paper trading ne réplique pas les conditions psychologiques du trading réel (pas de peur de la perte réelle). Il teste la mécanique, pas la psychologie.

### 9.3.6 Étape 6 : Déploiement et monitoring

🟢 **Taille de départ :** commencer avec une taille de position réduite (0,25–0,5 % de risque) pendant les 50 premiers trades en conditions réelles. Augmenter progressivement si les performances correspondent au backtest.

🟢 **Monitoring continu :** comparer les métriques réelles aux métriques de backtest tous les 20–30 trades. Une dégradation significative (Profit Factor réel \< 1,0 sur 30 trades consécutifs) signale un changement de régime ou un problème d'exécution.

🟡 **Fréquence de review :** mensuelle pour les stratégies intraday, trimestrielle pour les stratégies swing. Ne pas modifier les règles sur la base d'un seul trade ou d'une seule semaine.

---

## 9.4 La corrélation entre actifs — Risque de portefeuille

### 9.4.1 Corrélations fondamentales (valeurs approximatives — ⏳ variables)

🟢 Les corrélations entre actifs ne sont pas fixes — elles varient selon les conditions macro. Les valeurs suivantes sont des observations historiques moyennes, pas des constantes.

| Paire d'actifs | Corrélation historique moyenne | Statut | Note |
| :---- | :---- | :---- | :---- |
| CL (Crude Oil) ↔ DXY (Dollar) | Négative (−0,3 à −0,7) | ⏳ Variable | Pétrodollar : pétrole coté en USD |
| GC (Gold) ↔ DXY | Négative (−0,4 à −0,6) | ⏳ Variable | Or \= hedge contre USD |
| ES (S\&P 500\) ↔ VIX | Négative forte (−0,7 à −0,9) | 🟢 Structurelle | Relation offre/demande de protection |
| CL ↔ ES | Positive (0,3 à 0,6) | ⏳ Variable | Risk-on / risk-off |
| GC ↔ ES | Variable (−0,2 à \+0,3) | ⏳ Très variable | Dépend du régime macro |

🔴 Utiliser ces corrélations comme des certitudes est une erreur. En période de crise (2008, 2020), les corrélations convergent vers 1 (tout chute ensemble) — le phénomène de "correlation breakdown" annule les bénéfices de diversification.

### 9.4.2 Impact sur TRADEX-AI

🟢 **Risque de concentration :** trader simultanément CL et ES dans la même direction (deux positions longues corrélées positivement) double l'exposition nette. En termes de risque réel : 2R de risque apparent \= potentiellement 1,6–1,8R de risque corrélé.

🟡 **Règle pratique :** ne pas dépasser 2 positions simultanées sur des actifs corrélés. Si CL et GC sont tous deux en signal d'achat (corrélés négativement avec DXY en baisse), les considérer comme un seul trade pour le calcul du risque.

---

## 9.5 Adaptation de la stratégie au cycle de marché

### 9.5.1 Les quatre phases macro (Dow Theory — domaine public)

🟢 Charles Dow (1851–1902) a identifié trois phases dans les cycles de marché, largement reprises depuis :

1. **Accumulation :** les mains fortes achètent discrètement. Prix bas, volume faible. Marché range. Presse financière : pessimiste.  
2. **Participation :** les indicateurs techniques confirment la hausse. Tendance visible. La majorité des traders entre.  
3. **Distribution :** les mains fortes revendent aux acheteurs tardifs. Volume élevé, prix hauts. Presse financière : euphorique.  
4. **Déclin (Markdown) :** baisse généralisée. Panique. Volume de capitulation.

🟢 En termes Wyckoff (Chap. 6\) : Accumulation \= Phase A–D / Participation \= Phase E / Distribution \= Phase A–D inversée / Déclin \= Phase E inversée.

🟡 **Application à TRADEX-AI :**

- Phase d'accumulation : setups COG mean-reversion \+ Spring Wyckoff  
- Phase de participation : setups de continuation (LPS, pullback HL)  
- Phase de distribution : setups short (UTAD, COG bande haute)  
- Phase de déclin : setups short de continuation ou attente

### 9.5.2 Macro vs. Intraday

🟢 Les cycles macro (semaines à mois) et les cycles intraday (heures à jours) coexistent. Un trader intraday sur CL doit savoir si le marché est en accumulation macro (favorise les longs intraday) ou en distribution macro (favorise les shorts intraday).

🟡 **Convention pratique TRADEX-AI :** analyser le TF Weekly/Daily pour le biais directionnel macro, puis chercher des setups dans cette direction sur H4/H1.

---

## 9.6 Le plan de trading — Document opérationnel

### 9.6.1 Différence entre stratégie et plan de trading

🟢 **Stratégie :** le système (règles permanentes, backtestées, écrites). 🟢 **Plan de trading :** l'application de la stratégie à la session du jour (variables : niveaux clés du jour, annonces prévues, biais directionnel actuel, taille de position calculée).

Le plan se prépare avant l'ouverture de session. Il ne se modifie pas pendant la session.

### 9.6.2 Structure du plan de trading quotidien

🟡 **Template recommandé (à adapter selon la stratégie) :**

DATE : \_\_\_\_\_\_\_\_\_\_\_  ACTIF : \_\_\_\_\_\_\_\_\_\_\_  SESSION : RTH (heure locale : \_\_\_)

1\. BIAIS DIRECTIONNEL (TF Daily/H4)

   Structure : \[ \] HH/HL haussier \[ \] LH/LL baissier \[ \] Range

   ADX(14) : \_\_\_  Régime actif : \[ \] Mean-reversion \[ \] Tendance

2\. NIVEAUX CLÉS DU JOUR

   COG Ligne centrale : \_\_\_\_\_

   COG Bande haute : \_\_\_\_\_  COG Bande basse : \_\_\_\_\_

   POC session précédente : \_\_\_\_\_

   VAH : \_\_\_\_\_  VAL : \_\_\_\_\_

   Supports/résistances structurels : \_\_\_\_\_

3\. CALENDRIER ÉCONOMIQUE

   Annonces du jour (heure locale) :

   \[ \] Aucune annonce majeure  \[ \] Annonce à \_\_\_ h (éviter ±30 min)

4\. SETUPS POSSIBLES AUJOURD'HUI

   Setup 1 : \_\_\_\_\_\_\_  Niveau déclencheur : \_\_\_\_\_  Score /10 : \_\_\_

   Setup 2 : \_\_\_\_\_\_\_  Niveau déclencheur : \_\_\_\_\_  Score /10 : \_\_\_

5\. GESTION DU RISQUE DU JOUR

   Capital disponible : \_\_\_\_\_  Risque/trade (1%) : \_\_\_\_\_

   DD déjà subi aujourd'hui : \_\_\_  Limite DD restante : \_\_\_

6\. RÈGLES D'ARRÊT

   \[ \] Arrêt si DD journalier ≥ 2R

   \[ \] Arrêt après 3 trades (win ou loss)

   \[ \] Arrêt à \_\_\_ h (fermeture avant fin RTH)

🟡 Ce template est une convention — à adapter. L'important est qu'il soit rempli avant la session, pas pendant.

---

## 9.7 Erreurs systémiques dans la construction de stratégie

### 9.7.1 La sur-complexité

🟢 **Loi de la parcimonie (Occam's Razor appliqué au trading) :** entre deux stratégies avec le même edge, la plus simple est préférable car elle est plus robuste (moins de paramètres à over-fitter) et plus facile à exécuter sous stress.

🔴 **Indicateur de sur-complexité :** si la stratégie nécessite plus de 5 conditions simultanées pour déclencher un trade, elle sera rarement déclenchée et difficile à backtester rigoureusement.

🟡 **Règle pratique :** maximum 3 conditions d'entrée \+ 1 filtre de régime \+ règles de gestion. Au-delà, simplifier.

### 9.7.2 La stratégie du graal

🔴 **Mythe :** il existe une stratégie avec un taux de gain \> 80 % et un Profit Factor \> 3 sur tous les marchés et tous les TF. Non documenté de façon indépendante et vérifiable. Les stratégies avec des performances exceptionnelles en backtest sont presque toujours sur-optimisées.

🟢 **Réalité documentée :** les stratégies institutionnelles rentables long-terme ont typiquement des taux de gain entre 40 % et 55 % avec des RR entre 1,5 et 3\. La régularité de l'edge, pas son amplitude, fait la différence sur la durée.

### 9.7.3 L'optimisation excessive des paramètres

🔴 **Curve fitting :** ajuster le paramètre COG (période, k) jusqu'à ce que la stratégie soit parfaite sur les données historiques. Résultat : les paramètres sont optimaux pour le passé, pas pour le futur.

🟢 **Solution :** tester 3 valeurs de chaque paramètre (une "standard", une haute, une basse). Si la performance varie fortement entre les 3 valeurs, le paramètre est fragile. Si la performance est stable, le paramètre est robuste.

### 9.7.4 Négliger les frais de transaction

🟢 Chaque trade a un coût réel : commission \+ spread \+ slippage.

🟢 **Exemple sur CL :**

- Commission broker : \~$4 round-turn (⏳ variable selon broker)  
- Spread moyen RTH : 1–2 ticks \= $10–$20  
- Slippage moyen sur stop : 1–3 ticks \= $10–$30

🟢 Total par trade : \~$24–$54. Sur une stratégie avec RR de 2:1 et R \= 200 $ :

- Gain brut : 400 $. Gain net : 346–376 $.  
- Perte brute : 200 $. Perte nette : 224–254 $.

🟢 L'impact des frais réduit mécaniquement le Profit Factor. Un backtest sans frais est non représentatif. Toujours intégrer les frais réels dans les calculs.

---

## 9.8 Stratégie et TRADEX-AI — Architecture décisionnelle

### 9.8.1 Le moteur de décision TRADEX-AI

🔵 **Architecture proposée (hypothèse à valider) :**

NIVEAU 1 — FILTRE DE RÉGIME (automatique)

  Input : ADX(14), structure HH/HL, COG pente

  Output : Régime \= \[RANGE | TENDANCE\_H | TENDANCE\_B | INDÉFINI\]

NIVEAU 2 — IDENTIFICATION DES NIVEAUX (automatique)

  Input : COG bandes, Market Profile VAH/VAL/POC, structure Wyckoff

  Output : Liste des niveaux actifs \+ distance du prix actuel

NIVEAU 3 — SCORING DES SETUPS (semi-automatique)

  Input : Niveaux actifs \+ signal bougie \+ volume \+ calendrier éco

  Output : Score 0–10 par setup potentiel

NIVEAU 4 — DÉCISION D'ENTRÉE (humain ou automatique selon mode)

  Input : Score setup \+ capital \+ DD actuel

  Output : \[ENTRER | ATTENDRE | BLOQUER\]

NIVEAU 5 — GESTION DU TRADE (automatique)

  Input : Prix d'entrée \+ stop \+ cibles \+ trailing rules

  Output : Ordres de gestion (stop, cibles, trailing)

🔵 Cette architecture est une proposition de design — non implémentée. Chaque niveau doit être développé et testé indépendamment.

### 9.8.2 Données requises pour chaque niveau

| Niveau | Données requises | Source | Disponibilité |
| :---- | :---- | :---- | :---- |
| Filtre régime | OHLCV H4/Daily | Broker / Data feed | 🟢 Standard |
| Niveaux COG | OHLCV \+ calcul Python | belkhayate\_cog.py | 🟢 Disponible |
| Market Profile | Volume par prix | Broker tick data | 🟡 Dépend broker |
| Wyckoff phases | OHLCV \+ volume | Broker / Data feed | 🟡 Identification manuelle ou ML |
| Calendrier éco | API calendrier | Forex Factory / Econoday API | 🟢 API disponibles |
| Scoring setups | Agrégation des niveaux | Moteur interne | 🔵 À développer |

---

## 9.9 Synthèse du Chapitre 9

| Concept | Point clé | Tag | Action TRADEX-AI |
| :---- | :---- | :---- | :---- |
| Les 7 piliers | Univers, TF, régime, setup, gestion, risque, pause | 🟢 | Template obligatoire |
| Filtre de régime | ADX \+ structure \= condition préalable à tout signal | 🟢 | Niveau 1 du moteur |
| MTF analysis | TF supérieur prime pour la direction | 🟢 | H4 → H1 → M15 |
| Edge théorique | Mécanisme logique avant règles | 🟢 | Définir avant backtest |
| Pseudo-code | Règles non ambiguës \= backtestables | 🟢 | Format standard TRADEX |
| Backtest rigoureux | In-sample \+ out-of-sample obligatoires | 🟢 | Non négociable |
| Corrélations actifs | CL/GC/ES : corrélés → risque cumulatif | 🟡 ⏳ | Max 2 positions corrélées |
| Plan quotidien | Préparé avant session, non modifié pendant | 🟢 | Template journal |
| Architecture TRADEX | 5 niveaux : régime → niveaux → scoring → décision → gestion | 🔵 | Design à implémenter |

🟡 **Règle TRADEX de construction :** une stratégie qui ne peut pas être écrite en pseudo-code non ambigu n'est pas prête à être tradée. L'écriture force la clarté — les ambiguïtés apparaissent à l'écrit, pas dans la tête.

---

## 9.10 Checklist de validation d'une stratégie avant déploiement

- [ ] Les 7 piliers sont-ils définis et écrits ?  
- [ ] Le filtre de régime est-il défini avec des paramètres précis ?  
- [ ] Les règles sont-elles écrites en pseudo-code non ambigu ?  
- [ ] Un backtest in-sample (min 100 trades, min 2 ans) a-t-il été réalisé ?  
- [ ] Un backtest out-of-sample a-t-il été réalisé sur une période non consultée ?  
- [ ] Les frais de transaction réels sont-ils intégrés dans les calculs ?  
- [ ] Le Profit Factor out-of-sample est-il ≥ 1,3 ?  
- [ ] La stratégie a-t-elle été testée en paper trading (min 30 trades) ?  
- [ ] Le plan de trading quotidien est-il préparable en \< 15 minutes avant session ?  
- [ ] Les règles de pause (circuit-breakers) sont-elles définies et respectées ?

---

*Chapitre 9 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-17* *Tout le contenu de ce chapitre est éducatif. Rien ici n'est du conseil financier. L'architecture TRADEX-AI présentée est une proposition de design non implémentée — à valider techniquement et à backtester avant tout usage en conditions réelles.*  
