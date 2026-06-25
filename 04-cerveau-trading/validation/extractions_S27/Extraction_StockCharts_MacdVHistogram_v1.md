# Extraction StockCharts — MACD-V Histogram

**Source :** `bundles/stockcharts/macd_v_histogram.md` (HTTP 200 · ~2 992 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende locale + section fallback) · 1/1 certifiée
**Décisions :** D2491 → D2496 · **Page :** chartschool.stockcharts.com/.../technical-indicators/macd-v-histogram
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Périmètre** : famille MACD. Extension **histogramme** du MACD-V (Spiroglou). Page courte. CERCLE momentum **C3**.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | MACD-V Histogram applied to SPY in StockChartsACP | Using MACD-V Histogram in StockCharts ACP | D2495 |

---

## DÉCISIONS

### D2491 — MACD-V Histogram : nature et filiation
🟢 **FAIT VÉRIFIÉ** (Source : macd_v_histogram.md) : Le MACD-V Histogram est une **extension naturelle** du travail réalisé sur le MACD-V (Alex Spiroglou). Il représente la distance entre le MACD-V et sa ligne de signal.
**TRADEX-AI C3** : Variante histogramme du MACD-V à exposer comme proxy d'anticipation du croisement MACD-V/signal sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2492 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : macd_v_histogram.md) : Formule — `MACD-V = [(EMA 12p − EMA 26p) / ATR(26)] × 100` ; `Signal line = EMA 9p du MACD-V` ; `Histogram = MACD-V − Signal Line` (EMA = moyenne mobile exponentielle). Formule identique au MACD-V, l'histogramme étant l'écart MACD-V moins signal.
**TRADEX-AI C0** : Formule déterministe à répliquer côté export NinjaScript (besoin OHLC pour l'ATR 26) ; défaut 12/26/9 + ATR(26).
*Catégorie : indicateurs_momentum*

---

### D2493 — Seuil de risque haut (oversold) : histogramme < −40
🔵 **ÉCOLE** (Source : macd_v_histogram.md) : Le marché est considéré en **risque court terme (oversold/survendu)** quand le MACD-V Histogram est **< −40**.
**TRADEX-AI C3** : Seuil normalisé exploitable tel quel (échelle commune inter-marché) — armer un filtre survente histogramme <−40 sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2494 — Seuil de risque bas (overbought) : histogramme > +40
🔵 **ÉCOLE** (Source : macd_v_histogram.md) : Le marché est considéré en **risque court terme (overbought/suracheté)** quand le MACD-V Histogram est **> +40**.
**TRADEX-AI C3** : Seuil normalisé exploitable tel quel — armer un filtre surachat histogramme >+40 sur GC/HG/CL/ZW. Combiner avec D2493 pour une bande de risque ±40.
*Catégorie : indicateurs_momentum*

---

### D2495 — Disponibilité et paramétrage StockCharts ACP
🔵 **ÉCOLE** (Source : macd_v_histogram.md, image_01) : Le MACD-V Histogram est un indicateur **standard dans StockCharts ACP**. Accès : Chart Settings → faire défiler les Standard Indicators → sélectionner MACD-V Histogram → modifier les paramètres via l'icône de réglages. Exemple illustré : appliqué au SPY.
**TRADEX-AI C0** : Référence de paramétrage ; exposer le MACD-V Histogram (12/26/9 + ATR 26, bande ±40) en panneau séparé dans l'UI.
*Catégorie : configuration*

---

### D2496 — Cadre d'usage : seuils ±40 = bornes de risque court terme
🟡 **CONVENTION** : Les deux seuils documentés (±40) délimitent une **bande de risque court terme** — au-delà, le marché est jugé en extrême (sur-acheté/sur-vendu) potentiellement insoutenable ; l'histogramme MACD-V sert ici de détecteur d'extrêmes plutôt que de signal d'entrée direct.
**TRADEX-AI C3** : Pré-filtre Python — n'armer un signal d'extrême histogramme MACD-V (|valeur| > 40) qu'avec confirmation price action ; jamais entrée isolée sur GC/HG/CL/ZW. Garde anti-faux-signal en tendance forte (cf. piège des oscillateurs).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2491 → D2496 (6) |
| Images certifiées citées | 1/1 |
| Catégories utilisées | indicateurs_momentum · configuration · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Belkhayate | **NON CONCERNÉ** (variante MACD pure, aucun lien Belkhayate revendiqué) |
| Cas à vérifier | Aucun — page courte, faits tous littéraux ; D2496 = synthèse conventionnelle explicite |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
