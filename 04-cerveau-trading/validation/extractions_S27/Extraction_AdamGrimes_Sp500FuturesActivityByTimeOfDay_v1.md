# Extraction AdamGrimes — S&P 500 Futures Activity By Time Of Day
**Source :** `bundles/adamgrimes/sp_500_futures_activity_by_time_of_day.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image présente dans ce bundle
**Décisions :** D6691 → D6700 · **Page :** https://www.adamhgrimes.com/sp-500-futures-activity-by-time-of-day/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 312 (ES time of day) — DIRECTEMENT pertinent pour C4 (Macro/Timing) : fenêtres open/close ES à surveiller comme confirmation ; midday dead zone à exclure des analyses de tendance ES.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6691 — Concentration du volume ES sur open et close (2013-2018)
🟢 **FAIT VÉRIFIÉ** (Source : sp_500_futures_activity_by_time_of_day.md) : Dans la période 2013-2018, près de 20 % du volume journalier des futures S&P 500 (ES) se concentre sur les 15 premières et les 15 dernières minutes de la session. Cette concentration est nettement plus forte que dans la période 2003-2008.
**TRADEX-AI C4** : Pour la confirmation ES (actif Catégorie 2), les signaux TRADEX générés en dehors des fenêtres open/close auront une liquidité réduite ; pondérer la confirmation ES différemment selon l'heure de la session.
*Catégorie : timing*

### D6692 — Activité de range concentrée à l'open plutôt qu'étalée
🟢 **FAIT VÉRIFIÉ** (Source : sp_500_futures_activity_by_time_of_day.md) : L'activité de range (amplitude de prix par tranche de 15 min) est davantage concentrée sur l'ouverture dans la période récente, alors qu'elle était auparavant étalée sur la première heure. La fenêtre d'exploitation du range s'est donc réduite.
**TRADEX-AI C4** : Pour les actifs de confirmation (ES), les mouvements directionnels significatifs se produisent dans un laps de temps plus court qu'auparavant ; réduire la fenêtre de lecture de tendance ES en intraday.
*Catégorie : timing*

### D6693 — Zone morte de midi (heure de Chicago) — stable sur deux décennies
🟢 **FAIT VÉRIFIÉ** (Source : sp_500_futures_activity_by_time_of_day.md) : La période de faible activité ("dead zone") autour de l'heure du déjeuner à Chicago est visible sur les deux périodes (2003-2008 et 2013-2018), ainsi qu'une petite remontée d'activité vers 14:00 EDT marquant le début des tendances de l'après-midi.
**TRADEX-AI C4** : Eviter de prendre une confirmation ES comme signal fort en midday (Chicago lunch ≈ 12:00-13:00 CDT / 13:00-14:00 EDT) ; privilégier les confirmations ES sur la reprise de l'après-midi (14:00 EDT) pour les signaux TRADEX sur GC/HG/CL/ZW.
*Catégorie : timing*

### D6694 — Volume after-close ES en augmentation significative
🟢 **FAIT VÉRIFIÉ** (Source : sp_500_futures_activity_by_time_of_day.md) : Le volume après la clôture officielle (after-close) a augmenté de façon notable dans la période récente par rapport à 2003-2008, suggérant une activité institutionnelle accrue hors session.
**TRADEX-AI C4** : Les mouvements ES after-close peuvent préfigurer l'orientation de la session suivante ; surveiller les gaps ES overnight comme filtre de confirmation macro avant l'ouverture des marchés sur GC, HG, CL, ZW.
*Catégorie : timing*

### D6695 — Réduction progressive de la fenêtre intraday exploitable
🟡 **SYNTHÈSE** (Source : sp_500_futures_activity_by_time_of_day.md) : L'auteur conclut que la fenêtre d'activité exploitable pour le day-trading se réduit d'heure en heure vers quelques minutes à l'open et à la close, rendant le trading de mi-séance de moins en moins pertinent.
**TRADEX-AI C4** : Pour TRADEX, les signaux de confirmation ES sont les plus fiables dans les 15 premières minutes et les 15 dernières minutes de la session CME (08:30-08:45 CDT et 14:45-15:00 CDT pour les futures ES) ; pondérer la confirmation ES à 0 en midday si le module de timing est activé.
*Catégorie : timing*

### D6696 — Hypothèse ETF/ETP comme moteur de concentration du volume
⚫ **HYPOTHÈSE PROJET** (Source : sp_500_futures_activity_by_time_of_day.md) : Adam Grimes formule l'hypothèse que la concentration accrue du volume sur open/close serait liée aux besoins de rebalancement des ETF/ETP à levier, dont le rebalancement journalier obligatoire crée un afflux mécanique de volume en fin de session.
**TRADEX-AI C5** : Cette mécanique de rebalancement ETF sur ES à la clôture peut générer des faux signaux de momentum en fin de session ; ne pas interpréter un spike de volume ES dans les 15 dernières minutes comme signal directionnel confirmé.
*Catégorie : volume_liquidite*

### D6697 — Tendance mid-séance à la baisse de liquidité — évolution structurelle du marché
🟡 **SYNTHÈSE** (Source : sp_500_futures_activity_by_time_of_day.md) : Les données montrent que la réduction du volume midday n'est pas cyclique mais reflète une évolution structurelle du marché sur une décennie, vraisemblablement liée à l'institutionnalisation et à l'algorithmisation des marchés.
**TRADEX-AI C7** : Les corrélations calculées sur GC/HG/CL/ZW vs ES doivent être pondérées par l'heure de session ; une corrélation calculée sur données midday ES sera structurellement moins fiable qu'une corrélation calculée sur open/close.
*Catégorie : correlations*

### D6698 — Forme globale de la distribution volume/range stable sur deux décennies
🟢 **FAIT VÉRIFIÉ** (Source : sp_500_futures_activity_by_time_of_day.md) : Malgré les évolutions quantitatives (concentration accrue sur open/close), la forme générale de la distribution du volume et du range par tranche de 15 min reste stable : hausse à l'open, creux à midi, remontée à la clôture.
**TRADEX-AI C4** : Le pattern temporel bimodal (open/close) d'ES est robuste et peut être utilisé comme grille de référence pour calibrer les fenêtres de confirmation ES dans le moteur TRADEX.
*Catégorie : saisonnalite*

### D6699 — NQ (Nasdaq futures) vraisemblablement similaire à ES
⚫ **HYPOTHÈSE PROJET** (Source : sp_500_futures_activity_by_time_of_day.md) : L'auteur mentionne vouloir vérifier si le NQ présente le même profil que l'ES, supposant a priori une ressemblance forte. Aucune donnée NQ fournie dans ce bundle.
**TRADEX-AI C4** : En l'absence de données NQ dans ce bundle, extrapoler le profil ES au NQ avec précaution ; cette décision reste à confirmer. Non applicable directement à TRADEX (NQ n'est pas un actif de confirmation), retenu pour information générale.
*Catégorie : timing*

### D6700 — Activité intraday ES comme proxy de timing inter-marchés
🟡 **SYNTHÈSE** (Source : sp_500_futures_activity_by_time_of_day.md) : La concentration du volume et du range ES sur l'open et la close implique que les corrélations GC/HG/CL/ZW vs ES seront les plus fortes dans ces mêmes fenêtres temporelles, rendant la confirmation ES plus pertinente en début et fin de session.
**TRADEX-AI C7** : Implementer un filtre temporel dans le module de corrélations C7 : les corrélations GC-ES, HG-ES, CL-ES et ZW-ES calculées sur des données d'open (08:30-09:00 CDT) et de close (14:30-15:00 CDT) seront pondérées positivement ; les données midday pondérées négativement.
*Catégorie : correlations*
