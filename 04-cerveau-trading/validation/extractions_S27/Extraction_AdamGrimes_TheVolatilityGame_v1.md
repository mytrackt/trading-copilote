# Extraction AdamGrimes — The Volatility Game
**Source :** `bundles/adamgrimes/the_volatility_game.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6951 → D6970 · **Page :** https://www.adamhgrimes.com/the-volatility-game/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Visualisation de la volatilité implicite vs réalisée par secteur — outil de veille macro volatilité applicable à C5 (Sentiment/VIX) et C7 (Corrélations).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6951 — Volatilité implicite vs volatilité réalisée : deux mesures distinctes
🟢 **FAIT VÉRIFIÉ** (Source : the_volatility_game.md) : La volatilité implicite (IV) est une prévision du marché des options sur la volatilité future d'un actif. La volatilité historique (HV / réalisée) mesure les mouvements effectifs passés. Ces deux métriques ne sont pas identiques et leur relation est porteuse d'information sur le risque perçu vs le risque réel.
**TRADEX-AI C5** : Pour VX (VIX), suivre simultanément le VIX courant (IV du S&P 500) et la volatilité réalisée 20j. Un IV très supérieur à HV signale une prime de peur excessive — potentiel retour à la normale favorable aux actifs risqués (GC, CL).
*Catégorie : indicateurs_momentum*

### D6952 — Hausse de l'IV sans hausse de la HV : signal d'anticipation d'événement
🟢 **FAIT VÉRIFIÉ** (Source : the_volatility_game.md) : Quand la volatilité implicite monte mais que la volatilité réalisée reste stable, cela signifie que le marché des options price un événement futur risqué (ex. publication macro, résultats). Ce pattern est visible sector-wide lorsqu'un risque systémique est anticipé.
**TRADEX-AI C4** : Avant NFP/FOMC/CPI, l'IV des actifs GC/CL monte typiquement sans que la HV n'ait bougé. Le News Gate (blocage 30 min avant événements) est justifié précisément par ce mécanisme : la prime de risque est déjà dans les prix, le mouvement réel est imprévisible.
*Catégorie : macro_evenements*

### D6953 — Montée corrélée de l'IV dans tout un secteur : signal de risque systémique
🟡 **SYNTHÈSE** (Source : the_volatility_game.md) : Lorsque l'IV monte de façon coordonnée dans l'ensemble d'un secteur (et non sur un seul nom), cela indique un risque macro diffus plutôt qu'un risque idiosyncratique. L'analyse sectorielle de la volatilité donne une vue impossible actif par actif.
**TRADEX-AI C5** : Si VX (VIX) monte et que l'IV de CL/GC monte simultanément de façon cohérente, c'est un signal de risque macro. Réduire la taille des positions ou bloquer le mode Auto jusqu'à normalisation.
*Catégorie : gestion_risque_entree*

### D6954 — Visualisation HV vs IV : outil de surveillance hebdomadaire
🔵 **ÉCOLE** (Source : the_volatility_game.md) : Adam Grimes consulte un graphique HV (axe X) vs IV (axe Y) plusieurs fois par semaine pour chaque secteur. Le point courant + la queue du dernier mois permet de voir : (1) direction du mouvement récent de volatilité, (2) secteurs outliers, (3) fragmentation vs mouvement en unisson des marchés.
**TRADEX-AI C5** : Intégrer dans le dashboard une vue simplifiée HV vs IV pour les actifs CONFIRMATION (DX, ES, VX) actualisée à chaque cycle. Les outliers (actifs dont IV s'éloigne de la normale) déclenchent un flag de surveillance renforcée.
*Catégorie : indicateurs_momentum*

### D6955 — Corrélation de la volatilité : fragmentation vs mouvement en unisson
🟢 **FAIT VÉRIFIÉ** (Source : the_volatility_game.md) : L'analyse de la corrélation entre volatilités de différents marchés révèle si les marchés se comportent de façon coordonnée (risque systémique élevé) ou fragmentée (risque idiosyncratique). Un mouvement en unisson de la volatilité indique un stress généralisé.
**TRADEX-AI C7** : La matrice de corrélations C7 (GC/HG/CL/ZW/ES/VX) doit inclure non seulement les corrélations de rendement mais aussi un indicateur de corrélation des volatilités. Quand les volatilités se corrèlent fortement, réduire ou bloquer les signaux Auto.
*Catégorie : correlations*

### D6956 — IV croissante + HV croissante (Tech, secteur exemple) : double signal d'accélération
🟡 **SYNTHÈSE** (Source : the_volatility_game.md) : Lorsqu'un secteur voit à la fois son IV et sa HV augmenter (queue vers le haut-droite dans le graphique HV/IV), cela indique une accélération réelle de la volatilité confirmée par le marché des options. Ce double signal est plus fort qu'une hausse isolée d'IV.
**TRADEX-AI C1** : Pour GC (Or), si la HV 10j augmente ET que l'IV sur futures or monte simultanément, le contexte de volatilité est en expansion. Ajuster les stops en conséquence et ne pas trader les setups de range étroit (ils seraient invalidés par l'expansion de volatilité).
*Catégorie : gestion_position_active*

### D6957 — Anomalie d'IV non liée aux résultats : signal d'information asymétrique
🔵 **ÉCOLE** (Source : the_volatility_game.md) : Si l'IV d'un actif monte fortement sans calendrier d'événements connu (earnings, macro), il faut rechercher la cause. Cette anomalie peut signaler une information non publique ou un risque géopolitique/sectoriel émergent.
**TRADEX-AI C6** : Dans le moteur de news (C6), lier les alertes d'anomalie d'IV à un scan de nouvelles. Un spike d'IV inexpliqué sur GC ou CL (Or, Pétrole) déclenche un mode information-gathering : bloquer les signaux Auto jusqu'à identification de la cause.
*Catégorie : macro_evenements*
