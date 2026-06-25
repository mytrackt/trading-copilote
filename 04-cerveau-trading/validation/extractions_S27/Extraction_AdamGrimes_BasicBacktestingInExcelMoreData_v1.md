# Extraction AdamGrimes — Basic Backtesting In Excel: More Data
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_more_data.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5311 → D5320 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-more-data/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Principes de combinaison propre de séries multi-actifs — applicable à la construction de la matrice de corrélations live.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5311 — Convention de nommage cohérente pour les données multi-instruments
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_more_data.md) : Adam Grimes utilise la convention `TICKER_DATAELEMENT` (ex. `SPY_C` pour le close de SPY) pour distinguer les séries dans un fichier combinant plusieurs instruments. La cohérence absolue du nommage est critique pour retrouver ce qu'on a fait des années plus tard.
**TRADEX-AI C7** : Dans `correlations.py` et `data_reader.py`, adopter une convention de nommage uniforme : `{TICKER}_{FIELD}_{TIMEFRAME}` (ex. `GC_CLOSE_5m`, `VX_SETTLE_daily`). Documenter cette convention dans `settings.py` comme standard de fait.
*Catégorie : configuration*

### D5312 — Une formule live dépendant d'un fichier externe est fragile
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_more_data.md) : Une cellule Excel référençant un fichier externe (TLT.csv) est « live » — si ce fichier est déplacé, supprimé ou non ouvert, les valeurs disparaissent. La pratique recommandée est de convertir les formules en valeurs statiques (paste-special values) pour stabiliser les données une fois vérifiées.
**TRADEX-AI C1** : Dans `data_reader.py`, les snapshots JSON provenant de NT8 doivent être copiés atomiquement (`atomic_writer.py`) avant traitement. Ne jamais travailler directement sur le fichier source en cours d'écriture par NT8 — risque de corruption silencieuse des données.
*Catégorie : gestion_risque_entree*

### D5313 — Les données historiques tronquées créent des valeurs manquantes en début de série
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_more_data.md) : Quand une série (TLT) a un historique plus court qu'une autre (SPY), les dates antérieures au lancement de TLT génèrent des valeurs manquantes. Ce comportement est attendu et doit être géré explicitement (ex. : marqueur `.` ou `NaN`) plutôt que laissé comme erreur.
**TRADEX-AI C7** : Dans la matrice de corrélations 30j, si un actif a des données manquantes sur la fenêtre (ex. : HG non tradé un jour férié CME), les calculs de corrélation doivent exclure ces points et ne pas propager de `NaN` en cascade. Utiliser `dropna()` ou équivalent.
*Catégorie : correlations*

### D5314 — La combinaison de séries doit gérer les gaps de dates différentes par instrument
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_more_data.md) : Deux instruments peuvent avoir des calendriers différents (jours fériés, suspensions). Une jointure par date exacte (VLOOKUP / merge) avec gestion des valeurs manquantes (ISERROR → remplacement par marqueur) est la méthode correcte pour combiner des séries sans introduire de décalage silencieux.
**TRADEX-AI C7** : `correlations.py` doit utiliser un `pd.merge(..., how='inner')` ou `how='outer'` explicite selon le besoin, avec documentation du choix. Pour la corrélation entre actifs de fuseaux différents (ex. DX vs GC), n'utiliser que les timestamps communs.
*Catégorie : correlations*

### D5315 — Les raccourcis clavier et l'automatisation réduisent les erreurs de manipulation
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_more_data.md) : La maîtrise des raccourcis clavier (Ctrl-C, Ctrl-V, Ctrl-flèches, Shift, paste-special) réduit les erreurs de sélection manuelle et accélère le workflow. Copier-coller manuellement des plages de données larges augmente le risque d'erreur de sélection.
**TRADEX-AI C1** : Dans les scripts Python de la KB pipeline, toujours utiliser des lectures/écritures atomiques et des validations automatiques plutôt que des manipulations manuelles. Les scripts `scraper.py`, `scraper_static.py` et `scraper_pdf.py` doivent logger chaque opération pour permettre la détection d'erreurs silencieuses.
*Catégorie : configuration*

### D5316 — La persistance des données ne doit pas dépendre de l'état d'un autre processus
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_more_data.md) : Les formules qui dépendent d'un fichier externe ouvert (TLT.csv) perdent leur valeur si ce fichier est fermé. Convertir en valeurs statiques (paste-special) garantit la persistance indépendante.
**TRADEX-AI C1** : `staleness_monitor.py` doit détecter le cas où NT8 ou ATAS n'écrit plus dans les fichiers JSON (process arrêté). Le circuit breaker `CB_NT8` doit déclencher BLOCKED si les fichiers source ne sont pas mis à jour depuis plus que le seuil de staleness — pas seulement si les données sont numériquement aberrantes.
*Catégorie : gestion_risque_entree*
