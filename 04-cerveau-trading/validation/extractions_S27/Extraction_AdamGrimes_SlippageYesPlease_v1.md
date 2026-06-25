# Extraction AdamGrimes — Slippage Yes Please
**Source :** `bundles/adamgrimes/slippage_yes_please.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6671 → D6680 · **Page :** https://www.adamhgrimes.com/slippage-yes-please/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le slippage au breakout est un signal de qualité — un bon breakout doit être difficile à entrer, c'est un indicateur de force.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6671 — Slippage au breakout : signal de qualité, non coût
🟢 **FAIT VÉRIFIÉ** (Source : slippage_yes_please.md) : Autour des points de breakout, le slippage est désirable. Un bon breakout doit être difficile à acheter — devoir payer des prix plus élevés pour entrer confirme que le marché est réellement en mouvement. Un fill facile ou une « bonne surprise » à l'entrée d'un breakout est un signal d'alerte négatif.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, si le signal est un breakout et que l'exécution NT8 ATI remplit à un prix meilleur que le déclencheur, le risk_manager.py doit logger un warning « EASY_FILL_WARNING » — cette configuration peut indiquer un faux breakout.
*Catégorie : volume_liquidite*

### D6672 — Définition du slippage et perception standard
🟢 **FAIT VÉRIFIÉ** (Source : slippage_yes_please.md) : Le slippage est la différence entre le prix d'exécution prévu et le prix d'exécution réel. Exemple : ordre à 20.00$, fill à 20.20$ = 20 centimes de slippage. La perception standard est que le slippage est un coût à éviter. Grimes conteste cette vision pour les breakouts.
**TRADEX-AI C1** : Dans le calcul du R/R de TRADEX, le slippage estimé doit être intégré comme coût dans le calcul de l'entrée. Mais si le signal est un breakout avec momentum confirmé, le slippage prévu ne doit pas à lui seul invalider le signal.
*Catégorie : gestion_risque_entree*

### D6673 — Happy surprises : signal d'alerte sur breakout
🟢 **FAIT VÉRIFIÉ** (Source : slippage_yes_please.md) : Les « bonnes surprises » à l'entrée d'un breakout (fill meilleur que prévu, pas de slippage) peuvent signifier que le breakout n'est pas réel. Un vrai breakout avec participation institutionnelle crée de la compétition pour les fills — c'est cette compétition qui génère du slippage positif.
**TRADEX-AI C2** : Dans l'analyse order flow ATAS, un breakout sur GC/CL sans accélération du volume et sans aggression acheteur visible dans le footprint doit être traité avec suspicion même si le prix franchit le niveau.
*Catégorie : volume_liquidite*

### D6674 — Coût du slippage en swing trading et gap overnight
🟡 **SYNTHÈSE** (Source : slippage_yes_please.md) : En swing trading, le slippage et le risque de gap overnight sont des coûts réels qui rendent difficile la connaissance précise de son risque. Ils doivent être intégrés dans la planification du trade mais ne doivent pas être traités comme des risques absolus à éliminer.
**TRADEX-AI C1** : Pour ZW et HG (marchés avec risque de gap overnight plus prononcé), le risk_manager.py doit ajouter un buffer de slippage estimé de 1.5× le spread moyen dans le calcul du stop réel et du R/R minimum.
*Catégorie : gestion_risque_entree*

### D6675 — Backtesting et slippage : surestimation des performances
🟡 **SYNTHÈSE** (Source : slippage_yes_please.md) : Les développeurs de systèmes savent que le slippage va éroder les performances backtestées. Le backtesting sans modélisation réaliste du slippage surestime systématiquement les résultats réels.
**TRADEX-AI C1** : Toute validation de règle de trading dans la KB TRADEX doit être interprétée avec la conscience que les performances historiques citées sont probablement surestimées si le slippage n'est pas modélisé. Les règles doivent donc avoir une marge de robustesse suffisante.
*Catégorie : structure_marche*
