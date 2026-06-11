# See Trades BEFORE They Happen

> **Chaîne :** Single Videos  
> **Source :** https://youtu.be/IODJYl3bKu4  
> **Généré le :** 16/05/2026 à 23:12  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

### SETUP #1 : Tendance Baissière UBER avec Canal Descendant [Timestamp : 00:00:00]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur Rouge
  - EMA : Période INCONNU, Couleur Bleue
  - Canal Baissier : Période INCONNU, Couleur Noir (tracé manuel)
- **Action du Prix :** Tendance baissière marquée sur UBER (NYSE) depuis 13:00, prix évoluant de ~96.60 vers ~95.30 avec des chandeliers rouges dominants. Un canal baissier dessiné manuellement encadre la structure de prix. Les deux EMAs sont orientées à la baisse et agissent comme résistances dynamiques. Pattern triangle/fanion baissier visible en haut du graphique avant la continuation baissière.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_Rouge ET Price.Close < EMA_Bleue) Alors
    Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Retest(EMA_Rouge OU EMA_Bleue) ET
    Price.Rejet(Canal_Haut) ET
    Chandelier = ROUGE) Alors
    Action = VENTE;
FinSi

// Confirmation structurelle
Si (Price.Lower_Low = TRUE ET
    Price.Lower_High = TRUE) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #2 : Rejet sur Zone de Résistance avec Annotation UBER [Timestamp : 00:03:09]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur Rouge
  - EMA : Période INCONNU, Couleur Bleue
- **Action du Prix :** Flèche bleue tracée manuellement suggérant une anticipation de rebond haussier depuis un point bas vers ~95.90-96.00, dans un contexte globalement baissier. Des patterns en zigzag/triangles sont annotés à différents niveaux, avec des lignes horizontales rouges marquant des zones de support/résistance autour de 95.60-96.00.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_Rouge ET Price.Close < EMA_Bleue) Alors
    Tendance = BAISSIÈRE;

// Condition de Déclenchement (rebond technique)
Si (Price.Atteint(Zone_Support ~95.30) ET
    Flèche_Annotation = HAUSSIÈRE) Alors
    Action = ACHAT_COURT_TERME; // rebond vers 95.90-96.00

// Condition alternative (continuation baissière)
Si (Price.Rejet(Zone_Resistance ~95.90-96.00) ET
    Chandelier = ROUGE) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #3 : Vente sur Rejet Zone Annotée 96.00-96.20 UBER [Timestamp : 00:12:36]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur Bleue
  - EMA : Période INCONNU, Couleur Rouge
- **Action du Prix :** Tendance baissière avec annotation manuscrite rouge encerclant une zone de résistance autour de 96.00-96.20. Une flèche pointe vers le bas depuis cette zone, indiquant une continuation baissière anticipée. Prix actuel affiché à 95.12. Plusieurs cercles bleus marquent des points de rejet successifs sous les moyennes mobiles.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_Bleue ET Price.Close < EMA_Rouge) Alors
    Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Retrace(Zone_Resistance ~96.00-96.20) ET
    Price.Rejet(EMA_Rouge OU EMA_Bleue) ET
    Annotation_Flèche = VERS_BAS) Alors
    Action = VENTE;
FinSi

// Confirmation par structure
Si (Price.Lower_High_Confirmé = TRUE ET
    Chandelier_Rejet = ROUGE) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #4 : Color Change at 20-MA — Short UBER [Timestamp : 00:14:42]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période 20, Couleur Bleue
- **Action du Prix :** Baisse marquée sur UBER suivie d'un rebond, avec annotation manuelle d'une flèche en arc illustrant le mouvement. Le chat visible dans la vidéo mentionne explicitement "Color change at or near the 20-MA" et "beautiful drop with entries". Prix autour de 95.32.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_20) Alors
    Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Retrace(EMA_20) ET
    Chandelier.Couleur_Change(Vert → Rouge) ET
    Price.Near(EMA_20) = TRUE) Alors
    Action = VENTE; // "Color change at or near the 20-MA"
FinSi

// Signal de confirmation
Si (Chandelier_Précédent = VERT ET
    Chandelier_Actuel = ROUGE ET
    Price.Position = SOUS_EMA_20) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #5 : Color Change at 20-MA — Short NVDA [Timestamp : 00:16:48]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période 20, Couleur Rose/Rouge
  - EMA : Période INCONNU, Couleur Violette
- **Action du Prix :** Baisse sur NVDA après un sommet autour de 167-168, prix actuel à 163.23. Le chat mentionne "Color change at or near the 20-MA" et "beautiful drop with multiple entries". Tendance baissière visible avec plusieurs points d'entrée possibles sur les retours vers la EMA 20.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_20_Rose ET
    Price.Sommet_Récent ~167-168) Alors
    Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (Price.Retrace(EMA_20) ET
    Chandelier.Couleur_Change(Vert → Rouge) ET
    Price.Near(EMA_20) = TRUE) Alors
    Action = VENTE; // Entrées multiples possibles
FinSi

// Confirmation
Si (EMA_20 > Price.Close ET
    EMA_Violette > Price.Close) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #6 : Rebond sur 20-MA — Long BTC/USD [Timestamp : 00:17:51]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 15m
- **Indicateurs Actifs :**
  - MA : Période 20, Couleur INCONNU
- **Action du Prix :** Forte hausse sur BTC/USD avec chandelles haussières après une zone de consolidation. Un cercle est dessiné manuellement autour d'une zone de prix spécifique (~113,800) avec une flèche pointant vers le haut. Prix autour de 116,000-117,600 USD. Le chat mentionne "20-MA" et "high probability setups".

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close > MA_20) Alors
    Tendance = HAUSSIÈRE;

// Condition de Déclenchement
Si (Price.Retrace(MA_20 ~113,800) ET
    Price.Rebond(MA_20) = TRUE ET
    Chandelier = VERT) Alors
    Action = ACHAT; // "High probability setup"
FinSi

// Confirmation
Si (Price.Close > MA_20 ET
    Chandelier_Précédent = REBOND_VALIDÉ) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #7 : Breakdown de Consolidation — Short META [Timestamp : 00:18:54]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - MA : Période INCONNU, Couleur Bleue
- **Action du Prix :** Consolidation en range sur META (NASDAQ) clairement délimitée par des annotations rectangulaires (rouge et bleu), suivie d'une forte cassure baissière avec chandelles rouges. Prix autour de 717.51 au moment de la frame.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Range
Si (Price.Dans_Rectangle(Zone_Consolidation) = TRUE ET
    Price.Croisements_Multiples = TRUE) Alors
    Pattern = CONSOLIDATION;

// Condition de Déclenchement
Si (Price.Casse_Bas(Rectangle_Support) ET
    Chandelier = ROUGE ET
    Volume_Cassure > Volume_Moyen) Alors
    Action = VENTE; // Breakdown de la zone de consolidation
FinSi

// Confirmation
Si (Price.Close < Rectangle_Bas ET
    MA_Bleue > Price.Close) Alors
    Confirmation = VALIDÉE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU

---

### SETUP #8 : Tendance Baissière avec Pattern de Breakout — Short PYPL [Timestamp : 00:22:03]

#### 1. Contexte Visuel Détecté
- **Timeframe :** 2m
- **Indicateurs Actifs :**
  - EMA : Période INCONNU, Couleur Rouge
  - EMA : Période INCONNU, Couleur Bleue
- **Action du Prix :** Forte tendance baissière sur PYPL (NASDAQ), prix en baisse de 5.73% autour de 71.36. Un schéma dessiné à la main illustre un pattern de consolidation suivi d'une cassure baissière (breakdown). Chandeliers rouges dominants avec continuation à la baisse marquée depuis le sommet. Rebond partiel visible vers 71.97 avant nouvelle impulsion baissière.

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close < EMA_Rouge ET Price.Close < EMA_Bleue ET
    Price.Variation_Journée < -5%) Alors
    Tendance = BAISSIÈRE_FORTE;

// Condition de Déclenchement
Si (Price.Consolide(Zone_Haute) ET
    Price.Casse_Bas(Support_Consolidation) ET
    Chandelier = ROUGE) Alors
    Action = VENTE; // Breakdown du pattern de consolidation

// Entrée alternative sur rebond
Si (Price.Retrace(EMA_Rouge OU EMA_Bleue) ET
    Price.Rejet = TRUE) Alors
    Action = VENTE;
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** INCONNU
- **Take Profit (TP) :** INCONNU