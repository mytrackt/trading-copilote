# ICT Opening Range Theory _ 1st Presented FVG Logic

> **Chaîne :** Single Videos  
> **Source :** https://youtu.be/Zm9Q0NDRxoY  
> **Généré le :** 18/05/2026 à 19:22  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

> **Setups tradables :** 11/21 (10 exclus — pédagogiques)

---

---
### SETUP #1 : Rejet London Open Kill Zone – Continuation Baissière [Timestamp : 00:08:18]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Niveau horizontal : Période INCONNU, Couleur bleue
  - Niveau horizontal : Période INCONNU, Couleur rouge
  - Zone rectangulaire annotée "London Open Kill Zone" : Couleur rose
- **Action du Prix :** Tendance baissière marquée après une zone de rejet identifiée comme London Open Kill Zone. Le prix chute fortement après contact avec la zone rose supérieure.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Bleu) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.touche(London_Open_KillZone) ET Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 20,445.00
- **Take Profit (TP) :** 20,000.00

---
### SETUP #2 : Distribution depuis London Open Killzone [Timestamp : 00:16:36]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Ligne horizontale : Période N/A, Couleur bleue
  - Ligne horizontale : Période N/A, Couleur rouge
  - Zone de distribution annotée "London Open Killzone" : Couleur rose
- **Action du Prix :** Tendance baissière marquée après un pic de prix au contact de la zone rose de distribution. Consolidation visible dans la zone avant la chute.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < LigneHorizontale_Bleue) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.entre_dans(London_Open_Killzone) ET Price.rejette_vers_bas() ET
    Price.Close < LigneHorizontale_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 21,000.00
- **Take Profit (TP) :** 20,600.00

---
### SETUP #3 : Rupture Baissière sous Support Horizontal [Timestamp : 00:20:45]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Ligne horizontale rouge (x2) : niveaux clés de support/résistance
  - Zone grisée : délimite la période de consolidation pré-rupture
- **Action du Prix :** Chute brutale des prix après une zone de consolidation encadrée. Forte bougie baissière visible en fin de graphique après cassure du support horizontal rouge.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge_Inferieur) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.consolide_dans(ZoneGrisée) ET
    Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 19,949.00
- **Take Profit (TP) :** 19,289.00

---
### SETUP #4 : Rejet sur Résistance avec Bougie de Distribution [Timestamp : 00:22:08]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Ligne horizontale rouge : niveau de résistance clé
  - Zone rectangulaire rose : zone de rejet/distribution mise en évidence
- **Action du Prix :** Forte chute du prix après un rejet à la hausse sur la résistance horizontale rouge. Bougie rouge de grande amplitude visible après le rejet, signalant une distribution.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.teste(NiveauHorizontal_Rouge) ET
    Price.forme_bougie_rejet(ZoneRose) ET
    Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 20,645.00
- **Take Profit (TP) :** 19,900.00

---
### SETUP #5 : Cassure Baissière depuis Résistance Horizontale [Timestamp : 00:23:31]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Ligne horizontale rouge : niveau de résistance clé
  - Zone grisée : délimite la région de setup
- **Action du Prix :** Le prix teste le niveau de résistance horizontal rouge puis chute brutalement. Bougie baissière de grande amplitude visible après le rejet du niveau.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.teste(NiveauHorizontal_Rouge) ET
    Price.dans(ZoneGrisée) ET
    Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 21,044.00
- **Take Profit (TP) :** 20,944.00

---
### SETUP #6 : Effondrement depuis Zone de Résistance Rouge/Rose [Timestamp : 00:24:54]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Ligne horizontale rouge : niveau de résistance central
  - Zone rouge/rose supérieure : zone de résistance/distribution
  - Zone grisée : délimite la région d'intérêt
- **Action du Prix :** Forte chute du prix après un mouvement haussier vers la zone rouge/rose supérieure. Bougie baissière prononcée visible dans la partie droite du graphique, confirmant le rejet.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.monte_vers(ZoneResistance_RougeRose) ET
    Price.dans(ZoneGrisée) ET
    Price.rejette_vers_bas() ET
    Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 20,635.00
- **Take Profit (TP) :** 20,149.00

---

---
### SETUP #7 : Rupture Baissière sous Niveau Horizontal – E-mini NQ [Timestamp : 00:26:17]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Niveau horizontal : Période N/A, Couleur rouge
  - Zone d'offre (rectangle) : Période N/A, Couleur rose/rouge
- **Action du Prix :** Forte chute du prix après une zone de consolidation haute, avec une bougie baissière marquée. Le prix rompt sous un niveau horizontal clé en fin de session visible.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.BreakBelow(NiveauHorizontal_Rouge) ET
    ChandelleBaissière.Confirmée == true ET
    Prix.Dans.ZoneOffre == true) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 20,635.00 (axe horizontal de référence)
- **Take Profit (TP) :** 20,390.00 (axe horizontal de référence)

---
### SETUP #8 : Rejet de Résistance Horizontale avec Impulsion Baissière – E-mini NQ [Timestamp : 00:27:40]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Niveau horizontal : Période N/A, Couleur rouge
- **Action du Prix :** Rejet à la hausse suivi d'une forte bougie baissière. Le prix échoue à maintenir le niveau de résistance horizontal et chute brutalement en fin de séquence.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Rouge) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Rejet(NiveauResistance_Rouge) == true ET
    ChandelleBaissière.Confirmée == true ET
    Price.Close < NiveauHorizontal_Rouge) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 21,027.50 (axe horizontal de référence)
- **Take Profit (TP) :** 20,990.00 (axe horizontal de référence)

---
### SETUP #9 : Cassure de Support Majeur avec Bougie Impulsive Baissière – E-mini NQ [Timestamp : 00:29:03]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Niveau horizontal : Période N/A, Couleur rouge
  - Niveau horizontal : Période N/A, Couleur bleu/gris
  - Zone de résistance : Période N/A, Couleur rose
- **Action du Prix :** Forte chute des prix après une zone de consolidation. Le prix casse un support majeur avec une bougie de forte impulsion baissière. Zone de résistance identifiée sur la droite du chart.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauSupport_Majeur) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.BreakBelow(NiveauSupport_Majeur) == true ET
    BougieImpulsive.Baissière == true ET
    Prix.Sous.ZoneResistance_Rose == true) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 21,849.00 (axe horizontal de référence)
- **Take Profit (TP) :** 20,997.00 (axe horizontal de référence)

---
### SETUP #10 : Prise de Profits sur NQ après Sommet – Signal ICT [Timestamp : 00:30:26]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU (double graphique : court terme gauche / long terme droite)
- **Indicateurs Actifs :**
  - Niveau horizontal : Période N/A, Couleur bleue
  - Niveau horizontal : Période N/A, Couleur violette
- **Action du Prix :** Baisse significative après un sommet avec consolidation visible sur le graphique de droite. Message explicite de The Inner Circle Trader suggérant une prise de profits sur NQ.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauHorizontal_Bleu ET
    Price.Close < NiveauHorizontal_Violet) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Rejette(Sommet) == true ET
    ICT.Signal("Might be time to take some profits in NQ") == true ET
    Price.Close < NiveauHorizontal_Bleu) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 21,440.00 (axe horizontal de référence)
- **Take Profit (TP) :** 21,140.00 (axe horizontal de référence)

---
### SETUP #11 : Chute depuis Zone de Résistance avec Confirmation ICT – E-mini NQ [Timestamp : 00:33:12]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU (double graphique côte à côte)
- **Indicateurs Actifs :**
  - Niveau horizontal : Période N/A, Couleur bleue
- **Action du Prix :** Mouvement baissier marqué depuis un niveau de résistance horizontal. Chute prononcée visible sur le graphique de droite avec confirmation par le message ICT de prise de profits sur NQ.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < NiveauResistance_Horizontal) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Rejet(ZoneResistance) == true ET
    ICT.Signal("Might be time to take some profits in NQ") == true ET
    ChuteImpulsive.Confirmée == true) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 36,440.00 (axe horizontal de référence)
- **Take Profit (TP) :** 35,100.00 (axe horizontal de référence)

---
