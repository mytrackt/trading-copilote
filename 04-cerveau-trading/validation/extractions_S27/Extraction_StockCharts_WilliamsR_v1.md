# Extraction StockCharts — Williams %R
**Source :** `bundles/stockcharts/williams_r.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage (figcaption label) · 7/7 certifiées · 0 à vérifier
**Décisions :** D4891 → D4910 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/williams-r
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Williams %R est un oscillateur momentum directement applicable à GC/HG/CL/ZW — candidat pour Cercle C1 (indicateurs momentum) ou confirmation C5 (sentiment de prix court terme).

---

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/smMCyDYOnmv3AIXCxW1T | Williams %R - Spreadsheet 1 | Calcul | D4892 |
| /files/eKu3jgR4sZYbOwAtvhXS | Williams %R - Chart 1 | Calcul | D4892 |
| /files/Wd3YgGKe1hovA8qwVPmE | Williams %R - Chart 2 | Overbought/Oversold | D4895 |
| /files/OdHVHmc0woeJ9GvcLzvH | Williams %R - Chart 3 | Momentum Failure | D4899 |
| /files/1Co1Xg3BlnI94zxXsO1B | Williams %R - Chart 4 | Momentum Failure | D4900 |
| /files/Qub9BtMqmagwD7mKcu6u | Williams %R - Chart 5 | Conclusion | D4902 |
| /files/2yZI0t28HMoJr8xyxpRB | Williams %R - Chart 6 | SharpCharts | D4902 |

---

## DÉCISIONS

### D4891 — Définition Williams %R : oscillateur momentum inverse du Stochastique
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Développé par Larry Williams, %R est un oscillateur momentum qui est l'inverse du Fast Stochastic Oscillator. Il reflète le niveau du close relatif au highest high de la période look-back (le Stochastique utilise le lowest low). %R oscille de 0 à -100. Lectures 0 à -20 = suracheté. Lectures -80 à -100 = survendu. Le Fast Stochastic et %R produisent les mêmes lignes mais avec des échelles différentes.
**TRADEX-AI C1** : Williams %R peut être utilisé sur GC/HG/CL/ZW pour identifier les conditions d'extrême (suracheté/survendu) dans la logique Belkhayate d'énergie de marché — complémentaire au BGC et aux pivots pour le timing d'entrée.
*Catégorie : indicateurs_momentum*

---

### D4892 — Formule de calcul Williams %R
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md, image Spreadsheet 1) : `%R = (Highest High - Close) / (Highest High - Lowest Low) × -100`. Paramètre par défaut : 14 périodes. Le ×(-100) corrige l'inversion et déplace la décimale. Lowest Low = plus bas de la période. Highest High = plus haut de la période.
**TRADEX-AI C1** : Formule implémentable directement dans le moteur Python. Avec 14 périodes sur range bars NT8 (ex. 5 range bars GC), %R capte le momentum intraday. Exemple : Highest High=110, Lowest Low=100, Close=108 → %R = (110-108)/(110-100)×(-100) = -20 (limite suracheté).
*Catégorie : indicateurs_momentum*

---

### D4893 — La ligne centrale -50 comme niveau clé
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : La ligne centrale -50 est un niveau important. %R au-dessus de -50 = prix dans la moitié haute de la plage haut-bas → biais haussier ("cup is half full"). %R sous -50 = prix dans la moitié basse → biais baissier ("cup is half empty"). Analogie : la ligne des 50 yards au football — qui contrôle ce niveau contrôle la tendance à court terme.
**TRADEX-AI C1** : Dans TRADEX-AI, le croisement de %R au-dessus de -50 après une lecture survendue peut constituer un signal de confirmation supplémentaire pour les actifs GC/HG/CL/ZW — à ajouter dans la grille de scoring /10 au niveau C1.
*Catégorie : indicateurs_momentum*

---

### D4894 — Niveaux suracheté (-20) et survendu (-80) : définitions
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Seuils traditionnels : suracheté = au-dessus de -20 (prix près du haut de la plage 14 périodes). Survendu = sous -80 (prix près du bas de la plage 14 périodes). Ces niveaux peuvent être ajustés selon les besoins analytiques et les caractéristiques de l'instrument. %R est un oscillateur borné — quelles que soient les conditions, il reste dans la plage 0 à -100.
**TRADEX-AI C1** : Pour GC (Or), les seuils -20/-80 avec 14 périodes sur range bars sont un point de départ ; en période de fort trend (ex. breakout de GC à la hausse), %R peut rester en territoire suracheté longtemps — ne pas vendre uniquement sur -20 atteint sans confirmation directionnelle Belkhayate.
*Catégorie : indicateurs_momentum*

---

### D4895 — Suracheté n'est pas nécessairement baissier ; survendu n'est pas haussier
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md, image Chart 2) : En trend fort haussier, un actif peut rester suracheté durablement — les closes consistently près du haut indiquent une pression acheteuse soutenue. En trend fort baissier, un actif peut rester survendu durablement. Attendre une confirmation (ex. franchissement de -50) avant d'agir sur un signal de retournement.
**TRADEX-AI C1** : Règle critique pour TRADEX-AI : lors d'un fort trend sur GC/CL, le signal Williams %R seul est insuffisant. Requis : franchissement de -50 après lecture extrême + confirmation directionnelle Belkhayate (BGC, Direction) + au moins 3/4 actifs tradables alignés.
*Catégorie : gestion_risque_entree*

---

### D4896 — Confirmation après suracheté : franchir -50 à la baisse
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Après une lecture suracheté (%R > -20), le signal de confirmation d'un retournement baissier est un franchissement de %R sous -50. Cette confirmation réduit les faux signaux lors des pullbacks en tendance haussière forte.
**TRADEX-AI C1** : Dans la grille de scoring TRADEX-AI, un Williams %R qui passe sous -50 après suracheté sur GC/HG/CL/ZW peut contribuer comme signal momentum baissier confirmé — à pondérer avec BGC Direction et pivots.
*Catégorie : gestion_risque_entree*

---

### D4897 — Confirmation après survendu : franchir -50 à la hausse
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Après une lecture survendue (%R < -80), le signal de confirmation d'une reprise haussière est un franchissement de %R au-dessus de -50. Cette confirmation évite d'acheter lors des rebonds temporaires en tendance baissière forte.
**TRADEX-AI C1** : Dans TRADEX-AI, l'entrée ACHETER sur GC/HG/CL/ZW en mode auto requiert %R > -50 après lecture < -80 comme condition supplémentaire — cohérent avec la règle de confirmation 2/3 (Cercle C1 + C2 minimum).
*Catégorie : gestion_risque_entree*

---

### D4898 — Momentum Failure : définition et importance
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : L'échec de momentum ("momentum failure") se produit quand un actif ne parvient plus à repasser en territoire suracheté (ou survendu) après l'avoir atteint. L'incapacité à dépasser -20 à nouveau après plusieurs lectures > -20 signale un affaiblissement du momentum pouvant présager un déclin important. C'est un signal de "deuxième signe de faiblesse".
**TRADEX-AI C1** : Règle de momentum failure applicable à GC/CL : si %R a été > -20 plusieurs fois mais échoue à y retourner → signal de faiblesse → intégrer dans la grille de scoring C1 comme indicateur de retournement potentiel, en conjonction avec BGC et les niveaux Belkhayate.
*Catégorie : indicateurs_momentum*

---

### D4899 — Exemple Cisco : séquence momentum failure
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md, image Chart 3) : Exemple documenté Cisco : nombreuses lectures suracheté (Feb-Avr) → plongeon sous -80 début Avr → rebond au-dessus de -20 (force continue) → puis plongeon survendu Mai → récupération échoue sous -20 (1er signe faiblesse) → passage sous -50 (signal déclin momentum) → déclin marqué. Même pattern en mid-Juin → nouveau déclin.
**TRADEX-AI C1** : Ce pattern en 2 temps (échec à repasser > -20 puis passage < -50) est détectable algorithmiquement dans le moteur Python pour GC/HG/CL/ZW. Signal priorité : détecter premier échec sous -20 comme alerte précoce de retournement.
*Catégorie : indicateurs_momentum*

---

### D4900 — Williams %R adaptatif : look-back 28 périodes
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md, image Chart 4) : Exemple TJX avec Williams %R à 28 périodes (au lieu de 14). Un look-back plus long rend l'indicateur moins sensible — moins de signaux mais plus fiables. Après suracheté Oct, survendu 2x Déc, rebond Jan → %R en suracheté + breakout resistance. Pullback : %R tient au-dessus de -80 (force sous-jacente) → passage > -50 → avance marquée.
**TRADEX-AI C1** : Pour TRADEX-AI, tester Williams %R à 28 périodes sur ZW (Blé) qui peut avoir des swings plus lents — la sensibilité réduite donne des signaux plus propres. Le maintien au-dessus de -80 lors d'un pullback confirme la force sous-jacente sans aller chercher -50.
*Catégorie : indicateurs_momentum*

---

### D4901 — Williams %R 125 périodes : proxy tendance 6 mois
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Williams %R à 125 périodes couvre environ 6 mois. Au-dessus de -50 = prix au-dessus de leur moyenne 6 mois → cohérent avec uptrend. En-dessous de -50 = cohérent avec downtrend. Permet de définir la tendance principale (6 mois) avec un seul indicateur.
**TRADEX-AI C4** : Dans TRADEX-AI, %R 125 périodes sur données daily ES/DX peut servir de filtre de tendance macro — si %R 125 < -50 sur ES (marché en downtrend 6 mois), élever le seuil de signal pour les actifs de trading ACHETER sur GC/HG/CL/ZW (environnement macro défavorable).
*Catégorie : macro_evenements*

---

### D4902 — Règle d'usage : Williams %R en conjonction avec autres indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : williams_r.md) : Williams %R doit être utilisé en conjonction avec d'autres outils d'analyse technique. Volume, patterns de chart et breakouts peuvent confirmer ou infirmer les signaux de %R. L'indicateur seul est insuffisant pour prendre des décisions de trading.
**TRADEX-AI C1** : Règle alignée avec l'architecture TRADEX-AI : Williams %R contribue à la grille de scoring /10 mais ne génère jamais un signal seul. La règle 3/4 actifs tradables + 2/3 confirmation reste le filtre principal. %R est un indicateur parmi les 7 cercles d'intelligence.
*Catégorie : gestion_risque_entree*

---

### D4903 — Scan technique : %R remonte depuis survendu (signal haussier)
🔵 **ÉCOLE** (Source : williams_r.md) : Critères de scan haussier : actif au-dessus de sa SMA(200) (uptrend long terme) + %R(14) était < -80 il y a 20 jours + %R(14) croise -50 aujourd'hui. Cette combinaison identifie les pullbacks dans un uptrend qui se retournent à la hausse.
**TRADEX-AI C1** : Ce pattern (GC au-dessus SMA200 + %R pullback < -80 puis retour > -50) est un setup d'entrée ACHETER classique — applicable dans TRADEX-AI si la SMA200 daily est disponible via NT8 et si le scoring /10 ≥ 7,0.
*Catégorie : configuration*

---

### D4904 — Scan technique : %R descend depuis suracheté (signal baissier)
🔵 **ÉCOLE** (Source : williams_r.md) : Critères de scan baissier : actif sous sa SMA(200) (downtrend long terme) + %R(14) était > -20 il y a 20 jours + %R(14) croise -50 à la baisse aujourd'hui. Cette combinaison identifie les rebonds dans un downtrend qui se retournent à la baisse.
**TRADEX-AI C1** : Pour les actifs TRADEX en downtrend (GC < SMA200), ce pattern (%R rebond > -20 puis passage < -50) constitue un setup VENDRE — mais la règle R/R ≥ 1:2 doit être vérifiée avant toute exécution, et le mode Auto reste BLOQUÉ par défaut.
*Catégorie : configuration*
