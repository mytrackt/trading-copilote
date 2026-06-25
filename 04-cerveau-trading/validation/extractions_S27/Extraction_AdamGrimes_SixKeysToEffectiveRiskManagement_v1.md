# Extraction AdamGrimes — Six Keys To Effective Risk Management
**Source :** `bundles/adamgrimes/six_keys_to_effective_risk_management.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6611 → D6626 · **Page :** https://www.adamhgrimes.com/six-keys-to-effective-risk-management/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Cadre de gestion du risque en 6 axes (extrêmes, risques courants, edge, biais psychologique, risques hors-marché, humilité).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6611 — Risques impossibles à connaître : rester humble
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : Certains risques de marché sont par nature inconnaissables. Tout plan de gestion du risque doit intégrer une marge pour l'inconnu et l'inconnaissable. Les grands traders rappellent systématiquement d'éviter l'hubris.
**TRADEX-AI C4** : Le moteur TRADEX ne doit jamais signaler une confiance à 100% ; le fallback ATTENDRE s'active automatiquement dès que les conditions sont incomplètes ou inconnues.
*Catégorie : gestion_risque_entree*

### D6612 — Événements extrêmes : toujours sous-estimés
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : Il faut étudier les événements les plus extrêmes survenus dans son marché ET dans les marchés analogues sur toute l'histoire disponible, puis supposer que les événements futurs seront encore plus extrêmes que ce qu'on peut imaginer.
**TRADEX-AI C4** : Le circuit breaker de TRADEX doit être calibré sur les drawdowns extrêmes historiques de GC/HG/CL/ZW (ex. choc COVID mars 2020, krach 2008), pas seulement sur la volatilité récente. Le seuil VIX critique doit refléter ces extrema.
*Catégorie : gestion_risque_entree*

### D6613 — Risques « du milieu » : mille coupures fatales
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : Les risques courants (qui surviennent quelques fois par an) tuent autant de comptes que les événements extrêmes. Se concentrer uniquement sur les risques catastrophiques expose le trader aux risques ordinaires qui s'accumulent.
**TRADEX-AI C5** : La surveillance de staleness (données périmées), les glissements de stop répétés et les coûts de transaction récurrents sur GC/HG/CL/ZW doivent être trackés dans le risk_manager.py comme « risques courants ».
*Catégorie : gestion_position_active*

### D6614 — La stratégie elle-même est un risque
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : La plus grande erreur des traders en développement est d'utiliser une stratégie sans edge réel. Si on ne sait pas précisément quel est son edge, c'est qu'on n'en a pas. Un système non examiné ne mérite pas d'être tradé.
**TRADEX-AI C1** : La règle 3/4 actifs trading + 2/3 confirmation alignés est le filtre d'edge déterministe de TRADEX. Toute modification de ce filtre doit passer par un backtest validé avant déploiement.
*Catégorie : psychologie*

### D6615 — Le trader lui-même est le risque principal
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : La discipline doit être absolue à chaque instant de chaque journée de trading. La préparation, la planification et les heures d'écran ne valent rien si l'exécution dérive. Le marché pousse à la limite de l'endurance humaine.
**TRADEX-AI C5** : Le mode Manuel de TRADEX affiche le signal mais laisse Abdelkrim décider — ce design respecte ce principe en évitant l'over-ride émotionnel automatique. Le mode Auto est verrouillé par défaut précisément pour cette raison.
*Catégorie : psychologie*

### D6616 — Risques hors-marché : anticiper les interférences externes
🟢 **FAIT VÉRIFIÉ** (Source : six_keys_to_effective_risk_management.md) : Stress financier personnel, problèmes de santé, changements réglementaires, comportements irrationnels des investisseurs — tous ces éléments externes impactent le trading de façon difficile à quantifier mais réelle. Une planification prudente permet de les traverser.
**TRADEX-AI C4** : Le risk_manager.py doit inclure un flag « session_impaired » (activable manuellement) qui bascule le mode Auto en mode Manuel et réduit la taille des positions.
*Catégorie : gestion_risque_entree*

### D6617 — Humilité systémique : il y a toujours plus à ne pas savoir
🟡 **SYNTHÈSE** (Source : six_keys_to_effective_risk_management.md) : Même avec une analyse exhaustive des risques extrêmes et courants, la réalité dépassera les estimations les plus pessimistes. L'humilité n'est pas une posture mais une nécessité structurelle.
**TRADEX-AI C1** : Le score /10 de TRADEX doit intégrer un coefficient d'incertitude : si plus de 2 cercles sur 7 manquent de données fraîches, le score plafonné à 6.5 quelle que soit la somme brute.
*Catégorie : gestion_risque_entree*
