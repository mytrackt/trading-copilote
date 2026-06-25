# Extraction AdamGrimes — Support And Resistance Right Now
**Source :** `bundles/adamgrimes/support_and_resistance_right_now.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image présente dans ce bundle
**Décisions :** D6731 → D6745 · **Page :** https://www.adamhgrimes.com/support-and-resistance-right-now/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 314 (S/R en temps réel) — pertinent pour C1 (Prix/structure marché) et C2 (OrderFlow) : lecture active d'un niveau de support/résistance en développement, gestion de stop sur position existante.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle (graphique AUDUSD décrit textuellement) | — | — |

## DÉCISIONS

### D6731 — Le support/résistance ne peut être prédit à l'avance — seule la lecture en temps réel est fiable
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : Adam Grimes affirme explicitement qu'il est impossible de prédire à l'avance si un niveau de support/résistance va fonctionner. On peut seulement observer des signes qu'il fonctionne en temps réel ("right now").
**TRADEX-AI C1** : Le moteur TRADEX ne doit pas générer de signal basé sur des niveaux S/R projetés sans confirmation de price action autour du niveau. Un niveau S/R identifié est une zone de surveillance, pas un signal automatique.
*Catégorie : structure_marche*

### D6732 — Premier signe de support : le prix "arrête de descendre"
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : La première indication qu'un support fonctionne est que le prix arrête de descendre dans cette zone. C'est un signal brut, nécessitant confirmation, mais il doit être observé avant tout autre analyse.
**TRADEX-AI C1** : Dans le module de lecture des pivots NT8 (data_reader.py), un stop de progression directionnelle au niveau d'un pivot Belkhayate doit déclencher une alerte de surveillance S/R, précurseur d'une analyse approfondie par claude_brain.py.
*Catégorie : structure_marche*

### D6733 — Deuxième signe : rejection du prix à la borne basse de la zone
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : La deuxième confirmation d'un support actif est l'apparition de chandeliers de rejet (longue ombre basse, clôture au-dessus) à la borne basse de la zone. Ces chandeliers montrent qu'acheteurs défendent activement ce niveau.
**TRADEX-AI C1/C2** : La présence de bougies de rejet à un niveau pivot Belkhayate est une confirmation C1 (prix) ET C2 (order flow) simultanée. Poids renforcé dans le scoring /10 si NT8 montre des chandeliers de rejet + footprint ATAS confirme absorption.
*Catégorie : structure_marche*

### D6734 — Troisième signe : retour du prix dans la zone de rejet précédente
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : La troisième confirmation est le retour du prix dans la zone où les rejets ont eu lieu. Ce retour, combiné aux deux signes précédents, valide que la zone est activement défendue et représente un potentiel trade setup.
**TRADEX-AI C1** : La séquence "arrêt + rejet + retour dans zone" constitue un pattern de support validé en 3 étapes. Ce pattern doit être recherché sur les actifs tradables GC, HG, CL, ZW autour des pivots Belkhayate calculés par NT8.
*Catégorie : structure_marche*

### D6735 — Trade bidirectionnel autour d'une zone S/R active
🔵 **ÉCOLE** (Source : support_and_resistance_right_now.md) : Adam Grimes enseigne que tout niveau S/R actif offre deux trades possibles : (1) le breakout si les acheteurs perdent (short sur cassure sous le support), (2) le rebond si les acheteurs gagnent (long sur défense du support). Les deux setups sont valides et doivent être préparés.
**TRADEX-AI C1** : Le module de signal TRADEX doit toujours calculer et afficher les deux scénarios (cassure + rebond) autour d'un niveau S/R actif. La décision entre les deux appartient à Abdelkrim en Mode Manuel, ou est tranchée par le score /10 en Mode Auto.
*Catégorie : gestion_risque_entree*

### D6736 — Ne pas initier un nouveau short à l'intérieur d'une zone de support
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : Grimes indique explicitement : ne pas ouvrir un nouveau short à l'intérieur d'une zone de support. La raison est que le mouvement attendu sur la cassure nécessite que le prix sorte de la zone, pas qu'il soit dedans.
**TRADEX-AI C1** : Règle d'entrée stricte : interdire tout signal ACHETER/VENDRE généré lorsque le prix se trouve à l'intérieur d'une zone S/R active (entre borne haute et borne basse). Le signal doit attendre la sortie de zone (cassure ou rebond confirmé).
*Catégorie : gestion_risque_entree*

### D6737 — Position existante : règles différentes pour la gestion à l'intérieur d'une zone S/R
🔵 **ÉCOLE** (Source : support_and_resistance_right_now.md) : Pour une position déjà ouverte qui arrive dans une zone S/R, les règles sont différentes de l'initiation d'une nouvelle position : prendre des profits partiels + resserrer le stop sur le reste. Cette asymétrie initiation/gestion est fondamentale.
**TRADEX-AI C1** : Dans le module de gestion de position active (future implémentation), distinguer "nouveau signal" vs "gestion position existante" : en zone S/R, le moteur doit passer en mode "gestion" (alerte profit partiel + resserrement stop) plutôt qu'en mode "signal nouveau".
*Catégorie : gestion_position_active*

### D6738 — Breakout sur niveau S/R avec "vraie action" : meilleurs trades
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : Un breakout survenant après une lutte visible autour d'un niveau (pattern 3 étapes : arrêt + rejet + retour) génère certains des trades les plus nets et les plus propres. La "vraie action" autour du niveau valide la force du breakout.
**TRADEX-AI C1** : Un breakout sur un niveau S/R "testé en 3 étapes" obtient un bonus de qualité dans le scoring /10 TRADEX. Ce bonus peut être implémenté comme un critère "confirmation de structure" dans le cercle C1.
*Catégorie : gestion_risque_entree*

### D6739 — La psychologie des deux camps (acheteurs/vendeurs) doit être lue en permanence
🔵 **ÉCOLE** (Source : support_and_resistance_right_now.md) : L'auteur enseigne à lire qui est en train de "gagner" à chaque instant : les acheteurs défendent-ils bien les lows ? Si oui, leur force mérite le respect, même si la position actuelle est short. Cette lecture bidirectionnelle est une compétence clé.
**TRADEX-AI C1/C2** : Le prompt claude_brain.py doit inclure une instruction explicite : analyser les deux camps autour de chaque niveau clé identifié. Signal TRADEX non valide si un seul camp est évalué.
*Catégorie : psychologie*

### D6740 — Les patterns S/R se reproduisent sur tous les marchés et tous les timeframes
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : Adam Grimes affirme que les patterns de support/résistance (arrêt, rejet, retour) sont universels : ils se produisent sur des charts mensuels comme sur des charts tick-by-tick. La mécanique est la même.
**TRADEX-AI C1** : Les patterns S/R sont valides sur les range bars NT8 utilisées par TRADEX (actifs GC, HG, CL, ZW). L'universalité des patterns justifie l'application de cette logique quel que soit le timeframe configuré dans NT8.
*Catégorie : structure_marche*

### D6741 — Lire l'histoire du prix plutôt que des patterns spécifiques
🔵 **ÉCOLE** (Source : support_and_resistance_right_now.md) : La recommandation finale de Grimes : regarder les graphiques de prix en pensant à "l'histoire qui se déroule" (buyers vs sellers, qui perd, qui gagne) plutôt qu'en cherchant des patterns nommés ou des lignes d'indicateurs.
**TRADEX-AI C1** : Le prompt du cerveau Claude (claude_brain.py) doit demander une narration des forces en présence autour des niveaux clés, pas seulement l'identification de patterns. Exemple de directive : "Décris qui contrôle actuellement la zone [pivot X] sur [actif]."
*Catégorie : psychologie*

### D6742 — Mouvement de hausse "propre" après défense d'un support : signe de validité
🟢 **FAIT VÉRIFIÉ** (Source : support_and_resistance_right_now.md) : Dans l'exemple AUDUSD décrit, la cassure à la hausse après défense du support a produit un mouvement "clean" (propre, directionnel, sans retest immédiat). Ce type de mouvement confirme a posteriori la validité du support et la qualité du setup.
**TRADEX-AI C1** : Un mouvement post-breakout "propre" (sans retest dans les N barres suivantes) peut être utilisé comme signal de renforcement de position dans la gestion active. À implémenter dans le futur module de position management.
*Catégorie : gestion_position_active*

### D6743 — La zone S/R active fournit un niveau de stop clair pour le trade
🟡 **SYNTHÈSE** (Source : support_and_resistance_right_now.md) : La définition d'une zone S/R active (avec borne haute et borne basse identifiées) fournit naturellement un niveau de stop logique : pour un short sur cassure, le stop est au-dessus de la borne haute de la zone.
**TRADEX-AI C1** : Le calcul du stop loss dans TRADEX doit utiliser les bornes de la zone S/R active identifiée par NT8/Belkhayate. Un stop placé au-delà de la borne opposée de la zone est cohérent avec la mécanique S/R décrite.
*Catégorie : gestion_risque_entree*

### D6744 — Support/résistance : sujet controversé mais crucial à maîtriser
🔵 **ÉCOLE** (Source : support_and_resistance_right_now.md) : Grimes reconnaît que le S/R est controversé (biais cognitif, mouvement aléatoire du prix) mais conclut que c'est malgré tout un des sujets les plus importants pour un trader. La maîtrise du S/R en temps réel est une compétence différenciatrice.
**TRADEX-AI C1** : La base de connaissances KB (04-cerveau-trading) doit inclure cette nuance : le S/R est à utiliser avec rigueur (confirmation en 3 étapes) et non mécaniquement. Le cerveau Claude doit exprimer un niveau de confiance réduit sur les niveaux S/R non confirmés.
*Catégorie : structure_marche*

### D6745 — Le biais cognitif et le mouvement aléatoire peuvent simuler des niveaux S/R inexistants
🔴 **NON SOURCÉ** (Source : support_and_resistance_right_now.md) : L'auteur mentionne les biais cognitifs et le mouvement aléatoire comme facteurs de faux S/R, mais ne fournit pas de données quantitatives sur la fréquence des faux niveaux vs vrais niveaux.
**TRADEX-AI C1** : À retenir comme avertissement dans le KB : tout niveau S/R non confirmé par le pattern 3 étapes (D6732-D6734) est potentiellement un artefact cognitif. Règle d'hygiène analytique pour le cerveau Claude.
*Catégorie : psychologie*
