# Extraction KB — ChartSchool : Fundamental Analysis (Overview)
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/fundamental-analysis  
**Version :** v1 enrichie (texte + descriptions visuelles charts)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS ANTI-HALLUCINATION

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart ou la source officielle lue |
| 🟡 | Interprétation plausible basée sur observation visuelle, non certaine |
| 🔵 | Règle générale citée par auteur reconnu (Murphy, Schwager, ChartSchool) |
| ⏳ | À vérifier dans une autre source avant usage en signal |
| 🔴 | Affirmation risquée ou non prouvée — ne pas utiliser tel quel |
| ⚫ | Non auditable |

---

## 1. POSITIONNEMENT DE CETTE PAGE DANS LA KB

🔵 Cette page ne promeut **pas** l'analyse fondamentale. Elle l'utilise comme **repoussoir** pour démontrer les forces de l'analyse technique. Valeur KB TRADEX : comprendre pourquoi le prix prime sur les fondamentaux → justification philosophique de l'approche Belkhayate.

---

## 2. ANALYSE FONDAMENTALE VS TECHNIQUE — DISTINCTION CLEF

🔵 **Analyse fondamentale** = étude des facteurs économiques, financiers et qualitatifs sous-jacents (résultats, bilans, macro, management) pour estimer la **valeur intrinsèque** d'un actif.

🔵 **Analyse technique** = étude du **mouvement de prix et de volume** sur un graphique. Elle ne cherche pas à estimer la valeur, elle lit ce que le marché *fait*.

🔵 **Complémentarité (position ChartSchool) :** les deux approches ne s'excluent pas. Un technicien peut utiliser les fondamentaux pour sélectionner *quoi* analyser, puis le graphique pour décider *quand* agir.

---

## 3. PREUVE VISUELLE #1 — LES TENDANCES LONGUES TERME SONT LISIBLES SUR LE CHART

🟢 **Chart $SPX Monthly (1970 → 1999) + $UST10Y (taux 10 ans US) :**

### Panneau supérieur — S&P 500 (échelle logarithmique) :
- **Zone "10-year Trading Range" (ovale bleu, 1970→1982) :** le SPX oscille sans direction entre ~60 et ~120 pendant 12 ans. Aucune tendance exploitable. Un analyste fondamental de 1975 aurait eu du mal à timer l'entrée.
- **"20-year Trend" (trendline verte, 1982→1999) :** montée continue de ~100 (1982) à ~1469 (déc 1999) — gain de ~1369% en 17 ans sur l'indice. La trendline est touchée plusieurs fois comme support (1987, 1990, 1994).
- **SPX au 31 déc 1999 :** 1469.25 (Open: 1388.91, High: 1473.13, Low: 1387.38)
- **Volume :** 28.1 milliards, +5.78% sur la journée

### Panneau inférieur — $UST10Y (Taux Treasury 10 ans) :
- **Pic :** ~15-16% en 1984
- **Trendline descendante rouge (1984→1999) :** les taux baissent structurellement pendant 15 ans
- **Taux au 31 déc 1999 :** 6.45%
- **Relation inverse visible :** quand les taux baissent (1984→1999), le SPX monte (confirmation de la 20-year Trend). C'est la corrélation macro actions/taux.

🔵 **Règle déductible :** la relation inverse taux longs / marchés actions est un facteur macro à surveiller. Une hausse de taux prolongée est un **vent contraire** pour les marchés actions. ⏳ À surveiller pour TRADEX sur les futures or (corrélation or/taux réels).

🟡 **Interprétation pédagogique ChartSchool :** le graphique mensuel permet de visualiser des cycles de marché (trading range 10 ans, tendance 20 ans) qu'aucune analyse fondamentale trimestrielle ne peut anticiper directement.

---

## 4. PREUVE VISUELLE #2 — LA ROTATION SECTORIELLE EST INVISIBLE SANS GRAPHIQUE

🟢 **Chart $SPX Daily vs Indices Sectoriels — Performance Relative (sept 1999 → 13 mars 2000) :**

| Indice | Secteur | Performance |
|--------|---------|-------------|
| $DJINET | Internet | 🔴 +163.27% |
| $SOX | Semiconducteurs | 🔴 +165.14% |
| $OSX | Oil Services | 🟡 +23.39% |
| $SPX | S&P 500 | ⚪ +6.41% (référence) |
| $DRG | Pharmacie | 🟡 -4.05% |
| $BKX | Banques | 🟡 -17.19% |

🟢 **Observations visuelles :**
- **Internet ($DJINET, rouge) et Semiconducteurs ($SOX, violet) :** décollent verticalement à partir de jan 2000, atteignent +163-165% en 6 mois. Les deux courbes sont quasiment superposées.
- **Oil Services ($OSX, rose/magenta) :** surperforme le SPX (+23%) mais avec forte volatilité, visible par les pics et creux sur la courbe.
- **SPX (noir) :** progression modeste +6.41% — l'indice masque la dispersion extrême des secteurs.
- **Banques ($BKX, bleu foncé) et Pharma ($DRG, vert) :** sous-performance nette, corrélation négative avec la bulle internet.

🔵 **Règle de Relative Strength (RS) :** l'indice global ne dit pas tout. Identifier les secteurs qui surperforment l'indice de référence = **rotation sectorielle**. Un titre dans un secteur fort a un avantage structurel.

🟡 **Application TRADEX :** bien que TRADEX cible les futures (NQ, ES, or), la RS sectorielle peut servir à **filtrer le contexte macro** avant un signal Belkhayate. Ex : si $SOX en forte surperformance → NQ (Nasdaq) favorisé en direction longue.

🔴 **Attention :** ce chart date de mars 2000, pic de la bulle dot-com. Les performances +163% de $DJINET ont ensuite été effacées à -90%+. La surperformance passée n'est pas prédictive. ⏳

---

## 5. PREUVE VISUELLE #3 — LES ANALYSTES FONDAMENTAUX RÉAGISSENT APRÈS LE PRIX (CAS AMZN)

🟢 **Chart AMZN Daily — Amazon.com (Nasdaq, déc 2000 → fév 2001) :**

### Chronologie des recommandations analystes vs prix :

| Date | Recommandation analyste | Prix AMZN | Situation réelle |
|------|------------------------|-----------|-----------------|
| Déc 28, 2000 | ⚠️ *"Technical warning signal"* | ~$75 | Signal technique baissier |
| Jan 2000 | *"Strong Buy!"* | ~$75 | Prix au plus haut |
| Fév 2000 | *"Accumulate!"* | ~$65 | Prix en baisse |
| Mars 2000 | *"Recommended"* | ~$55 | Déclin en cours |
| Avr 2000 | *"Attractive"* | ~$45 | Déclin accéléré |
| Mai 2000 | *"Buy"* | ~$40 | -47% depuis le sommet |
| Juin 2000 | *"Accumulate"* | ~$35 | - |
| Juil 2000 | *"Reiterated Strong Buy!"* | ~$30 | - |
| Sep 2000 | *"Strong Buy!"* | ~$25 | - |
| Nov 2000 | *"Buy!"* | ~$22 | - |
| **Déc 20, 2000** | **"Hold!" — Premier vrai avertissement** | **~$19** | **-80% depuis le sommet** |
| Jan 2001 | *"Upgraded to Strong Buy - $30 Target"* | ~$15 | Cible irréaliste |
| Fév 2001 | *"Buy!"* | ~$13.69 | -82% |

🟢 **CMF(80) au 16 fév 2001 :** -0.087 → Chaikin Money Flow négatif = sortie nette de capitaux depuis 80 jours. La pression vendeuse institutionnelle est confirmée par le CMF pendant toute la période des "Strong Buy" analystes.

🔵 **Leçon centrale (ChartSchool) :** les analystes fondamentaux ont émis un premier avertissement ("Hold") seulement lorsque le titre avait déjà perdu **80% de sa valeur**. Le signal technique (déc 28, 2000) précédait ce premier avertissement d'**une semaine exactement** et au même niveau de prix (~$75).

🔵 **Règle anti-fondamental pour TRADEX :** ne jamais filtrer un signal technique baissier sur la base d'une recommandation "Strong Buy" analyste. Le prix et le volume (CMF) sont plus rapides que les révisions de recommandations.

🟡 **Biais des analystes :** conflit d'intérêt possible (banques d'investissement liées aux sociétés analysées). Le chartiste n'a pas ce biais — il lit le prix.

---

## 6. RÈGLES GÉNÉRALES DÉDUITES (APPLICABLES TRADEX)

🔵 **R1 — Prix avant fondamentaux :** un signal technique (trendline cassée, CMF négatif) prime sur une recommandation d'analyste. Le marché intègre l'information plus vite.

🔵 **R2 — Cycles longs visibles sur graphiques :** les cycles de 10-20 ans (trading range, mega-tendance) ne sont accessibles qu'en lisant le chart mensuel/hebdomadaire. Les fondamentaux trimestriels ne les capturent pas.

🔵 **R3 — CMF comme filtre de flux institutionnel :** CMF < 0 = sortie de capitaux institutionnels. Un signal d'achat dans un contexte CMF négatif est à risque élevé. ⏳ Vérifier période optimale CMF pour futures intraday.

🔵 **R4 — Rotation sectorielle = contexte directionnel :** identifier le secteur le plus fort permet de biaiser la direction du trade (long sur secteur RS+ vs short sur secteur RS-). Application TRADEX : RS or vs SPX avant signal COG sur gold futures.

🔵 **R5 — Le "Hold" tardif = signal de capitulation analyste :** historiquement, la première recommandation "Hold" après une longue série de "Buy" arrive **après** le pic. Elle peut indiquer que le bas n'est pas encore atteint (les institutionnels ont déjà vendu depuis longtemps).

---

## 7. CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Calcul du CMF et période optimale → voir extraction spécifique indicateurs
⏳ Méthode de calcul de la Relative Strength (RS) entre secteurs → non détaillée ici
⏳ Application aux futures et matières premières → mentionnée mais non développée
⏳ Corrélation or / taux réels US (observable sur le chart taux mais non explicitée)

---

*Fin d'extraction — ChartSchool Fundamental Analysis Overview — v1 enrichie visuellement*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
