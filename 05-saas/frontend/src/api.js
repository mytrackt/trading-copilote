// Le dashboard ne parle QU'A l'API locale (127.0.0.1). Aucune autre origine.
export const API_BASE = 'http://127.0.0.1:8000'

async function getJson(path) {
  const res = await fetch(`${API_BASE}${path}`)
  if (!res.ok) throw new Error(`HTTP ${res.status}`)
  return res.json()
}

export const fetchMode = () => getJson('/mode')
export const fetchHistory = (limit = 20) => getJson(`/history?limit=${limit}`)
export const fetchHealth = () => getJson('/health')

// L'UI n'envoie AUCUN ordre d'execution. Aucune fonction d'execution n'est exposee ici.
