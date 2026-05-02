# AUDIT MASTER MBK TRADING SAAS — RAPPORT COMPLET

**Document audité** : `MASTER_MBK_TRADING_SAAS_COMPLET.md` (1004 lignes)
**Date audit** : 2026-05-02
**Auditeur** : audit-trading-saas-prompts v2.1 — 11 passes
**Méthode** : PROMPT-GATE-AUDIT v3.1 + 11 passes anti-hallucination

---

## ⚠️ LIMITE DE L'AUDITEUR

Cet audit ne dispose pas de données marché temps réel. Toutes les corrélations annoncées dans le document, tous les coûts API, toutes les URLs, n'ont pas été testées en live. Les jugements ci-dessous portent sur la **cohérence interne** du document et sur la **plausibilité** des affirmations selon les références publiques connues — pas sur la validation empirique.

---

## 1. VERDICT EXÉCUTIF

| Élément | Valeur |
|---|---|
| **Score global** | **50 / 100** |
| **Statut** | FRAGILE — risque élevé |
| **Niveau de danger** | ÉLEVÉ — 3 problèmes BLOQUANTS |
| **Utilisable tel quel ?** | **❌ NON** |
| **Décision** | **À CORRIGER AVANT TOUT DÉPLOIEMENT** |

**Verdict en une phrase :** Le document est une vision architecturale séduisante mais bourrée de chiffres inventés (corrélations exactes, coûts Claude API ~15$/mois, codes COT, URLs APIs), de zones sous-spécifiées (timezone des couloirs, formules Belkhayate, fallbacks IA absents) et de risques non couverts (race conditions sur 12 JSONs, déconnexion Rithmic, conformité Maroc/CFTC).

---

## 2. PROBLÈMES CRITIQUES

| # | Gravité | Problème | Pourquoi c'est dangereux | Correction prioritaire |
|---|---|---|---|---|
| 1 | 🔴 BLOQUANT | Coût Claude API annoncé "15-20$/mois" | À 2 sec de fréquence, KB 2337 règles + 12 JSON + 7 cercles fusionnés en system prompt = ~5k-10k tokens × ~250k appels/mois = **~1.5B tokens input/mois**, soit ~4 500$/mois minimum (Sonnet à 3$/MTok). L'écart avec 15-20$ est d'**un facteur ×200 à ×300**. Si l'utilisateur déploie sur la base de ce budget, il découvre la facture après 2 jours. | Recalculer budget honnête : soit appels événementiels (signal qualifié uniquement) → ~50-200$/mois, soit prompt caching agressif → 50-100$/mois, soit Haiku 4.5 → 20-50$/mois. **Aucune** config réaliste ne tient à 15-20$ avec une fréquence 2 sec. |
| 2 | 🔴 BLOQUANT | Corrélations affichées comme constantes (`ρ=-0.85`, `ρ=-0.90`, etc.) | Toutes les corrélations sont **glissantes** et dépendent de la fenêtre. ES/VIX peut passer de -0.95 à -0.30. BTC/ES de +0.80 à -0.10 selon le régime. Coder ces valeurs en dur revient à donner à Claude un contexte **factuellement faux** la moitié du temps. Conséquence : signaux confiance 91% sur base de fausse corrélation = trades dangereux. | Recalculer en glissant 30j → recharger dans `correlations.py` à chaque appel → utiliser **valeur live** dans le prompt, jamais valeur figée. Marquer chaque corrélation avec `as_of` + `window`. |
| 3 | 🔴 BLOQUANT | Aucun fallback IA / broker / data feed | Si Claude API timeout (le doc cite Anthropic), le système se bloque sans plan de repli. Si Rithmic disconnect, NT8_data.csv se fige et les autres collecteurs continuent → Claude reçoit des données **stale** sans le savoir → signal sur prix d'il y a 10 min → ordre à un prix qui n'existe plus. Si ATAS plante, `ATAS_signals.json` se fige (pas de timestamp validation). | Ajouter pour chaque source : staleness check (`if now - last_update > N seconds: status=STALE`). Pour Claude : fallback règle déterministe locale (signal seulement si C1+C2 alignés ET pas d'alertes). Pour ATI : retry avec backoff + circuit breaker explicite. |
| 4 | 🔴 BLOQUANT | Race conditions sur 12 fichiers JSON | 11 collecteurs Python écrivent en parallèle dans `C:\MBK-SaaS\data\`. Le lecteur `claude_brain.py` lit ces fichiers pendant qu'un collecteur écrit → JSON tronqué = `JSONDecodeError` → exception non gérée → mode Auto se bloque silencieusement. | Pattern atomic write : écrire dans `*.tmp` puis `os.replace()`. Lecteur retry sur `JSONDecodeError`. Ou mieux : SQLite avec WAL (déjà présent pour trades, étendre à toutes les sources). |
| 5 | 🟠 GRAVE | Couloirs horaires sans timezone | `"GC": ["08:20-10:30"]` — heure locale Maroc ? UTC ? CST Chicago (où trade le contrat) ? ET New York ? Mojowit timezone implicite est une bombe à retardement. Si l'utilisateur déploie sur Windows local Maroc (UTC+1), `08:20` = 08:20 Maroc, alors que le pit COMEX ouvre à `08:20 ET = 13:20 Maroc`. Le système trade les fenêtres complètement à côté. | Forcer timezone explicite dans config : `"GC": [("13:20", "15:30", "Africa/Casablanca")]` ou stocker en UTC + tz du contrat. |
| 6 | 🟠 GRAVE | DX et VX listés "actifs piliers" mais sans couloirs / COT / règles | `"8 actifs piliers"` annoncé page 1, puis DX absent de `RÈGLES_RISQUE.couloirs`, COT_CODES (DX manquant, VX manquant), Cercle 1 BGC ne précise pas si les 8 sont calculés. VX (VIX futures) n'est pas tradé activement, c'est un actif de **sentiment** — incohérence sémantique. | Soit retirer DX/VX de la liste tradables et les marquer "indicateurs uniquement", soit compléter couloirs+COT+règles. Choisir, ne pas mélanger. |
| 7 | 🟠 GRAVE | Suspension Auto 10 min après tweet critique | Un tweet POTUS sur tarifs ou un tweet Fed peut produire une volatilité de **30-90 min**. 10 min est trop court — le système rouvre Auto en plein milieu du choc. | Aligner avec event windows news : suspendre 30 min minimum, et **ne pas réactiver tant que VIX_Δ% > seuil** sur les 15 dernières minutes. |
| 8 | 🟠 GRAVE | Confusion volume tick vs volume réel non levée | NinjaTrader 8 sur certains feeds (eSignal, IQFeed gratuit) renvoie tick volume, pas volume réel. Avec Rithmic, c'est volume réel. Le doc cite `volume_moyen_20 * 1.5` pour la cale ATAS — si quelqu'un branche un autre feed, la règle devient bidon sans alerte. | Document doit affirmer explicitement : "Rithmic obligatoire — Volume réel CME requis. Feed alternatif = règles ATAS désactivées." |

---

## 3. AUDIT 11 PASSES

| # | Passe | Statut | Erreurs / Oublis détectés | Correction |
|---|---|---|---|---|
| **P1** | PÉRIMÈTRE | ⚠️ À CORRIGER | Objectif clair (SaaS Belkhayate-MBK 8 actifs, mode Manuel/Auto). MAIS : DX et VX listés piliers mais sous-spécifiés. "OODA God Mode" et "Stratégie 7 Cercles" cités comme sources fusionnées sans définition. "21 sources gratuites" annoncées, on en compte 11-12 réelles. KB 2337 règles **non fournie** (Q3 du doc l'admet). | Rédiger glossaire en tête : pour chaque actif, dire "tradable / signal-only". Définir OODA + 7 Cercles. Compter et lister les 21 sources nominalement. |
| **P2** | ANTI-HALLUCINATION | 🔴 DANGEREUX | Voir §5 (tableau dédié). Corrélations exactes inventées. Coût Claude API irréaliste. URLs APIs (FRED, EIA, FINRA, AAII, GetXAPI, IMF) non vérifiées dans le doc. Codes COT non datés. Format `"ES: 13874+"` (avec `+`) est suspect. | Marquer toute corrélation `live, calc 30j, window glissante`. Marquer toute URL `À VÉRIFIER avant code`. Ajouter section "Sources non vérifiées — bloquer dev tant que tests passent". |
| **P3** | LOGIQUE TRADING | ⚠️ À CORRIGER | BGC ratio 0.618 cité sans formule. Direction/Energie/Pivots Belkhayate sans formule. Règle 3/4 marchés : "lesquels 4 parmi 8" non précisé. Règle 2/3 confirmations : "lesquelles 3" non précisé. Stop-loss présent dans le JSON IA mais aucune règle d'invalidation déterministe (qu'est-ce qui ferme avant TP/SL ?). Couloirs sans timezone (cf. §2 #5). | Annexer formules mathématiques exactes (Belkhayate publie ses formules). Préciser règle 3/4 : "4 majeurs : ES, GC, CL, DX" — règle 2/3 : "BGC + Cale + Pivot". Ajouter règles d'invalidation (delta inverse N barres → fermer). |
| **P4** | INTERMARCHÉ | ⚠️ À CORRIGER | Règles `RÈGLES_INTERMARKET` plausibles mais coefficients (`-1`, `+0.5`, `+1`) sans justification. Aucun garde-fou anti-corrélation : `max_trades_simultanes=2` autorise GC long + DX short → **double exposition synthétique** sur le même axe risk-off. Règle Cercle 7 + règle inter-market peuvent s'annuler (ex: dollar fort → GC -1, mais corrélation BTC/ES +0.65 sans impact dollar dans Cercle 7). | Ajouter contrôle **portefeuille** : si 2 trades dont la corrélation absolue > 0.6, taille combinée plafonnée à celle d'1 seul trade. Documenter origine empirique des coefficients (backtest période X). |
| **P5** | VOLUME / OI / COT | 🟠 GRAVE | COT Non-Commercials calculé en valeur **absolue** (`>+100k = haussier`) sans normaliser par Open Interest total. Un net long de 100k sur l'Or (OI ~500k) ≠ un net long 100k sur 6J (OI ~250k). Dark Pool FINRA J-14 bien qualifié **délai 2 semaines** ✅. Volume tick vs volume réel : non discuté (cf. §2 #8). Aucune mention de l'OI futures lui-même comme indicateur. Codes COT non datés (codes CFTC peuvent changer). | Normaliser COT en pourcentage de OI total. Ajouter feed OI dans Cercle 1. Vérifier codes COT contre CFTC `cmesf.txt` et figer la date de vérification. |
| **P6** | NEWS / MACRO | ⚠️ À CORRIGER | News gate 30 min (`zone_interdite_rouge=30`) cohérent. EIA mercredi 15h30 EST couvert ✅. NFP, FOMC, BOJ, OPEC meetings : pas de règles dédiées (juste filtrage Finnhub "Impact 3"). Suspension Auto 10 min après tweet : trop court (cf. §2 #7). Pas de règle sur **gap d'ouverture** ES dimanche 18h ET. | Ajouter table d'événements connus avec fenêtres custom : NFP=60min, FOMC=180min (avant + après), BOJ=120min. Suspension Auto post-tweet à 30min minimum + réactivation conditionnée VIX. |
| **P7** | RISQUE / EXÉCUTION / BROKER | 🟠 GRAVE | 2% par trade, 3% DD jour, 2 trades max, 3 pertes → 2h pause = **OK socle**. Port ATI 36973 par défaut NT8 = correct. **MANQUE** : timeout TCP ATI, retry policy, slippage max acceptable, gestion partial fill, gestion connection drop Rithmic, gestion ordre non confirmé, garde-fou doublon ordre, persistance ordres en cas de crash Python. | Ajouter section "Robustesse exécution" : timeout 5s sur PLACE, retry 3× backoff, slippage_max=2 ticks → annule, partial_fill < 50% → annule reste, heartbeat ATI 10s. |
| **P8** | PSYCHOLOGIE | ⚠️ À CORRIGER | "3 pertes consécutives → pause 2h" présent ✅. **MANQUE** : règle après gros gain (overconfidence — réduire taille 24h post +5%), règle fatigue (heures cumulées trading par jour), règle journal post-trade obligatoire, règle revenge trading explicite (pas de re-entry < 15 min après stop touché). | Ajouter `post_win_size_reduction`, `max_screen_hours_day`, `cooldown_post_stop=15min`, `journal_required_before_next_trade`. |
| **P9** | SAAS / ARCHITECTURE IA | 🔴 DANGEREUX | **Aucun fallback Claude API** (cf. §2 #3). Aucun fallback ATAS plante. Aucun fallback NT8 déconnecté. Race conditions sur 12 JSON (cf. §2 #4). Prompt GOD MODE + KB 2337 règles : context window 200k tokens Sonnet OK, mais coût exploser (cf. §2 #1). Pas de prompt caching mentionné. Pas de monitoring (Prometheus/health check). Pas de rotation de logs. SQLite write concurrency non addressée. | Section "Robustesse infra" complète : staleness check par source, fallback déterministe, prompt caching avec `cache_control` Anthropic, atomic writes JSON, healthcheck endpoint FastAPI. |
| **P10** | RÉGLEMENTAIRE | 🟠 GRAVE | Aucune mention : (a) Office des Changes Maroc pour transferts USD vers broker US, (b) Allocation Touristique limites annuelles, (c) déclaration IS/IR sur P&L au Maroc, (d) statut CFTC du SaaS comme système algo (le document parle Mode Auto = système algorithmique, ce qui peut activer obligations Algorithmic Trading auprès du broker NTB). Le doc évoque "broker NTB" mais ne dit rien sur le KYC trading algo. | Ajouter section "Conformité juridictionnelle Maroc + USA" : déclarer le Mode Auto au broker, clarifier statut Office des Changes, conserver registre des trades pour fiscalité marocaine. **Consultation juridique recommandée avant Live**. |
| **P11** | SCORE FINAL | ⚠️ — | Voir détail ci-dessous | — |

### Détail score P11 — 50/100

| Catégorie | Max | Note | Justification |
|---|---|---|---|
| Clarté objectif | 8 | **6** | Vision claire mais DX/VX flous, KB 2337 manquante |
| Anti-hallucination | 15 | **4** | Corrélations inventées, coûts API irréalistes, URLs non vérifiées |
| Logique trading | 13 | **7** | Belkhayate non détaillé, couloirs sans timezone, invalidation absente |
| Risque / money mgmt | 13 | **8** | Socle OK mais corrélation portfolio/slippage/partial fill absents |
| News / macro | 10 | **6** | Gate présent mais NFP/FOMC/BOJ/OPEC sous-traités |
| Intermarché | 8 | **5** | Règles présentes mais coefficients non sourcés, anti-corr absent |
| Volume / OI / COT | 8 | **4** | COT non normalisé OI, tick vs vol non levé |
| Broker / exécution | 10 | **5** | ATI port OK, mais timeout/retry/slippage/partial fill absents |
| SaaS / architecture IA | 15 | **5** | Pas de fallback, pas de race condition, coût Claude irréaliste |
| **TOTAL** | **100** | **50** | **FRAGILE — à corriger** |

---

## 4. CONTRADICTIONS INTERNES

| # | Contradiction | Emplacement | Impact | Correction |
|---|---|---|---|---|
| 1 | "8 actifs piliers" vs couloirs horaires définis pour 6 actifs (DX et VX absents) | §Métadonnées (l.30-32) ↔ Section 5 (l.554-562) | Le système ne peut pas trader DX/VX en mode Auto sans couloir | Soit retirer DX/VX, soit compléter les couloirs |
| 2 | Données NT8 "toutes les 2 secondes" vs Range Bars 5 ticks (asynchrones par nature) | §Stack (l.15) ↔ §Méthode (l.40) | Range Bar peut clore en plein milieu d'un cycle 2s → données partielles | Bascule sur événement de close de bar plutôt que polling 2s |
| 3 | "Plafond absolu 200$/mois" vs coût Claude API réaliste | §Budget (l.26) ↔ §Section 1 (l.78) | Premier mois → 4000$+ de facture API | Recalculer architecture coûts ou réduire fréquence appels |
| 4 | "Sonnet API ~15-20$/mois" vs "appels toutes les 2 secondes" implicites dans flux | l.78 vs l.115-117 | Idem #3 | Préciser : appels Claude **événementiels** (sur signal qualifié), pas en streaming |
| 5 | Cercle 7 corrélations figées vs "matrice corrélations glissante" Section 2 | l.385-393 ↔ l.140 | Le code utilisera quoi : valeurs figées ou glissantes ? | Choisir : valeurs **glissantes** uniquement, supprimer le tableau figé |
| 6 | Mode Auto "exécute ses propres ordres" vs "mode Manuel : tu décides" | §Vision (l.63-64) ↔ Section 8 | Pas de transition décrite Manuel → Auto et inversement | Ajouter machine d'états Manuel ↔ Auto avec triggers |
| 7 | "DD jour 3% → arrêt total journée" vs "DD > 2% → passage forcé Mode Manuel" | l.524 ↔ l.852 | Quel seuil prime ? 2% (Manuel) ou 3% (arrêt) ? | Hiérarchiser : 2% → Manuel forcé, 3% → arrêt complet |
| 8 | "Drawdown Stop = -3%" vs "Métrique validation : Max Drawdown/jour ≤ 3%" | l.524 ↔ l.879 | Si DD jour est arrêté à 3%, la métrique sera toujours ≤ 3% par construction → tautologie | Mesurer DD intra-day **avant** stop, ou métrique différente (ex: DD trades) |
| 9 | "Bullish > 55% AAII = signal contrarian baissier" mais aucun blocage de trade long | l.323 vs §Risque | AAII bullish = info pure, pas de règle d'action | Ajouter règle : `AAII_bull > 55% → boost confiance pour shorts uniquement` |

---

## 5. HALLUCINATIONS / AFFIRMATIONS NON PROUVÉES

| # | Affirmation | Type de risque | Donnée nécessaire | Reformulation sûre |
|---|---|---|---|---|
| 1 | `Claude API (Sonnet) ~15-20$/mois` | Coût | Calcul réel : tokens/appel × appels/mois × tarif Anthropic | "Coût Claude API : à calibrer selon fréquence d'appel. Estimation events-only : 50-200$/mois. Cf. annexe coûts." |
| 2 | `"GC_DX": "inverse (ρ ~ -0.85)"` | Corrélation figée | Calcul live 30j roulant | "GC_DX : corrélation **glissante** calculée 30j via `correlations.py`, valeur live, indicative" |
| 3 | `"ES_VX": "inverse (ρ ~ -0.90)"` | Corrélation figée | Idem | Idem |
| 4 | `"BTC_ES": "positive (ρ ~ +0.65)"` | Corrélation figée — historiquement très variable | Idem + warning instabilité | "BTC_ES : corrélation **instable** selon régime. Window 30j live. Ne pas figer." |
| 5 | `"CL_DX": "inverse (ρ ~ -0.70)"` | Corrélation figée | Idem | Idem |
| 6 | `"HG_ES": "positive (ρ ~ +0.70)"` | Corrélation figée | Idem | Idem |
| 7 | `"6J_VX": "positive (ρ ~ +0.55)"` | Corrélation figée | Idem | Idem |
| 8 | `"GC": "088691"` (codes COT) | Codes non datés, peuvent changer | Vérification CFTC + `as_of` | "Codes COT vérifiés au YYYY-MM-DD via cftc.gov/MarketReports/CommitmentsofTraders/HistoricalViewable" |
| 9 | `"ES": "13874+"` | Format `+` douteux | Vérification CFTC | Code ES exact, sans `+` |
| 10 | `https://www.cftc.gov/dea/futures/deacmesf.htm` | URL probablement obsolète (CFTC a refondu son site) | Test live | À vérifier — endpoint actuel : `cftc.gov/dea/futures/deacme_lf.htm` ou API publicReportingAPI |
| 11 | `https://www.finra.org/sites/default/files/ATS_Weekly.csv` | URL probablement inexacte | Test live | Endpoint réel FINRA OTC Transparency : `regulatoryservices.finra.org/.../ATSEquitiesData` |
| 12 | `https://feargreedchart.com/api/` | Source non officielle CNN | URL CNN officielle | F&G CNN officiel : `production.dataviz.cnn.io/index/fearandgreed/graphdata` |
| 13 | `https://api.getxapi.com/v1/timeline` | Service "GetXAPI" non documenté publiquement | Vérification existence | Marquer "Service à valider, sinon fallback Twitter API officiel ou alternative" |
| 14 | `~50$/mois data feed CME` | Approximatif sans source | Devis NTB officiel | "50$/mois indicatif — devis NTB requis selon contrats" |
| 15 | `~70$/mois ATAS Pro` | Tarif Lifetime ATAS varie | Tarif officiel atas.net daté | "ATAS Pro : ~80-99$/mois ou Lifetime, à vérifier sur atas.net" |
| 16 | `~1$/mois GetXAPI 6 comptes` | Calcul `6 × 50 × 30 / 20 = 0.45$` non sourcé | Pricing officiel GetXAPI | "À valider service par service" |
| 17 | `>+100k = haussier institutionnel fort` (COT) | Seuil arbitraire non normalisé OI | Backtest seuils sur historique | "Seuil = percentile 80 historique 5 ans, recalculé annuellement" |
| 18 | `>140 SKEW = institutionnels couverts contre crash` | Seuil arbitraire | Backtest | Seuil empirique à valider, sinon utiliser z-score |
| 19 | `Belkhayate BGC ratio 0.618` | Formule complète non donnée | Doc Belkhayate officielle | Annexer formule mathématique complète |
| 20 | `2337 règles KB` | KB non fournie (admis Q3) | Texte intégral KB | Sans la KB, le "cerveau" est creux |

---

## 6. RISQUES TRADING NON COUVERTS

| # | Risque oublié | Gravité | Pourquoi l'ajouter |
|---|---|---|---|
| 1 | **Slippage non borné** | 🔴 GRAVE | Aucun `slippage_max`. Sur ouverture marché ou news, slippage 5-10 ticks possible. Stop-loss "16$" peut se transformer en "60$". |
| 2 | **Partial fill** | 🟠 ÉLEVÉ | Si ordre 2 contrats et seul 1 fill, comportement non défini. Doit annuler le reste ou attendre ? |
| 3 | **Disconnect Rithmic en cours de trade** | 🔴 GRAVE | Si data feed coupe, NT8 voit prix figé, Claude reçoit prix figé, ordre exécuté à mauvais prix. Pas de heartbeat. |
| 4 | **Gap d'ouverture dimanche 18h ET (ES)** | 🟠 ÉLEVÉ | Aucune règle. ES peut gap 50 points ouverture week-end → stop saute → perte > 2% |
| 5 | **Rollover futures** | 🟠 ÉLEVÉ | "23:00-00:30 interdit" mais sans timezone et sans gestion contrat actif vs prochain |
| 6 | **Limit up / Limit down** | 🟠 MOYEN | Sur mouvement extrême, marché peut être halt-limit. Aucune règle. |
| 7 | **Corrélation portfolio (double exposition)** | 🟠 ÉLEVÉ | 2 trades ES long + BTC long = exposition risque-on doublée mais comptée 2 trades |
| 8 | **Revenge trading explicite** | 🟠 MOYEN | 3 pertes consécutives → pause, mais re-entry immédiat post-stop autorisé |
| 9 | **Surperformance / overconfidence** | 🟡 FAIBLE | Pas de réduction taille post-gros gain |
| 10 | **Coût d'opportunité Auto vs Manuel** | 🟡 FAIBLE | Si Auto rate signal 18-21 pendant pause 2h, pas tracé |
| 11 | **Margin call** | 🟠 ÉLEVÉ | Aucune règle si broker margin call |
| 12 | **Order non confirmé après envoi ATI** | 🔴 GRAVE | Si NT8 reçoit PLACE mais pas de confirmation, Python suppose-t-il open ou closed ? |
| 13 | **Doublon d'ordre** | 🟠 ÉLEVÉ | Si Python crash et redémarre, peut renvoyer ordre déjà placé |
| 14 | **Volatilité expansion intra-trade** | 🟡 FAIBLE | Si VIX passe 18→25 pendant trade, pas de réduction de taille active |

---

## 7. RISQUES SAAS / IA NON COUVERTS

| # | Module manquant | Impact | Recommandation |
|---|---|---|---|
| 1 | **Fallback Claude API** | 🔴 BLOQUANT | Si timeout/erreur 529/rate limit Anthropic → mode Auto figé sans signal | Fallback déterministe local (règle simple : 7C score ≥ 14 ET pas d'alerte rouge → signal proche). Sinon ATTENDRE. |
| 2 | **Prompt caching Anthropic** | 🔴 ÉCONOMIQUE | Sans cache, KB 2337 règles re-envoyée chaque appel = coût × 10-50 | Activer `cache_control` sur le system prompt (KB) — cache 5 min, économie ~90% |
| 3 | **Health check / monitoring** | 🟠 GRAVE | Si un collecteur plante silencieusement (ex: GDELT), Claude reçoit vieille donnée | Endpoint `/health` FastAPI listant `last_update_per_source`, alerte si > seuil |
| 4 | **Atomic writes JSON** | 🔴 GRAVE | Race condition lecture pendant écriture → JSON corrompu | Pattern `tempfile + os.replace()` |
| 5 | **Retry / circuit breaker APIs** | 🟠 GRAVE | Si Finnhub renvoie 429 5 fois, le collecteur abandonne et les news disparaissent | Backoff exponentiel + circuit breaker per-API |
| 6 | **Persistance d'état Auto** | 🔴 GRAVE | Si Python crash en plein trade ouvert, redémarrage perd l'état (ordre actif ?) | Persister state machine en SQLite + recovery au boot |
| 7 | **Logs structurés rotation** | 🟡 FAIBLE | `signals_log.json` grossit indéfiniment | Rotation journalière + compression |
| 8 | **Versionning KB** | 🟠 GRAVE | Si KB 2337 mise à jour, comment savoir quelle version a généré quel signal ? | Hash SHA256 KB stocké dans chaque signal |
| 9 | **Audit trail décisions** | 🟠 GRAVE | Pour debug ou conformité, quel cercle a bloqué quel signal ? | Logger snapshot complet input/output Claude par signal |
| 10 | **Test KB sur 50 scénarios** | 🟠 SOUS-DIMENSIONNÉ | Semaine 6 prévoit "50 scénarios historiques" — c'est trop peu | Minimum 500 scénarios, idéalement 2000+ couvrant tous les régimes |
| 11 | **Détection drift modèle** | 🟡 MOYEN | Anthropic peut changer Sonnet (silent updates) | Test régression hebdomadaire sur scénarios figés |
| 12 | **Sécurité .env** | 🟠 GRAVE | `.env` cité mais pas de mention de chiffrement OS-level (DPAPI Windows) ou variables d'environnement système | `.env` jamais commit + `keyring` ou DPAPI Windows pour clés |
| 13 | **Backup** | 🟠 GRAVE | SQLite local = single point of failure | Backup quotidien chiffré sur disque externe ou cloud |
| 14 | **Limit context window** | 🟡 MOYEN | Si l'historique est passé en contexte, dépasser 200k tokens fait planter | Contrôle pré-envoi `len(prompt_tokens)` |
| 15 | **Coût alarm** | 🟠 GRAVE | Pas d'alerte si dépassement budget API | Daily budget limit Anthropic + alerte > 80% |

---

## 8. CHECKLIST DE CORRECTIONS — P0 / P1 / P2

### 🔴 P0 — BLOQUANTS (obligatoire avant toute ligne de code)

- [ ] Recalculer budget Claude API avec hypothèse réaliste (events-only ou cache) — produire feuille Excel
- [ ] Remplacer toutes les corrélations figées par appels live `correlations.py` avec window 30j
- [ ] Ajouter section "Fallbacks" : Claude API down, ATAS down, Rithmic disconnect, NT8 disconnect
- [ ] Imposer atomic writes pour les 12 fichiers JSON
- [ ] Ajouter timezone explicite à TOUS les couloirs horaires (UTC, ET, ou Africa/Casablanca)
- [ ] Décider : DX et VX = tradables ou signal-only — compléter ou retirer
- [ ] Étendre suspension post-tweet à minimum 30 min + condition VIX

### 🟠 P1 — GRAVES (avant Semaine 6)

- [ ] Annexer formules Belkhayate (BGC, Direction, Energie, Pivots) avec références
- [ ] Définir précisément règle 3/4 (lesquels 4) et règle 2/3 (lesquels 3)
- [ ] Vérifier toutes URLs APIs (FRED, EIA, FINRA, AAII, GetXAPI, IMF, CBOE) avec date de vérification
- [ ] Vérifier codes COT contre CFTC officiel + dater
- [ ] Normaliser COT en % de OI total (pas valeur absolue)
- [ ] Spécifier feed Rithmic obligatoire + warning volume tick
- [ ] Ajouter fenêtres event custom : NFP=60min, FOMC=180min, BOJ=120min, OPEC=120min
- [ ] Ajouter règles slippage / partial fill / timeout ATI / heartbeat
- [ ] Ajouter règle anti-corrélation portfolio (max combo si |ρ|>0.6)
- [ ] Ajouter règle revenge trading (cooldown 15min post-stop)
- [ ] Activer `cache_control` Anthropic sur la KB
- [ ] Persistance d'état Mode Auto en SQLite + recovery au boot
- [ ] Section "Conformité juridictionnelle Maroc + USA" — consulter avocat
- [ ] Hiérarchiser DD seuils 2% (Manuel) vs 3% (arrêt total) — supprimer ambiguïté
- [ ] Étendre tests historiques de 50 → 500+ scénarios

### 🟡 P2 — IMPORTANT (avant Live Trading)

- [ ] Healthcheck endpoint FastAPI + alertes
- [ ] Hash SHA256 de la KB stocké dans chaque signal log
- [ ] Audit trail snapshot input/output Claude par signal
- [ ] Backup chiffré quotidien SQLite
- [ ] Daily budget limit Anthropic + alerte > 80%
- [ ] Rotation logs journalière + compression
- [ ] Test régression hebdomadaire sur scénarios figés
- [ ] Stockage clés API via keyring/DPAPI (pas .env clair)
- [ ] Règles psycho : post-win size reduction, max screen hours, journal obligatoire
- [ ] Documentation transition d'états Manuel ↔ Auto

---

## 9. SECTIONS À RÉÉCRIRE

| Section | Raison | Priorité |
|---|---|---|
| **Métadonnées & Décisions Gelées** | Lever ambiguïté DX/VX, ajouter timezone, marquer KB 2337 comme prérequis bloquant | 🔴 P0 |
| **Section 1 — Budget** | Recalcul honnête du coût Claude API + ATAS Lifetime vs mensuel + hypothèses explicites | 🔴 P0 |
| **Cercle 3 — Institutionnels** | Codes COT à dater, normalisation OI, URLs FINRA/CBOE à vérifier | 🟠 P1 |
| **Cercle 7 — Corrélations & Régime** | Supprimer toutes les valeurs figées `ρ ~ -0.85`, marquer "live calc", ajouter détecteur de **rupture** de corrélation | 🔴 P0 |
| **Section 4 — Moteur de décision Claude AI** | Ajouter prompt caching, fallback déterministe, gestion erreur API, gestion `JSONDecodeError` retour Claude | 🔴 P0 |
| **Section 5 — Règles de risque** | Ajouter slippage, partial fill, timeout ATI, anti-corrélation, revenge cooldown, post-win reduction, timezone couloirs | 🔴 P0 |
| **Section 7 — Calendrier Semaine 6** | Augmenter scénarios test 50 → 500+, ajouter prompt caching dans le scope | 🟠 P1 |
| **Section 7 — Calendrier Semaine 8** | Étendre circuit breaker : disconnects, partial fill, slippage, doublon ordre, persistance état | 🔴 P0 |
| **Section 9 — Structure des fichiers** | Documenter atomic writes, lock files, schéma SQLite étendu (state, audit trail) | 🟠 P1 |
| **Nouvelle Section — Conformité juridictionnelle** | Inexistante. Office des Changes Maroc + statut algo CFTC + KYC NTB | 🟠 P1 |
| **Nouvelle Section — Robustesse infrastructure** | Inexistante. Fallbacks, healthcheck, monitoring, alertes, backup | 🔴 P0 |
| **Nouvelle Section — Psychologie & discipline** | Inexistante en tant que telle. Règles tilt, fatigue, journal, post-win | 🟠 P1 |

---

## DÉCISION FINALE

> 🚫 **REJETÉ EN L'ÉTAT — DOCUMENT À CORRIGER**

Le document est **architecturalement séduisant** mais comporte **3 problèmes BLOQUANTS** qui rendent un déploiement live **dangereux** :
1. Budget Claude API irréaliste d'un facteur ×100 à ×300
2. Corrélations figées factuellement fausses la moitié du temps
3. Aucun fallback IA / broker / data feed

**Avant d'écrire la première ligne de code de production**, exécuter la checklist P0 complète. Re-soumettre le document à un nouvel audit après corrections — score cible ≥ 75/100.

> **Toujours préférer PAS DE TRADE à un mauvais trade.**
> **Toujours préférer DONNÉES INSUFFISANTES à une invention.**

---

*AUDIT MASTER MBK — 11 passes — Score 50/100 — 2026-05-02*
*audit-trading-saas-prompts v2.1 — conforme PROMPT-GATE-AUDIT v3.1*
