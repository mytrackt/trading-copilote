# Extraction StockCharts — On Balance Volume (OBV)
**Source :** `bundles/stockcharts/on_balance_volume_obv.md` (HTTP 200 · ~16 121 car.) + 12 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 12/12 certifiées
**Décisions :** D2791 → D2810 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/on-balance-volume-obv
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | On Balance Volume smoothed with a 20-day EMA | What Is On Balance Volume (OBV)? | CERTIFIE (accord .md + HTML) |
| image_02.png | On Balance Volume calculation example | Calculating OBV | CERTIFIE (accord .md + HTML) |
| image_03.png | On Balance Volume rises on up days and drops on down days | Calculating OBV | CERTIFIE (accord .md + HTML) |
| image_04.png | Bullish divergence with OBV | Divergences | CERTIFIE (accord .md + HTML) |
| image_05.png | Rising OBV during a trading range | Divergences | CERTIFIE (accord .md + HTML) |
| image_06.png | Bearish divergence with OBV | Divergences | CERTIFIE (accord .md + HTML) |
| image_07.png | Bearish divergence with OBV | Divergences | CERTIFIE (accord .md + HTML) |
| image_08.png | OBV confirming price trends | Trend Confirmation | CERTIFIE (accord .md + HTML) |
| image_09.png | OBV overlaid on price helps confirm price trend | Trend Confirmation | CERTIFIE (accord .md + HTML) |
| image_10.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_11.png | SharpCharts Settings for On Balance Volume | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_12.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2791 — Nature de l'OBV : pression acheteuse/vendeuse par volume cumulé
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_01) : L'On Balance Volume (OBV) évalue la pression acheteuse/vendeuse d'un actif en analysant le volume CUMULÉ. Il AJOUTE le volume les jours où le prix monte et le SOUSTRAIT les jours où le prix baisse.
**TRADEX-AI C2** : Indicateur de flux/volume cumulatif candidat comme couche de confirmation order flow (pression acheteuse/vendeuse).
*Catégorie : indicateurs_tendance*

---

### D2792 — Origine : Joe Granville (1963), précurseur du suivi des flux
🔵 **ÉCOLE (Granville)** (Source : on_balance_volume_obv.md) : L'OBV a été développé par Joe Granville, expliqué pour la première fois dans son livre de 1963 *Granville's New Key to Stock Market Profits*. C'est l'une des premières métriques à suivre les entrées/sorties de volume. En comparant l'OBV avec l'action des prix, on détecte des divergences pouvant préfigurer des mouvements futurs, ou on confirme des tendances existantes.
**TRADEX-AI C2** : Rationale historique ; deux usages canoniques — détection de divergences (anticipation) et confirmation de tendance.
*Catégorie : indicateurs_tendance*

---

### D2793 — Formule de calcul de la ligne OBV
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : L'OBV est un total cumulé de volume positif et négatif. Le volume d'une période est positif si la clôture est au-dessus de la clôture précédente, négatif si en dessous :
```
Si Close > Close précédent :  OBV courant = OBV précédent + Volume courant
Si Close < Close précédent :  OBV courant = OBV précédent - Volume courant
Si Close = Close précédent :  OBV courant = OBV précédent (inchangé)
```
**TRADEX-AI C2** : Formule déterministe implémentable telle quelle ; basée sur la clôture vs clôture précédente. Nécessite un flux volume fiable (NT8/ATAS) pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D2794 — Détail du tableur (multiplicateur +1/-1, total courant)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_02) : Dans le tableau, les volumes sont arrondis et exprimés en milliers (8200 = 8,2 M d'actions). On détermine d'abord si le titre a clôturé en hausse (+1) ou baisse (-1) ; ce nombre sert de multiplicateur du volume pour calculer le volume positif/négatif. La dernière colonne (OBV) forme le total courant. Comme l'OBV doit démarrer quelque part, la première valeur (8200) est simplement égale au volume positif/négatif de la première période.
**TRADEX-AI C2** : Confirme la mécanique du multiplicateur ±1 et la valeur de départ (1er volume signé) ; cas-test chiffré pour vérifier une implémentation.
*Catégorie : indicateurs_tendance*

---

### D2795 — L'échelle de l'OBV n'est pas pertinente
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_03) : L'échelle de l'OBV n'est PAS pertinente et n'est même pas affichée sur SharpCharts. Les chartistes regardent plutôt si la ligne OBV monte ou descend par rapport aux périodes précédentes.
**TRADEX-AI C2** : Garde-fou — seules la DIRECTION et la PENTE de l'OBV comptent, jamais sa valeur absolue. Normaliser/ignorer l'échelle dans le moteur.
*Catégorie : indicateurs_tendance*

---

### D2796 — Théorie de Granville : le volume précède le prix
🔵 **ÉCOLE (Granville)** (Source : on_balance_volume_obv.md) : Granville théorise que le volume PRÉCÈDE le prix. L'OBV monte quand le volume des jours haussiers surpasse celui des jours baissiers (pression de volume positive → prix plus hauts probables) et baisse quand le volume des jours baissiers domine. Attendre une hausse du prix si l'OBV monte alors que le prix est plat ou baisse ; attendre une baisse du prix si l'OBV baisse alors que le prix est plat ou monte.
**TRADEX-AI C2** : Principe directeur — l'OBV est un indicateur AVANCÉ (leading) du prix selon Granville ; base des signaux de divergence (D2798-D2801).
*Catégorie : indicateurs_tendance*

---

### D2797 — Méthode de lecture en 4 étapes (tendance, concordance, S/R, cassure)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : La valeur absolue n'importe pas ; se concentrer sur les caractéristiques de la ligne OBV. 1) Définir la tendance de l'OBV. 2) Déterminer si elle concorde avec celle du sous-jacent. 3) Chercher des niveaux de support/résistance. Une fois cassés, la tendance OBV change et ces cassures génèrent des signaux. L'OBV étant basé sur les clôtures, considérer les clôtures pour divergences ou cassures S/R. Les pics de volume peuvent fausser l'indicateur (mouvement brusque nécessitant une période de stabilisation).
**TRADEX-AI C2** : Procédure d'analyse codable en 4 features (tendance OBV, concordance prix/OBV, niveaux S/R sur OBV, cassures) ; garde-fou pics de volume.
*Catégorie : signal*

---

### D2798 — Définition des divergences OBV (haussière/baissière)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : Les divergences haussière et baissière anticipent un retournement, fondées sur « le volume précède le prix ». Divergence HAUSSIÈRE : l'OBV monte / forme un higher low alors que le prix baisse / forme un lower low. Divergence BAISSIÈRE : l'OBV baisse / forme un lower low alors que le prix monte / forme un higher high. La divergence OBV/prix alerte sur un retournement possible.
**TRADEX-AI C2** : Deux features de divergence directement codables (comparaison pentes/extrema OBV vs prix) ; signal d'alerte précoce.
*Catégorie : signal*

---

### D2799 — Exemple divergence haussière (SBUX) : volume précède le prix
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_04) : Sur Starbucks (SBUX), divergence haussière en juillet : le prix fait un lower low début juillet sous son low de juin, mais l'OBV tient au-dessus de son low de juin (higher low). L'OBV casse sa résistance AVANT que SBUX ne casse la sienne (cas classique de volume précédant le prix). SBUX casse une semaine plus tard puis gagne plus de 30%.
**TRADEX-AI C2** : Cas d'école « OBV casse avant le prix » → l'OBV peut servir de signal anticipateur de breakout prix.
*Catégorie : signal*

---

### D2800 — OBV montant en range = accumulation (haussier)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_05) : Sur Texas Instruments (TXN), l'OBV monte alors que le titre évolue en range (trading range). Un OBV montant durant un range indique de l'ACCUMULATION, ce qui est haussier.
**TRADEX-AI C2** : Feature « OBV haussier en phase de range » = signal d'accumulation/breakout haussier probable. Pertinent pour détecter la sortie de range sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D2801 — Exemples divergence baissière (MDT, VLO) + cassure de support
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_06, image_07) : Sur Medtronic (MDT), divergence baissière, volume entraînant le prix à la baisse : MDT monte (43→45) tandis que l'OBV baisse ET casse son support. L'uptrend de l'OBV s'inverse au passage sous le low de février ; MDT montait encore. Le volume l'emporte : MDT suit le volume à la baisse vers le bas des 30. Sur Valero Energy (VLO), OBV forme une divergence baissière en avril avec cassure de support confirmante en mai.
**TRADEX-AI C2** : Divergence baissière + cassure de support OBV = signal vendeur renforcé (double confirmation). La cassure de support sur l'OBV confirme la divergence.
*Catégorie : signal*

---

### D2802 — Confirmation de tendance (BBY : trends OBV ↔ prix concordants)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_08) : L'OBV confirme une tendance de prix, un breakout haussier ou une cassure baissière. Sur Best Buy (BBY), trois signaux confirmants : OBV et BBY baissent décembre-janvier, montent mars-avril, baissent mai-août, montent septembre-octobre. Les tendances de l'OBV correspondent à celles de BBY.
**TRADEX-AI C2** : Feature de concordance OBV/prix = confirmation de tendance (les deux dans le même sens). Renforce la confiance d'un signal directionnel.
*Catégorie : signal*

---

### D2803 — OBV confirme les retournements via cassures de trend lines
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : L'OBV confirme aussi les retournements de BBY : cassure de la downtrend line fin février confirmée par un breakout de résistance OBV en mars ; cassure de l'uptrend line fin avril confirmée par une cassure de support OBV début mai ; cassure de downtrend line début septembre confirmée par une cassure de trend line OBV une semaine plus tard. Ces signaux coïncidents indiquent que le volume positif/négatif est en harmonie avec le prix.
**TRADEX-AI C2** : Cassures de trend lines synchrones OBV+prix = confirmation forte de retournement. Tracer/détecter des trend lines sur la courbe OBV.
*Catégorie : signal*

---

### D2804 — OBV pas-à-pas avec le prix = confirmation de force (AZO)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_09) : Parfois l'OBV bouge pas-à-pas avec le sous-jacent, confirmant la force de la tendance sous-jacente (baisse ou hausse). Sur Autozone (AZO), prix (noir) et OBV (rose) montent régulièrement de novembre 2009 à octobre 2010 ; le volume positif reste fort tout au long de l'avance.
**TRADEX-AI C2** : OBV suivant pas-à-pas le prix = validation de la robustesse de tendance (pas de divergence latente). Feature de qualité de tendance.
*Catégorie : signal*

---

### D2805 — Synthèse : pression acheteuse/vendeuse, jamais standalone
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : L'OBV mesure la pression acheteuse/vendeuse via volume et prix. Pression acheteuse = volume positif > volume négatif → OBV monte ; pression vendeuse = volume négatif > positif → OBV baisse. Il sert à confirmer la tendance sous-jacente ou à repérer des divergences. Comme tous les indicateurs, NE PAS l'utiliser seul ; le combiner à d'autres aspects de l'AT, par exemple l'analyse de patterns ou la confirmation des oscillateurs de momentum.
**TRADEX-AI C2** : Règle architecturale — OBV = couche de confirmation flux (C2), jamais critère unique ; coupler à patterns/momentum (C1).
*Catégorie : signal*

---

### D2806 — Charting SharpCharts : positionnable, overlay possible
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_10) : Dans SharpCharts, l'OBV se positionne au-dessus, en dessous ou DERRIÈRE le tracé du prix. Le placer derrière facilite la comparaison OBV/sous-jacent. On peut ajouter une moyenne mobile ou un autre overlay à l'OBV via le réglage Overlay.
**TRADEX-AI C2** : Détail outil (UI) ; idée exploitable — superposer une MA sur l'OBV pour générer des croisements (cf. scans D2808-D2809 qui utilisent OBV Signal).
*Catégorie : configuration*

---

### D2807 — StockChartsACP : ajout via Chart Settings, sans paramètres
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md, image_11, image_12) : Dans StockChartsACP, l'OBV s'ajoute depuis le panneau Chart Settings, positionnable au-dessus, en dessous ou derrière le prix. L'indicateur n'a AUCUN paramètre, mais le panneau de réglages permet de changer le style de ligne ou d'ajouter un overlay à l'indicateur.
**TRADEX-AI C2** : Détail outil (UI) ; confirme que l'OBV brut est sans paramètre (à la différence du NVI dont l'EMA est paramétrable).
*Catégorie : configuration*

---

### D2808 — Scan : divergence haussière OBV + ADL (sous SMA prix)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : Scan de divergences haussières potentielles : base d'actions ≥ 10$ et ≥ 100 000 volume quotidien sur 60 jours ; prix SOUS ses SMA 65 et 20 jours, mais OBV et Accumulation Distribution Line AU-DESSUS de leurs signaux 65 et 20 :
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily Close < Daily SMA(65,Daily Close)]
AND [Daily AccDist > Daily AccDist Signal (65)]
AND [Daily OBV > Daily OBV Signal(65)]
AND [Daily Close < Daily SMA(20,Daily Close)]
AND [Daily AccDist > Daily AccDist Signal (20)]
AND [Daily OBV > Daily OBV Signal(20)]
```
**TRADEX-AI C2** : Logique « prix faible MAIS OBV+ADL forts » (double confirmation flux) = divergence haussière ; transposable en condition Python, syntaxe de scan propre à StockCharts.
*Catégorie : signal*

---

### D2809 — Scan : divergence baissière OBV + ADL (au-dessus SMA prix)
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : Scan symétrique baissier : prix AU-DESSUS de ses SMA 65 et 20, mais OBV et ADL EN DESSOUS de leurs signaux 65 et 20. Même base de liquidité que D2808.
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily Close > Daily SMA(65,Daily Close)]
AND [Daily AccDist < Daily AccDist Signal (65)]
AND [Daily OBV < Daily OBV Signal(65)]
AND [Daily Close > Daily SMA(20,Daily Close)]
AND [Daily AccDist < Daily AccDist Signal (20)]
AND [Daily OBV < Daily OBV Signal(20)]
```
**TRADEX-AI C2** : Symétrique baissier de D2808 ; combine deux indicateurs flux (OBV + ADL) pour fiabiliser la divergence.
*Catégorie : signal*

---

### D2810 — Garde-fou : volume intraday incomplet pour le scanning
🟢 **FAIT VÉRIFIÉ** (Source : on_balance_volume_obv.md) : Pour le scanning, les données de volume quotidiennes sont incomplètes en séance. Avec les indicateurs volume comme l'OBV, baser le scan sur la dernière clôture de marché (« Last Market Close »). Autres indicateurs volume concernés : Accumulation/Distribution, Chaikin Money Flow, PVO.
**TRADEX-AI C2** : Garde-fou data cohérent avec staleness_monitor — ne pas signaler sur volume non clos. À intégrer si calcul sur barres journalières.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2791 | Nature OBV (volume cumulé) | 🟢 | C2 | indicateurs_tendance |
| D2792 | Origine Granville (1963) | 🔵 ÉCOLE | C2 | indicateurs_tendance |
| D2793 | Formule de calcul | 🟢 | C2 | indicateurs_tendance |
| D2794 | Détail tableur (±1, départ) | 🟢 | C2 | indicateurs_tendance |
| D2795 | Échelle non pertinente | 🟢 | C2 | indicateurs_tendance |
| D2796 | Volume précède le prix | 🔵 ÉCOLE | C2 | indicateurs_tendance |
| D2797 | Lecture 4 étapes | 🟢 | C2 | signal |
| D2798 | Définition divergences | 🟢 | C2 | signal |
| D2799 | Divergence haussière SBUX | 🟢 | C2 | signal |
| D2800 | OBV montant en range = accumulation | 🟢 | C2 | signal |
| D2801 | Divergence baissière + cassure support | 🟢 | C2 | signal |
| D2802 | Confirmation de tendance BBY | 🟢 | C2 | signal |
| D2803 | Cassures trend lines synchrones | 🟢 | C2 | signal |
| D2804 | OBV pas-à-pas = force tendance | 🟢 | C2 | signal |
| D2805 | Synthèse — jamais standalone | 🟢 | C2 | signal |
| D2806 | Charting SharpCharts | 🟢 | C2 | configuration |
| D2807 | StockChartsACP (sans paramètre) | 🟢 | C2 | configuration |
| D2808 | Scan divergence haussière OBV+ADL | 🟢 | C2 | signal |
| D2809 | Scan divergence baissière OBV+ADL | 🟢 | C2 | signal |
| D2810 | Garde-fou volume intraday incomplet | 🟢 | C2 | gestion_risque_entree |

**Liens Belkhayate :** l'On Balance Volume n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé) : l'OBV est un indicateur de flux/volume (pression acheteuse/vendeuse) dont l'esprit recoupe la notion d'« Énergie » Belkhayate ; or la mémoire projet établit que l'Énergie Belkhayate = MFI standard (Money Flow Index, seuils 20/80), un indicateur DIFFÉRENT de l'OBV (l'OBV est un cumul de volume signé non borné ; le MFI est un oscillateur borné 0-100 intégrant le prix typique). Ne PAS assimiler OBV et MFI. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D2793 / D2808 / D2809 — formule et scans calibrés sur actions liquides US ; à revalider (walk-forward) sur les futures GC/HG/CL/ZW (microstructure volume différente, séances et roll des contrats).
- D2795 — l'échelle de l'OBV dépend du point de départ arbitraire ; normaliser (pente/direction) avant toute comparaison inter-actifs.
- D2796 / D2798 — l'hypothèse « volume précède le prix » et les divergences sont des signaux AVANCÉS donc faillibles : exiger une confirmation (cassure S/R OBV, cf. D2801/D2803) avant exploitation.
- D2810 — interdiction de signaler sur volume non clos : aligner avec staleness_monitor pour les calculs sur barres journalières.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
