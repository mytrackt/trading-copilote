# Extraction StockCharts — Volume-by-Price

**Source :** `bundles/stockcharts/volume_by_price.md` (HTTP 200) + 13 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 13/13 certifiées · 0 à vérifier
**Décisions :** D239 → D248 · **Page :** chartschool.stockcharts.com/.../technical-overlays/volume-by-price
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page PRIORITAIRE — Volume-by-Price = profil de volume horizontal (volume échangé par zone de prix). C'est une brique **order flow / structure de marché (C2)** : identification de support/résistance par concentration de volume, et signaux de cassure de barres longues. À ne PAS confondre avec un profil de volume order-flow intra-barre (ATAS) : ici le calcul repose sur les **clôtures** uniquement, pas sur le footprint tick-par-tick.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Calculating Volume-by-Price (section-fallback) | Calculating Volume-by-Price | D240 |
| image_02 | Calculating Volume-by-Price (section-fallback) | Calculating Volume-by-Price | D240 |
| image_03 | Calculating Volume-by-Price (section-fallback) | Calculating Volume-by-Price | D241 |
| image_04 | Nuances (section-fallback) | Nuances | D243 |
| image_05 | Identifying Support Using Volume-by-Price (section-fallback) | Identifying Support | D244 |
| image_06 | Identifying Support Using Volume-by-Price (section-fallback) | Identifying Support | D244 |
| image_07 | Identifying Resistance Using Volume-by-Price (section-fallback) | Identifying Resistance | D245 |
| image_08 | Identifying Resistance Using Volume-by-Price (section-fallback) | Identifying Resistance | D245 |
| image_09 | Identifying Support Breaks (section-fallback) | Identifying Support Breaks | D246 |
| image_10 | Identifying Support Breaks (section-fallback) | Identifying Support Breaks | D246 |
| image_11 | Identifying Resistance Breaks (section-fallback) | Identifying Resistance Breaks | D247 |
| image_12 | Identifying Resistance Breaks (section-fallback) | Identifying Resistance Breaks | D247 |
| image_13 | Using with SharpCharts (section-fallback) | Using with SharpCharts | D248 |

---

## DÉCISIONS

### D239 — Volume-by-Price : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md) : Volume-by-Price est un outil graphique qui montre le **volume échangé pour une plage de prix donnée, sur la base des prix de clôture**. Les barres sont **horizontales**, affichées à gauche du graphique en regard des plages de prix. Elles peuvent être en une seule couleur ou en deux couleurs (séparant up volume et down volume). En combinant volume et clôtures, les barres identifient les **plages de prix à fort volume** qui marquent support ou résistance. StockCharts affiche **12 barres par défaut** (ajustable).
**TRADEX-AI C2** : Profil de volume horizontal = brique de structure de marché basée volume ; sert à localiser les zones support/résistance à fort volume sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D240 — Calcul : 4 étapes, fondé sur les clôtures et la période affichée
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_01, image_02) : Le calcul repose sur **toute la période affichée à l'écran** (un chart daily 5 mois → 5 mois de clôtures daily ; un chart 30 min 2 semaines → 2 semaines de clôtures 30 min). Quatre étapes : (1) trouver la high-low range des clôtures sur toute la période ; (2) diviser cette range par 12 pour créer **12 zones de prix égales** ; (3) totaliser le volume échangé dans chaque zone ; (4) optionnellement séparer volume positif/négatif. Le **negative volume** d'une zone = somme du volume des down days dans cette zone ; **positive volume** = total du volume des up days.
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_02) : Exemple Nasdaq 100 ETF (12 avr.–15 sept. 2010) : clôtures de 40,32 $ à 47,87 $ (range 7,55) ; 110 clôtures triées et réparties en 12 zones égales (7,55/12 = 0,6292 par zone).
**TRADEX-AI C2/C0** : Calcul déterministe répliquable côté export NinjaScript (besoin clôtures + volume + bornage de la fenêtre temporelle) ; défaut = 12 zones, fenêtre = période visible.
*Catégorie : structure_marche*

---

### D241 — Séparation volume positif / négatif (vert / rouge)
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_03) : Les barres Volume-by-Price représentent le volume total par zone de prix ; ce volume peut être séparé en positif et négatif, affiché respectivement en **vert (demande)** et **rouge (offre)** pour distinguer la pression dominante dans chaque zone.
**TRADEX-AI C2** : Décomposition vert/rouge = proxy de pression nette demande/offre par zone ; à exposer pour qualifier la robustesse d'un support (vert dominant) ou d'une résistance (rouge dominant) sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D242 — Interprétation : support sous le prix, résistance au-dessus
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md) : Les zones à fort volume reflètent un intérêt élevé qui influence l'offre/demande future (résistance ou support). Une **longue barre sous le prix** est à surveiller comme **support potentiel** lors d'un pullback ; une **longue barre au-dessus du prix** comme **résistance potentielle** lors d'un rebond.
**TRADEX-AI C2** : Règle de lecture du profil — mapper les barres longues en niveaux S/R selon leur position relative au prix courant ; alimente la grille de score (zone de prix probable de réaction).
*Catégorie : structure_marche*

---

### D243 — Nuances : ne pas valider du support/résistance PASSÉ + gaps = barres nulles
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_04) : Les barres courantes **ne doivent PAS servir à valider des niveaux de support/résistance passés**, car l'indicateur est calculé sur l'ensemble des données prix-volume affichées (ex. 6 mois de janvier à juin). Une barre semblant marquer un support en mars contient en réalité des données qui s'étendent jusqu'en juin. Par ailleurs, **les gros gaps produisent des barres égales à zéro** (aucune clôture dans la zone de prix concernée).
**TRADEX-AI C2** : Garde anti-biais — le profil n'a de valeur que pour le support/résistance **présent ou futur**, pas pour confirmer rétroactivement un niveau ; traiter les zones vides (gaps) comme absence de référence, pas comme cassure.
*Catégorie : structure_marche*

---

### D244 — Identifier un SUPPORT via Volume-by-Price
🔵 **ÉCOLE** (Source : volume_by_price.md, image_05, image_06) : Exemple Netflix (NFLX) — Volume-by-Price identifie un support vers 95–100 $ fin juin (la barre la plus longue). NFLX entrant en pullback, on projette ce support pour le futur proche ; le titre s'y est retourné fin juillet, et le volume a bondi en août pour **valider le retournement sur support**.
**TRADEX-AI C2/C3** : La barre de volume la plus longue sous le prix = candidate support prioritaire ; n'armer le signal qu'avec confirmation (surge de volume au retournement) sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D245 — Identifier une RÉSISTANCE via Volume-by-Price
🔵 **ÉCOLE** (Source : volume_by_price.md, image_07, image_08) : Exemple TE Connectivity (TEL) — Volume-by-Price identifie une résistance vers 26–26,5 $ début août (2ᵉ barre la plus longue). La cassure d'avril n'est PAS un vrai breakout car le calcul courant s'étend de janvier à début août (rappel D243). Le titre échoue finalement à la résistance.
**TRADEX-AI C2/C3** : La barre longue au-dessus du prix = candidate résistance ; pondérer un signal de vente / prise de profit à son approche, sans la traiter comme cassure validée tant que le contexte temporel n'est pas levé, sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D246 — Cassure de support (break below) = pression vendeuse
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_09, image_10) : Une **cassure SOUS une longue barre** Volume-by-Price signale une hausse de l'offre / pression vendeuse pouvant préfigurer des prix plus bas. Exemple SanDisk (SNDK) : longue barre = support 39–43 $ mi-août (≥ 3 reaction lows vers 42), puis cassure sous cette zone **avec volume élevé** → la demande s'effondre, l'offre l'emporte, prix nettement plus bas.
**TRADEX-AI C2/C3** : Signal de continuation baissière — cassure d'une barre longue support **confirmée par un volume élevé** sur GC/HG/CL/ZW ; sans expansion de volume, traiter avec prudence.
*Catégorie : signal*

---

### D247 — Cassure de résistance (break above) = demande renforcée
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_11, image_12) : Une **cassure AU-DESSUS d'une longue barre** signale une hausse de la demande pouvant préfigurer des prix plus hauts (les barres longues au-dessus marquent un supply overhang que la demande surmonte). Exemple McDonald's (MCD) : barre longue = offre 60–61 $, résistance 61–62 $ ; combinaison price action + Volume-by-Price (triangle symétrique possible) ; cassure de la résistance en juillet → nouveaux sommets en août.
🟡 **CONVENTION** : Combiner price action ET Volume-by-Price pour délimiter les zones (la source le formule explicitement : « chartists need to combine price action and Volume-by-Price »).
**TRADEX-AI C2/C3** : Signal de continuation haussière — cassure au-dessus d'une barre longue résistance, confirmée par structure price action, sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D248 — Bottom line + paramétrage + confirmation multi-outil
🟢 **FAIT VÉRIFIÉ** (Source : volume_by_price.md, image_13) : Volume-by-Price est **le mieux adapté à l'identification du support/résistance présent ou futur** : support potentiel quand le prix est au-dessus d'une barre longue, résistance potentielle quand il est en dessous. Les portions vertes longues (demande) valident un support, les rouges longues (offre) valident une résistance. Il est **important de confirmer ses constats avec d'autres indicateurs** — oscillateurs de momentum et chart patterns sont de bons compléments. Paramétrage SharpCharts : section « overlays », défaut **12 périodes** (ajustable), basé sur les clôtures (highs/lows omis → un spike peut n'avoir aucune barre), 1 couleur (sans « color volume ») ou 2 tons (avec), opacité réglable.
**TRADEX-AI C2/C3** : Guard permanent — un niveau Volume-by-Price ne déclenche jamais seul ; le croiser avec momentum (cf. MFI/RSI) et patterns. Référence config : défaut 12 barres, calcul sur barres clôturées.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D239 → D248 (10) |
| Images certifiées citées | 13/13 |
| Catégories utilisées | structure_marche · signal · configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Belkhayate | **NON concerné directement** — outil order flow / structure (C2) ; aucun rattachement Énergie. Lien éventuel BGC/zones Belkhayate non affirmé par la source (hypothèse projet, non posée ici). |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
