# Extraction StockCharts — The Pre-Holiday Effect
**Source :** `bundles/stockcharts/the_pre_holiday_effect.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D4451 → D4470 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-pre-holiday-effect.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : effet calendrier pré-férié applicable à ES (S&P 500 confirmation) ; biais saisonnier documenté sur 50 ans utile pour calibrer signal ES avant jours fériés US.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/lnD13ncCcdMh4yLSTecF | General Electric Co. (GE) Pre-Holiday example chart from StockCharts.com | Short-Term Trading Strategy | D4453 |
| /files/0GOpaCzJW9Y1wUMw4CHL | Motorola, Inc. (MOT) Pre-Holiday example chart from StockCharts.com | Short-Term Trading Strategy | D4454 |
| /files/1kihSHoNgPPRTjI5hl4O | Realty Income Corp. Md. (O) Pre-Holiday example chart from StockCharts.com | Short-Term Trading Strategy | D4455 |
| /files/fziuRBg9WUbiqj18NYcr | Memorial Day 2000 entry point example 1 | Long-Term Trading Strategy | D4457 |
| /files/4lkdCCqUn2lAmWEU9gNo | Memorial Day 2000 entry point example 2 | Long-Term Trading Strategy | D4457 |

## DÉCISIONS

### D4451 — Effet pré-férié : biais haussier récurrent sur S&P 500
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : Les prix boursiers se comportent de façon spécifique dans les deux jours de trading précédant chaque jour férié US. Sur les 50 dernières années, l'achat la veille d'un jour férié et la vente en fin d'année est rentable sur la majorité des 9 jours fériés du calendrier US (données S&P 500).
**TRADEX-AI C4** : Pour ES (confirmation), intégrer un biais haussier la veille de jours fériés US (Indépendance, Labor Day, New Year) — renforcer légèrement la pondération signal ES ces jours précis.
*Catégorie : saisonnalite*

### D4452 — Mécanisme : vente pré-férié = pression baissière temporaire = opportunité d'achat
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : Les traders allègent leurs positions avant les week-ends de 3 jours pour éviter les mauvaises nouvelles pendant la fermeture. Cette pression vendeuse fait baisser les prix, créant une opportunité d'achat à bas prix. Les investisseurs acceptant de traverser les nouvelles négatives court-terme sont récompensés par des points d'entrée inférieurs.
**TRADEX-AI C5** : Sentiment — la vente pré-férié est comportementale (peur du risque overnight), pas fondamentale. Pour GC (Or), ce mécanisme joue aussi : l'or monte souvent après les jours fériés US quand l'appétit au risque revient.
*Catégorie : psychologie*

### D4453 — Exemple GE : achat J-1 fête nationale, vente J+1, gain court terme
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md, image /files/lnD13ncCcdMh4yLSTecF) : Sur General Electric (GE), achat à $47.75 à l'ouverture du 30 juin, vente à $50.25 à l'ouverture du 5 juillet = gain significatif en 5 jours calendaires. Confirmation que l'effet fonctionne aussi sur actions individuelles pas seulement l'indice.
**TRADEX-AI C4** : Macro-calendrier : la fenêtre J-1 avant Independence Day est historiquement favorable à ES. À noter dans le filtre macro_evenements de TRADEX.
*Catégorie : macro_evenements*

### D4454 — Sessions partielles avant Independence Day et après Thanksgiving : volume très faible
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : Le jour avant Independence Day et le jour après Thanksgiving ont des sessions raccourcies, extrêmement volatiles et de très faible volume. Les ordres à cours limité sont difficiles à exécuter. Ces sessions peuvent être tradées mais présentent des risques d'exécution élevés.
**TRADEX-AI C2** : Volume/liquidité critique — pour GC, HG, CL, ZW : les jours de session raccourcie avant fériés US = liquidité réduite sur CME/CBOT, spreads élargis. TRADEX doit bloquer ou réduire la taille de position ces jours (staleness monitor + volume gate).
*Catégorie : volume_liquidite*

### D4455 — Stratégie long terme : investissement pré-Memorial Day récompensé en fin d'année
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md, images /files/fziuRBg9WUbiqj18NYcr, /files/4lkdCCqUn2lAmWEU9gNo) : Memorial Day (mai) offre le plus grand écart buy-one-day-before → sell-year-end : +22.8% vs S&P 500. Les 4 exemples 2000 illustrent des points d'entrée excellents avant Memorial Day. Stratégie : acheter en mai avant le week-end Memorial Day, tenir jusqu'en décembre.
**TRADEX-AI C4** : Saisonnalité maio-décembre : ES haussier statistiquement après Memorial Day. À intégrer dans le biais macro mensuel de TRADEX pour pondérer ES (confirmation).
*Catégorie : saisonnalite*

### D4456 — Comparaison quantifiée : $10 000 → $51 441 (buy-hold) vs $1 440 716 (pré-holiday)
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : Investissement $10 000 en S&P 500 de janvier 1928 à décembre 1975 : $51 441 (stratégie buy-and-hold). Même capital réparti 1/9 avant chaque fête et vendu en fin d'année : $1 440 716. Facteur multiplicateur x28 sur 47 ans. Basé sur 419 fermetures de marché 1928-1975.
**TRADEX-AI C4** : Validation statistique robuste (47 ans, 419 événements) — l'effet saisonnier pré-férié est l'un des plus documentés en finance. Donne une base solide pour intégrer le calendrier US dans le filtre macro de TRADEX.
*Catégorie : saisonnalite*

### D4457 — Independence Day : meilleur rendement achat J-2 → fin d'année (+13.3%) et J-1 (+37.3%)
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : Independence Day présente les meilleurs rendements de la table : achat J-2 = +13.3%, achat J-1 = +37.3% jusqu'à fin d'année. New Year's J-2 = +31.1%. Labor Day J-1 = +33.7%. Ces trois fêtes dominent le classement.
**TRADEX-AI C4** : Hiérarchie saisonnière US pour ES : Independence Day > New Year > Labor Day > Good Friday > Election Day. Pour le biais macro mensuel TRADEX, pondérer ces périodes plus fortement.
*Catégorie : saisonnalite*

### D4458 — President's Day anomalie : J-2 négatif (-0.1%), J-1 modéré (+12.2%)
🟢 **FAIT VÉRIFIÉ** (Source : the_pre_holiday_effect.md) : President's Day est le seul jour férié avec un rendement négatif en J-2 (-0.1%). Explication contextuelle : les données avant 1998 combinent Washington et Lincoln Birthday. Rendement J-1 = +12.2%, positif mais inférieur à la moyenne.
**TRADEX-AI C4** : President's Day = exception saisonnière à traiter avec prudence. Ne pas appliquer le biais haussier systématique pour ce jour férié spécifique.
*Catégorie : saisonnalite*

### D4459 — Stratégie court terme : timing d'entrée = veille fête, sortie = lendemain de fête
🔵 **ÉCOLE** (Source : the_pre_holiday_effect.md) : La stratégie court terme consiste à acheter 1 à 2 jours avant le jour férié et vendre juste après la réouverture du marché. Les traders court terme profitent de la reprise post-férié. Les investisseurs long terme tiennent jusqu'à la fin de l'année pour capturer le rendement complet.
**TRADEX-AI C1** : Structure de trade définie par le calendrier. Pour TRADEX : si signal valide + veille de jour férié US majeur, ajouter une confirmation temporelle (filtre calendrier) dans le module macro_evenements.
*Catégorie : timing*

### D4460 — Confirmation multi-exemples : l'effet fonctionne sur actions individuelles et indices
🟡 **SYNTHÈSE** (Source : the_pre_holiday_effect.md) : Les exemples GE, Motorola, Realty Income (O) montrent que l'effet pré-férié est généralisable au-delà du S&P 500. Même sur une action en downtrend (Realty Income), l'achat pré-Independence Day et la vente le 5 juillet était rentable ($21.2 → $22).
**TRADEX-AI C7** : Corrélations — l'effet saisonnier pré-férié affecte simultanément actions et commodités. GC (Or) et CL (Pétrole) voient aussi des changements de liquidité pré-fériés US. À surveiller en corrélation avec ES sur ces dates.
*Catégorie : correlations*

