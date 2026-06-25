# Extraction SierraChart — Bar Delta Below Bar
**Source :** `bundles/sierrachart/sierra_444_bar_delta_below_bar.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9371 → D9380 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=444
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Bar Delta Below Bar affiche le delta (Ask Vol - Bid Vol) sous chaque barre — indicateur order flow C2 clé pour lire la pression acheteuse/vendeuse barre par barre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9371 — Définition Bar Delta : différence Ask Volume - Bid Volume par barre
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : Le Bar Delta est défini comme la différence entre le volume traité au Ask (acheteurs agressifs) et le volume traité au Bid (vendeurs agressifs) pour chaque barre : Delta = V_ask - V_bid. La valeur est affichée comme texte sous chaque barre.
**TRADEX-AI C2** : Le delta par barre est la mesure fondamentale d'order flow — un delta positif indique une pression acheteuse nette, un delta négatif indique une pression vendeuse nette. Donnée C2 primaire pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D9372 — Affichage textuel sous la barre (below bar)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : Le texte affichant la valeur du delta est positionné sous chaque barre, à une distance définie par la formule : position = Low_t - (k * tick_size), où k est le paramètre `Offset in Ticks` et tick_size est la taille d'un tick définie pour le symbole.
**TRADEX-AI C2** : Le positionnement sous la barre permet une lecture visuelle rapide du delta sans masquer l'action des prix. Pertinent pour l'interface dashboard TRADEX-AI si un affichage chart est intégré.
*Catégorie : volume_liquidite*

### D9373 — Paramètre Offset in Ticks : distance d'affichage configurable
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : L'input `Offset in Ticks` (noté k) détermine la distance verticale entre le Low de la barre et le texte du delta, exprimée en nombre de ticks. La taille d'un tick est celle définie dans les paramètres du chart (Chart >> Chart Settings).
**TRADEX-AI C2** : Pour GC (Or, tick = 0.10), un offset de 5-10 ticks est recommandé pour que le texte ne chevauche pas les barres adjacentes. Pour CL (pétrole, tick = 0.01), un offset plus grand peut être nécessaire sur les marchés volatils.
*Catégorie : volume_liquidite*

### D9374 — Coloration du texte : Subgraph Primary/Secondary
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : La coloration du texte delta est contrôlée par les couleurs Primary et Secondary du Subgraph. La logique de coloration suit la documentation Sierra Chart sur les Subgraphs (Studies >> Subgraphs Tab >> Color).
**TRADEX-AI C2** : Convention recommandée pour TRADEX-AI : Primary = vert (delta positif = pression acheteuse), Secondary = rouge (delta négatif = pression vendeuse). Cohérent avec les conventions d'affichage ATAS Pro déjà utilisées dans le projet.
*Catégorie : volume_liquidite*

### D9375 — Limitation données historiques : Ask Volume non garanti
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : Selon Sierra Chart, selon le service de données ou de trading utilisé, les données historiques Ask Volume peuvent ne pas être disponibles lors du téléchargement de données historiques. Tous les services ne fournissent pas ces données historiques.
**TRADEX-AI C2** : Cette limitation est critique pour TRADEX-AI : le calcul du delta historique (backtesting) n'est fiable que si le service de données (Rithmic via ATAS) fournit bien les volumes Ask/Bid historiques. À vérifier lors de la Phase C avec le feed Rithmic.
*Catégorie : volume_liquidite*

### D9376 — Compatibilité avec footprint charts (order flow avancé)
🟡 **SYNTHÈSE** (Source : sierra_444_bar_delta_below_bar.md) : Le Bar Delta Below Bar est une version simplifiée de l'analyse footprint — il affiche le delta total de la barre sans le détail niveau-par-niveau (footprint complet). Il est complémentaire aux études footprint plus détaillées de Sierra Chart.
**TRADEX-AI C2** : Pour TRADEX-AI, le delta total par barre suffit pour le Cercle C2 au Niveau 1 (filtre Python). Le footprint complet (niveau-par-niveau) est l'apanage d'ATAS Pro — Bar Delta Below Bar sert de proxy Sierra Chart si ATAS n'est pas disponible.
*Catégorie : volume_liquidite*

### D9377 — Formule de calcul : applicable à toutes les barres (t ≥ 1)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : La formule Delta_t = V_ask_t - V_bid_t est calculée pour chaque barre t, sans condition sur l'index minimum (pas de période de chauffe requise contrairement aux moyennes mobiles). Le delta est disponible dès la première barre.
**TRADEX-AI C2** : Avantage opérationnel : le delta est disponible immédiatement sans délai d'initialisation. TRADEX-AI peut utiliser le delta de la barre en cours sans attendre N barres de chauffe.
*Catégorie : volume_liquidite*

### D9378 — Interprétation signal : delta cumulé vs delta par barre
🟡 **SYNTHÈSE** (Source : sierra_444_bar_delta_below_bar.md) : La documentation Sierra Chart présente uniquement le delta par barre individuelle. L'analyse du delta cumulé (somme des deltas sur plusieurs barres) n'est pas couverte par cette étude — elle relève d'une étude séparée (Cumulative Delta).
**TRADEX-AI C2** : TRADEX-AI doit distinguer deux signaux C2 : (1) delta de la barre en cours (réactivité instantanée) et (2) delta cumulé sur N barres (tendance order flow). Le Bar Delta Below Bar couvre uniquement le signal (1).
*Catégorie : volume_liquidite*

### D9379 — Spreadsheet disponible pour validation
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : Sierra Chart fournit un fichier spreadsheet `Bar_Delta_Below_Bar.444.scss`. Dernière modification : 31 janvier 2023.
**TRADEX-AI C2** : Fichier de référence pour valider le calcul delta si une implémentation alternative est développée. Utile pour tester la cohérence avec les données ATAS Pro sur une période historique.
*Catégorie : volume_liquidite*

### D9380 — Dépendance tick size : paramètre critique pour l'affichage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_444_bar_delta_below_bar.md) : Le positionnement du texte dépend directement du Tick Size défini dans Chart >> Chart Settings. Si le Tick Size est incorrect, l'affichage sera mal positionné (chevauchement avec les barres ou distance excessive).
**TRADEX-AI C2** : Pour chaque actif TRADEX-AI, le Tick Size doit être configuré correctement dans Sierra Chart : GC = 0.10, HG = 0.0005, CL = 0.01, ZW = 0.25. Une configuration incorrecte invalide l'affichage du delta mais pas le calcul de la valeur elle-même.
*Catégorie : volume_liquidite*
