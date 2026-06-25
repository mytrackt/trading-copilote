# Extraction NinjaTrader — Common Mistakes When Using RSI Indicators in Futures
**Source :** `bundles/ninjatrader/common_mistakes_when_using_rsi_indicators_in_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7651 → D7670 · **Page :** https://ninjatrader.com/futures/blogs/common-mistakes-when-using-rsi-indicators-in-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : 5 erreurs critiques RSI en futures — filtrage des faux signaux et usage correct comme indicateur de confirmation dans le moteur TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune image sur la page source)*

---

## DÉCISIONS

### D7651 — RSI défini comme mesure de vitesse et probabilité des mouvements de prix
🔵 **ÉCOLE** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Le RSI (Relative Strength Index) mesure la vitesse et la probabilité des mouvements de prix d'un actif — utile pour identifier si un actif est suracheté ou survendu et si un retournement est probable à court terme.
**TRADEX-AI C1** : Dans le moteur TRADEX, le RSI est un indicateur de confirmation C1 — il sert à identifier tendances, divergences et niveaux S/R potentiels mais jamais comme signal unique d'achat/vente.
*Catégorie : indicateurs_momentum*

### D7652 — Erreur #1 : Trop s'appuyer sur le RSI seul
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Le RSI seul ne fournit pas de signaux d'achat/vente clairs — utilisé isolément, il conduit à des positions précaires. Les météorologues ne regardent pas uniquement le baromètre.
**TRADEX-AI C1** : Règle absolue TRADEX : le RSI n'est jamais un déclencheur de signal isolé. Il doit être croisé avec moyennes mobiles, MACD et trendlines pour confirmer un setup — conformément à la règle 3/4 + 2/3 actifs alignés.
*Catégorie : indicateurs_momentum*

### D7653 — Solution erreur #1 : RSI comme pièce d'un puzzle plus large
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Le RSI doit être considéré comme un élément parmi d'autres — croiser avec moving averages, MACD, trendlines pour surmonter les faux signaux et obtenir une vision holistique du marché.
**TRADEX-AI C1** : Le cerveau Claude analysant via la KB doit pondérer le RSI comme un cercle C1 parmi les 7 cercles d'intelligence — contribution au score /10 mais jamais critère isolé éliminatoire positif.
*Catégorie : indicateurs_momentum*

### D7654 — Erreur #2 : Ignorer la tendance globale du marché
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Une forte tendance haussière peut maintenir le RSI en zone surachetée (>70) pendant longtemps, poussant les traders à sortir prématurément de positions gagnantes. La tendance globale influence fortement la lecture du RSI.
**TRADEX-AI C1** : Sur GC ou CL en forte tendance directionnelle, un RSI >70 ne déclenche pas automatiquement un signal VENDRE — TRADEX doit d'abord vérifier la tendance macro (C4) et la confirmation ES/DX (C4) avant d'interpréter le RSI.
*Catégorie : indicateurs_tendance*

### D7655 — Solution erreur #2 : Utiliser RSI pour identifier les pullbacks, pas les tops/bottoms
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : En marché tendanciel, le RSI est plus utile pour identifier des pullbacks à l'intérieur de la tendance que pour détecter des tops ou bottoms absolus.
**TRADEX-AI C1** : Règle de lecture RSI en tendance : sur GC haussier, un RSI revenant de 70 vers 50 signale un pullback potentiel d'entrée — pas un renversement majeur. TRADEX doit contextualiser la lecture selon la direction de tendance C1.
*Catégorie : timing*

### D7656 — Erreur #3 : Interpréter les niveaux RSI comme conditions absolues
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : RSI <30 ne signifie PAS que le marché est automatiquement survendu et prêt à remonter. RSI >70 ne signifie PAS surachat absolu. Les marchés peuvent rester en territoire extrême longtemps en tendance forte.
**TRADEX-AI C1** : Le moteur TRADEX ne doit jamais déclencher un signal ACHETER sur simple RSI <30 ou VENDRE sur RSI >70 — ces niveaux sont des alertes à surveiller, pas des déclencheurs automatiques.
*Catégorie : indicateurs_momentum*

### D7657 — Solution erreur #3 : RSI comme alerte pour chercher des setups, non comme signal absolu
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Il faut penser aux niveaux RSI comme des alertes pour commencer à chercher des setups potentiels — pas comme des signaux absolus d'achat ou de vente.
**TRADEX-AI C1** : Implémentation TRADEX : RSI en zone extrême (<30 ou >70) = flag interne pour déclencher une analyse approfondie via le cerveau Claude — score /10 calculé sur l'ensemble des cercles, pas seulement sur le RSI.
*Catégorie : configuration*

### D7658 — Erreur #4 : Même période RSI pour tous les marchés
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Utiliser la même période RSI par défaut (généralement 14) pour tous les marchés et timeframes est une erreur fréquente — différents actifs et timeframes nécessitent des paramètres RSI distincts pour des signaux précis.
**TRADEX-AI C1** : Les paramètres RSI dans settings.py doivent être customisés par actif : GC (or) ≠ CL (pétrole) ≠ ZW (blé) ≠ HG (cuivre) — périodes plus courtes = plus de faux signaux ; périodes plus longues = lag accru.
*Catégorie : indicateurs_momentum*

### D7659 — Solution erreur #4 : Personnaliser la période RSI par actif et timeframe
🔵 **ÉCOLE** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Personnaliser la période RSI selon l'actif spécifique et le timeframe tradé — les périodes courtes génèrent plus de faux signaux, les périodes longues lagguent derrière les mouvements de prix.
**TRADEX-AI C1** : À documenter dans settings.py : définir RSI_PERIOD_GC, RSI_PERIOD_HG, RSI_PERIOD_CL, RSI_PERIOD_ZW avec des valeurs calibrées sur range bars NT8 — à valider en backtest avant déploiement.
*Catégorie : indicateurs_momentum*

### D7660 — Erreur #5 : Ignorer les divergences RSI
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Quand le RSI se déplace en direction opposée au prix, c'est un signal potentiel de retournement — les traders qui ignorent ces divergences se retrouvent souvent du mauvais côté du marché.
**TRADEX-AI C1** : Les divergences RSI/prix (bullish ou bearish) doivent être détectées par le moteur Python TRADEX et transmises au cerveau Claude comme élément clé C1 — surtout quand elles coïncident avec d'autres signaux techniques.
*Catégorie : indicateurs_momentum*

### D7661 — Solution erreur #5 : Surveillance des divergences coïncidant avec d'autres signaux
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Surveiller les divergences attentivement, surtout quand elles coïncident avec d'autres signaux techniques. Exemple : actif en downtrend + divergence haussière (prix = lower lows, RSI = higher lows) = signal de retournement potentiel.
**TRADEX-AI C1** : Règle de détection divergence : si GC fait un lower low ET que le RSI fait un higher low simultanément → flag divergence bullish → déclencher analyse complète Claude avec ce contexte comme élément prioritaire du prompt.
*Catégorie : configuration*

### D7662 — RSI pour identifier les tendances, spots et confirmer support/résistance
🟢 **FAIT VÉRIFIÉ** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Le RSI permet d'identifier des tendances, de repérer des divergences de patterns graphiques et de confirmer des niveaux de support ou résistance potentiels — trois usages distincts et complémentaires.
**TRADEX-AI C1** : Le prompt Claude pour analyse TRADEX doit distinguer explicitement ces 3 usages RSI : (1) identification tendance, (2) détection divergence, (3) confirmation S/R — chacun contribuant différemment au score /10.
*Catégorie : indicateurs_momentum*

### D7663 — RSI inefficace seul mais puissant dans un système multi-indicateurs
🟡 **SYNTHÈSE** (Source : common_mistakes_when_using_rsi_indicators_in_futures.md) : Le RSI bien utilisé en futures trading améliore la qualité des décisions — mais uniquement dans un système multi-indicateurs contextuel (tendance + volume + structure de marché) jamais en usage isolé.
**TRADEX-AI C1** : Le RSI est un contributeur valide au cercle C1 dans la grille /10 TRADEX — sa pondération doit refléter son rôle de confirmation et non de déclencheur principal du signal de trading.
*Catégorie : indicateurs_momentum*

