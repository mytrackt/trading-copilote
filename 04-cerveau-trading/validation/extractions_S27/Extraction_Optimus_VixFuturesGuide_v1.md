# Extraction Optimus — VIX Futures Guide
**Source :** `bundles/optimusfutures/vix_futures_guide.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D8791 → D8810 · **Page :** https://optimusfutures.com/blog/vix-futures-guide/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : VIX est un actif de CONFIRMATION (C5 Sentiment) dans TRADEX — ce guide fournit les seuils et mécanismes essentiels pour interpréter VX dans le moteur de signal.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | vix futures | VIX Index vs. VIX Futures Pricing | D8795 |
| image_02.png | A systematic hedge allocation helps stabilize total portfolio value | Hedging Strategies Using VIX | D8803 |

## DÉCISIONS

### D8791 — Spécifications contrat VX (VIX Futures) sur CFE
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Contrat VX sur Cboe Futures Exchange (CFE). Multiplicateur : 1 000 $ × prix VIX. Tick minimum : 0,05 point = 50 $. Jusqu'à 9 mois proches + mois supplémentaires. Settlement : cash via VIX SOQ (Special Opening Quotation). Heures de trading : quasi 24h/5j. Sous-jacent : volatilité implicite 30j du S&P 500.
**TRADEX-AI C5** : Paramètres techniques du contrat VX pour TRADEX. Le VIX n'est pas tradé directement mais son niveau est lu via l'API. Le multiplicateur 1 000 $/point explique la sensibilité extrême des positions VX — confirmation que VIX reste un actif de CONFIRMATION uniquement dans TRADEX.
*Catégorie : macro_evenements*

### D8792 — VIX Futures : définition — futures sur la volatilité implicite 30j du S&P 500
🔵 **ÉCOLE** (Source : vix_futures_guide.md) : Le VIX Index mesure la volatilité implicite actuelle sur 30 jours dérivée des options S&P 500. Les VIX Futures sont des contrats cash-settled sur la valeur FUTURE attendue du VIX. Contrairement aux futures sur actifs physiques (CL, GC), les VIX futures trackent une attente, pas un actif livrable.
**TRADEX-AI C5** : Distinction fondamentale : le niveau VIX spot (disponible en temps réel) est différent du prix des VIX futures (prime de terme). TRADEX utilise le VIX spot comme indicateur de sentiment (C5) — le niveau spot est suffisant pour le moteur de signal.
*Catégorie : macro_evenements*

### D8793 — VIX et S&P 500 : relation inverse fondamentale
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Le VIX Index dérive des options S&P 500. Quand le S&P 500 chute, la volatilité implicite monte — le VIX augmente. Cette relation inverse est structurelle et permanente, non conjoncturelle. Elle est exploitée pour le hedging de portefeuille actions.
**TRADEX-AI C5** : Règle d'interprétation TRADEX : hausse VIX = baisse ES probable = contexte macro risk-off. En contexte risk-off (VIX en hausse), les actifs refuge (GC/Or) ont un biais haussier potentiel ; les actifs cycliques (CL/Pétrole, HG/Cuivre) ont un biais baissier potentiel. Cette corrélation alimente C5 et C7.
*Catégorie : correlations*

### D8794 — Utilités du VIX Futures : hedge, diversification, spéculation sur sentiment
🔵 **ÉCOLE** (Source : vix_futures_guide.md) : Les traders utilisent les VIX futures pour : (1) hedger des portefeuilles actions contre les baisses, (2) diversifier avec la volatilité comme classe d'actifs distincte, (3) spéculer sur les changements de sentiment. Particulièrement utiles lors des chocs (2008, 2020).
**TRADEX-AI C5** : Rôle de VX dans TRADEX : indicateur de sentiment (C5) uniquement. Aucun ordre sur VX. Lecture du niveau : seuil bas (< 15) = calme → signaux TRADEX normaux ; seuil moyen (15-20) = vigilance ; seuil haut (> 20) = stress marché → filtres renforcés.
*Catégorie : macro_evenements*

### D8795 — Structure de terme VIX : contango (normal) vs backwardation (stress)
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : La structure de terme VIX décrit la différence entre le VIX spot et les prix des futures VIX sur différentes échéances. En temps normal : contango (futures > spot = prime de risque). En période de stress : backwardation (futures < spot = peur immédiate supérieure aux attentes futures). Image certifiée : vix futures / VIX Index vs VIX Futures Pricing.
**TRADEX-AI C5** : Seuil de lecture TRADEX : contango normal VIX = contexte favorable aux signaux directionnels. Backwardation VIX = choc en cours → activer le filtre de suspension auto (risk_manager.py) et réduire la confiance maximale des signaux Claude.
*Catégorie : macro_evenements*

### D8796 — VIX Premium (Volatility Risk Premium) : biais haussier structurel des futures VIX
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Le VIX Premium est la différence entre les prix des futures VIX et le niveau VIX spot. Il représente le coût de la protection contre la volatilité. Ce premium crée un biais structurel de contango : les positions longues VIX perdent de la valeur en marché calme (decay). Les positions courtes VIX profitent du contango mais risquent des pertes massives si la volatilité spike.
**TRADEX-AI C5** : Implication pour C5 : le VIX ne peut pas être tradé "en tendance" sur le long terme par un acheteur. La lecture TRADEX du VIX doit être tactique (niveau ponctuel) et non positionnelle. Jamais de trade sur VX dans TRADEX.
*Catégorie : indicateurs_momentum*

### D8797 — VIX ETPs (VXX, UVXY) vs VIX Futures directs : decay accéléré des ETPs
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Les ETPs VIX (VXX, UVXY) trackent des paniers de futures VIX roulés quotidiennement. Ce rolling daily en contango produit un decay structurel : la valeur de l'ETP diminue même si la volatilité reste stable. Les futures VIX directs offrent une meilleure efficacité en coût pour les traders actifs.
**TRADEX-AI C5** : TRADEX utilise le VIX Index (spot) comme donnée de confirmation, pas les ETPs. Si une donnée VX futures directe est disponible via NT8, elle est préférable. Les ETPs ne doivent jamais être utilisés comme source de données VIX dans TRADEX.
*Catégorie : indicateurs_momentum*

### D8798 — Seuils VIX pour calibrer l'amplitude des trades
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : L'article documente des seuils opérationnels : VIX > 20 → attendre des plages de prix plus larges et des oscillations de position plus importantes. VIX < 15 → marchés en plage étroite, cibles plus petites. Spikes VIX → opportunités tactiques fréquentes sur les futures d'indices.
**TRADEX-AI C5** : Règles TRADEX intégrables directement dans risk_manager.py : (1) VIX < 15 → réduire les cibles de profit (range étroit). (2) VIX 15-20 → paramètres normaux. (3) VIX > 20 → élargir stops/cibles, réduire taille de position. (4) VIX > seuil critique (configurable settings.py) → suspendre mode Auto.
*Catégorie : gestion_risque_entree*

### D8799 — Hedging VIX : allocation 2-5% du portefeuille, rééquilibrage trimestriel
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Les traders professionnels maintiennent une allocation permanente de 2-5% en positions longues VIX comme assurance de portefeuille. Rééquilibrage trimestriel ou quand la volatilité atteint certains seuils. Combiné avec des positions S&P 500 pour une exposition équilibrée. Image certifiée : hedge allocation stabilizes portfolio value.
**TRADEX-AI C5** : Pertinent pour C3 (Institutionnels) : une hausse soudaine du volume sur VX (achat d'assurance institutionnel) précède souvent une correction de marché. À surveiller comme signal d'alerte précoce dans C5.
*Catégorie : gestion_position_active*

### D8800 — Règles de gestion du roll VIX : expiration le mercredi, 30j avant options S&P
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : Les contrats VX expirent le mercredi 30 jours avant l'expiration des options S&P 500 du mois suivant. Settlement via VIX SOQ (Special Opening Quotation) basé sur les prix d'ouverture des options S&P 500. Risques : spreads bid-ask élargis en semaine d'expiration ; déviations de prix inattendues au SOQ.
**TRADEX-AI C5** : Calendrier des expirations VX = événements macro à intégrer dans le News Gate de TRADEX (C4). Semaine d'expiration VX → prudence renforcée sur les signaux, particulièrement pour ES (actif de confirmation C2 lié au S&P 500).
*Catégorie : timing*

### D8801 — Contango decay : principal risque des positions longues VIX
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : En marché calme (contango), chaque rollover de position longue VIX coûte la différence entre le prix du mois expirant (moins élevé) et le mois suivant (plus élevé). Ce coût de roulement (roll decay) érode progressivement la valeur de la position longue même si le VIX spot ne bouge pas.
**TRADEX-AI C5** : Confirmation de la règle TRADEX : VX = actif de CONFIRMATION uniquement, jamais de trade directionnel long VX dans TRADEX. Le decay structurel disqualifie les positions VX longues comme stratégie principale.
*Catégorie : gestion_position_active*

### D8802 — Timing des spikes VIX : imprévisible, favoriser les approches systématiques
🟢 **FAIT VÉRIFIÉ** (Source : vix_futures_guide.md) : La volatilité est mean-reverting (tendance à revenir vers sa moyenne historique). Prédire le timing exact d'un spike est extrêmement difficile. Les traders professionnels privilégient les approches systématiques (hedges permanents, overlays de scaling) plutôt que les paris directionnels sur le timing des pics.
**TRADEX-AI C5** : Règle de design TRADEX : le moteur ne tente pas de prédire le prochain spike VIX. Il utilise le niveau VIX courant comme filtre de contexte. Un VIX en forte hausse intraday (> +20% sur la session) déclenche un flag d'alerte dans staleness_monitor.py → bloquer les nouveaux signaux.
*Catégorie : gestion_risque_entree*
