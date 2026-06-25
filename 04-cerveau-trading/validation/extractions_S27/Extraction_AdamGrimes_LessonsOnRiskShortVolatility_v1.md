# Extraction AdamGrimes — Lessons On Risk Short Volatility
**Source :** `bundles/adamgrimes/lessons_on_risk_short_volatility.md` (HTTP 200) + 0 images certifiées
**Méthode images :** sans image · 0/0 certifiées · 0 à vérifier
**Décisions :** D6211 → D6230 · **Page :** https://www.adamhgrimes.com/lessons-on-risk-short-volatility/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Règles de gestion du risque, classification des produits financiers complexes, principe "no free lunch" comme filtre signal.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6211 — Ne jamais trader un produit incompris
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : Adam Grimes pose comme règle absolue de ne jamais trader un produit dont on ne comprend pas les mécanismes exacts (sous-jacent, structure, chaîne de dérivation). Dans le cas XIV/SVXY, les traders croyaient que "le produit monte quand la volatilité baisse" sans comprendre que le produit suivait des futures VIX, pas le VIX spot.
**TRADEX-AI C2** : Avant d'intégrer tout nouvel instrument dans le moteur, documenter explicitement le sous-jacent réel (ex : GC = futures or CME, pas un ETF or) et la chaîne de dérivation. Bannir tout instrument dont la mécanique est opaque.
*Catégorie : gestion_risque_entree*

### D6212 — Ne jamais trader une stratégie incomprise
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : La règle s'applique aussi à la stratégie : comprendre pourquoi elle génère un edge, pas seulement observer qu'elle "fonctionne". Les stratégies short volatilité semblaient profitables pendant des années uniquement parce que l'événement de perte extrême n'était pas encore survenu.
**TRADEX-AI C1** : Le moteur Belkhayate doit avoir une logique documentée pour chaque signal (pourquoi ce signal est valide), pas seulement un historique de gains. Tout signal dont la logique ne peut pas être expliquée doit être écarté.
*Catégorie : gestion_risque_entree*

### D6213 — Principe "no free lunch" : opportunité = risque inextricable
🟢 **FAIT VÉRIFIÉ** (Source : lessons_on_risk_short_volatility.md) : Il n'existe pas de rendement sans risque. Si une opportunité semble offrir un revenu stable avec peu ou pas de risque visible, c'est que le risque est présent mais non identifié. L'implosion XIV en une nuit (de 97$ à moins de 5$) après des années de gains apparents illustre ce principe.
**TRADEX-AI C5** : Tout signal TRADEX affichant une "confiance très haute" doit déclencher une revue du risque caché (VIX spike, news gate, liquidité). La confiance ≥ 90% ne supprime pas le risque — elle peut indiquer un biais de sur-confirmation.
*Catégorie : gestion_risque_entree*

### D6214 — Stratégies qui perdent rarement : pertes potentiellement catastrophiques
🟢 **FAIT VÉRIFIÉ** (Source : lessons_on_risk_short_volatility.md) : Les stratégies à haute fréquence de gains masquent des pertes rares mais de magnitude extrême. Si on "gagne presque toujours", les rares pertes peuvent effacer l'intégralité du compte. Ce n'est pas une probabilité marginale — c'est une caractéristique structurelle de la stratégie.
**TRADEX-AI C1** : Le circuit breaker TRADEX doit être calibré non seulement sur la fréquence des pertes mais sur leur magnitude maximale possible. Une configuration rare mais destructrice (ex : gap violent sur GC pendant NFP) doit être traitée comme certaine à long terme.
*Catégorie : gestion_risque_entree*

### D6215 — Plus de liens dans la chaîne = plus de façons de perdre
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : Chaque dérivé ajouté dans la chaîne (dérivé d'un dérivé d'un dérivé) multiplie les sources de perte indépendantes. Un trade directionnel simple sur une option a déjà plusieurs façons d'être perdant même si la direction est juste. Les ETN sur futures VIX sont un exemple extrême de cette complexité.
**TRADEX-AI C7** : Préférer les instruments les plus directs possible (futures GC, HG, CL, ZW) sur les ETF ou produits structurés. Chaque intermédiaire introduit un risque de base, un risque de tracking, un risque de liquidité propre.
*Catégorie : structure_marche*

### D6216 — La crédibilité sur les réseaux sociaux ne vaut rien sans vérification
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : Des "experts" short volatilité ont construit leur crédibilité sur des périodes favorables sans jamais avoir traversé un régime de marché adverse. Leurs disciples ont subi les pertes. La réputation sociale ne prouve pas la compétence réelle.
**TRADEX-AI C6** : Les signaux ou règles issus de sources non vérifiées par backtesting rigoureux sont taggués "NON SOURCÉ" dans la KB. La méthode Belkhayate est validée via ses propres fondements documentés, pas via popularité.
*Catégorie : psychologie*

### D6217 — La volatilité est un risque structurel, pas un indicateur de direction simple
🟢 **FAIT VÉRIFIÉ** (Source : lessons_on_risk_short_volatility.md) : Le VIX et ses dérivés ne se comportent pas linéairement. La volatilité réalisée peut exploser brutalement même après des années de compression. Le 5 février 2018, le VIX a doublé en quelques heures après une longue période de calme.
**TRADEX-AI C5** : VX (VIX) dans TRADEX est un actif de CONFIRMATION, pas de trading. Son rôle est de signaler un régime de risque. Un spike VIX ≥ seuil critique doit déclencher la suspension du mode Auto, indépendamment de la force du signal Belkhayate.
*Catégorie : indicateurs_momentum*

### D6218 — Lire le prospectus avant de trader un produit complexe
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : Le prospectus de XIV contenait 16 pages de risques. Peu de traders les ont lues avant de se positionner. Un investissement d'une heure de lecture aurait révélé des risques réels, pas seulement du "legalese".
**TRADEX-AI C2** : Avant d'intégrer une nouvelle source de données ou un nouveau type d'instrument dans TRADEX, documenter les risques de la source (ex : staleness risk ATAS, reconnection risk NT8, latence API). Ce travail de documentation est obligatoire avant le déploiement.
*Catégorie : gestion_risque_entree*

### D6219 — Le risque est le carburant du trading : comprendre sa nature exacte
🟡 **SYNTHÈSE** (Source : lessons_on_risk_short_volatility.md) : Le risque n'est pas l'ennemi — c'est la condition nécessaire pour générer du rendement. Le danger est le risque mal compris ou non quantifié. L'objectif du trader est de prendre "le bon type de risque, au bon moment, en bonne quantité".
**TRADEX-AI C1** : Le score signal TRADEX (/10) doit refléter non seulement la probabilité de la direction mais aussi la qualité du profil risque/récompense. Score ≥ 7 requis signifie que le R/R est acceptable ET que le risque est compris et maîtrisé.
*Catégorie : gestion_position_active*

### D6220 — Après un événement adverse : analyser pourquoi, adapter les garde-fous
🔵 **ÉCOLE** (Source : lessons_on_risk_short_volatility.md) : Si un trader a survécu à un événement dévastateur sans perte (par chance), c'est le moment d'intensifier la compréhension des risques — pas de continuer comme avant. Si le trader a subi des pertes, utiliser l'événement pour comprendre la cause structurelle et modifier les règles.
**TRADEX-AI C1** : Chaque perte réelle ou near-miss documentée dans TRADEX doit faire l'objet d'un post-mortem : quel garde-fou a manqué ? La liste des 32+ garde-fous (GARDE_FOUS_PROPOSES.md) doit être enrichie après chaque incident sérieux.
*Catégorie : psychologie*
