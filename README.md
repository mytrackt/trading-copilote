# TRADING-COPILOTE

Système d'aide à la décision de trading basé sur la méthode Belkhayate.
Un SaaS personnel appelé **TRADEX-AI** : données NinjaTrader 8 en temps réel → signaux
ACHETER / VENDRE / ATTENDRE selon les indicateurs Belkhayate (Barycentre, Direction,
Énergie, Pivots Belkhayate).

## Méthode

**Belkhayate — intouchable et suivie exactement.**

| Rôle | Actifs |
|------|--------|
| Trading | Or (GC), Cuivre (HG), Pétrole (CL), Blé (ZW) |
| Confirmation | Dollar (DX), SP500 (ES), VIX (VX) |

**Règle d'entrée : 3/4 trading + 2/3 confirmation alignés = signal valide**

## Workflow métier

```
TRANSCRIRE (01-moteur) → DISTILLER (04-cerveau) → CONSTRUIRE (05-saas)
```

## Structure du projet (réorganisation du 11/06/2026)

```
trading-copilote/
  00-pilotage/           Docs de pilotage : feuille de route, garde-fous, rapports, briefings (_context), dette technique
  01-moteur-transvideo/  Moteur de transcription YouTube (scripts Python + transvideo_pipeline.bat) — SEULE version vivante
  02-sources-brutes/     Corpus sources : methode-belkhayate, marches-trading, playbook, kb-sources (PDF + txt)
  03-transcriptions/     transcripts-bruts (142 whisper .txt) + nouvelles-sources (sorties du moteur)
  04-cerveau-trading/    KNOWLEDGE_BASE_MASTER.json (142 videos, 11 categories de regles) + processor_status.json
  05-saas/               Code TRADEX-AI : engine, config, utils, knowledge_base, maquettes
  06-skills/             10 skills Belkhayate (.md)
  _archive/              MBK en pause, ancien whisper_pipeline.py, vieux logs, methodes externes, backups
  _temp/                 Audio jetable (gitignore) — supprimable sans risque
```

À la racine : `CLAUDE.md` (instructions Claude Code), `AGENTS.md` (instructions agents), `.env` (clés, gitignoré).

## Documents clés

- `00-pilotage/FEUILLE_DE_ROUTE.md` → 11 phases A→K
- `00-pilotage/RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` → blueprint technique TRADEX-AI
- `00-pilotage/DETTE_TECHNIQUE.md` → bugs connus du SaaS, à corriger avant Phase C
- `00-pilotage/_context/` → historique des sessions de travail

## Disclaimer

Outil d'aide à la décision uniquement. Pas un conseiller en investissement.
Le trading comporte un risque de perte en capital.
