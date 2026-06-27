# Chapitre 8 — Patterns et setups de trading

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 8.0 Pourquoi ce chapitre

🟢 Un **setup** est un ensemble de conditions définies *a priori* qui justifient l'entrée en position. Sans définition précise du setup, il n'est pas possible de backtester, de mesurer l'edge, ni de maintenir une discipline d'exécution cohérente.

🟢 Un **pattern** est une configuration graphique récurrente. Un pattern seul n'est pas un setup : il devient un setup uniquement quand il est encadré par un contexte (structure de marché, niveau clé, volume) et des règles d'entrée/sortie précises.

🟡 **Convention de lecture de ce chapitre :** chaque pattern est présenté avec (a) sa définition mécanique non ambiguë, (b) ce qu'il mesure réellement, (c) ses limites documentées, (d) son intégration dans TRADEX-AI.

---

## 8.1 Fondements : qu'est-ce qu'un setup valide ?

### 8.1.1 Les 5 composantes d'un setup

🟢 Un setup tradeable doit contenir exactement ces 5 éléments — ni plus, ni moins :

| Composante | Description | Exemple |
| :---- | :---- | :---- |
| **1\. Contexte** | Type de marché et structure | Tendance haussière (HH/HL confirmés) |
| **2\. Niveau déclencheur** | Zone où le setup devient actif | COG bande externe \+ support Wyckoff |
| **3\. Signal d'entrée** | Condition précise et mesurable | Pin bar de rejet \+ clôture au-dessus du niveau |
| **4\. Invalidation** | Condition qui annule le setup | Clôture sous le niveau de support |
| **5\. Cible et stop** | Niveaux de sortie définis avant l'entrée | Stop sous le plus bas de la pin bar, cible COG centrale |

🟢 Un setup sans les 5 composantes est incomplet et non backtestable.

### 8.1.2 Setup vs. Trade

🟢 **Setup ≠ Trade.** Un setup est une opportunité potentielle. Il devient un trade uniquement quand toutes les conditions sont réunies ET que la gestion du risque (Chap. 7\) valide la taille de position.

🟡 **Règle de sélectivité :** mieux vaut manquer un setup que d'entrer sur un setup incomplet. La fréquence de trading n'est pas une vertu — la qualité des setups l'est.

---

## 8.2 Patterns de continuation de tendance

### 8.2.1 Le pullback sur Higher Low (HL)

🟢 **Définition mécanique :** en tendance haussière (succession de HH et HL confirmés), le prix recule temporairement, forme un nouveau HL, puis reprend la direction haussière.

🟢 **Ce qu'il mesure :** absorption des vendeurs sur un niveau de support structurel. Les acheteurs reprennent le contrôle après une correction.

🟢 **Conditions d'entrée (à définir avant utilisation) :**

1. Structure haussière confirmée (minimum 2 HH et 2 HL)  
2. Pullback jusqu'à une zone de support (HL précédent, niveau COG, MA)  
3. Signal de reprise : première bougie haussière clôturant au-dessus de la dernière bougie baissière du pullback

🟢 **Stop :** sous le HL formé (invalidation de la structure). 🟢 **Cible :** prochain HH potentiel ou extension (1,272 × hauteur du swing précédent — 🔵 niveau Fibonacci, convention).

🔴 **Piège fréquent :** entrer trop tôt pendant le pullback (avant confirmation du HL). Le pullback peut continuer et casser la structure.

### 8.2.2 Le flag (drapeau)

🟢 **Définition mécanique :** après un mouvement impulsif fort (le mât), le prix consolide dans un canal légèrement contra-tendance ou horizontal (le drapeau), puis reprend la direction initiale.

🟢 **Ce qu'il mesure :** consolidation ordonnée après une impulsion — les participants prennent des profits partiels sans que la pression directionnelle ne s'inverse.

🟢 **Conditions de validation :**

- Mât : mouvement directionnel fort, au moins 2× la hauteur du drapeau  
- Drapeau : consolidation de 3 à 20 bougies, volume décroissant pendant la consolidation  
- Déclencheur : cassure de la borne haute du drapeau avec volume en hausse

🟡 **Cible classique (convention) :** hauteur du mât projetée depuis le point de cassure. Non vérifiée statistiquement sur tous les actifs et TF — à backtester.

🔴 **Volume décroissant pendant le drapeau** est la condition clé. Un drapeau avec volume stable ou croissant peut signaler une distribution, pas une consolidation.

### 8.2.3 Le triangle de continuation

🟢 **Définition mécanique :** série de hauts décroissants et de bas croissants formant une zone de compression. La cassure reprend (statistiquement — 🔵) la direction de la tendance préalable.

🟡 **Types :**

- **Symétrique :** hauts décroissants \+ bas croissants (compression neutre)  
- **Ascendant :** hauts horizontaux \+ bas croissants (pression acheteuse)  
- **Descendant :** hauts décroissants \+ bas horizontaux (pression vendeuse)

🔴 **Taux de continuation annoncés (ex. "75 % de continuation") :** non vérifiables sans méthodologie de mesure précise et base de données large. À écarter comme fait — garder comme hypothèse 🔵.

🟢 **Condition d'entrée valide :** attendre la cassure confirmée (clôture hors du triangle) avant d'entrer. Les fausses cassures à l'intérieur du triangle sont fréquentes.

---

## 8.3 Patterns de renversement

### 8.3.1 La tête-épaules (Head & Shoulders)

🟢 **Définition mécanique :** trois sommets successifs, le central (tête) étant plus haut que les deux latéraux (épaules). La ligne reliant les deux creux entre les sommets est la **neckline** (ligne de cou).

🟢 **Ce qu'il mesure :** épuisement progressif de la pression acheteuse. Chaque tentative de faire un nouveau HH produit un résultat de plus en plus faible (épaule droite \< tête).

🟢 **Signal de déclenchement :** cassure de la neckline en clôture \+ idéalement volume en hausse sur la cassure.

🟢 **Stop :** au-dessus de l'épaule droite (invalidation du pattern).

🟡 **Cible classique (convention) :** hauteur de la tête au-dessus de la neckline, projetée sous la neckline. Convention largement utilisée, non vérifiée statistiquement de façon indépendante sur tous les actifs.

🔴 **Tête-épaules inversée :** pattern miroir, signal de renversement haussier. Mêmes règles, mêmes limites.

🔵 **Limite importante :** l'identification d'une "vraie" tête-épaules vs. une simple consolidation en 3 sommets est souvent rétrospective. En temps réel, le pattern n'est confirmé qu'à la cassure de la neckline.

### 8.3.2 Le double top / double bottom

🟢 **Définition mécanique :**

- **Double top :** deux sommets approximativement au même niveau de prix, séparés par un creux intermédiaire. Signal : cassure du creux intermédiaire.  
- **Double bottom :** deux creux approximativement au même niveau, séparés par un sommet intermédiaire. Signal : cassure du sommet intermédiaire.

🟢 **Ce qu'il mesure :** test et échec à franchir un niveau de résistance (double top) ou de support (double bottom). Le marché a "essayé deux fois" et n'a pas réussi.

🟡 **Condition de "même niveau" :** convention généralement ±0,5–1 % de l'actif. À définir avant utilisation pour être backtestable.

🟢 **Stop :** au-delà du deuxième sommet/creux (invalidation). 🟡 **Cible :** hauteur du pattern projetée depuis la cassure (même convention que H\&S).

🔵 **Risque de faux signal :** les doubles tops/bottoms avortés (price revient au-dessus/en dessous après la cassure) sont courants. Confirmer avec volume et/ou signal de bougie sur la cassure.

### 8.3.3 Le V-reversal (renversement en V)

🟢 **Définition :** chute ou montée rapide suivie d'un retournement immédiat et tout aussi rapide, sans phase de consolidation.

🔴 **Difficulté d'exploitation :** les V-reversals ne donnent pas de signal d'entrée clair *a priori*. Ils sont principalement identifiables après coup. Tenter d'entrer "dans" un V-reversal en temps réel expose à entrer dans une continuation du mouvement initial.

🟡 **Usage pratique :** utile pour identifier des niveaux de support/résistance importants après coup, pas comme setup d'entrée direct.

---

## 8.4 Patterns de bougie — Usage correct dans TRADEX-AI

### 8.4.1 Règle fondamentale

🟢 **Un pattern de bougie n'a de valeur que dans un contexte.** Une pin bar au milieu d'une range sans niveau clé n'a pas de valeur statistique démontrée. La même pin bar sur une bande externe COG \+ support Wyckoff \+ niveau Market Profile VAL \= confluence significative.

🟡 **Principe de filtre de contexte :** avant tout signal de bougie, vérifier :

1. Où sommes-nous dans la structure de marché ? (HH/HL ou LH/LL)  
2. Sommes-nous sur un niveau clé identifié *a priori* ?  
3. Le type de marché est-il compatible avec le signal ? (range vs. tendance)

### 8.4.2 Pin bar (Inside/Outside)

🟢 **Définition mécanique :** bougie avec un long corps de mèche (au moins 2× la taille du corps) et une clôture dans le tiers opposé à la mèche. La mèche représente un rejet fort d'un niveau de prix.

🟢 **Ce qu'elle mesure :** le marché a testé un niveau (via la mèche) et les participants ont rejeté ce niveau (clôture dans la direction opposée).

🟡 **Critères de validation (à fixer avant backtest) :**

- Mèche ≥ 2/3 de la longueur totale de la bougie  
- Corps dans le 1/3 opposé à la mèche  
- Position sur un niveau clé identifié *a priori*

🔵 **Taux de succès des pin bars en isolation :** non documenté de façon indépendante avec méthodologie rigoureuse. À backtester sur l'actif et le TF cibles avec les critères fixés ci-dessus.

### 8.4.3 Engulfing (bullish/bearish)

🟢 **Définition mécanique :** une bougie dont le corps englobe entièrement le corps de la bougie précédente (clôture \+ ouverture au-delà).

🟢 **Ce qu'il mesure :** renversement du momentum sur la période. Les acheteurs (engulfing haussier) ou vendeurs (engulfing baissier) ont complètement effacé le mouvement précédent.

🟡 **Variante forte :** le corps de la bougie engloutissante dépasse également les mèches de la bougie précédente. Signal considéré plus fort par convention.

🔴 **Engulfing sans contexte :** fréquent et peu prédictif. Valeur uniquement en confluence avec niveau clé \+ structure.

### 8.4.4 Inside Bar

🟢 **Définition mécanique :** bougie dont le high ET le low sont contenus dans le range de la bougie précédente (bougie mère).

🟢 **Ce qu'elle mesure :** compression de volatilité — indécision ou absorption temporaire. L'énergie s'accumule avant un mouvement directionnel.

🟡 **Signal d'entrée classique :** cassure du high ou du low de la bougie mère avec stop de l'autre côté. Direction de la cassure détermine le sens du trade.

🔵 **Fausse cassure fréquente :** le marché casse un côté puis revient — stop-hunt sur les stops évidents. Solution : attendre une clôture de confirmation au-delà de la bougie mère plutôt qu'entrer sur la cassure immédiate.

---

## 8.5 Setups spécifiques TRADEX-AI (COG Belkhayate)

### 8.5.1 Setup principal : Bande externe \+ Rejet

🟢 **Contexte requis :** marché en range ou début de correction dans tendance (COG pertinent — voir Chap. 5).

🔵 **Conditions (hypothèses à backtester) :**

1. Prix atteint ou dépasse la bande externe COG (bande ± 2σ ou ± 3σ selon paramétrage)  
2. Signal de rejet sur la bougie de contact : pin bar, engulfing, ou stopping volume VSA  
3. Wyckoff : phase compatible (B, C, ou début D)  
4. Market Profile : niveau dans la Value Area ou retour depuis l'extrême de session  
5. RR minimum 2:1 calculé vers la ligne centrale COG (cible primaire)

🔵 **Entrée :** clôture de la bougie signal au-delà du niveau de rejet 🔵 **Stop :** au-delà de l'extrême de la bougie signal (pin bar \= au-delà de la mèche) 🔵 **Cible 1 :** ligne centrale COG (\~1R à 2R selon distance) 🔵 **Cible 2 :** bande externe opposée (\~3R à 4R)

⚠️ **Statut : 🔵 — à backtester sur actif et TF cibles avant intégration en production.**

### 8.5.2 Setup secondaire : Spring Wyckoff \+ COG

🔵 **Conditions :**

1. Structure Wyckoff Phase C identifiée (range définie, tentative de cassure du support)  
2. Spring : cassure rapide sous le support \+ reprise immédiate (clôture au-dessus)  
3. COG : la bande externe coïncide avec la zone du Spring (confluence)  
4. Volume : Stopping Volume ou No Supply VSA au niveau du Spring

🔵 **Entrée :** clôture de la bougie de Spring au-dessus du support 🔵 **Stop :** au-delà du plus bas du Spring (invalidation) 🔵 **Cible :** ligne centrale COG / résistance de range / SOS Wyckoff

⚠️ **Statut : 🔵 — confluence forte théoriquement, à valider en walk-forward.**

### 8.5.3 Setup tertiaire : Continuation sur LPS Wyckoff

🔵 **Conditions :**

1. SOS (Sign of Strength) confirmé — cassure du plafond de range avec volume  
2. LPS (Last Point of Support) : pullback après SOS avec volume décroissant  
3. COG ligne centrale devient support (prix au-dessus de la ligne centrale)  
4. Price action : bougie de continuation (inside bar breakout, engulfing haussier)

🔵 **Entrée :** clôture au-dessus du plus haut de la bougie LPS 🔵 **Stop :** sous le LPS 🔵 **Cible :** extension du mouvement (1,272 × hauteur de la range — convention Fibonacci 🔵)

⚠️ **Statut : 🔵 — nécessite identification correcte de la Phase D Wyckoff, difficile en temps réel.**

---

## 8.6 Setups à éviter — Configurations à faible edge

### 8.6.1 Le trade "en plein milieu"

🟢 Entrer en position sans niveau clé identifié *a priori* — au milieu d'une range, sans support/résistance, sans signal COG. Résultat : RR défavorable ou stop arbitraire.

### 8.6.2 Le trade contre tendance sans Spring confirmé

🔴 Vendre dans une tendance haussière forte sans confirmation de distribution (Wyckoff Phase A/B). Statistiquement défavorable — la tendance a plus de probabilité de continuer que de se retourner à chaque bougie.

### 8.6.3 Le trade sur annonce économique

🟢 Les annonces macroéconomiques majeures (NFP, décision Fed, inventaires pétrole EIA) produisent des mouvements dont la direction est imprévisible et la volatilité extrême. Le spread s'élargit, les stops slippent.

🟡 **Règle pratique :** éviter toute entrée dans les **30 minutes avant** une annonce majeure (aligné DECISIONS_VEROUILLEES — Zone 2 News Gate). Fermer les positions ouvertes ou réduire la taille si une annonce est prévue pendant le trade.

### 8.6.4 Le trade en période de faible liquidité

🟢 Sessions hors RTH (pre-market tardif, after-hours, week-end sur certains marchés) : spread plus large, volume plus faible, mouvements moins représentatifs de la vraie intention du marché.

---

## 8.7 Backtesting des setups — Méthode rigoureuse

### 8.7.1 Pourquoi le backtest manuel est nécessaire

🟢 Un backtest automatique sur données historiques mesure la performance passée d'un ensemble de règles définies. Il est nécessaire mais insuffisant. Un backtest manuel (relecture chart par chart) permet de vérifier que les règles sont bien applicables en temps réel et qu'elles ne souffrent pas de biais de définition.

🔴 **Biais de look-ahead :** utiliser en backtest une information qui n'était pas disponible au moment de la décision (ex. le volume total d'une bougie en cours). Invalide le backtest.

🔴 **Biais de sélection :** ne retenir que les exemples favorables pour valider le setup. Invalide statistiquement les conclusions.

### 8.7.2 Protocole de backtest minimum

🟢 **Étapes obligatoires :**

1. **Définition stricte et écrite** de toutes les règles du setup avant d'ouvrir un seul chart  
2. **Période d'entraînement (in-sample) :** appliquer les règles sur une période historique (ex. 2020–2023)  
3. **Période de validation (out-of-sample / walk-forward) :** appliquer *exactement* les mêmes règles sur une période non vue (ex. 2024–2025)  
4. **Minimum 30 trades** en out-of-sample pour toute conclusion statistique (idéalement 100+)  
5. **Métriques à mesurer :** taux de gain, RR moyen réalisé, espérance, Profit Factor, Maximum Drawdown

🟢 **Si les résultats out-of-sample sont significativement inférieurs à l'in-sample :** le setup est sur-optimisé — retour à la définition.

🔴 **Walk-forward ≠ backtest sur données récentes :** le walk-forward impose que la période de validation soit postérieure à la période d'entraînement et que les règles ne soient jamais modifiées pour améliorer la période de validation.

### 8.7.3 Paramètres à ne pas optimiser

🔵 **Over-fitting (sur-ajustement) :** ajuster les paramètres du setup jusqu'à ce qu'il soit parfait sur les données historiques. Résultat : performances futures médiocres car le modèle a appris le bruit, pas le signal.

🟡 **Règle pratique :** ne pas avoir plus de 3 paramètres libres dans un setup. Au-delà, le risque d'over-fitting augmente significativement.

---

## 8.8 Grille de scoring des setups pour TRADEX-AI

🔵 **Objectif :** produire un score 0–10 par setup pour aider à la décision d'entrée. Chaque critère est binaire (présent \= 1 point, absent \= 0\) sauf indication.

| Critère | Points | Tag |
| :---- | :---- | :---- |
| Structure de marché confirmée (HH/HL ou LH/LL) | 1 | 🟢 |
| Niveau COG actif (bande externe ou centrale) | 2 | 🔵 |
| Signal de bougie valide (pin bar, engulfing, inside bar) | 1 | 🟡 |
| Phase Wyckoff compatible (B, C, D) | 1 | 🔵 |
| Volume confirmatoire (VSA No Supply / Stopping Volume) | 1 | 🟡 |
| RR ≥ 2:1 calculé avant entrée | 2 | 🟢 |
| Pas d'annonce économique dans les 30 min | 1 | 🟢 |
| Confluence Market Profile (POC, VAH, VAL) | 1 | 🟡 |
| **Total** | **10** |  |

🔵 **Seuils d'action (hypothèses à valider) :**

- Score 0–4 : ne pas trader  
- Score 5–6 : taille réduite (0,5 % de risque)  
- Score 7–8 : taille normale (1 % de risque)  
- Score 9–10 : taille pleine (1,5 % de risque si edge démontré)

⚠️ Ces seuils sont des points de départ — à calibrer selon les résultats de backtest réels.

---

## 8.9 Catalogue des setups TRADEX-AI — Récapitulatif

| Setup | Contexte requis | Signal déclencheur | Stop | Cible | Statut |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **COG Bande externe \+ Rejet** | Range ou correction | Pin bar / engulfing sur bande externe | Au-delà mèche signal | Ligne centrale COG | 🔵 À backtester |
| **Pullback sur HL** | Tendance haussière confirmée | Première bougie haussière après HL | Sous le HL | Prochain HH potentiel | 🟡 Convention |
| **Spring Wyckoff \+ COG** | Range (Phase C) | Clôture au-dessus support après cassure fausse | Sous le bas du Spring | Résistance range / COG centrale | 🔵 À backtester |
| **LPS Wyckoff** | Phase D confirmée | Pullback faible volume \+ bougie continuation | Sous le LPS | Extension de la range | 🔵 À backtester |
| **Flag continuation** | Tendance forte | Cassure borne haute du flag avec volume | Sous le bas du flag | Hauteur mât projetée | 🟡 Convention |
| **Double bottom** | Niveau support testé 2× | Cassure du sommet intermédiaire | Sous le 2e creux | Hauteur pattern projetée | 🟡 Convention |
| **H\&S inversée** | Base après tendance baissière | Cassure neckline avec volume | Au-dessus épaule droite | Hauteur tête projetée | 🟡 Convention |

---

## 8.10 Erreurs fréquentes dans l'application des setups

🟢 **Changer les règles après un trade perdant :** adapter le setup pour qu'il aurait évité la perte. C'est de l'over-fitting en temps réel. Les règles se modifient uniquement sur des données statistiques, pas sur des trades individuels.

🟢 **Multiplier les setups :** avoir 10 setups différents réduit la maîtrise de chacun. Un trader expert maîtrise 2–3 setups exécutés avec précision plutôt que 10 setups mal exécutés.

🔴 **Entrer avant la confirmation :** anticiper le signal d'entrée pour avoir un "meilleur prix". Le setup est défini par la confirmation — entrer avant, c'est entrer sur espoir, pas sur signal.

🟡 **Ignorer le contexte macro le jour d'un setup :** un setup techniquement parfait peut être invalidé par un événement macro (annonce Fed, conflit géopolitique, données d'inventaire EIA pour le pétrole). Vérifier le calendrier économique fait partie du protocole pré-trade.

🔵 **Confondre back-test visuel et edge statistique :** trouver 5 exemples visuels parfaits sur un chart ne prouve pas l'edge. L'edge se prouve par un protocole de backtest rigoureux sur un échantillon représentatif.

---

## 8.11 Synthèse du Chapitre 8

| Concept | Point clé | Tag | Action TRADEX-AI |
| :---- | :---- | :---- | :---- |
| Définition setup | 5 composantes obligatoires | 🟢 | Template setup obligatoire |
| Patterns continuation | Flag, pullback HL, triangle | 🟡 | Hypothèses à backtester |
| Patterns renversement | H\&S, double top/bottom | 🟡 | Confirmation obligatoire avant entrée |
| Patterns bougies | Pin bar, engulfing, inside bar | 🟡 | Valeur uniquement en confluence |
| Setup COG \+ Rejet | Setup principal TRADEX | 🔵 | Backtester en priorité 1 |
| Setup Spring Wyckoff | Setup secondaire | 🔵 | Backtester en priorité 2 |
| Grille de scoring 0–10 | Aide à la décision | 🔵 | Implémenter dans moteur scoring |
| Backtest rigoureux | In-sample \+ out-of-sample | 🟢 | Non négociable avant production |

🟡 **Règle TRADEX des setups :** tout setup intégré dans le cerveau TRADEX doit avoir (1) une définition écrite non ambiguë, (2) un tag de fiabilité, (3) un résultat de backtest out-of-sample ou être explicitement marqué 🔵 "hypothèse à tester". Aucun taux de réussite annoncé ne doit être intégré sans source et méthodologie vérifiables.

---

## 8.12 Checklist setup avant intégration dans TRADEX-AI

- [ ] Le setup a-t-il les 5 composantes (contexte, niveau, signal, invalidation, cible/stop) ?  
- [ ] Chaque règle est-elle définie de façon non ambiguë et calculable ?  
- [ ] Le setup a-t-il un tag de fiabilité appliqué à chaque paramètre ?  
- [ ] Un backtest out-of-sample a-t-il été réalisé (ou le setup est-il explicitement 🔵) ?  
- [ ] Le RR minimum est-il ≥ 2:1 calculé mécaniquement ?  
- [ ] La grille de scoring 0–10 a-t-elle été appliquée ?  
- [ ] Le calendrier économique a-t-il été vérifié pour la session concernée ?

---

*Chapitre 8 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-17* *Tout le contenu de ce chapitre est éducatif. Rien ici n'est du conseil financier. Les setups listés sont des hypothèses à backtester, jamais des vérités établies.*  
