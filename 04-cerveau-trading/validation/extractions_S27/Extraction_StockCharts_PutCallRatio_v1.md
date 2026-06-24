# Extraction StockCharts — Put/Call Ratio
**Source :** `bundles/stockcharts/put_call_ratio.md` (HTTP 200) + 8 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 8/8 certifiées · 0 à vérifier
**Décisions :** D259 → D270 · **Page :** chartschool.stockcharts.com/.../market-indicators/put-call-ratio
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : le Put/Call Ratio est un indicateur de **SENTIMENT contrarien** → cercle **C5 (sentiment)**, au même rang que le VIX. Il alimente la couche CONFIRMATION (ES·DX·VX), JAMAIS un ordre direct sur GC/HG/CL/ZW. Aucun lien Belkhayate affirmé par la source ; tout rattachement Énergie/pivots serait une hypothèse projet (signalée ⚫🔴 le cas échéant). Page PRIORITAIRE (sentiment C5).

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | Index, Equity, or Total [section-fallback] | Index, Equity, or Total ($CPCI 200j) | D262 |
| image_02 | Index, Equity, or Total [section-fallback] | Index, Equity, or Total ($CPCE 200j) | D262 |
| image_03 | Index, Equity, or Total [section-fallback] | Index, Equity, or Total ($CPC 200j) | D262 |
| image_04 | Spike Extremes [section-fallback] | Spike Extremes | D264 |
| image_05 | Smoothing the Ratio [section-fallback] | Smoothing the Ratio | D266 |
| image_06 | Shifting Ranges [section-fallback] | Shifting Ranges | D267 |
| image_07 | Put/Call Ratio on StockCharts.com [section-fallback] | SharpCharts (chart) | D269 |
| image_08 | Put/Call Ratio on StockCharts.com [section-fallback] | SharpCharts (settings) | D269 |

---

## DÉCISIONS

### D259 — Put/Call Ratio : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Le Put/Call Ratio est un indicateur qui montre le **volume de puts relatif au volume de calls**. Les puts servent à se couvrir contre la faiblesse du marché ou à parier sur une baisse ; les calls servent à se couvrir contre la force du marché ou à parier sur une hausse. Le ratio est **au-dessus de 1** quand le volume de puts dépasse celui des calls, **en dessous de 1** quand le volume de calls dépasse celui des puts.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Il est typiquement utilisé pour **jauger le sentiment de marché** — sentiment jugé excessivement baissier quand le ratio est à des niveaux relativement hauts, excessivement haussier quand il est à des niveaux relativement bas.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : `Put/Call Ratio = Put Volume / Call Volume` (calcul direct et simple).
**TRADEX-AI C5** : Brique sentiment macro — proxy de peur/avidité des options, à ranger aux côtés du VIX dans la couche CONFIRMATION (VX), jamais comme ordre direct.
*Catégorie : indicateurs_momentum*

---

### D260 — Indicateur CONTRARIEN (cœur de l'interprétation)
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Comme la plupart des indicateurs de sentiment, le Put/Call Ratio s'utilise en **contrarien** pour repérer les extrêmes haussiers et baissiers. Les contrariens deviennent baissiers quand trop de traders sont haussiers, et haussiers quand trop de traders sont baissiers.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Ratio aux **bas extrêmes** = haussiers excessifs (volume calls >> puts) → en termes contrariens, prudence et possibilité de déclin du marché. Ratio aux **hauts extrêmes** = baissiers excessifs (volume puts >> calls) → optimisme et possibilité de retournement haussier.
**TRADEX-AI C5** : Logique d'inversion à coder explicitement — un Put/Call élevé est un signal de biais HAUSSIER (et inversement) ; ne jamais lire le ratio « dans le sens » du volume dominant.
*Catégorie : structure_marche*

---

### D261 — Source de données : Cboe (Cboe = référence)
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : StockCharts fournit les Put/Call Ratios du **Chicago Board Options Exchange (Cboe)**, la plus grande bourse d'options ; ses statistiques sont les plus suivies. Le Cboe découpe en trois groupes : **equity** (`$CPCE`, options sur actions individuelles), **index** (`$CPCI`, indices majeurs : Dow, Nasdaq, Russell 2000, S&P 500, S&P 100) et **total** (`$CPC`, equity + index combinés).
**TRADEX-AI C5** : Source de données = tickers Cboe `$CPC`/`$CPCE`/`$CPCI` (donnée externe macro, hors NT8/ATAS) ; intégrer comme flux CONFIRMATION (sentiment), pas comme prix tradable.
*Catégorie : structure_marche*

---

### D262 — Index vs Equity vs Total : biais structurels distincts
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md, image_01, image_02, image_03) : Les options **index** sont associées aux pros, les options **equity** aux non-pros. Le `$CPCI` (index) reste **constamment au-dessus de 1** (SMA 200 jours à **1,41**) → biais vers les puts (couverture). Le `$CPCE` (equity) reste largement **sous 1** (SMA 200j à **0,61**) → biais vers les calls (non-pros plus haussiers). Le `$CPC` (total) oscille autour de 1 (SMA 200j à **0,91**) → léger biais calls, le biais put de l'index étant compensé par le biais call de l'equity.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Equity = sentiment retail, index = sentiment pro ; la combinaison (`$CPC` total) reflète le sentiment « marché » global. L'article se concentre sur le **Total ($CPC)** comme bon agrégat, en recommandant de regarder les trois.
**TRADEX-AI C5** : Ne jamais comparer un Put/Call à un seuil absolu universel — chaque variante a sa ligne de base (1,41 / 0,61 / 0,91). Privilégier `$CPC` total comme jauge marché, mais conserver les trois pour nuancer pro vs retail.
*Catégorie : structure_marche*

---

### D263 — Les extrêmes ne sont PAS fixes (seuils relatifs)
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Le sentiment atteint des extrêmes quand le ratio bouge vers des niveaux relativement hauts ou bas. **Ces extrêmes ne sont pas fixes et peuvent changer dans le temps.**
🟡 **CONVENTION** : Les seuils d'extrême doivent être recalibrés périodiquement (référence mobile type SMA 200j), pas figés en dur.
**TRADEX-AI C5** : Garde anti-faux-signal — paramétrer les seuils Put/Call relativement à une moyenne longue glissante par actif/variante, et les ré-évaluer ; un seuil codé en dur dérive.
*Catégorie : gestion_risque_entree*

---

### D264 — Spikes extrêmes sur le ratio brut : seuils 1,20 / 0,70
🔵 **ÉCOLE** (Source : put_call_ratio.md, image_04) : Sur le Total ($CPC) brut, un **spike au-dessus de 1,20** reflète une poussée de puts (baissier excessif → lecture contrarienne HAUSSIÈRE) ; un **spike sous 0,70** reflète une poussée de calls (haussier excessif → lecture contrarienne BAISSIÈRE).
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Les spikes au-dessus de 1,20 ont identifié des creux exploitables (fin octobre, début février), MAIS certains extrêmes (mai, juin) n'ont produit que des rebonds peu profonds ou un trading plat avant que le marché continue de baisser. Côté calls, le signal d'octobre a bien fonctionné, celui de décembre était trop tôt, celui d'avril a bien fonctionné.
**TRADEX-AI C5** : Seuils de spike sur ratio brut = 1,20 (plancher contrarien haussier) / 0,70 (plafond contrarien baissier). À traiter en confirmation/score, jamais en entrée isolée (taux d'échec et « trop tôt » documentés par la source elle-même).
*Catégorie : signal*

---

### D265 — Un extrême seul ne suffit pas : attendre que l'extrême soit ATTEINT
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Ces signaux contrariens peuvent parfois piquer les sommets et les creux, mais parfois ils seront **trop tôt ou simplement faux** — « les indicateurs ne sont pas parfaits ». Il est important d'**identifier les extrêmes et d'attendre qu'un extrême soit atteint** ; la plupart du temps le ratio fluctue entre ces extrêmes.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Important d'utiliser le Put/Call **conjointement avec d'autres indicateurs** (oscillateurs de momentum, chart patterns) pour confirmer les signaux ; attendre un peu de confirmation filtre souvent les mauvais signaux.
**TRADEX-AI C5** : Guard permanent — ne déclencher aucune pondération sentiment tant qu'un seuil d'extrême n'est pas réellement atteint ; exiger confirmation multi-outil (momentum, pattern, structure) avant tout impact sur le score.
*Catégorie : gestion_risque_entree*

---

### D266 — Lissage par SMA 10 jours : seuils déplacés 0,95 / 0,80 + confirmation
🔵 **ÉCOLE** (Source : put_call_ratio.md, image_05) : Le Total ($CPC) brut étant très bruité, une **SMA 10 jours** lisse les données et définit des tendances (moins de volatilité, peut tendre dans une direction plusieurs semaines, mais introduit un **lag**). Comme la volatilité baisse, **les seuils de spike sont abaissés**.
🔵 **ÉCOLE** (Source : put_call_ratio.md) : Sur la SMA 10j — **signal haussier** = le ratio passe AU-DESSUS de l'extrême baissier (0,95) PUIS revient en dessous ; **signal baissier** = le ratio passe SOUS l'extrême haussier (0,80) PUIS revient au-dessus.
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : Comme cette moyenne peut tendre longtemps, il faut **attendre la confirmation** (retour au-dessus/en dessous du seuil). Attendre cette confirmation aurait évité une position longue prématurée en mai (le ratio a continué de monter et est resté élevé longtemps).
**TRADEX-AI C5** : Variante lissée — SMA 10j avec seuils 0,95 (baissier) / 0,80 (haussier) ET règle de **cassure-puis-retour** obligatoire. Modéliser le lag : signal lissé = plus fiable mais plus tardif.
*Catégorie : signal*

---

### D267 — Plages mobiles : la SMA dérive avec le régime de marché
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md, image_06) : Selon les conditions, les plages du Total ($CPC) **se déplacent dans le temps**. Exemple : SMA 10j et 50j oscillant autour de 1,00 d'avril 2007 à début 2009 (marché plat puis déclin prolongé, niveaux élevés = biais puts) ; au retournement de mars 2009, le ratio est passé dans une plage plus basse centrée autour de **0,85** (biais calls) jusqu'à avril 2010, puis a repassé au-dessus de 1,00.
**TRADEX-AI C4/C5** : Le centre de gravité du Put/Call est fonction du **régime de marché** (bull/bear). Croiser la lecture sentiment avec le régime macro (C4) ; un même niveau brut n'a pas le même sens en bull qu'en bear.
*Catégorie : structure_marche*

---

### D268 — Conclusion : signaux à contre-tendance, imparfaits, jamais seuls
🟢 **FAIT VÉRIFIÉ** (Source : put_call_ratio.md) : En tant qu'indicateur de sentiment contrarien, les signaux du Put/Call seront souvent **à l'opposé de la tendance dominante** (le volume de calls augmente quand un rallye s'installe, le volume de puts pendant un déclin prolongé). À un extrême, les opérateurs d'options sont soit excessivement haussiers soit excessivement baissiers ; ces signaux contrariens peuvent piquer tops/bottoms mais sont parfois trop tôt ou faux.
**TRADEX-AI C5** : Synthèse opérationnelle — utiliser le Put/Call comme **modulateur de confiance** (sentiment de foule à contre-pied), pondéré faible, et toujours subordonné à price action/structure sur GC/HG/CL/ZW. Jamais déclencheur d'entrée autonome.
*Catégorie : gestion_risque_entree*

---

### D269 — Implémentation / paramétrage SharpCharts (référence)
🔵 **ÉCOLE** (Source : put_call_ratio.md, image_07, image_08) : Le Put/Call peut être tracé de plusieurs façons dans SharpCharts (fenêtre principale ou au-dessus/dessous). Exemple : `$CPC` total (gris) en fenêtre principale avec **SMA 10 jours** (noir) pour lissage ; type « Invisible » pour masquer les valeurs quotidiennes et focaliser sur la version lissée ; lignes horizontales en « Overlays » ; un indice correspondant en « Indicator » pour comparer le ratio aux mouvements de l'indice.
**TRADEX-AI C0** : Référence de paramétrage UI/config — exposer `$CPC` brut + SMA 10j superposée, seuils horizontaux paramétrables, et comparaison à un indice de confirmation (ES).
*Catégorie : signal*

---

### D270 — Rattachement Belkhayate : aucun lien affirmé par la source
⚫🔴 **PROPRIÉTAIRE / NON VÉRIFIÉ (rattachement TRADEX-AI)** : Le Put/Call Ratio est un indicateur de sentiment options externe ; **la source n'établit aucun lien avec la méthode Belkhayate** (ni Énergie/MFI, ni pivots, ni BGC). Tout usage comme proxy d'« Énergie » ou de sentiment Belkhayate serait une **hypothèse projet, non affirmée par la source**.
**TRADEX-AI C5** : Brancher le Put/Call uniquement dans la couche CONFIRMATION (sentiment, aux côtés de VX), en entrée du score /10 ; ne JAMAIS le présenter comme composante de la méthode Belkhayate.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D259 → D270 (12) |
| Images certifiées citées | 8/8 |
| Catégories utilisées | structure_marche · signal · gestion_risque_entree · indicateurs_momentum |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · ⚫🔴 (rattachement Belkhayate) |
| Cercle dominant | **C5 (sentiment)** — couche CONFIRMATION (VX), jamais ordre direct GC/HG/CL/ZW |
| Belkhayate | **NON CONCERNÉ** — aucun lien affirmé par la source ; rattachement éventuel = hypothèse projet (D270) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
