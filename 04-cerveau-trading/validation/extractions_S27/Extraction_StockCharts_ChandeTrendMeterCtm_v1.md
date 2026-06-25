# Extraction StockCharts — Chande Trend Meter (CTM)
**Source :** `bundles/stockcharts/chande_trend_meter_ctm.md` (HTTP 200 · ~4 500 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 1/1 certifiée
**Décisions :** D1191 → D1199 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chande-trend-meter-ctm
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Using CTM With SharpCharts | Using CTM With SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1191 — Nature et origine du Chande Trend Meter
🔵 **ÉCOLE (Chande)** (Source : chande_trend_meter_ctm.md) : Le Chande Trend Meter (CTM), développé par Tushar Chande, attribue à un actif un score numérique basé sur plusieurs indicateurs techniques différents couvrant six timeframes différents. Distiller toute cette information technique en un seul nombre fournit un moyen simple d'identifier la force de la tendance d'un actif.
**TRADEX-AI C1** : Indicateur composite de force de tendance candidat comme feature unique synthétique pour qualifier l'état tendanciel de GC/HG/CL/ZW ; jamais déclencheur d'ordre seul.
*Catégorie : indicateurs_tendance*

---

### D1192 — Composition du calcul (indicateurs sous-jacents)
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Le calcul du CTM repose sur :
- la position des high/low/close relativement aux Bollinger Bands sur quatre timeframes (20, 50, 75 et 100 jours) ;
- la variation de prix relative à l'écart-type (standard deviation) sur les 100 derniers jours ;
- la valeur du RSI 14 jours ;
- l'existence de cassures de canal de prix (price channel breakouts) court terme à 2 jours.
Le score résultant est converti sur une échelle 0-100 pour faciliter la comparaison.
**TRADEX-AI C1** : Recette composite documentée mais la pondération exacte n'est pas divulguée (cf. À vérifier) ; reproductible seulement partiellement. Mélange Bollinger + écart-type + RSI + breakout = agrégat multi-horizon.
*Catégorie : indicateurs_tendance*

---

### D1193 — Échelle 0-100 et signification des extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Sur l'échelle CTM de 0 à 100, un score de 100 indique une tendance haussière très forte ; un score de 0 indique une tendance baissière très forte.
**TRADEX-AI C1** : Feature continue normalisée 0-100 directement exploitable comme niveau de force de tendance (haut = bull fort, bas = bear fort).
*Catégorie : indicateurs_tendance*

---

### D1194 — Cinq niveaux de force de tendance
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : L'échelle se divise en 5 niveaux :
- 90-100 : tendances haussières très fortes ;
- 80-90 : tendances haussières fortes ;
- 60-80 : tendances haussières faibles ;
- 20-60 : plat ou tendances baissières faibles ;
- 0-20 : tendances baissières très fortes.
**TRADEX-AI C1** : Grille de seuils discrétisant la force de tendance, codable en classifieur 5 classes ; utile comme état de marché en amont des déclencheurs.
*Catégorie : structure_marche*

---

### D1195 — Règle opératoire momentum (seuil 80)
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Les traders momentum devraient chercher des actifs avec un score CTM de 80 ou plus, ce qui indique une tendance haussière forte. Plus la tendance haussière est forte, plus elle est susceptible de se poursuivre.
**TRADEX-AI C1** : Seuil 80 = filtre de tendance haussière forte exploitable comme condition de cohérence (n'autorise pas un long seul, mais peut bloquer/valider). Symétrie baissière implicite (≤ 20) non détaillée par la source côté short.
*Catégorie : signal*

---

### D1196 — Usage sur indices/ETF et échelle absolue
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Le CTM peut aussi être utilisé sur des indices et ETF pour évaluer la tendance relative de secteurs, industries ou marchés entiers. Avantage : la valeur est fixée sur une échelle absolue, pas relative aux autres actifs d'un groupe ; comparer les scores CTM de plusieurs types d'actifs permet des comparaisons « apples-to-apples ».
**TRADEX-AI C4 / C7** : Échelle absolue → comparabilité inter-actifs (GC vs HG vs CL vs ZW) et inter-marchés (ES, DX) sans renormalisation ; utile pour une lecture macro/corrélations de force relative.
*Catégorie : indicateurs_tendance*

---

### D1197 — Synthèse opératoire (The Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Le CTM fournit un moyen simple de déterminer si un actif est en uptrend ou downtrend et de jauger la force de cette tendance. En combinant plusieurs indicateurs de tendance éprouvés réduits à un seul nombre, il donne au chartiste une richesse d'information sur la tendance d'un coup d'œil.
**TRADEX-AI C1** : Confirme le rôle de feature agrégée « force de tendance » ; positionnement amont (état) et non déclencheur.
*Catégorie : indicateurs_tendance*

---

### D1198 — Affichage SharpCharts et code couleur des niveaux
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md, image_01) : Le CTM se trouve dans la section Indicators sous le graphique ; il peut être positionné au-dessus, en dessous ou derrière le tracé du prix. Au-dessus/en dessous, l'arrière-plan est codé par couleur selon la force :
- Vert foncé : 90-100 (uptrend très fort) ;
- Vert moyen : 80-90 (uptrend fort) ;
- Vert clair : 60-80 (uptrend faible) ;
- Jaune : 20-60 (plat / downtrend faible) ;
- Rose : 0-20 (downtrend fort).
**TRADEX-AI C1** : Mapping couleur ↔ niveau (UI StockCharts) ; transposable en palette d'affichage du dashboard TRADEX pour visualiser l'état de tendance. Cohérent avec la grille D1194.
*Catégorie : configuration*

---

### D1199 — Scans suggérés CTM (croisement 60 sur volume + CTM persistant ≥ 80)
🟢 **FAIT VÉRIFIÉ** (Source : chande_trend_meter_ctm.md) : Deux scans fournis :
1. « CTM croise au-dessus de 60 sur volume lourd » :
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Chande Trend Meter x 60.0]
AND [volume > SMA(50,volume) * 1.5]
```
2. « CTM constamment élevé » (moyenne ≥ 80 sur 50 jours) :
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 20]
AND [SMA(50,Chande Trend Meter) > 80.0]
```
**TRADEX-AI C1** : Logiques transposables — (a) « CTM franchit 60 + volume × 1,5 » = sortie de zone neutre confirmée par volume ; (b) « moyenne CTM 50 j ≥ 80 » = tendance haussière durable. Syntaxe propre à StockCharts (non réutilisable telle quelle), seule la logique compte.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1191 | Nature et origine CTM | 🔵 ÉCOLE | C1 | indicateurs_tendance |
| D1192 | Composition du calcul | 🟢 | C1 | indicateurs_tendance |
| D1193 | Échelle 0-100 / extrêmes | 🟢 | C1 | indicateurs_tendance |
| D1194 | Cinq niveaux de force | 🟢 | C1 | structure_marche |
| D1195 | Règle momentum seuil 80 | 🟢 | C1 | signal |
| D1196 | Usage indices/ETF / échelle absolue | 🟢 | C4 | indicateurs_tendance |
| D1197 | Synthèse opératoire | 🟢 | C1 | indicateurs_tendance |
| D1198 | Affichage / code couleur SharpCharts | 🟢 | C1 | configuration |
| D1199 | Scans CTM (60+volume / ≥80 persistant) | 🟢 | C1 | signal |

**Liens Belkhayate :** le Chande Trend Meter n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué. Rapprochement fonctionnel possible (non affirmé par Belkhayate) : son rôle de jauge de force de tendance recoupe la lecture « Direction » de la méthode, mais reste un agrégat indépendant. Ne rien inventer.

**À vérifier (humain) :**
- D1192 — la pondération exacte combinant Bollinger (4 TF) + écart-type + RSI 14 + breakout 2 j n'est PAS divulguée par la source ; le CTM n'est donc PAS reproductible à l'identique sans la formule propriétaire de Chande. Statut proche d'un [RECONSTRUCTION] si on tente de le recoder.
- D1195 — la source détaille le seuil haussier (≥ 80) mais ne formalise pas explicitement le pendant short (≤ 20) comme « règle trader » ; ne pas inventer un seuil short symétrique sans validation.
- D1199 — l'opérateur de scan « Chande Trend Meter x 60.0 » est une syntaxe StockCharts ; seule la logique (franchissement de 60 + confirmation volume) est transposable.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
