# Extraction NinjaTrader — Order Flow Indicators
**Source :** `bundles/ninjatrader/order_flow_indicators.md` (HTML statique · en-tête `# SOURCE: https://ninjatrader.com/learn/order-flow-indicators/`) + 0 image certifiée
**Méthode images :** ancrage figcaption locale (scraper_static) · **0/0 certifiée** · le manifest indique « aucune figure `<figure>`+`<figcaption>` sur la page »
**Décisions :** D339 → D349 · **Page :** ninjatrader.com/learn/order-flow-indicators/
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** pour le **cercle C2 (order flow ATAS)** — tape/Time&Sales, Level 2, DOM, footprint, delta cumulé, volume profile. NinjaTrader est une source **Tier 2 broker** : les définitions de structure de marché sont factuelles 🟢 ; toute consigne d'usage/lecture « maison NinjaTrader » est marquée 🔵 ÉCOLE. ATAS reste l'outil order flow verrouillé du projet ; cette page sert de cadre conceptuel transposable.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | (aucune figure `<figure>`+`<figcaption>` sur la page — manifest 0/0) | — | — |

> Aucune image citable. Toutes les décisions ci-dessous reposent sur le texte littéral du bundle.

---

## DÉCISIONS

### D339 — Définition de l'order flow en futures
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : L'order flow trading se concentre sur la façon dont les ordres **entrent, interagissent et sont exécutés** sur les marchés à terme. Chaque mouvement de prix résulte d'un échange de contrats entre acheteurs et vendeurs. À haut niveau, il observe : les **ordres au marché** frappant le bid ou l'offer, les **ordres à cours limité** en attente d'exécution, et les **changements de liquidité** à différents niveaux de prix.
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : L'order flow **ne prédit pas** les prix futurs ; il **réagit** à la participation de marché en temps réel et aide à interpréter ce qui se déroule, contrairement à l'analyse technique classique fondée sur les seules données historiques.
**TRADEX-AI C2** : Cadre fondateur du cercle order flow — surveiller flux d'ordres au marché vs limites et variations de liquidité sur GC/HG/CL/ZW (via ATAS), traités comme inputs **réactifs**, pas prédictifs.
*Catégorie : structure_marche*

---

### D340 — L'order flow révèle ce que les bougies cachent
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Les graphiques en chandeliers résument le mouvement de prix dans le temps mais ne montrent pas l'activité qui a créé ces mouvements. L'order flow vise à révéler le **processus de décision** derrière chaque changement de prix en analysant les transactions exécutées, les ordres au repos et les changements de liquidité.
🔵 **ÉCOLE** (Source : order_flow_indicators.md) : En étudiant les indicateurs d'order flow, le trader peut voir où la pression acheteuse/vendeuse **augmente, stagne ou se déplace**, ce qui aide à comprendre pourquoi le prix réagit à certains niveaux.
**TRADEX-AI C2/C1** : Coupler la lecture order flow (ATAS) à la structure prix Belkhayate (pivots/BGC) pour expliquer la réaction du prix aux niveaux clés sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D341 — Tape (Time and Sales) : brique de données fondamentale
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : L'analyse order flow repose sur quelques sources de données cœur montrant différents aspects de l'activité de marché. Le **Tape (Time and Sales)** en fait partie (énuméré comme brique de base aux côtés du Level 2 et du DOM).
🔴 **NON VÉRIFIÉ** (lacune source) : Le bundle **liste** Tape / Level 2 / DOM comme sous-sections mais leurs paragraphes de description sont **vides** sur cette page (en-têtes sans corps). Définition opérationnelle du Tape à compléter via une autre source.
**TRADEX-AI C2** : Brancher le flux Time&Sales d'ATAS comme entrée du cercle C2 ; documentation détaillée à compléter (source NinjaTrader muette ici).
*Catégorie : structure_marche*

---

### D342 — Level 2 et Depth of Market (DOM) : briques de liquidité
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Le **Level 2 Market Data** et le **Depth of Market (DOM)** sont identifiés comme sources de données cœur de l'order flow, montrant les ordres limités au repos et la liquidité aux différents niveaux de prix.
🔴 **NON VÉRIFIÉ** (lacune source) : Les sections Level 2 et DOM n'ont **pas de texte descriptif** dans le bundle (en-têtes seuls). La distinction Level 2 vs DOM n'est pas explicitée par la source.
**TRADEX-AI C2** : Exploiter le carnet d'ordres (DOM/L2) d'ATAS pour repérer accumulation/retrait de liquidité sur GC/HG/CL/ZW ; définitions précises à sourcer ailleurs.
*Catégorie : structure_marche*

---

### D343 — Volume footprint : volume négocié par niveau de prix
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Les **volume footprint charts** affichent le **volume négocié à chaque niveau de prix au sein d'une barre**.
**TRADEX-AI C2** : Footprint ATAS = lecture du volume intra-barre par niveau ; brique cœur du cercle order flow sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D344 — Bid-ask imbalance : zones de pression dominante
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Les **bid-ask imbalance tools** mettent en évidence les zones où la **pression acheteuse ou vendeuse est dominante**.
**TRADEX-AI C2** : Détecter les déséquilibres bid/ask dans le footprint ATAS comme signal de pression directionnelle ; à confirmer par price action (cf. D348).
*Catégorie : signal*

---

### D345 — Cumulative delta : différentiel net achat/vente dans le temps
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Le **cumulative delta** suit la **différence nette entre volume acheteur et volume vendeur dans le temps**.
**TRADEX-AI C2** : Delta cumulé ATAS = mesure du flux net acheteur/vendeur ; surveiller divergences delta/prix sur GC/HG/CL/ZW (confirmation, jamais signal isolé — cf. D348).
*Catégorie : signal*

---

### D346 — Volume profile : concentration d'activité par session
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Les **volume profiles** montrent **où l'activité de trading s'est concentrée durant une session**.
🔵 **ÉCOLE** (Source : order_flow_indicators.md) : Ces indicateurs d'order flow sont souvent utilisés **en complément** des graphiques traditionnels plutôt que comme signaux autonomes ; pour le débutant, l'objectif est de comprendre ce que chaque outil représente avant de décider de sa place dans le plan de trading.
**TRADEX-AI C2/C1** : Volume profile ATAS pour repérer zones de forte activité (HVN/LVN) et croiser avec pivots Belkhayate ; usage en complément du chart, pas en autonome.
*Catégorie : structure_marche*

---

### D347 — Lecture order flow en 3 étapes (cadre NinjaTrader)
🔵 **ÉCOLE** (Source : order_flow_indicators.md) : NinjaTrader propose une approche structurée en 3 étapes — **(1)** commencer avec **un seul outil** pour comprendre la donnée (ex. observer la réaction du prix quand de gros ordres au marché frappent le bid/ask) ; **(2)** **connecter l'order flow au comportement du prix** (le prix monte/baisse-t-il après l'apparition de pression, ou stagne-t-il malgré l'activité ?) ; **(3)** **pratiquer en simulation** pour observer sans la pression du live. L'accent est mis sur clarté, contexte et pratique régulière plutôt que la chasse aux signaux.
**TRADEX-AI C2** : Méthodologie d'apprentissage maison (interprétation NinjaTrader) ; transposable en protocole d'onboarding order flow, sans valeur de règle d'entrée.
*Catégorie : signal*

---

### D348 — Risques et erreurs : order flow réactif, jamais prédictif ni isolé
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Limites de l'order flow — les marchés à terme peuvent changer vite, la **liquidité visible peut se déplacer sans préavis**, et de **gros ordres n'entraînent pas toujours un mouvement durable**. Les indicateurs montrent l'**activité en temps réel, pas l'intention**, d'où l'importance du contexte large et d'une interprétation disciplinée.
🔵 **ÉCOLE** (Source : order_flow_indicators.md) : Erreurs courantes — traiter les indicateurs comme **prédictifs** plutôt que réactifs ; **surcharger** les graphiques de trop de visuels ; **ignorer la structure de timeframe supérieur** et les niveaux clés ; trader **émotionnellement** sur les fluctuations court terme.
**TRADEX-AI C2/gestion_risque** : Garde permanente — un signal order flow (footprint/delta/imbalance) sur GC/HG/CL/ZW exige confirmation par structure timeframe supérieur + niveaux Belkhayate ; ne jamais traiter comme prédictif ni l'utiliser seul. Garde anti-faux-signal.
*Catégorie : gestion_risque_entree*

---

### D349 — Order flow comme partie d'un cadre, pas un raccourci
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_indicators.md) : Comprendre les risques aide à aborder l'order flow avec des attentes réalistes et à l'utiliser comme **partie d'un cadre de trading plus large**, et non comme un raccourci.
🔵 **ÉCOLE** (Source : order_flow_indicators.md) : NinjaTrader se présente comme environnement d'apprentissage (charting avancé, outils DOM, indicateurs order flow intégrés, sim trading) pour étudier le développement de la pression acheteuse/vendeuse en temps réel.
**TRADEX-AI C2** : Intégrer l'order flow ATAS dans la grille déterministe /10 comme cercle C2 parmi 7, jamais comme déclencheur autonome ; cohérent avec la règle 3/4 trading + 2/3 confirmation.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D339 → D349 (11) |
| Images certifiées citées | 0/0 (aucune figure sur la page — manifest) |
| Catégories utilisées | structure_marche · signal · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🔴 NON VÉRIFIÉ |
| Cercle dominant | **C2 (order flow ATAS)** — tape, L2, DOM, footprint, delta, volume profile |
| Belkhayate | **NON directement concerné** — page conceptuelle order flow ; croisements C2↔C1 (pivots/BGC) signalés en D340, D346 |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.

### Cas « à vérifier » (lacunes source)
- **D341 (Tape) · D342 (Level 2 / DOM)** : les en-têtes existent dans le bundle mais les **paragraphes descriptifs sont vides** (contenu probablement chargé en JavaScript / accordéon non rendu par scraper_static). Définitions opérationnelles Tape / L2 / DOM à compléter via une autre source Tier 1/Tier 2 → marqué 🔴 NON VÉRIFIÉ.
- **Section « What you'll learn »** : en-tête vide, sans contenu exploitable.
- **0 image** : aucune figure certifiable sur la page — aucune décision ne s'appuie sur une image.
