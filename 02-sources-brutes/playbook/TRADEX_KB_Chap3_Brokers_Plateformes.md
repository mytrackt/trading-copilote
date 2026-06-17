# TRADEX-AI · BASE DE CONNAISSANCES

# Chapitre 3 — Brokers & plateformes : l'interaction concrète (version technique enrichie)

**Statut :** ressource de connaissance interne pour le cerveau IA de TRADEX. **Portée :** universelle. Ce chapitre décrit l'infrastructure d'exécution **indépendamment de toute méthode** (il ne dépend ni de Belkhayate, ni d'aucune école). Les concepts (DOM, types d'ordres, slippage) valent pour n'importe quelle stratégie. **Règle anti-hallucination :** les noms de firmes, prix et règles changent **en permanence**. Tout élément périssable est marqué ⏳ et doit être **re-vérifié à la source officielle** avant usage. Aucun prix n'est garanti à jour. **Avertissement :** contenu éducatif. Ni conseil financier, ni recommandation de courtier. La majorité des débutants perdent de l'argent.

---

## 🏷️ LÉGENDE DES NIVEAUX DE FIABILITÉ

| Tag | Signification |
| :---- | :---- |
| 🟢 **FAIT** | Vrai par construction (mécanique de marché) ou documenté par plusieurs sources fiables. Stable dans le temps. |
| 🟡 **CONVENTION** | Usage / réglage standard, modifiable. |
| 🔵 **ÉCOLE / CHOIX** | Préférence ou pratique courante, pas une règle universelle. |
| ⏳ **VOLATILE** | Vrai à la date de rédaction (2026) mais **change vite** (prix, règles de prop firms, propriété d'une plateforme). À re-vérifier. |
| 🔴 **RED FLAG** | Signal d'arnaque ou claim non vérifiable. **Ne jamais présenter comme un fait.** |

---

## 3.0 — Pourquoi ce chapitre vieillit vite

🟢 **FAIT.** L'infrastructure (qui possède quelle plateforme, quelle prop firm existe, à quel prix) est un secteur à **très forte rotation** : rachats, fusions, faillites de prop firms, changements de règles mensuels. Les **mécaniques** (ordres, carnet, slippage) sont stables ; les **acteurs et tarifs** ne le sont pas. → L'IA TRADEX doit séparer le **durable** (🟢) du **périssable** (⏳).

---

## 3.1 — Qu'est-ce qu'un broker futures (🟢 FAIT)

Un **broker** (courtier) est l'intermédiaire qui transmet tes ordres à la bourse (ex. le CME) et détient ton compte.

Vocabulaire réglementaire (marché US, le plus important pour les futures) :

- **FCM** (*Futures Commission Merchant*) : entité **régulée** autorisée à détenir les fonds des clients et à acheminer les ordres. C'est le vrai « broker » au sens légal.  
- **IB** (*Introducing Broker*) : apporteur d'affaires qui te dirige vers un FCM mais ne détient pas tes fonds.  
- **Régulateurs US** : la **CFTC** (*Commodity Futures Trading Commission*, le gendarme fédéral) et la **NFA** (*National Futures Association*, l'autorité d'autorégulation). 🟢 Tout broker futures US sérieux est enregistré FCM auprès de la CFTC et supervisé par la NFA.

**Analogie :** le FCM est la **banque** qui garde ton argent et exécute tes virements ; l'IB est le **conseiller** qui t'a amené à cette banque.

🟢 **Vérification anti-arnaque :** l'enregistrement d'un broker US se contrôle gratuitement via l'outil **BASIC de la NFA**. Un « broker » non enregistré qui accepte tes fonds \= 🔴 red flag majeur.

---

## 3.2 — Brokers retail VS prop firms : la distinction essentielle

C'est le point le plus mal compris par les débutants. Ce sont **deux choses différentes**.

### A. Le broker retail classique (🟢 FAIT)

Tu déposes **ton propre argent**, tu trades **ton capital**, tu gardes **100 % de tes gains** et tu assumes **100 % de tes pertes**. Exemples de catégories : brokers spécialisés futures (NinjaTrader, AMP, Optimus, Tradovate, etc.) ou multi-actifs (Interactive Brokers, TradeStation…). ⏳ La liste évolue.

### B. La prop firm (*proprietary trading firm*, firme de financement)

🟢 **Modèle :** tu paies une **évaluation** (un « challenge ») ; si tu atteins un objectif de profit **sans casser les règles de risque**, la firme t'octroie un **compte financé** et tu partages les gains (souvent **100 % des premiers gains** puis un partage type **90/10**).

🟢 **POINT CAPITAL (souvent caché) :** une grande partie des comptes « funded » sont des **comptes simulés (SIM)**, même une fois « financés ». Les **données sont réelles** (vrai flux CME), mais tu ne trades **pas** du capital réel sur le marché : les **gains sont payés par la firme** sur ses fonds propres, pas issus d'un P\&L de marché. Certaines firmes basculent en **live (capital réel)** seulement à un stade avancé. → Toujours savoir si on est en SIM ou en live.

🟢 **Les 3 règles qui « tuent » le plus de candidats :**

1. **Trailing drawdown** (perte max glissante) : le seuil de perte **monte avec tes gains**. Variantes **EOD** (recalculé en fin de journée) vs **intraday** (recalculé en temps réel, plus sévère).  
2. **Consistency rule** (règle de régularité) : aucun jour ne doit représenter une part trop élevée du profit total (souvent un plafond du type 30–50 %). Beaucoup échouent dessus.  
3. **Daily loss limit** (perte journalière max) : dépassée → compte grillé.

⏳ **Paysage 2026 (snapshot, à re-vérifier) :** des firmes très citées incluent **Topstep, Apex Trader Funding, Take Profit Trader, MyFundedFutures, Tradeify, Lucid Trading, Elite Trader Funding, Earn2Trade**. Les prix d'évaluation se comptent souvent en **dizaines de dollars/mois** avec des promos fréquentes (−50 à −80 %). 🔴 **Ne jamais figer un prix précis comme « le » tarif** : ils changent chaque mois.

🔴 **Red flags prop firms :** payouts jamais honorés, règles modifiées rétroactivement, « consistency » floue, firmes sans historique de paiement vérifiable, marketing à base de « 80 % de réussite ». La firme **gagne quand tu échoues à l'évaluation** → conflit d'intérêt structurel à garder en tête.

---

## 3.3 — Les plateformes (logiciels de trading)

Le **broker** détient le compte ; la **plateforme** est le logiciel avec lequel tu vois les prix et passes les ordres. Parfois c'est le même groupe, parfois non.

### NinjaTrader 8 (🟢 / ⏳)

- 🟢 Plateforme **desktop Windows** de référence, fondée en **2003** (Raymond Deux, Chicago). Réputée pour son **SuperDOM** (carnet d'ordres cliquable ultra-rapide), son langage d'automatisation **NinjaScript (C\#)** et son **Strategy Analyzer** (backtest).  
- 🟢 Ne tourne **pas nativement sur macOS** (nécessite une virtualisation type Parallels) ; sinon version **web** ou **Tradovate**, moins riches.  
- ⏳ **Changement de propriété majeur :** NinjaTrader a été **racheté par Kraken** (grande plateforme crypto) pour **1,5 milliard $** (annoncé en mars 2025). NinjaTrader avait lui-même acquis **Tradovate**. Comptes désormais **unifiés** (mêmes identifiants NinjaTrader ↔ Tradovate). C'est un FCM régulé CFTC/NFA. → Vérifier l'état du groupe avant toute affirmation.

### Alternatives (🟢 / ⏳)

- **Tradovate** : plateforme **cloud** (navigateur \+ mobile), moderne, faible friction, très utilisée par les prop firms. Moins personnalisable que NinjaTrader. Idéale mobilité/débutant.  
- **Sierra Chart** : plateforme **puissante** pour traders avancés (graphiques **footprint** haute résolution, exécution via Rithmic). Pas d'app mobile. Courbe d'apprentissage raide.  
- **Quantower**, **WealthCharts** : autres options multi-broker.  
- **TradingView** : excellent pour le **graphique**, peut router des ordres vers certains brokers (exécution parfois légèrement plus lente que la plateforme native en forte volatilité).

🔵 **Choix (pas de « meilleure » plateforme universelle) :** automatisation/indicateurs custom → NinjaTrader/Sierra ; mobilité/simplicité/prop firm → Tradovate ; analyse graphique → TradingView. **Toutes** servent n'importe quelle méthode.

---

## 3.4 — Le flux de données (data feed) (🟢 FAIT)

Le prix qui s'affiche vient d'une chaîne : **Bourse → passerelle → plateforme**.

- **La bourse** (ex. **CME Globex** pour ES, NQ, CL, GC) produit la donnée officielle.  
- **Les passerelles d'exécution/données** professionnelles : **Rithmic**, **CQG**, ou le moteur propre de **Tradovate**. Elles routent tes ordres et te livrent le flux. 🟢 Une même plateforme peut fonctionner sur différentes passerelles, **non interchangeables** (changer de passerelle \= souvent re-souscrire).  
- **Temps réel vs différé :** la donnée temps réel CME est **payante** (abonnement market data, frais mensuels) ; le différé (delayed) est gratuit mais **inutilisable** pour scalper.  
- **Données SIM/démo :** la plupart des plateformes offrent du **temps réel simulé gratuit** pour s'entraîner.

🟢 **À retenir :** sur futures, ce flux est du **vrai volume centralisé** (cf. Chap. 4\) — bien plus fiable que le tick volume du Forex décentralisé. Mais une **latence** (délai) existe toujours entre la bourse et ton écran.

---

## 3.5 — Le DOM / carnet d'ordres (Depth of Market) (🟢 FAIT)

Le **DOM** (*Depth of Market*, profondeur de marché) ou **carnet d'ordres** est un tableau vertical qui montre, **à chaque niveau de prix**, le nombre de contrats en attente à l'achat et à la vente.

        PRIX      VENTE (ask)        ← ordres limites vendeurs en attente

        5802.00      120

        5801.75       85

        5801.50       40   ← meilleur ask (best offer)

       ─────────────────── écart (spread)

        5801.25       55   ← meilleur bid (best bid)

        5801.00       90

        5800.75      130

        PRIX      ACHAT (bid)         ← ordres limites acheteurs en attente

Notions clés :

- **BBO** (*Best Bid / Best Offer*) : le meilleur prix acheteur et le meilleur prix vendeur. L'écart entre les deux \= le **spread**.  
- 🟢 **Fournir vs prendre la liquidité :** un **ordre limite** se **pose** dans le carnet (il *fournit* de la liquidité, *maker*). Un **ordre au marché** **consomme** la liquidité disponible (il *prend*, *taker*).  
- **SuperDOM** : version cliquable du carnet (NinjaTrader) où l'on trade directement sur l'échelle de prix.  
- ⚠️ Le DOM affiche les ordres **visibles** ; certains gros acteurs cachent leur taille (*iceberg*) ou affichent des ordres qu'ils retirent (*spoofing*, illégal). → Le carnet **informe**, il ne dit pas la vérité absolue. (L'order flow approfondi \= Chap. 6.)

---

## 3.6 — Les types d'ordres (🟢 FAIT — à connaître par cœur)

| Ordre | Définition | Garantit… | Risque |
| :---- | :---- | :---- | :---- |
| **Market** (au marché) | Exécution immédiate au meilleur prix dispo | l'**exécution** | pas le **prix** (slippage) |
| **Limit** (limite) | S'exécute à un prix **fixé ou meilleur** | le **prix** | pas l'**exécution** (peut ne jamais se remplir) |
| **Stop / Stop-market** | Devient un ordre **au marché** quand le prix franchit un seuil | le déclenchement | slippage au déclenchement |
| **Stop-limit** | Devient un ordre **limite** au seuil franchi | prix max/min | peut **ne pas** se remplir si ça va trop vite |
| **MIT** (*Market if Touched*) | Ordre au marché déclenché quand un prix est touché | déclenchement | slippage |
| **Trailing stop** | Stop qui **suit** le prix à distance fixe | protège le gain qui court | se déclenche sur un simple recul |

**Le combo essentiel :**

- **Bracket order** : un ordre d'entrée **accompagné automatiquement** d'un **stop-loss** ET d'un **take-profit**. 🟢 Indispensable en day trading : ta sortie est définie **avant** d'entrer.  
- **OCO** (*One-Cancels-the-Other*) : deux ordres liés ; si **l'un s'exécute, l'autre s'annule**. C'est le mécanisme qui relie ton stop et ton objectif (quand l'un part, l'autre disparaît).

🔵 **Bonne pratique :** un débutant devrait travailler en **bracket/OCO systématique** → impossible d'« oublier » un stop.

---

## 3.7 — Slippage, commissions, exécution (🟢 FAIT)

### Slippage

🟢 Différence entre le prix **attendu** et le prix **réellement obtenu**. Plus fort sur : ordres **au marché**, **stops** déclenchés, marchés **rapides** (news) ou **peu liquides**. Un stop ne te protège pas au tick près : il garantit la sortie, pas le prix de sortie.

### Coût de transaction (« round-turn »)

🟢 Le coût total d'un aller-retour (ouverture \+ clôture) se décompose en :

1. **Commission broker** (par contrat, par côté ou par round-turn) ;  
2. **Frais de bourse** (exchange fees, fixés par le CME) ;  
3. **Frais réglementaires** (NFA). ⏳ Les montants varient selon broker et statut (micro vs mini). 🔴 Ne pas citer un chiffre précis comme universel.

🟢 **Impact en scalping :** plus tu trades court et souvent, plus le coût de transaction **mange** ton edge. Un setup à \+2 ticks d'espérance peut devenir **perdant** une fois commissions \+ slippage déduits. → toujours raisonner **net de frais**.

### Exécution & latence

🟢 **Latence** \= délai ordre→exécution. Affectée par ta connexion, la passerelle, la charge du marché. Pour le scalping, un **VPS** (serveur distant proche des serveurs de la bourse) réduit la latence. 🔵 Utile surtout en automatisation/haute fréquence, pas indispensable au débutant.

---

## 3.8 — Choisir son setup d'infrastructure (cadre neutre)

🔵 **Démarche recommandée (toute méthode confondue) :**

1. **Apprendre en SIM** d'abord, sur données temps réel gratuites — avant tout argent ou évaluation.  
2. Choisir une **plateforme** selon ton besoin (cf. 3.3), pas selon le marketing.  
3. Décider **retail (ton capital)** ou **prop firm (capital financé)** en connaissant le modèle SIM/live et les 3 règles tueuses.  
4. Vérifier l'**enregistrement réglementaire** (NFA BASIC).  
5. Calculer ton **coût round-turn net** et l'intégrer à ton espérance de gain (lien Chap. 8).

---

## 3.9 — Pièges & arnaques (🔴)

- 🔴 Broker **non régulé** qui détient tes fonds.  
- 🔴 Promesses de **gains garantis**, « signaux » payants à haut taux de réussite annoncé.  
- 🔴 Prop firms qui **ne paient pas**, changent les règles rétroactivement, ou cachent le caractère **SIM** des comptes.  
- 🔴 « Gourous » vendant une formation avec captures de gains non vérifiables.  
- 🟢 Règle de survie : **si quelqu'un gagne de l'argent en te vendant le rêve** (formation, évaluation, signaux), ses chiffres de performance sont à traiter comme **marketing**, pas comme preuve.

---

## 3.10 — Garde-fous pour le moteur IA de TRADEX

🟢 **Règles que l'IA doit appliquer :**

1. Séparer **mécanique durable (🟢)** et **acteurs/prix périssables (⏳)**. Pour tout prix ou règle de firme → « à vérifier à la source, change fréquemment ».  
2. **Ne jamais** recommander un broker/prop firm précis comme « le meilleur » → présenter des catégories \+ critères.  
3. Toujours préciser **SIM vs live** quand une prop firm est évoquée.  
4. Rappeler le **coût round-turn net** dès qu'une stratégie de scalping est chiffrée.  
5. Sur tout ordre : associer **stop-loss** (bracket/OCO) par défaut.  
6. Marquer tout chiffre de performance externe comme **non vérifié** tant qu'il n'est pas mesuré.

---

## 📒 MINI-GLOSSAIRE

- **FCM** : courtier régulé détenant les fonds (US). **IB** : apporteur d'affaires.  
- **CFTC / NFA** : régulateur fédéral US / autorité d'autorégulation.  
- **Prop firm** : firme de financement (évaluation → compte financé, souvent SIM).  
- **Trailing drawdown** : seuil de perte glissant (EOD vs intraday).  
- **Consistency rule / daily loss limit** : règles de régularité / perte journalière max.  
- **Plateforme** : logiciel de trading (NinjaTrader, Tradovate, Sierra Chart…).  
- **Data feed** : flux de données ; passerelles Rithmic / CQG / Tradovate ; source CME Globex.  
- **DOM / carnet d'ordres** : profondeur de marché par niveau de prix.  
- **BBO** : meilleur bid / meilleur ask. **Spread** : écart entre les deux.  
- **Maker / taker** : fournir (limite) / prendre (marché) la liquidité.  
- **Market / Limit / Stop / Stop-limit / MIT / Trailing** : types d'ordres.  
- **Bracket / OCO** : entrée \+ stop \+ objectif liés ; l'un annule l'autre.  
- **Slippage** : écart prix attendu / prix obtenu.  
- **Round-turn** : coût total aller-retour (commission \+ bourse \+ réglementaire).  
- **Latence / VPS** : délai d'exécution / serveur distant pour le réduire.

## 🎯 3 POINTS CLÉS

1. **Broker ≠ prop firm.** Retail \= ton capital, 100 % du risque et du gain. Prop firm \= capital financé (souvent SIM) sous des règles de risque strictes ; la firme a un conflit d'intérêt.  
2. **Le prix n'est pas garanti.** Market exécute mais subit le slippage ; limit garantit le prix mais pas l'exécution. Travaille en **bracket/OCO** (stop défini avant d'entrer).  
3. **Le net de frais décide.** Commissions \+ slippage peuvent transformer un edge brut en perte ; raisonne toujours coût round-turn inclus.

## 🏋️ EXERCICE (compte démo, sans argent réel)

Sur une plateforme en SIM temps réel (ES ou NQ) :

1. Ouvre le **DOM**. Identifie le **best bid**, le **best ask**, le **spread** en ticks.  
2. Place un **ordre limite** 3 ticks sous le marché → observe-le **se poser** dans le carnet (maker).  
3. Place un **bracket order** : entrée \+ stop-loss \+ take-profit. Vérifie que toucher l'un **annule** l'autre (OCO).  
4. Passe un **ordre au marché** en période calme puis (mentalement) imagine-le en pleine news → note la notion de **slippage**.  
5. **Aucun argent réel.** Objectif : maîtriser l'outil avant la méthode.

---

*Fin du Chapitre 3 — version technique enrichie, universelle, pour TRADEX-AI. Acteurs et tarifs \= ⏳ à re-vérifier. Éducation, pas conseil financier.*  
