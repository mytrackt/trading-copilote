# Extraction SierraChart — Momentum Trend (ID 62)
**Source :** `bundles/sierrachart/sierra_62_momentum_trend.md` (HTTP 200) + 0 images certifiées
**Méthode images :** pas d'images dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9451 → D9470 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=62
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : idx 450 (Momentum Trend) — indicateur de direction momentum basé sur la variation de M(t) utilisable comme signal de retournement intra-barre en C1 pour GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image présente dans le bundle) | — | — | — |

## DÉCISIONS

### D9451 — Momentum Trend : définition et principe de dessin
🟢 **FAIT VÉRIFIÉ** (Source : sierra_62_momentum_trend.md) : Le Momentum Trend Study (ID 62) est basé sur l'étude Momentum standard. La règle de dessin est : si `M(t-1, X, n) < M(t, X, n)` → un point est dessiné sur le **haut de la barre** (momentum en hausse) ; si `M(t-1, X, n) >= M(t, X, n)` → un point est dessiné sur le **bas de la barre** (momentum en baisse ou stable). Ce dessin s'effectue pour tout `t > n`.
**TRADEX-AI C1** : Le Momentum Trend fournit un signal binaire directionnel barre par barre. Dans TRADEX-AI, ce signal peut servir de filtre de confirmation d'alignement directionnel C1 : point haut = momentum bullish, point bas = momentum bearish.
*Catégorie : indicateurs_tendance*

### D9452 — Paramètre Length (n) : longueur du Momentum
🟢 **FAIT VÉRIFIÉ** (Source : sierra_62_momentum_trend.md) : `Length` est le paramètre `n` contrôlant la fenêtre de calcul du Momentum M(t, X, n). Correspond au nombre de barres passées sur lesquelles la variation de prix (différence ou quotient) est calculée. Ce paramètre est directement configurable dans les inputs de l'étude.
**TRADEX-AI C1** : Paramètre à exposer dans `settings.py` sous `MOMENTUM_TREND_LENGTH`. Valeurs de départ suggérées pour les actifs TRADEX : 10 à 20 barres sur Range Bars NT8. À calibrer par actif (GC peut nécessiter un Length plus long que CL en raison d'une volatilité différente).
*Catégorie : indicateurs_tendance*

### D9453 — Paramètre Momentum Type : Différence vs Quotient
🟢 **FAIT VÉRIFIÉ** (Source : sierra_62_momentum_trend.md) : L'input `Momentum Type` détermine si le Momentum est calculé comme une **Différence** (`M = X(t) - X(t-n)`) ou un **Quotient** (`M = X(t) / X(t-n)`). Ce choix modifie la nature du signal : la différence est absolue (sensible à la magnitude des prix), le quotient est relatif (comparable entre actifs).
**TRADEX-AI C1** : Pour TRADEX-AI, le **Quotient** est préférable car il permet une comparaison cohérente entre GC (Or, prix ~2000$), HG (Cuivre, ~4$), CL (Pétrole, ~80$) et ZW (Blé, ~5$). Le type doit être documenté dans `settings.py`.
*Catégorie : indicateurs_tendance*

### D9454 — Input Data : série de prix utilisée
🟢 **FAIT VÉRIFIÉ** (Source : sierra_62_momentum_trend.md) : L'input `Input Data` détermine sur quelle série de prix (Close, Open, High, Low, HL/2, etc.) le Momentum est calculé. Configurable directement dans les paramètres de l'étude Sierra Chart.
**TRADEX-AI C1** : Utiliser le Close pour alignement avec la méthode Belkhayate (les BGC de Belkhayate sont calculés sur les closes). Documenter ce choix dans `settings.py` pour reproductibilité.
*Catégorie : indicateurs_tendance*

### D9455 — Spreadsheet Momentum_Trend.62.scss : formules de référence
🔵 **ÉCOLE** (Source : sierra_62_momentum_trend.md) : Sierra Chart fournit un fichier spreadsheet `Momentum_Trend.62.scss` contenant les formules de calcul de l'étude. Accessible via `File >> Open Spreadsheet` depuis le dossier Data Files.
**TRADEX-AI C1** : Référence pour implémenter le calcul en Python pur, indépendamment de Sierra Chart. Utile pour le module `05-saas/engine/` qui recalcule les indicateurs depuis les données NT8 JSON.
*Catégorie : indicateurs_tendance*

### D9456 — Relation avec l'étude Momentum parent (ID non précisé)
🔵 **ÉCOLE** (Source : sierra_62_momentum_trend.md) : Le Momentum Trend est dérivé de l'étude Momentum de Sierra Chart. La documentation renvoie explicitement à l'étude Momentum pour la notation complète. Les paramètres sont identiques mais l'affichage diffère : Momentum Trend affiche des points sur high/low au lieu d'une courbe continue.
**TRADEX-AI C1** : Le Momentum Trend est plus lisible visuellement dans le dashboard TRADEX-AI qu'une courbe Momentum oscillante. Pour le calcul algorithmique, les deux sont équivalents — utiliser la formule Momentum directement en Python.
*Catégorie : indicateurs_tendance*

### D9457 — Règle de dessin : condition stricte vs non-stricte
🟡 **SYNTHÈSE** (Source : sierra_62_momentum_trend.md) : La condition `M(t-1) >= M(t)` pour le point bas (bearish) inclut l'égalité — ce qui signifie qu'un momentum stable (variation nulle) est traité comme bearish. Il n'existe pas de zone neutre dans ce signal.
**TRADEX-AI C1** : Dans TRADEX-AI, traiter la condition d'égalité (momentum stable) comme un signal neutre/ATTENDRE plutôt que bearish. Modifier la logique Python en conséquence : `M(t) > M(t-1)` = bullish, `M(t) < M(t-1)` = bearish, `M(t) == M(t-1)` = neutre.
*Catégorie : indicateurs_tendance*

### D9458 — Condition de calcul : t > n obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : sierra_62_momentum_trend.md) : Le calcul est uniquement défini pour `t > n` — les `n` premières barres du chart ne produisent pas de signal Momentum Trend. Ce comportement est intrinsèque à tout indicateur basé sur un lookback de n barres.
**TRADEX-AI C1** : Le moteur Python doit vérifier qu'au moins `Length + 1` barres sont disponibles avant d'émettre un signal. Sinon, retourner ATTENDRE par défaut (règle de sécurité déjà présente dans `circuit_breaker.py`).
*Catégorie : gestion_risque_entree*

### D9459 — Application sur Range Bars NT8 : compatibilité
🟡 **SYNTHÈSE** (Source : sierra_62_momentum_trend.md) : Le Momentum Trend fonctionne sur n'importe quel type de chart Sierra Chart (OHLC, Range, Volume, Renko). L'étude n'a pas de contrainte temporelle — elle s'applique barre par barre indépendamment du type de barre.
**TRADEX-AI C1** : Directement applicable sur les Range Bars NT8 transmises via JSON. Pas de conversion de timeframe nécessaire. Le calcul peut être intégré dans `data_reader.py` ou un module dédié.
*Catégorie : indicateurs_tendance*

### D9460 — Interprétation opérationnelle : signal de retournement momentum
🟡 **SYNTHÈSE** (Source : sierra_62_momentum_trend.md) : Transition point-haut → point-bas = retournement baissier (fin d'accélération haussière). Transition point-bas → point-haut = retournement haussier (fin d'accélération baissière). Signal plus précoce qu'un croisement de MA car basé sur l'accélération du prix.
**TRADEX-AI C1** : Dans TRADEX-AI, utiliser le Momentum Trend comme détecteur d'accélération directionnelle en C1. Un signal Belkhayate valide aligné avec un retournement Momentum Trend haussier renforce la conviction ACHAT. À combiner avec le BGC Belkhayate pour filtrer les faux retournements.
*Catégorie : gestion_risque_entree*
