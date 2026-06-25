# Extraction AdamGrimes — Correlated Risk? Or Opportunity?
**Source :** `bundles/adamgrimes/correlated_risk_or_opportunity.md` (HTTP 200) + 1 image certifiée
**Méthode images :** ancrage figcaption locale · 1/1 certifiées · 0 à vérifier
**Décisions :** D5631 → D5650 · **Page :** https://www.adamhgrimes.com/correlated-risk-or-opportunity/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Gestion du risque corrélé entre actifs GC/HG/CL/ZW — les corrélations sont variables, dangereuses en stress de marché mais sources de surperformance si gérées consciemment (Cercle C7).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.jpg | correlations | AdamHGrimes | D5631 |

## DÉCISIONS

### D5631 — Variabilité des corrélations : le bêta d'une action fluctue entre +2.0 et -1.0 (image : correlations)
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md, image_01.jpg) : Les corrélations entre actifs financiers sont extrêmement variables dans le temps. Même des règles de base bien établies (corrélation Dollar/Or, corrélation inverse VIX/SPX) changent de régime. Un actif peut avoir un bêta oscillant entre +2.0 et -1.0 sur quelques années.
**TRADEX-AI C7** : Les corrélations calculées dans `correlations.py` (matrice live 30j) doivent inclure un indicateur de stabilité — une corrélation instable (forte variance sur fenêtre glissante) est moins fiable pour la décision de signal.
*Catégorie : correlations*

### D5632 — Corrélation ne montre pas ce que les traders débutants imaginent
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : Deux séries qui "vont dans la même direction" visuellement peuvent ne pas être corrélées. Il est possible de construire deux séries de prix parfaitement inversement corrélées (-1.0) qui montent toutes les deux sur le long terme. La corrélation mesure les mouvements relatifs simultanés, pas les tendances.
**TRADEX-AI C7** : Ne pas confondre "tendance commune" (deux actifs en hausse sur 6 mois) avec corrélation instantanée. Le `correlations.py` doit calculer la corrélation sur les rendements quotidiens (delta de prix), pas sur les niveaux de prix absolus.
*Catégorie : correlations*

### D5633 — Corrélation ≠ causalité (rappel universel)
🔵 **ÉCOLE** (Source : correlated_risk_or_opportunity.md) : La corrélation ne implique pas la causalité. Ce principe fondamental de statistiques est régulièrement oublié dans le feu de l'action des marchés. Les relations entre marchés peuvent être non-linéaires et plus complexes que ce qu'une corrélation linéaire peut capturer.
**TRADEX-AI C7** : Les corrélations du Cercle C7 sont des indicateurs de confirmation, pas des causalités. Une corrélation GC/DX ne signifie pas que le Dollar cause le mouvement de l'Or — utiliser avec discernement dans le prompt KB.
*Catégorie : correlations*

### D5634 — Les corrélations tendent vers 1.0 en période de stress de marché
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : Fait bien établi par des décennies d'histoire de marché : en période de stress, les corrélations entre actifs non-corrélés convergent vers 1.0. Cela se produit plusieurs fois par décennie, toujours précédé de mini-krach actions. En rétrospective, la connexion semble évidente mais n'était pas prévisible.
**TRADEX-AI C4/C5** : Quand VX (VIX) dépasse le seuil critique ET ES (S&P 500) est en forte baisse simultanément, activer le mode "stress corrélation" : les signaux sur GC/HG/CL/ZW deviennent fortement corrélés — réduire l'exposition totale, pas sur un seul actif.
*Catégorie : macro_evenements*

### D5635 — Le risque corrélé peut générer des rendements exceptionnels
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : Le risque corrélé est à double tranchant. Les traders qui comprennent, acceptent et gèrent le risque corrélé peuvent générer des performances exceptionnelles. Les périodes de forte performance concentrées (feast) coïncident souvent avec des risques corrélés élevés.
**TRADEX-AI C7** : Quand plusieurs actifs TRADEX signalent simultanément dans le même sens (ex : GC + HG haussiers, DX baissier, ES fort), c'est une configuration de "correlated opportunity" — non une raison de bloquer tous les trades mais de les gérer avec une conscience du risque total.
*Catégorie : gestion_position_active*

### D5636 — Positions indépendantes supposées peuvent se corréler subitement
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : Un book de trading est construit avec l'hypothèse que chaque position est un pari indépendant. Le risque corrélé est le risque que toutes ces positions bougent dans la même direction simultanément. Ce risque est sous-estimé par la plupart des traders.
**TRADEX-AI C7** : Le `risk_manager.py` doit calculer l'exposition corrélée totale : si GC + HG + CL sont simultanément en position longue avec corrélation > 0.7, l'exposition effective est bien supérieure à 3 positions indépendantes — appliquer un facteur de réduction.
*Catégorie : gestion_risque_entree*

### D5637 — Psychologie comme driver des corrélations de crise
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : En période de stress, c'est la psychologie collective (panique, ruée vers les sorties) qui force les corrélations vers 1.0, pas une connexion fondamentale. Les participants paniquent et vendent tout simultanément, quelle que soit la logique économique sous-jacente.
**TRADEX-AI C5** : Quand le VIX franchit un seuil critique, la panique potentielle invalide les corrélations habituelles. Le mode Auto doit être suspendu automatiquement — les corrélations KB ne sont plus fiables en panic mode.
*Catégorie : psychologie*

### D5638 — Les retours sont concentrés dans des fenêtres temporelles spécifiques
🟢 **FAIT VÉRIFIÉ** (Source : correlated_risk_or_opportunity.md) : Tant pour les traders discrétionnaires que pour les systèmes mécaniques, les rendements sont concentrés dans certaines périodes (feast), alternant avec des périodes de performance plate ou négative (famine). Ce pattern est universel dans le trading.
**TRADEX-AI C1** : En Mode Manuel, afficher à Abdelkrim le contexte de "régime de marché" — période favorable (tendance établie, corrélations cohérentes) vs période défavorable (chop, corrélations instables) — pour calibrer son niveau d'activité.
*Catégorie : psychologie*

### D5639 — Corrélation : mesure de relations linéaires uniquement
🔵 **ÉCOLE** (Source : correlated_risk_or_opportunity.md) : La corrélation est une mesure de relation linéaire. Les relations entre marchés peuvent être non-linéaires (ex : l'Or se comporte différemment selon que le Dollar baisse lentement ou s'effondre brutalement). Une corrélation linéaire peut sous-estimer la vraie richesse de la relation.
**TRADEX-AI C7** : La matrice de corrélation live 30j de `correlations.py` est un premier niveau d'analyse. Les relations non-linéaires (ex : régimes de volatilité) sont capturées par les règles KB de Claude — les deux couches sont complémentaires.
*Catégorie : correlations*

### D5640 — Accepter le risque corrélé consciemment vs le subir par ignorance
🟡 **SYNTHÈSE** (Source : correlated_risk_or_opportunity.md) : La distinction fondamentale est entre subir le risque corrélé par ignorance (trader qui ne voit pas que ses 3 positions sont corrélées) et accepter consciemment le risque corrélé parce qu'on voit une opportunité de marché concentrée. Le second cas est une stratégie; le premier est une erreur de gestion.
**TRADEX-AI C7** : TRADEX-AI doit afficher explicitement le niveau de corrélation du portefeuille courant en Mode Manuel — Abdelkrim peut alors décider en connaissance de cause s'il accepte le risque corrélé ou préfère diversifier.
*Catégorie : gestion_position_active*
