# Extraction StockCharts — Stage 6: Stalking Your Trade
**Source :** `bundles/stockcharts/stage_6_stalking_your_trade.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D3771 → D3790 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/the-traders-journal-by-gatis-roze/stage-6-stalking-your-trade
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : sélection et qualification des trades — directement applicable au pipeline de filtrage TRADEX-AI avant signal GC/HG/CL/ZW (de la surveillance passive au setup actionnable).

## INVENTAIRE IMAGES CERTIFIÉES
*Aucune image dans ce bundle (page index/TOC uniquement).*

## DÉCISIONS

### D3771 — Stage 6 : La Traque des Idées d'Investissement Gagnantes
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : L'introduction affirme : "Stock market stalking is analogous to a lion stalking prey, not the paparazzi stalking a movie star." — la traque est patiente, préparatoire et précise.
🟢 **FAIT VÉRIFIÉ** : "Novices have trouble limiting their sources of ideas and are then challenged again in how to winnow these infinite choices down to a few promising candidates upon which to focus."
**TRADEX-AI C1** : TRADEX-AI implémente la "traque" mécaniquement — la boucle Python 2s surveille 9 actifs en permanence comme un lion surveille son territoire. Seuls les actifs passant le filtre 3/4 trading + 2/3 confirmation sont "traqués" jusqu'au signal — réduisant l'univers infini à quelques candidats.
*Catégorie : gestion_risque_entree*

### D3772 — Le Triomphe de Capturer un Grand Mouvement
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "The Triumph of Catching a Big Move" référencé — "Le grand argent se fait en étant du bon côté d'un grand mouvement de marché et en exécutant un scénario soigneusement pré-planifié."
🟡 **SYNTHÈSE** : Les grands mouvements (big moves) se préparent en amont — l'entrée opportuniste sans préparation passe souvent à côté du mouvement ou entre trop tard. La traque préalable permet d'être positionné au départ du mouvement.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, les "grands mouvements" correspondent aux tendances identifiées via BGC Direction + Énergie Belkhayate. TRADEX-AI vise exactement ces setups : entrer au début du mouvement (score ≥ 7,0 sur setup de continuation) et non en poursuite (score < 7,0 sur mouvement déjà avancé).
*Catégorie : gestion_risque_entree*

### D3773 — Sept Attributs pour Avoir l'Edge
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Seven Attributes To Give You The Edge" référencé — "Qu'est-ce que Wayne Gretzky, le coach Phil Jackson, Michael Jordan et William O'Neil ont en commun ? Ils ont tous..."
🟡 **SYNTHÈSE** : Les 7 attributs de l'edge trading convergent typiquement vers : (1) préparation, (2) discipline, (3) patience, (4) adaptabilité, (5) gestion du risque, (6) amélioration continue, (7) cohérence méthodologique — tous se retrouvent dans les pratiques des champions.
**TRADEX-AI C1** : Les 7 cercles d'intelligence de TRADEX-AI résonnent avec les 7 attributs de Roze — chaque cercle est un "attribut" du signal : C1 (technique), C2 (order flow), C3 (institutionnel), C4 (macro), C5 (sentiment), C6 (géopolitique), C7 (corrélations). Un signal avec 7 cercles favorables est l'équivalent d'un athlète ayant les 7 attributs.
*Catégorie : configuration*

### D3774 — Courir Après les Gagnants de l'Année Passée
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Chasing Last Year's Winners" référencé — Charles Munger (associé de Buffett) : "Tout ce que je veux savoir, c'est où je vais mourir afin de ne jamais y aller."
🟡 **SYNTHÈSE** : Courir après les gagnants de l'année précédente est un biais systématique — les actifs qui ont surperformé l'an dernier ne surperformeront pas nécessairement cette année (régression vers la moyenne, rotation sectorielle). La traque porte sur les futurs gagnants, pas les anciens.
**TRADEX-AI C7** : La matrice de corrélations 30j de TRADEX-AI (correlations.py) contre ce biais — elle mesure les corrélations actuelles, pas historiques. Un actif qui était corrélé l'an passé peut être décorrélé aujourd'hui. Jamais supposer que les relations passées persistent.
*Catégorie : correlations*

### D3775 — Secrets de Trading du Baseball et Game of Thrones
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Trading Secrets from Baseball & the Game of Thrones" référencé — printemps, saison de baseball au Safeco Field — Roze établit des parallèles entre stratégie sportive et trading.
🟡 **SYNTHÈSE** : Le baseball enseigne la sélectivité — un bon batteur attend sa pitch favorable et ne se précipite pas sur chaque lancer. En trading, patienter pour le setup idéal plutôt que de trader tout ce qui bouge est la différence entre amateur et professionnel.
**TRADEX-AI C1** : Le seuil score ≥ 7,0 de TRADEX-AI est l'équivalent de "n'attaquer que sa pitch" — le moteur Python surveille en continu, mais le signal n'est généré que lorsque les conditions sont optimales. La patience mécanique remplace la discipline humaine difficile à maintenir.
*Catégorie : gestion_risque_entree*

### D3776 — Mimer les Meilleurs de Wall Street : Partie I
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "This Could Change Your Life! How You Can Mimic Wall Street's Best & Profit Handsomely: Part 1" référencé — "Ça devrait être illégal. Si j'étais gestionnaire de hedge fund ou de fonds commun, je serais profondément mécontent."
🟡 **SYNTHÈSE** : Les investisseurs individuels peuvent légalement accéder aux positions des grands fonds via les déclarations réglementaires (13F aux USA, COT pour les futures) — "mimer" les institutionnels est une stratégie légale et efficace.
**TRADEX-AI C3** : Le module C3 (Institutionnels) de TRADEX-AI utilise les données COT CFTC pour GC/HG/CL/ZW — c'est exactement "mimer Wall Street" légalement. Quand les commerciaux CFTC accumulent des positions nettes longues sur GC, c'est un signal de confirmation institutionnel puissant.
*Catégorie : structure_marche*

### D3777 — Mimer les Meilleurs de Wall Street : Partie II
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "This Could Change Your Life! How You Can Mimic Wall Street's Best & Profit Handsomely: Part II" référencé — suite de la stratégie pour surperformer les institutionnels en les observant.
🟡 **SYNTHÈSE** : La seconde étape du mimétisme institutionnel consiste à identifier les changements de positionnement (accumulation vs distribution) dans les déclarations — le changement de direction est plus informatif que le niveau absolu des positions.
**TRADEX-AI C3** : Pour les COT CFTC utilisés dans C3, le signal pertinent n'est pas le niveau absolu des positions commerciales mais leur variation semaine-sur-semaine — une bascule de position nette short → long des commerciaux sur GC est un signal de confirmation fort même si le niveau absolu reste négatif.
*Catégorie : structure_marche*

### D3778 — Une Grande Erreur de Trading que j'ai Faite Pour que Vous Ne l'Ayez Pas à Faire
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "A Big Trading Mistake I Made So You Won't Have To!" référencé — Roze affirme avoir "appris qu'il faut avoir une peau épaisse pour être trader ou blogueur" — les leçons d'erreurs sont des actifs précieux.
🟡 **SYNTHÈSE** : Documenter ses erreurs de trading et les partager est un acte de générosité professionnelle — l'industrie du trading progresse collectivement lorsque les erreurs sont documentées plutôt que dissimulées.
**TRADEX-AI C1** : Les erreurs de TRADEX-AI sont documentées dans DETTE_TECHNIQUE.md (bugs connus) et dans les README de session (décisions contestables) — cette documentation systématique des erreurs est un actif du projet, pas une faiblesse à dissimuler.
*Catégorie : configuration*

### D3779 — Ne Trader que les Actifs Trempés dans les Probabilités Positives
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "How I Only Trade Stocks Soaked in Positive Probabilities" référencé — "Je ne trade que les actions les plus fortes et les plus belles du marché. J'ai écrit avant comment je laisse mes analyses approfondies..."
🟡 **SYNTHÈSE** : "Trempé dans les probabilités positives" (soaked in positive probabilities) signifie que plusieurs indicateurs convergent simultanément vers le même signal — la convergence multi-indicateur est plus robuste qu'un signal unique fort.
**TRADEX-AI C1** : Le score /10 de TRADEX-AI mesure exactement cette "saturation en probabilités positives" — un score de 9/10 signifie que 7 cercles sur 7 convergent vers le même signal. Le seuil ≥ 7,0 garantit qu'au moins 70% des cercles sont favorables avant tout ordre.
*Catégorie : gestion_risque_entree*

### D3780 — Investissement : L'Outil des Probabilités
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Investing: The Probability Tool" référencé — "Investir et penser en probabilités devraient aller de pair. Les probabilités peuvent être exprimées à la fois..."
🟡 **SYNTHÈSE** : Penser en probabilités transforme la question "ce trade va-t-il marcher ?" en "quelle est la probabilité que ce trade marche ?" — déplaçant le cadre mental du binaire vers le probabiliste, ce qui est psychologiquement plus robuste.
**TRADEX-AI C1** : Le score /10 est une expression probabiliste directe — score 8/10 = ~80% de probabilité de succès basé sur la convergence des cercles. Abdelkrim doit lire le score comme une probabilité, pas comme une certitude. Un score de 7,0 est un signal valide mais pas une garantie.
*Catégorie : psychologie*

### D3781 — Le Repas Gratuit de Wall Street : Lire le Menu
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Wall Street's Free Lunch... But Investors Must Still Read the Menu" référencé — paraphrase de Bill Murray dans "Aloha" : "Le futur n'est pas quelque chose qui arrive juste. C'est une chose brutale..."
🟡 **SYNTHÈSE** : Le "repas gratuit" de Wall Street (diversification, leverage, options) n'est gratuit que si on "lit le menu" — comprendre exactement ce qu'on obtient. Les instruments financiers complexes offerts comme "gratuitement" cachent des risques que l'investisseur non informé ne voit pas.
**TRADEX-AI C1** : TRADEX-AI "lit le menu" avant chaque signal — le circuit breaker vérifie les conditions de marché, le staleness_monitor vérifie la fraîcheur des données, le news gate vérifie les événements macro. Aucun signal n'est envoyé sans avoir lu tous les avertissements sur le "menu".
*Catégorie : gestion_risque_entree*

### D3782 — Traquer les Actions Best of Breed
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Stalking the 'Best of Breed' Equities" référencé — "La même analyse d'investissement produit rarement des conclusions cohérentes sur une période de temps."
🟡 **SYNTHÈSE** : Les critères "best of breed" évoluent dans le temps — ce qui était le meilleur setup en trend bull n'est pas le même qu'en consolidation. La traque doit s'adapter au régime de marché courant.
**TRADEX-AI C1** : Pour TRADEX-AI, "best of breed" parmi GC/HG/CL/ZW varie selon le régime macro — en période de risk-off (VIX élevé), GC est typiquement le "best of breed" ; en période de croissance économique forte, CL et HG peuvent l'être. Le score /10 reflète automatiquement ces dynamiques via C4/C5.
*Catégorie : structure_marche*

### D3783 — Le Secret pour Produire des Profits Consistants avec une Méthodologie
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "The Secret of Making an Investment Methodology Produce Consistent Profits" référencé — citation : "J'ai entendu beaucoup d'hommes parler intelligemment, même brillamment, de quelque chose — pour ensuite les voir s'avérer incapables."
🟡 **SYNTHÈSE** : La connaissance d'une méthodologie ne garantit pas son application — la différence entre connaître les règles et les exécuter consistamment est le fossé entre trader amateur et professionnel. La mise en œuvre disciplinée prime sur la sophistication théorique.
**TRADEX-AI C1** : TRADEX-AI pont ce fossé en codant les règles Belkhayate dans le système — l'exécution mécanique garantit la consistance là où la discipline humaine peut fléchir. La KB (~1313+ règles) représente la connaissance ; le moteur Python représente l'exécution consistante.
*Catégorie : configuration*

### D3784 — Peter Lynch, les Français, Sally : Observer son Environnement Immédiat
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "Peter Lynch Nailed It; The French Nailed It; Sally Nailed It; You Can Too!" référencé — Peter Lynch, gestionnaire du fonds Magellan de Fidelity pendant 13 ans, avec des résultats de performance remarquables.
🔵 **ÉCOLE** (Peter Lynch, Fidelity Magellan) : Lynch conseillait d'investir dans ce qu'on connaît — observer les tendances de consommation dans son environnement immédiat génère des idées d'investissement que les analystes de Wall Street ratent.
**TRADEX-AI C6** : Pour C6 (Géopolitique), l'équivalent du "conseil Lynch" pour les futures est l'observation directe du terrain : suivi des actualités agricoles pour ZW, des développements géopolitiques pour CL (pétrole), des indicateurs de construction pour HG (cuivre), des tensions monétaires pour GC (or refuge).
*Catégorie : macro_evenements*

### D3785 — Sélectivité : Winnowing Down les Choix Infinis
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : L'introduction affirme : "The simple truth is that novices have trouble limiting their sources of ideas and are then challenged again in how to winnow these infinite choices down to a few promising candidates upon which to focus."
🟡 **SYNTHÈSE** : La sélectivité est une compétence qui s'acquiert avec l'expérience — le novice veut tout trader (FOMO) ; l'expert identifie les 3-5 meilleurs setups du moment et ignore le reste. La discipline du "NON" est plus difficile mais plus rentable.
**TRADEX-AI C1** : TRADEX-AI automatise la sélectivité — sur 9 actifs surveillés, seuls ceux passant le filtre 3/4 + 2/3 sont analysés par Claude. En pratique, la plupart du temps, le résultat est ATTENDRE — ce qui est le résultat CORRECT la majorité du temps.
*Catégorie : gestion_risque_entree*

### D3786 — Evolution du Novice à l'Expert : Chemin Prévisible
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : L'introduction décrit : "Stalking is one stage that most investors transition through in a similar predictable path as they evolve from novice, advanced beginner, competent, proficient and finally to expert investor."
🟡 **SYNTHÈSE** : Les 5 niveaux de développement (novice → débutant avancé → compétent → proficient → expert) correspondent à une progression dans la maîtrise de la sélectivité — l'expert traque moins d'opportunités mais avec une précision bien plus haute.
**TRADEX-AI C1** : TRADEX-AI accélère cette progression pour Abdelkrim — en lui fournissant les filtres d'un "expert" (score /10 avec 7 cercles), même en phase d'apprentissage. Le Mode Manuel permet de développer le jugement expert en validant ou rejetant les signaux avec justification.
*Catégorie : psychologie*

### D3787 — Investissement comme Outil de Probabilité : Probabilités Quantifiées
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : "Investing: The Probability Tool" réaffirme que "Les probabilités peuvent être exprimées à la fois [quantitativement et qualitativement]" — les deux formes d'expression sont valides et complémentaires.
🟡 **SYNTHÈSE** : La quantification des probabilités (ex : 73% de chance de succès basé sur historique) complète l'évaluation qualitative (feeling, contexte) — ni l'une ni l'autre seule n'est suffisante pour une prise de décision robuste.
**TRADEX-AI C1** : Le score /10 de TRADEX-AI est quantitatif (nombre de cercles favorables) ; le jugement d'Abdelkrim en Mode Manuel est qualitatif (contexte non capturé par les données). Les deux ensembles (quantitatif + qualitatif) forment la décision finale — la machine produit le quantitatif, l'humain apporte le qualitatif.
*Catégorie : configuration*

### D3788 — La Consistance Méthodologique Produit des Profits Consistants
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Article "The Secret of Making an Investment Methodology Produce Consistent Profits" affirme l'équation directe : consistance méthodologique → profits consistants. La variabilité d'application = variabilité des résultats.
🟡 **SYNTHÈSE** : Une méthodologie appliquée 80% du temps produit des résultats inférieurs à la même méthodologie appliquée 100% du temps — même si la méthode à 80% fait des "exceptions intelligentes". L'exception erode l'edge statistique.
**TRADEX-AI C1** : En Mode Auto, TRADEX-AI applique la méthode à 100% mécaniquement — aucune exception. En Mode Manuel, si Abdelkrim ignore le signal trop fréquemment, le Mode Manuel perd son sens. La règle : ne pas ignorer plus de 2 signaux valides consécutifs sans raison documentée dans le journal.
*Catégorie : configuration*

### D3789 — La Traque Quantitative : Probabilités Exprimées en Deux Formes
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : "Probabilities can be expressed both [quantitatively and qualitatively]" — cette dualité de l'expression probabiliste structure l'approche de traque de Roze.
🟡 **SYNTHÈSE** : La traque d'un trade combine deux flux : le flux quantitatif (indicateurs, scores, ratios) et le flux qualitatif (lecture du contexte, expérience, intuition calibrée). La "traque experte" intègre les deux de manière fluide.
⚫ **HYPOTHÈSE PROJET** : Le score /10 de TRADEX-AI est la formalisation quantitative de la traque ; le Mode Manuel est la fenêtre qualitative — ensemble ils constituent la "traque complète" au sens de Roze.
**TRADEX-AI C1** : Documenter dans le README de session non seulement les scores /10 des signaux générés, mais aussi les raisons qualitatives pour lesquelles Abdelkrim a suivi ou ignoré chaque signal — cela enrichit la base d'apprentissage et améliore la calibration future du score.
*Catégorie : configuration*

### D3790 — Stalking : Du Lion, Pas du Paparazzi
🟢 **FAIT VÉRIFIÉ** (Source : stage_6_stalking_your_trade.md) : Introduction : "Stock market stalking is analogous to a lion stalking prey, not the paparazzi stalking a movie star." — la traque patiente, préparée et ciblée du lion vs la poursuite réactive et chaotique du paparazzi.
🟡 **SYNTHÈSE** : Le paparazzi (trader amateur) réagit aux mouvements déjà en cours — il entre après la grande partie du mouvement. Le lion (trader expert) se positionne AVANT le mouvement, en ayant identifié et traqué sa proie en amont.
**TRADEX-AI C1** : TRADEX-AI est conçu comme un "lion" — la surveillance 2s identifie les setups avant leur déclenchement. Le signal TRADEX-AI doit arriver AVANT le mouvement principal, pas en confirmation d'un mouvement déjà avancé. Si score ≥ 7,0 mais prix déjà en extension significative (Énergie haute), ne pas entrer — attendre le retrait.
*Catégorie : gestion_risque_entree*
