# Extraction Optimus — How To Set Up Your Trading Charts For Order Flow Trading
**Source :** `bundles/optimusfutures/how_to_set_up_your_trading_charts_for_order_flow_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image scrappée · 0/0 certifiées · 0 à vérifier
**Décisions :** D8511 → D8520 · **Page :** https://optimusfutures.com/blog/how-to-set-up-your-trading-charts-for-order-flow-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Configuration de base d'un chart Order Flow (Cumulative Delta + Volume) — alimente C2 Order Flow.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image scrappée — bundle est un transcript vidéo YouTube) | — | — | — |

## NOTE CONTENU
Ce bundle est un transcript court d'une vidéo YouTube promotionnelle pour la plateforme Optimus Flow. Le contenu factuel extractible est minimal mais identifie les éléments essentiels d'un chart Order Flow.

## DÉCISIONS

### D8511 — Cumulative Delta : élément clé du chart Order Flow
🔵 **ÉCOLE** (Source : how_to_set_up_your_trading_charts_for_order_flow_trading.md) : Pour démarrer l'analyse Order Flow, le Cumulative Delta (CD) doit être ajouté au chart en priorité. Il mesure l'accumulation nette des achats agressifs moins les ventes agressives sur la période.
**TRADEX-AI C2** : Le Cumulative Delta est une entrée C2 (Order Flow) dans TRADEX. Il complète la lecture Footprint ATAS pour confirmer la pression directionnelle des institutionnels.
*Catégorie : indicateurs_momentum*

### D8512 — Volume : indicateur indispensable en Order Flow trading
🔵 **ÉCOLE** (Source : how_to_set_up_your_trading_charts_for_order_flow_trading.md) : L'affichage du volume sur le chart est une composante cruciale pour comprendre l'activité du marché en Order Flow trading. Sans le volume, le delta seul est incomplet.
**TRADEX-AI C2** : Confirme la règle TRADEX : analyse Order Flow = Delta + Volume. Le volume brut est une donnée source pour le calcul des seuils Big Trades dans le moteur ATAS.
*Catégorie : volume_liquidite*

### D8513 — Organisation des charts : lisibilité avant tout
🔵 **ÉCOLE** (Source : how_to_set_up_your_trading_charts_for_order_flow_trading.md) : La personnalisation des charts vise à les rendre lisibles et non surchargés. Un chart trop chargé nuit à la prise de décision rapide. Prioriser les éléments essentiels Order Flow uniquement.
**TRADEX-AI C2** : Principe de conception applicable au dashboard TRADEX : afficher Delta + Volume + Footprint sans surcharge visuelle. Pertinent pour la phase UI (maquettes f1→f8).
*Catégorie : psychologie*

### D8514 — Setup Order Flow minimal = Delta + Volume + indicateurs spécifiques
🟡 **SYNTHÈSE** (Source : how_to_set_up_your_trading_charts_for_order_flow_trading.md) : Un setup Order Flow fonctionnel comprend au minimum : (1) Cumulative Delta, (2) Volume, (3) indicateurs spécifiques Order Flow selon la plateforme. Ce triptyque constitue la base avant d'ajouter d'autres éléments.
**TRADEX-AI C2** : Ce triptyque correspond à la configuration ATAS dans TRADEX (data_reader.py lit Footprint + Delta + Volume depuis ATAS). À documenter comme socle minimal C2.
*Catégorie : configuration*
