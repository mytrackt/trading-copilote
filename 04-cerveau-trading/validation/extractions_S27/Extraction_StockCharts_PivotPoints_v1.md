# Extraction StockCharts — Pivot Points
**Source :** `bundles/stockcharts/pivot_points.md` (HTTP 200 · ~9 800 car.) + 12 images (11 certifiées · 1 à vérifier = visuel livre affilié, non-contenu)
**Méthode images :** double ancrage (.md figcaption + HTML légende locale) · 11/12 certifiées
**Décisions :** D189 → D198 · **Page :** chartschool.stockcharts.com/.../technical-overlays/pivot-points
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : les **Pivots Belkhayate** (= Pivot Point standard + Gann + clôture veille, mémoire projet) reposent sur ce socle. Le Pivot Point standard `P=(H+L+C)/3` en est une brique 🟢 ; l'assemblage propre à Belkhayate est ⚫🔴 (non publié). Les pivots Fibonacci utilisent 0,618 — **écho du ratio COG 0,618/1,618** (COGParams figés).

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Example of pivot points on a 10-minute chart | Timeframes | D190 |
| image_02 | Pivot points on a 60-minute chart | Timeframes | D190 |
| image_03 | Pivot Points on a daily chart | Timeframes | D190 |
| image_04 | Example of standard Pivot Points on a 15-minute chart | Standard Pivot Points | D191 |
| image_05 | Example of Fibonacci Pivot Points on a 15-minute chart | Fibonacci Pivot Points | D192 |
| image_06 | Example of Demark Pivot Points on a 15-minute chart | Demark Pivot Points | D193 |
| image_07 | When price moves above the Pivot Point, it's positive | Setting the Tone | D194 |
| image_08 | Support and resistance levels based on Pivot Points | Support and Resistance | D195 |
| image_09 | Second S/R levels identifying overbought/oversold | Support and Resistance | D196 |
| image_10 | Example of Pivot Points in SharpCharts | Using with SharpCharts | D198 |
| image_11 | (section-fallback : Using with SharpCharts) | Using with SharpCharts | D198 |
| (à vérifier) | visuel livre « Technical Trading Tactics » (Person) | Recommended Books | — (non-contenu) |

---

## DÉCISIONS

### D189 — Pivot Points : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md) : Les Pivot Points sont des **niveaux significatifs** servant à déterminer le mouvement directionnel et les supports/résistances potentiels. Ils utilisent le **plus haut, plus bas et clôture de la période précédente** pour estimer les S/R futurs — ce sont des indicateurs **prédictifs / leading**. Au moins cinq versions existent ; l'article traite Standard, Demark et Fibonacci.
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md) : Origine = floor traders, qui calculaient au début de séance un Pivot Point depuis les H/L/C de la veille, puis en dérivaient S1/S2/R1/R2 pour la journée.
**TRADEX-AI C1** : Niveaux déterministes calculables en Python depuis les barres clôturées de GC/HG/CL/ZW ; base des Pivots Belkhayate (cf. en-tête).
*Catégorie : structure_marche*

---

### D190 — Pivot Points : horizons et règle de fixité
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_01, image_02, image_03) : Mapping période → données utilisées — graphiques **1/5/10/15 min** = H/L/C de la **veille** ; **30/60/120 min** = H/L/C de la **semaine précédente** (semaines calendaires) ; **daily** = données du **mois précédent** ; **weekly/monthly** = **année précédente**.
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md) : Une fois posés, les Pivot Points **ne changent pas** et restent en jeu toute la période (jour/semaine/mois).
**TRADEX-AI C1/C3** : Recalcul à chaque ouverture de période ; niveaux figés intra-période. Cohérent avec les timeframes Belkhayate (Standard 15 min → pivots de la veille).
*Catégorie : structure_marche*

---

### D191 — Standard Pivot Points : formule
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_04) : `P = (High + Low + Close)/3` (moyenne simple, période précédente). `S1 = (P×2) − High` ; `S2 = P − (High − Low)` ; `R1 = (P×2) − Low` ; `R2 = P + (High − Low)`. Le pivot médian (P) est tracé en ligne pleine entre supports et résistances.
**TRADEX-AI C0/C1** : Formule à coder telle quelle ; `P=(H+L+C)/3` = brique du pivot Belkhayate. Citer cette source comme référence non propriétaire.
*Catégorie : structure_marche*

---

### D192 — Fibonacci Pivot Points : formule (0,382 / 0,618 / 1,0)
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_05) : Même base `P=(H+L+C)/3`, puis multiples de Fibonacci du différentiel high-low : `S1/R1 = P ∓ 0,382×(H−L)` ; `S2/R2 = P ∓ 0,618×(H−L)` ; `S3/R3 = P ∓ 1,0×(H−L)`.
🔵 **ÉCOLE** : Variante Fibonacci des pivots (38,2 % / 61,8 % / 100 %).
**TRADEX-AI C1** : Le coefficient **0,618** rejoint le ratio COG figé (0,618/1,618) — point de convergence à exploiter pour la cohérence des niveaux Belkhayate sur GC/HG/CL/ZW (sans affirmer que Belkhayate utilise ces pivots Fibonacci).
*Catégorie : structure_marche*

---

### D193 — Demark Pivot Points : formule conditionnelle
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_06) : Base conditionnelle selon clôture vs ouverture — si `Close < Open` : `X = High + 2×Low + Close` ; si `Close > Open` : `X = 2×High + Low + Close` ; si `Close = Open` : `X = High + Low + 2×Close`. Puis `P = X/4` ; `S1 = X/2 − High` ; `R1 = X/2 − Low`. **Un seul** R1 et un seul S1 (pas de niveaux multiples).
**TRADEX-AI C1** : Variante alternative (single S/R) ; non prioritaire vs Standard pour le socle Belkhayate.
*Catégorie : structure_marche*

---

### D194 — Pivot médian : donner le ton directionnel
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_07) : Le Pivot Point (P) donne le **ton général** du price action. Au-dessus de P = positif/force, cible la 1re résistance ; cassure de R1 = force accrue, cible R2. À l'inverse, sous P = faiblesse, cible S1 puis S2.
**TRADEX-AI C1/C3** : Position du prix vs P = filtre directionnel binaire (biais long/short) sur GC/HG/CL/ZW, à confirmer (cf. D197).
*Catégorie : structure_marche*

---

### D195 — Pivots comme supports/résistances traditionnels
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_08) : Les S/R issus des pivots s'emploient comme des S/R classiques : surveiller le price action quand un niveau entre en jeu. Repli vers support + raffermissement → test réussi + rebond (chercher un pattern haussier / signal d'indicateur pour confirmer). Avancée vers résistance + stagnation → échec + repli (confirmer par pattern/indicateur baissier).
**TRADEX-AI C3** : Traiter les pivots comme zones de confirmation, pas comme entrées automatiques ; exiger price action / pattern à l'approche du niveau.
*Catégorie : gestion_risque_entree*

---

### D196 — S2 / R2 : zones de surachat / survente
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md, image_09) : Un mouvement au-dessus de **R2** montre de la force mais indique une situation de **surachat** pouvant mener à un pullback ; sous **S2**, faiblesse mais **survente** court terme pouvant mener à un rebond.
**TRADEX-AI C3/C5** : Utiliser R2/S2 comme bornes d'épuisement pour pondérer le risque d'un retournement court terme sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D197 — Takeaway : direction d'abord, confirmation obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : pivot_points.md) : Méthodologie — la **direction** se lit via le price action courant relatif au pivot (ouverture au-dessus/au-dessous, ou franchissement en séance) ; les S/R interviennent **après** détermination de la direction. Comme tout indicateur, confirmer les signaux de pivots par d'autres outils : pattern chandelier baissier à R2, RSI survendu à S2, retournement MACD pour valider un test de support.
🟡 **CONVENTION** : Un niveau de pivot seul n'est pas une entrée.
**TRADEX-AI C3/C4** : Hiérarchie — direction (prix vs P) → niveau S/R → confirmation multi-outil (chandelier, RSI, MACD) avant décision sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

---

### D198 — Implémentation SharpCharts (référence)
🔵 **ÉCOLE** (Source : pivot_points.md, image_10, image_11) : Pivot Points = **Overlay** SharpCharts. Standard par défaut (paramètres vides) ; « F » → Fibonacci ; « D » → Demark ; les trois affichables simultanément. Note : S2/S3 ou R2/R3 peuvent sortir de l'échelle de prix (hors graphique).
**TRADEX-AI C0** : Référence de paramétrage ; exposer Standard/Fibonacci/Demark en option ; gérer l'affichage hors-échelle des niveaux 2/3.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D189 → D198 (10) |
| Images certifiées citées | 11/12 (1 visuel livre non-contenu écarté) |
| Catégories utilisées | structure_marche · gestion_risque_entree · configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · ⚫🔴 (rattachement Belkhayate) |
| Belkhayate | **CONCERNÉ** — Pivot standard `P=(H+L+C)/3` = brique des Pivots Belkhayate (assemblage PP+Gann+clôture veille non publié = ⚫🔴) · pivots Fibonacci 0,618 = écho COG |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
