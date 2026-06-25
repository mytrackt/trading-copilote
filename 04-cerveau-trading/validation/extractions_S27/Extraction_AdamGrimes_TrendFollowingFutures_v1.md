# Extraction AdamGrimes — Trend Following Futures
**Source :** `bundles/adamgrimes/trend_following_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7151 → D7170 · **Page :** https://www.adamhgrimes.com/trend-following-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 335 — trend following futures DIRECTEMENT GC/CL/HG/ZW. Canaux Donchian validés sur futures, résultats quantitatifs présentés. Applicable stratégie système TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Images charts mentionnées dans le texte mais non présentes dans le bundle | — | — |

---

## DÉCISIONS

### D7151 — Channel breakout (Donchian) : méthode trend-following validée sur futures
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Le breakout de canal (Donchian channels) est une méthode de trend-following reconnue et testée empiriquement sur les marchés futures. Elle a servi de base aux "Turtles" (Richard Dennis) et reste valide. Grimes la publie quotidiennement dans sa recherche pour Waverly Advisors.
**TRADEX-AI C1** : Les canaux Donchian 20/50 jours sur GC, CL, HG, ZW constituent un signal de trend-following quantitativement validé sur futures — intégrable comme composante du cercle C1 dans la grille /10.
*Catégorie : indicateurs_tendance*

### D7152 — Test de tendance sur futures : biais haussier ET baissier confirmé
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Test quantitatif sur un ensemble de marchés futures : achat au breakout du plus haut 50 jours → retours moyens positifs après le signal. Vente au breakout du plus bas 50 jours → retours moyens négatifs (profitables en short). Les deux directions fonctionnent.
**TRADEX-AI C1** : Sur CL (pétrole), les breakouts 50 jours sont exploitables à la hausse ET à la baisse — valider l'inclusion de ce filtre dans la grille TRADEX pour les actifs tradables GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D7153 — Whipsaws et drawdowns : coût psychologique du trend-following systématique
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Le trend-following sur canal génère des whipsaws (faux signaux répétés) et des drawdowns difficiles psychologiquement, même quand le système est rentable sur un grand échantillon. Beaucoup de traders abandonnent le système pendant les mauvaises passes alors qu'il fonctionne.
**TRADEX-AI C5** : Le garde-fou de suspension Mode Auto (15-60 min après perte) protège exactement contre ce comportement. Le score /10 ≥ 7,0 réduit les faux signaux en exigeant la confluence multi-cercles.
*Catégorie : psychologie*

### D7154 — Test robuste : comparer au rendement baseline (buy & hold)
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Tout test de système doit inclure le rendement baseline (buy & hold sur le même marché) pour évaluer l'alpha réel. Un système profitable peut simplement capturer le beta du marché sans valeur ajoutée. La significativité statistique est nécessaire — pas seulement le P&L brut.
**TRADEX-AI C1** : Lors du backtest des signaux Belkhayate sur GC/HG/CL/ZW, toujours comparer avec le rendement buy-and-hold de référence sur la même période. Critère documenté dans DETTE_TECHNIQUE.md pour la Phase C.
*Catégorie : configuration*

### D7155 — Test joint (système + règles) : problème méthodologique fondamental
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Tout backtest de système est un test conjoint de (1) la tendance de fond potentielle du marché ET (2) les règles spécifiques imposées (entrée, sortie, durée de détention, stop). Les choix de paramètres peuvent masquer ou exagérer l'edge réel. Changer la durée de détention ou le stop change radicalement les résultats.
**TRADEX-AI C1** : Le backtest COG Belkhayate (daily invalide, S11) illustre exactement ce problème. La validation réelle nécessite les range bars NT8 Phase C — décision verrouillée.
*Catégorie : configuration*

### D7156 — Event study approach : tester la tendance brute sans règles de sortie
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Grimes préfère les "event studies" : définir une condition simple, enregistrer ce qui se passe sur une fenêtre temporelle après chaque occurrence, comparer aux retours baseline. Cette approche isole la tendance pure sans biais introduit par les règles de sortie.
**TRADEX-AI C1** : Pour valider les signaux Belkhayate sur GC/CL, adopter la méthodologie event study : enregistrer les retours 1j/3j/5j/10j après chaque signal ≥ 7,0, comparer au baseline marché. Faisable en Phase C avec données NT8.
*Catégorie : configuration*

### D7157 — Filtre 20 jours minimum entre entrées : réduire autocorrélation
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Dans le test Donchian 50 jours sur futures, Grimes applique un filtre de 20 jours minimum entre deux entrées dans la même direction. Les résultats sont similaires avec ou sans ce filtre — mais il reste utile pour éviter de compter des trades liés au même mouvement.
**TRADEX-AI C1** : Pour le Rate Limiting TRADEX (max 1 analyse/10s), ajouter une logique de filtre : pas de nouveau signal Donchian dans le même actif si le signal précédent date de moins de 20 barres.
*Catégorie : gestion_risque_entree*

### D7158 — Canaux 20 jours vs 50 jours : deux échelles de signal utiles
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Grimes montre simultanément les canaux 20 et 50 jours sur le marché CL. Les deux sont utiles — le canal 20 jours pour les signaux intermédiaires, le canal 50 jours pour les tendances de fond. Leur croisement peut identifier les confirmations.
**TRADEX-AI C1** : Dual Donchian (20j + 50j) applicable sur GC/CL NT8 : signal fort quand le breakout 20j se produit dans la direction du trend 50j. À intégrer dans la grille /10 comme composante C1.
*Catégorie : indicateurs_tendance*

### D7159 — CL (crude oil) : marché adapté au trend-following
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Le marché des futures pétrole (CL) est utilisé par Grimes comme exemple principal pour illustrer les canaux Donchian — et le short au bottom channel aurait été "très profitable" sur la période montrée. CL est explicitement nommé comme marché adapté.
**TRADEX-AI C1** : CL est un actif TRADING TRADEX (Catégorie 1). Les signaux Donchian sur CL sont à inclure en priorité dans les tests de validation Phase C.
*Catégorie : indicateurs_tendance*

### D7160 — Futures trend-following : applicable aux stocks et devises également
🟡 **SYNTHÈSE** (Source : trend_following_futures.md) : Grimes conclut en annonçant l'extension du test aux stocks et aux devises. La méthode event study est universelle — mais les résultats peuvent différer selon les marchés (structure microstructure, liquidité, régime macro différents).
**TRADEX-AI C4/C7** : Pour TRADEX, la corrélation inter-marché (C7) entre GC et DX, GC et ES, CL et DX doit être testée via la même méthodologie event study — signaux Donchian sur un actif de confirmation précèdent-ils les moves sur les actifs tradables ?
*Catégorie : correlations*

### D7161 — Robustesse du système : résultats stables avec ou sans filtre
🟢 **FAIT VÉRIFIÉ** (Source : trend_following_futures.md) : Un bon système de trading montre des résultats robustes avec des variations mineures des paramètres. Le fait que les résultats Donchian soient "peu changés avec ou sans le filtre 20 jours" est un signal de robustesse réelle et non d'over-fitting.
**TRADEX-AI C1** : Critère de validation pour les paramètres Belkhayate (ex. COGParams 180/3) : tester avec ±20% de variation des paramètres — si les résultats s'effondrent, le système est overfit et non robuste.
*Catégorie : configuration*
