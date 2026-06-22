# Extraction StockCharts — RSI (Relative Strength Index)
**Source :** `bundles/stockcharts/rsi.md` (HTTP 200 · 22 157 car.) + 15 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende locale) · 15/15 certifiées
**Décisions :** D18 → D39 · **Page :** chartschool.stockcharts.com/.../relative-strength-index-rsi

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | RS vs. RSI Plots | RSI Calculation | D19 |
| image_02 | RSI Calculation Example | RSI Calculation | D19 |
| image_03 | Overbought and Oversold RSI | OB/OS Levels | D21 |
| image_04 | Overbought/Oversold RSI in a Trading Range | OB/OS Levels | D22 |
| image_05 | RSI Divergences | Divergences | D24 |
| image_06 | RSI Divergences in a strong trend | Divergences | D26 |
| image_07 | Bullish RSI Failure Swing | Failure Swings | D27 |
| image_08 | Bearish RSI Failure Swing | Failure Swings | D28 |
| image_09 | Using RSI to identify an uptrend | Identify Trends | D29 |
| image_10 | Using RSI to identify a downtrend | Identify Trends | D30 |
| image_11 | Identifying a positive reversal with RSI | Reversals | D32 |
| image_12 | Identifying a negative reversal with RSI | Reversals | D33 |
| image_13 | Using RSI on a SharpChart | SharpCharts | D38 |
| image_14 | RSI Settings on the SharpCharts Workbench | SharpCharts | D38 |
| image_15 | Using RSI on an ACP chart | StockChartsACP | D38 |

---

## DÉCISIONS

### D18 — RSI : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Le RSI est un oscillateur de momentum développé par J. Welles Wilder ; il mesure la vitesse et l'ampleur des mouvements de prix et oscille entre 0 et 100.
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Wilder présente le RSI dans son livre de 1978 *New Concepts in Technical Trading Systems* (même ouvrage que Parabolic SAR, ATR et ADX).
**TRADEX-AI C0** : RSI fait partie des indicateurs exportés depuis NinjaScript (OHLCV, COG, ADX, MA, EMA, RSI, MACD) pour NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D19 — RSI : formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md, image_01, image_02) : Trois composants — RS, Average Gain, Average Loss. Formule : `RSI = 100 − [100 / (1 + RS)]` avec `RS = Average Gain / Average Loss`. Les pertes sont exprimées en valeurs positives.
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Premier calcul = moyennes simples sur 14 périodes ; calculs suivants = lissage `[(moyenne précédente × 13) + valeur courante] / 14` (technique proche d'une EMA).
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : RSI = 0 si Average Gain = 0 (14 périodes baissières) ; RSI = 100 si Average Loss = 0 (14 périodes haussières).
**TRADEX-AI C0** : Formule à répliquer côté export NinjaScript ; prévoir ≥ 250 points de données amont pour des valeurs stabilisées (cf. D20).
*Catégorie : indicateurs_momentum*

---

### D20 — RSI : profondeur de calcul et lissage
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : SharpCharts utilise au moins 250 points de données avant la date de début du graphique ; une formule a besoin d'au moins 250 points pour répliquer ces valeurs.
🔵 **ÉCOLE** (Source : rsi.md) : Le lissage fait que les valeurs RSI varient selon la période totale de calcul (250 périodes lissent davantage que 30).
**TRADEX-AI C1** : Pré-filtrage Python — toujours alimenter le calcul RSI avec un historique suffisant (≥ 250 barres) avant d'émettre un signal sur NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D21 — Surachat / survente : seuils de Wilder
🔵 **ÉCOLE** (Source : rsi.md, image_03) : Wilder considère le RSI en surachat au-dessus de 70 et en survente en dessous de 30 (exemple McDonald's, RSI 14 jours).
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md, image_03) : Un creux peut « évoluer » après une lecture de survente — le bas ne se forme pas forcément dès la première lecture de survente.
🟡 **CONVENTION** : Seuils ajustables — relever à 80 / abaisser à 20 réduit le nombre de lectures extrêmes ; le RSI 2 périodes sert au surachat > 80 / survente < 20 (court terme).
**TRADEX-AI C3** : Confirmation multi-indicateur — une lecture RSI > 70 ou < 30 sur NQ/ES/Gold est un signal de momentum, jamais une entrée seule (cf. D37).
*Catégorie : indicateurs_momentum*

---

### D22 — Surachat / survente : meilleur en range
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md, image_04) : Les lectures de surachat/survente du RSI fonctionnent le mieux quand le prix évolue latéralement dans un range (exemple MEMC Electronics / WFR, range 13,5–21).
🟡 **CONVENTION** : Filtrer les signaux OB/OS par le régime de marché (range vs tendance).
**TRADEX-AI C1** : Pré-filtrage — n'activer les signaux OB/OS purs que si le marché est identifié en range (sinon risque de faux signaux, cf. D23).
*Catégorie : structure_marche*

---

### D23 — Piège du momentum en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Un oscillateur de momentum peut devenir et rester en surachat (survente) durant une tendance haussière (baissière) forte ; les premières lectures de surachat ont précédé de simples consolidations, pas un retournement.
**TRADEX-AI C2/C3** : En tendance directionnelle forte sur NQ/ES/Gold, ne pas traiter un RSI > 70 comme un signal de vente — exiger une confirmation de structure/price action.
*Catégorie : indicateurs_momentum*

---

### D24 — Divergence baissière / haussière (Wilder)
🔵 **ÉCOLE** (Source : rsi.md, image_05) : Selon Wilder, une divergence signale un retournement potentiel. Divergence haussière = le titre fait un plus bas plus bas mais le RSI fait un plus bas plus haut. Divergence baissière = le titre fait un plus haut plus haut mais le RSI fait un plus haut plus bas (exemple eBay).
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Les divergences sont plus robustes lorsqu'elles se forment après une lecture de surachat ou de survente.
**TRADEX-AI C3** : Détecter les divergences RSI/prix sur NQ/ES/Gold comme signal de confirmation de retournement, priorisé après un extrême OB/OS.
*Catégorie : indicateurs_momentum*

---

### D25 — Divergence : confirmation par cassure
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Dans l'exemple eBay, la cassure (breakdown mi-octobre / breakout mi-mars) a confirmé le changement de momentum après la divergence.
🟡 **CONVENTION** : Une divergence n'est exploitable qu'après confirmation par cassure de prix.
**TRADEX-AI C3/C4** : N'émettre le signal de divergence qu'après cassure confirmée du niveau d'ancrage (résistance/support) sur NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D26 — Divergences trompeuses en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md, image_06) : Les divergences sont trompeuses en tendance forte ; une forte tendance haussière peut afficher de nombreuses divergences baissières avant qu'un sommet ne se matérialise (exemple SPY, trois divergences baissières et tendance haussière continue).
**TRADEX-AI C2/C3** : Désactiver / dégrader le poids des divergences baissières quand NQ/ES/Gold est en tendance haussière forte confirmée.
*Catégorie : indicateurs_momentum*

---

### D27 — Bullish Failure Swing (Wilder)
🔵 **ÉCOLE** (Source : rsi.md, image_07) : Un failure swing haussier se forme quand le RSI passe sous 30 (survente), rebondit au-dessus de 30, recule, tient au-dessus de 30, puis casse son plus haut précédent (exemple RIMM, RSI 10 jours). Indépendant du prix, basé uniquement sur le RSI.
**TRADEX-AI C3** : Détecter le failure swing haussier comme signal de retournement RSI-only sur NQ/ES/Gold, distinct de la divergence.
*Catégorie : indicateurs_momentum*

---

### D28 — Bearish Failure Swing (Wilder)
🔵 **ÉCOLE** (Source : rsi.md, image_08) : Un failure swing baissier se forme quand le RSI passe au-dessus de 70, recule, rebondit sans dépasser 70, puis casse son plus bas précédent (exemple Texas Instruments / TXN, mai–juin 2008).
**TRADEX-AI C3** : Détecter le failure swing baissier comme signal de retournement RSI-only sur NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D29 — Bull market range du RSI (Brown)
🔵 **ÉCOLE** (Source : rsi.md, image_09) : Constance Brown (*Technical Analysis for the Trading Professional*) : en marché haussier, le RSI fluctue entre 40 et 90, la zone 40–50 agissant comme support (exemple SPY 2003–2007, RSI 14 semaines).
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Ces plages varient selon les paramètres RSI, la force de la tendance et la volatilité du sous-jacent.
**TRADEX-AI C2/C3** : Utiliser le maintien du RSI dans 40–90 comme confirmation de régime haussier sur NQ/ES.
*Catégorie : indicateurs_tendance*

---

### D30 — Bear market range du RSI (Brown)
🔵 **ÉCOLE** (Source : rsi.md, image_10) : En marché baissier, le RSI fluctue entre 10 et 60, la zone 50–60 agissant comme résistance (exemple US Dollar Index $USD, tendance baissière 2009).
**TRADEX-AI C2/C3** : Utiliser le plafonnement du RSI sous 60 comme confirmation de régime baissier sur NQ/ES/Gold.
*Catégorie : indicateurs_tendance*

---

### D31 — Zone 40–50 : entrée à faible risque (bull)
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Dans l'exemple SPY, les pullbacks vers la zone 40–50 ont fourni des points d'entrée à faible risque pour participer à la tendance haussière (zone tenue au moins cinq fois de janv. 2005 à oct. 2007).
**TRADEX-AI C3** : En régime haussier confirmé sur NQ/ES, un pullback RSI vers 40–50 est un emplacement d'entrée long candidat (à confirmer par price action).
*Catégorie : gestion_risque_entree*

---

### D32 — Positive Reversal (Cardwell)
🔵 **ÉCOLE** (Source : rsi.md, image_11) : Andrew Cardwell — un positive reversal se forme quand le RSI fait un plus bas plus bas tandis que le titre fait un plus bas plus haut, ce plus bas n'étant pas en survente mais généralement entre 30 et 50 (exemple MMM, juin 2009). Le price action prime sur le momentum.
**TRADEX-AI C3** : Détecter le positive reversal comme signal haussier où le prix surpasse le momentum sur NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D33 — Negative Reversal (Cardwell)
🔵 **ÉCOLE** (Source : rsi.md, image_12) : Un negative reversal (inverse du positive) — le RSI fait un plus haut plus haut tandis que le titre fait un plus haut plus bas, généralement dans la zone 50–70 (exemple Starbucks / SBUX). A précédé une cassure de support et un fort déclin.
**TRADEX-AI C3** : Détecter le negative reversal comme signal baissier où le prix échoue à confirmer le momentum.
*Catégorie : indicateurs_momentum*

---

### D34 — Réinterprétation Cardwell des divergences
🔵 **ÉCOLE** (Source : rsi.md) : Cardwell considère les divergences baissières comme un phénomène de marché haussier (plus probables en tendance haussière) et les divergences haussières comme un phénomène de marché baissier.
**TRADEX-AI C2/C3** : Pondérer l'interprétation des divergences par le régime de marché (selon le cadre Cardwell) plutôt que de les traiter comme signaux de retournement isolés.
*Catégorie : indicateurs_momentum*

---

### D35 — Priorité au price action sur le momentum
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : La conclusion de l'article place le price action du sous-jacent en premier et l'indicateur en second (logique des positive/negative reversals), par opposition aux divergences qui placent l'indicateur en premier.
**TRADEX-AI C3/C4** : Hiérarchie de décision — price action > signal RSI lors d'un conflit, sur NQ/ES/Gold.
*Catégorie : indicateurs_momentum*

---

### D36 — RSI multi-temporalité
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Le RSI peut être appliqué à de nombreuses temporalités — journalier, hebdomadaire, horaire, minute ; la meilleure dépend de la stratégie et des objectifs.
**TRADEX-AI C3** : Calculer le RSI sur plusieurs temporalités (ex. confirmation H1 + Daily) pour les signaux NQ/ES/Gold.
*Catégorie : timing*

---

### D37 — Confirmation obligatoire du RSI
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Comme tout indicateur technique, le RSI doit être utilisé avec d'autres outils et indicateurs pour confirmer les signaux et éviter les faux signaux.
🟡 **CONVENTION** : Aucun signal RSI seul n'est une entrée valide.
**TRADEX-AI C3** : Guard permanent — un signal RSI sur NQ/ES/Gold exige une confirmation multi-indicateur (MACD, volume) et un ancrage price action avant toute décision.
*Catégorie : gestion_risque_entree*

---

### D38 — Implémentation RSI sur plateforme (référence)
🔵 **ÉCOLE** (Source : rsi.md, image_13, image_14, image_15) : RSI disponible dans SharpCharts (dropdown Indicator, paramètre, position above/below/behind) et dans StockChartsACP (Chart Settings) ; paramètre par défaut = 14 périodes, ajustable.
**TRADEX-AI C0** : Référence d'implémentation/paramétrage ; aligner le calcul RSI exporté sur le défaut 14 périodes documenté.
*Catégorie : indicateurs_momentum*

---

### D39 — Scans RSI officiels StockCharts
🟢 **FAIT VÉRIFIÉ** (Source : rsi.md) : Scan « RSI Oversold in Uptrend » = clôture > SMA200 ET `RSI(5) <= 30`. Scan « RSI Overbought in Downtrend » = clôture < SMA200 ET `RSI(5) >= 70`.
**TRADEX-AI C1** : Transposer ces deux règles de pré-filtrage (tendance via SMA200 + RSI court 5 périodes) en filtres Python pour NQ/ES/Gold.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D18 → D39 (22) |
| Images certifiées citées | 15/15 |
| Catégories utilisées | indicateurs_momentum · indicateurs_tendance · structure_marche · timing · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Belkhayate | non concerné (page RSI) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
