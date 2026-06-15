# 📌 RÈGLE À COLLER UNE SEULE FOIS DANS `CLAUDE.md` (racine)

> **Quoi faire :** ouvre `C:\trading-copilote\CLAUDE.md`, et **colle le bloc ci-dessous** dans la section des règles permanentes de Cowork. Tu ne le refais **jamais** ensuite.

---

```markdown
## 🧠 RÈGLE D'ENRICHISSEMENT DU CERVEAU (interstice)

À la FIN de chaque mission de `FEUILLE_DE_ROUTE.md`, et AVANT de démarrer la
mission suivante :

1. Lire `00-pilotage/BACKLOG_ENRICHISSEMENTS.md`.
2. S'il existe au moins un ticket à l'état "📥 À TRAITER" :
   - Prendre celui de PLUS HAUTE priorité (P1 avant P2…).
   - Exécuter la chaîne décrite dans `00-pilotage/PIPELINE_ENRICHISSEMENT_KB.md`
     (étapes 3 à 7) pour CE SEUL ticket.
   - Puis reprendre la feuille de route.
3. Sinon, passer directement à la mission roadmap suivante.

DÉPÔT EN COURS DE MISSION :
- Si l'utilisateur dépose une source dans le chat ("Nouvelle source pour le
  cerveau"), ARCHIVER immédiatement via Claude Code (sauvegarde dans
  `02-sources-brutes/` + ajout d'un ticket 📥 dans le backlog), PUIS continuer
  la mission en cours. Le TRAITEMENT complet attend le prochain interstice.

INTERDITS ABSOLUS :
- NE JAMAIS interrompre une mission roadmap en cours pour traiter une source.
- NE JAMAIS modifier `FEUILLE_DE_ROUTE.md` lors d'un enrichissement.
- NE JAMAIS écrire dans `04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json` sans
  passer par `04-cerveau-trading/validation/` + audit automatique réussi.
- Traiter UN SEUL ticket par interstice.
- Cowork écrit les PROMPTS ; Claude Code EXÉCUTE tout (fabrication, audit,
  fusion, commit Git).
```

---

**Vérification après collage :** demande à Cowork
> « Relis ton CLAUDE.md et résume-moi la règle d'enrichissement du cerveau. »
S'il te la restitue correctement, c'est en place.
