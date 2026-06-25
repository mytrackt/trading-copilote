# Extraction AdamGrimes — When Good Setups Go Bad
**Source :** `bundles/adamgrimes/when_good_setups_go_bad.md` (HTTP 200) + 0 images certifiées
**Méthode images :** pas d'images dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7491 → D7505 · **Page :** https://www.adamhgrimes.com/when-good-setups-go-bad/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 352 — les flags haussiers parfaits (bull flags) peuvent échouer violemment ; la règle de réactivité et la nature probabiliste des setups sont DIRECTEMENT applicables à GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

---

## DÉCISIONS

### D7491 — Momentum adverse fort = signal d'échec de pullback
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : Quand un pullback haussier (bull flag) s'accompagne d'un mouvement fort en direction opposée (-3,3 sigma dans l'exemple EURCHF), c'est le signal classique d'échec du setup. Grimes décrit ce cas comme "l'une des façons classiques dont les pullbacks échouent : un momentum fort contre la direction anticipée du trade."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, si un bull flag se forme mais qu'une bougie de forte amplitude (≥ 2 ATR) casse le bas du drapeau, c'est un signal d'annulation immédiate — ne pas entrer long.
*Catégorie : configuration*

### D7492 — Réactivité informationnelle : lire le marché sans biais directionnel
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : "Nous devons être réactifs à l'information que le marché nous donne. Si l'on reste enfermé dans un biais ('EURCHF va monter'), on risque de rationaliser ou d'ignorer un mouvement contraire." La lecture objective du marché prime sur la conviction pré-trade.
**TRADEX-AI C1/C5** : Le moteur TRADEX doit réévaluer le signal à chaque cycle de 2 secondes sans mémoriser de biais directionnel. Un signal ACHETER émis au cycle N ne doit pas influencer l'analyse au cycle N+5 si le price action a changé.
*Catégorie : psychologie*

### D7493 — La qualité esthétique d'un setup ne prédit pas son issue
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : "Je suis arrivé à croire que la 'beauté' d'un pattern ou la qualité d'un setup n'a que peu de rapport avec les résultats du trade. Ce n'est pas une observation anodine — c'est le résultat de l'analyse de centaines de patterns." Un setup parfait reste un coin biaisé, pas une certitude.
**TRADEX-AI C1** : Le score /10 de TRADEX ne doit jamais dépasser un seuil de confiance de 85 % même pour un setup techniquement parfait (bull flag + alignement Belkhayate) — la nature probabiliste est irréductible.
*Catégorie : gestion_risque_entree*

### D7494 — Les résultats trading ne sont importants que sur un grand échantillon
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : "Mes résultats ne sont importants que sur un large échantillon de taille, et le résultat de n'importe quel trade est aléatoire." La performance se juge sur une série de trades, pas sur un trade individuel.
**TRADEX-AI C1** : Le mode Auto de TRADEX ne doit jamais être suspendu après un seul trade perdant isolé (sauf règle VIX/news gate activée). La suspension ne s'applique qu'après N pertes consécutives définies dans risk_manager.py.
*Catégorie : gestion_position_active*

### D7495 — Stop obligatoire et plan de sortie défini avant l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : "Si vous aviez une position, votre tâche est simple et claire : suivre votre plan de trading. Avoir votre stop en place (mental ou dans le marché) et sortir du trade quand le mouvement de prix prouve que vous avez tort."
**TRADEX-AI C1** : Pour tout signal ACHETER/VENDRE émis par TRADEX, le niveau de stop loss doit être calculé et affiché simultanément au signal — pas après l'entrée. Le stop est une composante non négociable du signal, pas une option.
*Catégorie : gestion_risque_entree*

### D7496 — Surextension parabolique : signal de vigilance sur un uptrend
🟡 **SYNTHÈSE** (Source : when_good_setups_go_bad.md) : Dans l'exemple EURCHF, la montée parabolique de mi-avril était un signal de surextension. Grimes note : "c'est une sur-extension acceptable et normale dans une tendance forte" mais souligne qu'elle constitue un négatif mineur à surveiller.
**TRADEX-AI C1** : Sur GC/CL notamment (actifs sujets aux accélérations parabouliques), un mouvement > 3 ATR en une seule session doit déclencher un flag de surextension dans le moteur — le setup bull flag suivant est statistiquement plus risqué.
*Catégorie : structure_marche*

### D7497 — La durée du pullback absorbe la surextension
🟡 **SYNTHÈSE** (Source : when_good_setups_go_bad.md) : "La durée du pullback était probablement suffisante pour compenser toute surextension." La longueur temporelle d'une consolidation/correction compte autant que son amplitude pour neutraliser une surextension.
**TRADEX-AI C1** : Dans l'évaluation d'un bull/bear flag sur GC/HG/CL/ZW, le nombre de barres du pullback doit être >= N (paramètre config) pour valider que la surextension est absorbée. Un flag trop court (< 5 barres range) est insuffisant.
*Catégorie : configuration*

### D7498 — Absence d'entrée = absence de perte sur setup échoué
🟢 **FAIT VÉRIFIÉ** (Source : when_good_setups_go_bad.md) : "Dans ce cas, la plupart des traders n'auraient pas eu d'entrée, donc pas de perte associée à ce pattern échoué." La discipline de n'entrer qu'à la confirmation évite les pertes sur les setups qui se dégradent avant le déclencheur.
**TRADEX-AI C1** : Le signal TRADEX doit exiger une confirmation de déclencheur (breakout du flag, bougie de clôture au-dessus du niveau) avant d'émettre un ordre. Pas de signal sur anticipation seule d'un setup qui "semble parfait."
*Catégorie : gestion_risque_entree*
