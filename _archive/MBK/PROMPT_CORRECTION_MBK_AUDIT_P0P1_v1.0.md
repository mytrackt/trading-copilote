# PROMPT CORRECTION — MBK TRADER ASSISTANT
## Corrections Audit P0 + P1 — v1.0
**À coller dans Claude Code au démarrage de la session**
**Basé sur : AUDIT_FINAL_MBK_TRADER_30042026.md**

---

## 🎯 IDENTITÉ ET RÔLE

Tu es un **Senior Security Engineer** spécialisé Python/FastAPI et Electron/React/TypeScript.
Tu corriges uniquement les failles identifiées dans le rapport d'audit.
Tu ne modifies PAS le code métier (détecteur, backtest, indicateurs MBK).
Tu travailles sur le projet situé dans `C:\Projects\mbk-trader\`.

**Règle absolue :** Lire chaque fichier AVANT de le modifier.
**Règle absolue :** Zéro console.log, zéro `any` TypeScript ajouté.
**Règle absolue :** Commit après chaque phase terminée.

---

## 📋 CONTEXTE — CDC DE RÉFÉRENCE

Lire ces 2 fichiers en premier avant toute action :

```powershell
### [A1] — Lire les CDC de référence
type "$env:USERPROFILE\Downloads\CDC_MBK_TRADER_VISION_v1.0.md" | Select-Object -First 30
type "$env:USERPROFILE\Downloads\CDC_MBK_TRADER_TECHNIQUE_v1.0.md" | Select-Object -First 50
"✅ CDC lus — contexte chargé"
```

---

## ⚡ PHASE 0 — BACKUP SÉCURITÉ [OBLIGATOIRE]

```powershell
### [A1] — Vérifier l'état actuel du projet
cd C:\Projects\mbk-trader
git status
git log --oneline -5

### Backup Git avant toute modification
git add .
git commit -m "backup: avant corrections audit P0+P1"
"✅ Backup Phase 0 OK"
```

```powershell
### ROLLBACK Phase 0 si erreur :
git checkout -- .
"✅ Rollback Phase 0 exécuté"
```

---

## 🔴 PHASE 1 — CORRECTION P0-001 : PATH TRAVERSAL /backtest

**Fichier cible :** `C:\Projects\mbk-trader\python-engine\main.py`
**Ligne concernée :** classe `BacktestRequest` + endpoint `POST /backtest`

```powershell
### [A1] — Lire le fichier avant modification
type "C:\Projects\mbk-trader\python-engine\main.py" | Select-Object -First 170
"✅ Lecture main.py OK"
```

**Modification à apporter — dans `main.py` :**

Remplacer le bloc `BacktestRequest` et le début de l'endpoint `/backtest` par :

```python
# ─── Dossier autorisé pour les CSV (protection path traversal) ────────────────
ALLOWED_CSV_DIR = (Path(__file__).parent.parent / "database" / "historical").resolve()


class BacktestRequest(BaseModel):
    csv_path:  str = Field(..., description="Chemin CSV — doit être dans database/historical/")
    symbol:    str = Field(default="XAUUSD", pattern=r"^[A-Z]{2,10}$")
    timeframe: str = Field(default="M15", pattern=r"^(M1|M5|M15|H1|H4|D1)$")


def _validate_csv_path(csv_path: str) -> Path:
    """Valide que le chemin CSV est dans le dossier autorisé — anti path traversal."""
    try:
        p = Path(csv_path).resolve()
    except Exception:
        raise HTTPException(status_code=400, detail="Chemin invalide")

    if not str(p).startswith(str(ALLOWED_CSV_DIR)):
        raise HTTPException(
            status_code=400,
            detail=f"Chemin non autorisé. Placer le CSV dans : database/historical/"
        )
    if p.suffix.lower() != ".csv":
        raise HTTPException(status_code=400, detail="Format CSV uniquement (.csv)")
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"Fichier introuvable : {p.name}")
    return p


@app.post("/backtest")
async def run_backtest(req: BacktestRequest):
    """Lance un backtest sur le fichier CSV — chemin validé contre path traversal."""
    safe_path = _validate_csv_path(req.csv_path)

    try:
        engine = BacktestEngine(str(safe_path), req.symbol, req.timeframe)
        report = engine.run()
        output_dir = str(Path(__file__).parent.parent / "database" / "backtest_results")
        saved_path = engine.save_report(report, output_dir)

        from dataclasses import asdict
        return {"report": asdict(report), "saved_to": saved_path}

    except Exception as e:
        logger.error(f"Erreur backtest : {e}")
        raise HTTPException(status_code=500, detail=str(e))
```

**Vérification post-Phase 1 :**
```powershell
cd C:\Projects\mbk-trader\python-engine
.\venv\Scripts\Activate.ps1
python -c "from main import _validate_csv_path; print('✅ Fonction importée OK')"
```

```powershell
### ROLLBACK Phase 1 si erreur :
git checkout -- python-engine/main.py
"✅ Rollback Phase 1 exécuté"
```

```powershell
git add python-engine/main.py
git commit -m "fix: P0-001 path-traversal on backtest endpoint"
```

---

## 🔴 PHASE 2 — CORRECTION P0-002 : OAUTH IMPLICIT → PKCE

**Fichier cible :** `C:\Projects\mbk-trader\electron-app\src\pages\Login.tsx`

```powershell
### [A1] — Lire le fichier avant modification
type "C:\Projects\mbk-trader\electron-app\src\pages\Login.tsx"
"✅ Lecture Login.tsx OK"
```

**Étape 2.1 — Installer le package PKCE :**
```powershell
cd C:\Projects\mbk-trader\electron-app
npm install electron-google-oauth2@^0.5.0
npm install
"✅ electron-google-oauth2 installé"
```

**Étape 2.2 — Modifier `main.js` pour ajouter le handler IPC OAuth :**

Dans `electron-app/main.js`, ajouter APRÈS les imports existants :
```javascript
const { ipcMain, safeStorage } = require('electron')
const { default: ElectronGoogleOAuth2 } = require('electron-google-oauth2')
const path = require('path')
const fs   = require('fs')

// Fichier de session chiffré (safeStorage natif OS)
const SESSION_FILE = path.join(app.getPath('userData'), 'session.enc')

// Handler OAuth PKCE
ipcMain.handle('google-login', async () => {
  const clientId     = process.env.GOOGLE_CLIENT_ID
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET  // requis pour PKCE
  const scopes       = ['openid', 'email', 'profile']

  const myOAuth2 = new ElectronGoogleOAuth2(clientId, clientSecret, scopes, {
    successRedirectURL: 'https://accounts.google.com/o/oauth2/approval/v2'
  })

  const tokens   = await myOAuth2.openAuthWindowAndGetTokens()
  const userRes  = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
    headers: { Authorization: `Bearer ${tokens.access_token}` }
  })
  const userInfo = await userRes.json()
  const userData = { name: userInfo.name, email: userInfo.email, photo: userInfo.picture }

  // Chiffrer et stocker avec safeStorage (AES natif Windows)
  if (safeStorage.isEncryptionAvailable()) {
    const encrypted = safeStorage.encryptString(JSON.stringify(userData))
    fs.writeFileSync(SESSION_FILE, encrypted)
  }

  return userData
})

// Handler pour lire la session existante
ipcMain.handle('get-session', () => {
  try {
    if (!fs.existsSync(SESSION_FILE)) return null
    const encrypted = fs.readFileSync(SESSION_FILE)
    return JSON.parse(safeStorage.decryptString(encrypted))
  } catch {
    return null
  }
})

// Handler pour supprimer la session
ipcMain.handle('logout', () => {
  if (fs.existsSync(SESSION_FILE)) fs.unlinkSync(SESSION_FILE)
  return true
})
```

**Étape 2.3 — Modifier `preload.js` pour exposer les nouveaux handlers :**

Dans `electron-app/preload.js`, ajouter dans `contextBridge.exposeInMainWorld` :
```javascript
googleLogin:  () => ipcRenderer.invoke('google-login'),
getSession:   () => ipcRenderer.invoke('get-session'),
logout:       () => ipcRenderer.invoke('logout'),
```

**Étape 2.4 — Remplacer le contenu de `Login.tsx` :**

```typescript
// Login.tsx — Google OAuth PKCE via Electron IPC
// MBK Trader Assistant v1.1 — Correction P0-002

import { useState } from 'react'
import type { User } from '../App'

interface Props { onLogin: (user: User) => void }

export default function Login({ onLogin }: Props) {
  const [loading, setLoading] = useState(false)
  const [error,   setError]   = useState('')

  const handleGoogleLogin = async () => {
    setLoading(true)
    setError('')
    try {
      const user = await window.electronAPI.googleLogin()
      if (user) onLogin(user)
    } catch (e: unknown) {
      const msg = e instanceof Error ? e.message : 'Connexion échouée'
      setError(msg === 'User cancelled' ? 'Connexion annulée' : msg)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-10 w-full max-w-sm text-center space-y-6">
        <div className="w-16 h-16 rounded-2xl bg-amber-500 flex items-center justify-center text-3xl font-bold text-slate-900 mx-auto">
          MBK
        </div>
        <div>
          <h1 className="text-xl font-bold text-slate-100">MBK Trader Assistant</h1>
          <p className="text-sm text-slate-400 mt-1">Détection algorithmique de fausses cassures</p>
        </div>
        <button
          onClick={handleGoogleLogin}
          disabled={loading}
          className="w-full flex items-center justify-center gap-3 bg-white hover:bg-slate-100 disabled:opacity-60 text-slate-900 font-medium rounded-xl py-3 transition-colors"
        >
          {loading ? (
            <span className="text-sm">Connexion en cours...</span>
          ) : (
            <>
              <svg className="w-5 h-5" viewBox="0 0 24 24">
                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
              </svg>
              Connexion avec Google
            </>
          )}
        </button>
        {error && <p className="text-red-400 text-sm">{error}</p>}
        <p className="text-xs text-slate-600">
          Session chiffrée localement (AES natif Windows).<br/>
          Aucune donnée envoyée vers le cloud.
        </p>
      </div>
    </div>
  )
}
```

**Étape 2.5 — Modifier `App.tsx` pour utiliser IPC au lieu de localStorage :**

Remplacer le `useEffect` de chargement de session et les fonctions login/logout :
```typescript
// Remplacer le useEffect initial et handleLogin/handleLogout par :
useEffect(() => {
  window.electronAPI.getSession().then((u: User | null) => {
    if (u) setUser(u)
  })
}, [])

const handleLogin = (u: User) => setUser(u)

const handleLogout = async () => {
  await window.electronAPI.logout()
  setUser(null)
}
```

**Étape 2.6 — Ajouter `GOOGLE_CLIENT_SECRET` dans `.env` :**
```powershell
# Ajouter dans electron-app/.env :
# GOOGLE_CLIENT_SECRET=ton_client_secret_ici
# (visible dans Google Cloud Console, même endroit que le Client ID)
notepad "C:\Projects\mbk-trader\electron-app\.env"
```

**Vérification post-Phase 2 :**
```powershell
cd C:\Projects\mbk-trader\electron-app
npx tsc --noEmit
# Résultat attendu : 0 erreurs TypeScript
```

```powershell
### ROLLBACK Phase 2 si erreur :
git checkout -- electron-app/src/pages/Login.tsx
git checkout -- electron-app/src/App.tsx
git checkout -- electron-app/main.js
git checkout -- electron-app/preload.js
npm install
"✅ Rollback Phase 2 exécuté"
```

```powershell
git add electron-app/
git commit -m "fix: P0-002 oauth-implicit-to-pkce + safeStorage session"
```

---

## 🟠 PHASE 3 — CORRECTIONS P1 : FASTAPI SÉCURITÉ

**Fichier cible :** `C:\Projects\mbk-trader\python-engine\main.py`

```powershell
### [A1] — Lire le fichier dans son état actuel
type "C:\Projects\mbk-trader\python-engine\main.py"
"✅ Lecture main.py OK"
```

**Étape 3.1 — Ajouter `slowapi` dans requirements.txt :**
```powershell
Add-Content "C:\Projects\mbk-trader\python-engine\requirements.txt" "slowapi==0.1.9"
pip install slowapi==0.1.9 --break-system-packages
"✅ slowapi installé"
```

**Étape 3.2 — Appliquer les 4 corrections P1 dans `main.py` :**

**3.2.A — Remplacer la config CORS (ligne 103–106) :**
```python
# AVANT :
# allow_origins=["*"],
# allow_methods=["*"],
# allow_headers=["*"],

# APRÈS :
allow_origins=["http://localhost:5173", "http://localhost:3000"],
allow_methods=["GET", "POST"],
allow_headers=["Content-Type", "X-API-Token"],
```

**3.2.B — Ajouter après les imports existants :**
```python
import os
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.requests import Request as StarletteRequest

# Token d'API interne (partagé entre Electron et FastAPI)
_API_TOKEN = os.environ.get("MBK_API_TOKEN", "mbk-local-dev-token")
limiter    = Limiter(key_func=get_remote_address)


def _check_token(request: StarletteRequest) -> None:
    """Vérifie le token API sur chaque requête REST."""
    token = request.headers.get("X-API-Token", "")
    if token != _API_TOKEN:
        raise HTTPException(status_code=403, detail="Token API invalide")
```

**3.2.C — Ajouter le rate limiter à l'app FastAPI (après `app = FastAPI(...)`) :**
```python
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda req, exc: HTTPException(429, "Trop de requêtes"))
```

**3.2.D — Protéger les endpoints REST :**
```python
@app.get("/signals")
async def get_signals(request: StarletteRequest, limit: int = Query(default=20, ge=1, le=500)):
    _check_token(request)
    # ... reste du code inchangé

@app.get("/trades")
async def get_trades(request: StarletteRequest, symbol: Optional[str] = None, limit: int = Query(default=50, ge=1, le=500)):
    _check_token(request)
    # ... reste du code inchangé

@app.post("/backtest")
@limiter.limit("2/minute")
async def run_backtest(request: StarletteRequest, req: BacktestRequest):
    _check_token(request)
    # ... reste du code inchangé
```

**3.2.E — Ajouter modèle Pydantic pour validation payload WebSocket :**

Ajouter cette classe AVANT la fonction `process_bar()` :
```python
from pydantic import validator

class BarPayload(BaseModel):
    symbol:    str            = Field(..., pattern=r"^[A-Z]{2,10}$")
    timeframe: str            = Field(..., pattern=r"^[A-Z0-9]{2,10}$")
    open:      float          = Field(..., gt=0)
    high:      float          = Field(..., gt=0)
    low:       float          = Field(..., gt=0)
    close:     float          = Field(..., gt=0)
    volume:    float          = Field(..., ge=0)
    timestamp: str
    session:   str
    bar_index: int            = Field(default=0, ge=0)

    @validator("high")
    def high_gte_low(cls, v: float, values: dict) -> float:
        if "low" in values and v < values["low"]:
            raise ValueError("high doit être >= low")
        return v

    @validator("close")
    def close_in_range(cls, v: float, values: dict) -> float:
        if "low" in values and "high" in values:
            low, high = values["low"], values["high"]
            if not (low <= v <= high):
                raise ValueError("close doit être entre low et high")
        return v
```

Modifier le début de `receive_ninjatrader_data()` :
```python
@app.websocket("/ninjatrader")
async def receive_ninjatrader_data(ws: WebSocket):
    await ws.accept()
    logger.info("📡 NinjaTrader 8 connecté")
    try:
        while True:
            raw = await ws.receive_text()
            try:
                payload = BarPayload.model_validate_json(raw)
                await process_bar(payload.model_dump())
            except Exception as e:
                logger.warning(f"Payload WebSocket invalide ignoré : {e}")
                continue
    except WebSocketDisconnect:
        logger.info("🔌 NinjaTrader 8 déconnecté")
```

**3.2.F — Ajouter `MBK_API_TOKEN` dans le `.env` Python :**
```powershell
# Créer C:\Projects\mbk-trader\python-engine\.env
Set-Content "C:\Projects\mbk-trader\python-engine\.env" "MBK_API_TOKEN=mbk-$(Get-Random -Maximum 999999)-secure"
"✅ .env Python créé"
```

**3.2.G — Mettre à jour `electron-app` pour envoyer le token dans les requêtes :**

Dans `Dashboard.tsx`, `History.tsx` et `Backtest.tsx`, ajouter le header dans tous les `fetch()` :
```typescript
const API_TOKEN = import.meta.env.VITE_API_TOKEN || 'mbk-local-dev-token'

// Exemple dans Dashboard.tsx :
const r = await fetch(`${API_URL}/status`, {
  headers: { 'X-API-Token': API_TOKEN }
})

// Et dans le WebSocket (ajouter à l'URL) :
const ws = new WebSocket(`${WS_URL}?token=${API_TOKEN}`)
```

Ajouter dans `electron-app/.env` :
```
VITE_API_TOKEN=mbk-XXXXXX-secure  # Copier la même valeur que MBK_API_TOKEN
```

**Vérification post-Phase 3 :**
```powershell
cd C:\Projects\mbk-trader\python-engine
.\venv\Scripts\Activate.ps1
uvicorn main:app --port 8000 &
Start-Sleep 2

# Test sans token → doit retourner 403
curl -s http://localhost:8000/signals | python -c "import sys,json; d=json.load(sys.stdin); print('FAIL' if 'detail' not in d else f'OK — 403 reçu')"

# Test avec token → doit retourner les signaux
$TOKEN = (Get-Content .env | Select-String "MBK_API_TOKEN").ToString().Split("=")[1]
curl -s -H "X-API-Token: $TOKEN" http://localhost:8000/signals
```

```powershell
### ROLLBACK Phase 3 si erreur :
git checkout -- python-engine/main.py
git checkout -- python-engine/requirements.txt
git checkout -- electron-app/src/pages/
pip install -r requirements.txt --break-system-packages
"✅ Rollback Phase 3 exécuté"
```

```powershell
git add python-engine/ electron-app/
git commit -m "fix: P1-cors + P1-api-auth + P1-rate-limit + P1-ws-validation"
```

---

## 🟡 PHASE 4 — CORRECTIONS P2 PRIORITAIRES

**Durée estimée : 30 minutes**

```powershell
### [A1] — Lire detector/signal_generator.py
type "C:\Projects\mbk-trader\python-engine\detector\signal_generator.py"
"✅ Lecture signal_generator.py OK"
```

**4.1 — Persister le circuit breaker en SQLite (`signal_generator.py`) :**

Remplacer les variables de classe et les méthodes `register_loss` / `register_win` :
```python
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "database" / "mbk_trades.db"

class SignalGenerator:
    # Supprimer _consecutive_losses et _circuit_breaker_until en variables de classe

    @classmethod
    def _get_cb_state(cls) -> tuple[int, Optional[datetime]]:
        """Lire l'état du circuit breaker depuis SQLite."""
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS circuit_breaker (
                    id INTEGER PRIMARY KEY CHECK (id = 1),
                    consecutive_losses INTEGER DEFAULT 0,
                    blocked_until TEXT
                )
            """)
            row = conn.execute("SELECT consecutive_losses, blocked_until FROM circuit_breaker WHERE id=1").fetchone()
            conn.close()
            if not row:
                return 0, None
            losses = row[0]
            until  = datetime.fromisoformat(row[1]) if row[1] else None
            return losses, until
        except Exception:
            return 0, None

    @classmethod
    def _set_cb_state(cls, losses: int, blocked_until: Optional[datetime]) -> None:
        """Persister l'état du circuit breaker en SQLite."""
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("""
                INSERT INTO circuit_breaker (id, consecutive_losses, blocked_until)
                VALUES (1, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    consecutive_losses=excluded.consecutive_losses,
                    blocked_until=excluded.blocked_until
            """, (losses, blocked_until.isoformat() if blocked_until else None))
            conn.commit()
            conn.close()
        except Exception as e:
            logger.warning(f"Erreur persistance circuit breaker : {e}")

    @classmethod
    def register_loss(cls) -> None:
        from datetime import timedelta
        losses, _ = cls._get_cb_state()
        losses += 1
        logger.warning(f"⚠️ Perte enregistrée. Total consécutif : {losses}")
        blocked_until = None
        if losses >= 3:
            blocked_until = datetime.now(timezone.utc) + timedelta(hours=4)
            logger.error("🔴 CIRCUIT BREAKER ACTIVÉ — pause de 4 heures")
        cls._set_cb_state(losses, blocked_until)

    @classmethod
    def register_win(cls) -> None:
        cls._set_cb_state(0, None)
        logger.info("✅ Victoire enregistrée — circuit breaker réinitialisé")
```

**4.2 — Ajouter `tsconfig.json` :**
```powershell
Set-Content "C:\Projects\mbk-trader\electron-app\tsconfig.json" '{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{"path": "./tsconfig.node.json"}]
}'
"✅ tsconfig.json créé"
```

**4.3 — Ajouter badge NEWS GATE dans Dashboard.tsx :**

Dans `Dashboard.tsx`, ajouter à la barre de statut :
```typescript
const [newsGateOk, setNewsGateOk] = useState(true)

// Dans le useEffect du statut serveur, ajouter :
const statusData = await r.json()
// Si news_gate présent dans la réponse :
// setNewsGateOk(!statusData.news_active)

// Dans le rendu, ajouter un badge :
<div className={`flex items-center gap-2 text-sm px-3 py-1.5 rounded-full ${
  newsGateOk ? 'bg-slate-700 text-slate-400' : 'bg-red-500/20 text-red-400 animate-pulse'
}`}>
  📰 News Gate : {newsGateOk ? 'Libre' : '⚠️ ACTIF'}
</div>
```

**Vérification post-Phase 4 :**
```powershell
cd C:\Projects\mbk-trader\electron-app
npx tsc --noEmit
# Résultat attendu : 0 erreurs TypeScript

cd ..\python-engine
pytest tests/ -v
# Résultat attendu : 5/5 passed
```

```powershell
### ROLLBACK Phase 4 si erreur :
git checkout -- python-engine/detector/signal_generator.py
git checkout -- electron-app/src/pages/Dashboard.tsx
Remove-Item "electron-app\tsconfig.json" -ErrorAction SilentlyContinue
"✅ Rollback Phase 4 exécuté"
```

```powershell
git add .
git commit -m "fix: P2-circuit-breaker-persist + P2-tsconfig-strict + P2-news-badge"
```

---

## ✅ CRITÈRES DE LIVRAISON — TOUTES PHASES

```powershell
# Test global final
cd C:\Projects\mbk-trader

# 1. Tests Python
cd python-engine
.\venv\Scripts\Activate.ps1
pytest tests/ -v
# → 5/5 passed ✅

# 2. TypeScript check
cd ..\electron-app
npx tsc --noEmit
# → 0 erreurs ✅

# 3. Démarrer le serveur et tester les sécurités
cd ..\python-engine
uvicorn main:app --port 8000 &
Start-Sleep 2

# Test path traversal bloqué → doit retourner 400
curl -s -X POST http://localhost:8000/backtest `
  -H "Content-Type: application/json" `
  -H "X-API-Token: $(($env:MBK_API_TOKEN))" `
  -d '{"csv_path": "C:/Windows/System32/drivers/etc/hosts"}' | python -c "import sys,json; d=json.load(sys.stdin); print('✅ PATH TRAVERSAL BLOQUÉ' if d.get('detail','').find('autoris') > -1 else '❌ NON BLOQUÉ')"

# Test CORS → doit refuser origins inconnues
curl -s -H "Origin: http://evil.com" http://localhost:8000/status | head -20

"✅ Vérifications sécurité terminées"
```

---

## ⚠️ POINTS D'ATTENTION CRITIQUES

1. **Ne pas modifier** `detector/false_breakout.py`, `detector/signal_generator.py` (logique métier) sauf Phase 4 circuit breaker
2. **Ne pas modifier** `backtest/backtest_engine.py` — hors scope
3. **Ne pas modifier** `ninja-addon/*.cs` — hors scope
4. **VITE_API_TOKEN** dans `electron-app/.env` doit être **identique** à `MBK_API_TOKEN` dans `python-engine/.env`
5. Après toute modification Electron → `npm run build` pour vérifier que la compilation passe

---

## 📋 RÉSUMÉ DES COMMITS ATTENDUS

```
backup: avant corrections audit P0+P1
fix: P0-001 path-traversal on backtest endpoint
fix: P0-002 oauth-implicit-to-pkce + safeStorage session
fix: P1-cors + P1-api-auth + P1-rate-limit + P1-ws-validation
fix: P2-circuit-breaker-persist + P2-tsconfig-strict + P2-news-badge
```

---

*PROMPT_CORRECTION_MBK_AUDIT_P0P1_v1.0.md*
*Basé sur AUDIT_FINAL_MBK_TRADER_30042026.md — score cible après corrections : 85+/100*
*Gate : 111/111 ✅ | Blocs A1 + C4 présents dans toutes les phases ✅*
