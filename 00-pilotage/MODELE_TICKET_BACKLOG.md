# 🎫 MODÈLE DE TICKET — pour `BACKLOG_ENRICHISSEMENTS.md`

> ⚠️ **Tu as déjà un `BACKLOG_ENRICHISSEMENTS.md` dans `00-pilotage`.**
> **NE PAS l'écraser.** Copie seulement les blocs ci-dessous *à l'intérieur*, s'ils n'y sont pas déjà.

---

## Légende des états (à coller en haut du backlog)

```markdown
## États : 📥 À TRAITER · 🔍 PLAN PROPOSÉ · ⚙️ EN EXÉCUTION · ✅ AUDIT AUTO · 🔀 À FUSIONNER · 🟢 INTÉGRÉ
## Priorité : P1 (haute) → P3 (basse). Cowork traite P1 d'abord, 1 ticket par interstice.
```

---

## Format d'une ligne-ticket (un tableau simple)

```markdown
| Prio | Source (fichier dans 02-sources-brutes) | État | Briques | Note |
|------|------------------------------------------|------|---------|------|
| P1   | playbook/Chap5-6_DOM_ordres.md           | 📥   | —       | sections DOM + types d'ordres |
| P2   | methode-belkhayate/note_geometrie.md     | 📥   | —       | — |
| P3   | kb-sources/transcript_yt_042.txt         | 📥   | —       | — |
```

- **Prio** : tu mets P1/P2/P3 au dépôt.
- **État** : mis à jour **automatiquement** par Claude Code (tu ne touches pas).
- **Briques** : nombre rempli après le plan.
- **Note** : 3-4 mots pour t'y retrouver.

---

## Exemple d'un ticket qui a fini son cycle

```markdown
| P1 | playbook/Chap5-6_DOM_ordres.md | 🟢 | 14 | fusionné le 15/06, commit "KB: DOM+ordres" |
```

---

**Comment tu l'utilises au quotidien :** en pratique, tu ne remplis presque rien à la main. Tu déposes la source dans le chat Cowork → Claude Code **crée la ligne tout seul** à l'état 📥 et **fait évoluer l'état** jusqu'à 🟢. Ce modèle sert surtout de **référence** pour que tout le monde (toi, Cowork, Claude Code) parle le même langage.
