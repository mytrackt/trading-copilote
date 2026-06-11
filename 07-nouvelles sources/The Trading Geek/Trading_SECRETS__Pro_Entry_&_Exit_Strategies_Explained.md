# Trading SECRETS_ Pro Entry & Exit Strategies Explained

> **Chaîne :** The Trading Geek  
> **Source :** https://www.youtube.com/watch?v=kis7l0y1JUg  
> **Généré le :** 15/05/2026 à 23:31  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

---
### SETUP #1 : Rejet sur zone de supply NZD/USD [Timestamp : 00:01:24]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif
- **Action du Prix :** Après une forte baisse suivie d'un rallye haussier, le prix consolide sous une zone de résistance/supply (rectangle gris). Des bougies indécises apparaissent, puis un rejet visible (mèches hautes, encerclé en blanc) confirme la pression vendeuse sur cette zone.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < Zone_Supply_Supérieure) Alors Tendance = BAISSIÈRE_POTENTIELLE;

// Condition de Déclenchement
Si (Price atteint Zone_Supply_Grise ET
    Bougie forme mèche_haute de rejet ET
    Bougie_Close < Zone_Supply_Bas) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #2 : Confirmation vente sur supply zone NZD/USD 15min [Timestamp : 00:02:48]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15min
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif
- **Action du Prix :** Le prix a fait une forte impulsion haussière puis consolide dans la zone de supply/résistance supérieure (rectangle gris). Plusieurs bougies rouges à mèches hautes confirment le rejet. Sur les frames suivantes (04:12 et 04:40), la pression vendeuse se confirme avec une chute depuis la zone de supply, suivie d'une petite bougie verte de pullback.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close entre dans Zone_Supply_Grise_Supérieure ET
    Price forme bougies_rouges_mèches_hautes) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price rejette Zone_Supply_Supérieure ET
    Nombre_Bougies_Baissières >= 2 ET
    Bougie_Close < Zone_Supply_Bas) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Au-dessus de la zone de supply grise supérieure (environ 0.6470)
- **Take Profit (TP) :** INCONNU

---
### SETUP #3 : Double top retest entry GBP/USD [Timestamp : 00:05:36]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur jaune
- **Action du Prix :** Le prix a formé un double top puis casse le support. Une ligne jaune dessinée illustre le mouvement attendu : après la cassure, le prix revient retester le niveau cassé (ancien support devenu résistance). L'annotation "ENTER HERE instead!" en vert indique que l'entrée optimale se fait sur le retest et non au moment de la cassure initiale.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price forme Double_Top ET
    Price.Close < Neckline_Support) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Neckline est cassé à la baisse ET
    Price revient retester Neckline_comme_résistance ET
    Bougie_Rejet sur ancien_support) Alors
    Action = VENTE;
    // NE PAS entrer au moment de la cassure initiale
    // ATTENDRE le pullback/retest
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #4 : Piège débutant vs entrée pro sur support GBP/USD [Timestamp : 00:06:04]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif
- **Action du Prix :** Le prix revient tester un niveau de support horizontal (zone grise) après une baisse. Un cercle jaune et une flèche indiquent le point où les "noob traders" entrent prématurément. Le setup est présenté comme une erreur pédagogique : entrer directement sur le support sans confirmation supplémentaire est un piège.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close approche Zone_Support_Grise) Alors Tendance = INCERTAINE;

// Condition ERREUR (ce qu'il ne faut PAS faire)
Si (Price touche Zone_Support ET
    Aucune_Confirmation_Bougie) Alors
    Action = NE_PAS_ACHETER;  // Piège débutant
FinSi

// Condition CORRECTE
Si (Price touche Zone_Support ET
    Confirmation_Momentum_Shift ET
    Bougie_Retournement_Validée) Alors
    Action = ACHAT;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #5 : Achat sur zone de support avec momentum shift GBP/USD [Timestamp : 00:07:28]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15min
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif
- **Action du Prix :** Le prix a chuté fortement puis atteint une zone de support (rectangle gris). Une grande flèche verte anticipe un rebond haussier. Sur les frames suivantes (07:56 et 08:24), un trade long est exécuté avec boîte verte (TP) et boîte rouge (SL) visibles. Un momentum shift (changement de structure) est identifié au point de retournement (cercle blanc), confirmant le retournement haussier. Une zone de selling pressure est également identifiée.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close atteint Zone_Support_Grise ET
    Selling_Pressure diminue) Alors Tendance = RETOURNEMENT_HAUSSIER;

// Condition de Déclenchement
Si (Price touche Zone_Support_Grise ET
    Momentum_Shift détecté (changement de structure) ET
    Bougie_Retournement confirmée au creux) Alors
    Action = ACHAT;
    Entrée = Niveau_Zone_Support_Grise;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** En dessous de la zone de support grise (boîte rouge visible sous le point d'entrée)
- **Take Profit (TP) :** Au-dessus de l'entrée (boîte verte visible), ratio risque/récompense estimé à environ 1:2

---
### SETUP #6 : Achat sur support XAU/USD avec cassure haussière [Timestamp : 00:10:16]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15min
- **Indicateurs Actifs :**
  - Aucun indicateur technique actif
- **Action du Prix :** Le prix a rebondi depuis un creux et remonte vers une zone de résistance/supply (rectangle gris) autour de 1728. Une trajectoire haussière jaune dessinée à la main projette un scénario de continuation à la hausse. Sur les frames suivantes (10:44 et 11:12), un outil de position longue (risk/reward) est affiché. Le prix casse la zone grise et monte fortement avec des bougies vertes impulsives, dépassant largement la zone de TP — trade gagnant confirmé.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close rebondit depuis creux ET
    Price approche Zone_Résistance_Grise ~1728) Alors Tendance = HAUSSIÈRE;

// Condition de Déclenchement
Si (Price rebondit sur Zone_Support_Grise ET
    Momentum haussier confirmé ET
    Price.Close > Zone_Grise_Bas) Alors
    Action = ACHAT;
    Entrée = Proche_Zone_Support_Grise;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Zone rouge sous le point d'entrée, approximativement au niveau 1714 (sous la zone grise de support)
- **Take Profit (TP) :** Zone verte au-dessus de l'entrée, approximativement au niveau 1736, ratio risque/récompense environ 1:2