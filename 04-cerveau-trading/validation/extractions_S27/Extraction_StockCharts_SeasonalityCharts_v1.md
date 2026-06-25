# Extraction StockCharts — Seasonality Charts
**Source :** `bundles/stockcharts/seasonality_charts.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D3551 → D3562 · **Page :** chartschool.stockcharts.com/.../chart-types/seasonality-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : la page illustre la saisonnalité sur **$GOLD (futures spot)** → directement applicable à GC, et à la saisonnalité des commodities (CL/HG/ZW). Cercle C4 (macro/calendrier) + timing.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Seasonality chart $GOLD futures spot | Calculations | D3553 |
| image_02 | Seasonality Intel (biais avril/octobre) | Interpreting | D3556 |
| image_03 | Seasonality Russell 2000 vs S&P 500 | Relative Seasonality | D3559 |
| image_04 | Seasonality line chart (MRK vs SPX) | Viewing Options | D3560 |
| image_05 | Seasonality same-scale (meilleure/pire année) | Viewing Options | D3561 |

## DÉCISIONS

### D3551 — Saisonnalité : définition
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : Tendance d'un titre à mieux/moins bien performer selon des périodes (jours de semaine, mois, semestres, années). Ex. Yale Hirsch (*Stock Trader's Almanac*) : depuis 1950, meilleur semestre S&P 500 = nov.→avr., pire = mai→oct. (« sell in May and go away »).
🔵 **ÉCOLE** : Concept de Yale Hirsch.
**TRADEX-AI C4** : Biais saisonnier = couche contextuelle de timing macro.
*Catégorie : timing*

### D3552 — Calcul : 2 nombres par mois
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : L'outil calcule (1) le **% de fois où le mois est positif** et (2) le **gain/perte moyen** du mois. Ex. sur 19 ans, 19 points/mois ; 9 hausses → 47 % (9/19), 15 hausses → 74 % (15/19).
**TRADEX-AI C1** : Statistiques déterministes calculables par actif (GC/HG/CL/ZW).
*Catégorie : structure_marche*

### D3553 — Exemple $GOLD
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md, image_01) : Histogramme du gold futures spot ($GOLD) — nombre du haut = % de clôtures plus hautes pour le mois, nombre du bas = gain/perte moyen sur 19 mois.
**TRADEX-AI C4** : Profil saisonnier de l'Or directement exploitable pour GC.
*Catégorie : timing*

### D3554 — Effet du mois en cours
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : Le mois en cours est « work in progress » (chiffres susceptibles de changer jusqu'à la fin du mois) ; les mois futurs (slider - 1) reposent sur une année de moins.
**TRADEX-AI C1** : Garde — figer les stats saisonnières sur mois clôturés.
*Catégorie : configuration*

### D3555 — Tendance historique, pas garantie
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : La saisonnalité décrit le passé ; aucune garantie que la performance future égale la passée. À utiliser pour compléter d'autres signaux.
**TRADEX-AI C3** : Jamais déclencheur seul ; complément contextuel.
*Catégorie : gestion_risque_entree*

### D3556 — Seuils de biais (35 %/65 %)
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md, image_02) : Biais haussier si gain > 50 % du temps, baissier si < 50 %. Chercher des lectures plus extrêmes : > 65 % = biais haussier au-dessus de la moyenne, < 35 % = biais baissier au-dessus de la moyenne (ex. INTC : avril 84 %, octobre 79 %).
**TRADEX-AI C4** : Seuils 35 %/65 % pour qualifier un biais saisonnier fort.
*Catégorie : timing*

### D3557 — % positif ≠ rendement net
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : Un titre peut monter plus souvent qu'il ne baisse mais avoir une perte moyenne (ex. INTC juin : 58 % positif, gain moyen -0,3 %) — les pertes des baisses dépassent les gains des hausses.
**TRADEX-AI C3** : Croiser % positif ET gain moyen, pas l'un seul.
*Catégorie : gestion_risque_entree*

### D3558 — Chiffres saisonniers = volatils/datés
⏳ **VOLATILE** (Source : seasonality_charts.md) : Les pourcentages (84 %, 79 %, 47 %…) sont calculés sur une fenêtre historique datée (article de janv. 2014) et évoluent avec les données ; ne pas figer comme constantes.
**TRADEX-AI C1** : Recalculer les stats saisonnières en continu sur fenêtre glissante par actif.
*Catégorie : configuration*

### D3559 — Saisonnalité relative
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md, image_03) : Comparer la performance d'un titre contre un autre (option « compare ») pour trouver les sur/sous-performances mensuelles (ex. Russell 2000 surperforme le S&P 500 en juin 70 % du temps).
**TRADEX-AI C7** : Saisonnalité relative inter-marché (ex. GC vs DX par mois).
*Catégorie : timing*

### D3560 — Modes d'affichage (line)
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md, image_04) : 3 vues — line, same-scale, histogram. La vue line ne montre que la direction (pas d'échelle).
**TRADEX-AI C0** : Référence d'affichage.
*Catégorie : configuration*

### D3561 — Modes d'affichage (same-scale)
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md, image_05) : Vue same-scale = toutes les lignes de performance partent de 0 % (comparaison année par année).
**TRADEX-AI C0** : Référence d'affichage.
*Catégorie : configuration*

### D3562 — Takeaway
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_charts.md) : La saisonnalité donne une perspective historique pour augmenter l'edge ; chercher setups haussiers quand le pattern saisonnier est fortement haussier (et inverse). À combiner avec d'autres techniques.
**TRADEX-AI C4** : Intégrer le biais saisonnier GC/HG/CL/ZW comme pondération contextuelle de la grille, jamais comme déclencheur.
*Catégorie : timing*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3551 → D3562 (12) |
| Images citées | 5/5 |
| Catégories | timing · structure_marche · gestion_risque_entree · configuration |
| Tags | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · ⏳ VOLATILE |
| Belkhayate | NON CONCERNÉ (saisonnalité $GOLD directement utile à GC) |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
