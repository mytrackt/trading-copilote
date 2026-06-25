# Extraction AdamGrimes — This Is What Manipulation Looks Like
**Source :** `bundles/adamgrimes/this_is_what_manipulation_looks_like.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6991 → D7010 · **Page :** https://www.adamhgrimes.com/this-is-what-manipulation-looks-like/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Corrélations de volatilité inter-marchés comme détecteur d'anomalie/manipulation — applicable à C7 (Corrélations) et C3 (Institutionnels).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6991 — Corrélations sur rendements, pas sur prix : erreur fondamentale à éviter
🟢 **FAIT VÉRIFIÉ** (Source : this_is_what_manipulation_looks_like.md) : Calculer des corrélations sur les prix (et non sur les rendements/returns) est une erreur de niveau stats-101 qui produit des résultats trompeurs. La quasi-totalité des livres de trading et des logiciels de charting font cette erreur. Les corrélations doivent être calculées sur les variations (returns), jamais sur les niveaux de prix absolus.
**TRADEX-AI C7** : La matrice de corrélations C7 (GC/HG/CL/ZW/ES/VX/MBT/6J) DOIT être calculée sur les returns (variations en %) et non sur les prix absolus. Vérifier et corriger le module `correlations.py` pour s'assurer que l'input est bien `pct_change()` et non les prix bruts.
*Catégorie : correlations*

### D6992 — Les corrélations changent plus souvent qu'on ne le croit
🟢 **FAIT VÉRIFIÉ** (Source : this_is_what_manipulation_looks_like.md) : Les corrélations entre marchés ne sont pas stables dans le temps. Elles évoluent significativement selon les régimes de marché. S'appuyer sur des corrélations historiques longues pour des décisions court-terme est une erreur. Les corrélations court-terme (20 jours) peuvent diverger radicalement des corrélations longues.
**TRADEX-AI C7** : La matrice live C7 utilise une fenêtre glissante 30 jours. Ajouter une comparaison avec la corrélation 90 jours pour détecter les ruptures de régime. Une divergence forte (court terme vs long terme) est un signal de changement de régime à signaler dans le dashboard.
*Catégorie : correlations*

### D6993 — Corrélations de volatilité : outil contre-intuitif mais puissant
🟡 **SYNTHÈSE** (Source : this_is_what_manipulation_looks_like.md) : Les corrélations entre volatilités de marchés différents (corrélations du second moment des distributions) sont encore moins intuitives que les corrélations de rendements. Elles ont pris des mois à Adam Grimes avant d'être jugées utiles — mais elles révèlent des patterns impossibles à voir autrement, notamment lors des stress de marché.
**TRADEX-AI C7** : Envisager d'ajouter aux métriques C7 la corrélation de volatilité (ex. corrélation entre VX et la volatilité réalisée de GC sur 20 jours). Ce signal avancé de stress systémique est complémentaire aux corrélations de rendements standard.
*Catégorie : correlations*

### D6994 — Lors d'un stress de marché, les volatilités convergent (sauf exception)
🟢 **FAIT VÉRIFIÉ** (Source : this_is_what_manipulation_looks_like.md) : En période de stress, les volatilités de marchés normalement distincts tendent à augmenter en même temps et à se corréler fortement. Les marchés "bougent ensemble". Ce phénomène est quantifiable et prévisible.
**TRADEX-AI C7** : Implémenter un "Stress Index" basé sur la corrélation instantanée des volatilités entre ES, GC, CL et VX. Quand ce Stress Index dépasse un seuil (ex. corrélation moyenne > 0,7), déclencher un mode défensif : réduire les tailles, bloquer le mode Auto, alerter Abdelkrim.
*Catégorie : gestion_risque_entree*

### D6995 — Marché qui se découple de son groupe : signal d'anomalie à investiguer
🟢 **FAIT VÉRIFIÉ** (Source : this_is_what_manipulation_looks_like.md) : Lors du stress mondial de 2015 (exemple Chine dans l'article), les marchés chinois ont montré une faible corrélation de volatilité avec les autres marchés mondiaux — en raison d'une intervention gouvernementale (interdictions de vente). Ce découplage est détectable quantitativement avant même de connaître la cause.
**TRADEX-AI C7** : Un actif qui se découple de la corrélation de volatilité de son groupe (ex. HG/Cuivre qui ne suit pas GC/ES lors d'un stress) doit déclencher une alerte. Le découplage peut signaler une manipulation institutionnelle, une intervention ou une information asymétrique. Réponse : mode information-gathering + blocage Auto sur l'actif concerné.
*Catégorie : macro_evenements*

### D6996 — Tableaux de corrélations à deux horizons (court + long terme) : veille hebdomadaire
🔵 **ÉCOLE** (Source : this_is_what_manipulation_looks_like.md) : Adam Grimes présente simultanément les corrélations long terme ET court terme (20 jours) dans ses rapports, en surlignant les changements de corrélation court terme d'une semaine à l'autre. Ce delta hebdomadaire est la vraie information.
**TRADEX-AI C7** : Le dashboard doit afficher deux colonnes de corrélation : C7_long (90j) et C7_short (20j). La colonne delta (différence entre les deux) identifie les paires en rupture de régime. Actualisation hebdomadaire minimum, quotidienne idéalement.
*Catégorie : correlations*

### D6997 — Outil quantitatif de visualisation de volatilité : avantage informationnel
🟡 **SYNTHÈSE** (Source : this_is_what_manipulation_looks_like.md) : Les outils quantitatifs de visualisation des corrélations de volatilité offrent une perspective sur les marchés mondiaux complexes que l'analyse chartiste traditionnelle ne peut pas atteindre. Ces outils donnent un avantage informationnel immédiat et puissant.
**TRADEX-AI C7** : Le module `correlations.py` doit évoluer vers un système complet incluant : (1) corrélations de rendements court/long terme, (2) corrélations de volatilité 20j, (3) Stress Index agrégé, (4) alertes de découplage. Ce module constitue un différenciateur fort de TRADEX-AI vs systèmes simples.
*Catégorie : correlations*
