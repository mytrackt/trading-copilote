# Extraction StockCharts — Advance-Decline Line (AD Line)
**Source :** `bundles/stockcharts/advance_decline_line.md` (HTTP 200 · ~7 100 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 7/7 certifiées · 0 à vérifier
**Décisions :** D491 → D500 · **Page :** chartschool.stockcharts.com/.../market-indicators/advance-decline-line
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **PERTINENCE LIMITÉE FUTURES** : l'AD Line est un indicateur de **BREADTH (largeur de marché ACTIONS)** construit sur le nombre d'actions montantes vs descendantes d'une bourse (NYSE, Nasdaq…). Son univers natif = des milliers d'actions individuelles. Les actifs TRADING de TRADEX-AI (GC·HG·CL·ZW) sont des **futures isolés** : il n'existe PAS de breadth pour un contrat unique. L'AD Line ne peut donc alimenter QUE la couche CONFIRMATION via l'indice actions ES (santé du marché actions S&P 500) — cercle **C5 (sentiment/participation)** —, jamais un signal direct sur les matières premières. Aucun lien Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | Spreadsheet 1 | Calculating the AD Line | D492 |
| image_02 | Breadth AD Line - Chart 1 | Calculating the AD Line | D492 |
| image_03 | Breadth AD Line - Chart 2 | Bullish Divergence | D495 |
| image_04 | Breadth AD Line - Chart 3 | Bearish Divergence | D496 |
| image_05 | Breadth AD Line - Chart 4 | Quirks | D497 |
| image_06 | Breadth AD Line - Chart 5 | Applying in SharpCharts | D499 |
| image_07 | Breadth AD Line - Chart 6 | Applying in SharpCharts | D499 |

---

## DÉCISIONS

### D491 — AD Line : définition et nature (breadth, Net Advances cumulés)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : L'Advance-Decline Line (AD Line) est un **indicateur de breadth** basé sur les **Net Advances** = nombre d'actions montantes MOINS nombre d'actions descendantes. Net Advances est positif quand les hausses dépassent les baisses, négatif sinon. L'AD Line est une **mesure cumulative** des Net Advances : elle monte quand Net Advances est positif, descend quand il est négatif.
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : L'AD Line d'un indice doit **confirmer** une avance ou un déclin par des mouvements similaires. Des **divergences haussières ou baissières** dans l'AD Line signalent un changement de participation pouvant préfigurer un retournement.
**TRADEX-AI C5** : Brique participation/breadth du marché ACTIONS. *Pertinence limitée futures* : applicable uniquement via l'indice ES (S&P 500) en couche CONFIRMATION ; aucun équivalent pour un future isolé (GC/HG/CL/ZW). Ne jamais générer d'ordre sur matière première à partir d'une AD Line.
*Catégorie : structure_marche*

---

### D492 — Calcul : valeur précédente + Net Advances courant (point de départ arbitraire)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md, image_01, image_02) : Formule = `AD Line (valeur précédente) + Net Advances (valeur courante)`. La première valeur est simplement Net Advances d'une période ; les suivantes ajoutent Net Advances courant à l'AD Line de la veille.
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : La valeur absolue de l'AD Line **dépend du point de départ** du calcul (arbitraire). Quel que soit ce point, la **forme** de la courbe sur une même période est identique : « **La forme et la direction de l'AD Line sont importantes, pas la valeur absolue.** »
**TRADEX-AI C5** : Indicateur à lire en **forme/pente/divergence**, jamais en niveau absolu. Tout codage doit comparer la direction de l'AD Line (ES) à celle de l'indice, pas un seuil chiffré.
*Catégorie : indicateurs_tendance*

---

### D493 — Ce que l'AD Line mesure : degré de participation
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : L'AD Line mesure le **degré de participation** à une avance ou un déclin. Une AD Line qui monte et inscrit de nouveaux sommets EN MÊME TEMPS que l'indice = participation forte = **haussier**. Une AD Line qui ne suit pas le rythme de l'indice et ne confirme pas les nouveaux sommets = **participation qui se rétrécit**.
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : La force du marché est **minée** quand moins d'actions participent à une avance ; ce rétrécissement s'identifie souvent par une **divergence baissière** entre l'AD Line et l'indice.
**TRADEX-AI C5** : Mesure de « largeur » de la santé du marché actions (ES). Une avance de l'ES non confirmée par l'AD Line = signal de fragilité macro à intégrer en pondération CONFIRMATION, jamais en déclencheur sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D494 — Côté baissier : confirmation des nouveaux creux et divergence haussière
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : Le marché est jugé **faible** quand l'AD Line inscrit de nouveaux creux EN MÊME TEMPS que l'indice (participation large au déclin). Une **divergence haussière** se forme quand l'AD Line **ne fait PAS** un creux plus bas alors que l'indice le fait : moins d'actions baissent et le déclin de l'indice pourrait approcher de sa fin.
**TRADEX-AI C5** : Détecter le tarissement de la participation baissière (ES) comme signe de fin de déclin macro possible — élément contextuel de confiance, subordonné à la price action sur les futures tradés.
*Catégorie : signal*

---

### D495 — Divergence haussière (exemple NYSE AD Line vs NYSE Composite)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md, image_03) : Comme la NYSE AD Line repose sur les statistiques advance-decline du NYSE, on la compare logiquement au **NYSE Composite**. Une divergence haussière s'est formée en juin-juillet 2009 : le NYSE Composite est passé sous son creux de juin tandis que la NYSE AD Line faisait un **creux plus haut** ; elle a préfiguré un creux important en juillet 2009 (l'indice a ensuite avancé de plus de 10 % du creux de juillet au sommet d'août).
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : De plus grandes divergences haussières ont été observées (oct. 2002→mars 2003 ; mai 2004→août 2004), préfigurant des creux importants du marché.
**TRADEX-AI C5** : Règle d'appariement = comparer l'AD Line à l'indice DE SA bourse (NYSE AD Line ↔ NYSE Composite). Pour TRADEX-AI, l'analogue serait AD Line NYSE/SP500 ↔ ES. *Pertinence limitée futures* : informe le contexte actions, pas l'or/cuivre/pétrole/blé.
*Catégorie : signal*

---

### D496 — Divergence baissière (exemple 2007 → bear market 2008)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md, image_04) : De juin à novembre 2007, deux divergences baissières dans la NYSE AD Line : le NYSE Composite a fait de nouveaux sommets en juillet puis octobre, mais l'AD Line a culminé début juin et a formé des **sommets plus bas** (breadth ne confirme pas l'indice). Cette série de divergences baissières a **préfiguré la rupture de support de janvier et le bear market de 2008**.
**TRADEX-AI C5** : Cas d'école = breadth qui décroche avant un retournement majeur du marché actions. Utiliser comme signal d'alerte macro de **réduction de risque** (couche CONFIRMATION), jamais comme ordre vendeur direct sur une matière première.
*Catégorie : signal*

---

### D497 — Quirk 1 : Nasdaq AD Line biaisée à la baisse (délistages)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md, image_05) : La **Nasdaq AD Line peut chuter durablement même si le Nasdaq monte**, car les exigences de cotation du Nasdaq sont moins strictes que celles du NYSE : beaucoup de valeurs (biotech, tech, énergies alternatives) à fort potentiel mais aussi à risque d'échec. Les sociétés en faillite sont retirées et remplacées, mais **leur effet négatif sur l'AD Line demeure**. Exemple : Nasdaq AD Line en baisse alors que le Nasdaq avançait de 2010 à 2012.
**TRADEX-AI C5** : Garde anti-faux-signal — une AD Line **dépend de la bourse** et de ses règles de cotation (biais structurel Nasdaq). Si jamais intégrée, privilégier la NYSE AD Line ; ne jamais comparer une AD Line à un indice d'une autre bourse.
*Catégorie : structure_marche*

---

### D498 — Quirk 2 : biais small/mid-cap (« le grand égalisateur »)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : Les statistiques advance-decline **favorisent les small et mid-caps** : la grande majorité des milliers d'actions du NYSE/Nasdaq sont small/mid-cap. Quels que soient capitalisation ou volume, une hausse compte **+1** et une baisse **-1**. Une hausse d'ExxonMobil (capi > 200 Md$) compte autant qu'une hausse de Teco Energy (capi < 5 Md$) : « **l'AD Line est le grand égalisateur** ».
**TRADEX-AI C5** : L'AD Line pondère chaque action également (1 action = 1 vote), donc reflète la **largeur** et non la capitalisation — complémentaire d'un indice cap-pondéré (ES) qui, lui, est dominé par les méga-caps. Lecture conjointe = détection des divergences participation vs prix.
*Catégorie : structure_marche*

---

### D499 — Synthèse interprétative + paramétrage SharpCharts (référence)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_line.md) : « Bottom line » — l'AD Line reflète la participation : avance large = force sous-jacente (haussier) ; avance étroite = marché mitigé/sélectif. La participation étroite installe les **signaux de divergence** (une avance étroite ne tient pas le rythme de l'indice → divergence baissière ; un déclin avec peu d'actions participantes → divergence haussière), aidant à identifier des retournements potentiels de l'indice.
🔵 **ÉCOLE** (Source : advance_decline_line.md, image_06, image_07) : Dans SharpCharts, l'AD Line se crée pour Amex, Vancouver, Nasdaq, NYSE ou Toronto : saisir le symbole de Net Advances de l'indice voulu, passer le type de graphique en « **cumulative** », cliquer « update ». On peut superposer l'indice sous-jacent (ex. NYSE Composite en gris derrière l'AD Line), ajouter une SMA, afficher Net Advances en histogramme.
**TRADEX-AI C0/C5** : Référence de config — l'AD Line est un graphe **cumulatif** d'un flux Net Advances externe (donnée bourse, hors NT8/ATAS). Si exposée, la rattacher à l'indice ES en CONFIRMATION, en mode forme/divergence.
*Catégorie : indicateurs_tendance*

---

### D500 — Rattachement TRADEX-AI : breadth actions, hors univers futures, hors Belkhayate
⚫🔴 **PROPRIÉTAIRE / NON VÉRIFIÉ (rattachement TRADEX-AI)** : La source décrit un indicateur de **breadth d'actions** ; elle n'établit **aucun lien avec la méthode Belkhayate** (ni Énergie/MFI, ni pivots, ni BGC) ni avec les futures matières premières. Construire une « AD Line » pour GC/HG/CL/ZW est **impossible** (pas de population d'actions sous-jacentes pour un contrat unique).
🟡 **CONVENTION** : Seul usage légitime dans TRADEX-AI = AD Line d'un indice actions (NYSE / S&P 500) comme **proxy de santé/participation du marché actions**, branchée sur l'actif de CONFIRMATION **ES**, en lecture divergence avec l'indice. Jamais comme composante d'un signal d'entrée sur une matière première, jamais comme « indicateur Belkhayate ».
**TRADEX-AI C5** : Statut = donnée de contexte macro/participation, pondération faible, couche CONFIRMATION exclusivement. *Pertinence limitée futures confirmée.*
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D491 → D500 (10) |
| Images certifiées citées | 7/7 |
| Catégories utilisées | structure_marche · signal · indicateurs_tendance |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · ⚫🔴 (rattachement) |
| Cercle dominant | **C5 (participation/sentiment)** — couche CONFIRMATION via ES uniquement |
| Pertinence futures GC/HG/CL/ZW | **LIMITÉE / INDIRECTE** — breadth = univers d'actions ; aucun équivalent pour un future isolé. Applicable seulement au marché actions (ES), pas aux matières premières. |
| Belkhayate | **NON CONCERNÉ** — aucun lien affirmé par la source (D500) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
