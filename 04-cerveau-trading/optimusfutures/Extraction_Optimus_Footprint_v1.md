# Extraction_Optimus_Footprint_v1.md
**Source :** Optimus Futures (blog) — Footprint Charts: A Futures Trader's Guide to Volume Analysis  
**URL :** https://optimusfutures.com/blog/footprint-charts/  
**Décisions :** D112 → D120  
**Images certifiées :** 7/7 (scraper_static v1 · ancrage alt+filename)  
**Date extraction :** 23/06/2026  
**⚠️ Nature source :** blog de broker (Tier 2). Le texte indique lui-même « This article is the opinion of Optimus Futures ». Faits techniques retenus uniquement.

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — DÉFINITION ET LECTURE

### D112 — Footprint chart : définition et origine (images_01/02)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §What Are Footprint Charts + image_01 · label certifié : A Futures Trader's Guide to Volume Analysis + image_02 · label certifié : Footprint charts vs Candlestick) : Un footprint chart est un type de chandelier **multidimensionnel** affichant le volume échangé à chaque niveau de prix précis dans une barre. Créé par la société (aujourd'hui disparue) **MarketDelta en 2003** comme produit déposé. Synonymes : cluster charts, bid/ask profiles, numbered bars.

**TRADEX-AI C2** : Brique de la Couche order flow (ATAS) — le footprint donne le détail intra-barre que le chandelier OHLC masque.

---

### D113 — Lire un footprint : bid (vendeurs) vs ask (acheteurs) (images_02/03)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §How to Read + §Best Footprint Charts, Note + image_03 · label certifié : Candlestick charts) : Sur un cluster bid/ask, le **côté gauche = vendeurs** ayant frappé le bid (sold) · le **côté droit = acheteurs** ayant levé l'offre (bought). Exemple : cluster 749 × 864 = 749 lots au bid (vendus) et 864 lots à l'ask (achetés). **Règle clé : volume au bid = vendeurs · volume à l'ask = acheteurs.**

**TRADEX-AI C2** : Convention de lecture à coder pour interpréter le footprint ATAS — distinguer agression acheteuse (ask) vs vendeuse (bid).

---

### D114 — Depth of Market (DOM)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Depth of Market (DOM)) : Le DOM (aussi « order book ») mesure l'offre et la demande d'un actif liquide — il montre le nombre d'ordres ouverts et quantités à chaque prix (bid/ask). Distinct du footprint : le DOM montre les ordres **en attente**, le footprint les ordres **exécutés**.

**TRADEX-AI C2** : DOM = ordres limites en attente (intention) · footprint = transactions réalisées (action). Deux flux complémentaires en C2.

---

## BLOC 2 — TYPES DE FOOTPRINT

### D115 — Trois types : bid/ask, volume, delta (image_04)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Best Footprint Charts + image_04 · label certifié : Delta Footprint) :
- **Bid/Ask Footprint** : le plus courant — contrats échangés au bid et à l'ask par période.
- **Volume Profile** : total des contrats à chaque prix sans distinction bid/ask — montre les prix d'intérêt mutuel acheteurs/vendeurs.
- **Delta Footprint** : delta = différence entre ordres exécutés à l'ask et au bid pour un prix donné.

**TRADEX-AI C2** : Trois vues à exposer depuis ATAS — bid/ask, volume, delta — exploitées séparément en C2.

---

### D116 — Interprétation du delta (image_04)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Delta Footprint + image_04) : Le delta révèle quelle partie est la plus agressive. Exemples du chart : delta +826 = 1 514 acheteurs (ask) contre 688 vendeurs (bid) · delta −436 = 1 956 acheteurs contre 2 392 vendeurs · delta −75 = 2 402 contre 2 477. Connaître ces écarts par niveau de prix aide à confirmer une tendance émergente.

**TRADEX-AI C2** : Delta = mesure d'agressivité directionnelle. Delta positif soutenu = pression acheteuse · négatif = pression vendeuse. Signal de confirmation en C2.

---

## BLOC 3 — ANALYSE ORDER FLOW ET STRATÉGIES

### D117 — Points d'analyse order flow

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §How to Analyze Order Flow) : Trois points clés — **Imbalances** (quantités déséquilibrées d'achat/vente) · **Order blocks** (gros volumes contractuels) · **High volume nodes** (zones de forte accumulation de volume). Chacun identifie une zone de support/résistance ou un point précédant une expansion de prix. Règle : toujours utiliser le **contexte** (bigger picture). Astuce : aligner les timeframes du footprint et du chandelier sous-jacent.

**TRADEX-AI C2/C1** : Imbalances / order blocks / HVN = générateurs de niveaux S/R order-flow, à confluencer avec la structure prix (C1).

---

### D118 — Stratégie : Stacked Imbalances (image_05)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Stacked Imbalances + image_05 · label certifié : Footprint Trading Strategies - Stacked Imbalances) : Un déséquilibre empilé verticalement (plusieurs niveaux de prix où achats >> ventes, ou inverse) indique un niveau de support/résistance. Le delta footprint donne l'image la plus claire. Usage : chercher des retournements ou un ralentissement d'un mouvement fort.

**TRADEX-AI C2** : Stacked imbalances = signal de S/R order-flow → entrée contre-tendance ou détection d'essoufflement.

---

### D119 — Stratégie : Unfinished Auctions (image_06)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Unfinished Auctions + image_06 · label certifié : Footprint Trading Strategies - Unfinished Auctions) : Chaque prix voit une enchère acheteurs/vendeurs dans une barre. Quand un prix extrême (mèche) ne voit que des acheteurs OU que des vendeurs (zéro bid ou zéro ask), c'est une **enchère inachevée** — spécifique au footprint.

**TRADEX-AI C2** : Unfinished auction sur extrême de barre = niveau susceptible d'être re-testé (l'enchère doit « se terminer »). Signal de cible/aimant de prix.

---

### D120 — Stratégie : Volume Profile / High Volume Nodes (image_07)

🟢 **FAIT VÉRIFIÉ** (Source : footprint.md §Volume Profile + image_07 · label certifié : Footprint Trading Strategies - Volume Profile) : Les zones de **haut volume** agissent comme support, résistance et nœuds d'attraction du prix courant. Le prix au volume le plus élevé d'une période sert ensuite de support/résistance (temporaire). Usage : scalp en sens inverse depuis ces zones, ou swing vers ces zones de liquidité.

**TRADEX-AI C2/C1** : HVN = niveaux de liquidité structurants. Cohérent avec le futur module VWAP/Volume Profile (P2 #10, Sierra Chart).

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D112
Dernière décision session  : D120
Prochaine décision         : D121
Total décisions            : 9
Total KB cumulé            : D1 → D120
```

---

*Extraction_Optimus_Footprint_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
