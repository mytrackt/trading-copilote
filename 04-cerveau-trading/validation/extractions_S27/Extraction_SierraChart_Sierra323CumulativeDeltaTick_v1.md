# Extraction SierraChart — Cumulative Delta Bars - Up/Down Tick Volume
**Source :** `bundles/sierrachart/sierra_323_cumulative_delta_tick.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9191 → D9200 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=323
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Delta cumulatif tick par tick = mesure directe de pression acheteurs/vendeurs sur GC/HG/CL/ZW en intraday.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9191 — Définition Cumulative Delta Bars Up/Down Tick Volume
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : Le Cumulative Delta Bars Up/Down Tick Volume est la somme cumulative, sur les données du graphique ou la journée de trading, de la différence entre le volume UpTick et le volume DownTick. Il s'affiche sous forme de chandeliers High-Low.
**TRADEX-AI C2** : Indicateur order flow de référence — mesure la pression nette acheteur (UpTick) vs vendeur (DownTick) bar par bar sur NT8, directement applicable aux actifs GC/HG/CL/ZW via ATAS.
*Catégorie : volume_liquidite*

### D9192 — Règle de calcul UpTick / DownTick
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : Le volume UpTick est le volume échangé à un prix supérieur au trade précédent ; le volume DownTick est le volume échangé à un prix inférieur. Si le dernier prix ne change pas, le tick est classé selon la direction précédente (uptick si le dernier tick était up, downtick sinon).
**TRADEX-AI C2** : Règle de classification tick utilisée par ATAS pour le delta — la cohérence de cette règle avec l'implémentation ATAS doit être vérifiée avant toute fusion KB ; toute divergence fausse les signaux order flow.
*Catégorie : volume_liquidite*

### D9193 — Construction du chandelier CDB (Open/High/Low/Close)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : La construction OHLC du chandelier CDB suit ces règles : Open = Close du bar CDB précédent (ou 0 si reset/premier bar) ; High = Close précédent + DifferenceHigh du bar ; Low = Close précédent + DifferenceLow du bar ; Close = Close précédent + (AskVolume - BidVolume) du bar de prix principal.
**TRADEX-AI C2** : Le Close du CDB est strictement (AskVolume - BidVolume) — identique au Delta standard ATAS. High/Low du CDB capturent les extremes de pression intra-bar, fournissant un contexte plus riche qu'un simple delta close.
*Catégorie : volume_liquidite*

### D9194 — Exigence données tick par tick pour résultat précis
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : Pour que le CDB donne un résultat précis, les données tick par tick doivent impérativement être présentes dans le fichier de données Intraday. Sans tick by tick, les résultats sont inexacts.
**TRADEX-AI C2** : Règle de qualité de données critique — TRADEX-AI doit vérifier la disponibilité du feed tick-by-tick Rithmic/NT8 avant d'utiliser le delta cumulatif comme signal ; un feed agrégé invaliderait les lectures. Contrôle à intégrer dans le staleness_monitor.
*Catégorie : gestion_risque_entree*

### D9195 — Input : Reset at Start of Trading Day
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : Quand cet input est à Yes, le calcul cumulatif est remis à zéro au début de chaque journée de trading (défini par les Session Times du graphique). La valeur d'ouverture après reset sera égale à la différence Ask-Bid du premier trade/record — elle ne sera donc pas forcément à 0.
**TRADEX-AI C2** : Pour les futures (GC/CL/HG/ZW) en trading intraday, le reset journalier est la configuration recommandée — permet de mesurer la pression nette de la session en cours sans contamination des sessions précédentes.
*Catégorie : indicateurs_momentum*

### D9196 — Input : Reset at Both Session Start Times
🟢 **FAIT VÉRIFIÉ** (Source : sierra_323_cumulative_delta_tick.md) : Quand cet input est à Yes, il implique que Reset at Start of Trading Day est actif, et ajoute un second reset au Evening Start Time si la session du soir est activée pour le graphique.
**TRADEX-AI C2** : Pour les actifs avec session extended (notamment GC or qui trade quasi 24h), ce double reset permet de séparer le delta session jour du delta session nuit — pertinent pour isoler les mouvements institutionnels nocturnes sur l'or.
*Catégorie : indicateurs_momentum*

### D9197 — Interprétation signal : divergence prix vs CDB
🔵 **ÉCOLE** (Source : sierra_323_cumulative_delta_tick.md) : La divergence entre la tendance du prix et la tendance du Cumulative Delta est un signal classique d'order flow — si le prix monte mais que le CDB baisse, les vendeurs absorbent les achats (bearish divergence).
**TRADEX-AI C2** : Divergence CDB/Prix = signal de confirmation order flow pour C2 dans la grille TRADEX. Une divergence haussière (prix en baisse, CDB en hausse) sur GC renforce un signal ACHETER; une divergence baissière affaiblit ou annule un signal.
*Catégorie : configuration*

### D9198 — Pertinence pour ATAS vs Sierra Chart
🟡 **SYNTHÈSE** (Source : sierra_323_cumulative_delta_tick.md) : Sierra Chart ID=323 est l'équivalent Sierra du delta cumulatif ATAS. Les deux calculent AskVolume - BidVolume de manière cumulative. La différence clé : Sierra supporte l'affichage chandelier OHLC du delta (DifferenceHigh/DifferenceLow intra-bar), ce qu'ATAS appelle le "Delta Candle" dans son footprint.
**TRADEX-AI C2** : ATAS Pro (connecté Rithmic) est l'outil principal pour TRADEX-AI. La logique Sierra ID=323 confirme la validité conceptuelle du delta cumulatif ATAS — les deux sont interchangeables pour les signaux C2, sous réserve de disponibilité tick by tick.
*Catégorie : volume_liquidite*

### D9199 — Seuil opérationnel : DifferenceHigh/DifferenceLow comme proxy de volatilité order flow
🟡 **SYNTHÈSE** (Source : sierra_323_cumulative_delta_tick.md) : Le DifferenceHigh et DifferenceLow d'un bar CDB mesurent les extremes de pression nette intra-bar. Un écart large (DifferenceHigh - DifferenceLow élevé) indique une forte lutte acheteurs/vendeurs sur ce bar — potentiel retournement ou accélération.
**TRADEX-AI C2** : Pour TRADEX-AI, surveiller l'amplitude intra-bar du CDB sur les actifs TRADING (GC/HG/CL/ZW) : une amplitude anormalement élevée peut précéder un breakout ou un rejet de niveau — à corréler avec les niveaux Belkhayate (pivots, BGC).
*Catégorie : structure_marche*

### D9200 — Configuration recommandée TRADEX-AI pour le CDB intraday
🟡 **SYNTHÈSE** (Source : sierra_323_cumulative_delta_tick.md) : Combinaison optimale pour TRADEX-AI intraday futures : (1) Reset at Start of Trading Day = Yes pour sessions jour ; (2) Reset at Both Session Start Times = Yes pour actifs 24h comme GC ; (3) Feed tick-by-tick Rithmic obligatoire validé par staleness_monitor avant usage.
**TRADEX-AI C2** : Ces paramètres constituent la configuration de référence pour le delta cumulatif C2 dans TRADEX-AI. À documenter dans settings.py comme CONFIG_CDB_INTRADAY = {"reset_day": True, "reset_both_sessions": True, "require_tick_data": True}.
*Catégorie : gestion_risque_entree*
