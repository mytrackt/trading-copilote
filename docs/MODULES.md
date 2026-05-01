# Modules — Trading Copilote

## Module 1 — MBK Trader Assistant
**Statut :** v1.1 — Code genere + Securite auditee (score 85+/100)
**Repo :** C:\Projects\mbk-trader\ (repo Git separe)
**CDC Vision :** docs/mbk-trader/CDC_MBK_TRADER_VISION_v1.1.md
**CDC Technique :** docs/mbk-trader/CDC_MBK_TRADER_TECHNIQUE_v1.1.md

**Fonction :**
Detecte automatiquement les fausses cassures institutionnelles (Liquidity Grab)
sur matieres premieres et intermarches.
Signale les entrees apres pullback Fibonacci confirme.
Genere 4 statuts : TRADE_ALLOWED / WAIT / REDUCE_RISK / NO_TRADE

**Marches couverts :** XAUUSD, XAGUSD, CL (Petrole), NG (Gaz), ES, NQ, DXY
**Timeframes :** M5, M15, H1
**Sessions :** LONDON (09h-12h) / NEW_YORK (15h-18h) GMT+1

**Stack :**
- NinjaTrader 8 add-on (C# NinjaScript) -> flux donnees temps reel
- Python FastAPI -> moteur IA detection (localhost:8000)
- Electron React -> dashboard desktop Windows
- SQLite -> stockage local

**Garde-fous trading implementes :**
- Stop-Loss : 1.5 x ATR obligatoire
- Risk/Trade : max 1% du capital
- Circuit Breaker : 3 pertes consecutives -> pause 4h (persiste SQLite)
- News Gate : ForexFactory RSS, bloque +/-30 min HIGH IMPACT
- Filtrage session : signaux ignores hors LONDON/NEW_YORK/OVERLAP

---

## Module 2 — TRADEX-AI (en cours)
**Statut :** Blueprint V4 pret — developpement non demarre
**Methode :** Belkhayate (Barycenter + Direction + Energie + Pivots)
**Marches trading :** Or, Cuivre, Petrole, Ble
**Marches confirmation :** Dollar (DXY), SP500, VIX
**Regle entree :** 3/4 trading + 2/3 confirmation alignes = signal valide
**Blueprint :** RAPPORT_ORTOGONEX_V4_POST_AUDIT.md

---

*Mis a jour le 01/05/2026*
