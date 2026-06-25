# Extraction SierraChart — Numbers Bars Avg Volume Per Price Graph
**Source :** `bundles/sierrachart/sierra_368_numbers_bars_avg_vol_per_price.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9271 → D9273 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=368
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : calcul du volume moyen par niveau de prix sur chaque barre — indicateur volume/liquidité C2.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9271 — Définition Average Volume Per Price (VPP)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_368_numbers_bars_avg_vol_per_price.md) : L'Average Volume Per Price (VPP) d'une barre est calculé comme le Volume total de la barre divisé par le nombre de niveaux de prix distincts touchés sur cette même barre. Formula : VPP_t = V_t / N_t^(P) où V_t = volume total et N_t^(P) = nombre de prix distincts accessibles via sc.VolumeAtPriceForBars.
**TRADEX-AI C2** : Le VPP moyen par barre permet de détecter les zones de forte concentration de volume par tick — utile en order flow pour identifier les niveaux de liquidité réelle sur GC/HG/CL/ZW dans Sierra Chart ou ATAS.
*Catégorie : volume_liquidite*

### D9272 — Absence d'inputs configurables
🟢 **FAIT VÉRIFIÉ** (Source : sierra_368_numbers_bars_avg_vol_per_price.md) : Cette étude n'a aucun paramètre d'entrée utilisateur. Le calcul est entièrement déterministe à partir des données de volume brutes de chaque barre.
**TRADEX-AI C2** : Aucun risque de sur-optimisation paramétrique. L'indicateur produit une valeur objective par barre, intégrable directement dans data_reader.py sans configuration additionnelle.
*Catégorie : volume_liquidite*

### D9273 — Disponibilité via ACSIL (API Sierra Chart)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_368_numbers_bars_avg_vol_per_price.md) : La donnée N_t^(P) (nombre de prix distincts) est accessible programmatiquement via l'interface ACSIL avec sc.VolumeAtPriceForBars. Un fichier spreadsheet (.scss) est disponible pour implémentation directe : Numbers_Bars_Avg_Volume_Per_Price_Graph.368.scss.
**TRADEX-AI C2** : L'accès ACSIL confirme que cette métrique peut être exportée vers un fichier JSON NT8-compatible et lue par data_reader.py pour alimenter le moteur de signal en temps réel.
*Catégorie : volume_liquidite*
