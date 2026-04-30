# TRADING-COPILOTE — Instructions Claude Code
> Lis ce fichier EN ENTIER avant toute action. Aucune exception.

---

## RÈGLE 0 — PROTOCOLE DE DÉMARRAGE OBLIGATOIRE

Chaque nouvelle session suit cet ordre exact :

1. Lire ce fichier (CLAUDE.md) — déjà fait
2. Lire le fichier le plus récent dans `_context/` (date la plus récente)
3. Annoncer exactement : "📍 Phase X — État : [résumé 1 ligne] — Prochaine action : [action]"
4. Attendre confirmation de l'utilisateur avant toute exécution

Ne jamais sauter une étape. Ne jamais supposer l'état du projet sans lire `_context/`.

---

## PROJET EN UNE LIGNE

Construire **TRADEX-AI** : un SaaS trading personnel basé sur la méthode Belkhayate,
alimenté par une Knowledge Base extraite de YouTube + PDFs.

---

## DÉCISIONS VERROUILLÉES — NE JAMAIS ROUVRIR

| Décision | Valeur verrouillée |
|----------|--------------------|
| Méthode | **Belkhayate exactement** — intouchable |
| Marchés trading | **Or, Cuivre, Pétrole, Blé** |
| Marchés confirmation | **Dollar (DXY), SP500, VIX** |
| Règle d'entrée | **3/4 trading + 2/3 confirmation alignés = signal valide** |
| Actifs | Choix de l'utilisateur — la méthode s'applique à tout actif |
| Architecture | **1 seul projet** : tout dans `C:\trading-copilote\` |
| Code | Toujours dans `C:\trading-copilote\code\` |
| Supprimés définitivement | Bitcoin, Yen |

---

## ARCHITECTURE DU PROJET

### Composante A — KB + 10 Skills (Phase actuelle)
Objectif : extraire les règles Belkhayate depuis YouTube + PDFs → générer 10 skills custom

```
code\scraper\           → scripts Python scraping YouTube
code\transcripts\       → fichiers .txt des vidéos
code\knowledge_base\    → KNOWLEDGE_BASE_MASTER.json
05-skills\              → 10 skills Belkhayate .md générés
```

### Composante B — TRADEX-AI (Phase suivante)
Objectif : SaaS temps réel, screenshot TradingView → signal ACHETER/VENDRE/ATTENDRE

```
code\frontend\          → React 18 + Vite + Tailwind 3.4
code\backend\           → NestJS + Supabase + BullMQ
```

Signal = 3 indicateurs Belkhayate alignés :
- Belkhayate Barycenter (bande rose/rouge)
- Belkhayate Direction (zones vertes/rouges)
- BELKHAYATE ÉNERGIE (histogramme)
- Pivots : Sol / Fa / Mi / Ré / Do

---

## FICHIERS CLÉS — LIRE DANS CET ORDRE

| Priorité | Fichier | Contenu |
|----------|---------|---------|
| 1 | `_context/[le plus récent]` | État exact de la session précédente |
| 2 | `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | Blueprint complet TRADEX-AI (prompt Vision V4 + architecture 7 layers) |
| 3 | `PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md` | Spec complète KB + 10 skills (1299 lignes) |

---

## RÈGLES TECHNIQUES NON NÉGOCIABLES

```
CHEMINS     : toujours absolus C:\trading-copilote\
COMMITS     : Conventional Commits stricts, JAMAIS d'accents dans les messages
PYTHON      : python -m py_compile fichier.py AVANT toute exécution
API KEY     : JAMAIS dans le code → toujours os.getenv("ANTHROPIC_API_KEY")
.env        : vérifier git check-ignore .env avant tout push
LINT        : obligatoire avant tout push
ROLLBACK    : documenter avant chaque phase risquée
```

---

## STACK TECHNIQUE

```
Scraping    : Python 3.14 + yt-dlp + youtube-transcript-api v1.x
KB          : Claude API (anthropic) + JSON
Frontend    : React 18 + Vite + Tailwind CSS 3.4
Backend     : NestJS (TypeScript)
IA Vision   : claude-sonnet-4-20250514 (Claude Vision API)
BDD         : Supabase (PostgreSQL + Auth)
Queue       : BullMQ + Redis (mode Octogone)
Deploy      : Vercel (frontend) + Railway (backend)
Validation  : Zod (TypeScript) + Pydantic (Python)
```

---

## SÉCURITÉS OBLIGATOIRES DANS TRADEX-AI

1. **News Gate** : bloquer signaux 30min avant NFP/FOMC/CPI
2. **Circuit Breaker** : timeout 15s → retry 2x → fallback ATTENDRE automatique
3. **Validation JSON** : schema Zod sur chaque retour Claude Vision
4. **Rate Limiting** : max 1 analyse/10s
5. **Disclaimer légal** : visible en permanence dans l'interface

---

## ÉTAT ACTUEL (mis à jour le 28/04/2026 à 23h00)

| Élément | État |
|---------|------|
| Structure dossiers | ✅ Terminé (28/04) |
| Rapport V4 Ortogonex | ✅ Présent à la racine |
| Phase 0 (setup Python) | ✅ Terminé dans code/ |
| Scraping YouTube | 🔄 En cours — scheduler actif |
| Transcripts récupérés | 31 (non utilisables — contenu marketing) |
| Prochaine action | Tester scrape_one.py le 29/04 matin |
| Phase 2 (extraction KB) | ⏳ Démarre à ~50 transcripts |
| TRADEX-AI | ⏳ Blueprint V4 prêt, développement non démarré |

---

## PROTOCOLE FIN DE SESSION OBLIGATOIRE

```
1. Générer _context/briefing-[YYYY-MM-DD].md (résumé complet)
2. Mettre à jour la section ÉTAT ACTUEL de ce fichier (CLAUDE.md)
3. Proposer le commit : git add . && git commit -m "chore: session [date] terminée"
4. Rappeler à l'utilisateur de faire git push
```

---

## PROFIL UTILISATEUR

- **Nom** : Abdelkrim
- **Niveau technique** : débutant — expliquer chaque commande comme à un élève du primaire
- **Objectif** : faire du trading un métier rentable avec la méthode Belkhayate
- **Approche** : l'IA comme copilote, l'utilisateur qui décide
- **OS** : Windows 11 — PowerShell — chemins backslash

---

*Ce fichier est la source de vérité absolue du projet.*
*En cas de doute entre ce fichier et une conversation : ce fichier a priorité.*
