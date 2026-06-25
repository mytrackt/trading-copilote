# Extraction StockCharts — MACD-V (volatility-normalized MACD)

**Source :** `bundles/stockcharts/macd_v.md` (HTTP 200 · ~7 101 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende locale + section fallback) · 1/1 certifiée
**Décisions :** D2471 → D2480 · **Page :** chartschool.stockcharts.com/.../technical-indicators/macd-v
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Périmètre** : famille MACD. Variante **MACD-V** (Alex Spiroglou) — MACD normalisé par la volatilité (ATR). CERCLE momentum **C3**. Le MACD de base est extrait ailleurs.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | MACD-V applied to 10-year Treasury Yields in StockChartsACP | Using MACD-V in StockCharts ACP | D2480 |

---

## DÉCISIONS

### D2471 — MACD-V : créateur, origine, distinctions
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Le MACD-V a été créé par **Alex Spiroglou, CFTe, DipTA (ATAA)**, découvert en 2015 et publié en 2022 dans un papier de recherche. Ce papier a reçu le **Founders Award** de la NAAIM et le **Charles H. Dow Award** (CMT Association) pour recherche exceptionnelle en analyse technique. Objectif : surmonter les limites des indicateurs bornés (RSI, Stochastique) et non bornés (MACD, ROC).
**TRADEX-AI C3** : MACD-V = brique momentum primée et reconnue ; candidate sérieuse pour la couche momentum normalisée.
*Catégorie : indicateurs_momentum*

---

### D2472 — Problème des indicateurs bornés vs non bornés
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Les indicateurs **bornés** (échelle 0–100) ne peuvent pas s'étendre avec le marché : ils se « pegguent » à des niveaux hauts/bas pendant les mouvements forts et sont « biaisés » par les tendances ; mais leur échelle normalisée les rend **comparables** entre marchés et dans le temps. Les indicateurs **non bornés** (prix absolu) ne sont **pas comparables** entre marchés/temps mais s'étendent avec le marché et offrent une forme de momentum « plus vraie ».
**TRADEX-AI C3** : Contexte de conception — justifie le besoin d'un momentum à la fois comparable inter-marché ET extensible. Pertinent pour comparer GC/HG/CL/ZW entre eux.
*Catégorie : indicateurs_momentum*

---

### D2473 — La solution MACD-V : MACD normalisé par la volatilité
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Spiroglou crée un indicateur hybride « le meilleur des deux mondes » — non borné avec échelle normalisée — en **normalisant le MACD par la volatilité**, créant un modèle de cycle de vie du momentum. Il adresse 5 limites du MACD : (1) non comparable dans le temps ; (2) non comparable entre marchés ; (3) pas de cadre de momentum normalisé ; (4) ligne de signal MACD imprécise ; (5) signal MACD n'aide pas au timing.
**TRADEX-AI C3** : MACD-V répond directement au besoin TRADEX d'un momentum comparable entre actifs et calibré au timing.
*Catégorie : indicateurs_momentum*

---

### D2474 — Formule de calcul (normalisation par ATR 26)
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Formule — `MACD-V = [(EMA 12p − EMA 26p) / ATR(26)] × 100` ; `Signal line = EMA 9p du MACD-V` ; `Histogram = MACD-V − Signal Line`. La différence avec le MACD est l'incorporation de la **volatilité (ATR 26)** dans le calcul.
**TRADEX-AI C0** : Formule déterministe à répliquer côté export NinjaScript (besoin OHLC pour l'ATR) ; défaut 12/26/9 + ATR(26).
*Catégorie : indicateurs_momentum*

---

### D2475 — Avantages : stabilité inter-marché, non borné, pattern recognition
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Avantages — (1) **stable entre titres** : applicable aux cryptos, mega-cap tech, matières premières, etc., en gardant les mêmes lectures ; (2) **non borné** : à momentum très élevé, on peut juger de la force du pic car aucune borne 0/100 ne limite l'indicateur ; (3) **permet des stratégies de reconnaissance de patterns** impossibles avec le MACD classique.
**TRADEX-AI C7** : La stabilité inter-marché autorise une comparaison directe du momentum GC/HG/CL/ZW (matrice corrélations 30j) sur une échelle commune.
*Catégorie : indicateurs_momentum*

---

### D2476 — Les 7 stades de momentum (Range Rules) — partie haussière/risque
🔵 **ÉCOLE** (Source : macd_v.md) : Stades de momentum (lecture du niveau MACD-V + position vs ligne de signal) — **1. Risk (oversold)** : MACD-V < −150. **2. Rebounding** : entre −150 et 50 ET au-dessus du signal (remontée depuis un bas). **3. Rallying** : entre 50 et 150 ET au-dessus du signal (forte dynamique haussière). **4. Risk (overbought)** : MACD-V > 150 ET au-dessus du signal.
**TRADEX-AI C3** : Seuils normalisés exploitables tels quels (échelle commune) — armer un filtre de stade momentum (oversold <−150 / overbought >150) sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2477 — Les 7 stades de momentum — partie baissière/range
🔵 **ÉCOLE** (Source : macd_v.md) : **5. Retracing** : MACD-V > −50 ET sous le signal (repli depuis un haut). **6. Reversing** : entre −50 et −150 ET sous le signal (forte dynamique baissière). **7. Ranging** : entre −50 et 50 pendant plus de **20–30 barres** (range court terme). Ces 7 stades forment un cycle de vie du momentum.
**TRADEX-AI C3** : Compléter le filtre de stade (retracing / reversing / ranging) ; le stade « Ranging » (>20–30 barres entre ±50) = signal de non-trade / consolidation sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

### D2478 — Cadre de lecture : position vs ligne de signal détermine le stade
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Le stade dépend conjointement du **niveau** MACD-V ET de sa **position relative à la ligne de signal** (au-dessus = haussier, en dessous = baissier). Plusieurs setups peuvent être conçus à partir de ces 7 ranges.
**TRADEX-AI C3** : Encoder l'état comme couple (niveau, signe MACD-V vs signal) pour une classification déterministe du stade momentum.
*Catégorie : configuration*

---

### D2479 — Version avancée sans ligne de signal
🟢 **FAIT VÉRIFIÉ** (Source : macd_v.md) : Spiroglou a créé une version plus puissante du MACD-V **n'utilisant PAS la ligne de signal**, rendant l'indicateur plus rapide à signaler les changements de momentum et à localiser les hauts/bas pour des stratégies avancées de reconnaissance de patterns.
🔴 **NON VÉRIFIÉ (détail absent)** : Le détail des règles de cette version avancée n'est pas fourni dans la page (mentionné mais non spécifié).
**TRADEX-AI C3** : Variante « sans signal » plus réactive notée comme piste ; règles non documentées ici — ne pas implémenter sans source complémentaire.
*Catégorie : indicateurs_momentum*

---

### D2480 — Disponibilité et paramétrage StockCharts ACP
🔵 **ÉCOLE** (Source : macd_v.md, image_01) : Le MACD-V est un indicateur **standard dans StockCharts ACP**. Accès : Chart Settings → faire défiler les Standard Indicators → sélectionner MACD-V → modifier les paramètres via l'icône de réglages. Exemple illustré : MACD-V appliqué aux rendements des Treasuries 10 ans.
**TRADEX-AI C0** : Référence de paramétrage ; exposer le MACD-V (12/26/9 + ATR 26) en panneau séparé dans l'UI.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2471 → D2480 (10) |
| Images certifiées citées | 1/1 |
| Catégories utilisées | indicateurs_momentum · configuration |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🔴 NON VÉRIFIÉ |
| Belkhayate | **NON CONCERNÉ** (variante MACD pure, aucun lien Belkhayate revendiqué) |
| Cas à vérifier | D2479 : règles de la version « sans ligne de signal » non documentées dans la source |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
