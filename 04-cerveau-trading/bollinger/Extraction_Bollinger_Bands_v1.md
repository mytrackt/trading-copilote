# Extraction_Bollinger_Bands_v1.md
**Source :** bollingerbands.com — Bollinger Bands (John Bollinger, créateur)  
**URL :** https://www.bollingerbands.com/bollinger-bands  
**Décisions :** D143 → D147  
**Images :** 0 (page texte · scraper_static v1.1)  
**Date extraction :** 23/06/2026  
**Nature source :** Tier 1 — source du créateur (John Bollinger, CFA, CMT).

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — BOLLINGER BANDS

### D143 — Bollinger Bands : définition et mécanisme adaptatif

🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : Les Bollinger Bands sont des courbes tracées autour de la structure de prix, composées d'une **moyenne mobile (bande médiane)**, d'une bande supérieure et d'une bande inférieure, qui répondent à la question : le prix est-il haut ou bas sur une base **relative** ? Elles utilisent l'**écart-type** (standard deviation) pour s'adapter aux conditions de marché changeantes (volatilité dynamique).

🔵 **ÉCOLE** (John Bollinger) : Contrairement aux percentage bands (fixes), Donchian (plus hauts/bas récents) et Keltner (ATR), les Bollinger Bands utilisent l'écart-type comme mécanisme adaptatif.

**TRADEX-AI C1** : Indicateur de volatilité relative. La largeur des bandes = mesure de volatilité courante (lien VIX/régime).

---

### D144 — Paramètres par défaut

🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : Paramètres par défaut inchangés depuis ~35 ans : **moyenne mobile de 20 périodes**, bandes à **± 2 écarts-types** des mêmes données que la moyenne. Calcul de l'écart-type en **population** (population calculation). La bande médiane fonctionne mieux quand elle reflète la **tendance intermédiaire**.

**TRADEX-AI C0** : Export NinjaScript `BollingerBands(20, 2)` sur clôtures, écart-type population. Médiane = SMA 20 (tendance intermédiaire).

---

### D145 — %b et BandWidth

🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : John Bollinger a créé deux indicateurs dérivés :
- **%b** : situe le prix par rapport aux bandes (position relative dans le canal).
- **BandWidth** : largeur des bandes en fonction de la bande médiane (mesure de volatilité).

**TRADEX-AI C1** : %b = position normalisée (comparable entre actifs, contrairement au MACD D57). BandWidth = détection de squeeze (faible volatilité → expansion à venir).

---

### D146 — Trading bands vs envelopes et typologie

🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : Une **bande** s'appuie sur une mesure de tendance centrale (ex. moyenne mobile) ; une **envelope** encadre la structure de prix sans focus central défini. Types principaux aujourd'hui : Donchian, Keltner, Percentage, Bollinger. Percentage bands = fixes (non adaptatives) ; Donchian = plus hauts/bas récents ; Keltner = ATR ; Bollinger = écart-type.

**TRADEX-AI C1** : Distinguer les mécanismes adaptatifs — Keltner (ATR) vs Bollinger (std dev). Combinables (ex. squeeze = Bollinger dans Keltner).

---

### D147 — Usage : tag de bande non confirmé + W bottom

🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : Méthode historique de Bollinger — un **tag de la bande supérieure NON confirmé** par un outil de volume/momentum (ex. Intraday Intensity) = **setup de vente** ; un tag de la bande inférieure non confirmé = setup d'achat. Le **W bottom** (double creux en termes Bollinger) avec %b plus haut au second test = configuration haussière.

**TRADEX-AI C1/C3** : Le tag de bande seul n'est PAS un signal — exiger non-confirmation par un oscillateur volume/momentum (cohérent avec la logique de divergence RSI/MACD D44/D87).

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D143
Dernière décision session  : D147
Prochaine décision         : D148
Total décisions            : 5
Total KB cumulé            : D1 → D147
```

---

*Extraction_Bollinger_Bands_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
