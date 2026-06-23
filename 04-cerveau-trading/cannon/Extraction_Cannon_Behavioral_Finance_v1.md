# Extraction_Cannon_Behavioral_Finance_v1.md
**Source :** CFA Institute Research Foundation — *Behavioral Finance: Theories and Evidence* (Byrne & Brooks, 2008) — hébergé par Cannon Financial  
**URL :** https://www.cannonfinancial.com/uploads/main/Behavioral_Finance-Theories_Evidence.pdf  
**Décisions :** D121 → D130  
**Images :** 0 (PDF texte — pas d'image à certifier · scraper_pdf v1)  
**Date extraction :** 23/06/2026  
**Nature source :** revue de littérature académique (CFA Institute). Fiabilité haute.

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — CADRE

### D121 — Finance comportementale : prémisse

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : La finance traditionnelle suppose des agents **rationnels** (traitement efficace et non biaisé de l'information, maximisation d'utilité). La finance comportementale pose que les investisseurs (ou une minorité significative) sont sujets à des **biais comportementaux** rendant leurs décisions financières moins que pleinement rationnelles. Les preuves viennent de la psychologie cognitive, appliquées au contexte financier.

**TRADEX-AI C5 / garde-fous** : Justifie les garde-fous anti-biais du moteur (discipline d'exécution, règles déterministes) — l'IA copilote doit contrer les biais de l'opérateur humain.

---

## BLOC 2 — LES BIAIS COGNITIFS CLÉS

### D122 — Overconfidence & overoptimism

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les investisseurs **surestiment leur capacité** et la précision de l'information dont ils disposent.

**TRADEX-AI gestion_risque** : Biais le plus dangereux pour le sizing — contremesure : taille de position déterministe plafonnée, jamais discrétionnaire à la hausse sur « conviction ».

---

### D123 — Representativeness

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les investisseurs évaluent les situations sur des **caractéristiques superficielles** plutôt que sur les probabilités sous-jacentes.

**TRADEX-AI C1** : Contremesure — exiger des critères statistiques/déterministes (grille /10) plutôt qu'une « ressemblance » de pattern jugée à l'œil.

---

### D124 — Conservatism

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les prévisionnistes **s'accrochent à leurs croyances antérieures** face à une information nouvelle.

**TRADEX-AI** : Contremesure — réévaluation systématique du signal à chaque nouvelle donnée (staleness monitor + recalcul), pas d'ancrage sur la thèse initiale.

---

### D125 — Availability bias

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les investisseurs **surévaluent la probabilité** d'événements récemment observés/vécus (mémoire fraîche).

**TRADEX-AI** : Contremesure — décisions basées sur des fenêtres statistiques fixes (corrélations 30j, etc.), pas sur le dernier trade marquant.

---

### D126 — Frame dependence & anchoring

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : La **forme de présentation** de l'information affecte la décision ; les individus s'ancrent sur une référence (ex. prix d'achat).

**TRADEX-AI gestion_risque** : Contremesure — le stop et la cible se calculent sur la structure (ATR, S/R, comptage P&F Wyckoff D111), jamais sur le prix d'entrée comme ancre.

---

### D127 — Mental accounting

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les individus rangent la richesse dans des **compartiments mentaux séparés** et ignorent la fongibilité et les effets de corrélation.

**TRADEX-AI C7** : Contremesure — gestion du risque au niveau **portefeuille global** (corrélations C7 GC/HG/CL/ZW/ES), pas trade par trade isolé.

---

### D128 — Regret aversion

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.1) : Les individus décident de manière à **éviter la douleur émotionnelle** du regret en cas de résultat défavorable.

**TRADEX-AI** : Contremesure — règles d'entrée/sortie pré-engagées et automatisables ; l'aversion au regret pousse à ne pas couper les pertes ou à ne pas reprendre après une perte.

---

## BLOC 3 — THÉORIE DES PERSPECTIVES

### D129 — Prospect theory & loss aversion (Kahneman-Tversky 1979)

🔵 **ÉCOLE** (Source : behavioral_finance.md p.1, Kahneman & Tversky 1979) : La **prospect theory** décrit la décision en situation risquée. Les résultats sont évalués par rapport à un **point de référence subjectif** (ex. prix d'achat). Les investisseurs sont **loss averse** : comportement **risk-seeking face aux pertes** (on prend plus de risque pour éviter d'acter une perte) et **risk-averse face aux gains** (on sécurise trop tôt).

**TRADEX-AI gestion_risque** : Biais central — explique le « cut winners short, let losers run ». Contremesure forte : R/R ≥ 1:2 imposé, stop non déplaçable contre soi, prise de profit selon cibles structurelles (non émotionnelle).

---

### D130 — Les professionnels ne sont PAS immunisés

🟢 **FAIT VÉRIFIÉ** (Source : behavioral_finance.md p.2) : Plusieurs articles examinent si les **traders et gérants professionnels** subissent les mêmes biais que les particuliers : ils sont « far from immune to the biases ».

**TRADEX-AI** : Justifie le mode copilote — même un opérateur expérimenté (Abdelkrim) reste exposé aux biais ; les garde-fous déterministes s'appliquent en mode Manuel comme Auto.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D121
Dernière décision session  : D130
Prochaine décision         : D131
Total décisions            : 10
Total KB cumulé            : D1 → D130
```

---

*Extraction_Cannon_Behavioral_Finance_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
