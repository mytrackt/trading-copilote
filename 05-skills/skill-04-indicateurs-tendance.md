---
name: skill-04-indicateurs-tendance
description: Règles sur les indicateurs de tendance Belkhayate — Gravity Center, Belkhayate 30, Trend, pivots, VWAP, moyennes mobiles, et structures d'impulsion.
trigger: Utiliser pour identifier la direction de la tendance et valider les signaux d'entrée avant de trader.
source: KNOWLEDGE_BASE_MASTER.json — 470 règles extraites
---

# SKILL 04 — INDICATEURS DE TENDANCE (Méthode Belkhayate)

## Indicateurs principaux Belkhayate

### Belkhayate Gravity Center (Centre de gravité)
- Installer et configurer le Gravity Center comme outil de base pour devenir un trader gagnant.
- Le Gravity Center agit comme zone d'accumulation cachée pour les algorithmes.
- Attendre que le prix revienne au Gravity Center plutôt que de chasser le prix.
- Le Gravity Center recalcule après chaque barre pour suivre le marché en temps réel.
- Le centre de gravité oscille entre une zone rouge (haute) et une zone verte (basse) → vendre dans les zones rouges, acheter dans les zones vertes.
- L'amplitude du marché se calcule depuis le centre de gravité : si l'amplitude est 30 ticks, attendre 15 ticks vers le centre et 30 ticks vers les extrêmes.
- Se rapprocher de la zone rouge (centre de gravité) augmente la probabilité que le marché revienne vers ce centre.
- Acheter lorsque le prix est sous le centre de gravité, vendre lorsqu'il est dans la zone rouge au-dessus.
- Le Gravity Center est vert/blanc = achat, rouge = vente.
- Acheter uniquement lorsque le Gravity Center devient vert, pas avant.
- Sortir de la position dès que le Gravity Center devient rouge.
- Le centre de gravité anticipe la cassure du point pivot.
- Le centre de gravité attire le marché vers lui quand on s'en éloigne trop.
- Le Gravity Center Belkhayate sur les FESX : identifier les vagues d'impulsion et les corrections.

### Belkhayate 30 (multi-unités de temps)
- Le Belkhayate 30 est une composition de 6 centres de gravité sur 6 unités de temps différentes pour détecter la tendance multidimensionnelle.
- Quand Belkhayate 30 est vert → tendance haussière, ne pas vendre.
- Quand Belkhayate 30 est rouge → tendance baissière, ne pas acheter.
- Peut être utilisé comme filtre de tendance ou comme signal direct d'achat/vente.
- S'adapte au trading court terme et au swing trading.
- Le centre de gravité en multidimension reste résolument baissier même si le marché cherche à corriger.

### Belkhayate Trend
- Le Belkhayate Trend extrait la réelle tendance du marché indépendamment de l'unité de temps.
- Belkhayate Trend vert = acheter.
- Belkhayate Trend orange/rouge = vendre.
- Belkhayate Trend blanc = prendre ses profits.
- Belkhayate Trend bleu = ne rien faire.
- Belkhayate Trend et Belkhayate Direction vous gardent en position jusqu'à la fin de la tendance.
- Ne pas acheter tant que Belkhayate Trend n'est pas vert et que la MM209 n'est pas cassée avec force.
- Entrer lors d'un pullback sur une tendance haussière confirmée par Belgeat Trend vert.

### Belkhayate Direction
- Belkhayate Direction confirme la tendance mais ne décide pas l'entrée ou la sortie.
- Quand Belkhayate Direction devient vert → signal d'inversion potentielle de la position vendeur.

### Belkhayate Cycle
- Belkhayate Cycle indique quand sortir du marché.

---

## Pivots Belkhayate

- Les pivots Belkhayate (PP, niveaux de GAN) sont les points clés pour entrer et sortir.
- Les niveaux de GAN sont tracés selon la méthode GAN et sont plus puissants que les pivots standards.
- Le marché respecte les niveaux de GAN bien plus que les pivots standards.
- Les pivots Belkhayate fonctionnent à la perfection pour confirmer les fausses cassures sur tous les marchés.
- Utiliser les données de la veille pour calculer les pivots, pas celles d'avant-veille.
- La clôture de la veille et le pivot forment une ceinture importante — respecter cette zone.
- Ajouter la clôture de la veille (ligne jaune) crée un ensemble très puissant appelé Belkhéad Pivot.
- Quand la clôture de la veille s'aligne ou se rapproche du pivot → signal très fort de support ou résistance.
- Les trois résistances (R1, R2, R3) et les trois supports (S1, S2, S3) sont prévus par formule mathématique dès le début de la journée.
- Les écarts entre bandes de pivots indiquent la volatilité probable : bandes écartées = forte volatilité, bandes rapprochées = faible volatilité.
- Le Dow Jones respecte beaucoup mieux les niveaux pivots que les autres marchés.
- N'entrez jamais entre les lignes des pivots — attendez que le marché arrive à ces lignes.
- Utiliser uniquement les pivots standards, ignorer les formules sophistiquées alternatives.

---

## VWAP & Bell-Riyad VWAP

- Le VWAP est un niveau clé : au-dessus = fort, au-dessous = faible.
- Acheter lorsque le prix casse une résistance et se positionne au-dessus du VWAP.
- Sortir la position lorsque le VWAP change de couleur ou devient rouge.
- Le Bell-Riyad VWAP rouge → vendeurs contrôlent le carnet d'ordres.
- Le Bell-Riyad VWAP vert → retournement dans le carnet d'ordres.
- Le Bell-Riyad VWAP blanc → équilibre entre acheteurs et vendeurs.
- Un feu de mort (grand chandelier rouge à volume élevé) sous le VWAP = confirmation de baisse.
- Si l'achat recasse le VWAP, la tendance baissière est cassée.
- Ne short que si le candle ferme sous le VWAP (sur carte 5 min).

---

## Moyennes mobiles

- Moyenne mobile 209 (11 x 19) comme référence majeure de la tendance.
- Tant que le marché n'a pas cassé la MM 209, la tendance haussière reste intacte.
- Une fois que le marché casse la MM 209, il revient en pullback avant de repartir avec force.
- Une cassure de la MM 209 avec volume indique une vraie accélération.
- Lorsque Belkhayate Trend est très loin de la MM 209, il y a de la force dans le mouvement.
- Utiliser le 200 SMA comme support long terme sur le chart quotidien.
- Utiliser le 8 EMA pour identifier les stocks en momentum haussier.
- Acheter uniquement les stocks situés au-dessus du 8 EMA et du 200 SMA.
- La 8 EMA est un indicateur de momentum : chercher les stocks qui se maintiennent le long de cette ligne.
- Un breakout au-dessus du 200 SMA avec volume qui s'éloigne au-dessus de la moyenne de volume = signal de continuation.
- La moyenne 19 sert de support sur le ZN. La moyenne 57 tient également comme niveau de support.
- Utiliser la moyenne mobile Hull (HMA) à 25 périodes comme ligne de base pour la direction de tendance.

---

## Structure d'impulsion (Vagues)

- Toute tendance se décompose en 5 vagues d'impulsion : 1, 2, 3, 4, 5.
- Il n'existe que 2 points d'entrée intéressants : cassure du point A (après vagues 1-2) et cassure du point B (après vagues 3-4).
- Ne jamais chercher à trader les corrections ou les retracements d'un mouvement d'impulsion.
- Ne pas acheter pendant les vagues 1, 2, 3 ou 4 : attendre uniquement les cassures des hauts.
- Le principe s'applique à toutes les unités de temps : 1 minute, 5 minutes, daily, weekly, range-bar.
- Pour calculer l'objectif haussier : comparer la vague 1 et la vague 3 — utiliser la plus grande comme référence pour l'extension Fibonacci.
- Comparer la taille des vagues : si la vague 2 est plus petite que la vague 1, utiliser Fibonacci extension sur la vague 3.
- Une impulsion perd en intensité lorsqu'une vague est plus grande que la précédente dans une tendance haussière.
- Ne jamais acheter dans le segment AB d'une impulsion — attendre le segment CD pour les meilleures entrées.
- Comparer l'amplitude des cassures successives : amplitude supérieure = signal plus puissant.

---

## Règles de correction et tendance

- Une tendance n'est valable que si la correction ne dépasse pas 50% du mouvement d'impulsion.
- Si la correction dépasse 50% → c'est le centre de gravité qui dirige, non la tendance. Ne pas chercher de tendance.
- Un marché qui corrige plus de 50% est un trading range.
- Si la correction reste en dessous de 50% → tendance reste saine et puissante.
- Une tendance saine ne corrige jamais plus de 50% de son mouvement précédent.
- L'impulsion D peut être 20-40% plus haute que l'impulsion A-B dans une configuration saine.
- Sur timeframe daily, vérifier le contexte sur le weekly pour valider la présence d'une tendance.

---

## Signaux de cassure et fausses cassures

- La première cassure du rectangle peut être un faux signal (fausse cassure).
- Une cassure de résistance ou support avec grande bougie et volume peut être une fausse cassure si elle s'accompagne d'un pattern ABCD.
- Les pivots Belkhayate marquent les points exacts où le marché revient buter et se renverse.
- Tester la résistance puis casser le support est un faux signal d'algorithme → indique une forte hausse à 85% de probabilité.
- Les fausses cassures de support/résistance offrent les meilleures opportunités de trading de la journée.
- Identifier les fausses cassures permet d'être parmi les premiers avec les professionnels.
- Lorsque le marché casse la résistance et reste plus de 4h au-dessus → atteindra le niveau suivant.
- Lorsque le marché casse une résistance avec force (première cass.) → le deuxième niveau atteint à 80% de probabilité.

---

## Indicateurs complémentaires

- Range Filter : visualiser les trading range et zones de non-trading. Vert et prix au-dessus = tendance haussière.
- Hurst Exponent : la ligne rouge doit être au-dessus de 0.5 pour confirmer un marché de tendance. Ne pas trader quand il coupe sur les côtés.
- Signal MBK (Belkhayate Ressort) : indique un effet ressort sur le prix — anticipe un tremplin haussier.
- MBK Signal donne des signaux d'achat avant le retournement effectif de la tendance.
- Utiliser le T3 pour la direction : chercher les courtes quand le prix est en dessous du T3, et les longues quand au-dessus.
- Utiliser les modèles Hidden Markov pour détecter les 7 régimes de marché (bullrun, crash, bruit, chop, etc.).

---

## Lecture des bougies pour la tendance

- Bougies devenant de plus en plus petites → beaucoup moins de mouvement et de latitude.
- Une mèche supérieure combinée à du volume en haut de marché = signal de vente.
- Une queue longue (4 ticks) suivie d'une pierre tombale = signal puissant d'entrée acheteur.
- Une ombre haute (queue haute) signale que les vendeurs attaquent → sortir immédiatement.
- Observer les queues des bougies pour identifier les impulsions des algo-traders.
- Une queue signifie que le marché a récupéré des ticks contre la tendance initiale.
- Une queue dont la hauteur est supérieure au corps de la bougie précédente → forte probabilité (80%) de baisse.
