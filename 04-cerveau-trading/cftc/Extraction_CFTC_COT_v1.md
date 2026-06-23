# Extraction_CFTC_COT_v1.md
**Source :** CFTC — Commitments of Traders (COT) Explanatory Notes  
**URL :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/ExplanatoryNotes/index.htm  
**Décisions :** D156 → D162  
**Images :** 0 (page texte · scraper_static v1.1)  
**Date extraction :** 23/06/2026  
**Nature source :** Tier 1 — source officielle régulateur (CFTC).

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — RAPPORT COT (CERCLE C3 — INSTITUTIONNELS)

### D156 — Open Interest : définition

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md §Open Interest) : L'**open interest** est le total de tous les contrats futures et/ou options ouverts et non encore compensés (par transaction, livraison, exercice…). L'agrégat de tout l'open interest long = l'agrégat de tout l'open interest short. L'open interest détenu par un trader = sa **position**. Pour le rapport Futures-and-Options-Combined, les options sont converties en équivalent-futures via les **delta factors** des bourses.

**TRADEX-AI C3** : Open interest = base du COT. À collecter (CFTC hebdo) pour le cercle institutionnels.

---

### D157 — Firmes déclarantes et seuils de reporting

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Les firmes déclarantes (clearing members, FCM, brokers étrangers) déposent des rapports quotidiens. Si un trader atteint le **seuil de reporting** de la CFTC dans un mois de future/option, toute sa position dans cette commodity est déclarée. L'agrégat des positions déclarées représente généralement **70 à 90 % de l'open interest total** d'un marché.

**TRADEX-AI C3** : Le COT couvre 70-90 % de l'OI — proxy fiable mais non exhaustif du positionnement.

---

### D158 — Classification Commercial vs Non-commercial

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Un trader déclarable est classé **commercial** ou **non-commercial**. Commercial = utilise les futures pour le **hedging** (CFTC Reg 1.3, déclaré via **Form 40**) — typiquement producteurs/industriels. Non-commercial = spéculateurs (managed funds, etc.). Un trader peut être commercial sur une commodity et non-commercial sur une autre, mais jamais les deux sur la même commodity.

**TRADEX-AI C3** : Distinction clé — **commercials = « smart money » hedgers** (souvent contrariens aux extrêmes) · non-commercials = spéculateurs (suiveurs de tendance). Lecture cœur du COT.

---

### D159 — Positions non déclarables (Nonreportable)

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Les **Nonreportable Positions** = open interest total moins les Reportable Positions (long et short). Le nombre de traders et leur classification commercial/non-commercial y sont **inconnus**. (Proxy usuel du « petit » trader / retail.)

**TRADEX-AI C3** : Nonreportable ≈ retail — souvent utilisé comme indicateur contrarien aux extrêmes.

---

### D160 — Spreading

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Le **spreading** mesure dans quelle mesure un trader non-commercial détient des positions long et short **égales**. Exemple : 2 000 long + 1 500 short → 500 en « Long » et 1 500 en « Spreading ». Exclut l'intermarket spreading.

**TRADEX-AI C3** : Le spreading isole la position directionnelle nette des spéculateurs (retirer la part neutre).

---

### D161 — Index Traders (rapport Supplemental)

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Le rapport **Supplemental** ajoute une catégorie **Index Traders** sur certains marchés agricoles — traders répliquant un indice de matières premières (long-only, roulé de future en future), tirés des catégories commercial et non-commercial (managed/pension funds passifs, swap dealers hedgeant un index OTC).

**TRADEX-AI C3** : Sur ZW (blé), tenir compte des Index Traders (long-only structurel) qui biaisent le positionnement.

---

### D162 — Ratios de concentration (4 et 8 plus gros)

🟢 **FAIT VÉRIFIÉ** (Source : cot_explanatory.md) : Le rapport montre le **pourcentage d'open interest détenu par les 4 et 8 plus gros traders déclarables**, sans égard à leur classification. Calculé sur base gross long / gross short ET net long/short (après compensation des positions égales de chaque trader).

**TRADEX-AI C3** : Concentration élevée (4/8 plus gros) = risque de marché dominé par peu d'acteurs → signal de fragilité/retournement potentiel.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D156
Dernière décision session  : D162
Prochaine décision         : D163
Total décisions            : 7
Total KB cumulé            : D1 → D162
```

---

*Extraction_CFTC_COT_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
