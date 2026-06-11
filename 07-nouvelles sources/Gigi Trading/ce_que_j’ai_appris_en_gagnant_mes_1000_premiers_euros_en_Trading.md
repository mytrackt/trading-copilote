# ce que j’ai appris en gagnant mes 1000 premiers euros en Trading

> **Chaîne :** Gigi Trading  
> **Source :** https://www.youtube.com/watch?v=jYaqZni5Esk  
> **Généré le :** 16/05/2026 à 22:46  
> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI

---

---
### SETUP #1 : Croisement MM5/MM12 avec Cassure de Niveau et Volume [Timestamp : 00:02:34]

#### 1. Contexte Visuel Détecté
- **Timeframe :** INCONNU
- **Indicateurs Actifs :**
  - Moyenne Mobile : Période 5, Couleur INCONNU
  - Moyenne Mobile : Période 12, Couleur INCONNU
- **Action du Prix :** Cassure d'un niveau de prix clé accompagnée d'un volume significatif, dans le sens de la tendance dominante

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (MM5 > MM12) Alors Tendance = HAUSSIÈRE;
Si (MM5 < MM12) Alors Tendance = BAISSIÈRE;

// Condition de Déclenchement
Si (MM5 croise MM12 dans le sens de la Tendance
    ET Price.Close franchit Niveau_Clé
    ET Volume > Volume_Moyen) Alors
    Si (Tendance == HAUSSIÈRE) Alors Action = ACHAT;
    Si (Tendance == BAISSIÈRE) Alors Action = VENTE;
FinSi

// Filtre de Fréquence
Nb_Trades_Jour = Maximum 1 trade par session journalière;
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** 3 pips depuis le point d'entrée
- **Take Profit (TP) :** INCONNU

---