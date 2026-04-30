# TRADING-COPILOTE

Système d'aide à la décision de trading basé sur la méthode Belkhayate.

## Ce que c'est

Un SaaS personnel appelé **TRADEX-AI** qui analyse des graphiques TradingView
en temps réel et génère des signaux ACHETER / VENDRE / ATTENDRE selon les
indicateurs Belkhayate (Barycenter, Direction, Énergie, Pivots Sol/Fa/Mi/Ré/Do).

## Méthode

**Belkhayate — intouchable et suivie exactement.**
La méthode s'applique à n'importe quel actif. Le choix des actifs appartient
à l'utilisateur.

## Marchés configurés

| Rôle | Actifs |
|------|--------|
| Trading | Or (GC1!), Cuivre (HG1!), Pétrole (CL1!), Blé (ZW1!) |
| Confirmation | Dollar (DX1!), SP500, VIX |

**Règle d'entrée : 3/4 trading + 2/3 confirmation alignés = signal valide**

## Où en est le projet

1. ✅ Structure et bibliothèque de connaissances (PDFs Belkhayate)
2. 🔄 Scraping YouTube @MostafaBelkhayate (200 vidéos — en cours)
3. ⏳ Extraction règles → Knowledge Base JSON
4. ⏳ Génération 10 skills Belkhayate custom
5. ⏳ Développement TRADEX-AI (SaaS)

## Documents clés

- `CLAUDE.md` → instructions pour Claude Code
- `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` → blueprint technique TRADEX-AI
- `PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md` → spec KB + 10 skills
- `_context/` → historique des sessions de travail

## Structure du projet

```
trading-copilote/
  01-methode-belkhayate/   Principes, timing, gestion du risque
  02-marches-trading/      Or, Cuivre, Pétrole, Blé
  03-marches-confirmation/ Dollar, SP500, VIX
  04-kb-sources/           Sources YouTube et PDFs
  05-skills/               10 skills Belkhayate (à générer)
  06-playbook/             Playbook personnel
  07-tradex-ai/            Blueprint et specs du SaaS
  code/                    Tout le code (Python + React + NestJS)
  _context/                Briefings de session
  _archive/                Fichiers archivés
```

## Disclaimer

Outil d'aide à la décision uniquement. Pas un conseiller en investissement.
Le trading comporte un risque de perte en capital.
