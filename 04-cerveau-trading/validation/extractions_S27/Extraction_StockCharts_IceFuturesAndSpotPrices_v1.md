# Extraction StockCharts — ICE Futures and Spot Prices

**Source :** `bundles/stockcharts/ice_futures_and_spot_prices.md` (HTTP 200 · ~2 100 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende) · 1/1 certifiée
**Décisions :** D2131 → D2135 · **Page :** https://chartschool.stockcharts.com/table-of-contents/index-and-market-indicator-catalog/ice-futures-and-spot-prices
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🟡 **PERTINENCE FUTURES : CATALOGUE/CONFIG** — page de catalogue de symboles ICE (EOD spot Brent, Café, Cacao, Coton, Sucre). Aucun de ces actifs n'est dans ACTIFS_TRADABLES (GC/HG/CL/ZW). Valeur = note de configuration data/symboles (CL = pétrole WTI = CME, PAS ICE Brent). Belkhayate NON CONCERNÉ. Bundle court par nature (page de référence symboles).

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Décision |
|-------|-------|---------|----------|
| image_01.png | ICE | Chart Example | D2133 |

## DÉCISIONS

### D2131 — StockCharts fournit des données EOD pour certains futures ICE
🟡 **CONVENTION** (Source : ice_futures_and_spot_prices.md) : « StockCharts.com provides end-of-day (EOD) data for select futures traded through the Intercontinental Exchange (ICE). These include spot prices for Brent Crude, Coffee, Cocoa, Cotton, and Sugar. Users will see the word "spot" in the name for these symbols. Spot prices allow users to create long-term charts for a specific commodity. »
**TRADEX-AI C4** : note de couverture data — StockCharts ne sert que 5 spots ICE en EOD (Brent, Café, Cacao, Coton, Sucre). Le mot « spot » dans le nom du symbole = prix au comptant. Aucun de ces actifs ≠ GC/HG/CL/ZW ; à connaître seulement comme source de référence inter-marché potentielle (Brent vs CL/WTI).
*Catégorie : configuration*

---

### D2132 — Métadonnées du groupe de symboles ICE
🟡 **CONVENTION** (Source : ice_futures_and_spot_prices.md) : « Symbol Group: ICE ; Publisher: Intercontinental Exchange ; Update Frequency: End-of-day (EOD) ; Online Source: ICE (ice.com). »
**TRADEX-AI C4** : fiche technique de la source — groupe ICE, publisher Intercontinental Exchange, fréquence EOD. Fréquence EOD = inadaptée au moteur temps réel TRADEX (surveillance 2s sur NT8/ATAS) ; donnée purement contextuelle/long terme.
*Catégorie : configuration*

---

### D2133 — Exemple de graphique ICE (image certifiée)
🟡 **CONVENTION** (Source : ice_futures_and_spot_prices.md, image_01) : la section « Chart Example » présente un graphique illustratif d'un symbole spot ICE (figcaption « ICE »).
**TRADEX-AI C4** : illustration documentaire d'un spot ICE EOD. Aucune règle de trading ni paramètre — valeur strictement visuelle/catalogue.
*Catégorie : configuration*

---

### D2134 — Accès à la liste à jour des symboles ICE
🟡 **CONVENTION** (Source : ice_futures_and_spot_prices.md) : « StockCharts.com users can access an up-to-date list of symbols for all our ICE Futures Spot Prices. From this list, click the "Mentions" icon to the right of a specific symbol for more details about the symbol, as well as recent mentions in Public ChartLists, blog articles, and more. »
**TRADEX-AI C4** : la liste des symboles ICE est dynamique (consultable via recherche StockCharts). Implication config : ne jamais coder en dur un symbole ICE — passer par la recherche de catalogue. Sans objet pour TRADEX (data feed = Rithmic/NT8, pas StockCharts).
*Catégorie : configuration*

---

### D2135 — Distinction Brent (ICE/spot) vs WTI (CME/CL) pour le moteur
🟡 **CONVENTION** (Source : ice_futures_and_spot_prices.md) : la page liste « Brent Crude » spot comme symbole ICE EOD ; elle ne concerne PAS le WTI.
**TRADEX-AI C4** : garde-fou data — l'actif tradable CL est le **pétrole WTI sur CME** (cf. CLAUDE.md), distinct du Brent spot ICE de cette page. Ne pas confondre Brent ICE (EOD, référence) et CL/WTI (temps réel, tradable). Le Brent pourrait au mieux servir de référence inter-marché énergie (corrélation), jamais d'actif d'ordre.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2131 | Data EOD pour 5 spots ICE | 🟡 | C4 | configuration |
| D2132 | Métadonnées groupe ICE (EOD) | 🟡 | C4 | configuration |
| D2133 | Exemple graphique ICE (image) | 🟡 | C4 | configuration |
| D2134 | Liste symboles ICE dynamique | 🟡 | C4 | configuration |
| D2135 | Brent (ICE) ≠ WTI (CL/CME) | 🟡 | C4 | configuration |

| Élément | Valeur |
|---------|--------|
| Décisions | D2131 → D2135 (5) |
| Images certifiées | 1/1 |
| Cercles | C4 (macro/data inter-marché — page catalogue) |
| Catégories | configuration (exclusif) |
| Actif applicable | AUCUN tradable (Brent/Café/Cacao/Coton/Sucre ≠ GC/HG/CL/ZW) — Brent = référence inter-marché énergie au mieux |
| Belkhayate | NON CONCERNÉ (page catalogue de symboles) |
| Pertinence futures | FAIBLE — page de référence/config, EOD inadapté au moteur temps réel |
| Cas « à vérifier » | (1) Bundle court par nature (page catalogue symboles) — 5 décisions seulement, NON paddé. (2) Aucun actif ICE n'est tradable dans TRADEX ; risque de confusion Brent (ICE/spot/EOD) vs WTI (CL/CME/temps réel) explicité en D2135. (3) Fréquence EOD = incompatible avec la surveillance 2s du moteur. |

**Liens Belkhayate :** Aucun lien — page de catalogue de symboles ICE, sans rapport avec la méthode Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
