# Extraction SierraChart — Momentum
**Source :** `bundles/sierrachart/sierra_35_momentum.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9251 → D9270 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=35
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Momentum = mesure brute de la vitesse du prix sur N périodes — confirmateur de l'Energie Belkhayate (stub en attente), deux variantes (Difference/Quotient) avec usages distincts.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9251 — Définition Momentum Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : L'indicateur Momentum calcule et affiche le momentum des données spécifiées par l'input Input Data. La formule dépend du paramètre Momentum Type (Difference ou Quotient). Le calcul commence à l'index t ≥ n (où n est le Length).
**TRADEX-AI C1** : Le Momentum est l'indicateur de vitesse du prix le plus simple — il mesure directement combien le prix a bougé sur N périodes. Potentiellement lié à l'Energie Belkhayate (stub non encore codé, D_ref CLAUDE.md) — à valider quand la définition exacte de l'Energie sera tranchée.
*Catégorie : indicateurs_momentum*

### D9252 — Momentum Type : Difference
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : Quand Momentum Type est réglé sur Difference, le Momentum est calculé comme : M_t(X, n) = X_t - X_(t-n). C'est-à-dire la différence entre la valeur actuelle et la valeur n périodes auparavant.
**TRADEX-AI C1** : La variante Difference mesure l'amplitude absolue du mouvement sur N bars — directement comparable à d'autres indicateurs de momentum absolus. Sur GC (or), un Momentum Difference positif et croissant confirme une tendance haussière en cours.
*Catégorie : indicateurs_momentum*

### D9253 — Momentum Type : Quotient
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : Quand Momentum Type est réglé sur Quotient, le Momentum est calculé comme : M_t(X, n) = X_t / X_(t-n). C'est-à-dire le ratio entre la valeur actuelle et la valeur n périodes auparavant. Une valeur > 1 indique une hausse, < 1 une baisse.
**TRADEX-AI C1** : La variante Quotient normalise le momentum en ratio — utile pour comparer le momentum entre actifs de niveaux de prix différents (ex: GC à ~2000$ vs ZW à ~600 cents). Pour la comparaison inter-actifs TRADEX-AI (C7 corrélations), préférer Quotient.
*Catégorie : indicateurs_momentum*

### D9254 — Input : Length (période)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : L'input Length (noté n) détermine la période de comparaison. Le Momentum compare le prix actuel au prix d'il y a n bars. Les calculs commencent à t ≥ n — les n premiers bars ne produisent pas de valeur.
**TRADEX-AI C1** : Choix de la période n : une période courte (n=10-14) mesure le momentum à court terme (élan intraday) ; une période longue (n=50-100) mesure le momentum de moyen terme (tendance multi-sessions). Pour TRADEX-AI sur range bars NT8, tester n=20 comme valeur de base.
*Catégorie : indicateurs_momentum*

### D9255 — Input : Input Data (source de prix)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : L'input Input Data détermine la source de prix utilisée pour le calcul du Momentum. Peut être Open, High, Low, Last/Close, ou d'autres types disponibles dans Sierra Chart.
**TRADEX-AI C1** : Utiliser Last/Close par défaut — cohérent avec la convention Belkhayate. L'utilisation du High ou Low peut détecter le momentum des extrêmes de bar (utile pour identifier des accélérations de prix intra-bar sur les range bars NT8).
*Catégorie : indicateurs_momentum*

### D9256 — Spreadsheet Sierra Chart disponible (Momentum.35.scss)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_35_momentum.md) : Sierra Chart fournit un fichier spreadsheet de référence nommé Momentum.35.scss contenant les formules complètes de l'indicateur Momentum. Sauvegardé dans le Data Files Folder, ouvert via File >> Open Spreadsheet.
**TRADEX-AI C1** : Le fichier Momentum.35.scss est la référence de calcul exacte Sierra — utile pour valider l'implémentation Python du momentum dans le moteur TRADEX-AI (cohérence avec NT8).
*Catégorie : indicateurs_momentum*

### D9257 — Momentum Difference : interprétation signal zéro
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : En mode Difference, le croisement de la ligne de zéro est le signal de base : croisement vers le haut = prix aujourd'hui supérieur à il y a n bars (momentum positif) ; croisement vers le bas = momentum négatif. L'oscillation autour de zéro indique une consolidation.
**TRADEX-AI C1** : Le croisement zéro du Momentum Difference sur les actifs TRADING (GC/HG/CL/ZW) est un signal de confirmation d'un nouveau mouvement directionnel — à utiliser comme filtre dans la grille TRADEX-AI pour confirmer que l'élan est présent avant validation du signal Belkhayate.
*Catégorie : configuration*

### D9258 — Momentum Quotient : interprétation signal 1.0
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : En mode Quotient, la ligne de référence est 1.0 (au lieu de 0). Valeur > 1.0 = momentum positif (prix en hausse sur n périodes) ; < 1.0 = momentum négatif. L'amplitude d'écart par rapport à 1.0 indique l'intensité du momentum.
**TRADEX-AI C1** : Pour les comparaisons inter-actifs (C7 corrélations), le Momentum Quotient permet de comparer l'intensité relative du momentum entre GC et HG (corrélation positive), ou entre CL et ZW — un écart significatif de momentum entre actifs corrélés peut signaler une divergence de corrélation.
*Catégorie : correlations*

### D9259 — Divergence Momentum/Prix comme signal de retournement
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : La divergence entre le prix (nouveau plus haut/bas) et le Momentum (qui ne confirme pas) est un signal classique d'affaiblissement de la tendance et de retournement potentiel. Plus le momentum décélère avant le retournement, plus le signal est anticipé.
**TRADEX-AI C1** : Divergence Momentum/Prix sur GC ou CL = signal d'alerte précoce pour le cerveau Claude dans la grille /10. Une divergence baissière (nouveau plus haut prix mais momentum en baisse) peut déclencher une révision du signal ACHETER vers ATTENDRE même si les autres critères Belkhayate sont alignés.
*Catégorie : configuration*

### D9260 — Lien entre Momentum et Energie Belkhayate (stub)
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : L'Energie Belkhayate (stub non codé dans TRADEX-AI) mesure la force/faiblesse du marché — concept proche du Momentum Sierra ID=35 mais avec une logique propriétaire. Le Momentum Difference ou Quotient peut servir de proxy temporaire jusqu'à la définition exacte de l'Energie Belkhayate.
**TRADEX-AI C1** : DÉCISION ARCHITECTURE : En attendant la résolution du conflit MFI vs proxy ATR pour l'Energie Belkhayate (voir CLAUDE.md état actuel), le Momentum Sierra ID=35 (Length=14, Type=Difference) peut être utilisé comme placeholder C1. À remplacer dès validation définitive de la formule Energie.
*Catégorie : indicateurs_momentum*

### D9261 — Momentum comme confirmateur de rupture de niveau
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : Un breakout de niveau de support/résistance accompagné d'un momentum fort (Difference élevé, s'éloignant rapidement de zéro) valide la rupture. Un breakout avec momentum faible ou décélérant suggère un faux breakout (bull/bear trap).
**TRADEX-AI C1** : Pour TRADEX-AI, lors d'une rupture de pivot Belkhayate sur GC/CL : vérifier que le Momentum Difference s'éloigne de zéro dans la même direction. Un pivot rompu + momentum faible = risque de bull trap élevé → réduire score signal dans la grille /10.
*Catégorie : structure_marche*

### D9262 — Période optimale selon timeframe
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : La période optimale du Momentum dépend du timeframe utilisé. Sur des graphiques intraday (range bars, tick charts), des périodes courtes (n=10 à 20) captent le momentum de session. Sur des graphiques daily, des périodes plus longues (n=14 à 21) sont standard.
**TRADEX-AI C1** : Pour TRADEX-AI sur range bars NT8 (actifs TRADING) : n=14 (standard RSI, utilisé pour cohérence) ou n=20. Sur les actifs CONFIRMATION (ES, DX) en daily : n=14. Ces valeurs sont des points de départ à valider en Phase C backtest.
*Catégorie : indicateurs_momentum*

### D9263 — Momentum Difference vs ROC (Rate of Change)
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : Le Momentum Quotient de Sierra Chart est mathématiquement équivalent au ROC (Rate of Change) + 1. Le ROC classique = (X_t - X_(t-n)) / X_(t-n) = (X_t / X_(t-n)) - 1. La variante Difference de Sierra est identique au Momentum classique.
**TRADEX-AI C1** : Clarification nomenclature pour TRADEX-AI : ce que Sierra appelle Momentum Quotient correspond au ROC(1) + 1 dans d'autres plateformes. Lors de l'implémentation Python dans 05-saas/engine/, utiliser la formule Sierra exacte pour cohérence avec NT8.
*Catégorie : indicateurs_momentum*

### D9264 — Application Momentum sur actifs CONFIRMATION (DX, ES, VX)
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : Le Momentum peut être appliqué sur les actifs de confirmation TRADEX-AI (DX/Dollar Index, ES/SP500, VX/VIX) pour évaluer leur élan directionnel et ainsi confirmer ou infirmer le contexte macro des signaux de trading.
**TRADEX-AI C4/C5** : Un momentum DX positif et fort (dollar qui monte) est corrélé négativement avec GC (or qui baisse) — signal de contexte macro C4. Un momentum VX positif (VIX qui monte) signale un risque accru → activer garde-fous G1-G10 dans TRADEX-AI. Surveillance à inclure dans le moteur Python.
*Catégorie : macro_evenements*

### D9265 — Momentum sur VIX : signal de stress marché
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : Le Momentum appliqué au VIX mesure la vitesse de montée/descente de la peur sur les marchés. Un Momentum VIX positif et accélérant (VIX monte vite) indique un stress de marché croissant — conditions défavorables aux positions directionnelles sur futures.
**TRADEX-AI C5** : Pour TRADEX-AI, un Momentum VIX Difference > seuil_critique = signal de suspension mode Auto (en cohérence avec la sécurité Suspension Auto du CLAUDE.md). Seuil à définir en Phase C — valeur initiale suggérée : Momentum VIX(14) > 5 sur une session.
*Catégorie : gestion_risque_entree*

### D9266 — Configuration Momentum recommandée TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : Configuration opérationnelle pour TRADEX-AI : Momentum Type = Difference (lecture directe en points de prix), Length = 14 (standard marché), Input Data = Last/Close. Appliquer sur : (1) actifs TRADING GC/HG/CL/ZW sur range bars NT8 — signal C1 ; (2) actifs CONFIRMATION DX/ES/VX — signal C4/C5 ; (3) actif REFERENCE MBT — signal C7 corrélations.
**TRADEX-AI C1** : Ces paramètres constituent la configuration Momentum de base pour TRADEX-AI. Le Momentum Difference(14) sur Last/Close est le proxy temporaire de l'Energie Belkhayate jusqu'à validation définitive de sa formule. À implémenter dans 05-saas/engine/ comme MODULE_MOMENTUM.
*Catégorie : indicateurs_momentum*

### D9267 — Momentum nul / oscillation zéro = consolidation
🔵 **ÉCOLE** (Source : sierra_35_momentum.md) : Un Momentum Difference qui oscille autour de zéro sans directionnel clair indique une zone de consolidation ou de range — le marché ne génère pas de momentum directionnel. En mode Quotient, une oscillation autour de 1.0 produit le même signal.
**TRADEX-AI C1** : Pour TRADEX-AI, un Momentum oscillant autour de zéro sur GC/CL = condition de marché en range → signal ATTENDRE automatique dans la grille, même si d'autres critères Belkhayate semblent alignés. Absence de momentum = absence d'élan = signal invalide.
*Catégorie : configuration*

### D9268 — Momentum comme filtre anti-faux signal
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : L'utilisation du Momentum comme filtre de validation évite les faux signaux en consolidation. Règle : ne valider un signal directionnel (ACHETER/VENDRE) que si le Momentum est dans la même direction ET s'éloigne de zéro (accélération). Un Momentum qui ralentit ou diverge annule le signal.
**TRADEX-AI C1** : Règle de filtrage TRADEX-AI : signal Belkhayate ACHETER valide SEULEMENT SI Momentum(14) > 0 ET croissant sur 2 derniers bars. Signal VENDRE valide SEULEMENT SI Momentum(14) < 0 ET décroissant. Cette règle réduit les faux signaux en range — à intégrer comme check dans claude_brain.py.
*Catégorie : gestion_risque_entree*

### D9269 — Momentum sur GC : caractéristiques spécifiques
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : L'or (GC) présente des caractéristiques de momentum particulières : mouvements lents et prolongés en tendance, faux breakouts fréquents en range, sensibilité au Dollar Index (DX). Un Momentum GC positif fort + Momentum DX négatif = contexte haussier or renforcé (double confirmation).
**TRADEX-AI C1/C4** : Pour les signaux GC dans TRADEX-AI : croiser systématiquement le Momentum GC avec le Momentum DX (relation inverse). Si Momentum GC > 0 ET Momentum DX < 0 = signal ACHETER GC avec contexte favorable. Si les deux sont positifs = signal contradictoire → ATTENDRE.
*Catégorie : correlations*

### D9270 — Momentum Rate of Acceleration (dérivée secondaire)
🟡 **SYNTHÈSE** (Source : sierra_35_momentum.md) : L'accélération du Momentum (variation du Momentum d'un bar à l'autre = dérivée seconde du prix) est un indicateur avancé des retournements. Quand le Momentum commence à décélérer (sa variation diminue) avant un plus haut/bas de prix, c'est le premier signe d'un retournement imminent.
**TRADEX-AI C1** : Pour TRADEX-AI, calculer la variation du Momentum sur 3 bars (Momentum[t] - Momentum[t-3]) dans le moteur Python — une décélération forte (variation fortement négative sur Momentum positif) avant un plus haut de prix GC/CL est un signal de sortie/réduction de position anticipé. À documenter comme règle avancée Phase D.
*Catégorie : gestion_position_active*
