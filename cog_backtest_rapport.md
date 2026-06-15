# COG BACKTEST HOSTILE — TRADEX-AI
Date : 2026-06-15 15:37
Parametres testes : Belkhayate (180/3) vs 3 alternatives (100/3, 125/2, 250/3)
Donnees : yfinance 5y journalier | reversion window = 10 bougies

## Verdict global
| Asset | Verdict | Taux reversion 0.618 | R2 moyen | Meilleurs params |
|---|---|---|---|---|
| GC | ⚠️ A_REVISER | 50.3% | 0.811 | 100/3 (57.9%) |
| HG | ❌ REJETE | 42.5% | 0.608 | 100/3 (54.3%) |
| ZW | ❌ REJETE | 32.9% | 0.492 | 100/3 (57.4%) |

## Analyse par asset

### GC (GC=F)
| Params | nb signaux | rev 0.618 | rev 1.618 | R2 moyen | verdict |
|---|---|---|---|---|---|
| 180/3 **(Belkhayate)** | 741 | 50.3% | 55.7% | 0.811 | A_REVISER |
| 100/3 | 770 | 57.9% | 61.4% | 0.747 | CONFIRME |
| 125/2 | 758 | 49.9% | 55.1% | 0.712 | A_REVISER |
| 250/3 | 683 | 51.1% | 57.8% | 0.829 | A_REVISER |

### HG (HG=F)
| Params | nb signaux | rev 0.618 | rev 1.618 | R2 moyen | verdict |
|---|---|---|---|---|---|
| 180/3 **(Belkhayate)** | 713 | 42.5% | 48.1% | 0.608 | REJETE |
| 100/3 | 799 | 54.3% | 65.2% | 0.64 | A_REVISER |
| 125/2 | 746 | 39.4% | 56.5% | 0.525 | REJETE |
| 250/3 | 630 | 39.4% | 50.0% | 0.639 | REJETE |

### ZW (ZW=F)
| Params | nb signaux | rev 0.618 | rev 1.618 | R2 moyen | verdict |
|---|---|---|---|---|---|
| 180/3 **(Belkhayate)** | 751 | 32.9% | 57.0% | 0.492 | REJETE |
| 100/3 | 766 | 57.4% | 70.9% | 0.656 | CONFIRME |
| 125/2 | 820 | 39.9% | 46.3% | 0.456 | REJETE |
| 250/3 | 561 | 41.2% | 58.2% | 0.486 | REJETE |

## Decision recommandee
- **GC** : A REVISER (reversion 50.3% ; tester 100/3 (57.9%)).
- **HG** : REJETE sur daily (reversion 42.5%, n=713, R2 0.608). Ne pas s'appuyer sur ces parametres en daily.
- **ZW** : REJETE sur daily (reversion 32.9%, n=751, R2 0.492). Ne pas s'appuyer sur ces parametres en daily.

**Conclusion** : 180/3 NON confirme en daily sur aucun actif. Le backtest daily ne valide PAS la formule ; la validation Belkhayate porte sur range bars (CL) — re-tester sur le bon timeframe avant tout usage reel.

## ⚠️ Limites de ce backtest
- Donnees journalieres (NT8 utilise des range bars 5 ticks) : biais possible.
- Aucun slippage ni spread modelise.
- Belkhayate a valide CL (petrole) sur range bars : comparaison imparfaite sur daily.
- Test de reversion 'retour dans la bande sous 10 bougies' = permissif (mean-reversion triviale).
- Ce backtest evalue la FORMULE COG, PAS le TIMING d'execution ni la rentabilite reelle.
