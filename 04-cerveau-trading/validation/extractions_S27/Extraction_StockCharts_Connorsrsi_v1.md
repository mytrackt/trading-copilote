# Extraction StockCharts — ConnorsRSI
**Source :** `bundles/stockcharts/connorsrsi.md` (HTTP 200 · ~7 700 car.) + 0 image certifiée
**Méthode images :** double ancrage v3 — manifest « À VÉRIFIER » : intégrité .md=1 figure vs HTML=2 images → alignement impossible. 0/2 certifiées (aucune image citée ; le texte reste exploitable).
**Décisions :** D1351 → D1370 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/connorsrsi
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (manifest : 0 certifiée · 2 à vérifier · désalignement .md=1 vs HTML=2 → aucune citée).

## DÉCISIONS

### D1351 — Origine et but du ConnorsRSI
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « ConnorsRSI is a momentum oscillator developed by Larry Connors and the team at Connors Research. It's used to identify overbought/oversold conditions in shorter trading timeframes. »
**TRADEX-AI C3** : Oscillateur de momentum propriétaire de l'école Connors, ciblant les timeframes courts (cohérent avec mode Rapide range bar / Scalping TRADEX). À traiter comme variante d'école, non comme standard universel.
*Catégorie : indicateurs_momentum*
---

### D1352 — Limite du RSI 14 classique en court terme
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The traditional 14-period RSI indicator developed by Welles Wilder reacts too slowly to be useful for short-term trading; Connors Research sought to improve on this indicator, making it more suitable for shorter timeframes. »
**TRADEX-AI C3** : Justification de l'école — le RSI(14) de Wilder est jugé trop lent pour le scalping. Argument d'école, pas un fait universel.
*Catégorie : indicateurs_momentum*
---

### D1353 — Étape intermédiaire RSI(2) et ses limites
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « They initially developed their RSI(2) strategy, which used a 2-period RSI and moved overbought/oversold levels out to 90 and 10, but this approach still resulted in more false signals than desired. »
**TRADEX-AI C3** : Historique — RSI(2) avec seuils 90/10 générait encore trop de faux signaux, d'où le composite. Contexte d'école.
*Catégorie : indicateurs_momentum*
---

### D1354 — Nature composite à trois mesures
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « ConnorsRSI combines the momentum measurement of RSI with components that measure the duration of the trend and the magnitude of the price change, to create a more reliable short-term RSI indicator. »
**TRADEX-AI C3** : Indicateur composite = momentum + durée de tendance + magnitude du changement de prix. Trois dimensions combinées en une note 0-100.
*Catégorie : indicateurs_momentum*
---

### D1355 — Formule de combinaison
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « ConnorsRSI(3,2,100) = (RSI(3) + RSI(Streak,2) + PercentRank(100)) / 3 ». « ConnorsRSI is calculated by taking the average of its three components. »
**TRADEX-AI C3** : Formule déterministe codable (niveau 1, 0$) : moyenne arithmétique des trois composants. Paramètres par défaut (3,2,100).
*Catégorie : indicateurs_momentum*
---

### D1356 — Composant 1 : RSI(3) de prix
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The first component is a simple 3-period RSI of price. This component measures price momentum on a scale of 0-100. »
**TRADEX-AI C3** : 1er composant = RSI 3 périodes du prix (momentum pur, 0-100). Réutilise le RSI standard déjà documenté KB.
*Catégorie : indicateurs_momentum*
---

### D1357 — Composant 2 : longueur de série (streak)
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The second component is a 2-period RSI of the up/down streak length. It measures the duration of the trend... the number of days in a row that the security's closing price has been higher (up) or lower (down) than the previous day's close. »
**TRADEX-AI C3** : 2e composant = RSI(2) appliqué à la série de clôtures consécutives haussières/baissières. Mesure la durée de la tendance.
*Catégorie : indicateurs_momentum*
---

### D1358 — Règle de calcul de la série (streak)
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « If a stock closes above its previous close three days in a row, then the up/down streak is +3. If it has closed below its previous close for 2 days, then its streak is -2. If it does not change price between one period and the next, then the streak is reset to 0. »
**TRADEX-AI C3** : Logique exacte du streak : +N clôtures up consécutives, -N clôtures down, reset à 0 si prix inchangé. Codable sans ambiguïté.
*Catégorie : indicateurs_momentum*
---

### D1359 — Composant 3 : rang de magnitude (PercentRank)
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The third component ranks the most recent period's price change against the price change of the other periods in the specified timeframe (100 periods by default)... if 7 of those 20 price change values are lower than today's price change, then 7 / 20 = 0.35 = 35%. »
**TRADEX-AI C3** : 3e composant = percentile de la variation du jour vs les N dernières variations (défaut 100). Grand mouvement positif → proche de 100 ; grand négatif → proche de 0.
*Catégorie : indicateurs_momentum*
---

### D1360 — Résultat borné 0-100 et paramètres recommandés
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « the three values are added together and divided by 3. The resulting ConnorsRSI value ranges between 0 and 100. Connors recommends parameters of 3, 2, and 100 for the three components, but these parameters can be adjusted to meet your trading needs. »
**TRADEX-AI C3** : Sortie bornée 0-100 (contrairement au CCI non borné). Paramètres recommandés (3,2,100) ajustables.
*Catégorie : configuration*
---

### D1361 — Usage principal : surachat/survente court terme
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The ConnorsRSI indicator is typically used to identify overbought and oversold conditions in shorter trading timeframes. »
**TRADEX-AI C3** : Usage cible = conditions extrêmes sur horizons courts. Adapté au mode Rapide/Scalping TRADEX.
*Catégorie : signal*
---

### D1362 — Seuils 90/10 (vs 70/30 du RSI classique)
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « While the traditional RSI typically defines 70 and 30 as the overbought and oversold levels, ConnorsRSI is more volatile and faster-moving, and requires more extreme levels to be set. Connors recommends using 90 and 10 for overbought/oversold levels... »
**TRADEX-AI C3** : Seuils par défaut 90 (surachat) / 10 (survente), plus extrêmes que le RSI classique car indicateur plus volatil.
*Catégorie : configuration*
---

### D1363 — Seuils 95/5 pour titres très volatils
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « For more volatile securities, some chartists even use 95 and 5. »
**TRADEX-AI C3** : Pour actifs très volatils (GC/CL), envisager 95/5 plutôt que 90/10. Paramètre à caler par actif.
*Catégorie : configuration*
---

### D1364 — Interprétation directionnelle des extrêmes
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « a security dropping below the oversold threshold indicates a buying opportunity, and a security rising above the overbought threshold indicates a pullback may be in its future. »
**TRADEX-AI C3** : Sous seuil bas = opportunité d'achat potentielle ; au-dessus seuil haut = repli possible. Logique mean-reversion.
*Catégorie : signal*
---

### D1365 — Extrême = signal d'examen rapproché (multi-facteurs)
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « Whenever a security reaches either extreme, it is a signal to look closely at technical conditions for that security, including trend, volume, and other indicators. »
**TRADEX-AI C7** : Un extrême ConnorsRSI déclenche une analyse multi-facteurs (tendance + volume + autres) — cohérent avec l'escalade niveau 2→3 TRADEX. Pas un signal autonome.
*Catégorie : signal*
---

### D1366 — RSI classique sature trop vite en court terme
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « Traditional RSI reaches extreme overbought/oversold levels very frequently when looking at shorter-term timeframes. »
**TRADEX-AI C3** : Constat motivant ConnorsRSI : le RSI standard atteint trop souvent les extrêmes en intraday → faible pouvoir discriminant.
*Catégorie : indicateurs_momentum*
---

### D1367 — Composants durée+magnitude rendent l'extrême plus fiable
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « The incorporation of components that measure the duration of the trend and the magnitude of the price change, as well as setting the overbought/oversold levels further out, help make ConnorsRSI more suitable for shorter-term trades. »
**TRADEX-AI C3** : L'ajout durée+magnitude + seuils éloignés = extrêmes plus rares mais plus fiables que le RSI nu en court terme.
*Catégorie : indicateurs_momentum*
---

### D1368 — Moins de signaux mais plus de qualité
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « Despite the increased volatility in short-term trading, ConnorsRSI typically generates fewer trading signals than traditional RSI for this timeframe. When ConnorsRSI reaches an extreme level, it is more likely to actually be overbought/oversold. »
**TRADEX-AI C3** : Compromis fréquence/qualité : moins de signaux mais probabilité plus élevée qu'un extrême soit réel. Favorable à un système sélectif.
*Catégorie : signal*
---

### D1369 — Faux signaux possibles + usage combiné obligatoire
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : « However, as with any indicator, it may occasionally produce false signals. As with all indicators, traders should use ConnorsRSI in conjunction with other indicators and analysis techniques. »
**TRADEX-AI C7** : Garde-fou — faux signaux possibles ; ne jamais l'utiliser seul. Combiner avec d'autres briques (cohérent règle 3/4 + 2/3 TRADEX).
*Catégorie : signal*
---

### D1370 — Scans surachat/survente avec filtre de tendance SMA200
🔵 **ÉCOLE Connors** (Source : connorsrsi.md) : Scan « ConnorsRSI Oversold in Uptrend » : `[Daily Close > Daily SMA(200,Daily Close)] AND [Daily ConnorsRSI(3,2,100) <= 10]` ; scan « Overbought in Downtrend » : `[Daily Close < Daily SMA(200,Daily Close)] AND [Daily ConnorsRSI(3,2,100) >= 90]`.
**TRADEX-AI C3** : Bonne pratique — coupler le signal extrême ConnorsRSI à un filtre de tendance majeure (SMA 200) : acheter la survente SEULEMENT en tendance haussière, vendre le surachat SEULEMENT en tendance baissière. Évite de contrer la tendance de fond.
*Catégorie : configuration*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1351 → D1370 (20 décisions) |
| Images certifiées | 0/2 (manifest « à vérifier » — désalignement .md=1 vs HTML=2 ; aucune image citée) |
| Cercle dominant | C3 (momentum) · renvois C7 (D1365, D1369) |
| Tags | 🔵 ÉCOLE Connors ×20 (indicateur propriétaire Larry Connors) |
| Catégories | indicateurs_momentum, configuration, signal |
| Actifs concernés | GC · HG · CL · ZW (applicable, surtout modes court terme) + ES/VX |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Paramètres clés | ConnorsRSI(3,2,100) ; seuils 90/10 (défaut) ou 95/5 (volatils) ; filtre SMA200 |
| À vérifier | Images : alignement .md/HTML impossible → vérif manuelle si réutilisation visuelle. Texte intégralement exploitable. |

> ⚠️ Extraction BRUT, zone validation/. Indicateur d'ÉCOLE (Connors) — non standard universel. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
