# Extraction AdamGrimes — Know Your Risk
**Source :** `bundles/adamgrimes/know_your_risk.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6171 → D6185 · **Page :** https://www.adamhgrimes.com/know-your-risk/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : gestion du risque multi-dimensionnelle — contexte C2/C3/C7 pour les garde-fous TRADEX (risk_manager.py, corrélations, circuit breaker, gap risk).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6171 — Règle fondamentale : définir le risque AVANT l'entrée, chaque trade
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : La règle absolue du trader professionnel est de définir le risque maximal accepté AVANT d'entrer dans un trade. Les amateurs pensent aux gains; les professionnels définissent d'abord la perte maximale.
**TRADEX-AI C1** : Le moteur TRADEX doit calculer et afficher le risque (distance stop × taille position) AVANT d'envoyer un signal, tant en mode Manuel qu'en mode Auto. Toujours afficher "Risque max : X$" dans l'interface avant toute décision.
*Catégorie : gestion_risque_entree*

### D6172 — Un stop serré n'est PAS équivalent à un faible risque
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Un stop serré peut paradoxalement porter plus de risque qu'un stop large si l'espérance (expectancy) du système ne le supporte pas. Le risque réel dépend du ratio gain/perte combiné au taux de réussite, pas seulement de la distance du stop.
**TRADEX-AI C1** : Dans risk_manager.py : ne pas paramétrer les stops uniquement sur une distance fixe. Intégrer l'expectancy du système dans l'évaluation. Un stop trop serré sur GC (Or, volatil) peut avoir une espérance négative même avec un bon signal Belkhayate.
*Catégorie : gestion_risque_entree*

### D6173 — Risque de corrélation : 6 positions ne sont pas 6 risques indépendants
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Les positions corrélées amplifient le risque réel. En actions, long et short peuvent se comporter comme un seul risque. En futures/devises, les corrélations se resserrent souvent dans les moments de stress — précisément quand on ne le veut pas.
**TRADEX-AI C7** : Les 4 actifs TRADING (GC/HG/CL/ZW) ne doivent jamais être traités comme 4 risques indépendants. La matrice de corrélation live 30j dans correlations.py doit bloquer ou réduire la taille si GC et CL montrent une corrélation > 0,7 simultanément — risque agrégé amplifié.
*Catégorie : gestion_position_active*

### D6174 — Penser horizontalement (portefeuille) pas seulement verticalement (trade unique)
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Même un trader court terme a un portefeuille dès qu'il a plusieurs positions ouvertes. Il faut penser à la fois à la gestion verticale (stop/target d'un trade) et horizontale (comportement des positions ensemble).
**TRADEX-AI C7** : TRADEX doit afficher une vue agrégée du risque total (somme des risques sur positions ouvertes GC+HG+CL+ZW). Le tableau de bord Mode Manuel doit inclure "Risque portefeuille total" en temps réel, pas seulement le risque du signal en cours.
*Catégorie : gestion_position_active*

### D6175 — Risque de gap : planifier avant, pas réagir après
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Le gap risk (ouverture bien au-delà du stop) doit être évalué à l'avance, pas géré en urgence. Avoir un plan pré-défini pour les gaps permet d'éviter les réactions émotionnelles.
**TRADEX-AI C1** : Le moteur TRADEX doit inclure une alerte pre-session sur les événements gap potentiels (NFP, FOMC, CPI). Le News Gate existant couvre 30min avant/après — l'étendre pour identifier également les gaps overnight sur GC/CL en cas d'événement géopolitique C6 majeur.
*Catégorie : gestion_risque_entree*

### D6176 — Risque de liquidité : le spread peut exploser au mauvais moment
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : La liquidité peut se détériorer précisément quand on doit sortir. Un ordre moyen peut déplacer le marché. Le spread peut passer de minimal à significatif lors d'une sortie forcée.
**TRADEX-AI C2** : Pour les actifs moins liquides (ZW — Blé), le moteur TRADEX doit surveiller la profondeur du marché (bid-ask spread via ATAS). Un spread anormalement large doit déclencher un avertissement avant d'émettre un signal. Intégrer dans staleness_monitor.py comme indicateur de santé de liquidité.
*Catégorie : volume_liquidite*

### D6177 — Risque émotionnel : certains événements cassent le contrôle émotionnel
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Des événements externes peuvent déclencher une réaction en chaîne qui compromet le contrôle émotionnel du trader, même chez les professionnels. Ce risque est réel, non académique.
**TRADEX-AI C5** : Le garde-fou G de suspension automatique après une perte (15–60 min dans risk_manager.py) est directement aligné sur ce principe. Après 2 pertes consécutives, le mode Auto se suspend pour éviter le trading émotionnel. Ce mécanisme doit être non-bypassable dans l'UI.
*Catégorie : psychologie*

### D6178 — Risque de contrepartie et de crédit : pas une abstraction académique
🟢 **FAIT VÉRIFIÉ** (Source : know_your_risk.md) : Les risques de crédit et de contrepartie sont réels, même pour les traders individuels (broker failure, défaut de chambre de compensation, etc.).
**TRADEX-AI C3** : Conserver les actifs de confirmation C3 (COT/CFTC) pour détecter les signaux de stress institutionnel inhabituels qui pourraient précéder des événements de contrepartie. Dans l'interface, afficher le statut du broker/connexion Rithmic comme indicateur de santé système.
*Catégorie : gestion_risque_entree*

### D6179 — Le risque réel est toujours plus profond que le risque apparent
🟡 **SYNTHÈSE** (Source : know_your_risk.md) : Le risque "déclaré" (distance stop × taille) est la surface visible. Dessous : expectancy, corrélations, gaps, liquidité, émotions, contrepartie. Chaque trade a plus de risques visibles qu'on ne le pense.
**TRADEX-AI C1** : Le score de confiance TRADEX (/10) doit intégrer implicitement plusieurs couches de risque : Belkhayate (C1), order flow (C2), contexte macro (C4), sentiment (C5). Un score ≥ 7,0 ne garantit pas un trade gagnant — il garantit uniquement que les conditions multiples sont alignées selon les règles Belkhayate.
*Catégorie : gestion_risque_entree*
