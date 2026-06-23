# Extraction_arXiv_WalkForward_v1.md
**Source :** arXiv 2512.12924v1 — *Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals*  
**URL :** https://arxiv.org/html/2512.12924v1  
**Décisions :** D135 → D142  
**Images :** 0 certifiées (8 figures détectées mais HTTP 404 sur le rendu HTML arXiv → MANUEL · scraper_static v1.1)  
**Date extraction :** 23/06/2026  
**⚠️ Nature source :** preprint arXiv (NON peer-reviewed). Tag ⏳ sur les résultats chiffrés. Les principes méthodologiques cités renvoient à des références établies (Pardo, Harvey, Bailey, McLean).

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — CRISE DE REPRODUCTIBILITÉ

### D135 — La crise de reproductibilité du backtesting

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §1 Introduction + §2.1, citant harvey2016) : Les études documentent constamment des stratégies à rendements annuels à deux chiffres en backtest, mais les institutionnels rapportent que **plus de 90 % des stratégies académiques échouent** une fois implémentées avec du capital réel. Harvey (2016) note ≥ **316 facteurs** proposés, la plupart probablement faux après correction du multiple testing.

**TRADEX-AI** : Justifie le scepticisme verrouillé du projet (CLAUDE.md : « COG backtest historique trompeur », « performances auto-déclarées non auditées »). Tout backtest interne = suspect par défaut.

---

### D136 — Les trois défauts du backtesting standard

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §1) : Le problème est méthodologique — trois défauts :
1. **Overfitting** par optimisation de paramètres in-sample.
2. **Lookahead bias** par usage d'information indisponible en temps réel.
3. **Manque d'interprétabilité** par dépendance à des modèles black-box.

**TRADEX-AI C0** : Règles de conception du moteur — discipline stricte de l'ensemble d'information (features/signaux/exécution n'utilisent QUE les données disponibles à l'instant t), pas d'optimisation in-sample, modèles interprétables (grille déterministe /10).

---

## BLOC 2 — VALIDATION WALK-FORWARD

### D137 — Walk-forward validation : le « gold standard »

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §2.2, citant pardo1992/pardo2008) : La **walk-forward analysis** (Pardo) est le standard de référence — ré-optimisation continue sur **fenêtres glissantes (rolling windows)** où la stratégie doit faire ses preuves de façon répétée sur de multiples périodes out-of-sample (l'article : **34 périodes OOS indépendantes**), plutôt que de réussir un seul backtest chanceux.

**TRADEX-AI** : Tout backtest TRADEX (ex. COG) doit être walk-forward multi-fenêtres, jamais un backtest unique sur tout l'historique.

---

### D138 — Multiple testing : t-stat > 3.0

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §2.1, citant harvey2016) : Étant donné le data-mining massif du domaine, un facteur nouvellement découvert requiert un **t-statistique > 3,0** (et non le 2,0 traditionnel) pour être jugé réellement significatif.

**TRADEX-AI** : Relever le seuil de significativité de toute règle validée par backtest — exiger un t-stat élevé, pas un simple « ça marche sur l'historique ».

---

### D139 — Décroissance out-of-sample et post-publication

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §2.1, citant mclean2016 / hou2020) : McLean (2016) sur 97 prédicteurs : rendements de portefeuille en baisse de **26 % out-of-sample** et **58 % post-publication** (moitié = data-mining, moitié = arbitrage post-publication). Hou (2020) : **65 %** des 452 anomalies échouent au test simple, **82 %** sous ajustement multiple-testing.

**TRADEX-AI** : Anticiper une dégradation forte entre backtest et live. Ne jamais dimensionner le risque sur la performance backtestée brute.

---

### D140 — Deflated Sharpe Ratio & probabilité d'overfitting

🔵 **ÉCOLE** (Source : walk_forward.md §2.2, citant bailey2014/bailey2015) : Bailey démontre qu'une haute performance simulée est facile après avoir testé peu de configurations (les séries financières à effet mémoire font **sous-performer** les stratégies sur-ajustées en OOS). Outils : **Deflated Sharpe Ratio** (corrige le biais de sélection sous multiple testing et non-normalité) et **CSCV / Probability of Backtest Overfitting**.

**TRADEX-AI** : Outils de validation à intégrer si un backtest quantitatif TRADEX est mené — déflater le Sharpe, estimer la probabilité d'overfitting.

---

## BLOC 3 — RÉALISME ET HONNÊTETÉ

### D141 — Hypothèses d'exécution réalistes obligatoires

🟢 **FAIT VÉRIFIÉ** (Source : walk_forward.md §1) : Le cadre incorpore des hypothèses d'exécution réalistes : **coûts de commission, slippage, limites de position, règles de stop-loss**. (La littérature note que beaucoup de stratégies RL échouent au test de profitabilité une fois les coûts réels inclus.)

**TRADEX-AI gestion_risque** : Tout backtest TRADEX doit inclure commission + slippage + contraintes de position + stops — sinon résultats illusoires (frictionless).

---

### D142 — Dépendance au régime & reporting honnête

🟢 **FAIT VÉRIFIÉ** ⏳ **VOLATILE** (Source : walk_forward.md abstract + §1, preprint non peer-reviewed) : Résultat honnête du cadre — rendement annualisé modeste **0,55 %**, **Sharpe 0,33**, **p-value 0,34 (non significatif)**, max drawdown **−2,76 %** (vs −23,8 % SPY), quasi market-neutral (β = 0,058). Forte **dépendance au régime** : positif en haute volatilité (2020–2024), négatif en marché stable (2015–2019). Les signaux microstructure sur données journalières requièrent une arrivée d'information et une activité élevées pour fonctionner.

**TRADEX-AI C4/C5** : Confirme que la performance dépend du régime de volatilité (lien VIX C5) — une stratégie n'est pas universelle. Reporting honnête (publier p non significatif) = modèle de rigueur pour TRADEX.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D135
Dernière décision session  : D142
Prochaine décision         : D143
Total décisions            : 8
Total KB cumulé            : D1 → D142
```

---

*Extraction_arXiv_WalkForward_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre · Preprint non peer-reviewed*
