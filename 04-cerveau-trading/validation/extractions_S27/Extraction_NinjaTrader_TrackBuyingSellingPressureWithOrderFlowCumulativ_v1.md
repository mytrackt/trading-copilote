# Extraction NinjaTrader — Track Buying & Selling Pressure with Order Flow Cumulative Delta
**Source :** `bundles/ninjatrader/track_buying_selling_pressure_with_order_flow_cumulative_delta.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8111 → D8120 · **Page :** https://ninjatrader.com/futures/blogs/track-buying-selling-pressure-with-order-flow-cumulative-delta/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Cumulative Delta mesure la pression achat/vente en temps réel — confirmation d'alignement C2 (Order Flow) pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8111 — Définition du Delta (Order Flow)
🟢 **FAIT VÉRIFIÉ** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Delta = différence nette entre volume d'achat et volume de vente à chaque niveau de prix. Formule : Market Buy Orders − Market Sell Orders = Delta. Résultat positif → acheteurs plus agressifs ; résultat négatif → vendeurs plus agressifs.
**TRADEX-AI C2** : Le Delta est la métrique de base de l'Order Flow. Pour GC/HG/CL/ZW, un Delta positif croissant renforce un signal ACHETER ; un Delta négatif croissant renforce un signal VENDRE.
*Catégorie : indicateurs_momentum*

### D8112 — Ordres passifs vs agressifs (Cumulative Delta)
🟢 **FAIT VÉRIFIÉ** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Les ordres limites sont passifs (attendent une contrepartie) ; les ordres marché sont agressifs (exécution immédiate au ask ou au bid). Acheter au ask ou vendre au bid = urgence de marché. Le Cumulative Delta mesure uniquement les ordres agressifs (marché), pas les ordres passifs (limite).
**TRADEX-AI C2** : Dans le moteur TRADEX, l'agressivité des ordres (achat au ask / vente au bid) est le signal primaire d'Order Flow à monitorer via ATAS. Les ordres passifs ne constituent pas un signal d'entrée en eux-mêmes.
*Catégorie : structure_marche*

### D8113 — Cumulative Delta : mode Session vs mode Bar
🟢 **FAIT VÉRIFIÉ** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Deux modes d'affichage existent — (1) Session : accumulation du Delta sur toute la session de trading, le prix de clôture de la barre précédente est reporté à l'ouverture de la suivante (vue continue) ; (2) Bar : valeur du Delta par barre uniquement, sans continuité (affichage en histogramme positif/négatif). Le mode Bar est utile pour identifier les retournements ou les changements soudains dans l'activité Order Flow.
**TRADEX-AI C2** : Le mode Bar est recommandé pour détecter les retournements ponctuels d'Order Flow (signal C2 court terme) ; le mode Session est préférable pour confirmer la tendance directionnelle intraday sur les actifs tradables.
*Catégorie : indicateurs_momentum*

### D8114 — Divergence Cumulative Delta / Prix (signal de retournement)
🟢 **FAIT VÉRIFIÉ** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Lorsque le prix suggère une tendance haussière mais que le Cumulative Delta ne confirme pas cette direction (ex : Delta plat ou décroissant pendant une hausse des prix), il y a divergence — signal que la tendance haussière manque de conviction d'achat réelle.
**TRADEX-AI C2** : Règle d'alerte : si le prix de GC/HG/CL/ZW monte mais que le Cumulative Delta est négatif ou en baisse, NE PAS entrer en position longue. La divergence Delta/Prix est un critère éliminatoire pour le signal C2 dans la grille /10.
*Catégorie : configuration*

### D8115 — Cumulative Delta : confirmation de tendance (usage principal)
🔵 **ÉCOLE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : L'une des utilisations principales du Cumulative Delta est de confirmer ou infirmer les tendances de marché. Un Cumulative Delta haussier accompagnant une hausse des prix confirme la tendance ; un Cumulative Delta baissier sur une hausse des prix l'infirme.
**TRADEX-AI C2** : Critère C2 de validation dans la grille /10 : le Cumulative Delta doit être aligné avec la direction du signal prix (C1). Alignement requis pour valider le signal — non-alignement = réduction du score ou blocage.
*Catégorie : indicateurs_tendance*

### D8116 — Paramètre par défaut ATR (lié aux outils Order Flow+)
🔵 **ÉCOLE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : L'outil Order Flow+ de NinjaTrader 8 inclut Cumulative Delta, barres volumétriques et Volume Profile. Le Cumulative Delta se présente sous forme de chandeliers dans un panneau sous le prix.
**TRADEX-AI C2** : ATAS (connecté Rithmic) est l'outil Order Flow retenu dans TRADEX-AI. NinjaTrader Order Flow+ peut servir de source secondaire de validation pour le Cumulative Delta si ATAS est indisponible (circuit breaker CB_ATAS).
*Catégorie : structure_marche*

### D8117 — Urgence de marché comme signal de force directionnelle
🟡 **SYNTHÈSE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : L'accumulation d'ordres agressifs dans une direction (achat au ask ou vente au bid) indique une urgence : les participants sont prêts à payer le spread pour s'exécuter immédiatement. Une accumulation d'achats agressifs = pression achat forte = probabilité de continuation haussière augmentée.
**TRADEX-AI C2** : Dans le contexte Belkhayate, l'urgence Order Flow est un signal C2 complémentaire à la direction C1 (BGC, Pivots). Lorsque la pression Order Flow est alignée avec un signal C1 ≥ 3/4 actifs, le score /10 de la grille augmente.
*Catégorie : gestion_risque_entree*

### D8118 — Cumulative Delta : réinitialisation en mode Session
🔵 **ÉCOLE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : En mode Session, le Cumulative Delta se réinitialise à chaque nouvelle session de trading. Les comparaisons inter-sessions ne sont donc pas pertinentes avec ce mode — il mesure la pression d'une seule session.
**TRADEX-AI C2** : Pour les actifs futures tradés sur plusieurs sessions (GC, CL notamment), utiliser le mode Bar pour les analyses multi-sessions ou conserver la comparaison intra-session uniquement avec le mode Session.
*Catégorie : timing*

### D8119 — Order Flow : complémentarité avec analyse prix
🟡 **SYNTHÈSE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Le Cumulative Delta ne remplace pas l'analyse de prix classique — il la complète. L'analyse de prix (C1) fournit la direction ; le Cumulative Delta (C2) confirme ou infirme la conviction derrière cette direction.
**TRADEX-AI C2** : Architecture TRADEX confirmée : C1 (Belkhayate : BGC, Direction, Énergie, Pivots) est le signal primaire ; C2 (Order Flow : Cumulative Delta, Footprint, Big Trades) est le signal de confirmation. Aucun des deux ne suffit seul.
*Catégorie : configuration*

### D8120 — Outil premium NinjaTrader Order Flow+ (contexte implémentation)
🔵 **ÉCOLE** (Source : track_buying_selling_pressure_with_order_flow_cumulative_delta.md) : Le Cumulative Delta est inclus dans la suite Order Flow+ de NinjaTrader 8 (outil premium payant), avec les barres volumétriques et les Volume Profiles. La suite offre analyse Order Flow, Volume et profondeur de marché.
**TRADEX-AI C2** : TRADEX-AI utilise ATAS Pro (connecté Rithmic) comme outil Order Flow principal. NinjaTrader Order Flow+ constitue une redondance possible mais n'est pas l'outil retenu. Les données NT8 transitent par fichiers JSON vers le moteur Python.
*Catégorie : structure_marche*
