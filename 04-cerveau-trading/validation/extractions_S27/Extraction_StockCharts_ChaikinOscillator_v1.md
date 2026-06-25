# Extraction StockCharts — Chaikin Oscillator
**Source :** `bundles/stockcharts/chaikin_oscillator.md` (HTTP 200 · ~8 000 car.) + 8 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 8/8 certifiées
**Décisions :** D1171 → D1184 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-oscillator
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - Chaikin Oscillator | Calculating the Chaikin Oscillator | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 - Chaikin Oscillator | Interpreting the Chaikin Oscillator | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 - Chaikin Oscillator | Buying/Selling Bias | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 - Chaikin Oscillator | Buying/Selling Bias | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 5 - Chaikin Oscillator | Divergences | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 6 - Chaikin Oscillator | Divergences | CERTIFIE (accord .md + HTML) |
| image_07.png | Chart 7 - Chaikin Oscillator | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_08.png | SharpCharts - Chaikin Oscillator | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1171 — Nature et origine du Chaikin Oscillator
🔵 **ÉCOLE (Chaikin)** (Source : chaikin_oscillator.md) : Développé par Marc Chaikin, le Chaikin Oscillator mesure le momentum de l'Accumulation Distribution Line (ADL) en appliquant la formule du MACD. C'est donc un « indicateur d'un indicateur ». Il est conçu pour anticiper les changements de direction de l'ADL en mesurant le momentum derrière les mouvements ; un changement de momentum étant la première étape d'un changement de tendance. Il génère des signaux par croisement au-dessus/dessous de la ligne zéro ou par divergences haussières/baissières.
**TRADEX-AI C2** : Indicateur de flux monétaire (buying/selling pressure) candidat comme couche de confirmation order flow ; jamais déclencheur d'ordre seul (l'auteur le dit explicitement, cf. D1180).
*Catégorie : indicateurs_momentum*

---

### D1172 — Formule de calcul (4 étapes ADL → oscillateur)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_01) : Le calcul passe par l'ADL puis une différence d'EMA :
```
1. Money Flow Multiplier = [(Close - Low) - (High - Close)] / (High - Low)
2. Money Flow Volume = Money Flow Multiplier x Volume de la période
3. ADL = ADL précédent + Money Flow Volume de la période courante
4. Chaikin Oscillator = (EMA 3 jours de l'ADL) - (EMA 10 jours de l'ADL)
```
**TRADEX-AI C2** : Formule déterministe implémentable telle quelle ; nécessite un flux volume fiable (NT8/ATAS) pour GC/HG/CL/ZW. Paramètres par défaut (3,10).
*Catégorie : indicateurs_momentum*

---

### D1173 — Mécanique du Money Flow Multiplier et bascule positive/négative
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md) : L'ADL monte quand le Money Flow Multiplier est positif et baisse quand il est négatif. Le multiplicateur est positif quand la clôture est dans la moitié haute du range high-low de la période, négatif quand elle est dans la moitié basse. En tant qu'oscillateur de type MACD, le Chaikin Oscillator devient positif quand l'EMA 3 jours rapide passe au-dessus de l'EMA 10 jours lente, et négatif quand l'EMA 3 jours passe en dessous.
**TRADEX-AI C2** : La position de la clôture dans le range pondère le flux ; cohérent avec une lecture order flow de la pression acheteuse/vendeuse.
*Catégorie : indicateurs_momentum*

---

### D1174 — Indicateur de 3e dérivée, risque de déconnexion du prix
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_02) : L'indicateur est à trois étapes du prix sous-jacent : (1) prix et volume sont transformés en ADL, (2) des EMA sont appliquées à l'ADL, (3) la différence des EMA forme le Chaikin Oscillator. En tant que 3e dérivée, il est plus susceptible de se déconnecter du prix du sous-jacent.
**TRADEX-AI C2** : Garde-fou : ne jamais traiter ce signal comme primaire ; sa distance au prix impose une confirmation par un indicateur de prix pur.
*Catégorie : indicateurs_momentum*

---

### D1175 — Biais acheteur/vendeur par signe (positif/négatif)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_02) : L'indicateur sert à définir un biais général acheteur ou vendeur selon le signe. Un passage en territoire positif indique que l'ADL monte et que la pression acheteuse domine ; un passage en territoire négatif indique que l'ADL baisse et que la pression vendeuse domine. On peut anticiper ces croisements via les divergences haussières/baissières.
**TRADEX-AI C2** : Feature binaire de biais (signe de l'oscillateur) combinable avec la Direction Belkhayate comme filtre de cohérence flux.
*Catégorie : signal*

---

### D1176 — Lissage par allongement des moyennes (3,10) vs (6,20)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_03, image_04) : Les réglages par défaut (3,10) produisent souvent une ligne qui croise fréquemment le zéro. On peut lisser l'indicateur en allongeant les moyennes : l'exemple (6,20) double les deux moyennes pour conserver le ratio et lisser. Sur US Steel (X), le Chaikin Oscillator (6,20) a croisé la ligne zéro six fois en 12 mois, avec de bons signaux (vente d'avril, achat d'octobre) mais aussi de mauvais signaux / whipsaws. La clé est de confirmer les signaux avec d'autres aspects de l'analyse technique.
**TRADEX-AI C2** : Le couple (période rapide, lente) est un hyperparamètre de sensibilité ; conserver le ratio en le doublant. Whipsaws fréquents → confirmation obligatoire.
*Catégorie : signal*

---

### D1177 — Divergence haussière (définition + confirmation)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_05) : Une divergence haussière se forme quand le prix fait de nouveaux plus bas tandis que le Chaikin Oscillator forme un plus bas plus haut (higher low), traduisant une pression vendeuse moindre. Il est important d'attendre une confirmation (retournement de l'indicateur ou passage en territoire positif). Un passage en territoire positif montre un momentum haussier de l'ADL. Tant qu'il n'y a pas de croisement au-dessus de zéro, la pression vendeuse l'emporte malgré la divergence.
**TRADEX-AI C2** : Pattern divergence + condition de confirmation (cross > 0) codable en machine à états ; alerte précoce de retournement, pas signal exécutoire.
*Catégorie : divergence*

---

### D1178 — Divergence baissière (définition + confirmation)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_06) : Une divergence baissière se forme quand le prix fait un nouveau plus haut tandis que le Chaikin Oscillator ne confirme PAS ce plus haut (échoue à faire un higher high), reflétant une pression acheteuse réduite, ce qui peut parfois préfigurer un retournement baissier. La confirmation vient quand l'oscillateur passe en territoire négatif. Rappel : avec les réglages (3,10), il devient négatif quand l'EMA 3 jours de l'ADL passe sous l'EMA 10 jours.
**TRADEX-AI C2** : Symétrique de D1177 ; confirmation = passage sous zéro. Combinable avec la pression vendeuse ATAS.
*Catégorie : divergence*

---

### D1179 — Sensibilité des réglages (3,10) : beaucoup de divergences, distinguer robustes vs bogus
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_05) : Sur Fastenal (FAST) en 2010, cinq divergences apparaissent avec les réglages par défaut (3,10), qui produisent un oscillateur sensible générant de nombreuses divergences. La clé est de différencier les signaux robustes des signaux bidons en attendant confirmation. Sur Alcoa (AA), six croisements de la ligne zéro en 2010 : les cinq premiers n'ont pas donné de bons signaux, seul le sixième fut bon. Les cassures de lignes de tendance tracées sur l'oscillateur sont souvent plus précoces que les croisements de la ligne zéro ; une ligne de tendance capture aussi la direction (oscillateur montant = hausse régulière de la pression acheteuse, descendant = hausse de la pression vendeuse).
**TRADEX-AI C2** : Taux de faux signaux élevé en (3,10) → exiger confirmation ; trend lines sur l'oscillateur = signal plus précoce mais subjectif (non automatisable proprement).
*Catégorie : signal*

---

### D1180 — Synthèse opératoire (jamais en standalone)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md) : Le Chaikin Oscillator est un indicateur de momentum de l'ADL qui « turbo-charge » l'ADL en mesurant son momentum, rendant les signaux plus fréquents et plus quantifiables. En tant qu'oscillateur de flux monétaire, il peut être utilisé avec des oscillateurs de prix pur tels que MACD ou RSI. Comme tous les indicateurs, il ne doit PAS être utilisé seul (stand-alone).
**TRADEX-AI C2** : Règle architecturale : Chaikin Oscillator = couche de confirmation flux, jamais critère unique. Coupler à RSI/MACD (prix) côté C1.
*Catégorie : signal*

---

### D1181 — Placement et paramétrage SharpCharts
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md, image_07, image_08) : Le Chaikin Oscillator peut être positionné au-dessus, en dessous ou derrière le tracé du prix. Une fois choisi, le réglage par défaut (3,10) apparaît ; il est ajustable pour augmenter/diminuer la sensibilité. Les « advanced options » permettent d'ajouter une ligne horizontale ou une moyenne mobile.
**TRADEX-AI C2** : Détail outil StockCharts (UI) ; pas de paramètre nouveau pour le moteur, valeur de référence du défaut (3,10).
*Catégorie : configuration*

---

### D1182 — Scan « Chaikin Oscillator positif + RSI > 55 »
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md) : Scan d'upturn sur bon volume : le Chaikin Oscillator passe au-dessus de +1000 (juste au-dessus de sa ligne médiane 0), confirmé par RSI franchissant 55 (juste au-dessus de sa médiane 50). Base : actifs ≥ 10 $ et ≥ 100 000 de volume quotidien moyen sur 60 jours.
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily Chaikin Osc(3,10) crosses 1000]
AND [Daily RSI(14,Daily Close) crosses 55]
```
**TRADEX-AI C2** : La logique « Chaikin > seuil ET RSI > 55 » (double confirmation flux + prix) est transposable en condition Python ; le seuil +1000 est dépendant de l'échelle de l'ADL (donc du volume), à recalibrer par actif. Syntaxe de scan propre à StockCharts (non réutilisable telle quelle).
*Catégorie : signal*

---

### D1183 — Scan « Chaikin Oscillator négatif + RSI < 45 »
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md) : Scan de downturn sur bon volume : le Chaikin Oscillator passe sous -1000 (juste sous sa médiane 0), confirmé par RSI passant sous 45 (juste sous sa médiane 50). Même base de liquidité que D1182.
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [-1000 crosses Daily Chaikin Osc(3,10)]
AND [45 crosses Daily RSI(14,Daily Close)]
```
**TRADEX-AI C2** : Symétrique baissier de D1182 ; mêmes réserves (seuil -1000 dépendant de l'échelle volume, à recalibrer par actif).
*Catégorie : signal*

---

### D1184 — Garde-fou volume incomplet en intraday pour le scanning
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_oscillator.md) : Pour le scanning, les données de volume quotidiennes sont incomplètes pendant la séance. Avec les indicateurs basés sur le volume comme le Chaikin Oscillator, baser le scan sur la dernière clôture de marché (« Last Market Close »). Autres indicateurs volume concernés : Accumulation/Distribution, On Balance Volume, PVO.
**TRADEX-AI C2** : Garde-fou data : le volume intraday partiel fausse l'oscillateur ; cohérent avec la logique staleness_monitor (ne pas signaler sur volume non clos). À intégrer si calcul sur barres journalières.
*Catégorie : timing*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1171 | Nature et origine Chaikin Oscillator | 🔵 ÉCOLE | C2 | indicateurs_momentum |
| D1172 | Formule 4 étapes ADL → oscillateur | 🟢 | C2 | indicateurs_momentum |
| D1173 | Money Flow Multiplier / bascule signe | 🟢 | C2 | indicateurs_momentum |
| D1174 | 3e dérivée / risque déconnexion prix | 🟢 | C2 | indicateurs_momentum |
| D1175 | Biais acheteur/vendeur par signe | 🟢 | C2 | signal |
| D1176 | Lissage (3,10) vs (6,20) | 🟢 | C2 | signal |
| D1177 | Divergence haussière + confirmation | 🟢 | C2 | divergence |
| D1178 | Divergence baissière + confirmation | 🟢 | C2 | divergence |
| D1179 | Sensibilité (3,10) / trend lines | 🟢 | C2 | signal |
| D1180 | Synthèse — jamais standalone | 🟢 | C2 | signal |
| D1181 | Placement / paramétrage SharpCharts | 🟢 | C2 | configuration |
| D1182 | Scan Chaikin+ / RSI>55 | 🟢 | C2 | signal |
| D1183 | Scan Chaikin- / RSI<45 | 🟢 | C2 | signal |
| D1184 | Garde-fou volume intraday incomplet | 🟢 | C2 | timing |

**Liens Belkhayate :** le Chaikin Oscillator n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé par Belkhayate) : sa lecture de pression acheteuse/vendeuse via la position de clôture dans le range recoupe l'esprit de l'analyse de flux, mais la formule reste indépendante de la méthode. Ne rien inventer.

**À vérifier (humain) :**
- D1182 / D1183 — les seuils +1000 / -1000 dépendent de l'échelle de l'ADL (cumul de volume) et donc du volume absolu de chaque contrat ; ils NE sont PAS universels et doivent être recalibrés par actif (GC/HG/CL/ZW) avant tout codage. Source ne donne pas de seuil normalisé.
- D1184 — applicabilité au flux temps réel NT8/ATAS : la règle « Last Market Close » suppose des barres journalières ; à réévaluer si le moteur calcule l'oscillateur sur Range Bars intraday.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
