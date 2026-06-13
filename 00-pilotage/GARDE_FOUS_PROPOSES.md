# GARDE-FOUS PROPOSÉS — TradEx AI

## DISCLAIMERS RÉGLEMENTAIRES (obligatoires)
- Usage strictement privé — pas de conseil en investissement, pas de distribution à des tiers.
- Les performances passées ne préjugent pas des performances futures.
- Ce système est un outil d'aide à la décision. La décision finale appartient toujours au trader.

---

> Document de proposition uniquement — **aucune ligne de code modifiée** dans cette phase.
> Source : audit `code/config/settings.py` + `code/engine/risk_manager.py`
> + `code/engine/correlations.py` + `code/utils/atomic_writer.py`
> + `docs/APPORTS_GUIDE_EXTERNE.md` + `docs/MASTER_TRADEX_AI_v2.md`
> + prompt `PROMPT_TRADEX_AI_CLAUDE_CODE_v4.md` (points d'attention critiques).
>
> **Date** : 2026-05-03 — Phase 4-Light v4.0.

---

## ✅ DÉFINIS DANS LE CODE (opérabilité NON validée — voir DETTE_TECHNIQUE.md) (20 garde-fous actifs)

⚠️ Note audit 13/06/2026 : aucun de ces modules n'est prouvé opérationnel. Validation prévue Phase C-G.

> Ces 20 garde-fous sont définis dans le code. Opérabilité NON validée — voir DETTE_TECHNIQUE.md.
> Les 2 premiers ont été harmonisés cette session (commit pending).

| # | Garde-fou | Valeur actuelle | Source code |
|---|-----------|-----------------|-------------|
| 1 | **DD journalier max → STOP jour** | `0.02` (2 %) | `settings.py:82` (corrigé) + `risk_manager.py:12` |
| 2 | **Confiance Auto unifiée signal+exécution** | `85 %` | `settings.py:96` (corrigé) + `risk_manager.py:16` |
| 3 | VIX no-trade | `> 35` | `settings.py:84` + `risk_manager.py:14` |
| 4 | DD semaine max | `0.05` (5 %) | `settings.py:83` |
| 5 | News gate critique (NFP/FOMC/CPI/GDP/JOLTS/PPI) — timezone ET (New York) | `30 min` | `settings.py:115-124` |
| 6 | Confiance max fallback (Auto interdit) | `65 %` | `settings.py:97` |
| 7 | Score min appel Claude API | `17/21 (BULL) / 18/21 (NEUTRAL) / 20/21 (BEAR/CRASH) — table G7` | `settings.py:94` |
| 8 | Vérif corrélation portefeuille | `seuil 0.60` | `correlations.py:92` |
| 9 | Circuit Breaker (timeout / retry / open) | `15 s / 2 / 60 s` | `settings.py:140-143` |
| 10 | Staleness monitor (NT8 / ATAS / COT / news) | `10 s / 30 s / 168 h / 5 min` | `settings.py:106-109` |
| 11 | Suspension Auto sur tweets critiques (Fed, POTUS, OPEC, Saylor, Musk, WSJ) | `60 / 45 / 30 / 20 / 20 / 15 min` | `risk_manager.py:34-41` |
| 12 | Rate limiting Claude API | `1 appel / 10 s` | `settings.py:98` |
| 13 | Atomic writes JSON (tempfile + os.replace) | actif | `code/utils/atomic_writer.py` |
| 14 | EIA surprise stocks pétrole — taille réduite | `> 3 M barils` | `risk_manager.py:22` |
| 15 | GDELT `score_crise > 7/10` → stop Auto (seuil : 3 événements géopolitiques majeurs détectés en moins de 24h) | `True` | `risk_manager.py:23` |
| 16 | Cooldown psychologique post-stop / 3 pertes / post-win | `15 min / 2 h / -50 % size` | `risk_manager.py:27-29` |
| 17 | Trades simultanés max | `2` | `risk_manager.py:10` |
| 18 | Risque max par trade | `1 % (compte > 50% patrimoine) / 0.5 % (compte ≤ 50% patrimoine)` | `risk_manager.py:9` |
| 19 | Filtre delta — actif si `delta_bid_ask > 60 %` du volume total de la bougie | `True` | `risk_manager.py:19` |
| 20 | Marchés alignés requis | `3/4 trading + 2/3 confirmation` | `risk_manager.py:15` + `settings.py:50-52` |

**ANTI-HALLUCINATION — Indicateur illisible** : si un indicateur renvoie une valeur incertaine, illisible ou hors plage → forcer la valeur NON_DÉTECTÉ et le signal à ATTENDRE. Interdit de deviner une valeur manquante.

---

## ❌ À IMPLÉMENTER (10 garde-fous prioritaires manquants)

### G1. Stop-loss obligatoire (validation runtime)

- **Règle** : aucun ordre ne peut être envoyé si `stop_loss == None` — REJET immédiat.
- **Justification** : risque de ruine si une position est laissée courir sans SL ; un seul oubli peut effacer 6 mois de gains.
- **Module cible** : `code/engine/trade_validator.py` (à créer)
- **Config recommandée** :
  ```
  ORDER_RULES["stop_loss_obligatoire"] = True
  ```
- **Source** : prompt v4.0 § Sécurité + APPORTS_GUIDE_EXTERNE.md

---

### G2. Slippage buffers par actif (ticks)

- **Règle** : SL et TP recalculés en ajoutant N ticks d'écart pour absorber le slippage réel.
- **Justification** : exécution réelle ≠ prix demandé — surtout en news, illiquidité ou gap d'ouverture.
- **Module cible** : `code/config/settings.py` + `code/execution/order_manager.py`
- **Valeurs recommandées** :
  | Actif | Buffer ticks | Valeur monétaire |
  |-------|--------------|------------------|
  | GC | 2 ticks | 2 × 0.10 USD = 0.20 USD |
  | HG | 2 ticks | 2 × 0.0005 USD = 0.001 USD |
  | CL | 3 ticks | 3 × 0.01 USD = 0.03 USD |
  | ZW | 4 ticks | 4 × 0.25 cents = 1.00 cent |
- **Source** : prompt v4.0 § Sécurité

---

### G3. Anti double-exécution (UUID signal + window dédoublonnage)

- **Règle** : chaque signal porte un UUID v4 unique ; deux signaux identiques (même actif + même direction) émis en moins de 60 s sont considérés comme doublon → second rejeté.
- **Justification** : éviter doublons sur reconnexion NT8, retry réseau, ou clic accidentel utilisateur.
- **Module cible** : `code/engine/trade_validator.py` + persistance signaux récents (SQLite)
- **Config recommandée** :
  ```
  ORDER_RULES["anti_doublon_id"]         = True
  ORDER_RULES["anti_doublon_window_sec"] = 60
  ```
- **Source** : prompt v4.0 § Mode AUTO

---

### G4. Dead zone horaire (faible volume)

- **Règle** : aucun signal trade entre 17h00 et 19h00 sur GC/HG/CL.
- **Justification** : faible volume CME (maintenance break + lunch ET) → spreads élargis et faux signaux.
- **Actifs concernés** : GC, HG, CL (ZW exclu — CBOT, plages différentes)
- **Module cible** : `code/config/settings.py` + `code/engine/trade_validator.py`
- **Config recommandée** :
  ```
  DEAD_ZONE = {
      "actifs": ["GC", "HG", "CL"],
      "start":  "17:00",
      "end":    "19:00",
      "tz":     "Europe/Paris",
  }
  ```
- ⚠️ **Timezone à confirmer** par l'utilisateur (Maroc / Paris / ET) avant codage.
- **Source** : prompt v4.0 § Points d'attention

---

### G5. Rollover front-month (48 h avant expiration)

- **Règle** : aucun nouveau trade dans les 48 h précédant l'expiration du contrat actif (front-month). Positions ouvertes gérées manuellement.
- **Justification** : volume migre vers le contrat suivant → gaps + slippage majeurs + faux breakouts.
- **Module cible** : `code/collectors/macro_collector.py` (calendriers expiration CME/CBOT) + `code/engine/trade_validator.py`
- **Cycles d'expiration** :
  | Actif | Cycle |
  |-------|-------|
  | GC | Fév / Avr / Jun / Aou / Oct / Dec |
  | HG | Mar / Mai / Jul / Sep / Dec |
  | CL | Tous les mois |
  | ZW | Mar / Mai / Jul / Sep / Dec |
- **Config recommandée** :
  ```
  ROLLOVER_BLOCK_HOURS = 48
  ```
- **Source** : prompt v4.0 § Points d'attention + master file SEMAINE 1

---

### G6. Mandatory Lock File à DD total 10 %

- **Règle** : si DD depuis sommet > 10 % → fichier `TRADING_LOCKED.lock` créé sur disque, le bot refuse de démarrer tant que ce fichier existe. Suppression manuelle obligatoire après analyse de l'échec.
- **Justification** : forcer une "conscience humaine" avant reprise — empêche toute spirale algorithmique destructrice.
- **Module cible** : `code/engine/risk_manager.py` (extension)
- **Config recommandée** :
  ```
  PALIERS_DD_TOTAL = { 0.10: "MANDATORY_LOCK" }
  LOCK_FILE_PATH    = os.path.join(DATA_DIR, "TRADING_LOCKED.lock")
  ```
- **Contenu fichier lock** : timestamp + raison + valeur DD + dernier trade
- **Source** : APPORTS_GUIDE_EXTERNE.md section 4

---

### G7. Détection régime marché (BULL / NEUTRAL / BEAR / CRASH)

- **Règle** : classifier l'environnement en continu (depuis ES, VIX, GC trend, breaks corrélation), adapter levier + taille position + seuil score selon régime.
- **Justification** : un signal valide en BULL est souvent un piège en CRASH ; sans contexte régime, le moteur 7 cercles fonce dans le mur.
- **Module cible** : extension `code/engine/correlations.py` (`detect_market_regime()`) + `code/engine/signal_scorer.py`
- **Tableau régime → action** :
  | Régime | Critère | Levier | Score min | Mode Auto |
  |--------|---------|--------|-----------|-----------|
  | BULL | ES > SMA200, VIX < 20, corrélations stables | 1.00 | 17/21 | autorisé |
  | NEUTRAL | ES ±5 % SMA200, VIX 20-30 | 1.00 | 18/21 | autorisé |
  | BEAR | ES < SMA200, VIX 25-35, corrélations instables | 0.50 | 20/21 | **interdit** |
  | CRASH | VIX > 35 OU DD > 2 % jour OU > 4 ruptures corrélation | 0.00 | — | **interdit** + sortie immédiate |
- **Source** : APPORTS_GUIDE_EXTERNE.md section 3

---

### G8. Killswitch Internet (mode Auto)

- **Règle** : si mode Auto actif + position ouverte + perte de connexion Internet → ordre GTC de fermeture envoyé au broker AVANT déconnexion totale.
- **Justification** : éviter une position orpheline sans contrôle pendant des heures ou jours.
- **Module cible** : `code/execution/nt8_ati_client.py` + nouveau `code/engine/network_monitor.py`
- **Config recommandée** :
  ```
  KILLSWITCH = {
      "internet_check_interval_sec": 5,
      "internet_lost_action":        "GTC_CLOSE_ALL",
      "ping_target":                 "8.8.8.8",
      "consecutive_failures_trigger": 3,
  }
  ```
- **Source** : prompt v4.0 § Mode AUTO

---

### G9. Calendrier OPEC meetings programmés

- **Règle** : blackout 30 min avant/après chaque meeting OPEC+ programmé (en plus des tweets `@OPECSecretariat` déjà couverts).
- **Justification** : impact direct CL — surprise possible même sans tweet (annonce dans le communiqué officiel).
- **État actuel** : tweets couverts via `SUSPENSION_DURATIONS["@OPECSecretariat"] = 30 min` (`risk_manager.py:38`). Calendrier programmé NON.
- **Module cible** : `code/collectors/macro_collector.py`
- **Config recommandée** :
  ```
  OPEC_CALENDAR_SOURCE   = "https://www.opec.org/opec_web/en/data_graphs/40.htm"
  OPEC_BLACKOUT_MINUTES  = 30
  ```

---

### G10. Monitoring santé FastAPI / Backend IA

- **Règle** : ping FastAPI toutes les 5 s — si pas de réponse > 30 s → flag `IA_HORS_LIGNE` → blocage de tous les signaux Auto + dashboard affiche "IA HORS LIGNE" en rouge.
- **Justification** : éviter qu'un crash silencieux du backend laisse passer des décisions stales ou contradictoires.
- **Module cible** : `code/api/health.py` (endpoint `/healthz`) + dashboard React (composant `BackendHealthBanner`)
- **Config recommandée** :
  ```
  HEALTH_CHECK = {
      "fastapi_ping_interval_sec": 5,
      "fastapi_max_silence_sec":   30,
      "on_down_block_signals":     True,
  }
  ```
- **Source** : prompt v4.0 § Données

---

## ⚠️ PARTIELS — À ENRICHIR (2)

### P1. Invalidation setup Belkhayate

- **État** : `MASTER_TRADEX_AI_v2.md` SEMAINE 5 planifie le module `code/engine/belkhayate.py` avec BGC ratio 0.618, Direction, Énergie, Pivots.
- **Manque** : code Python qui calcule l'invalidation (BGC franchi à contre-sens, énergie inversée, pivot stratégique cassé) et envoie un signal de sortie immédiat.
- **Module cible** : `code/engine/belkhayate.py` (à créer en phase KB Belkhayate)

### P2. OPEC blackout calendrier

- Couvert par G9 ci-dessus. État actuel = tweets seulement.

---

## 📊 SYNTHÈSE

| Catégorie | Compte |
|-----------|--------|
| ✅ Garde-fous déjà actifs (config + code) | **20** |
| ❌ Garde-fous à implémenter (haute priorité) | **10** |
| ⚠️ Partiels à enrichir | **2** |
| **Total cible** | **32 garde-fous** |

**Aucune ligne de code modifiée dans ce document.**
**Implémentation à étaler dans les phases dédiées de la Feuille de Route.**

---

*Phase 4-Light v4.0 — `GARDE_FOUS_PROPOSES.md` généré le 2026-05-03.*
