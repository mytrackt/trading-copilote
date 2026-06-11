# I Tested 100+ Trading Indicators (Found The Combination That Pays The Most)

> **Chaîne :** Single Videos  
> **Source :** https://www.youtube.com/watch?v=PmQTvswoZvw  
> **Généré le :** 19/05/2026 à 00:02  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

> **Setups tradables :** 1/7 (6 exclus — pédagogiques)

---

---
### SETUP #1 : Retest Support avec Confirmation Triple Indicateur [Timestamp : 00:11:22]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 1h
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur Bleue
  - RSI : Période INCONNU, Couleur Blanche
  - OBV : Période INCONNU, Couleur Jaune
- **Action du Prix :** Le prix est revenu tester un ancien niveau de résistance devenu support (zone ~173.800) que les acheteurs ont activement défendu, confirmant l'inversion de polarité

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close > EMA) Alors Tendance = HAUSSIÈRE;
Si (RSI > 50) Alors Momentum = HAUSSIER;
Si (OBV.Direction == HAUSSE) Alors Volume = CONFIRME;

// Condition de Déclenchement
Si (
    Price.Retest == AncienNiveau_Résistance_Devenu_Support
    ET Tendance == HAUSSIÈRE
    ET Momentum == HAUSSIER
    ET Volume == CONFIRME
) Alors
    Action = ACHAT;
    Entrée = Clôture_Bougie_Sur_Support;
FinSi

// Filtre de Qualité
Si (NombreIndicateurs_Verts < 3) Alors
    Action = IGNORER;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 173.800 (niveau d'axe / ancien support-résistance)
- **Take Profit (TP) :** 174.400 (niveau d'axe suivant)

---