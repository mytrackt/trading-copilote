# Extraction AdamGrimes — Trade Pullbacks
**Source :** `bundles/adamgrimes/trade_pullbacks.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7091 → D7110 · **Page :** https://www.adamhgrimes.com/trade-pullbacks/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthode pullback applicable directement sur GC/CL/HG/ZW — entrée après retracement vers la moyenne dans un trend validé.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

---

## DÉCISIONS

### D7091 — Pullback = prédiction de continuation de tendance
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Trader un pullback est une prédiction explicite que le marché va continuer à trendre — il ne s'agit pas seulement d'identifier un trend existant mais d'anticiper sa prolongation sur au moins une jambe supplémentaire.
**TRADEX-AI C1** : Pour GC/CL/HG/ZW, tout signal pullback doit être validé par la lecture de structure de marché Belkhayate (BGC, Direction) confirmant la continuation — signal ACHETER ou VENDRE uniquement si le trend sous-jacent est actif.
*Catégorie : structure_marche*

### D7092 — Conditions préalables au pullback : trend + oscillation
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Deux conditions nécessaires et simultanées : (1) le marché doit être en trend, (2) le marché doit osciller (pullbacks présents). Les trends très forts sans oscillation ne se tradent pas en pullback — forcer l'entrée dans ce cas est une erreur.
**TRADEX-AI C1** : Si GC ou CL est en tendance directionnelle très forte (barres Belkhayate consécutives sans retracement), passer en mode ATTENDRE pour les entrées pullback.
*Catégorie : structure_marche*

### D7093 — Bandes calibrées pour identifier le mouvement fort
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Les bandes (Keltner ou Bollinger) doivent contenir ~80-90% de l'action prix. Le contact avec la bande extérieure signale un mouvement fort (condition de déclenchement). Keltner jugé préférable à Bollinger par Grimes. Paramètres à fixer une fois pour toutes sans modification.
**TRADEX-AI C1** : Utiliser des bandes Keltner calibrées 80-90% comme filtre de déclenchement sur les charts NT8 pour GC/HG/CL/ZW — un bar touchant la bande extérieure = condition de setup pullback active.
*Catégorie : indicateurs_tendance*

### D7094 — Entrée près de la moyenne mobile : concept, pas magie
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : L'avantage statistique existe en entrant près de la moyenne quelle que soit la longueur exacte de la MM utilisée. Ce n'est pas la valeur de la MM qui compte mais la discipline d'une approche cohérente et systématique des entrées. L'entrée peut se faire en avance ou au travers de la MM.
**TRADEX-AI C1** : La MM centrale des bandes Keltner sur NT8 sert de zone d'entrée cible pour les pullbacks sur GC/CL/HG/ZW — la cohérence d'application prime sur la valeur exacte du paramètre.
*Catégorie : gestion_risque_entree*

### D7095 — Éviter les moves d'épuisement (climax) lors des entrées
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Acheter/vendre après un move potentiellement climactique (grande range, bar avec-tendance dépassant loin la bande) est à éviter. Distinguer la force réelle avec-tendance de l'épuisement est la compétence technique clé du trading directionnel. Aucun système parfait mais les cas évidents sont esquivables.
**TRADEX-AI C2** : Sur GC/CL, corroborer avec l'order flow ATAS : un delta épuisé (acheteurs présents mais prix stagne ou retourne) identifie l'épuisement vs la vraie force. Bloquer signal si barre climactique détectée.
*Catégorie : configuration*

### D7096 — Déclencheur d'entrée : breakout sur timeframe inférieure
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Raffiner l'entrée pullback par un breakout sur timeframe inférieure (ex. dépassement du high de la barre précédente). Alternative : trades autour de pivots TF inférieure (failure test). Ces confluences multi-timeframe renforcent la qualité du signal.
**TRADEX-AI C1** : Pour NT8, combiner le signal pullback sur le timeframe principal avec un déclencheur sur la TF inférieure (breakout pivot) avant de soumettre l'ordre — applicable en mode Manuel et Auto.
*Catégorie : gestion_risque_entree*

### D7097 — Stop placement : au-delà de l'extrême précédent
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Les stops sur les pullbacks doivent être placés au-delà de l'extrême précédent pertinent. Règle approximative de départ : 2 à 4 ATR au-delà de l'entrée. Connaître son point de sortie avant l'entrée, sur chaque trade.
**TRADEX-AI C1** : Risk Manager TRADEX doit calculer automatiquement le stop initial à 2-4 ATR de l'entrée pour tout signal pullback sur GC/HG/CL/ZW, valeur affichée avant confirmation.
*Catégorie : gestion_risque_entree*

### D7098 — Gestion de trade : prise de profit partielle = 1R
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Prendre les premiers profits quand le profit équivaut au risque initial (1R). Réduire la position ensuite. Cette approche favorise la consistance plutôt que les home runs. Style swing = une oscillation propre.
**TRADEX-AI C1** : En mode Auto, programmer la sortie partielle à 1R pour les actifs GC/CL/HG/ZW. Remainder tenu jusqu'au swing target ou stop suivant.
*Catégorie : gestion_position_active*

### D7099 — Pyramiding sécurisé dans les trends forts
🟢 **FAIT VÉRIFIÉ** (Source : trade_pullbacks.md) : Construire une position en pyramide via des pullbacks successifs est possible en respectant cette règle : après chaque ajout, prendre profits partiels et déplacer les stops de sorte que le risque total ne dépasse jamais l'équivalent d'un seul trade. Les gaps et slippage peuvent survenir — respecter le risque en toutes circonstances.
**TRADEX-AI C1/C4** : Sur GC en trend fort (ex. breakout institutionnel Belkhayate), la pyramide est autorisée uniquement si chaque palier respecte la règle de risque ≤ 1 trade. Bloquer en Mode Auto si conditions non réunies.
*Catégorie : gestion_position_active*

### D7100 — Le "meilleur pullback" plutôt que "tout pullback"
🟡 **SYNTHÈSE** (Source : trade_pullbacks.md) : L'expérience fait évoluer le trader d'une approche mécanique "prendre tout pullback" vers une approche sélective "trouver le meilleur pullback". Les meilleurs patterns sont souvent visuellement imparfaits mais positionnés sur de beaux niveaux de structure. La symétrie visuelle n'est pas le critère de qualité.
**TRADEX-AI C1** : Le filtre qualitatif Belkhayate (score /10 ≥ 7,0 + critères éliminatoires) incarne cette sélectivité — ne pas déclencher de signal sur chaque pullback visible mais seulement ceux répondant aux critères de structure.
*Catégorie : psychologie*

### D7101 — Pyramiding requiert discipline sur les stops
⚫ **HYPOTHÈSE PROJET** (Source : trade_pullbacks.md) : Scaler dans les pullbacks (ajouter des lots progressivement) expose au risque d'être "le plus grand quand on a le plus tort" — position maximale au moment où le trade va contre soi. Cette technique requiert un niveau de discipline supérieur et n'est pas recommandée aux traders débutants.
**TRADEX-AI C1** : En Mode Auto TRADEX, le scaling-in est désactivé par défaut. Uniquement disponible en Mode Manuel avec confirmation explicite d'Abdelkrim.
*Catégorie : gestion_position_active*
