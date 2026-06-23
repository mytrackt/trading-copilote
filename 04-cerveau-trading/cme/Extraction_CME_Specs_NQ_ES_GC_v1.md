# Extraction_CME_Specs_NQ_ES_GC_v1.md
**Source :** CME Group — Contract Specs (PDF officiels, fournis manuellement)  
**Fichiers :** `cme_nq_specs.pdf` · `cme_es_specs.pdf` · `cme_gc_specs.pdf`  
**Décisions :** D173 → D176  
**Images :** 0 (specs texte · scraper_pdf v1)  
**Date extraction :** 23/06/2026 (PDF datés 23/06/2026)  
**Nature source :** Tier 1 — spécifications officielles CME Group. Données factuelles 🟢.

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — SPECS CONTRATS (COUCHE C0)

### D173 — E-mini Nasdaq-100 (NQ) : spécifications

🟢 **FAIT VÉRIFIÉ** (Source : cme_nq_specs.pdf, CME Group) :
- **Contract Unit** : $20 × Nasdaq-100 Index
- **Price Quotation** : USD et cents par point d'indice
- **Tick Size (outright)** : 0,25 point d'indice
- **Tick Value** : **$5,00** par tick (0,25 × $20)
- **Trading Hours (Globex)** : Dimanche 18:00 – Vendredi 17:00 ET, maintenance quotidienne 17:00–18:00 ET
- **Settlement** : **Financially Settled** (cash)
- **Termination of Trading** : 9:30 ET le **3e vendredi** du mois de contrat
- **Product Code** : Globex/Clearing **NQ** (BTIC NQT · TACO NQQ · TMAC NQX)
- **Listed Contracts** : trimestriels (Mar/Jun/Sep/Dec), 6 trimestres consécutifs + 2 juin + 4 décembre additionnels

**TRADEX-AI C0** : `NQ` · tick 0,25 = $5,00 → conversion points↔$ pour P&L, stops, R/R. Cash-settled (pas de livraison).

---

### D174 — E-mini S&P 500 (ES) : spécifications

🟢 **FAIT VÉRIFIÉ** (Source : cme_es_specs.pdf, CME Group) :
- **Contract Unit** : $50 × S&P 500 Index
- **Price Quotation** : USD et cents par point d'indice
- **Tick Size (outright)** : 0,25 point d'indice
- **Tick Value** : **$12,50** par tick (0,25 × $50)
- **Trading Hours (Globex)** : Dimanche 18:00 – Vendredi 17:00 ET, maintenance quotidienne 17:00–18:00 ET
- **Settlement** : **Financially Settled** (cash)
- **Termination of Trading** : 9:30 ET le **3e vendredi** du mois de contrat
- **Product Code** : Globex/Clearing **ES** (BTIC EST · TACO ESQ · TMAC ESX)
- **Listed Contracts** : trimestriels (Mar/Jun/Sep/Dec), **21 trimestres consécutifs**

**TRADEX-AI C0** : `ES` · tick 0,25 = $12,50. ES sert aussi de **confirmation marché** (cercle confirmation). Cash-settled.

---

### D175 — Gold Futures (GC) : spécifications

🟢 **FAIT VÉRIFIÉ** (Source : cme_gc_specs.pdf, CME Group / COMEX) :
- **Contract Unit** : **100 troy ounces**
- **Price Quotation** : USD et cents par troy ounce
- **Tick Size** : 0,10 par troy ounce
- **Tick Value** : **$10,00** par tick (0,10 × 100)
- **Trading Hours (Globex)** : Dimanche – Vendredi 18:00 – 17:00 ET, **pause de 60 min/jour** à 17:00 ET
- **Settlement** : **Deliverable** (livraison physique)
- **Termination of Trading** : 12:30 CT le **3e dernier jour ouvré** du mois de contrat
- **Product Code** : Globex/Clearing **GC** (TAS GCT · TAM GCD)
- **Listed Contracts** : mensuels, 26 mois consécutifs + tout Jun/Dec dans les 72 mois les plus proches
- **Rulebook** : COMEX 113

**TRADEX-AI C0 ⚠️** : `GC` · tick 0,10 = $10,00. **Livrable physiquement** → garde-fou obligatoire : clôturer/rouler AVANT le 3e dernier jour ouvré pour éviter toute obligation de livraison. Diffère de NQ/ES (cash).

---

### D176 — Synthèse C0 : table tick value (moteur P&L)

🟢 **FAIT VÉRIFIÉ** (Source : 3 PDF CME ci-dessus) :

| Code | Contrat | Contract Unit | Tick | Tick Value | Settlement | Fin de trading |
|------|---------|---------------|------|------------|------------|----------------|
| **NQ** | E-mini Nasdaq-100 | $20 × indice | 0,25 pt | **$5,00** | Cash | 3e vendredi 9:30 ET |
| **ES** | E-mini S&P 500 | $50 × indice | 0,25 pt | **$12,50** | Cash | 3e vendredi 9:30 ET |
| **GC** | Gold | 100 oz | 0,10 $/oz | **$10,00** | **Livraison physique** | 3e dernier jour ouvré 12:30 CT |

**TRADEX-AI C0** : Constantes moteur pour conversion points/ticks → $ (P&L, sizing, R/R, stops). À exporter dans `config\settings.py` (tick_size, tick_value par actif). ⚠️ GC = gestion d'échéance physique distincte.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D173
Dernière décision session  : D176
Prochaine décision         : D177
Total décisions            : 4
Total KB cumulé            : D1 → D176
```

---

*Extraction_CME_Specs_NQ_ES_GC_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre · Specs à revérifier sur cmegroup.com avant tout usage live*
