# Extraction AdamGrimes — Choosing the Best Pullbacks
**Source :** `bundles/adamgrimes/choosing_best_pullbacks.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption locale · 0/0 certifiées (1 décorative ignorée) · 0 à vérifier
**Décisions :** D5571 → D5590 · **Page :** https://www.adamhgrimes.com/choosing-best-pullbacks/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Critères de sélection des meilleurs pullbacks — qualité de la bougie de setup et position par rapport au Keltner channel.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image certifiée — 1 décorative ignorée) | — | — | — |

## DÉCISIONS

### D5571 — Règle : ne pas entrer après un climax dans le sens du trade
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Un pullback précédé d'une bougie de setup présentant une longue ombre supérieure (shadow/wick couvrant ~50% du range) signale un climax acheteur sur timeframe inférieur. Entrer en pullback après un tel climax dans la direction du trade est une erreur de sélection documentée.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, si la bougie de setup d'un pullback haussier présente une ombre supérieure dépassant ~40% du range total, exclure ce pullback — signal de fin de pression acheteuse.
*Catégorie : configuration*

### D5572 — Qualité du setup bar : corps vs ombre
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : La qualité de la bougie de setup précédant le pullback est un élément critique de sélection. Une bougie où la moitié du range est une ombre (wick) affaiblit substantiellement le signal de continuation.
**TRADEX-AI C1** : Pour tout actif TRADING (GC/HG/CL/ZW), évaluer systématiquement le ratio corps/ombre de la bougie de setup avant validation d'un signal pullback — corps dominant = meilleur signal.
*Catégorie : configuration*

### D5573 — Position du pullback par rapport au Keltner channel
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Un pullback qui se consolide au-dessus du Keltner channel supérieur est de meilleure qualité qu'un pullback qui retombe vers la moyenne mobile centrale. La position du pullback dans la structure du Keltner channel discrimine les setups forts des setups faibles.
**TRADEX-AI C1** : Dans le moteur de scoring, un pullback maintenu au-dessus du Keltner channel supérieur reçoit un bonus de qualité ; un pullback retombant vers la MA centrale est déclassé.
*Catégorie : configuration*

### D5574 — Rebond décisif immédiat après climax mineur
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Un climax mineur sur la bougie de setup n'invalide pas systématiquement le trade si la bougie suivante trade de façon décisive dans la direction du trend. La résolution rapide du climax mineur par une continuation est un signal de force relative.
**TRADEX-AI C1** : Distinguer climax majeur (invalide le pullback) de climax mineur suivi d'une clôture de continuation décisive (maintient la validité du signal).
*Catégorie : configuration*

### D5575 — Problème de sélection sur marchés de futures corrélés
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Sur les futures, plusieurs actifs corrélés se configurent simultanément en pullback — GC/SI, CL/HO/RBOB, W/S/C. Ne pas pouvoir prendre tous les trades, il faut sélectionner le meilleur selon des critères techniques rigoureux.
**TRADEX-AI C7** : Quand GC et HG (ou CL et ZW) présentent simultanément un signal pullback, appliquer les critères de qualité (bougie setup, position Keltner) pour ne retenir que le signal de meilleure qualité et éviter le risque corrélé non maîtrisé.
*Catégorie : gestion_risque_entree*

### D5576 — Caractère de la bougie de setup comme filtre primaire
🟡 **SYNTHÈSE** (Source : choosing_best_pullbacks.md) : La qualité du mouvement qui précède le pullback (la bougie ou la séquence de setup) est l'un des éléments critiques de sélection d'un pullback. Ce filtre doit être appliqué en premier, avant d'analyser le caractère du pullback lui-même.
**TRADEX-AI C1** : Dans la grille de scoring /10, la qualité de la bougie de setup précédant le pullback constitue un critère éliminatoire potentiel — mauvaise qualité (climax + ombre dominante) → signal abaissé ou rejeté.
*Catégorie : gestion_risque_entree*

### D5577 — Trading comme jeu de choix : maximiser les bons choix
🔵 **ÉCOLE** (Source : choosing_best_pullbacks.md) : Le trading est un jeu de choix. L'objectif n'est pas de faire 100% de bons choix (impossible) mais de faire plus de bons choix que de mauvais choix sur la durée. Les facteurs discriminants subtils entre bon et mauvais trade sont plus importants que les règles évidentes.
**TRADEX-AI C1** : Intégrer dans la documentation trader (mode Manuel) : l'analyse de qualité du setup pullback est un différenciateur probabiliste, pas une garantie — renforce la discipline de sélection d'Abdelkrim.
*Catégorie : psychologie*

### D5578 — Analyse comparative inter-actifs sur même cross devise
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Quand plusieurs paires de devises (ex : CAD/JPY vs USD/JPY) se configurent contre le même sous-jacent simultanément, une analyse comparative des qualités de setup respectives permet d'identifier le trade à prendre et celui à ignorer.
**TRADEX-AI C7** : Principe transposable aux futures TRADEX : quand GC et HG signalent simultanément, comparer la qualité des setups (structure Keltner + bougie setup + absence de climax) avant d'allouer le capital.
*Catégorie : correlations*

### D5579 — Règle de skip : mieux vaut passer que prendre un mauvais setup
🟢 **FAIT VÉRIFIÉ** (Source : choosing_best_pullbacks.md) : Quand le seul trade disponible présente un setup de mauvaise qualité (climax + ombre dominante), il vaut mieux passer le trade que de forcer l'entrée. Le skip est une décision active et valide.
**TRADEX-AI C1** : Implémenter un verdict PASSER explicite dans l'interface Mode Manuel quand le score de qualité du setup pullback est insuffisant — distinct du verdict ATTENDRE global.
*Catégorie : gestion_risque_entree*

### D5580 — Caractère du pullback lui-même (annoncé comme futur sujet)
🔵 **ÉCOLE** (Source : choosing_best_pullbacks.md) : Au-delà de la bougie de setup, le caractère du pullback lui-même (profondeur, structure interne, vitesse) est un second niveau d'analyse à combiner avec la qualité du setup. Grimes annonce ce sujet comme complémentaire indispensable.
**TRADEX-AI C1** : La grille de scoring pullback TRADEX doit intégrer deux niveaux : (1) qualité bougie setup, (2) caractère du pullback — profondeur par rapport à la structure Keltner/Belkhayate.
*Catégorie : configuration*
