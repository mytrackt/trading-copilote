# Extraction Sierra Chart — Volume by Price (Volume Profile)

**Source :** `bundles/sierrachart/sierra_141_volume_by_price.md` (HTTP 200 · ~175 609 car.) + 0 image
**Méthode images :** ancrage figcaption locale (STATIC) — **0 figure `<figure>+<figcaption>` sur la page** → 0 certifiée / 0 à vérifier (cf. manifest)
**Décisions :** D419 → D429 · **Page :** sierrachart.com/index.php?page=doc/StudiesReference.php&ID=141
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** — le Volume Profile alimente le **Cercle C2 (order flow / structure de marché)**. POC, Value Area, HVN/LVN (Peaks/Valleys) et VWAP sont les niveaux de référence d'order flow exploitables sur GC/HG/CL/ZW.
> ⚠️ **Filtrage volontaire** : la page Sierra Chart est massivement consacrée aux paramètres logiciels (Draw Mode, couleurs, Subgraphs SG2–SG21, alignements, menus). Ces éléments sont **IGNORÉS**. Ne sont retenus que les faits TRADING : ce que mesure le Volume Profile et comment le lire.

---

## INVENTAIRE IMAGES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | aucune figure `<figure>+<figcaption>` exploitable sur la page | — | — |

> Les 3 « Example Chart Images » mentionnées dans le texte (Visible Bars, 1 Day profiles bid/ask, 1 Bar par profil) n'ont **pas** de légende ancrable → non certifiées, non citées.

---

## DÉCISIONS

### D419 — Volume by Price : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Le Volume by Price superpose un **Volume Profile** pour chaque période sur un graphique en barres. Le volume cumulé à **chaque incrément de prix** sur une période donnée est affiché sous forme de **barres horizontales** en arrière-plan du graphique. C'est une lecture du volume **par niveau de prix** (et non par unité de temps).
**TRADEX-AI C2** : Brique « volume par niveau de prix » — donne la carte de l'activité d'order flow sur GC/HG/CL/ZW ; identifie où le marché a accepté/refusé le prix.
*Catégorie : structure_marche*

---

### D420 — Point of Control (POC)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Le **Point of Control (POC)** est la **barre de volume la plus haute** du profil (le niveau de prix avec le plus de volume échangé) — littéralement « the volume bar with the highest volume ». Sierra Chart peut l'étendre vers la droite (End of Period / Until Future Intersection) jusqu'à intersection d'un profil futur.
**TRADEX-AI C2** : Le POC = prix de plus forte acceptation / aimant de prix. À exporter comme niveau de référence C2 sur GC/HG/CL/ZW ; un POC étendu non encore touché = cible / zone de réaction probable.
*Catégorie : structure_marche*

---

### D421 — Value Area et Value Area Percentage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : La **Value Area** est composée des barres de volume **centrées sur et autour du POC** qui représentent le **Value Area Percentage du volume total** du profil. Le pourcentage est réglable (Value Area Percentage). [Convention de marché non explicitée par la source : 70 % typique — ⚠️ à vérifier, non littéral ici.]
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : La **Value Area High (VAH)** et la **Value Area Low (VAL)** bornent cette zone ; elles sont disponibles comme Subgraphs et peuvent être tracées en lignes.
**TRADEX-AI C2** : VAH/VAL = bornes de la zone de juste valeur. Hors Value Area = zone de déséquilibre. Exporter VAH/VAL comme niveaux de structure pour GC/HG/CL/ZW (rejet vers la VA = retour à la valeur ; acceptation hors VA = continuation).
*Catégorie : structure_marche*

---

### D422 — Peaks et Valleys (HVN / LVN)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Un **Peak** (pic) est une barre dont les barres au-dessus ET en dessous ont un volume **inférieur** (selon une sensibilité de N ticks au-dessus/en dessous). Une **Valley** (vallée) est une barre dont les barres au-dessus ET en dessous ont un volume **supérieur ou égal**. Peaks et Valleys sont **toujours calculés sur le Total Volume** (insensibles au Volume Bar Calculation Method).
**TRADEX-AI C2** : Peak = **HVN** (high volume node = acceptation, prix « collant »/support-résistance). Valley = **LVN** (low volume node = rejet, prix traversé vite → zone de cassure rapide). Exporter HVN/LVN comme niveaux d'order flow sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D423 — Volume Weighted Average Price (VWAP) du profil
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : L'étude fournit le **Volume Weighted Average Price (VWAP)** pour chaque Volume Profile et chaque barre, disponible comme Subgraph et traçable / extensible en ligne.
**TRADEX-AI C2/C1** : VWAP du profil = prix moyen pondéré volume de la période → référence d'équilibre intra-période. À exporter comme niveau dynamique de structure pour GC/HG/CL/ZW (prix au-dessus/en dessous du VWAP = biais acheteur/vendeur de la session).
*Catégorie : structure_marche*

---

### D424 — Bid Volume / Ask Volume par niveau (delta)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Chaque barre de volume peut être décomposée en **Bid Volume** et **Ask Volume**, et l'étude peut afficher leur différence (`Ask Volume - Bid Volume`, `Bid Volume - Ask Volume`). ⚠️ Cette décomposition **n'existe que si le service de données fournit le bid/ask historique** ; sinon la portion non attribuée est dessinée en couleur de remplissage standard.
**TRADEX-AI C2** : Delta par niveau (Ask−Bid) = pression acheteuse/vendeuse à chaque prix → cœur de l'order flow C2. Dépendance données : sur GC/HG/CL/ZW via Rithmic/ATAS, vérifier la disponibilité bid/ask avant d'exploiter ce delta.
*Catégorie : structure_marche*

---

### D425 — Developing POC / Developing Value Area
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Avec **Calculate Developing POC and Value Area = Yes**, le POC, la VAH et la VAL contiennent à **chaque barre** les valeurs calculées **jusqu'à ce moment précis** (et non la valeur figée de toute la période). On voit ainsi le POC/VA « se développer » au fil de la session.
**TRADEX-AI C2** : Le developing POC/VA permet un suivi temps réel de la migration de la valeur intra-session sur GC/HG/CL/ZW (migration du POC = direction de l'acceptation). Plus exploitable en mode live qu'un profil figé.
*Catégorie : structure_marche*

---

### D426 — Mean Price et bandes d'écart-type (volume)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Avec **Calculate Mean Price and Standard Deviation Bands = Yes**, l'étude calcule le **Trade Weighted Mean Price** et des bandes **± 1 σ** et **± 2 σ** autour de ce prix moyen.
**TRADEX-AI C2** : Mean Price ± σ = mesure de dispersion de la distribution de volume → bornes statistiques de la valeur. ± 2 σ = extrêmes de distribution (zones de réversion potentielle) pour GC/HG/CL/ZW. Confirmation, jamais entrée seule.
*Catégorie : signal*

---

### D427 — Périodes de profil (1 jour, semaine, session, bar count…)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Le **Volume Graph Period Type** est le réglage le plus important : il définit la durée de chaque profil et s'il y en a un ou plusieurs. Options notables côté trading : profils **1 jour** (Multiple Profiles Based on Fixed Time, Days=1), **profil de session** (From Session Start Time to End), **profil composite multi-jours**, **1 profil par barre**, **profil par volume atteint** (Specified Volume).
**TRADEX-AI C2** : Le choix de période détermine le sens du POC/VA (POC de session vs POC composite). Pour GC/HG/CL/ZW : profil de session pour l'intraday, profil composite N jours pour les niveaux structurels majeurs. Aligner la période sur le timeframe de décision Belkhayate.
*Catégorie : structure_marche*

---

### D428 — Précision : données tick-by-tick et Tick Size requis
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : Pour une bonne précision, les enregistrements Intraday doivent être **1 Tick ou 1 Seconde**. Si les enregistrements sont d'un timeframe plus large, le volume d'un niveau de prix est **estimé par moyenne** (volume total ÷ nombre de prix dans la plage de la barre) → profil **approximatif**. Le **Tick Size** doit être correct : trop petit = lenteur/CPU ; trop grand = profil peu précis ; non multiple du vrai tick = volume mal mappé.
**TRADEX-AI C0/C2** : Garde-fou data — n'exploiter le Volume Profile C2 sur GC/HG/CL/ZW qu'avec un flux tick-by-tick (Rithmic) et un Tick Size correct ; sinon POC/VA/HVN/LVN sont approximatifs et ne doivent pas armer un signal.
*Catégorie : gestion_risque_entree*

---

### D429 — Lecture combinée : niveaux de référence, jamais isolés
🟢 **FAIT VÉRIFIÉ** (Source : sierra_141_volume_by_price.md) : L'étude fournit un ensemble cohérent de niveaux dérivés du même profil — POC, VAH, VAL, VWAP, Peaks/Valleys (HVN/LVN), Mean ± σ — tous extensibles en lignes vers le futur jusqu'à intersection d'un profil ultérieur.
🟡 **CONVENTION** : Hiérarchiser la confluence — un niveau de prix sur GC/HG/CL/ZW est plus fort quand **plusieurs** repères de profil coïncident (ex. POC = VAH d'un profil antérieur = HVN).
**TRADEX-AI C2/C3** : Score de signal — pondérer un niveau d'order flow par le **nombre de repères de profil en confluence** ; ne jamais déclencher sur un POC seul. Confirmation price action Belkhayate requise (cf. règle 3/4 trading + 2/3 confirmation).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D419 → D429 (11) |
| Images certifiées citées | 0 (aucune figure légendée sur la page · cf. manifest) |
| Catégories utilisées | structure_marche · signal · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🟡 CONVENTION |
| Cercle TRADEX-AI | **C2 (order flow / structure de marché)** — page PRIORITAIRE |
| Belkhayate | **NON concerné** — Volume Profile = outil C2 indépendant de la méthode prix Belkhayate (complémentaire, pas substitut) |
| Cas « à vérifier » | D421 : la valeur conventionnelle 70 % de la Value Area **n'est PAS** littérale dans la source (le % est seulement « réglable ») → marqué à vérifier, non affirmé 🟢 |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
