# Extraction StockCharts — Fibonacci Time Zones

**Source :** `bundles/stockcharts/fibonacci_time_zones.md` (HTTP 200 · ~8 200 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D1791 → D1810 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-time-zones
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.jpg | Fibonacci Time Zones on QQQ | How To Use Fibonacci Time Zones | CERTIFIE (accord .md + HTML) |
| image_02.png | Fibonacci Time Zones applied to a chart of QQQ. | QQQ Example | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3. Plotting Fibonacci Time Zones in the future. | QQQ Example | CERTIFIE (accord .md + HTML) |
| image_04.png | Note how the Fibonacci Time Zones can mark significant highs… | Euro Example | CERTIFIE (accord .md + HTML) |
| image_05.png | Adding extra bars to a chart can project potential reversal… | Euro Example | CERTIFIE (accord .md + HTML) |
| image_06.png | The Annotate button in the new SharpCharts workbench. | Adding Fibonacci Time Zones in SharpCharts | CERTIFIE (accord .md + HTML) |
| image_07.png | Example of a chart annotated with Fibonacci Time Zones using… | Adding Fibonacci Time Zones in SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1791 — Définition des Fibonacci Time Zones (lignes verticales temporelles)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « Fibonacci Time Zones are a technical analysis tool designed to identify potential areas of price reversal using the Fibonacci sequence. The tool draws vertical lines to the right at each Fibonacci ratio… based on significant swing highs and lows. »
**TRADEX-AI C1** : outil de timing — projette des intervalles temporels de retournement potentiel, pas des niveaux de prix.
*Catégorie : timing*

---

### D1792 — Ratios temporels communs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « most commonly 23.6%, 38.2%, 50%, 61.8%, and 78.6% ». (FAQ : « The most common ratios are 23.6%, 38.2%, 50%, 61.8%, and 78.6%. »)
🔵 ÉCOLE (Fibonacci) : grille de ratios standard de l'école Fibonacci.
⚫🔴 (écho COG 0,618) : le 61,8 % figure dans la grille — convergence de ratio avec les COGParams Belkhayate (0,618/1,618), non affirmée par la source.
**TRADEX-AI C1** : ratios de zonage temporel candidats.
*Catégorie : timing*

---

### D1793 — Lignes le long de l'axe des dates, espacement croissant
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « These lines extend along the date axis, marking expected intervals where reversals might occur based on the time that has passed… the distances between these zones start relatively small and grow in accordance with the Fibonacci Sequence. »
**TRADEX-AI C1** : la structure temporelle suit la suite de Fibonacci (espacement croissant) — paramètre de projection.
*Catégorie : timing*

---

### D1794 — Base mathématique 1,618 / 0,618
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « A number divided by the previous number approximates 1.618… A number divided by the next highest number approximates .6180… This is the basis for the 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : dérivation standard.
⚫🔴 (écho COG 0,618) : convergence du couple 0,618/1,618 avec le COG Belkhayate, non affirmée par la source.
**TRADEX-AI C1** : traçabilité des constantes employées.
*Catégorie : timing*

---

### D1795 — Nombre d'or (Phi)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « 1.618 refers to the Golden Ratio or Golden Mean, also called Phi. The inverse of 1.618 is .618. »
🔵 ÉCOLE (Fibonacci) : contexte théorique.
**TRADEX-AI C1** : contextualise les constantes ; pas d'implication opérationnelle directe.
*Catégorie : timing*

---

### D1796 — Ignorer les premières zones (clustering serré au départ)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « The slow start in the Fibonacci sequence creates relatively tight clustering at the beginning… You may need to ignore the first five or so time zones as, after that point, the zones expand pretty quickly. »
**TRADEX-AI C1** : garde-fou pratique — les premières zones sont peu exploitables (bruit). Filtre de timing.
*Catégorie : timing*

---

### D1797 — Zones-cibles : 21, 34, 55, 89, 144 jours (nombres de Fibonacci)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « potential reversal points can be found by looking ahead 21, 34, 55, 89, and 144 days, all of which are Fibonacci numbers. 21 days mark the 8th Fibonacci Time Zone. »
**TRADEX-AI C1** : horizons temporels privilégiés pour surveiller des retournements (en jours/périodes).
*Catégorie : timing*

---

### D1798 — Mapping zones → nombre de jours/périodes
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « 8th zone = 21 · 9th = 34 · 10th = 55 · 11th = 89 · 12th = 144 · 13th = 233 days or periods. » Construction récursive : « you can find future time zones by adding the previous two time zones (89 + 144 = 233). »
**TRADEX-AI C1** : table de correspondance reproductible pour positionner les zones futures.
*Catégorie : timing*

---

### D1799 — Indépendance vis-à-vis du timeframe (« days or periods »)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : la source qualifie systématiquement les zones de « days **or periods** », et l'outil compte des barres.
🟡 CONVENTION : interprétation — les zones se comptent en barres/périodes du graphe, donc applicables aux range bars NT8 (4-5 ticks) ou aux barres 15 min selon le mode.
**TRADEX-AI C1** : permet d'adapter l'outil aux timeframes Belkhayate (Standard 15 min / Rapide range bar) en comptant des barres plutôt que des jours calendaires.
*Catégorie : timing*

---

### D1800 — Exemple QQQ : zones coïncidant avec des tournants
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md, image_01, image_02) : QQQ depuis le pic nov. 2022 — « the sixth time zone (8 days)… coincides with the December low. The seventh time zone (13 days) coincides with the January 2022 low, the ninth time [zone] (34 days) coincides with the March high, and the 10th time zone (55 days) coincides with the June 2022 low. »
**TRADEX-AI C1** : illustration de coïncidences zone/tournant ; usage en confirmation temporelle.
*Catégorie : timing*

---

### D1801 — Exemple QQQ : zones sans signification (faux positifs temporels)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md, image_02) : « The eighth time zone (21 days) occurred in the middle of a downtrend and was insignificant. »
**TRADEX-AI C3** : toutes les zones ne marquent pas un tournant — preuve de faux positifs ; confirmation requise.
*Catégorie : gestion_risque_entree*

---

### D1802 — Extension future (Extra Bars) pour voir la prochaine zone
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md, image_03) : « you can add "extra bars" to view future Fibonacci Time Zones. The next Fibonacci Time Zone comes at the 89-day mark… 60 extra bars were added to display the next Fibonacci Time Zone. »
**TRADEX-AI C1** : nécessité d'extrapoler temporellement pour anticiper la prochaine zone — paramètre de projection.
*Catégorie : timing*

---

### D1803 — Question ouverte sur l'efficacité prédictive (QQQ 89 jours)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « Will the 89-day Fibonacci time zone mark a significant high or low? » (question laissée ouverte par la source).
🔴 NON VÉRIFIÉ : la source ne tranche pas l'issue de cette projection — efficacité prédictive non démontrée pour ce cas.
**TRADEX-AI C3** : pas de preuve d'efficacité ; à traiter comme alerte, non comme signal. Confirmation/prudence.
*Catégorie : gestion_risque_entree*

---

### D1804 — Exemple Euro FXE : tolérance temporelle requise
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md, image_04) : FXE depuis le pic avril 2008 — « The 8th Fibonacci Time Zone (21 days) marked a top in July, the 34-day line didn't mark anything significant, and the 55-day line marked a significant low… As with most forecasting and cycle tools, a little leeway is required, especially when the lengths grow longer. »
**TRADEX-AI C3** : tolérance (leeway) nécessaire autour des zones, croissante avec l'horizon — paramètre de fenêtre temporelle.
*Catégorie : timing*

---

### D1805 — Exemple Euro FXE : projection lointaine (233, puis 377)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md, image_05) : « 50 days were added to this chart to see the next Fibonacci Time Zone [at 233]. After 233, the next line would be at day 377, which means the chart would need around 330 extra days for viewing. »
**TRADEX-AI C1** : contrainte pratique — les zones lointaines exigent de larges extensions de barres.
*Catégorie : timing*

---

### D1806 — Nature « zones » : potentiels, pas points durs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « They are not hard reversal points but *potential* reversal points to watch as prices approach this zone. Fibonacci Time Zones provide a cross between cycle analysis and Fibonacci analysis. »
**TRADEX-AI C1** : croisement analyse cyclique × Fibonacci ; statut d'alerte temporelle.
*Catégorie : timing*

---

### D1807 — Confirmation par d'autres outils à l'approche d'une zone
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : « As these reversal points approach, chartists should turn to other aspects of technical analysis to confirm the reversal. This could be a bullish or bearish pattern, candlesticks, indicators or clues from the price chart itself. »
**TRADEX-AI C3** : confirmation multi-outils obligatoire — cohérent avec la règle 3/4 + 2/3 alignés. Confirmation.
*Catégorie : gestion_risque_entree*

---

### D1808 — Procédure d'ajout dans SharpCharts
🟡 CONVENTION (Source : fibonacci_time_zones.md, image_06, image_07) : « Select the **Annotate** button > Line Study tool > Fibonacci Time Zone » depuis un point bas/haut significatif.
**TRADEX-AI C1** : procédure outil (StockCharts) — informatif pour comprendre l'ancrage, non transposable tel quel à NT8.
*Catégorie : timing*

---

### D1809 — Précision limitée (FAQ)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : FAQ — « While they offer valuable insights, they aren't always pinpoint accurate. They serve as potential indicators rather than certainties. » et « No, they are zones indicating potential reversals. Other technical analysis aspects should be used in conjunction to confirm reversals. »
**TRADEX-AI C3** : garde-fou — précision non garantie ; jamais en signal autonome. Confirmation.
*Catégorie : gestion_risque_entree*

---

### D1810 — Synthèse : construction récursive et usage en confirmation temporelle
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_time_zones.md) : FAQ — « Starting from 0 and 1, each subsequent number is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8…). » Les zones marquent « expected intervals where price reversals might occur, offering traders potential entry or exit points. »
**TRADEX-AI C1** : récapitulatif décisionnel — outil de timing complémentaire (alerte), à confirmer par le prix/order flow avant toute entrée.
*Catégorie : timing*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1791 → D1810 (20) |
| Images certifiées | 7/7 (dont image_01 en .jpg) |
| Tags dominants | 🟢 littéral · 🔵 ÉCOLE Fibonacci · 🟡 CONVENTION (D1799, D1808) · 🔴 NON VÉRIFIÉ (D1803) · ⚫🔴 écho COG 0,618 (D1792, D1794) |
| Cercles TRADEX | C1 (timing/structure) · C3 (confirmation : D1801, D1803, D1807, D1809) |
| Catégories | timing · gestion_risque_entree |
| Actifs cibles | GC · HG · CL · ZW |
| Cas à vérifier | D1803 (🔴 efficacité prédictive 89-jours non tranchée par la source) ; D1799 & D1808 (🟡 interprétation barres/périodes & procédure SharpCharts → adaptation NT8 à valider) ; ⚫🔴 écho COG = arbitrage humain, NE PAS fusionner comme équivalence Belkhayate |

> ⚠️ Outil éducatif (StockCharts ChartSchool) · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
