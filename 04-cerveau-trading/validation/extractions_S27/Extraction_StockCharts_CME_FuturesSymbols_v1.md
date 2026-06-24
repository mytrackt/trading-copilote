# Extraction StockCharts — CME Futures & Spot Prices (symboles de contrats)
**Source :** `bundles/stockcharts/cme_futures_and_spot_prices.md` (HTTP 200 · ~4 300 car.) + 2 images
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 « certifiées » par section-fallback mais figcaptions VIDES (visuels décoratifs « Chart Example », aucun contenu factuel exploitable)
**Décisions :** D319 → D325 · **Page :** chartschool.stockcharts.com/.../index-and-market-indicator-catalog/cme-futures-and-spot-prices
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page PRIORITAIRE — convention de **symboles de contrats futures CME** (préfixe `^`, codes mois F→Z, format année). Décrit la nomenclature StockCharts pour identifier un contrat précis. Concerne directement les actifs TRADING **GC·HG·CL·ZW** (tous CME Group : COMEX/NYMEX/CBOT) et CONFIRMATION **ES**. ⚠️ La page ne liste PAS explicitement les codes GC/HG/CL/ZW (seul **ES** est donné en exemple) — les symboles de nos actifs relèvent de la **convention générale** décrite, pas d'une citation littérale.

---

## INVENTAIRE IMAGES (traçabilité)

| Image | Label certifié | Section | Décision liée | Exploitable |
|-------|----------------|---------|---------------|-------------|
| image_01 | Chart Example (section-fallback) | Chart Example | D323 | Non — figcaption vide, visuel décoratif |
| image_02 | Chart Example (section-fallback) | Chart Example | D323 | Non — figcaption vide, visuel décoratif |

---

## DÉCISIONS

### D319 — StockCharts : données EOD pour futures CME Group
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : StockCharts.com fournit des données **end-of-day (EOD)** pour une sélection de futures négociés via le **CME Group**. Le CME, Cboe, COMEX, KBCT et NYMEX font désormais partie du CME Group. Cela inclut les contrats futures e-mini et les **prix spot** pour métaux précieux, pétrole, etc. Le mot « spot » dans le nom d'un symbole permet de tracer des graphiques long terme sur une matière première.
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : **Symbol Group** = CME · **Publisher** = CME Group · **Update Frequency** = End-of-day (EOD).
**TRADEX-AI C0** : Bourses de nos actifs TRADING (GC/HG Or·Cuivre = COMEX, CL Pétrole = NYMEX, ZW Blé = CBOT) toutes regroupées sous CME Group. ⚠️ Source StockCharts = EOD seulement, donc **inadaptée** au temps réel TRADEX-AI (données live = NT8/Rithmic) ; pertinente uniquement comme référence de nomenclature/historique long terme.
*Catégorie : configuration*

---

### D320 — Préfixe caret `^` réservé aux contrats futures
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : Le symbole d'un future e-mini se compose de plusieurs parties. Le **premier caractère est un caret (^)**, réservé aux contrats futures. Le ou les caractères suivants représentent le **nom du contrat** (ex. le « ES » dans `^ESM13` désigne le e-mini S&P 500).
**TRADEX-AI C0** : Convention StockCharts — un contrat future se note `^<CODE><MOIS><ANNÉE>`. Ne s'applique qu'aux symboles StockCharts (data EOD) ; ne pas confondre avec les symboles NinjaTrader/Rithmic du flux live.
*Catégorie : configuration*

---

### D321 — Codes mois des contrats (F→Z) et format année
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : Après le code du contrat, **trois caractères** indiquent mois et année. Les **deux derniers chiffres = l'année**, la **lettre = le mois**. Exemple : `^ESH14` = contrat E-Mini **mars 2014**. Table des codes mois :
> F=Janvier · G=Février · H=Mars · J=Avril · K=Mai · M=Juin · N=Juillet · Q=Août · U=Septembre · V=Octobre · X=Novembre · Z=Décembre
**TRADEX-AI C0** : Codes mois CME standard (identiques au standard de l'industrie). Réutilisables pour parser/afficher l'échéance d'un contrat GC/HG/CL/ZW dans l'UI (ex. `GCM26` = Or juin 2026). ⚠️ Cette table mois n'est PAS propre à ES : c'est la convention CME générale, applicable à nos actifs.
*Catégorie : configuration*

---

### D322 — Symbole ES (CONFIRMATION) : exemple littéral de la page
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : La page donne explicitement **ES** = e-mini S&P 500. Exemples cités : `^ESM13` (juin 2013) et `^ESH14` (mars 2014). Le contrat E-mini S&P 500 **se négocie 23 h/24, 5 j/7** (lundi→vendredi), ce qui rend le prix d'« ouverture » quasi sans objet (pas de période « overnight »).
**TRADEX-AI C0/C7** : ES = actif CONFIRMATION du projet. Symbole StockCharts EOD = `^ES<mois><année>`. La quasi-continuité 23 h/24 du e-mini est à garder en tête pour le calcul de corrélations live 30j (peu/pas de gap d'ouverture). Confirmation only — jamais d'ordre sur ES.
*Catégorie : configuration*

---

### D323 — Exemples graphiques (visuels décoratifs)
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md, image_01, image_02) : La section « Chart Example » contient deux figures illustrant des graphiques de futures/spot CME. **Figcaptions vides** — aucune donnée factuelle exploitable (illustrations décoratives).
**TRADEX-AI C0** : Aucune règle dérivable de ces images ; conservées pour traçabilité uniquement.
*Catégorie : configuration*

---

### D324 — Symboles GC·HG·CL·ZW non listés littéralement (convention applicable)
🔴 **NON VÉRIFIÉ (sur cette page)** : La page ne cite PAS les codes **GC (Or), HG (Cuivre), CL (Pétrole WTI), ZW (Blé)**. Seul **ES** est donné en exemple. Les symboles StockCharts de nos actifs TRADING ne sont donc **pas confirmés littéralement** par cette source.
🟡 **CONVENTION** (déduction de D320–D321) : Par application de la convention décrite, un contrat de nos actifs s'écrirait `^GC<mois><année>`, `^HG…`, `^CL…`, `^ZW…` (codes mois F→Z). Codes GC/HG/CL/ZW = codes CME usuels de l'industrie, mais **à confirmer** via le catalogue de symboles StockCharts (lien « Symbol List ») ou la spec CME — hors de cette page.
**TRADEX-AI C0** : Ne PAS coder en dur `^GC…/^HG…/^CL…/^ZW…` comme symboles StockCharts certifiés. Marquer « à vérifier » et valider sur la page de catalogue symboles avant tout usage. Pour le flux live, ce sont de toute façon les symboles NT8/Rithmic qui font foi, pas ceux de StockCharts.
*Catégorie : configuration*

---

### D325 — Accès à la liste de symboles à jour (catalogue dynamique)
🟢 **FAIT VÉRIFIÉ** (Source : cme_futures_and_spot_prices.md) : Une **liste de symboles à jour** de tous les CME Futures & Spot Prices est accessible aux utilisateurs StockCharts (lien catalogue de symboles). Depuis cette liste, l'icône « Mentions » à droite d'un symbole donne plus de détails (mentions dans ChartLists publiques, articles de blog, etc.).
⏳ **VOLATILE** : Le contenu exact de la liste (codes/échéances disponibles) **change dans le temps** et nécessite un compte StockCharts — non capturé dans ce bundle.
**TRADEX-AI C0** : Source à interroger MANUELLEMENT pour confirmer les symboles GC/HG/CL/ZW (cf. D324). N'est pas une source automatisable pour TRADEX-AI (EOD + accès compte) ; usage ponctuel de vérification de nomenclature.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D319 → D325 (7) |
| Images | 2/2 (décoratives, figcaptions vides — aucune règle dérivée) |
| Catégories utilisées | configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🟡 CONVENTION · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ |
| Actifs concernés | TRADING GC·HG·CL·ZW (convention seulement, non listés) · CONFIRMATION ES (cité littéralement `^ESM13`/`^ESH14`) |
| Belkhayate | Non concerné (page = nomenclature de symboles de contrats) |

### À VÉRIFIER (humain)
- **D324** : codes StockCharts exacts de **GC/HG/CL/ZW** absents de la page → confirmer via catalogue « Symbol List » StockCharts ou spec CME avant tout usage.
- **D325** : liste de symboles = contenu VOLATILE + accès compte StockCharts → vérification manuelle ponctuelle, non automatisable.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
