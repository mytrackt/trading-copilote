import { useEffect, useState } from 'react'
import { fetchMode, fetchHistory } from './api.js'

// ------------------------------------------------------------------
// Signal d'exemple (forme identique a la reponse de l'API /signal).
// Utilise uniquement pour l'affichage quand l'API locale n'est pas lancee.
// ------------------------------------------------------------------
const SAMPLE_SIGNAL = {
  actif: 'GC',
  sens: 'ACHAT',
  decision: 'SIGNAL',
  score: 8.5,
  score_max: 10,
  rr: 2.5,
  validation_humaine_requise: true,
  mode_auto_autorise: false,
  banniere: 'KB provisoire — transcription Whisper non terminee',
  breakdown: {
    prix_bande_2_3: 2.0,
    timing_ok: 2.0,
    bandes_resserrees: 1.0,
    biais_h4_aligne: 1.5,
    volume_ok: 1.0,
    atr_normal: 0.0,
    structure_non_cassee: 0.5,
    confirmation_favorable: 1.0,
    news_clean: 0.5,
  },
}

const BREAKDOWN_LABELS = {
  prix_bande_2_3: 'Prix en bande 2/3 (R2)',
  timing_ok: 'Timing dans la zone (R3)',
  bandes_resserrees: 'Bandes resserrées (R4)',
  biais_h4_aligne: 'Biais H4 aligné',
  volume_ok: 'Volume ≥ 1,2× moy20',
  atr_normal: 'ATR normal (pas de choc)',
  structure_non_cassee: 'Structure non cassée',
  confirmation_favorable: 'Confirmation DX/ES/VX',
  news_clean: 'Aucune news ±30/15 min',
}

const DECISION_STYLE = {
  SIGNAL: 'bg-brand-light text-brand-dark',
  SURVEILLER: 'bg-amber-100 text-amber-700',
  IGNORER: 'bg-slate-100 text-slate-500',
  NON_TRADE: 'bg-rose-100 text-rose-700',
}

function Card({ title, subtitle, children, className = '' }) {
  return (
    <div className={`rounded-2xl bg-white p-5 shadow-card ${className}`}>
      {title && (
        <div className="mb-3">
          <h3 className="text-sm font-semibold text-slate-800">{title}</h3>
          {subtitle && <p className="text-xs text-slate-400">{subtitle}</p>}
        </div>
      )}
      {children}
    </div>
  )
}

function ModeBadge() {
  // Le mode Auto est VERROUILLE : badge fige "BLOQUE", aucun moyen de l'activer depuis l'UI.
  return (
    <div className="flex items-center gap-2 rounded-full bg-rose-50 px-3 py-1.5 text-xs font-semibold text-rose-700 ring-1 ring-rose-200">
      <span className="h-2 w-2 rounded-full bg-rose-500" />
      Mode Auto : BLOQUÉ
    </div>
  )
}

function ScoreGauge({ score, max }) {
  const pct = Math.max(0, Math.min(100, (score / max) * 100))
  return (
    <div>
      <div className="flex items-baseline gap-1">
        <span className="text-4xl font-bold text-slate-900">{score.toFixed(1)}</span>
        <span className="text-lg text-slate-400">/ {max}</span>
      </div>
      <div className="mt-2 h-2 w-full rounded-full bg-slate-100">
        <div className="h-2 rounded-full bg-brand" style={{ width: `${pct}%` }} />
      </div>
      <p className="mt-1 text-xs text-slate-400">Seuil signal ≥ 7,0 · validation humaine obligatoire</p>
    </div>
  )
}

function Breakdown({ breakdown }) {
  return (
    <ul className="space-y-1.5">
      {Object.entries(breakdown).map(([key, pts]) => (
        <li key={key} className="flex items-center justify-between text-sm">
          <span className="flex items-center gap-2 text-slate-600">
            <span className={`h-1.5 w-1.5 rounded-full ${pts > 0 ? 'bg-brand' : 'bg-slate-300'}`} />
            {BREAKDOWN_LABELS[key] || key}
          </span>
          <span className={pts > 0 ? 'font-medium text-slate-800' : 'text-slate-400'}>
            {pts.toFixed(1)} pt
          </span>
        </li>
      ))}
    </ul>
  )
}

function SignalCard({ signal }) {
  const style = DECISION_STYLE[signal.decision] || DECISION_STYLE.NON_TRADE
  return (
    <Card title="Dernier signal" subtitle={`${signal.actif} · ${signal.sens} · R/R ${signal.rr}`}>
      <div className="mb-4 flex items-center justify-between">
        <span className={`rounded-full px-3 py-1 text-xs font-semibold ${style}`}>
          {signal.decision}
        </span>
        {signal.validation_humaine_requise && (
          <span className="rounded-full bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700 ring-1 ring-blue-200">
            Validation humaine requise
          </span>
        )}
      </div>

      <ScoreGauge score={signal.score} max={signal.score_max || 10} />

      <div className="mt-5 border-t border-slate-100 pt-4">
        <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-400">
          Détail du score (/10)
        </p>
        <Breakdown breakdown={signal.breakdown} />
      </div>

      <div className="mt-4 rounded-xl bg-slate-50 px-4 py-3 text-xs text-slate-500">
        Aucune exécution d'ordre depuis l'interface. En mode Manuel, la décision finale
        appartient à Abdelkrim.
      </div>
    </Card>
  )
}

function AutoPanel() {
  const raisons = [
    'Mode Auto verrouillé par défaut (décision projet).',
    'KB provisoire — transcription Whisper non terminée.',
    'Circuit breaker / staleness / news gate non encore validés en production.',
  ]
  return (
    <Card title="Mode Automatique" subtitle="Exécution automatique d'ordres">
      <div className="flex flex-col items-center gap-3 py-6">
        <div className="flex items-center gap-2 rounded-full bg-rose-50 px-4 py-2 text-sm font-bold text-rose-700 ring-1 ring-rose-200">
          <span className="h-2.5 w-2.5 rounded-full bg-rose-500" />
          BLOQUÉ
        </div>
        {/* Interrupteur volontairement desactive : impossible d'activer l'Auto depuis l'UI. */}
        <div
          className="flex h-7 w-12 cursor-not-allowed items-center rounded-full bg-slate-200 px-1 opacity-60"
          title="Activation impossible depuis l'interface"
          aria-disabled="true"
        >
          <span className="h-5 w-5 rounded-full bg-white shadow" />
        </div>
        <p className="text-xs text-slate-400">Non activable depuis l'interface</p>
      </div>
      <ul className="space-y-2 border-t border-slate-100 pt-4 text-sm text-slate-600">
        {raisons.map((r) => (
          <li key={r} className="flex gap-2">
            <span className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-rose-400" />
            {r}
          </li>
        ))}
      </ul>
    </Card>
  )
}

function HistoryTable({ rows }) {
  if (!rows.length) {
    return (
      <Card title="Historique des signaux">
        <p className="py-6 text-center text-sm text-slate-400">
          Aucun historique (API locale non connectée).
        </p>
      </Card>
    )
  }
  return (
    <Card title="Historique des signaux">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wide text-slate-400">
            <th className="pb-2 font-medium">Horodatage</th>
            <th className="pb-2 font-medium">Actif</th>
            <th className="pb-2 font-medium">Décision</th>
            <th className="pb-2 text-right font-medium">Score</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id} className="border-t border-slate-100">
              <td className="py-2 text-slate-500">{r.ts}</td>
              <td className="py-2 text-slate-700">{r.actif || '—'}</td>
              <td className="py-2">
                <span className={`rounded-full px-2 py-0.5 text-xs font-medium ${DECISION_STYLE[r.decision] || DECISION_STYLE.NON_TRADE}`}>
                  {r.decision}
                </span>
              </td>
              <td className="py-2 text-right font-medium text-slate-800">
                {r.score != null ? Number(r.score).toFixed(1) : '—'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
  )
}

function Sidebar({ screen, setScreen }) {
  const items = [
    { id: 'MANUEL', label: 'Manuel' },
    { id: 'AUTO', label: 'Auto' },
  ]
  return (
    <aside className="flex w-48 shrink-0 flex-col gap-2 rounded-2xl bg-white p-4 shadow-card">
      <div className="mb-4 flex items-center gap-2 px-1">
        <div className="grid h-8 w-8 place-items-center rounded-lg bg-brand text-sm font-bold text-white">
          TX
        </div>
        <span className="font-semibold text-slate-800">TRADEX-AI</span>
      </div>
      {items.map((it) => (
        <button
          key={it.id}
          onClick={() => setScreen(it.id)}
          className={`rounded-xl px-3 py-2 text-left text-sm font-medium transition ${
            screen === it.id
              ? 'bg-brand text-white'
              : 'text-slate-500 hover:bg-slate-50'
          }`}
        >
          {it.label}
        </button>
      ))}
      <div className="mt-auto px-1 pt-4 text-[11px] leading-snug text-slate-400">
        Backend local 127.0.0.1 · usage privé
      </div>
    </aside>
  )
}

function DisclaimerBar() {
  // Disclaimer legal VISIBLE EN PERMANENCE (sticky bas d'ecran).
  return (
    <div className="sticky bottom-0 z-10 border-t border-amber-200 bg-amber-50 px-6 py-3 text-center text-xs text-amber-800">
      ⚠️ Outil d'aide à la décision à usage strictement privé — aucun conseil en investissement.
      Le trading comporte un risque de perte en capital. Les performances passées ne préjugent pas
      des performances futures. La décision finale appartient toujours au trader.
    </div>
  )
}

export default function App() {
  const [screen, setScreen] = useState('MANUEL')
  const [history, setHistory] = useState([])
  const [apiOnline, setApiOnline] = useState(false)
  const signal = SAMPLE_SIGNAL // affichage ; remplace par la reponse /signal quand l'API tourne

  useEffect(() => {
    let cancelled = false
    Promise.all([fetchMode(), fetchHistory(20)])
      .then(([, hist]) => {
        if (cancelled) return
        setHistory(hist.history || [])
        setApiOnline(true)
      })
      .catch(() => !cancelled && setApiOnline(false))
    return () => {
      cancelled = true
    }
  }, [])

  return (
    <div className="flex min-h-full flex-col bg-slate-100">
      <div className="flex flex-1 gap-5 p-5">
        <Sidebar screen={screen} setScreen={setScreen} />

        <main className="flex-1">
          {/* Header */}
          <header className="mb-5 flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-slate-900">
                Tableau de bord — {screen === 'MANUEL' ? 'Manuel' : 'Auto'}
              </h1>
              <p className="text-sm text-slate-400">
                Méthode Belkhayate · {apiOnline ? 'API locale connectée' : 'API locale hors ligne (affichage exemple)'}
              </p>
            </div>
            <ModeBadge />
          </header>

          {screen === 'MANUEL' ? (
            <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
              <SignalCard signal={signal} />
              <HistoryTable rows={history} />
            </div>
          ) : (
            <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
              <AutoPanel />
              <SignalCard signal={signal} />
            </div>
          )}
        </main>
      </div>

      <DisclaimerBar />
    </div>
  )
}
