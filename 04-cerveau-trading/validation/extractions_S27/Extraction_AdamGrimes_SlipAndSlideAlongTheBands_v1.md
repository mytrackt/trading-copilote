# Extraction AdamGrimes — Slip And Slide Along The Bands
**Source :** `bundles/adamgrimes/slip_and_slide_along_the_bands.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6651 → D6666 · **Page :** https://www.adamhgrimes.com/slip-and-slide-along-the-bands/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Approfondissement du slide pattern appliqué au pétrole brut (CL) — mécanique de formation, gestion des stops, comportement à la fin du pattern.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Chart crude oil mentionné dans le texte mais non inclus dans le bundle | — | D6652 |

## DÉCISIONS

### D6651 — Simplicité des patterns efficaces
🟢 **FAIT VÉRIFIÉ** (Source : slip_and_slide_along_the_bands.md) : Les patterns de trading efficaces sont simples. Plus une idée est complexe, plus elle est probablement le résultat d'un ajustement artificiel à des données aléatoires (overfitting). Les patterns de l'analyse technique traditionnelle semblent bons dans le passé mais manquent d'utilité au bord droit du graphique.
**TRADEX-AI C1** : Ce principe valide la philosophie de TRADEX : le filtre d'entrée (3/4 + 2/3) doit rester simple et déterministe. Toute complication supplémentaire (patterns complexes, ratios de Fibonacci multiples) doit être rejetée sans backtest rigoureux.
*Catégorie : structure_marche*

### D6652 — CL comme exemple canonique du slide pattern (2014 Q4)
🟢 **FAIT VÉRIFIÉ** (Source : slip_and_slide_along_the_bands.md) : Le pétrole brut (CL) en Q4 2014 est cité comme exemple référence d'un slide pattern baissier : prix pressant dans la bande basse Keltner sans retracements réels. Autres exemples historiques : Silver 2010-2011, Blé 2014, US Stocks 2010/2012/2013, Nasdaq post-2000.
**TRADEX-AI C1** : Pour CL et ZW (actifs tradables TRADEX), les périodes historiques de slide pattern sont connues. Les règles de filtre SLIDE_PATTERN s'appliquent prioritairement à ces deux actifs qui ont démontré cette tendance.
*Catégorie : indicateurs_tendance*

### D6653 — Mécanique du slide : volatilité réduite + pression directionnelle simultanées
🟢 **FAIT VÉRIFIÉ** (Source : slip_and_slide_along_the_bands.md) : Le slide pattern se forme quand le groupe dominant pousse dans la direction de la tendance en même temps que la volatilité se contracte. C'est la conjonction de ces deux facteurs (directionnalité + faible volatilité) qui crée le glissement progressif contre la bande.
**TRADEX-AI C2** : Signal de détection : ATR en contraction (ATR_n < 0.8 × ATR_20) ET delta order flow persistant dans la direction de la tendance sur ≥ 3 barres consécutives = conditions nécessaires pour confirmer un slide pattern naissant.
*Catégorie : volume_liquidite*

### D6654 — Gestion de position côté favorable : stop trailing serré toutes les 2-3 barres
🟢 **FAIT VÉRIFIÉ** (Source : slip_and_slide_along_the_bands.md) : Quand on est positionné du bon côté d'un slide pattern, la règle est : maintenir un stop correct ET le resserrer toutes les 2-3 barres au fur et à mesure que le marché fait de nouveaux extrêmes. Ne pas regarder le P&L. Ne pas sur-analyser. Laisser le marché décider de la sortie.
**TRADEX-AI C1** : Règle de gestion active si SLIDE_PATTERN_ACTIF = True et position ouverte : le risk_manager.py doit resserrer le stop toutes les 2 barres range NT8 vers le dernier pivot opposé formé, sans attendre de signal de sortie de l'analyse Claude.
*Catégorie : gestion_position_active*

### D6655 — Fin du slide pattern : spike violent et émotionnel
🟢 **FAIT VÉRIFIÉ** (Source : slip_and_slide_along_the_bands.md) : Quand le slide pattern se termine, il se termine souvent par un spike violent dans la direction opposée. Les stops doivent être absolument respectés. Se faire stopper dans le bruit est acceptable — le trader ne doit pas être émotionnel quand le marché l'est.
**TRADEX-AI C5** : Règle psychologique codée : après un stop sur slide pattern, un signal inverse ne doit pas être généré pendant les 3 barres suivantes (délai de « décompression émotionnelle du marché »). Ce délai est géré dans risk_manager.py.
*Catégorie : psychologie*

### D6656 — Directive universelle : ne pas faire de bêtises
🟡 **SYNTHÈSE** (Source : slip_and_slide_along_the_bands.md) : L'auteur résume la description du métier de trader à une directive simple : « ne pas faire de bêtises, ne pas faire d'erreurs ». Comprendre les patterns dangereux comme le slide permet d'éviter la majorité des erreurs graves.
**TRADEX-AI C5** : Les garde-fous de TRADEX (news gate 30 min, circuit breaker, staleness monitor, suspension auto après perte) traduisent exactement ce principe : le système est conçu pour empêcher les erreurs, pas pour maximiser les entrées.
*Catégorie : psychologie*
