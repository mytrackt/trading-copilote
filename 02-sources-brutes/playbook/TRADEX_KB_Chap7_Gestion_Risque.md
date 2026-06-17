# Chapitre 7 — Gestion du risque et money management

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 7.0 Pourquoi ce chapitre est le plus important

🟢 La gestion du risque est la seule variable que le trader contrôle totalement. Le prix, la direction, le timing — tout cela est incertain. Le montant risqué par trade, la taille de position, le stop-loss : ce sont des décisions entièrement sous contrôle du trader.

🟢 **Fait empirique documenté :** un trader avec un edge statistique positif (espérance mathématique \> 0\) peut perdre son capital s'il applique une mauvaise gestion du risque. Inversement, une gestion rigoureuse du risque peut préserver le capital même pendant une série de pertes inévitables.

🔵 **École classique (Van Tharp, Ralph Vince, Ed Seykota) :** la gestion du risque est le facteur primaire de survie à long terme — avant la méthode de trading elle-même.

---

## 7.1 Les fondamentaux mathématiques du risque

### 7.1.1 L'espérance mathématique (Edge)

🟢 **Formule de l'espérance :**

E \= (Taux de gain × Gain moyen) − (Taux de perte × Perte moyenne)

Exemple chiffré (illustratif) :

- Taux de gain : 45 %  
- Gain moyen : 2R (deux fois le risque unitaire)  
- Taux de perte : 55 %  
- Perte moyenne : 1R

E \= (0,45 × 2R) − (0,55 × 1R) \= 0,90R − 0,55R \= \+0,35R par trade

🟢 Une espérance positive ne garantit pas le profit sur chaque trade — elle garantit statistiquement le profit sur un grand nombre de trades, sous réserve que la taille de position ne compromette pas la survie lors des séries de pertes.

🔴 **À ne pas faire :** calculer l'espérance sur un échantillon \< 30 trades. Statistiquement non significatif. Minimum recommandé par les praticiens : 100 trades dans des conditions de marché homogènes.

### 7.1.2 Le ratio Risque/Rendement (RR)

🟢 **Définition :** rapport entre le gain potentiel ciblé et le risque accepté sur un trade.

RR \= (Prix cible − Prix d'entrée) / (Prix d'entrée − Stop-loss)

🟢 **Table de survie minimale selon le RR :**

| RR | Taux de gain minimum pour espérance nulle |
| :---- | :---- |
| 1:1 | 50,0 % |
| 1,5:1 | 40,0 % |
| 2:1 | 33,3 % |
| 3:1 | 25,0 % |
| 4:1 | 20,0 % |

🟡 **Convention importante :** un RR élevé n'est pas intrinsèquement supérieur. Un RR de 3:1 avec 25 % de taux de gain produit la même espérance qu'un RR de 1:1 avec 50 % de taux de gain. Ce qui compte : la combinaison RR × taux de gain réel sur l'actif et le TF cibles.

🔵 **École Belkhayate :** le COG cible naturellement des RR de 2:1 à 4:1 (entrée sur bande externe, cible ligne centrale ou bande opposée). 🔴 Cette affirmation nécessite validation backtest sur l'actif cible — non vérifiée universellement.

### 7.1.3 La notion de R (Risk Unit)

🟢 **R \= montant en devise risqué sur un trade.** Toutes les statistiques de trading s'expriment en multiples de R pour permettre la comparaison entre traders avec des capitaux différents.

Exemple : capital 10 000 $ — risque par trade 1 % \= R \= 100 $.

- Trade gagné à 2R \= \+200 $  
- Trade perdu \= −100 $  
- Série de 10 pertes consécutives \= −1 000 $ (−10 % du capital)

🟢 Exprimer les résultats en R élimine le biais de la taille du capital et permet de comparer des stratégies sur des périodes et des comptes différents.

---

## 7.2 Dimensionnement de position (Position Sizing)

### 7.2.1 La règle du pourcentage fixe

🟢 **Méthode standard :** risquer un pourcentage fixe du capital par trade.

Taille de position \= (Capital × % risque) / (Distance stop en ticks × Valeur du tick)

🟢 **Exemple sur Crude Oil Futures (CL) :**

- Capital : 50 000 $  
- Risque par trade : 1 % → R \= 500 $  
- Stop-loss : 30 ticks  
- Valeur du tick CL : 10 $ (1 tick \= 0,01 $ × 1 000 barils)

Taille \= 500 / (30 × 10\) \= 500 / 300 \= 1,67 contrat → arrondir à 1 contrat

🟡 **Convention de sécurité :** toujours arrondir à l'inférieur. Ne jamais arrondir à la hausse pour "récupérer" un trade précédent.

### 7.2.2 Pourcentage recommandé selon le niveau

🟡 Ces fourchettes sont des conventions de la communauté, pas des règles universelles vérifiées statistiquement :

| Profil | % risque par trade | Justification |
| :---- | :---- | :---- |
| Débutant (\< 1 an) | 0,25 % – 0,5 % | Préserver le capital pendant l'apprentissage |
| Intermédiaire | 0,5 % – 1 % | Standard industry |
| Expérimenté | 1 % – 2 % | Avec edge démontré sur 200+ trades |
| Professionnel | \> 2 % | Uniquement avec edge robuste et drawdown contrôlé |

🔴 **Mythe à déconstruire :** "risquer 5-10 % par trade pour récupérer rapidement les pertes." Une série de 10 pertes à 10 % de risque \= −65 % du capital (effet cumulatif). Mathématiquement destructeur.

### 7.2.3 La formule de Kelly et ses limites

🟢 **Critère de Kelly (formule originale) :**

f\* \= (bp − q) / b

Où :

- f\* \= fraction du capital à risquer  
- b \= ratio gain/perte moyen  
- p \= probabilité de gain  
- q \= probabilité de perte (1 − p)

🟢 **Exemple :** p \= 0,45 ; b \= 2 ; q \= 0,55

f\* \= (2 × 0,45 − 0,55) / 2 \= (0,90 − 0,55) / 2 \= 0,175 → 17,5 %

🔴 **Pourquoi Kelly pur est dangereux en trading :**

1. Il suppose que les paramètres (p, b) sont stables dans le temps — faux en trading.  
2. Il maximise la croissance géométrique mais produit des drawdowns extrêmes.  
3. En pratique, les traders utilisent **Half-Kelly** (f\*/2) ou **Quarter-Kelly** (f\*/4) pour réduire la volatilité du capital.

🟡 **Recommandation pratique :** utiliser Kelly uniquement comme borne supérieure théorique, jamais comme règle d'allocation directe.

---

## 7.3 Le Stop-Loss — Mécanique et placement

### 7.3.1 Pourquoi le stop-loss est non négociable

🟢 Le stop-loss est le mécanisme qui transforme une perte potentiellement illimitée en perte définie et acceptée à l'avance. Sans stop-loss, une seule position adverse peut détruire un compte entier.

🟢 **Sur les futures à fort levier (CL, ES, GC) :** un mouvement de 1 % du sous-jacent peut représenter 10 à 20 % du capital engagé en marge. Le stop-loss n'est pas une option — c'est une nécessité structurelle.

### 7.3.2 Méthodes de placement du stop-loss

🟢 **Stop basé sur la structure (recommandé) :** Placer le stop au-delà d'un niveau structural invalidant la thèse du trade (sous le dernier Higher Low en tendance haussière, au-dessus du dernier Lower High en tendance baissière).

Avantage : logique par rapport au marché. Inconvénient : distance variable → taille de position variable.

🟢 **Stop basé sur la volatilité (ATR) :**

Stop \= Prix d'entrée − (N × ATR(période))

N est conventionnellement entre 1,5 et 3 selon la tolérance au bruit.

🟡 L'ATR est calculé sur une période définie. Le choix de la période (14 bougies par défaut, Wilder 1978\) et du multiplicateur N doit être fixé avant utilisation et maintenu constant en backtest.

🟢 **Stop basé sur le Chande Kroll (vu Chap. 5\) :** Indicateur calculé comme stop dynamique adaptatif. Avantage : suit la tendance. Inconvénient : peut donner des stops trop larges en début de tendance.

🔴 **À éviter absolument :**

- Stop mental (non saisi dans la plateforme) — le biais émotionnel l'annule systématiquement.  
- Stop placé sur un niveau "rond" évident (ex. 80,00 $) — concentration de stops → cible pour stop-hunts.  
- Stop réduit après une perte pour "sauver" le trade — déplacement dans la mauvaise direction.

### 7.3.3 Le stop dynamique (Trailing Stop)

🟢 **Principe :** une fois le trade en profit, déplacer le stop progressivement pour protéger les gains, tout en laissant courir la tendance.

🟡 **Méthodes courantes :**

- **Trailing sur structure :** déplacer le stop sous chaque nouveau Higher Low confirmé (tendance haussière).  
- **Trailing sur ATR :** stop \= prix max atteint − N × ATR.  
- **Trailing sur Chande Kroll :** utiliser la valeur dynamique de l'indicateur.

🔵 **Compromis fondamental :** un trailing stop serré protège plus de profit mais sort plus tôt (avant la fin de la tendance). Un trailing stop large laisse courir mais rend plus de profit en cas de retournement. Il n'existe pas de réglage optimal universel — à backtester sur l'actif cible.

---

## 7.4 Le drawdown — Comprendre, mesurer, survivre

### 7.4.1 Définition et types

🟢 **Drawdown (DD) :** baisse du capital depuis un pic vers un creux, exprimée en pourcentage du capital au pic.

DD \= (Capital\_pic − Capital\_creux) / Capital\_pic × 100

🟢 **Maximum Drawdown (MDD) :** drawdown le plus profond observé sur la période analysée. Indicateur clé de risque d'une stratégie.

🟢 **Drawdown de récupération :** après un MDD de X %, le capital doit regagner plus que X % pour retrouver le niveau initial (asymétrie mathématique).

| Perte subie | Gain nécessaire pour récupérer |
| :---- | :---- |
| 10 % | 11,1 % |
| 20 % | 25,0 % |
| 30 % | 42,9 % |
| 40 % | 66,7 % |
| 50 % | 100,0 % |
| 60 % | 150,0 % |

🟢 Cette asymétrie est une vérité mathématique (pas une convention) : elle découle directement du calcul des rendements composés.

### 7.4.2 Drawdown et séries de pertes

🟢 **Probabilité d'une série de N pertes consécutives** avec un taux de perte q :

P(N pertes consécutives) \= q^N

Exemple : q \= 0,55 (55 % de trades perdants)

- 5 pertes consécutives : 0,55^5 \= 5,0 %  
- 7 pertes consécutives : 0,55^7 \= 1,5 %  
- 10 pertes consécutives : 0,55^10 \= 0,25 %

🟢 Une série de 10 pertes consécutives avec q \= 0,55 a une probabilité de 0,25 % — ce qui, sur 1 000 trades, **se produira presque certainement au moins une fois**.

🟡 **Implication pratique :** dimensionner le risque par trade de façon à survivre à la pire série statistiquement probable. Avec R \= 1 % et 10 pertes consécutives → DD \= 9,56 % (pertes composées). Acceptable. Avec R \= 5 % → DD \= 40,1 %. Potentiellement fatal.

### 7.4.3 Limites de drawdown — règles de circuit-breaker

🟡 Ces limites sont des conventions pratiques largement utilisées dans l'industrie :

| Seuil | Action recommandée |
| :---- | :---- |
| DD journalier \> 2R | Arrêt de trading pour la journée |
| DD hebdomadaire \> 4R | Réduction de la taille de position de 50 % |
| DD total \> 10 % du capital | Arrêt complet, review de la stratégie |
| DD total \> 20 % | Réinitialisation : retour au compte simulé |

🔵 Les prop firms (FTMO, TopstepTrader, etc.) imposent des limites similaires comme règles contractuelles. La discipline de ces limites est non négociable dans ce contexte.

---

## 7.5 Money Management — Systèmes avancés

### 7.5.1 Le système à taille fixe vs. taille variable

🟢 **Taille fixe (Fixed Fractional) :** risquer toujours le même % du capital. Avantage : simple, automatisable. L'effet composé fait croître la taille absolue avec le capital.

🟢 **Taille fixe en unités (Fixed Units) :** risquer toujours le même montant absolu (ex. toujours 200 $). Avantage : prévisibilité. Inconvénient : ne bénéficie pas de la croissance du capital.

🟡 **Martingale :** doubler la taille après chaque perte pour "récupérer". 🔴 Mathématiquement destructeur sur futures à levier — une série de pertes suffisamment longue dépasse toujours le capital disponible. À proscrire absolument.

🟡 **Anti-Martingale :** augmenter la taille après les gains, réduire après les pertes. Logiquement cohérent avec la gestion du capital. Variante : augmenter seulement après avoir établi un nouveau pic de capital (Optimal f, Ralph Vince).

### 7.5.2 Pyramidage (Scale-in / Scale-out)

🟢 **Scale-in (ajout de positions) :** ajouter des contrats à une position gagnante pour augmenter l'exposition dans la direction favorable.

🟢 **Règle de pyramidage sain :**

1. La position initiale doit être en profit avant tout ajout.  
2. Le stop de l'ensemble est ramené au seuil de rentabilité ou mieux.  
3. Chaque ajout est plus petit que le précédent (pyramide décroissante).

🔴 **Pyramidage inversé (positions égales ou croissantes) :** augmente le risque moyen par contrat à mesure que le prix s'éloigne. Dangereux si le marché se retourne.

🟢 **Scale-out (sortie partielle) :** clôturer une fraction de la position à la première cible, laisser courir le reste avec stop ramené au seuil de rentabilité. Avantage : sécurise une partie du profit tout en conservant un potentiel de continuation.

### 7.5.3 Le seuil de rentabilité (Break-Even Stop)

🟢 Déplacer le stop au prix d'entrée dès que le trade atteint 1R de profit. Résultat : le trade devient "gratuit" — la perte maximale est nulle (hors slippage et frais).

🟡 **Inconvénient :** le marché peut revenir au prix d'entrée (stop activé) avant de repartir dans la direction initiale. Ce comportement est courant sur les futures liquides — les pullbacks testent fréquemment les niveaux d'entrée.

🔵 **Compromis :** certains traders placent le BE stop légèrement en dessous du prix d'entrée (ex. −5 ticks) pour absorber le bruit de marché sans être stoppés sur un pullback technique.

---

## 7.6 Gestion du risque spécifique aux Futures

### 7.6.1 Marge et levier — mécanique réelle

🟢 **Marge initiale (Initial Margin) :** dépôt requis pour ouvrir une position. Fixé par la bourse (CME) et peut être modifié sans préavis.

🟢 **Marge de maintenance (Maintenance Margin) :** niveau minimum sous lequel le courtier émet un appel de marge (margin call). Si le capital tombe sous ce niveau, le courtier peut clôturer les positions de force.

🟢 **Exemple Crude Oil (CL) — valeurs approximatives 2025 (⚠️ vérifier sur CME Group avant utilisation) :**

- Valeur nominale d'1 contrat CL : \~80 000 $ (1 000 barils × \~80 $)  
- Marge initiale : \~6 000 – 8 000 $ (⏳ volatile selon conditions de marché)  
- Levier implicite : \~10:1 à 13:1

🔴 **Levier ≠ risque réel si le stop-loss est respecté.** Le levier détermine la sensibilité du P\&L aux mouvements de prix, pas le risque maximum — qui est défini par le stop-loss et la taille de position.

### 7.6.2 Rollover et coût de portage

🟢 **Rollover :** à l'approche de l'expiration du contrat actif, le trader doit "rouler" sa position vers le contrat du mois suivant. Coût \= différence de prix entre les deux contrats (basis).

🟢 **Date de rollover CL :** généralement \~3-4 jours ouvrables avant l'expiration du contrat actif. Le volume migre naturellement vers le contrat suivant — le rollover se fait quand le contrat suivant devient le plus liquide.

🟡 **Convention pratique :** surveiller le volume relatif entre contrat actif et contrat suivant. Rouler quand le volume du contrat suivant dépasse celui du contrat actif.

### 7.6.3 Risque de gap et risque overnight

🟢 **Gap :** différence de prix entre la clôture d'une session et l'ouverture de la suivante. Sur les futures avec session étendue (ETH), les gaps sont moins fréquents mais existent à l'ouverture RTH.

🟢 **Risque overnight :** positions tenues en dehors de la session principale sont exposées aux annonces économiques nocturnes (inventaires pétrole, décisions Fed, géopolitique). Le stop-loss ne protège pas contre un gap au-delà du niveau du stop (le remplissage se fait au prix de marché disponible).

🟡 **Pratique commune :** les day traders en scalping/intraday clôturent toutes les positions avant la fin de session RTH pour éviter le risque overnight. Décision à adapter selon la stratégie.

---

## 7.7 Le journal de trading — Outil de mesure du risque

### 7.7.1 Pourquoi le journal est indissociable de la gestion du risque

🟢 Sans mesure, il est impossible de savoir si l'edge est réel ou illusoire. Le journal de trading est l'outil de mesure de la performance réelle vs. la performance espérée.

🟢 **Champs minimum à enregistrer par trade :**

| Champ | Utilité |
| :---- | :---- |
| Date/heure d'entrée | Détection des patterns temporels |
| Actif \+ TF | Comparaison entre actifs/TF |
| Direction (long/short) | Biais directionnel |
| Prix d'entrée | Calcul exact du RR |
| Prix du stop initial | Calcul de R |
| Prix de la cible | RR théorique |
| Prix de sortie réel | RR réalisé |
| Résultat en R | Normalisation |
| Setup utilisé | Performance par setup |
| Contexte de marché | Range vs. tendance |
| Respect des règles (oui/non) | Discipline |
| Notes | Observations qualitatives |

### 7.7.2 Métriques à calculer périodiquement

🟢 **Métriques fondamentales :**

Taux de gain \= Nombre de trades gagnants / Nombre total de trades

RR moyen réalisé \= Somme des gains en R / Nombre de trades gagnants

Espérance \= (Taux de gain × RR moyen) − (Taux de perte × 1\)

Profit Factor \= Somme des gains bruts / Somme des pertes brutes

Maximum Drawdown \= Drawdown maximum observé sur la période

🟢 **Profit Factor :** ratio des gains totaux bruts sur les pertes totales brutes.

- \< 1,0 : stratégie perdante  
- 1,0–1,5 : stratégie marginale  
- 1,5–2,0 : bonne stratégie  
- 2,0 : excellente stratégie (rare et souvent sur-optimisée en backtest)

🔴 Un Profit Factor calculé sur \< 30 trades est statistiquement non significatif.

---

## 7.8 Les biais psychologiques qui sabotent la gestion du risque

🟢 **Biais de récence :** après une série de gains, sous-estimer le risque ("le marché est facile"). Après une série de pertes, sur-estimer le risque ("tout va mal"). Les deux altèrent le dimensionnement de position.

🟢 **Aversion à la perte (Kahneman & Tversky, 1979\) :** la douleur d'une perte est psychologiquement environ 2 fois plus intense que le plaisir d'un gain équivalent. Ce biais pousse à :

- Couper les gains trop tôt (pour sécuriser)  
- Laisser courir les pertes (pour éviter de "réaliser" la perte) → Résultat : exact inverse de ce que la gestion du risque recommande.

🟢 **Revenge trading :** après une perte, augmenter la taille pour "récupérer". Mécanisme psychologique documenté, mathématiquement destructeur.

🔵 **École comportementale (Kahneman, Thaler) :** ces biais sont cognitifs et résistants à la volonté. La solution n'est pas la discipline mentale seule — c'est la mise en place de règles mécaniques qui ne laissent pas de place à la décision émotionnelle (stop saisi dès l'entrée, taille calculée avant le trade).

---

## 7.9 Application dans TRADEX-AI

### 7.9.1 Paramètres de risque à intégrer dans le cerveau

| Paramètre | Valeur par défaut | Statut | Action |
| :---- | :---- | :---- | :---- |
| Risque par trade | 1 % du capital | 🟡 Convention | Configurable par utilisateur |
| RR minimum accepté | 2:1 | 🟡 Convention | Filtrer les setups \< 2:1 |
| DD journalier max | 2R | 🟡 Convention | Circuit-breaker automatique |
| DD total max | 10 % | 🟡 Convention | Alerte \+ réduction taille |
| Trailing stop méthode | Structure HH/HL | 🔵 À backtester | Comparaison ATR vs structure |
| Rollover CL | J−4 avant expiration | 🟢 CME standard | ⏳ Vérifier date exacte chaque mois |

### 7.9.2 Formule de calcul de taille de position pour TRADEX-AI

🟢 **Formule universelle (à implémenter dans le moteur de scoring) :**

Contrats \= floor( (Capital × %\_risque) / (Stop\_ticks × Valeur\_tick) )

Variables à récupérer :

- `Capital` : capital disponible (saisi par l'utilisateur)  
- `%_risque` : paramètre configurable (défaut 1 %)  
- `Stop_ticks` : distance en ticks entre entrée et stop (calculée par le signal COG)  
- `Valeur_tick` : fixe par contrat (CL \= 10 $, ES \= 12,50 $, GC \= 10 $)

🟡 `floor()` \= arrondi à l'inférieur — règle de sécurité non négociable.

### 7.9.3 Checklist risque avant tout signal TRADEX-AI

- [ ] Le RR théorique du setup est-il ≥ 2:1 ?  
- [ ] La taille de position est-elle calculée selon la formule ci-dessus ?  
- [ ] Le stop-loss est-il placé sur un niveau structural valide (pas arbitraire) ?  
- [ ] Le DD journalier actuel est-il sous la limite de 2R ?  
- [ ] Le DD total actuel est-il sous la limite de 10 % ?  
- [ ] S'agit-il d'un trade overnight ? (Si oui → alerte risque gap)  
- [ ] Le contrat actif est-il dans sa période de rollover ? (Si oui → attention liquidité)

---

## 7.10 Pièges fréquents en gestion du risque

🟢 **Sur-optimisation du stop :** placer le stop si serré que le bruit de marché l'active avant que le trade ait une chance de se développer. Résultat : taux de perte élevé même avec un bon edge.

🟢 **Incohérence du dimensionnement :** changer la taille de position selon l'humeur ou la "conviction" sur un trade. En dehors d'un système rigoureux, la conviction subjective est statistiquement non corrélée avec la probabilité réelle de succès.

🔴 **Double position après une perte :** forme de martingale déguisée. Si la stratégie a un edge, le dimensionnement normal récupère les pertes statistiquement. Si elle n'a pas d'edge, doubler accélère la ruine.

🟡 **Confusion entre drawdown de marché et drawdown de stratégie :** un drawdown pendant une phase de marché défavorable (ex. range serré sur stratégie de tendance) n'invalide pas la stratégie. Un drawdown hors des conditions normales d'utilisation de la stratégie doit déclencher une review.

🔵 **L'illusion du "je récupérerai" :** croire qu'une série de pertes doit statistiquement être suivie d'une série de gains (Gambler's Fallacy). Les trades sont indépendants — chaque trade a la même probabilité de gain indépendamment des trades précédents.

---

## 7.11 Synthèse du Chapitre 7

| Concept | Formule / Règle clé | Tag | Action TRADEX |
| :---- | :---- | :---- | :---- |
| Espérance | E \= (p × b) − (q × 1\) | 🟢 | Calculer sur 100+ trades réels |
| Taille de position | Capital × %R / (stop\_ticks × valeur\_tick) | 🟢 | Implémenter dans moteur |
| Stop sur structure | Au-delà du niveau structural invalidant | 🟢 | Règle de placement |
| Stop sur ATR | Entrée ± N × ATR(14) | 🟡 | N à backtester |
| Maximum Drawdown | (Pic − Creux) / Pic × 100 | 🟢 | Surveiller en temps réel |
| Asymétrie perte/gain | Perte 50 % → gain 100 % requis | 🟢 | Afficher dans dashboard |
| Kelly | f\* \= (bp − q) / b | 🟢 formule / 🔴 usage direct | Utiliser Half-Kelly max |
| Circuit-breaker DD | 2R/jour, 10 % total | 🟡 | Automatiser dans TRADEX |
| Profit Factor | Gains bruts / Pertes brutes | 🟢 | Métrique journal obligatoire |

🟡 **Règle TRADEX de gestion du risque :** calculer la taille AVANT d'analyser le setup. Un setup dont la taille correcte produit moins de 1 contrat entier est à ignorer (capital insuffisant pour ce marché).

---

## 7.12 Checklist avant d'intégrer une règle de risque dans TRADEX-AI

- [ ] La règle est-elle définie de façon non ambiguë et calculable automatiquement ?  
- [ ] Les données requises (capital, valeur tick, distance stop) sont-elles accessibles dans le système ?  
- [ ] La règle a-t-elle été validée en backtest sur l'actif cible ou est-elle taguée 🟡/🔵 ?  
- [ ] Le tag de fiabilité est-il appliqué à chaque paramètre de la règle ?  
- [ ] Les circuit-breakers sont-ils automatiques (non soumis à la décision humaine en temps réel) ?

---

*Chapitre 7 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-17* *Tout le contenu de ce chapitre est éducatif. Rien ici n'est du conseil financier. Les paramètres listés sont des conventions à adapter et backtester sur l'actif et le capital réels de l'utilisateur.*  
