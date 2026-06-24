# Extraction StockCharts — Volume-Weighted Average Price (VWAP)
**Source :** `bundles/stockcharts/volume_weighted_average_price_vwap.md` (HTTP 200) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 10/10 certifiées · 0 à vérifier
**Décisions :** D199 → D210 · **Page :** chartschool.stockcharts.com/.../technical-overlays/volume-weighted-average-price-vwap
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page PRIORITAIRE. Le VWAP est un indicateur clé d'**order flow / prix moyen pondéré volume** (Cercle C2). Il fournit un repère intraday de valeur (cher/pas cher) et de qualité d'exécution pour les actifs TRADING GC/HG/CL/ZW. Aucun lien Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | What Is the Volume-Weighted Average Price? (section-fallback) | What Is the VWAP? | D199 |
| image_02 | VWAP calculation example for IBM | VWAP Formulas | D201 |
| image_03 | One-minute bars with VWAP on the IBM chart | VWAP Formulas | D201 |
| image_04 | VWAP compared with a 150-minute SMA at noon and a 390-minute SMA at close | VWAP vs. Moving Averages | D203 |
| image_05 | Example of flat VWAP line | Determining the Intraday Trend | D205 |
| image_06 | Example of rising VWAP line | Determining the Intraday Trend | D205 |
| image_07 | Example of falling VWAP line | Determining the Intraday Trend | D205 |
| image_08 | Using with SharpCharts (section-fallback) | Using with SharpCharts | D209 |
| image_09 | SharpCharts settings for the VWAP overlay | Using with SharpCharts | D209 |
| image_10 | Using with StockChartsACP (section-fallback) | Using with StockChartsACP | D209 |

---

## DÉCISIONS

### D199 — VWAP : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md, image_01) : Le Volume-Weighted Average Price (VWAP) est le **prix moyen pondéré par le volume**. Il égale la valeur en dollars de toutes les périodes de trading divisée par le volume total échangé pour la journée en cours. L'overlay VWAP est calculé à partir des **données intraday d'une seule journée de marché**, du début à la fin de la séance.
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Développé à l'origine par les investisseurs institutionnels pour placer de gros ordres sans perturber le marché ; utilisable aussi par les particuliers. La ligne VWAP fonctionne presque comme une **moyenne mobile d'une seule journée**.
**TRADEX-AI C2** : VWAP = repère intraday de prix moyen pondéré volume (order flow) pour GC/HG/CL/ZW ; brique « valeur relative » de la séance.
*Catégorie : indicateurs_tendance*

---

### D200 — VWAP : indicateur intraday uniquement (pas daily/weekly/monthly)
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Le VWAP traditionnel s'appuie sur les **données tick**. StockCharts propose un VWAP intraday basé sur des périodes intraday (1, 5, 10, 15, 30 ou 60 minutes). Le VWAP **n'est PAS défini** pour les périodes daily, weekly ou monthly du fait de la nature du calcul.
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Les données tick sont très gourmandes en ressources (titres actifs : 20–30 ticks/minute ; 390 minutes/séance → souvent plus de 5000 ticks/jour).
**TRADEX-AI C2** : Côté NinjaTrader, calculer le VWAP sur barres intraday (ou ticks réels) ; ne JAMAIS l'exposer sur un timeframe daily+ pour GC/HG/CL/ZW — garde anti-mauvais-usage.
*Catégorie : configuration*

---

### D201 — VWAP : formule de calcul (cumulative, reset à l'ouverture)
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md, image_02, image_03) : Formule = `Cumulative(Volume × Typical Price) / Cumulative(Volume)`. Cinq étapes — (1) `Typical Price = (H+L+C)/3` ; (2) multiplier le typical price par le volume de la période ; (3) total courant (cumulatif) de ces produits ; (4) total courant du volume (volume cumulatif) ; (5) diviser le cumul prix-volume par le cumul volume.
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : La **première valeur VWAP est toujours égale au typical price**, car le volume au numérateur et au dénominateur s'annule lors du premier calcul.
**TRADEX-AI C2** : Formule déterministe à répliquer côté export NinjaScript (besoin OHLCV + volume) ; **réinitialiser le cumul à chaque ouverture de séance**.
*Catégorie : indicateurs_tendance*

---

### D202 — VWAP : exemple chiffré IBM (volatilité des 30 premières minutes)
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md, image_02, image_03) : Sur l'exemple IBM (VWAP 1-minute, 30 premières minutes) les prix ont oscillé de 127,36 $ (plus haut) à 126,67 $ (plus bas) — séance volatile — tandis que le VWAP est resté dans une plage étroite de 127,21 à 127,09, au **milieu du range**.
**TRADEX-AI C2** : Illustration de la propriété de lissage du VWAP (il reste centré dans le range quand le prix oscille) ; utile comme repère de prix « équitable » intraday.
*Catégorie : indicateurs_tendance*

---

### D203 — VWAP vs moyenne mobile : comparaison de fenêtre correcte
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md, image_04) : Le VWAP se comporte comme une moyenne mobile mais n'utilise que les valeurs d'une seule journée : peu de points en début de séance, beaucoup à la clôture. La valeur VWAP 1-minute en fin de séance est souvent proche d'une **MM 390 minutes** (1 journée complète).
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : On ne peut PAS comparer le VWAP à une MM 390 minutes **en cours de séance** (la MM 390 inclurait des données de la veille). À 12h00 (150 minutes écoulées), il faut comparer le VWAP à une **MM 150 minutes**.
**TRADEX-AI C2** : Si comparaison VWAP↔MM utilisée dans le moteur, ajuster dynamiquement la fenêtre de la MM au nombre de minutes écoulées depuis l'ouverture — garde anti-comparaison-biaisée sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D204 — VWAP : nature retardée (lag) croissant au fil de la séance
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Comme les moyennes mobiles, le VWAP **retarde** le prix car il moyenne des données passées ; plus il y a de données, plus le lag est grand. Le VWAP est un **indicateur cumulatif** : le nombre de points augmente progressivement (IBM 1-min : 90 points à 11h00, 210 à 13h00, 390 à la clôture), donc le lag s'accroît au fil de la journée.
**TRADEX-AI C2** : Pondérer la réactivité attendue du VWAP selon l'heure de séance ; en fin de séance le VWAP est très inerte (à ne pas traiter comme signal rapide) pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D205 — Tendance intraday : prix vs VWAP (au-dessus / en dessous / plat)
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md, image_05, image_06, image_07) : En général, les prix intraday **baissent quand ils sont sous le VWAP** et **montent quand ils sont au-dessus**. Le VWAP se situe dans le range high-low quand le prix est sans tendance (range-bound). Exemples : MRK en range → VWAP plat ; GE en hausse → prix au-dessus du VWAP la plupart de la séance ; MSFT en baisse → prix sous le VWAP la plupart de la séance.
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : La direction de la ligne VWAP ET sa position relative aux barres de prix donnent des indices sur la tendance intraday. Les premières valeurs VWAP sont erratiques (peu de points accumulés).
**TRADEX-AI C2** : Filtre Python de biais intraday — prix > VWAP = biais haussier de séance, prix < VWAP = biais baissier ; ignorer les toutes premières barres (valeurs instables) sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D206 — VWAP : points de liquidité et entrée/sortie
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Le VWAP sert à identifier les **points de liquidité**. En tant que mesure de prix pondérée par le volume, il reflète les niveaux de prix pondérés par le volume, aidant les institutionnels à placer de gros ordres sans perturber le marché et à repérer les points de prix liquides / illiquides sur un horizon très court.
**TRADEX-AI C2** : Utiliser le VWAP comme repère de zones de liquidité intraday pour le timing d'entrée/sortie ; cohérent avec la logique order flow (ATAS) sur GC/HG/CL/ZW.
*Catégorie : timing*

---

### D207 — VWAP : mesure de la qualité d'exécution (good fill)
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Le VWAP mesure l'efficacité de trading. Un **ordre d'achat exécuté SOUS le VWAP** = bon remplissage (acheté sous le prix moyen). Un **ordre de vente exécuté AU-DESSUS du VWAP** = bon remplissage (vendu au-dessus du prix moyen).
**TRADEX-AI C2** : Benchmark d'exécution — après un fill sur GC/HG/CL/ZW, comparer le prix obtenu au VWAP pour scorer la qualité d'exécution (achat<VWAP / vente>VWAP = bon).
*Catégorie : gestion_risque_entree*

---

### D208 — Bottom line : VWAP = repère de valeur relative intraday
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Le VWAP est un point de référence des prix d'**une seule journée**, donc surtout adapté à l'**analyse intraday**. Prix **sous** le VWAP = relativement bas pour la journée/l'instant ; prix **au-dessus** = relativement haut. C'est un indicateur cumulatif : le nombre de points croît au fil de la journée, ce qui explique son lag croissant.
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Implicite tout au long de la page — le VWAP est un overlay de référence, pas un système de signal autonome (combiner avec tendance/structure).
**TRADEX-AI C2** : Guard — traiter le VWAP comme repère de valeur relative et de biais intraday, jamais comme déclencheur d'ordre isolé sur GC/HG/CL/ZW ; le combiner aux autres cercles.
*Catégorie : structure_marche*

---

### D209 — Implémentation / paramétrage (référence)
🔵 **ÉCOLE** (Source : volume_weighted_average_price_vwap.md, image_08, image_09, image_10) : VWAP disponible en overlay sur SharpCharts (period intraday + range « one day » ou « fill the chart ») et StockChartsACP (Chart Settings). L'overlay **ne prend aucun paramètre** sous ACP (seuls couleur/style sont réglables). Tracé sur plusieurs jours : le VWAP **saute** de sa clôture précédente au typical price de la nouvelle ouverture (nouveau cycle de calcul). La valeur VWAP est affichée dans la légende en haut à gauche.
🟡 **CONVENTION** : Le VWAP peut parfois « sortir » de l'échelle de prix du graphe (ex. VWAP 45,50 invisible sur un range 45,80–47) ; étendre le range à une journée complète pour le voir.
**TRADEX-AI C2** : Référence de paramétrage — VWAP reset par séance, sans paramètre numérique ; exposer choix période intraday (1/5/15/30/60 min) et range dans l'UI/config.
*Catégorie : configuration*

---

### D210 — Anchored VWAP : ancrage sur un événement significatif
🟢 **FAIT VÉRIFIÉ** (Source : volume_weighted_average_price_vwap.md) : Pour démarrer la ligne VWAP à une date/heure précise (plus haut/bas significatif, annonce de résultats, ou tout autre indicateur de changement de psychologie de marché), StockChartsACP propose l'**Anchored VWAP** : le VWAP est alors calculé uniquement à partir de l'action de prix postérieure à l'événement ancré.
**TRADEX-AI C2** : Variante Anchored VWAP intéressante pour caler le repère de valeur sur un swing/news majeur (NFP/FOMC/CPI déjà gérés par News Gate) sur GC/HG/CL/ZW ; à considérer en Phase C order flow.
*Catégorie : timing*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D199 → D210 (12) |
| Images certifiées citées | 10/10 |
| Catégories utilisées | indicateurs_tendance · configuration · timing · gestion_risque_entree · structure_marche |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Belkhayate | **NON CONCERNÉ** — aucun lien Belkhayate affirmé par la source ; VWAP = brique order flow / prix moyen pondéré volume (Cercle C2) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
