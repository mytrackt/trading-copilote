---
name: skill-08-structure-marche
description: Règles de structure de marché Belkhayate — identifier les ranges, impulsions, fausses cassures, configurations de marché, et régimes pour ne trader que les setups valides.
trigger: Utiliser avant d'entrer pour valider que la structure de marché est favorable (impulsion, non range, non correction > 50%).
source: KNOWLEDGE_BASE_MASTER.json — 328 règles extraites
---

# SKILL 08 — STRUCTURE DE MARCHÉ (Méthode Belkhayate)

## Principe fondamental

- Le marché est en trading range 75% du temps — ne trader que les 25% restants (tendances et impulsions).
- 95% du temps le marché est dangereux. 5% du temps seulement il donne facilement de l'argent.
- Un range (trait de règle) n'offre pas d'opportunité selon la méthode Belkhayate.
- Ignorer les cassures des ranges tant qu'il n'y a pas de phase d'impulsion établie.
- Trader uniquement les 20% représentant les tendances où on gagne l'argent.

---

## Identification des phases de marché

### Phase de range (consolidation)
- Tracer un rectangle pour identifier si le marché est en impulsion ou en correction.
- Un trait de règle (range/consolidation) n'offre pas d'opportunité d'entrée.
- Identifier un range en définissant un support et une résistance sur le marché.
- Utiliser le Range Filter pour visualiser les trading range et les zones de non-trading.
- Un trading range est confirmé quand le marché tape plusieurs fois sur le même niveau sans cassure.
- Un marché qui corrige plus de 50% est un trading range — ne pas chercher de tendance.
- À midi heure de Paris, il n'y a pratiquement jamais de tendance sur les indices.
- Le marché baisse plus rapidement et brutalement qu'il ne monte.

### Phase d'impulsion
- Chercher les mouvements d'impulsion sortant du rectangle, pas les mouvements latéraux.
- Un mouvement d'impulsion se compose de 5 vagues : 1, 2, 3, 4, 5.
- Les deux seuls points d'entrée valides sur un mouvement d'impulsion : cassure du haut de la vague 1 et cassure du haut de la vague 3.
- Ne jamais chercher à trader les corrections ou les retracements d'un mouvement d'impulsion.
- L'ouverture et la fermeture de session contiennent en général des mouvements d'impulsion.
- Les 90 premières minutes produisent généralement des mouvements d'impulsion provoqués par les algo-traders.

### Phase de correction
- Une correction inférieure à 50% → tendance valide, on peut acheter.
- Une correction supérieure à 50% → pas de potentiel haussier, transformation en trading range probable.
- Si la correction reste en dessous de 50% → tendance reste saine et puissante.
- Tracer les niveaux de retracement à 50% de l'impulsion AB pour identifier les zones de correction.

---

## Fausses cassures (appâts d'algorithmes)

- La première cassure du rectangle peut être un faux signal (fausse cassure).
- Le vrai signal d'entrée vient de la cassure confirmée par un retour et une re-cassure.
- Les fausses cassures de support/résistance offrent les meilleures opportunités de trading de la journée.
- Identifier les fausses cassures permet d'être parmi les premiers avec les professionnels.
- Le marché s'écoule très rapidement après une fausse cassure, sans laisser de temps pour respirer.
- Tester la résistance puis casser le support est un faux signal d'algorithme → indique une forte hausse à 85%.
- Une cassure de résistance ou support avec grande bougie et volume peut être une fausse cassure si accompagnée d'un pattern ABCD.
- Les pivots Belkhayate marquent les points exacts où le marché revient buter et se renverse lors d'une fausse cassure.
- Chercher l'appât (faux signal) qui précède l'accélération — tracer une ligne de cassure pour déclencher l'entrée.

---

## Structures de cassure valides

- Entrer sur la deuxième cassure du niveau de support/résistance, pas sur la première.
- Attendre une cassure du rectangle, puis un retour (pullback) vers le niveau cassé avant d'entrer.
- Un breakout du range donne le signal que la tendance est confirmée.
- Lorsque le marché casse une résistance et reste plus de 4h au-dessus → il va atteindre le niveau suivant.
- Lorsque le marché casse une résistance et reste plus de 2h au-dessus → forte probabilité d'atteindre le prochain.
- Une cassure de trading range avec une bougie supérieure à toutes les autres du range = bon signal d'achat.
- Un couloir baissier cassé avec force et volume constitue un bon signal d'achat.
- Casser une résistance avec force combinée à une ombre inférieure confirme un excellent signal d'achat.
- Une résistance cassée devient un support — rebondir dessus confirme la force du mouvement.
- Une résistance se casse après plusieurs tests (le marché tape plusieurs fois avant de casser).

---

## Supports et résistances

- Tracer les supports depuis plusieurs périodes pour identifier les niveaux clés à casser.
- Un support qui résiste plusieurs fois (test 1, 2, 3) est un support intéressant.
- Si un support est cassé → forte probabilité d'une baisse supplémentaire.
- Chercher les hauts et bas précédents comme résistance et support.
- Construire un rectangle sur la zone d'accumulation/distribution passée pour identifier les vrais supports et résistances.
- Identifier les supports et résistances importants avant de décider d'une vente.
- Utiliser les hauts et bas pré-marché pour compléter les supports et résistances clés du chart quotidien.
- Une résistance qui se casse après plusieurs tests puis qui revient en pullback confirme la force du mouvement.

---

## Régimes de marché (Hidden Markov)

- Utiliser les modèles Hidden Markov pour détecter les 7 régimes : bullrun, crash, bruit, chop, et autres états.
- Identifier automatiquement le régime bullrun : périodes de revenus les plus positifs.
- Identifier les régimes de crash : périodes de revenus les plus négatifs.
- Vérifier la confiance du régime détecté pour connaître la probabilité réelle du régime en cours.

---

## Structure du marché du blé

- Le marché du blé respecte un couloir horaire précis qui se reproduit chaque jour.
- Une zone dormante sur les prix et les volumes précède toujours les mouvements d'impulsion du blé.
- Casser les anciens sommets (vieux high) avec force après une zone dormante confirme un signal d'achat.

---

## Structures récurrentes par marché

### Small caps (day 1 / day 2)
- Les marchés du jour 2 offrent plus d'avantages pour la vente à découvert que le jour 1.
- Le jour 1 offre plus d'avantages pour aller long, le jour 2 pour aller court.
- Setup A+ First Red Day : stock monte plusieurs jours de suite, puis premier jour rouge = court fort.
- Éviter les premiers jours rouges chaotiques — attendre le jour 2.

### ES / ZN
- Si le marché ouvre en dessous du pivot et de la clôture de la veille → chercher des signaux vendeurs.
- Si le marché ouvre au-dessus du pivot et de la clôture de la veille → chercher des signaux acheteurs.
- Quand le pivot et la clôture de la veille forment une bande (matelas) → support ou résistance très fort.

---

## Patterns graphiques clés

- Tracer un triangle de consolidation et attendre le breakout par le haut ou par le bas.
- Identifier un breakout de wedge : stock en consolidation sous une résistance puis breakout après retest du déclin.
- Un graphique se compose d'impulsions et de corrections alternées.
- La force d'une tendance se détermine par la profondeur du retracement de sa correction.
- Identifier le pattern ABCD : point A (début impulsion), B (fin impulsion/début correction), C (fin correction), D (fin impulsion suivante).
- Un pullback après cassure d'une zone de support confirme la validité du signal.
- Le marché pénètre un espace historiquement jamais atteint → surveiller le retrait avec mèche.
