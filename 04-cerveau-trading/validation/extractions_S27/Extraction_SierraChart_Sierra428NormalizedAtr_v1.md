# Extraction SierraChart — Normalized Average True Range
**Source :** `bundles/sierrachart/sierra_428_normalized_atr.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9331 → D9340 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=428
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : ATR normalisé (% du prix) pour comparaison de volatilité inter-actifs — proxy potentiel pour l'Énergie Belkhayate sur Historical Daily.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9331 — Définition ATR Normalisé (ATR^Norm)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_428_normalized_atr.md) : Le Normalized ATR (ATR^Norm_t) est calculé pour t >= n-1 en divisant l'Average True Range par le prix de clôture, puis en exprimant le résultat en pourcentage. Formule : ATR^Norm_t = ATR_t / Close_t × 100. Cela produit un indicateur de volatilité exprimé en % du prix plutôt qu'en valeur absolue.
**TRADEX-AI C1** : L'ATR normalisé permet de comparer la volatilité relative entre GC (or ~2300$), HG (cuivre ~4$), CL (pétrole ~80$) et ZW (blé ~6$) sur une échelle commune. Un ATR^Norm élevé (ex: >1.5% sur GC) signale une volatilité anormale — condition de risque à intégrer dans risk_manager.py.
*Catégorie : gestion_risque_entree*

### D9332 — Contrainte Historical Daily Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_428_normalized_atr.md) : Cette étude fonctionne correctement UNIQUEMENT sur un Historical Daily chart (ouvert via File >> Find Symbol >> Open Historical Chart). Sur un graphique intraday, l'étude ne produit pas de résultats corrects.
**TRADEX-AI C1** : Le Normalized ATR est donc un indicateur daily — non applicable directement sur les barres Range intraday NT8 de TRADEX-AI. Usage recommandé : calcul daily en fin de session via Study/Price Overlay sur graphique intraday pour obtenir le contexte de volatilité de fond.
*Catégorie : gestion_risque_entree*

### D9333 — Overlay intraday via Study/Price Overlay
🟢 **FAIT VÉRIFIÉ** (Source : sierra_428_normalized_atr.md) : Sierra Chart permet d'overlay le Normalized ATR (calculé sur Daily) sur un graphique intraday en utilisant le study Study/Price Overlay. Cette technique permet de combiner la précision intraday avec la référence de volatilité daily.
**TRADEX-AI C1** : Dans TRADEX-AI, l'ATR Normalisé daily peut être exporté comme valeur de référence contextuelle. En pratique : si ATR^Norm_daily(GC) > seuil_config → augmenter le stop distance dans risk_manager.py. Seuil recommandé initial : 1.2% pour GC, 1.5% pour CL.
*Catégorie : gestion_risque_entree*

### D9334 — Paramètres configurables : Moving Average Length et Type
🟢 **FAIT VÉRIFIÉ** (Source : sierra_428_normalized_atr.md) : Deux inputs configurables : (1) Moving Average Length — longueur de la MA appliquée à l'ATR dans le calcul. (2) Moving Average Type — type de lissage (SMA, EMA, Wilder, etc., identique aux types disponibles pour le RSI ID=38). Ces paramètres héritent de la même nomenclature que les autres études Sierra Chart.
**TRADEX-AI C1** : Paramètres recommandés initiaux : Moving Average Length = 14 (standard ATR Wilder), Moving Average Type = Wilders Moving Average (cohérence avec l'ATR classique). Valeur ajustable par actif dans settings.py : ATR_NORM_LENGTH = 14 (global), avec option de surcharge par symbole.
*Catégorie : gestion_risque_entree*

### D9335 — Disponibilité spreadsheet (.scss)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_428_normalized_atr.md) : Un fichier spreadsheet Sierra Chart est disponible : Average_True_Range_-_Normalized.428.scss. Importable via File >> Open Spreadsheet pour vérification indépendante des formules.
**TRADEX-AI C1** : Le fichier .scss documente la formule exacte de normalisation. À utiliser pour valider l'implémentation Python de l'ATR normalisé dans engine/ avant intégration dans le moteur de signal (évite toute divergence de calcul entre Sierra Chart et TRADEX-AI).
*Catégorie : gestion_risque_entree*

### D9336 — Proxy potentiel pour l'Énergie Belkhayate (stub actuel)
🟡 **SYNTHÈSE** (Source : sierra_428_normalized_atr.md) : L'ATR normalisé est un indicateur de volatilité relative standardisé (%prix) calculé sur Historical Daily. L'Énergie Belkhayate (actuellement stub dans TRADEX-AI) utilise une combinaison de MFI et ATR selon certaines transcriptions. L'ATR^Norm constitue la composante ATR de ce calcul hybride.
**TRADEX-AI C1** : L'ATR^Norm daily peut servir de composante ATR dans un futur proxy de l'Énergie Belkhayate, en attendant la résolution du conflit MFI vs ATR (ticket ouvert, CLAUDE.md). Ne pas fusionner dans la KB comme "Énergie Belkhayate" — marquer comme composante candidate uniquement.
*Catégorie : indicateurs_momentum*

### D9337 — Comparaison inter-actifs (normalisation par prix)
🟡 **SYNTHÈSE** (Source : sierra_428_normalized_atr.md) : La normalisation par le prix (ATR/Close × 100) rend l'ATR comparable entre actifs à prix très différents. Exemple : ATR_abs(GC)=15$ sur or à 2300$ = ATR^Norm=0.65% ; ATR_abs(CL)=1.2$ sur pétrole à 80$ = ATR^Norm=1.5% → le pétrole est relativement plus volatil même si son ATR absolu est plus faible.
**TRADEX-AI C7** : Intégrer l'ATR^Norm dans la matrice de corrélations (cercle C7) pour comparer la volatilité relative en temps réel entre GC/HG/CL/ZW. Un pic de volatilité simultané sur plusieurs actifs (ATR^Norm > 1.5% sur 3+ actifs) → alerte macro à transmettre à claude_brain.py.
*Catégorie : correlations*
