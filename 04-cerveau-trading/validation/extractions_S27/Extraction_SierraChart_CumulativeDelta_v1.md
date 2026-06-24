# Extraction Sierra Chart — Cumulative Delta Bars (Volume)

**Source :** `bundles/sierrachart/sierra_292_cumulative_delta_volume.md` (HTTP 200) + 0 image
**Méthode images :** ancrage figcaption locale (STATIC) · 0/0 — aucune figure `<figure>+<figcaption>` sur la page
**Décisions :** D439 → D450 · **Page :** sierrachart.com/index.php?page=doc/StudiesReference.php&ID=292
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** pour le **Cercle C2 (order flow)**. Le Cumulative Delta (Volume) mesure le delta cumulé = volume acheteur (Ask) − volume vendeur (Bid) au marché, agrégé sur la journée ou le chart. Source = **Sierra Chart** (référence de calcul, revendiqué « 100% correctement calculé »). Cette extraction est **complémentaire** de l'angle NinjaTrader du delta (traité séparément). Les faits ci-dessous sont 🟢 quand littéraux.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | (aucune figure sur la page) | — | — |

*Bilan manifest : 0 certifiée · 0 à vérifier · 0 décorative.*

---

## DÉCISIONS

### D439 — Cumulative Delta Bars (Volume) : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Le Cumulative Delta Bars - Volume est la **somme cumulée**, sur les données du chart ou sur la journée de trading, de la **différence entre l'Ask Volume et le Bid Volume**, affichée en bougies (CandleStick) High-Low. L'étude ne fonctionne que sur les **charts Intraday**.
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Sierra Chart revendique un calcul « 100% correct », basé sur un Bid Volume et un Ask Volume exacts ; la page avertit qu'une comparaison directe avec d'autres programmes (ex. TradingView, cité comme ne fournissant pas un vrai Cumulative Delta) n'est pas possible.
**TRADEX-AI C2** : Le delta cumulé = brique order flow centrale ; mesure la pression Ask vs Bid agrégée pour lire l'agressivité acheteuse/vendeuse sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D440 — Définition Ask Volume / Bid Volume et trades entre Bid et Ask
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : **AskVolume** = volume des trades exécutés au meilleur prix Ask **ou au-dessus**. **BidVolume** = volume des trades exécutés au meilleur prix Bid **ou en dessous**. Si un trade survient **entre** le Bid et l'Ask, un algorithme spécial l'assigne au Bid ou à l'Ask selon que le trade est un **uptick ou un downtick**.
**TRADEX-AI C2** : Définition canonique du delta (acheteur au marché − vendeur au marché) à répliquer côté lecture order flow ; cadre l'interprétation du signe du delta sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D441 — Méthode de calcul des bougies CDB (Open/High/Low/Close)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Pour chaque barre, on calcule la différence Ask−Bid au fil des trades ; on conserve son maximum (**DifferenceHigh**) et son minimum (**DifferenceLow**). Avec CDB = Cumulative Delta Bars : **Open** = Close de la CDB précédente (ou 0 si pas de précédente / reset journalier, ajusté pour rester dans le range High-Low) ; **High** = Close CDB précédent + DifferenceHigh ; **Low** = Close CDB précédent + DifferenceLow ; **Close** = Close CDB précédent + (AskVolume − BidVolume de la barre de prix principale).
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Si « Reset at Start of Trading Day » = Yes, les valeurs OHLC de la bougie CDB sont remises à 0 ; elles partent aussi de 0 au début du chart.
**TRADEX-AI C0** : Formule déterministe du delta cumulé (besoin Ask/Bid volume par trade) ; le Close cumulé est la grandeur de référence à suivre, pas le prix.
*Catégorie : structure_marche*

---

### D442 — Coloration des barres : signe du delta, PAS le prix
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Une barre est **Up** si Close > Open (couleur Up), **Down** si Close < Open (couleur Down). Point crucial : Open et Close **n'impliquent pas des prix** mais des **différences Ask−Bid**. Une barre verte = pression nette acheteuse sur la barre ; rouge = pression nette vendeuse.
**TRADEX-AI C2** : Lire la couleur des barres comme un proxy de la dominance acheteur/vendeur au marché, indépendamment du sens du prix — base de la détection de divergence prix/delta.
*Catégorie : signal*

---

### D443 — Divergence prix / delta cumulé (usage order flow)
🔵 **ÉCOLE** (Source : sierra_292_cumulative_delta_volume.md — déduit du fait que Open/Close du CDB ne reflètent PAS le prix mais le delta) : Puisque le delta cumulé évolue indépendamment du prix, une **désynchronisation** entre la direction du prix et celle du delta cumulé constitue une divergence order flow (prix qui monte sans soutien du delta acheteur, ou inverse).
🔴 **NON VÉRIFIÉ** : La page Sierra Chart **ne formalise pas** de règle de trading de divergence (pas de seuil, pas de signal d'entrée) ; l'usage divergence relève de l'interprétation order flow, non de la doc source.
**TRADEX-AI C2** : Détecter la divergence prix/delta cumulé comme **confirmation** (jamais entrée isolée) sur GC/HG/CL/ZW ; à croiser avec price action et pivots Belkhayate.
*Catégorie : divergence*

---

### D444 — Reset journalier obligatoire pour la stabilité du signal
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : La sortie de l'étude **change probablement après un rechargement** du chart car le Date-Time de départ peut différer, ce qui affecte tous les calculs cumulés suivants. Pour éviter ce problème, **régler « Reset at Start of Trading Day » sur Yes**.
🟡 **CONVENTION** : Le delta cumulé n'est interprétable de façon stable que borné à une session ; sans reset il est dépendant de la fenêtre de données chargée.
**TRADEX-AI C2** : Côté TRADEX-AI, calculer le delta cumulé **avec reset journalier** pour une lecture reproductible session par session sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D445 — Exigence de données : tick by tick / stockage ≤ 2 secondes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Note importante — pour un résultat précis, l'**Intraday Data Storage Time Unit doit être ≤ 2 secondes**, sinon les résultats sont moins précis ; pour la **précision maximale, utiliser des données tick by tick**.
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : L'étude requiert un **Bid Volume et Ask Volume historiques** fournis par le service de données. À défaut, le delta reste à zéro ou inchangé pendant les déconnexions ; il faut rester connecté pour stocker ces données en temps réel.
**TRADEX-AI C2** : Garde-fou data — le delta cumulé fiable exige un feed tick-by-tick avec Bid/Ask volume (Rithmic via NTB) ; sans cette granularité, marquer la source order flow comme STALE/non fiable (cf. Staleness Monitor).
*Catégorie : gestion_risque_entree*

---

### D446 — Trois versions de l'étude (Volume / Trades / Up-Down Tick)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Il existe **3 versions différentes** des Cumulative Delta Bars (Volume / Trades / Up-Down Tick Volume). Une différence de valeurs entre deux charts peut venir de l'usage de versions différentes de l'étude.
**TRADEX-AI C2** : Fixer explicitement la variante = **Volume** (Ask vol − Bid vol) pour TRADEX-AI ; ne pas mélanger avec la version Trades ou Up/Down Tick afin d'éviter des deltas incohérents.
*Catégorie : structure_marche*

---

### D447 — Conditions de reproductibilité entre charts / copies
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Pour que deux charts/copies donnent le même delta cumulé, doivent être identiques : même version de l'étude, même feed de marché cohérent, stockage **tick by tick**, même Time Zone, **Session Times 100% identiques** (avec « New Bar At Session Start » = Yes recommandé), et même Days to Load / Date Range (si reset = No). Re-télécharger via « Delete All Data and Download » pour garantir la cohérence.
🟡 **CONVENTION** : Le delta cumulé n'est pas une grandeur absolue universelle : il dépend du paramétrage de session et de la profondeur de données.
**TRADEX-AI C2** : Verrouiller session/timezone/feed côté collecteur pour que le delta cumulé TRADEX-AI soit reproductible ; documenter ces paramètres comme part du contrat de données order flow.
*Catégorie : gestion_risque_entree*

---

### D448 — Filtrage du volume (Volume Filtering)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : On peut appliquer un **Volume Filtering** au résultat via Chart Settings, en filtrant le volume **au-dessus et en dessous** de quantités spécifiques. Pour comparer deux filtrages, dupliquer le chart, régler un filtrage différent, ajouter l'étude, puis superposer via Study/Price Overlay.
**TRADEX-AI C2** : Le filtrage volume permet d'isoler le delta des **gros lots vs petits lots** (proxy institutionnels vs retail) ; piste d'analyse big-trades sur GC/HG/CL/ZW (complémentaire ATAS Footprint/Big Trades).
*Catégorie : signal*

---

### D449 — Inputs de reset (Trading Day / Both Session Start Times)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Input **« Reset at Start of Trading Day »** = Yes → la somme cumulée est remise à zéro au début de la journée (Start Time, ou Evening Start Time si session du soir activée) ; la valeur d'ouverture (= différence Ask/Bid du premier trade) n'est alors **pas** à zéro, ce qui est normal. Input **« Reset at Both Session Start Times »** = Yes → implique toujours le reset journalier, plus un reset additionnel à l'Evening Start Time.
**TRADEX-AI C2** : Choisir le mode de reset selon la session tradée (day session vs session du soir) ; aligner sur les heures de session des contrats CME/CBOT pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D450 — Outils de dessin : les barres bougent, pas les dessins
🟢 **FAIT VÉRIFIÉ** (Source : sierra_292_cumulative_delta_volume.md) : Avec « Reset at Start of Trading Day » = No, les valeurs cumulées d'un Date-Time changent à chaque nouveau jour/rechargement, donnant l'impression que les **dessins (drawings) bougent** ; en réalité ce sont les barres delta qui se déplacent relativement aux dessins. Solutions : mettre le reset journalier à Yes, ou augmenter « Days to Load » de 1 chaque jour (ou Use Date Range).
**TRADEX-AI C2** : Conséquence directe : sans reset, le delta cumulé n'a pas d'ancrage absolu fiable dans le temps — confirme D444 (reset journalier = mode par défaut TRADEX-AI).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D439 → D450 (12) |
| Images certifiées citées | 0/0 (aucune figure sur la page) |
| Catégories utilisées | structure_marche · signal · divergence · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · 🔴 NON VÉRIFIÉ |
| Cercle dominant | **C2 (order flow)** — delta cumulé = Ask volume − Bid volume |
| Belkhayate | **NON concerné directement** — brique order flow (C2), complémentaire des pivots/BGC/Énergie ; sert de confirmation, jamais d'entrée isolée |
| Complémentarité | Angle **Sierra Chart** (calcul de référence) — complémentaire de l'angle **NinjaTrader** du delta (traité séparément) |

### Cas « à vérifier »
- **D443 (divergence)** : la page Sierra Chart **ne formalise aucune règle de trading** de divergence prix/delta (pas de seuil ni signal d'entrée). Le concept de divergence est déduit du fait que les barres CDB encodent le delta et non le prix → tag 🔴 NON VÉRIFIÉ sur la partie « règle d'usage ». À confirmer/compléter par une source order flow dédiée (ATAS Footprint, ou angle NinjaTrader du delta).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
