# This ICT Trading Strategy should be illegal...

> **Chaîne :** The Trading Geek  
> **Source :** https://www.youtube.com/watch?v=A-MdplrMAzE  
> **Généré le :** 15/05/2026 à 23:23  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

---
### SETUP #1 : SSL Sweep Reversal AUD/USD [Timestamp : 00:04:42]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - Aucun indicateur technique classique : Zones de liquidité manuelles (Sellside Liquidity) annotées sur le graphique
- **Action du Prix :** Le prix a balayé la Sellside Liquidity (SSL) située sous une zone de support horizontale, chassant les stop-loss des acheteurs positionnés sur les lows. Après ce sweep, le prix a violemment retourné à la hausse, confirmant une prise de liquidité institutionnelle suivie d'un mouvement impulsif haussier.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Low < SSL_Zone.Low) Alors Liquidité_Prise = VRAI;

// Condition de Déclenchement
Si (Liquidité_Prise == VRAI)
ET (Price.Close > SSL_Zone.High)  // Bougie de réintégration au-dessus du support balayé
ET (Bougie_Actuelle.Close > Bougie_Actuelle.Open)  // Confirmation haussière
Alors
    Action = ACHAT;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---
### SETUP #2 : Sell from Supply Zone après Structure Baissière EUR/USD [Timestamp : 00:09:24]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15m
- **Indicateurs Actifs :**
  - Aucun indicateur technique classique : Zone de supply/résistance grise annotée manuellement, annotations jaunes de structure (LH / LL)
- **Action du Prix :** Le prix évolue dans une structure baissière caractérisée par des Lower Highs (LH) et Lower Lows (LL) annotés en jaune. Après un retracement haussier, le prix revient tester la zone de supply/résistance grise marquée "LH". Le setup anticipe un rejet depuis cette zone pour une continuation baissière. À 00:10:11, un trade short est en cours avec entrée sur rejet de la zone grise, SL au-dessus de ~1.0580 et prix autour de 1.0540.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Structure == Lower_High ET Structure == Lower_Low) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Tendance == BAISSIÈRE)
ET (Price.High >= Supply_Zone.Low)  // Prix retrace dans la zone de supply
ET (Price.Close < Supply_Zone.Low)  // Rejet confirmé par clôture sous la zone
ET (Dernier_Pivot == Lower_High)    // Le retour forme un nouveau LH
Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Au-dessus de la zone de supply grise, environ 1.0580
- **Take Profit (TP) :** INCONNU

---
### SETUP #3 : Market Shift Short GBP/USD après Double Top [Timestamp : 00:12:32]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - Aucun indicateur technique classique : Annotation "MARKET SHIFT" sur le graphique, zones de supply/demand grises, rectangle orange marquant une zone de déséquilibre (FVG/Imbalance), sommets encerclés en jaune
- **Action du Prix :** Le prix a formé un double top avec deux sommets encerclés en jaune dans la zone de supply grise supérieure (~1.1625-1.1650). Un Market Shift (cassure de structure) est identifié lorsque le prix casse à la baisse sous le dernier swing low. Une zone de déséquilibre orange/jaune autour de 1.1575 sert de zone d'entrée optimale pour la vente. Le prix a déjà réagi à la baisse depuis cette zone, visant la zone de demand grise inférieure.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Double_Top_Formé == VRAI)
ET (Price.Close < Dernier_Swing_Low)  // Cassure de structure = Market Shift
Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Tendance == BAISSIÈRE)
ET (Price.High >= Imbalance_Zone.Low)  // Retour dans la zone de déséquilibre (~1.1575)
ET (Price.Close < Imbalance_Zone.Low)  // Rejet confirmé
Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Au-dessus de la zone de supply grise supérieure, environ 1.1625–1.1650
- **Take Profit (TP) :** Zone de demand grise inférieure, environ 1.1100–1.1150

---