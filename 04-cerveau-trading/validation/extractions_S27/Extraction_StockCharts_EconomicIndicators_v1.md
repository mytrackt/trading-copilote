# Extraction StockCharts — Economic Indicators

**Source :** `bundles/stockcharts/economic_indicators.md` (HTTP 200 · ~3 100 car.) + 1 image certifiée
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 1/1 certifiée · 0 à vérifier
**Décisions :** D1631 → D1636 · **Page :** chartschool.stockcharts.com/table-of-contents/index-and-market-indicator-catalog/economic-indicators
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **NATURE** : page **catalogue** (très courte). Décrit la disponibilité d'indicateurs macro **FRED** sur StockCharts (Initial Jobless Claims, Non-farm Payrolls…), pas une méthode d'interprétation. Relève de la couche **MACRO (C4)** de TRADEX-AI et alimente directement la **News Gate** (NFP/FOMC/CPI). Données VOLATILE par nature (publication périodique). Aucun lien Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | (Chart Example — figcaption vide, section-fallback) | Chart Example | D1634 |

---

## DÉCISIONS

### D1631 — Disponibilité d'indicateurs économiques sur StockCharts
🟢 **FAIT VÉRIFIÉ** (Source : economic_indicators.md) : StockCharts fournit les données d'un **groupe restreint d'indicateurs économiques**, mis à jour sur base **hebdomadaire, mensuelle ou trimestrielle** selon la série. Exemples cités : **Initial Jobless Claims** (`$$UNEMPCIN`, hebdo) et **Non-farm Payrolls** (`$$EMPLOY`, mensuel). Ces séries peuvent être comparées au **S&P 500** pour analyse.
**TRADEX-AI C4** : Brique macro — disponibilité de séries macro clés (emploi). NFP est un événement majeur de la News Gate du système.
*Catégorie : configuration*

---

### D1632 — Source des données : FRED (Federal Reserve / St Louis Fed)
🟢 **FAIT VÉRIFIÉ** (Source : economic_indicators.md) : **Symbol Group** = Economic Indicators. **Publisher** = **Federal Reserve Economic Data (FRED)**. **Online Source** = St Louis Fed Economic Research. **Update Frequency** = Weekly, Monthly ou Quarterly.
**TRADEX-AI C4** : Traçabilité de la provenance macro (FRED) — référence pour un éventuel collecteur de données macro.
*Catégorie : configuration*

---

### D1633 — Fréquence de mise à jour = donnée volatile/périodique
⏳ **VOLATILE** (Source : economic_indicators.md) : Les séries sont publiées **périodiquement** (hebdo/mensuel/trimestriel) ; leur valeur change à chaque publication officielle. Aucune valeur chiffrée fixe dans la source.
**TRADEX-AI C4** : Garde-fou de fraîcheur — toute série macro doit être horodatée et soumise au Staleness Monitor ; la News Gate doit bloquer autour des publications (NFP/FOMC/CPI).
*Catégorie : timing*

---

### D1634 — Exemple de graphique (illustratif)
🟢 **FAIT VÉRIFIÉ** (Source : economic_indicators.md, image_01) : La page comporte une section « Chart Example » avec un graphique illustratif unique (légende vide, certifié par section-fallback). Aucune méthode d'interprétation n'est décrite dans la source.
**TRADEX-AI C4** : Illustration seulement — aucune brique de signal exploitable au-delà de l'existence d'un exemple visuel.
*Catégorie : configuration*

---

### D1635 — Accès à la liste des symboles
🟢 **FAIT VÉRIFIÉ** (Source : economic_indicators.md) : Les utilisateurs StockCharts accèdent à une **liste à jour des symboles** d'indicateurs économiques (lien recherche `q="Economic Indicators"`). L'icône « Mentions » à droite d'un symbole donne plus de détails et les mentions récentes (ChartLists publiques, articles de blog).
**TRADEX-AI C4** : Méta-information de navigation StockCharts — non opérationnel pour le moteur ; informatif.
*Catégorie : configuration*

---

### D1636 — Portée et limite : catalogue, pas méthode
🟢 **FAIT VÉRIFIÉ** (Source : economic_indicators.md) : La page est un **catalogue de disponibilité de données**, sans méthode d'interprétation, sans seuils ni règles de trading. Elle se limite à décrire quelles séries macro sont accessibles, leur source (FRED) et leur fréquence.
**TRADEX-AI C4** : Cadrage honnête — cette source n'apporte AUCUNE règle de signal ; elle documente seulement la disponibilité de données macro à brancher en couche CONFIRMATION/MACRO.
*Catégorie : configuration*

---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie | Actifs |
|---|----------|-----|--------|-----------|--------|
| D1631 | Indicateurs dispo (NFP, jobless) | 🟢 | C4 | configuration | ES·DX (macro) |
| D1632 | Source FRED / St Louis Fed | 🟢 | C4 | configuration | ES·DX (macro) |
| D1633 | Fréquence = volatile/périodique | ⏳ | C4 | timing | ES·DX (macro) |
| D1634 | Exemple de graphique | 🟢 | C4 | configuration | — |
| D1635 | Liste des symboles | 🟢 | C4 | configuration | — |
| D1636 | Catalogue, pas méthode | 🟢 | C4 | configuration | ES·DX (macro) |

**Total : 6 décisions (D1631→D1636) · 1/1 image certifiée · 0 cas à vérifier.**
Lien Belkhayate : **NON CONCERNÉ** (la source ne mentionne pas Belkhayate).
**Note de cadrage** : page-catalogue très mince ; volontairement **non paddée** (6 décisions = plancher du gabarit). Valeur réelle = alimenter la couche MACRO (C4) et la News Gate (NFP/FOMC/CPI), pas un signal direct.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
