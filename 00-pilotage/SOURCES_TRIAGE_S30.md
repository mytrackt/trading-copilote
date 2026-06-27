# SOURCES TRIAGE — Session S30 (26/06/2026)

> Décisions verrouillées sur les sources vidéo à traiter pour TRADEX-AI.

---

## DÉCISION 1 — Trading Geek : WHISPER ARCHIVÉ → GEMINI À FAIRE

- **Anciennes transcriptions Whisper (113 .txt)** → ❌ ARCHIVÉES (non fiables — audio seul, pas de synchro image)
- **Action** : déplacer `03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\` → `_archive\trading-geek-whisper-elimine\`
- **Audio MP3** : CONSERVER — nécessaires pour la re-transcription Gemini
- **113 vidéos Trading Geek** → ✅ À RE-TRANSCRIRE avec `gemini_transcriber.py` (méthode fiable)
- **Usage après transcription** : décidé en Phase 4 (audit contenu — Couche 2 ou 3 selon pertinence Belkhayate)

---

## DÉCISION 2 — 91 nouvelles vidéos : TOUTES À GARDER

### Groupe A — Référence Architecture / Écosystème Claude (15 vidéos)
**Chaînes : Trading with DaviddTech + Alex Carter**
**Usage : informer la conception de l'application (frontend, MCP, workflow IA) — PAS pour la KB trading**

| ID | Notes |
|----|-------|
| h6qUy92Maco | I Gave Claude Full Access to TradingView |
| G7zv25c7Z8M | |
| 4z1I0u1UnXQ | |
| cXhEw2jF4go | |
| y_bsjZThP0o | |
| EUSXhJNwRqI | |
| vIX6ztULs4U | |
| HfEu7XPUnAU | |
| lH5wrfNwL3k | |
| R7O2TaM709Y | |
| tkAq6g2Gjz4 | I Let Claude AI Opus 4.8 Trade For Me |
| 3IgYhw5WqTY | |
| Ebzawm73H4I | |
| jnJF0W2XgqA | |
| GlkJMO_ufYA | How I Built My Own AI Trading Assistant Using Claude Cowork (Alex Carter) |

> ⚠️ `7rianyn0wPI` présent dans ce groupe = vidéo Belkhayate déjà dans KB → ignorer

---

### Groupe B — KB Couche 3 : Structure Marché ICT (40 vidéos)
**Chaîne : TTrades**
**Usage : enrichir structure_marche · volume_liquidite · gestion_risque_entree · psychologie**
**Méthode transcription : Gemini multimodal (vidéos avec charts)**

| ID | ID | ID | ID |
|----|----|----|----|
| q3nauvjT3q0 | -ocfPuD_oqE | v1X8UMWgWmI | HbOeD_JVens |
| yH4eYwUgdTY | 9BY-MQRNy-Y | PQiRV0JMhIQ | eywpZT3z6GQ |
| Kf4c41_qO1s | vn1RYjhJUnQ | -KKuZb5Z5aU | w-JekHg6Ldk |
| tyoxl1l-6iI | SlWxhzhLo3A | 3eVxTV_7L2U | FAKWJ-1NlLE |
| qdQYhePcvGE | MvD7fQQ0szE | m4k_1pF5zFI | 8BWkRGhuj1k |
| VD4xb9VfMHA | TNybDCtwBnc | 4Gm8p6O7Ebs | WFqLwOp2pXw |
| JHVaSKtE1Ys | -wr4xATE37g | r_UF8U-hsL8 | 5fnFOh5YuM0 |
| 4jU547ocod4 | iEaMbuFZb24 | ubCe509_JLY | Ibw4saRtYMk |
| LKNQDAdId4s | TfHlNgAZ_II | caaS6_Q7O78 | sIcsLFSNoXM |
| EYzP7c24AwM | FGkb_50BfT8 | WwmS47Gb3M0 | mwmWNCTEYtY |

---

### Groupe C — KB Couche 3 : Quant / Corrélations (5 vidéos)
**Chaîne : Lewis Jackson**
**Usage : enrichir correlations · structure_marche (méthodes statistiques / Markov)**

| ID |
|----|
| ZVMTeDBmSrI |
| 6njREUQAFdg |
| 4vZZReXFKkQ |
| reiPfBnUBys |
| aDWJ6lLemJU |

---

### Groupe D — KB Couche 3 : Psychologie / Gestion Risque (9 vidéos)
**Chaîne : Rayner Teo**
**Usage : enrichir psychologie · gestion_risque_entree · gestion_position_active**

| ID |
|----|
| k1TKN8iGDao |
| lLOKH4ThTP0 |
| tAR_JREOjvE |
| pGO9MwMCJKo |
| ej1UdL-oj_o |
| YxiJRWBy8ZA |
| yF6fCCz3IJU |
| yKk_HmtE-Zc |
| M9DCW8TaWuE |

---

### Groupe E — KB Couche 3 : Order Flow / Day Trading (16 vidéos)
**Chaîne : Humbled Trader**
**Usage : enrichir volume_liquidite · structure_marche**

| ID | ID | ID | ID |
|----|----|----|----|
| IqvnryFzZD4 | Vxj7QD6Lbvk | YGpiVS8BNLw | i37xXd_wI5k |
| Eico0SYYNnk | vswa9HZv7q4 | uV84kDLUgZ4 | GVbWx5x2i-Q |
| T3sCLOvsdus | UWKNLR4jOI0 | ZP_3AIko08w | _Dqiuf-9Lps |
| OLS9w6DOpOg | UpmJJjKvJxo | o4bB5UsgnX4 | IEu3NHVE_lQ |

---

### Groupe F — KB Couche 2 : Or / GC — PRIORITÉ (5 vidéos)
**Chaîne : Kasper Trading SMC**
**Usage : indicateurs_tendance · structure_marche spécifiques à l'Or (GC = actif principal TRADEX)**
**Couche 2 = compatible Belkhayate sur l'actif Or**

| ID |
|----|
| cPceiD1PWrI |
| 1SLbe0k6x4I |
| TXLqKZRx6hg |
| RQ36kizIDk0 |
| 6_BCuy5QYPc |

---

## DÉCISION 3 — Méthode de transcription

**Toutes ces sources (Trading Geek re-triage exclu + 91 nouvelles) → Gemini multimodal uniquement**
- Script : `05-saas\utils\gemini_transcriber.py`
- Modèle : `gemini-2.5-flash` (verrouillé)
- Chunking auto si > 50 min

**Ordre de priorité transcription :**
1. Groupe F — Kasper Gold (5 vidéos — Couche 2, Or = actif principal)
2. Groupe B — TTrades (40 vidéos — structure marché)
3. Groupe A — DaviddTech + Alex Carter (15 vidéos — conception app)
4. Groupe C — Lewis Jackson (5 vidéos)
5. Groupe D — Rayner Teo (9 vidéos)
6. Groupe E — Humbled Trader (16 vidéos)
7. Trading Geek — 113 vidéos (Whisper archivé → re-transcription Gemini)

---

## RÉSUMÉ

| Catégorie | Nb vidéos | Action |
|---|---|---|
| Trading Geek | 113 | ⚠️ Whisper archivé → ✅ RE-TRANSCRIRE Gemini |
| Architecture Claude (DaviddTech + Alex Carter) | 15 | ✅ Gemini → référence conception |
| KB Couche 2 (Kasper Gold) | 5 | ✅ Gemini → KB priorité |
| KB Couche 3 (TTrades + Lewis Jackson + Rayner Teo + Humbled Trader) | 70 | ✅ Gemini → KB |
| Trading Geek (re-triage) | 113 | ✅ Gemini — usage décidé Phase 4 |
| **TOTAL nouvelles transcriptions** | **203** | Gemini multimodal |

---

*Fichier créé session S30 — 26/06/2026*
*Décisions validées par Abdelkrim*
