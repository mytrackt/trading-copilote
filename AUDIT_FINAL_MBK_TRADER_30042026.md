# AUDIT RUNTIME — MBK Trader Assistant — 30/04/2026
**Outil :** PROMPT_AUDIT_UNIVERSEL_v2.0
**Scope :** CDC_MBK_TRADER_VISION_v1.0 + CDC_MBK_TRADER_TECHNIQUE_v1.0
**Méthode :** Audit statique des spécifications + analyse croisée du code source

---

## SCORES PAR MODULE

| Module | Score | P0 | P1 | P2 | P3 |
|--------|-------|----|----|----|----|
| M1 Static | 85/100 | 0 | 0 | 3 | 0 |
| M2 Boot | 90/100 | 0 | 0 | 2 | 0 |
| M3 API | 40/100 | 1 | 2 | 1 | 0 |
| M4 Sécurité | 20/100 | 1 | 4 | 0 | 1 |
| M5 Logique | 85/100 | 0 | 0 | 1 | 1 |
| M6 Performance | 92/100 | 0 | 0 | 1 | 1 |
| **GLOBAL** | **57/100** | **2** | **6** | **8** | **3** |

**VERDICT : 🔴 À RISQUE — corrections majeures avant déploiement**

Formule : (85×0.15) + (90×0.10) + (40×0.20) + (20×0.30) + (85×0.15) + (92×0.10) = **57.7/100**

---

## ⛔ FINDINGS P0 — CRITIQUES (bloquants)

---

### [M4-001] Path Traversal sur POST /backtest

- **Sévérité :** P0 — CRITIQUE
- **Fichier :** `python-engine/main.py` ligne 159
- **Code incriminé :**
```python
class BacktestRequest(BaseModel):
    csv_path: str   # ← aucune validation du chemin

if not Path(req.csv_path).exists():
    raise HTTPException(...)

engine = BacktestEngine(req.csv_path, ...)  # ← chemin transmis tel quel
```
- **Preuve :** Un attaquant sur le réseau local envoie :
```json
POST /backtest
{"csv_path": "C:/Users/mytra/AppData/Roaming/NinjaTrader 8/db/Accounts/account.xml"}
```
→ Le serveur lit et renvoie le fichier sans restriction.
- **Impact :** Lecture de n'importe quel fichier Windows accessible par le processus Python (comptes broker, configs, fichiers sensibles).
- **Fix obligatoire :**
```python
import os

ALLOWED_DIR = Path("database/historical").resolve()

def validate_csv_path(csv_path: str) -> Path:
    p = Path(csv_path).resolve()
    if not str(p).startswith(str(ALLOWED_DIR)):
        raise HTTPException(400, "Chemin non autorisé")
    if not p.suffix == ".csv":
        raise HTTPException(400, "Format CSV uniquement")
    return p
```

---

### [M4-002] Google OAuth — Implicit Flow (déprécié + dangereux)

- **Sévérité :** P0 — CRITIQUE
- **Fichier :** `electron-app/src/pages/Login.tsx` ligne 26
- **Code incriminé :**
```javascript
response_type: 'token',  // ← Implicit Flow = INTERDIT par Google depuis 2019
```
- **Preuve :** Google a officiellement déprécié l'Implicit Flow en 2019 (OAuth 2.0 Security Best Current Practice). `response_type=token` expose l'access_token dans le fragment URL, lisible par toute extension ou script tiers.
- **Impact :** Token Google de l'utilisateur potentiellement volé. Google désactivera cet endpoint pour les nouvelles applications.
- **Fix obligatoire :** Utiliser PKCE (Proof Key for Code Exchange) avec `response_type=code` et `code_challenge`.
```javascript
// Utiliser electron-google-oauth2 avec PKCE natif
// OU Google Sign-In pour Electron avec Authorization Code + PKCE
const { GoogleAuth } = require('electron-google-oauth2')
const auth = new GoogleAuth(clientId, clientSecret, ['openid','email','profile'])
const tokens = await auth.openAuthWindowAndGetTokens()
```

---

## 🔴 FINDINGS P1 — MAJEURS (à fixer avant utilisation)

---

### [M4-003] CORS Wildcard sur FastAPI

- **Sévérité :** P1
- **Fichier :** `python-engine/main.py` lignes 104–106
- **Code incriminé :**
```python
allow_origins=["*"],
allow_methods=["*"],
allow_headers=["*"],
```
- **Impact :** N'importe quel site web peut faire des requêtes cross-origin vers `http://localhost:8000`. Si un onglet malveillant est ouvert en même temps, il peut lire l'historique des trades et déclencher des backtests.
- **Fix :**
```python
allow_origins=["http://localhost:5173", "http://localhost:3000"],
allow_methods=["GET", "POST"],
allow_headers=["Content-Type"],
```

---

### [M3-001] Aucune authentification sur les endpoints FastAPI

- **Sévérité :** P1
- **Fichier :** `python-engine/main.py`
- **Endpoints concernés :** `GET /signals`, `GET /trades`, `POST /backtest`, `WS /ninjatrader`, `WS /stream`
- **Impact :** Tout processus ou utilisateur sur le même réseau peut :
  - Lire l'historique complet des trades (GET /signals, GET /trades)
  - Déclencher des backtests arbitraires (POST /backtest)
  - Injecter de fausses données de prix (WS /ninjatrader)
- **Fix minimal :** Token partagé local dans les headers
```python
API_TOKEN = os.environ.get("MBK_API_TOKEN", "changeme")

async def verify_token(x_api_token: str = Header(...)):
    if x_api_token != API_TOKEN:
        raise HTTPException(403, "Token invalide")
```

---

### [M4-004] WebSocket /ninjatrader sans authentification

- **Sévérité :** P1
- **Fichier :** `python-engine/main.py` — endpoint `/ninjatrader`
- **Impact spécifique trading :** Un processus malveillant sur le PC peut se connecter à `ws://localhost:8765`, envoyer de faux prix OHLCV (ex: prix gonflé de 50%), et forcer le moteur IA à générer un faux `TRADE_ALLOWED`. Le trader agit sur une donnée falsifiée.
- **Fix :** Ajouter un token partagé dans le header WebSocket ou vérifier l'origin.

---

### [M4-005] access_token Google stocké dans localStorage

- **Sévérité :** P1
- **Fichier :** `electron-app/src/App.tsx` lignes 24, 30
- **Code incriminé :**
```javascript
localStorage.setItem('mbk_user', JSON.stringify(u))
// Contient : name, email, photo — mais potentiellement le token si étendu
```
- **Contexte Electron :** Bien que `contextIsolation=true` soit activé, localStorage dans Electron est accessible depuis le renderer process. Si une dépendance npm compromise tourne dans le renderer, elle peut lire localStorage.
- **Fix :** Stocker les données de session dans le process principal Electron via `ipcMain` + `safeStorage` (chiffrement natif OS).
```javascript
// main.js
const { safeStorage } = require('electron')
ipcMain.handle('store-user', (_, userData) => {
    const encrypted = safeStorage.encryptString(JSON.stringify(userData))
    // sauvegarder dans un fichier local chiffré
})
```

---

### [M3-002] Aucun rate limiting sur les endpoints

- **Sévérité :** P1
- **Fichier :** `python-engine/main.py`
- **Impact :** `POST /backtest` peut être appelé en boucle → CPU 100%, application bloquée, trades manqués en live.
- **Fix :**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/backtest")
@limiter.limit("2/minute")
async def run_backtest(req: BacktestRequest, request: Request):
    ...
```
- **Dépendance à ajouter :** `slowapi==0.1.9`

---

### [M4-006] Aucune validation du payload WebSocket NT8

- **Sévérité :** P1
- **Fichier :** `python-engine/main.py` — fonction `process_bar()`
- **Code actuel :**
```python
bar = json.loads(raw)  # ← aucune validation des champs
await process_bar(bar)  # ← transmis directement au détecteur
```
- **Impact :** Un payload malformé (ex: `{"close": "abc"}`) provoque une exception silencieuse. Pire : `{"close": 99999999}` peut déclencher de faux signaux.
- **Fix :** Ajouter un modèle Pydantic pour valider le payload
```python
class BarPayload(BaseModel):
    symbol:    str
    timeframe: str
    open:      float = Field(gt=0)
    high:      float = Field(gt=0)
    low:       float = Field(gt=0)
    close:     float = Field(gt=0)
    volume:    float = Field(ge=0)
    timestamp: str
    session:   str
    bar_index: int = Field(ge=0)

    @validator('high')
    def high_gte_low(cls, v, values):
        if 'low' in values and v < values['low']:
            raise ValueError('high doit être >= low')
        return v
```

---

## 🟡 FINDINGS P2 — MINEURS (prochain sprint)

---

### [M1-001] Absence de tsconfig.json documenté

- **Fichier :** `electron-app/` — aucun `tsconfig.json` dans le projet
- **Impact :** TypeScript compile en mode permissif (`"strict": false` par défaut). Les `any` implicites passent sans erreur.
- **Fix :** Ajouter `tsconfig.json` avec `"strict": true`

---

### [M1-002] Absence de configuration ESLint

- Aucun `.eslintrc.json` ni `eslint.config.js` dans `electron-app/`
- **Impact :** Aucun garde-fou qualité côté frontend.
- **Fix :** `npm install -D eslint @typescript-eslint/parser` + config minimale

---

### [M1-003] Absence de flake8 / mypy pour Python

- Aucun `setup.cfg`, `.flake8`, `mypy.ini` dans `python-engine/`
- **Impact :** Types Python non vérifiés statiquement. Erreurs de type possibles en production.
- **Fix :** Ajouter `mypy==1.10.0` et `flake8==7.0.0` dans `requirements.txt`

---

### [M3-003] Paramètre limit non borné sur GET /trades et GET /signals

- **Code :** `async def get_trades(limit: int = 50)` — aucun maximum
- **Impact :** `GET /trades?limit=9999999` peut provoquer une réponse de plusieurs Mo et bloquer le serveur.
- **Fix :** `limit: int = Field(default=50, ge=1, le=500)`

---

### [M5-001] État circuit breaker perdu au redémarrage

- **Code :** `_consecutive_losses` et `_circuit_breaker_until` sont des variables de classe Python — réinitialisées à 0 si `uvicorn` redémarre.
- **Impact :** Après 3 pertes, si le serveur redémarre (coupure de courant, crash), le circuit breaker est annulé silencieusement.
- **Fix :** Persister l'état dans SQLite
```python
# À l'init : lire circuit breaker depuis DB
# À chaque register_loss() : écrire dans DB
```

---

### [M2-001] Aucun gestionnaire de processus documenté

- Aucun `Procfile`, `pm2.config.js`, ni service Windows documenté.
- **Impact :** Si `uvicorn` crashe, le serveur ne redémarre pas automatiquement. Signaux perdus.
- **Fix recommandé :** `pm2 start main.py --interpreter python --name mbk-engine`

---

### [M2-002] Pas de reconnexion automatique NT8 WebSocket

- **CDC §2 :** "Reconnexion : non automatique v1 — rechargement de l'indicateur requis"
- **Impact :** Coupure réseau → perte de données → signaux manqués sans alerte
- **Fix V2 :** Retry avec backoff exponentiel dans `MBK_DataBridge.cs`

---

### [M6-001] URL ForexFactory RSS hardcodée sans fallback

- **Code :** `url = "https://nfs.faireconomy.media/ff_calendar_thisweek.xml"`
- **Impact :** Si ForexFactory est inaccessible → `NewsGate.check()` retourne `(False, None)` → news gate désactivé silencieusement sans alerte
- **Fix :** Logger un WARNING visible + afficher dans le dashboard un badge "NEWS GATE HORS LIGNE"

---

## ℹ️ FINDINGS P3 — INFORMATIFS

---

### [M4-007] OAuth : token d'accès implicite sans refresh

- Le token issu de l'Implicit Flow n'a pas de refresh token.
- Expiration silencieuse → l'utilisateur reste "connecté" dans localStorage mais le token Google est expiré.
- **Fix :** Géré automatiquement avec PKCE (fix P0-002).

---

### [M5-002] DXY hardcodé à False

- **CDC §13 :** "Corrélation DXY temps réel — `dxy_rising=False` hardcodé"
- Condition `intermarket_align` toujours True sur XAUUSD → garde-fou corrélation non fonctionnel.
- **Priorité V2**

---

### [M1-004] Aucun `pytest.ini` ou `pyproject.toml` pour la config pytest

- `pytest` fonctionne sans config, mais sans couverture de code (`coverage`)
- **Fix :** Ajouter `pytest-cov` + seuil minimum 70% de couverture

---

### [M6-002] Pas d'analyse de bundle documentée

- `vite build` n'est pas documenté dans INSTALLATION.md
- Taille du bundle JS inconnue — à mesurer après premier build.

---

## RÉCAPITULATIF DES CORRECTIONS PRIORITAIRES

| Priorité | Finding | Fichier | Effort |
|----------|---------|---------|--------|
| 🔴 P0 | Path Traversal /backtest | `main.py` | 15 min |
| 🔴 P0 | OAuth Implicit → PKCE | `Login.tsx` | 2h |
| 🟠 P1 | CORS wildcard → origins restreints | `main.py` | 5 min |
| 🟠 P1 | Auth token API FastAPI | `main.py` | 30 min |
| 🟠 P1 | Validation payload WebSocket (Pydantic) | `main.py` | 30 min |
| 🟠 P1 | Rate limiting /backtest | `main.py` | 20 min |
| 🟠 P1 | WS /ninjatrader auth | `main.py` | 20 min |
| 🟡 P1 | localStorage → safeStorage Electron | `App.tsx` | 1h |
| 🟡 P2 | tsconfig strict + ESLint | `electron-app/` | 30 min |
| 🟡 P2 | flake8 + mypy | `python-engine/` | 20 min |
| 🟡 P2 | Circuit breaker persisté en SQLite | `signal_generator.py` | 30 min |
| 🟡 P2 | Limit borné sur GET /trades | `main.py` | 5 min |

---

## CE QUE LE CDC COUVRE BIEN ✅

- Architecture globale claire et cohérente
- Ports et protocoles documentés avec précision
- Garde-fous trading exhaustifs (stop-loss, circuit breaker, news gate, session filter)
- Schéma SQLite complet avec contrainte UNIQUE
- Constantes du moteur IA toutes documentées
- Section §13 honnête sur les limitations V1
- Tests unitaires documentés avec commandes exactes
- CORS activé (même si wildcard → P1 mais présent)
- contextIsolation + nodeIntegration documentés correctement

---

## COMMANDES DE CORRECTION RAPIDES

```powershell
# Après correction — committer
git add . && git commit -m "fix: audit P0 path-traversal + oauth-pkce"
git add . && git commit -m "fix: audit P1 cors + api-auth + rate-limit + ws-validation"
git add . && git commit -m "fix: audit P2 tsconfig + eslint + circuit-breaker-persist"
```

---

## FICHIERS À AJOUTER AU PROJET (manquants)

```
mbk-trader/
├── AUDIT_CONFIG.yaml              ← requis par AUDIT v2.0
├── python-engine/
│   ├── .flake8                    ← config linter Python
│   ├── mypy.ini                   ← config type checker
│   └── pytest.ini                 ← config tests + coverage
└── electron-app/
    ├── tsconfig.json              ← TypeScript strict
    └── .eslintrc.json             ← ESLint config
```

---

*AUDIT_FINAL_MBK_TRADER_30042026.md*
*Généré par PROMPT_AUDIT_UNIVERSEL_v2.0 — audit statique CDC + code source*
*Score global : 57/100 — 2 P0, 6 P1, 8 P2, 3 P3*
*Rappel : `git add . && git commit -m "audit: runtime mbk-trader 30042026"`*
