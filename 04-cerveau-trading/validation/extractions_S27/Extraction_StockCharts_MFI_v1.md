# Extraction StockCharts — Money Flow Index (MFI)
**Source :** `bundles/stockcharts/money_flow_index_mfi.md` (HTTP 200 · 15 701 car.) + 8 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende locale) · 8/8 certifiées · 0 à vérifier
**Décisions :** D177 → D188 · **Page :** chartschool.stockcharts.com/.../technical-indicators/money-flow-index-mfi
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : le MFI est le candidat #1 pour l'**Énergie Belkhayate** (mémoire projet : Énergie = MFI standard, seuils 20/80). L'équivalence MFI↔Énergie reste une **hypothèse projet NON affirmée par la source** (cf. arbitrage Énergie 13/06, conflit MFI vs proxy ATR non tranché). Les faits MFI ci-dessous sont 🟢 ; le rattachement Énergie est signalé ⚫🔴.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | What Is the MFI? (section-fallback) | What Is the MFI? | D177 |
| image_02 | Money Flow Index - Spreadsheet | Calculating the MFI | D178 |
| image_03 | Money Flow Index at extreme oversold levels | Overbought/Oversold Levels | D181 |
| image_04 | Money Flow Index at extreme overbought levels | Overbought/Oversold Levels | D181 |
| image_05 | Failure swings and divergences with the MFI | Divergences and Failure Swings | D185 |
| image_06 | Using MFI on a SharpChart | Using with SharpCharts | D187 |
| image_07 | MFI settings on the SharpCharts Workbench | Using with SharpCharts | D187 |
| image_08 | Using with StockChartsACP (section-fallback) | Using with StockChartsACP | D187 |

---

## DÉCISIONS

### D177 — MFI : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md, image_01) : Le Money Flow Index (MFI) est un oscillateur qui utilise le **prix ET le volume** pour mesurer la pression acheteuse et vendeuse. Créé par Gene Quong et Avrum Soudack. Il est aussi appelé **RSI pondéré par le volume** (volume-weighted RSI).
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Le money flow est positif quand le typical price monte (pression acheteuse) et négatif quand il baisse (pression vendeuse) ; l'oscillateur évolue entre 0 et 100. En tant qu'oscillateur de momentum lié au volume, le MFI est adapté à l'identification des retournements et des extrêmes de prix.
⚫🔴 **PROPRIÉTAIRE / NON VÉRIFIÉ (rattachement TRADEX-AI)** : Candidat retenu pour l'**Énergie Belkhayate** (mémoire projet, seuils 20/80). Équivalence non affirmée par la source — arbitrage MFI vs proxy ATR non tranché (Énergie stub, attendre fin Trading Geek).
**TRADEX-AI C2/C5** : MFI = brique « volume + momentum » candidate pour l'Énergie et le sentiment de pression d'ordres sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D178 — MFI : formule de calcul (14 périodes par défaut)
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md, image_02) : Calcul en étapes — `Typical Price = (High + Low + Close)/3` ; `Raw Money Flow = Typical Price × Volume` ; `Money Flow Ratio = (Positive Money Flow 14p)/(Negative Money Flow 14p)` ; `MFI = 100 − 100/(1 + Money Flow Ratio)`.
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Le Raw Money Flow est positif quand le typical price monte d'une période à l'autre, négatif quand il baisse ; il est **ignoré** si le typical price est inchangé. Le Raw Money Flow équivaut au « dollar volume » (volume × prix typique).
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Réglage par défaut = **14 périodes** (recommandé par les créateurs et défaut SharpCharts).
**TRADEX-AI C0** : Formule déterministe à répliquer côté export NinjaScript (besoin OHLCV + volume) ; aligner sur 14 périodes.
*Catégorie : indicateurs_momentum*

---

### D179 — MFI vs RSI : le volume comme valeur ajoutée
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Le MFI s'interprète comme le RSI, la grande différence étant le **volume**. La théorie veut que le volume précède le prix ; comme le RSI mène déjà le prix (momentum), l'ajout du volume peut **augmenter ce temps d'avance**.
**TRADEX-AI C2/C3** : Préférer le MFI au RSI nu quand le signal repose sur la pression de volume (order flow GC/HG/CL/ZW) ; sinon traiter MFI et RSI comme complémentaires, pas redondants (cf. multicollinéarité).
*Catégorie : indicateurs_momentum*

---

### D180 — Les 3 signaux de base (Quong & Soudack)
🔵 **ÉCOLE** (Source : money_flow_index_mfi.md) : Quong et Soudack identifient trois signaux — (1) niveaux surachat/survente avertissant d'extrêmes insoutenables ; (2) divergences haussières/baissières anticipant des retournements ; (3) failure swings à 80 ou 20 signalant des retournements potentiels. L'article combine divergences et failure swings en un groupe de signaux pour plus de robustesse.
**TRADEX-AI C3** : Cadre de lecture du MFI à trois familles de signaux ; les traiter comme confirmations, jamais comme entrées isolées (cf. D182, D186).
*Catégorie : indicateurs_momentum*

---

### D181 — Surachat / survente : 80/20 puis extrêmes 90/10
🔵 **ÉCOLE** (Source : money_flow_index_mfi.md, image_03, image_04) : Classiquement MFI > 80 = surachat, MFI < 20 = survente. Quong et Soudack recommandent d'**étendre** les extrêmes : > 90 = véritablement suracheté, < 10 = véritablement survendu ; ces lectures rares suggèrent un mouvement insoutenable (exemples Nike < 10, Philip Morris à 90).
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Un niveau de survente seul ne suffit pas à devenir haussier — il faut une confirmation de retournement (cassure de résistance, gap + cassure de trend line sur volume).
**TRADEX-AI C1/C3** : Pré-filtre Python — n'armer un signal MFI extrême (>90 / <10) qu'avec confirmation price action sur GC/HG/CL/ZW. Seuils 20/80 = cohérents avec l'hypothèse Énergie Belkhayate (cf. D177).
*Catégorie : indicateurs_momentum*

---

### D182 — Piège : surachat/survente persistants en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : En tendance forte, le MFI peut rester suracheté (>80) pendant que le prix continue de monter, ou survendu (<20) pendant que le prix continue de baisser. Les niveaux classiques posent problème en tendance directionnelle.
**TRADEX-AI C2/C3** : Ne jamais traiter MFI > 80 comme vente (ou < 20 comme achat) en tendance forte confirmée sur GC/HG/CL/ZW — exiger structure/price action. Garde anti-faux-signal.
*Catégorie : indicateurs_momentum*

---

### D183 — Divergence et failure swing HAUSSIERS
🔵 **ÉCOLE** (Source : money_flow_index_mfi.md) : **Divergence haussière** = le prix fait un plus bas plus bas mais le MFI fait un plus bas plus haut (money flow qui s'améliore). **Failure swing haussier** = le MFI passe sous 20 (survente), remonte au-dessus de 20, tient au-dessus de 20 sur un pullback, puis casse son plus haut de réaction précédent. Tous deux haussiers en downtrend (retournement possible).
**TRADEX-AI C3** : Détecter divergence MFI/prix et failure swing haussier comme signaux de retournement sur GC/HG/CL/ZW, priorisés après extrême de survente.
*Catégorie : indicateurs_momentum*

---

### D184 — Divergence et failure swing BAISSIERS
🔵 **ÉCOLE** (Source : money_flow_index_mfi.md) : **Divergence baissière** = le prix fait un plus haut plus haut mais le MFI fait un plus haut plus bas (money flow qui se détériore). **Failure swing baissier** = le MFI passe au-dessus de 80, replonge sous 80, échoue à repasser 80 sur un rebond, puis casse son plus bas de réaction précédent. Tous deux baissiers en uptrend.
**TRADEX-AI C3** : Détecter divergence et failure swing baissiers comme signaux de retournement sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D185 — Robustesse : divergence + failure swing simultanés
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md, image_05) : Quand une divergence ET un failure swing surviennent **en même temps**, le signal est bien plus fort que l'un ou l'autre seul (exemple CVS 2012 haussier ; à l'inverse, en mars-mai 2013 une divergence baissière SANS failure swing net n'a pas produit de déclin marqué).
🟡 **CONVENTION** : Pondérer le signal MFI par la **coïncidence** des deux sous-signaux.
**TRADEX-AI C3/C4** : Score de signal — augmenter la confiance d'un retournement MFI uniquement si divergence + failure swing coïncident sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D186 — Bottom line : centerline 50 non idéal, jamais seul
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Le MFI combine momentum, volume et formule RSI. Bien que « RSI pondéré volume », utiliser la **ligne médiane 50** pour un biais haussier/baissier **n'est pas idéal** : le MFI est mieux adapté aux retournements (surachat/survente, divergences, failure swings). Comme tout indicateur, il **ne doit pas être utilisé seul** — le combiner à un oscillateur de momentum pur (RSI) ou à l'analyse de patterns.
**TRADEX-AI C3** : Guard permanent — un signal MFI sur GC/HG/CL/ZW exige confirmation multi-outil (price action, pattern, volume) ; ne pas baser la décision sur le seul franchissement de 50.
*Catégorie : gestion_risque_entree*

---

### D187 — Implémentation / paramétrage (référence)
🔵 **ÉCOLE** (Source : money_flow_index_mfi.md, image_06, image_07, image_08) : MFI disponible dans SharpCharts (above/below/behind le prix) et StockChartsACP (Chart Settings). Défaut = 14 périodes ; timeframe plus court = plus sensible, plus long = moins sensible. Lignes horizontales personnalisables (ex. 10,90).
**TRADEX-AI C0** : Référence de paramétrage ; défaut 14 périodes + lignes 10/90 (ou 20/80) à exposer dans l'UI / config.
*Catégorie : configuration*

---

### D188 — Scans MFI officiels StockCharts
🟢 **FAIT VÉRIFIÉ** (Source : money_flow_index_mfi.md) : Scan « MFI Oversold » = prix > 20 $, volume moyen filtré, `Daily MFI(14) < 10`. Scan « MFI Overbought » = `Daily MFI(14) > 90`. ⚠️ Note officielle : le volume intraday est incomplet — lancer les scans MFI sur « Last Market Close » (vrai aussi pour A/D, OBV, PVO).
**TRADEX-AI C1** : Transposer ces seuils (MFI(14) <10 / >90) en filtres Python de pré-sélection sur GC/HG/CL/ZW ; calculer le MFI sur barres clôturées (jamais sur la barre en cours).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D177 → D188 (12) |
| Images certifiées citées | 8/8 |
| Catégories utilisées | indicateurs_momentum · gestion_risque_entree · configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · ⚫🔴 (rattachement Énergie) |
| Belkhayate | **CONCERNÉ** — MFI = candidat Énergie (hypothèse projet, non affirmée par la source ; arbitrage MFI vs ATR non tranché) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
