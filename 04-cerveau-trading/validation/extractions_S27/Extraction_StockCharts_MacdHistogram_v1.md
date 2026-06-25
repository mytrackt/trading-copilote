# Extraction StockCharts — MACD-Histogram

**Source :** `bundles/stockcharts/macd_histogram.md` (HTTP 200 · ~16 645 car.) + 8 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende locale + section fallback) · 8/8 certifiées
**Décisions :** D2451 → D2462 · **Page :** chartschool.stockcharts.com/.../technical-indicators/macd-histogram
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Périmètre** : famille MACD. Le MACD de base est déjà extrait ailleurs — ce fichier ne couvre QUE la variante **MACD-Histogram** (Thomas Aspray). CERCLE momentum **C3**.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Example of the MACD. | How Do You Calculate the MACD Histogram? | D2452 |
| image_02 | MACD and MACD Histogram showing crossovers, convergences, and divergences. | How Do You Interpret the MACD Histogram? | D2454 |
| image_03 | MACD-Histogram - Chart 2 | How Do You Interpret Peak-Trough Divergence... | D2455 |
| image_04 | MACD-Histogram - Chart 3 | How Do You Interpret Peak-Trough Divergence... | D2455 |
| image_05 | MACD-Histogram - Chart 4 | Slant Divergence | D2456 |
| image_06 | MACD-Histogram - Chart 5 | Slant Divergence | D2456 |
| image_07 | MACD-Histogram - Chart 6 | Using with SharpCharts | D2459 |
| image_08 | MACD - Chart 7 | Using with SharpCharts | D2459 |

---

## DÉCISIONS

### D2451 — MACD-Histogram : définition et créateur
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Le MACD-Histogram mesure la **distance entre la ligne MACD et sa ligne de signal** (EMA 9 jours du MACD). Comme le MACD, c'est un oscillateur qui fluctue au-dessus et en dessous de la ligne zéro. Développé par **Thomas Aspray** pour **anticiper** les croisements de ligne de signal du MACD : comme le MACD utilise des moyennes mobiles qui retardent le prix, ces croisements peuvent arriver tard et dégrader le ratio rendement/risque ; une divergence du MACD-Histogram alerte d'un croisement imminent.
**TRADEX-AI C3** : Le MACD-Histogram = brique de momentum d'anticipation (signal avant croisement MACD) à exposer sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2452 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md, image_01) : Formule — `MACD = EMA 12 jours − EMA 26 jours` (sur cours de clôture) ; `Signal Line = EMA 9 jours du MACD` ; `MACD-Histogram = MACD − Signal Line`. L'histogramme est **positif quand le MACD est au-dessus de son EMA 9 jours**, négatif quand il est en dessous.
**TRADEX-AI C0** : Formule déterministe à répliquer côté export NinjaScript (besoin clôtures uniquement) ; défaut 12/26/9.
*Catégorie : indicateurs_momentum*

---

### D2453 — Quatrième dérivée du prix (indicateur d'un indicateur)
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Le MACD-Histogram est à **quatre étapes** du prix du sous-jacent (quatrième dérivée). 1re dérivée : EMA 12 + EMA 26 ; 2e : MACD (EMA12 − EMA26) ; 3e : ligne de signal MACD (EMA 9 du MACD) ; 4e : MACD-Histogram (MACD − signal). À garder à l'esprit lors de l'analyse : c'est un indicateur d'un indicateur, conçu pour anticiper les signaux du MACD.
**TRADEX-AI C3** : Garde de prudence — l'éloignement du prix (4 dérivées) impose de ne jamais traiter le MACD-Histogram comme signal autonome sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2454 — Interprétation : convergence, divergence, croisement zéro
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md, image_02) : L'histogramme est positif quand le MACD est au-dessus de sa ligne de signal ; les valeurs positives **augmentent** quand le MACD s'écarte (à la hausse) et **diminuent** quand MACD et signal convergent. Le MACD-Histogram **croise la ligne zéro quand le MACD croise sa ligne de signal**. Valeurs négatives quand le MACD est sous sa ligne de signal (augmentent à mesure que l'écart se creuse vers le bas).
**TRADEX-AI C3** : Le passage par zéro de l'histogramme = proxy temps réel du croisement MACD/signal ; l'expansion/contraction mesure la force/faiblesse du momentum.
*Catégorie : indicateurs_momentum*

---

### D2455 — Divergence peak-trough (pic-creux)
🔵 **ÉCOLE** (Source : macd_histogram.md, image_03, image_04) : Deux types de divergences — **peak-trough** et **slant**. Une divergence peak-trough se forme avec **deux pics ou deux creux** dans l'histogramme. **Haussière** = le MACD fait un plus bas plus bas mais l'histogramme fait un plus bas plus haut (deux creux distincts, ex. Caterpillar). **Baissière** = le MACD fait un plus haut plus haut mais l'histogramme fait un plus haut plus bas (deux pics distincts avec creux intermédiaire, ex. Aeropostale). Des creux/pics bien définis sont importants pour la robustesse.
**TRADEX-AI C3** : Détecter divergence peak-trough MACD-Histogram comme alerte de croisement de signal à venir sur GC/HG/CL/ZW ; exiger pics/creux bien définis.
*Catégorie : divergence*

---

### D2456 — Divergence slant (en pente)
🔵 **ÉCOLE** (Source : macd_histogram.md, image_05, image_06) : Les divergences **slant** se forment **sans pics ni creux bien définis** : simplement une pente vers la ligne zéro à mesure que l'histogramme s'en rapproche, reflétant une convergence MACD/signal. Le momentum est fort quand le MACD s'écarte de son signal (histogramme s'étend) et faiblit quand il s'en rapproche (histogramme se contracte). Un histogramme qui se **contracte est la première étape vers un croisement de signal** (ex. Boeing haussier, Disney baissier).
**TRADEX-AI C3** : Surveiller la contraction de l'histogramme comme signal précoce de retournement de momentum ; complément des divergences peak-trough.
*Catégorie : divergence*

---

### D2457 — Croisement de signal = signal MACD le plus fréquent
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Le MACD-Histogram est conçu pour **prédire les croisements de ligne de signal du MACD**, qui sont les signaux MACD **les plus fréquents**. Les divergences de l'histogramme peuvent servir à **filtrer** ces croisements, ce qui réduit le nombre de signaux.
**TRADEX-AI C3** : Utiliser les divergences de l'histogramme comme filtre des croisements MACD/signal pour réduire les faux signaux sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D2458 — Robustesse des divergences : durée et amplitude
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Même avec un filtre, la **robustesse** des divergences reste un problème. Les divergences **courtes et peu profondes** (quelques jours, mouvements faibles) sont bien plus fréquentes et **généralement moins robustes** que les divergences **longues et amples** (quelques semaines, mouvements plus prononcés).
🟡 **CONVENTION** : Pondérer la divergence par sa durée et son amplitude.
**TRADEX-AI C3** : Score de signal — n'accorder de confiance qu'aux divergences amples/longues ; filtrer les divergences courtes/superficielles sur GC/HG/CL/ZW.
*Catégorie : divergence*

---

### D2459 — Entrée agressive : zone proche du zéro (−0,20 / +0,20)
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md, image_07, image_08) : Le croisement de signal fournit la **confirmation ultime**, mais les traders agressifs peuvent améliorer le ratio rendement/risque en agissant **juste avant le croisement** — quand le MACD-Histogram est aussi proche que possible de la ligne zéro sans la croiser, **généralement entre −0,20 et +0,20**.
🔴 **NON VÉRIFIÉ (généralisation)** : Le seuil ±0,20 dépend de l'échelle de prix du sous-jacent (exemple StockCharts sur actions) ; à recalibrer pour GC/HG/CL/ZW, non transposable tel quel.
**TRADEX-AI C3** : Entrée anticipée optionnelle proche de zéro ; seuil ±0,20 à NE PAS coder en dur — recalibrer par actif. Garde mode AUTO : confirmation croisement requise.
*Catégorie : signal*

---

### D2460 — Histogramme en stand-alone et paramétrage SharpCharts
🔵 **ÉCOLE** (Source : macd_histogram.md, image_07, image_08) : Le MACD-Histogram peut être affiché en **indicateur autonome** (facilite l'identification des divergences/croisements), placé au-dessus/en dessous/derrière le prix (souvent au-dessus ou en dessous car il prend de la place). Pour afficher le MACD **sans** histogramme : choisir MACD et changer le nombre de la ligne de signal de 9 à **1 (9,26,1)** (supprime signal + histogramme) ; la ligne de signal peut ensuite être rajoutée séparément (EMA 9 jours).
**TRADEX-AI C0** : Référence de paramétrage UI ; exposer l'histogramme en panneau séparé. Astuce (9,26,1) = MACD nu.
*Catégorie : configuration*

---

### D2461 — Scan « MACD-Histogram passe positif » (après pullback en uptrend)
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Scan officiel — actions au-dessus de leur SMA 200 (uptrend global), histogramme passant de négatif à positif, **MACD requis négatif** pour assurer que la reprise survient après un pullback. Conditions : `Yesterday's MACD Hist(12,26,9) < 0 AND MACD Hist(12,26,9) > 0 AND MACD Line(12,26,9) < 0 AND Close > SMA(200)`.
**TRADEX-AI C1** : Transposer en filtre Python de pré-sélection long sur GC/HG/CL/ZW (histogramme bascule positif + MACD encore <0 + tendance haussière), sur barres clôturées.
*Catégorie : signal*

---

### D2462 — Scan « MACD-Histogram passe négatif » (après bounce en downtrend)
🟢 **FAIT VÉRIFIÉ** (Source : macd_histogram.md) : Scan officiel — actions sous leur SMA 200 (downtrend global), histogramme passant de positif à négatif, **MACD requis positif** pour assurer que le retournement survient après un rebond. Conditions : `Yesterday's MACD Hist(12,26,9) > 0 AND MACD Hist(12,26,9) < 0 AND MACD Line(12,26,9) > 0 AND Close < SMA(200)`.
**TRADEX-AI C1** : Transposer en filtre Python de pré-sélection short sur GC/HG/CL/ZW (histogramme bascule négatif + MACD encore >0 + tendance baissière), sur barres clôturées.
*Catégorie : signal*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2451 → D2462 (12) |
| Images certifiées citées | 8/8 |
| Catégories utilisées | indicateurs_momentum · divergence · signal · configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · 🔴 NON VÉRIFIÉ |
| Belkhayate | **NON CONCERNÉ** (variante MACD pure, aucun lien Belkhayate revendiqué) |
| Cas à vérifier | D2459 : seuil ±0,20 non transposable tel quel aux futures (dépend de l'échelle de prix) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
