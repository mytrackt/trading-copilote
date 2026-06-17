# Chapitre 2 — Les fondamentaux des marchés futures (version technique enrichie)

**Statut :** support éducatif, pas un conseil financier. **Règle anti-hallucination :** chiffres marqués *(illustratif)* \= exemples pour comprendre un mécanisme, pas des données réelles. Les spécifications de contrat (tick, point, marge) font foi **uniquement sur la fiche officielle CME / ton broker** — jamais une valeur de mémoire pour engager de l'argent.

---

## 1\. C'est quoi un « contrat à terme » (future) ?

Un **future** est un contrat **standardisé** (taille, qualité, échéance fixées par la bourse) pour acheter/vendre un sous-jacent à un prix décidé aujourd'hui, pour une échéance future. Il se négocie sur une bourse réglementée (ex. **CME Group** pour les indices US) et passe par une **chambre de compensation** qui garantit que l'autre partie paiera (tu ne dépends pas de la solvabilité d'un inconnu).

**L'analogie du fellah :** l'agriculteur fixe aujourd'hui le prix de son blé livré dans 3 mois → il se protège de la baisse. Ce contrat est un future.

**En day trading :** tu ne reçois jamais la marchandise. Tu achètes/revends **le contrat lui-même** dans la journée et tu refermes tout avant la fin de séance.

### 1.1 Pourquoi tu ne reçois jamais la marchandise — le vrai mécanisme

Deux modes de **règlement à l'échéance** (important, souvent oublié) :

- **Règlement en espèces (cash-settled)** : à l'échéance, aucun bien ne change de main ; seul un solde en argent est échangé. → Cas des indices : **ES, NQ, MES, MNQ**. Il n'y a **rien** à livrer, même si tu oubliais de fermer.  
- **Livraison physique (physically delivered)** : à l'échéance, le détenteur devrait recevoir/livrer le bien réel (barils, lingots). → Cas du **pétrole (CL)** et de l'**or (GC)**.

👉 Conséquence pratique : sur CL et GC, tu **dois** fermer (ou rouler) avant l'échéance, sinon tu t'exposes en théorie à la livraison. En day trading tu refermes de toute façon chaque jour, donc le risque ne se pose pas — mais comprends la différence.

### 1.2 Long / Short : gagner à la hausse comme à la baisse

- **Long** \= tu achètes d'abord, tu espères que ça monte.  
- **Short (vente à découvert)** \= tu **vends d'abord** (le mécanisme du future le permet sans posséder le bien), tu espères que ça baisse pour racheter moins cher.

C'est l'avantage clé du future : un marché qui chute est une opportunité, pas seulement un danger.

---

## 2\. Échéances, codes et roulement (section absente du doc original — essentielle)

Un future **n'est pas éternel** : chaque contrat a une **date d'échéance**.

### 2.1 Le code complet d'un contrat

Symbole \= **racine \+ code du mois \+ année**. Exemple : `ESU6` \= ES, échéance **septembre 2026**.

**Codes de mois (standard CME) :**

| Mois | Code | Mois | Code |
| :---- | :---- | :---- | :---- |
| Janvier | F | Juillet | N |
| Février | G | Août | Q |
| Mars | **H** | Septembre | **U** |
| Avril | J | Octobre | V |
| Mai | K | Novembre | X |
| Juin | **M** | Décembre | **Z** |

Les indices (ES, NQ) utilisent le **cycle trimestriel** : **H (mars), M (juin), U (sept), Z (déc)**.

### 2.2 Le « roulement » (rollover) — le piège du débutant

À l'approche de l'échéance, le volume **migre** vers le contrat trimestriel suivant. La bascule se fait conventionnellement **\~8 jours avant** l'échéance (l'échéance des indices tombe le **3ᵉ vendredi** du mois).

⚠️ Erreur classique : continuer à trader l'ancien contrat la semaine du roulement → tu te retrouves sur un marché qui se vide (liquidité qui s'effondre). **Règle :** tu trades toujours le **contrat le plus actif (front month)**, et tu changes pendant la semaine de roulement. Ta plateforme indique souvent le contrat « actif » par défaut.

---

## 3\. Les contrats phares

| Symbole | Sous-jacent | Surnom | Règlement |
| :---- | :---- | :---- | :---- |
| **ES** | Indice S\&P 500 | « le ES » | Espèces |
| **NQ** | Indice Nasdaq-100 | « le NQ » | Espèces |
| **CL** | Pétrole brut (WTI) | « le crude » | Physique |
| **GC** | Or | « le gold » | Physique |

Le **ES** est le plus liquide et régulier → idéal pour débuter la lecture.

### Les MICRO contrats (pour débuter sans se ruiner)

Versions **10× plus petites** créées par le CME :

- **MES** \= micro S\&P 500 · **MNQ** \= micro Nasdaq · **MGC** \= micro or.

👉 On s'entraîne **toujours** sur les micros d'abord : une erreur y coûte 10× moins cher.

---

## 4\. Tick, point, multiplicateur, valeur du tick (LE cœur du chapitre)

### 4.1 Définitions

- **Tick** \= le plus petit cran de mouvement de prix autorisé. Le prix saute par crans (comme les graduations d'une règle), pas en continu.  
- **Point** \= unité de prix large \= plusieurs ticks.  
- **Multiplicateur** \= combien de dollars vaut **1 point entier** de mouvement. C'est lui qui « traduit » le prix en argent.

### 4.2 La formule universelle (à connaître par cœur)

Valeur d'un tick ($) \= taille du tick × multiplicateur

Avec cette formule tu **retrouves** la valeur de n'importe quel contrat sans la mémoriser :

| Contrat | Taille du tick | Multiplicateur | → Valeur du tick | Valeur d'1 point/unité |
| :---- | :---- | :---- | :---- | :---- |
| **ES** | 0,25 pt | 50 $/pt | **12,50 $** | 50 $ |
| **MES** | 0,25 pt | 5 $/pt | **1,25 $** | 5 $ |
| **NQ** | 0,25 pt | 20 $/pt | **5 $** | 20 $ |
| **MNQ** | 0,25 pt | 2 $/pt | **0,50 $** | 2 $ |
| **CL** | 0,01 $ | 1 000 $/$ (1 000 barils) | **10 $** | 1 000 $ |
| **GC** | 0,10 $ | 100 $/$ (100 onces) | **10 $** | 100 $ |

**Exemple ES :** tu achètes 1 ES, le prix monte de 2 points → 2 × 50 \= **\+100 $**. S'il baisse de 2 points → **−100 $**. En **MES**, le même mouvement \= **±10 $**.

⚠️ Ces valeurs sont stables depuis des années, mais **vérifie la fiche contrat** (CME / broker) avant de trader. Le multiplicateur, lui, ne change quasi jamais — c'est ton point d'ancrage pour tout calcul de risque (chapitre 9).

---

## 5\. La marge : trader « gros » avec « peu »

La **marge** n'est **pas** le prix du contrat : c'est un **dépôt de garantie** bloqué pour couvrir le risque.

**Analogie location de voiture :** une caution de 2 000 dh pour une voiture à 30 000 dh.

### 5.1 Les trois marges à distinguer

- **Marge initiale** : le dépôt exigé pour **ouvrir** la position. Fixée par la bourse via une **méthodologie de risque (type SPAN)** → elle **monte quand la volatilité monte**.  
- **Marge de maintenance** : le **minimum** à conserver sur le compte tant que la position est ouverte. Si ton solde passe dessous → **appel de marge (margin call)** : tu dois renflouer ou le broker **liquide** ta position automatiquement.  
- **Marge intraday (day-trade margin)** : bien **plus faible**, accordée par le broker **parce que tu fermes tout avant la nuit**. C'est elle qui permet de day-trader un ES avec quelques centaines de dollars *(montant variable selon broker et volatilité — pas un chiffre fixe)*.

---

## 6\. Le levier : valeur notionnelle et calcul réel

Le levier découle de la marge : un petit dépôt **contrôle** une grosse valeur. Pour le mesurer précisément :

Valeur notionnelle \= prix × multiplicateur

Levier ≈ valeur notionnelle ÷ marge déposée

**Exemple *(prix et marge illustratifs)* :**

- ES à **6 000** → notionnel \= 6 000 × 50 \= **300 000 $** contrôlés.  
- Marge intraday ≈ **500 $** → levier ≈ 300 000 ÷ 500 \= **\~600 pour 1**.  
- Conséquence : un mouvement de **0,2 %** du notionnel (≈ 600 $) **double ou efface** ta marge de 500 $.

Le levier **n'enrichit pas** : il **amplifie** ce que ton processus produit déjà. Processus perdant \+ levier \= ruine plus rapide. D'où : micros \+ simulateur \+ gestion du risque (chapitre 9\) **avant** tout levier réel.

⚠️ Le day trading avec levier fait perdre de l'argent à la **majorité** des débutants.

---

## 7\. Sessions et horaires

Les futures US se négocient **presque 24h/24**, du dimanche soir au vendredi soir (heure US), avec une **courte coupure de maintenance** quotidienne. Mais tout n'est pas bon à trader.

### 7.1 RTH vs ETH

- **RTH (Regular Trading Hours)** \= la séance « cash » américaine, **9h30 → 16h00 heure de New York**. C'est là que se concentrent **volume et meilleurs mouvements**.  
- **ETH (Extended/overnight)** \= le reste (séance électronique de nuit). Souvent **calme, fin, piégeux** → à éviter pour débuter.

### 7.2 Structure type d'une séance US *(tendance observée, pas une loi)*

- **Ouverture (1ʳᵉ heure, \~9h30–10h30 ET)** : volume et volatilité maximaux.  
- **Milieu de journée (\~12h–13h30 ET)** : « creux du déjeuner », volume plus faible, mouvements moins fiables.  
- **Dernière heure (\~15h–16h ET)** : le volume remonte souvent.

### 7.3 Conversion pour le Maroc (point vérifié)

Le Maroc est en **GMT+1 la majeure partie de l'année**. L'ouverture de New York (9h30 ET) tombe donc :

- **\~14h30** quand les USA sont en heure d'été (EDT),  
- **\~15h30** quand les USA sont en heure d'hiver (EST).

→ Ta **fenêtre de travail principale \= après-midi / soirée marocaine**. Pratique.

🌙 **Nuance Ramadan (à connaître) :** pendant le Ramadan (\~1 mois, dates variables selon le croissant lunaire — en **2026, du 15 février au 22 mars**), le Maroc **repasse à GMT+0** (horloges reculées d'1 h). Sur cette période, l'ouverture de New York tombe **1 h plus tôt** chez toi. **Vérifie les dates exactes chaque année.**

---

## 8\. La liquidité (et le slippage qui en découle)

**Liquidité** \= facilité à entrer/sortir **instantanément sans bouger le prix**, parce qu'il y a beaucoup d'acheteurs et de vendeurs en même temps.

**Analogie :** un souk bondé (le ES en pleine séance) → preneur en 1 seconde. Un village désert à 3h du matin (contrat exotique de nuit) → personne en face, ou à un prix bien pire.

### 8.1 Le carnet d'ordres (DOM) et le spread

- Le **DOM (Depth of Market)** affiche les ordres en attente à chaque prix, côté achat et côté vente.  
- Le **spread (bid-ask)** \= écart entre le meilleur prix d'achat et de vente. Sur un contrat très liquide comme le **ES en RTH**, ce spread est typiquement **d'1 tick** → coût d'entrée/sortie minimal.

### 8.2 Le slippage

Quand il manque de la liquidité au prix voulu, tu es exécuté **plus loin** : tu cliques pour vendre à 100, mais comme personne n'est là à 100, tu pars à 99,75 → **slippage** \= la différence perdue. C'est pire sur contrats peu liquides ou heures creuses. (Détaillé chapitre 3.)

👉 D'où la règle : contrats **très liquides** (ES, NQ) \+ **heures actives** (RTH) \= slippage minimal.

---

## 📖 Mini-glossaire enrichi

- **Future** : contrat standardisé d'achat/vente à prix fixé maintenant ; en day trading, revendu le jour même, sans livraison.  
- **Chambre de compensation** : organisme qui garantit l'exécution des deux côtés du contrat.  
- **Cash-settled / livraison physique** : règlement en argent (indices) vs en bien réel (CL, GC).  
- **Long / Short** : parier sur la hausse / sur la baisse (vente à découvert).  
- **Échéance** : date de fin de vie du contrat. **Roulement (rollover)** : bascule vers le contrat suivant quand le volume migre.  
- **Front month** : le contrat le plus actif/liquide, celui qu'on trade.  
- **Code de mois** : lettre désignant le mois d'échéance (H=mars, M=juin, U=sept, Z=déc…).  
- **Tick** : plus petit cran de prix. **Point** : plusieurs ticks.  
- **Multiplicateur** : $ par point entier. **Valeur du tick** \= taille du tick × multiplicateur.  
- **Valeur notionnelle** : prix × multiplicateur \= valeur réellement contrôlée.  
- **Marge initiale / maintenance / intraday** : dépôt pour ouvrir / minimum à garder / dépôt réduit pour le day trading.  
- **Appel de marge** : demande de renflouement sous peine de liquidation.  
- **Levier** : valeur notionnelle ÷ marge ; amplifie gains **et** pertes.  
- **RTH / ETH** : heures régulières US (9h30–16h ET) / séance de nuit.  
- **DOM (carnet d'ordres)** : ordres en attente à chaque prix.  
- **Spread (bid-ask)** : écart achat/vente ; coût caché.  
- **Slippage** : écart entre prix voulu et prix réellement exécuté.

---

## 🎯 4 points clés à retenir

1. En day trading tu traites **le contrat** (jamais la marchandise) et tu peux gagner **à la hausse comme à la baisse** ; les indices sont réglés en **espèces**, le pétrole/or en **physique**.  
2. Tout contrat a une **échéance** : tu trades le **front month** et tu fais attention au **roulement**.  
3. **Valeur du tick \= taille du tick × multiplicateur** : maîtrise cette formule avant tout, c'est la base du calcul de risque.  
4. On débute sur **micros**, en **heures actives (RTH \= après-midi au Maroc)**, sur contrats **liquides**, et **sur simulateur d'abord** ; le **levier** amplifie, il n'enrichit pas.

---

## ✏️ Exercice pratique (simulateur uniquement)

Sur ton compte démo, ouvre le **MES** :

1. Repère la **valeur du tick** affichée par la plateforme et **retrouve-la** avec la formule (0,25 × 5 \= 1,25 $).  
2. Note le prix, attends un mouvement de **10 ticks**, calcule à la main : **10 × 1,25 \= 12,50 $**.  
3. Refais le calcul **comme si** c'était 1 ES : **10 × 12,50 \= 125 $**. Ressens l'écart → c'est pourquoi on commence petit.  
4. **Bonus structure :** repère sur ta plateforme le **code d'échéance** du contrat MES affiché (ex. `MESU6`) et identifie le mois grâce au tableau des codes.

---

*Fin du Chapitre 2 (v2 technique). Prochain : Chapitre 3 — exécution, types d'ordres et slippage en détail.*  
