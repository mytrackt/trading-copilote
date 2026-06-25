# Extraction Optimus — Index Futures Trading vs Index ETFs
**Source :** `bundles/optimusfutures/index_futures_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image scrappée · 0/0 certifiées · 0 à vérifier
**Décisions :** D8551 → D8570 · **Page :** https://optimusfutures.com/blog/index-futures-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Avantages structurels des futures d'indice (levier, horaires, fiscalité, liquidité) — contexte institutionnel C3 et mécanismes opérationnels de ES/NQ/YM.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image scrappée — bundle texte uniquement) | — | — | — |

## DÉCISIONS

### D8551 — Contrats futures d'indice US : ES, NQ, YM (et leurs micro-contrats)
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Trois contrats principaux : ES (E-mini S&P 500, 500 entreprises, micro = MES), NQ (E-mini Nasdaq-100, 100 entreprises tech, micro = MNQ), YM (Dow Jones, 30 blue-chips, micro = MYM). Tradés sur CME.
**TRADEX-AI C3** : ES et VX (VIX) sont les actifs de confirmation TRADEX. ES = exposition au marché broad US. Dans le score /10, la direction ES est une entrée de la grille déterministe.
*Catégorie : structure_marche*

### D8552 — Levier futures vs ETF : contrôle d'une position bien plus grande que le capital déposé
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Les futures offrent un levier substantiel. Un contrat ES contrôle une exposition >200k$ pour une fraction en marge. Les micro-contrats (MES) offrent une exposition de 5$ par point d'indice, accessibles avec moins de capital.
**TRADEX-AI C3** : Mécanisme de levier applicable aux futurs tradables de TRADEX (GC/HG/CL/ZW). Le risk manager de TRADEX doit dimensionner les positions en tenant compte du levier réel, pas seulement du capital engagé.
*Catégorie : gestion_risque_entree*

### D8553 — Trading quasi-24h/5j : avantage majeur des futures vs ETF
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Les futures tradent quasi-24h/5j permettant de réagir aux news globales quand le cash market est fermé. Les ETFs (SPY, QQQ, DIA) ne tradent que 9h30-16h ET, laissant les traders exposés aux gaps overnight non couverts.
**TRADEX-AI C4** : Justifie la surveillance continue du moteur Python de TRADEX (boucle 2s 24/5). Les matières premières (GC, CL) tradent également quasi-24h — les signaux Belkhayate peuvent se former en dehors des heures US.
*Catégorie : timing*

### D8554 — Avantage fiscal 60/40 sur les futures (Section 1256 US)
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Les gains sur futures bénéficient de la règle 60/40 (Section 1256 US) : 60% des gains imposés au taux long terme, 40% au taux court terme, quelle que soit la durée de détention. Avantage fiscal significatif vs ETF pour les traders actifs.
**TRADEX-AI C3** : Information de contexte institutionnel pour Abdelkrim si trading sur compte US. Non applicable directement dans le moteur mais pertinent pour l'éducation fiscale des utilisateurs du SaaS.
*Catégorie : macro_evenements*

### D8555 — Liquidité supérieure des futures : spreads plus étroits et coûts de transaction réduits
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Les grands contrats futures (ES, NQ, Dow) bénéficient d'une liquidité élevée → spreads bid-ask étroits → coûts de transaction inférieurs vs ETF pour les traders actifs.
**TRADEX-AI C2** : Liquidité élevée = slippage réduit sur les entrées/sorties. Pour TRADEX sur GC/CL (actifs liquides CME), les conditions de liquidité doivent être monitorées via le volume C2 avant de valider une entrée ordre flow.
*Catégorie : volume_liquidite*

### D8556 — Risque de volatilité amplifié par le levier : sizing critique
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : Le levier amplifie profits ET pertes. Une petite variation défavorable peut causer des pertes significatives si la position est surdimensionnée. Risque de "going debit" : perdre plus que le capital du compte si le risk management est absent.
**TRADEX-AI C1** : Règle absolue de TRADEX : le risk_manager.py doit calculer le sizing maximal en fonction du capital disponible et du levier du contrat. Mode Auto BLOQUÉ par défaut précisément pour éviter un "going debit" automatisé.
*Catégorie : gestion_risque_entree*

### D8557 — Complexité des futures : dates d'expiration et rollover obligatoires
🔵 **ÉCOLE** (Source : index_futures_trading.md) : Les futures ont des dates d'expiration. Les traders doivent "roller" (passer au contrat suivant) avant l'expiration ou fermer la position. Les ETFs n'expirent pas, ce qui les rend plus simples pour les détenteurs passifs.
**TRADEX-AI C1** : Dans TRADEX, les données NT8 portent le code du contrat actif (front-month). Le data_reader.py doit gérer le changement de contrat lors des rollovers (trimestriels pour GC, CL, HG, ZW) pour éviter des lectures de données erronées.
*Catégorie : configuration*

### D8558 — Index ETFs : instruments simples pour les investisseurs long-terme, pas pour le day trading
🔵 **ÉCOLE** (Source : index_futures_trading.md) : Les ETFs (SPY, QQQ, DIA) sont adaptés aux investisseurs buy-and-hold de long terme cherchant une exposition simple aux indices sans complexité de levier, d'expiration ou d'appel de marge. Pas l'outil optimal pour le day trading actif.
**TRADEX-AI C4** : Contexte éducatif : TRADEX utilise les futures ES/VX comme actifs de confirmation (pas d'ordres sur ces actifs) en cohérence avec leur supériorité pour l'analyse de marché intraday.
*Catégorie : structure_marche*

### D8559 — Spécifications contrats : Dow (YM) = 30 blue-chips; Nasdaq (NQ) = 100 tech; S&P (ES) = 500 large-caps
🟢 **FAIT VÉRIFIÉ** (Source : index_futures_trading.md) : YM/MYM : Dow Jones 30 grandes valeurs industrielles blue-chip. NQ/MNQ : Nasdaq-100 100 plus grandes non-financières (dominance tech). ES/MES : S&P 500 les 500 plus grandes cotées US tous secteurs.
**TRADEX-AI C7** : Ces distinctions de composition expliquent les divergences de comportement entre les 3 contrats (C7 corrélations). ES est le baromètre macro le plus large ; NQ le plus sensible au risk-off tech ; YM le plus stable en période de rotation value.
*Catégorie : correlations*

### D8560 — Futures adaptés aux day traders : levier + horaires + liquidité + fiscalité = avantage combiné
🟡 **SYNTHÈSE** (Source : index_futures_trading.md) : Pour les day traders cherchant à capitaliser rapidement sur les mouvements d'indice, les futures cumulent 4 avantages : levier élevé, trading quasi-24h, meilleure liquidité/spreads, avantage fiscal 60/40. Les ETFs sont supérieurs pour buy-and-hold passif uniquement.
**TRADEX-AI C4** : Confirme l'architecture TRADEX : utiliser les futures (GC/HG/CL/ZW) pour les ordres, ES/VX en confirmation, surveillance quasi-24h par le moteur Python. La combinaison levier+liquidité+horaires justifie l'approche futures-only du système.
*Catégorie : structure_marche*
