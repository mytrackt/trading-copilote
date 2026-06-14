# Modules — Trading Copilote

> Architecture modulaire : chaque module fonctionne seul ou integre dans le copilote principal.
> Mis a jour le 01/05/2026

---

## Module 1 — MBK Trader Assistant
**Statut :** ⏸️ 60% — En pause volontaire (01/05/2026)
**Repo source :** C:\Projects\mbk-trader\ (repo Git separe — 4 commits propres)
**CDC Vision :** docs/mbk-trader/CDC_MBK_TRADER_VISION_v1.1.md
**CDC Technique :** docs/mbk-trader/CDC_MBK_TRADER_TECHNIQUE_v1.1.md
**Reprendre :** C:\Projects\mbk-trader\REPRENDRE_ICI.md

**Fonction :**
Detecte automatiquement les fausses cassures institutionnelles (Liquidity Grab)
sur matieres premieres et intermarches.
Signale les entrees apres pullback Fibonacci confirme.
Genere 4 statuts : TRADE_ALLOWED / WAIT / REDUCE_RISK / NO_TRADE

**Marches couverts :** XAUUSD, XAGUSD, CL (Petrole), NG (Gaz), ES, NQ, DXY
**Timeframes :** M5, M15, H1
**Sessions :** LONDON (09h-12h) / NEW_YORK (15h-18h) GMT+1

**Ce qui est fait (100% recuperable) :**
- Code source complet : 34 fichiers Python 3.14 compatible
- Python engine teste : 5/5 tests PASSES
- Securite auditee : score 57 -> 85/100 (Path traversal, OAuth PKCE, CORS, rate limiting)
- CDC v1.1 complets
- Electron app : code genere, npm install non execute

**Ce qui reste :**
1. cd electron-app && npm install
2. Creer electron-app/.env depuis .env.example
3. Creer Google Client ID (console.cloud.google.com)
4. Creer python-engine/.env avec MBK_API_TOKEN
5. Tester : uvicorn main:app --port 8000
6. Tester : npm run dev dans electron-app/
7. Charger MBK_DataBridge.cs dans NinjaTrader 8

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

## Module 2 — TRADEX-AI
**Statut :** 🔜 Blueprint V4 pret — developpement non demarre
**Methode :** Belkhayate (Barycenter + Direction + Energie + Pivots)
**Marches trading :** Or, Cuivre, Petrole, Ble
**Marches confirmation :** Dollar (DXY), SP500, VIX
**Regle entree :** 3/4 trading + 2/3 confirmation alignes = signal valide
**Blueprint :** RAPPORT_ORTOGONEX_V4_POST_AUDIT.md
**KB :** code/knowledge_base/KNOWLEDGE_BASE_MASTER.json (2337 regles Belkhayate)
**Skills :** 05-skills/ (10 skills generes — skill-01 a skill-10)

**Ce qui est fait :**
- Blueprint V4 Ortogonex complete
- Knowledge Base : 142 videos YouTube transcrites, 2337 regles extraites
- 10 skills Belkhayate generes

**Ce qui reste :**
1. Dashboard React (données NT8 JSON -> signal ; PAS de screenshot)
2. Lecture marché via fichiers JSON NinjaTrader 8 (PAS de Claude Vision API)
3. Regle 3/4 + 2/3 marchés alignes
4. News Gate, Circuit Breaker, Rate Limiting
5. Deploy Vercel + Railway

---

## Feuille de Route Globale

| Phase | Module | Action | Statut |
|-------|--------|--------|--------|
| Phase 1 | Belkhayate KB | Scraping YouTube 143 videos | ✅ Termine |
| Phase 2 | Belkhayate KB | Extraction 2337 regles | ✅ Termine |
| Phase 3 | Belkhayate KB | 10 skills generes | ✅ Termine |
| Phase 4 | MBK Trader | Code 34 fichiers + securite | ⏸️ 60% pause |
| Phase 4b | MBK Trader | npm install + .env + NinjaTrader | 🔜 A reprendre |
| Phase 5 | TRADEX-AI | Dashboard + lecture NT8 JSON | 🔜 Prochain |
| Phase 6 | TRADEX-AI | Deploy Vercel + Railway | ⏳ Futur |
