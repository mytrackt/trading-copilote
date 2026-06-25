# Extraction SierraChart — Bollinger Squeeze (ID 221)
**Source :** `bundles/sierrachart/sierra_221_bollinger_squeeze.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9111 → D9130 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=221
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Détecteur de compression de volatilité (squeeze BB < KC) utilisable comme filtre d'entrée sur GC/HG/CL/ZW avant signal directionnel.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9111 — Définition du Bollinger Squeeze (Type 1)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Le Bollinger Squeeze calcule un ratio de bandes (Bands Ratio) comparant la largeur des Bandes de Bollinger à celle des Bandes de Keltner. Le squeeze est actif (point vert) quand BB Top > KC Top ET BB Bottom < KC Bottom — c'est-à-dire quand les bandes de Bollinger englobent les bandes de Keltner.
**TRADEX-AI C1** : Condition de squeeze = bandes Bollinger plus larges que Keltner → précède souvent un mouvement directionnel fort sur GC/CL. À surveiller comme pré-condition d'entrée dans le moteur Python (niveau 1, coût $0).
*Catégorie : configuration*

### D9112 — Interprétation du Bands Ratio (histogramme)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Le Bands Ratio (BR) est affiché en histogramme coloré : BR ≥ 0 → vert (BB plus large que KC, momentum croissant), BR < 0 → rouge (BB plus étroite que KC, compression en cours).
**TRADEX-AI C1** : Transition rouge → vert du BR signale la fin de la compression et le début d'une expansion de volatilité. Dans TRADEX-AI, ce signal peut être incorporé comme condition C1 dans la grille /10 pour GC ou CL.
*Catégorie : configuration*

### D9113 — Paramètre Bollinger Bands Length (nB)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input configurable nB = longueur de la moyenne mobile des Bandes de Bollinger. Contrôle la période de calcul de la moyenne centrale et des bandes ±vB×écart-type.
**TRADEX-AI C1** : Paramètre à aligner avec les autres indicateurs du cercle C1. Valeur standard recommandée : 20 périodes (usage courant en analyse technique). À documenter dans settings.py pour cohérence inter-indicateurs.
*Catégorie : indicateurs_tendance*

### D9114 — Paramètre Bollinger Bands Multiplier (vB)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input configurable vB = multiplicateur de l'écart-type pour les Bandes de Bollinger. Détermine l'écartement des bandes supérieure et inférieure par rapport à la moyenne.
**TRADEX-AI C1** : Valeur standard = 2,0. Sur les matières premières volatiles (CL, GC), un vB de 2,0 à 2,5 est approprié. À conserver fixe pour reproductibilité des signaux squeeze.
*Catégorie : indicateurs_tendance*

### D9115 — Paramètre Keltner Bands Length (nK)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input configurable nK = longueur de la moyenne mobile centrale des Bandes de Keltner. Calcul indépendant du nB des Bollinger.
**TRADEX-AI C1** : Permet un ajustement fin de la sensibilité au squeeze. Si nK = nB, les deux bandes répondent à la même fenêtre temporelle. Cohérence recommandée : nK = nB = 20 pour un signal homogène.
*Catégorie : indicateurs_tendance*

### D9116 — Paramètre Keltner True Range MovAvg Length (nATR)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input configurable nATR = longueur de la moyenne mobile de l'ATR utilisée pour calculer les Bandes de Keltner. Contrôle la réactivité des bandes Keltner à la volatilité récente.
**TRADEX-AI C2** : nATR court (ex. 10) → bandes Keltner réactives, squeeze détecté plus tôt. nATR long (ex. 20) → bandes lissées, moins de faux signaux. Sur actifs tradables (GC, HG, CL, ZW), préférer nATR = 14 (cohérence avec ATR standard Belkhayate).
*Catégorie : indicateurs_momentum*

### D9117 — Paramètre Keltner Bands Multiplier (vK)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input configurable vK = multiplicateur ATR pour les bandes de Keltner. Note importante : les bandes Top et Bottom de Keltner utilisent le MÊME multiplicateur (contrairement au Keltner Channel standard qui peut différencier Top/Bottom).
**TRADEX-AI C1** : vK standard = 1,5. Symétrie imposée par le study Sierra Chart — à noter dans la documentation technique TRADEX pour éviter confusion avec Keltner Channel classique (asymétrique possible).
*Catégorie : indicateurs_tendance*

### D9118 — Moving Average Type pour calcul interne
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Input "Moving Average Type for Internal Calculation" contrôle le type de moyenne mobile utilisé simultanément pour les Bollinger Bands, l'ATR, ET les Keltner Bands. Un seul paramètre gouverne les trois calculs.
**TRADEX-AI C1** : La cohérence du type de MA entre les trois composantes est garantie par design. Pour TRADEX-AI, utiliser SMA (Simple) ou EMA (Exponential) selon la préférence backtest. La modification d'un seul input modifie tout le comportement du study — vigilance lors des ajustements.
*Catégorie : indicateurs_tendance*

### D9119 — Squeeze Indicator : couleur verte = squeeze actif
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Le Squeeze Indicator est tracé à la ligne zéro. Point VERT = squeeze actif (BB englobent KC = BB top > KC top ET BB bottom < KC bottom). Point ROUGE = pas de squeeze (BB intérieur à KC, ou une seule condition vérifiée).
**TRADEX-AI C1** : Signal opérationnel direct : un point vert suivi d'un Bands Ratio qui passe positif constitue un signal de "breakout imminent". À intégrer comme condition booléenne dans le filtre pré-Claude (niveau 1) pour réduire les appels API inutiles.
*Catégorie : configuration*

### D9120 — Squeeze Indicator : point rouge = compression terminée ou absente
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : Point ROUGE du Squeeze Indicator = TB(Bollinger) ≤ TB(Keltner) OU BB(Bollinger) ≥ BB(Keltner). La condition OR signifie qu'il suffit que l'une des deux bandes (haute ou basse) sorte de la compression pour casser le squeeze.
**TRADEX-AI C1** : Transition vert → rouge = fin du squeeze = mouvement en cours ou volatilité déjà libérée. Si le BR est encore positif lors de cette transition, le trend est établi. Si BR repasse négatif simultanément, signal ambigu → ATTENDRE (règle de prudence).
*Catégorie : gestion_risque_entree*

### D9121 — Formule Bands Ratio : différence normalisée BB vs KC
🟢 **FAIT VÉRIFIÉ** (Source : sierra_221_bollinger_squeeze.md) : BR = f(X, nB, vB, nK, nATR, vK) — fonction des 6 paramètres clés. Calculé pour t ≥ max{nB, nK, nATR} − 1. Avant cette borne, aucune valeur n'est affichée (warm-up period).
**TRADEX-AI C1** : La période de warm-up = max(nB, nK, nATR). Avec nB=20, nK=20, nATR=14, warm-up = 20 barres. Donnée à prendre en compte lors du démarrage du moteur Python après reconnexion NT8 pour éviter de lire des valeurs NaN ou zéro erronées.
*Catégorie : configuration*

### D9122 — Utilisation du spreadsheet Sierra Chart (.scss)
🔵 **ÉCOLE** (Source : sierra_221_bollinger_squeeze.md) : Sierra Chart fournit le fichier `Bollinger_Squeeze.221.scss` contenant toutes les formules en format tableur. Accessible via File >> Open Spreadsheet après sauvegarde dans le dossier Data Files.
**TRADEX-AI C1** : Le fichier .scss permet la vérification indépendante des calculs. Pour TRADEX-AI, si une implémentation Python du Bollinger Squeeze est nécessaire, ce fichier sert de référence de validation avant mise en production.
*Catégorie : configuration*

### D9123 — Pertinence squeeze pour actifs TRADEX : GC et CL prioritaires
🟡 **SYNTHÈSE** (Source : sierra_221_bollinger_squeeze.md) : La structure du Bollinger Squeeze (compression → explosion) est particulièrement adaptée aux matières premières qui alternent phases de consolidation et de tendance forte.
**TRADEX-AI C1** : Pour GC (Or) et CL (Pétrole WTI), le Bollinger Squeeze peut servir de filtre pré-signal : exiger squeeze_actif = True avant de valider un signal directionnel dans la grille /10. Réduit les entrées en marché sans conviction.
*Catégorie : gestion_risque_entree*

### D9124 — Bands Ratio négatif = phase de squeeze (compression)
🟡 **SYNTHÈSE** (Source : sierra_221_bollinger_squeeze.md) : BR < 0 signifie que les bandes Bollinger sont plus étroites que les bandes Keltner → volatilité comprimée. Cette phase est souvent une période d'attente avant un mouvement directionnel.
**TRADEX-AI C1** : Durant un BR < 0 persistant, le mode Auto TRADEX-AI devrait être en attente (WAIT). Le moteur Python peut surveiller ce paramètre pour filtrer les signaux Claude et éviter les whipsaws en période de faible volatilité.
*Catégorie : gestion_risque_entree*

### D9125 — Double condition pour le squeeze : symétrie des bandes requise
🔵 **ÉCOLE** (Source : sierra_221_bollinger_squeeze.md) : Le squeeze Type 1 (Sierra Chart ID 221) exige que SIMULTANÉMENT BB_top > KC_top ET BB_bottom < KC_bottom. Une seule condition vérifiée ne suffit pas — asymétrie = pas de squeeze.
**TRADEX-AI C1** : Condition stricte : asymétrie de volatilité (une seule bande dépassant) n'est pas un squeeze et ne doit pas déclencher de signal d'attente de breakout. Le filtre booléen Python doit implémenter un AND logique, pas un OR.
*Catégorie : configuration*
