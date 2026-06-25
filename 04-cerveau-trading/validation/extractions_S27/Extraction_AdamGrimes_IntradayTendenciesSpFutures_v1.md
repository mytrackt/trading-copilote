# Extraction AdamGrimes — Intraday Tendencies SP Futures
**Source :** `bundles/adamgrimes/intraday_tendencies_sp_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6131 → D6145 · **Page :** https://www.adamhgrimes.com/intraday-tendencies-sp-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : ES intraday tendencies — contexte C4/timing pour signaux TRADEX (filtrer horaire d'analyse sur GC/CL/ZW selon session ouverte/fermée).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6131 — Tendance intraday ES : 3 phases distinctes
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : Les futures S&P 500 suivent un schéma prévisible en 3 phases — (1) forte tendance dans la première heure et demie après l'ouverture, (2) tendance faible et range vers 14h00 ET, (3) tendance forte à nouveau vers la clôture.
**TRADEX-AI C4** : Pour ES (actif CONFIRMATION), les signaux d'analyse de tendance sont plus fiables dans les plages 09:30–11:00 ET et 15:00–16:00 ET. Éviter d'utiliser ES comme signal de confirmation pendant la zone morte mid-session (~12:00–14:00 ET).
*Catégorie : timing*

### D6132 — Tendance après-midi ES plus forte que le matin
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : Les données montrent que la tendance de l'après-midi (session US) est en moyenne plus forte que celle du matin. Le mouvement directionnel en fin de session surpasse celui de l'ouverture.
**TRADEX-AI C4** : Ne jamais fader (trader contre) une tendance ES forte en fin de session US. Si ES confirme une direction dans la plage 14:30–16:00 ET, ce signal de confirmation a un poids élevé pour les actifs TRADING (GC, CL, ZW).
*Catégorie : timing*

### D6133 — Ne pas trader en range contre la tendance mid-day
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : La plage mid-session (~12:00–14:00 ET) est statistiquement la zone de plus faible tendance sur ES. Les trades directionnels en trend-following y sont les moins efficaces.
**TRADEX-AI C4** : Règle de filtre horaire : si l'heure EST est entre 12:00 et 14:00, réduire le poids de confirmation ES dans la grille de score. Un signal ES mid-day compte moins qu'un signal ES morning ou afternoon.
*Catégorie : timing*

### D6134 — Volume intraday : même sourire que la tendance
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : Le volume (tick volume) suit le même schéma en "sourire" que la force de tendance — fort à l'ouverture, faible au milieu, fort à la clôture. Volume et tendance sont co-incidants.
**TRADEX-AI C2** : Le volume tick sur ES confirme la phase de la session. Faible volume mid-session = range probable = signal de confirmation ES à pondération réduite dans le moteur TRADEX.
*Catégorie : volume_liquidite*

### D6135 — Mesure C%R : fermeture en % du range comme proxy de tendance
🔵 **ÉCOLE** (Source : intraday_tendencies_sp_futures.md) : Le Close as Percent of Range (C%R) — fermeture divisée par le range de la bougie — est un indicateur simple de force de tendance. Une valeur proche de 100% = forte tendance haussière. Valeur inversée (25% → 75%) pour normaliser les baisses.
**TRADEX-AI C1** : Ce concept est applicable à GC, CL, ZW pour mesurer la force d'une bougie individuelle dans le moteur Python. Un C%R > 70% ou < 30% (normalisé) est un signal de force directionnelle à intégrer dans la détection de l'alignement 3/4.
*Catégorie : indicateurs_tendance*

### D6136 — Statistiques de marché à mettre à jour périodiquement
🟡 **SYNTHÈSE** (Source : intraday_tendencies_sp_futures.md) : Les tendances intraday sont stables mais pas figées. Le marché évolue dans ses comportements de façon subtile. Comparer les statistiques récentes à l'historique long est utile pour diagnostiquer si une baisse de performance vient du trader ou du changement de marché.
**TRADEX-AI C4** : La grille de score TRADEX doit pouvoir être recalibrée si les tendances horaires ES changent. Prévoir un mécanisme de comparaison des stats récentes vs historiques dans le module de monitoring (staleness_monitor.py étendu).
*Catégorie : structure_marche*

### D6137 — Principe général : bursts d'activité à l'ouverture et à la clôture
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : Ce pattern (forte activité ouverture/clôture, calme mid-session) s'applique au-delà d'ES — il est décrit comme un principe général valable pour les devises et les commodités.
**TRADEX-AI C4** : Pour GC (Or), CL (Pétrole) et ZW (Blé), anticiper que les meilleurs setups directionnels se forment pendant les sessions actives correspondant à leurs marchés respectifs (CME opening hours). Éviter les signaux produits en pleine zone de faible liquidité inter-session.
*Catégorie : timing*

### D6138 — Timing : être agressif sur les trades tendanciels morning et afternoon
🟢 **FAIT VÉRIFIÉ** (Source : intraday_tendencies_sp_futures.md) : La recommandation explicite est d'être agressif avec les trades en tendance pendant le matin ET l'après-midi, et de ne pas "chopper" l'argent sur des trades de tendance en mid-session.
**TRADEX-AI C4** : Le moteur TRADEX doit appliquer une règle de timing : score de signal pondéré positivement si heure dans la plage 09:30–11:00 ET ou 14:30–16:00 ET pour ES (confirmation). Signal mid-session = malus de pondération dans la grille /10.
*Catégorie : timing*
