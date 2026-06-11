# Master Supply & Demand Trading (ULTIMATE In-Depth Guide)

> **Chaîne :** The Trading Geek  
> **Source :** https://www.youtube.com/watch?v=50rVEJhAWdA  
> **Généré le :** 15/05/2026 à 23:27  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

---
### SETUP #1 : Supply Zone Rejection Short [Timestamp : 00:06:48]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif (analyse pure price action avec zones Supply/Demand)
- **Action du Prix :** Le prix a consolidé dans une supply zone (rectangle rouge en haut du graphique), puis a quitté cette zone par le bas avec une forte impulsion baissière. Après cette chute, le prix a rebondi et entamé une tendance haussière prolongée. Actuellement en phase de correction/baisse depuis les sommets. La supply zone agit comme résistance majeure ayant provoqué un rejet baissier violent.

#### 2. Logique Algorithmique
```pseudo-code
// Identification de la Supply Zone
Si (Price consolidait dans une zone étroite AVANT une impulsion baissière forte) Alors
    Marquer zone haute comme SUPPLY_ZONE;
FinSi

// Condition de Tendance
Si (Price.Close < SUPPLY_ZONE.Lower) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price entre dans SUPPLY_ZONE ET montre un rejet (mèche haute / bougie baissière englobante)) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #2 : Demand Zone Pullback Long [Timestamp : 00:17:00]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif (zones de demande tracées manuellement)
- **Action du Prix :** Le prix a effectué un rallye haussier significatif. Un retracement est anticipé vers une zone de support/demande horizontale (rectangle vert). Le scénario illustré montre une chute du prix vers la zone verte suivie d'un rebond haussier en forme de V. La paire semble être AUD/USD ou similaire.

#### 2. Logique Algorithmique
```pseudo-code
// Identification de la Demand Zone
Si (Price consolidait dans une zone étroite AVANT une impulsion haussière forte) Alors
    Marquer zone basse comme DEMAND_ZONE;
FinSi

// Condition de Tendance
Si (Tendance globale = HAUSSIÈRE ET Price retracement vers DEMAND_ZONE) Alors
    Biais = ACHAT;
FinSi

// Condition de Déclenchement
Si (Price.Low touche DEMAND_ZONE ET bougie de rejet haussière apparaît (marteau, englobante haussière)) Alors
    Action = ACHAT;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** En dessous de la zone de support/demande verte (sous le bas de la demand zone)
- **Take Profit (TP) :** INCONNU

---
### SETUP #3 : Supply Zone Rejection Short — EUR/USD 15m [Timestamp : 00:19:16]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15m
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif (supply zone tracée manuellement en rose/rouge)
- **Action du Prix :** Le prix EUR/USD a fortement monté puis a atteint une supply zone (large bande rose/rouge en haut du graphique). Une mèche haute visible pénètre dans la zone avant que le prix ne redescende, signalant un rejet clair depuis la supply zone. La pression vendeuse reprend le contrôle à ce niveau.

#### 2. Logique Algorithmique
```pseudo-code
// Identification de la Supply Zone
Si (Zone historique de consolidation AVANT une impulsion baissière forte) Alors
    Marquer comme SUPPLY_ZONE;
FinSi

// Condition de Tendance
Si (Price.Close approche SUPPLY_ZONE par le bas) Alors
    Anticiper résistance;
FinSi

// Condition de Déclenchement
Si (Price.High pénètre SUPPLY_ZONE ET bougie clôture en dessous avec mèche haute > corps) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Au-dessus de la supply zone (au-dessus du haut de la zone rose/rouge)
- **Take Profit (TP) :** INCONNU

---
### SETUP #4 : Order Block / Supply-Demand Consolidation Zone [Timestamp : 00:20:24]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 30m
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif (rectangles gris marquant des zones d'intérêt / order blocks)
- **Action du Prix :** Le prix a réalisé un fort mouvement haussier suivi d'une correction baissière significative. Il consolide ensuite dans une zone marquée par un rectangle gris, identifiant un order block ou zone de supply/demand. Un second petit rectangle gris est visible plus à gauche sur une zone de consolidation antérieure, servant de référence structurelle.

#### 2. Logique Algorithmique
```pseudo-code
// Identification de l'Order Block
Si (Dernière bougie opposée AVANT une impulsion directionnelle forte) Alors
    Marquer comme ORDER_BLOCK (rectangle gris);
FinSi

// Condition de Tendance
Si (Impulsion précédente = HAUSSIÈRE ET Price retrace vers ORDER_BLOCK) Alors
    Biais = ACHAT;
Sinon Si (Impulsion précédente = BAISSIÈRE ET Price retrace vers ORDER_BLOCK) Alors
    Biais = VENTE;
FinSi

// Condition de Déclenchement
Si (Price entre dans ORDER_BLOCK ET montre une réaction (rejet / absorption)) Alors
    Action = SELON Biais;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #5 : Demand Zone Long — EUR/USD avec RR 3:1+ [Timestamp : 00:22:40]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif (zones TP vertes et SL rouges tracées manuellement)
- **Action du Prix :** Le prix EUR/USD a chuté depuis un sommet puis montre un rebond potentiel dans la zone d'entrée. Un rectangle vert (take profit) significativement plus grand que le rectangle rouge (stop loss) est affiché, illustrant un ratio risque/récompense d'environ 3:1 ou supérieur. L'entrée se fait sur rebond après la baisse, dans une zone de demande implicite.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Structure de marché montre des creux ascendants OU price rebondit sur demand zone) Alors
    Tendance = HAUSSIÈRE (retournement attendu);
FinSi

// Condition de Déclenchement
Si (Price atteint DEMAND_ZONE ET montre un rejet haussier (bougie de retournement)) Alors
    Action = ACHAT;
FinSi

// Validation du Ratio Risque/Récompense
Si (Distance_TP / Distance_SL >= 3.0) Alors
    Trade = VALIDÉ;
Sinon
    Trade = REJETÉ;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Juste en dessous du prix d'entrée, matérialisé par le rectangle rouge (sous la demand zone / dernier creux)
- **Take Profit (TP) :** Grande zone verte au-dessus de l'entrée, ratio risque/récompense d'environ 3:1 ou supérieur, ciblant la prochaine zone de supply ou le sommet précédent

---