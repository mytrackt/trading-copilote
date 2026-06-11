# Je n'utilise que cette stratégie de Trading (et ça suffit largement)

> **Chaîne :** Gigi Trading  
> **Source :** https://www.youtube.com/watch?v=Sgd6zaQCqF4  
> **Généré le :** 16/05/2026 à 22:29  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

### SETUP #1 : Rejet de Zone + Confirmation Structure M5 [Timestamp : 00:03:54]

#### 1. Contexte Visuel Détecté
- **Timeframe :** M5
- **Indicateurs Actifs :**
  - Aucun indicateur technique — price action pure
- **Action du Prix :** Mèche de rejet sur zone de décision, suivi d'un changement de structure sur M5 ou d'une bougie impulsive de validation

#### 2. Logique Algorithmique
```pseudo-code
// Étape 1 : Identifier la tendance
Si (Price.HigherHighs ET Price.HigherLows) Alors Tendance = HAUSSIÈRE;
Si (Price.LowerHighs ET Price.LowerLows) Alors Tendance = BAISSIÈRE;

// Étape 2 : Tracer les zones de décision
Zone = NiveauSupport OU NiveauResistance OU ZoneCassée_Retestée;

// Étape 3 : Attendre le signal
Si (Prix.Atteint(Zone) ET
   (Bougie.Mèche_Rejet == true
    OU StructureM5.Changement == true
    OU Bougie.Impulsive == true)) Alors
    Signal = VALIDE;
FinSi

// Étape 4 : Entrer avec logique
Si (Signal == VALIDE ET Trade.ASensDansTendance == true) Alors
    Action = ACHAT OU VENTE; // selon direction de tendance
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Juste au-dessus du dernier sommet (en vente) / juste sous le dernier creux (en achat)
- **Take Profit (TP) :** Ratio minimum 1:1 — objectif recommandé 1:2

---

### SETUP #2 : Rejet sur Résistance avec Confirmation Unité Inférieure [Timestamp : 00:05:38]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU (confirmation sur unité de temps inférieure)
- **Indicateurs Actifs :**
  - Aucun indicateur technique — price action pure
- **Action du Prix :** Le prix arrive sur une résistance et rejette avec une grande mèche, suivi d'un petit retournement visible sur les bougies ou d'une cassure de structure sur l'unité de temps inférieure (exemple cité : EUR/USD)

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Prix.Approche(NiveauResistance)) Alors Contexte = POTENTIEL_REJET;

// Condition de Déclenchement
Si (Bougie.Mèche_Haute == GRANDE ET Prix.AtResistance == true) Alors
    SignalPrimaire = VALIDE;
FinSi

// Confirmation sur unité inférieure
Si (SignalPrimaire == VALIDE ET
   (StructureUTF_Basse.Retournement == true
    OU StructureUTF_Basse.Cassure == true)) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #3 : Pullback sur Zone Support/Résistance — Entrée dans la Tendance [Timestamp : 00:06:56]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - FVG (Fair Value Gap) : Période INCONNU, Couleur verte/rouge
  - Zone de consolidation : Période INCONNU, Couleur noire (rectangle)
  - Zone de résistance : Période INCONNU, Couleur violette
- **Action du Prix :** Le prix effectue un pullback sur une zone de support/résistance précédemment testée (incluant FVG ou zone de consolidation), puis amorce une reprise dans le sens de la tendance avec une mèche de rejet visible

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Prix.Au_Dessus(ZoneConsolidation) ET Tendance == HAUSSIÈRE) Alors
    Biais = ACHAT;
FinSi

// Condition de Déclenchement
Si (Prix.Pullback_Vers(ZoneSupport OU FVG OU ZoneCassée)) Alors
    Attendre_Signal = true;
FinSi

Si (Attendre_Signal == true ET
    Bougie.Mèche_Rejet == true) Alors
    Action = ACHAT;
    EntréeSur = PullbackSuivant_AprèsMèche;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** Juste sous la mèche de la bougie d'entrée
- **Take Profit (TP) :** Objectif minimum 1:1 — cible recommandée 1:2 (deux fois le risque) / Zone de résistance suivante (ex. : ~4120 sur le graphique observé)

---