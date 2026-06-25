# Extraction NinjaTrader — Volume Analysis in Futures Trading
**Source :** `bundles/ninjatrader/volume_analysis_in_futures_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8191 → D8210 · **Page :** https://ninjatrader.com/futures/blogs/volume-analysis-in-futures-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Confirmation de tendance et identification de retournements via volume (C2 Order Flow) pour les actifs GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8191 — Volume comme validateur de mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : volume_analysis_in_futures_trading.md) : Un fort mouvement de prix accompagné d'un volume élevé indique que les traders supportent le mouvement, lui conférant plus de durabilité. Un mouvement avec volume faible suggère un manque de conviction.
**TRADEX-AI C2** : En C2 (Order Flow), vérifier que chaque signal de tendance sur GC/HG/CL/ZW est accompagné d'un volume supérieur à la moyenne pour valider l'entrée.
*Catégorie : volume_liquidite*

### D8192 — Quadrant Dow : 4 scenarios volume/prix
🔵 **ÉCOLE** (Source : volume_analysis_in_futures_trading.md) : Principe de Charles Dow — (1) Prix ↑ + Volume ↑ = confirmation haussière (acheteurs actifs) ; (2) Prix ↑ + Volume ↓ = divergence baissière (momentum s'affaiblit) ; (3) Prix ↓ + Volume ↑ = confirmation baissière (pression vendeuse forte) ; (4) Prix ↓ + Volume ↓ = divergence haussière (vendeurs perdent de l'intérêt).
**TRADEX-AI C2** : Appliquer cette grille à chaque signal TRADEX-AI sur les 4 actifs tradables pour discriminer signal fort (cas 1 ou 3) vs signal douteux (cas 2 ou 4).
*Catégorie : volume_liquidite*

### D8193 — Moyenne mobile 20 jours sur le volume
🔵 **ÉCOLE** (Source : volume_analysis_in_futures_trading.md) : Une moyenne mobile simple 20 jours sur le volume sert de référence pour évaluer si le volume actuel est fort ou faible. Particulièrement utile en périodes saisonnières à faible liquidité (vacances, fin d'année).
**TRADEX-AI C2** : Intégrer une SMA 20 sur le volume dans data_reader.py pour qualifier chaque signal : volume actuel > SMA20 = signal fort ; volume actuel < SMA20 = signal à pondérer négativement dans la grille /10.
*Catégorie : volume_liquidite*

### D8194 — Volume smile intraday
🟡 **SYNTHÈSE** (Source : volume_analysis_in_futures_trading.md) : En intraday, le volume forme une courbe en "sourire" (smile) : pic à l'ouverture, creux en milieu de session, remontée vers la clôture. Ce pattern est caractéristique des marchés à terme liquides.
**TRADEX-AI C2** : Pour les signaux intraday sur GC/CL notamment, tenir compte de la période de faible volume (milieu de session) : un signal détecté en creux de volume smile est moins fiable qu'un signal à l'ouverture ou à la clôture.
*Catégorie : timing*

### D8195 — Volume Profile : cartographie du volume par niveau de prix
🟢 **FAIT VÉRIFIÉ** (Source : volume_analysis_in_futures_trading.md) : Le Volume Profile mappe le volume sur les niveaux de prix (et non dans le temps), révélant le Point of Control (POC) = niveau de prix avec le plus grand volume échangé, et la Value Area = zone où 70% du volume total a été échangé.
**TRADEX-AI C2** : Le POC et les bornes de la Value Area constituent des niveaux de support/résistance objectifs basés sur l'activité réelle des participants. À intégrer en C2 comme zones d'intérêt prioritaires pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D8196 — Value Area : zone de 70% du volume
🟢 **FAIT VÉRIFIÉ** (Source : volume_analysis_in_futures_trading.md) : La Value Area contient 70% du volume total échangé sur la période. Les bornes hautes (VAH) et basses (VAL) de cette zone agissent comme support et résistance dynamiques.
**TRADEX-AI C2** : Une entrée longue sous le VAL ou une entrée courte au-dessus du VAH offre un contexte de mean reversion vers le POC. Règle complémentaire à intégrer dans la grille de décision pour C2.
*Catégorie : structure_marche*

### D8197 — VWAP comme "juste valeur" de session
🟢 **FAIT VÉRIFIÉ** (Source : volume_analysis_in_futures_trading.md) : Le VWAP calcule le prix moyen de tous les trades pondéré par le volume sur une session. Il représente la "juste valeur" du contrat selon l'activité réelle. Les traders institutionnels l'utilisent comme benchmark d'exécution.
**TRADEX-AI C2** : Le VWAP est un niveau dynamique de support/résistance intraday. Un signal sur GC/HG/CL/ZW au-dessus du VWAP est haussier ; en dessous est baissier. Renforce ou affaiblit un signal selon sa position par rapport au VWAP.
*Catégorie : volume_liquidite*

### D8198 — VWAP avec bandes d'écart-type
🔵 **ÉCOLE** (Source : volume_analysis_in_futures_trading.md) : L'ajout de bandes d'écart-type au VWAP crée des zones reflétant les plages de trading attendues, aidant les traders à définir des points d'entrée et de sortie dans le contexte de la session.
**TRADEX-AI C2** : Les bandes VWAP ±1σ et ±2σ définissent des zones d'extension et de retour potentiel. Complémentaire au Z-score (D8231+). À implémenter dans le moteur de données intraday NT8.
*Catégorie : gestion_risque_entree*

### D8199 — Volume analyse : anti-exhaustion de tendance
🟡 **SYNTHÈSE** (Source : volume_analysis_in_futures_trading.md) : L'analyse du volume permet de détecter l'exhaustion d'une tendance avant que le prix ne la révèle. Prix en hausse avec volume décroissant = signal d'affaiblissement possible = timing de sortie ou de prudence.
**TRADEX-AI C2** : Avant de valider un signal ACHETER sur une tendance haussière établie, vérifier que le volume confirme. Volume décroissant sur rallye = attendre ou réduire la taille de position.
*Catégorie : gestion_position_active*

### D8200 — Volume analysis comme couche d'analyse au-delà du prix seul
🔵 **ÉCOLE** (Source : volume_analysis_in_futures_trading.md) : Le volume ajoute contexte et clarté à la prise de décision : il aide à évaluer la validité des mouvements de prix, à anticiper les points de retournement potentiels, et à mieux comprendre où les autres participants de marché sont les plus actifs.
**TRADEX-AI C2** : Principe fondateur de C2 dans l'architecture TRADEX-AI : volume = validation obligatoire de tout signal de prix C1. Sans confirmation C2, le signal C1 reste hypothétique.
*Catégorie : configuration*
