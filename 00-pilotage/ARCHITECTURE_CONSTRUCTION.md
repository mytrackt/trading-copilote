# ARCHITECTURE DE CONSTRUCTION — TRADEX-AI v2
> Version corrigée post-audit (9 corrections intégrées) — Session S30 — 26/06/2026
> **RÈGLE** : Décisions par Cowork → Claude Code enregistre sur instruction → jamais autonome.

---

## PRINCIPE FONDATEUR

> Un module = un fichier = un sous-agent focalisé.
> Aucun module ne démarre sans que ses prérequis soient vérifiés.
> Chaque module a sa propre branche Git, son rollback, sa limite de taille.

---

## COUCHE 1 — GOUVERNANCE (fichiers maîtres)

| Fichier | Rôle | Taille max | Qui modifie |
|---|---|---|---|
| `CLAUDE.md` | Index court — pointe vers tout | 60 lignes | Cowork uniquement |
| `DECISIONS_VEROUILLEES.md` | Registre daté de toutes les décisions | Illimitée | Cowork uniquement |
| `FEUILLE_DE_ROUTE.md` | Phases + missions + état | 200 lignes | Cowork uniquement |
| `GARDE_FOUS.md` | 42 garde-fous trading | 150 lignes | Cowork uniquement |
| `DETTE_TECHNIQUE.md` | Bugs connus à réparer | 100 lignes | Cowork ou Claude Code |

**RÈGLE ABSOLUE** : Les décisions viennent toujours de Cowork (débat avec Abdelkrim).
Claude Code enregistre et exécute — jamais de manière autonome sur les fichiers de gouvernance.

---

## COUCHE 2 — MODULES CDC

### Règles communes à tous les modules

- **Taille max** : 200 lignes par fichier MODULE_XX.md
- **Si dépassement** : découper en MODULE_XX_A.md + MODULE_XX_B.md
- **Branche Git** : `feature/module-XX` — jamais directement sur `main`
- **Merge vers main** : seulement après tests verts + validation Abdelkrim
- **Rollback documenté** : chaque module commence par sa section ROLLBACK

### ÉTAPE 0 OBLIGATOIRE avant tout module — Audit du code existant

```
Avant d'écrire ou d'exécuter un module, Claude Code doit :
1. Lire tous les fichiers de 05-saas/ (engine/, config/, utils/, knowledge_base/)
2. Produire un inventaire : ce qui EXISTE déjà vs ce qui EST À CRÉER
3. Soumettre l'inventaire à Abdelkrim (via Cowork) avant de coder quoi que ce soit
4. Jamais reconstruire ce qui existe déjà
```

---

### MODULE 00 — FONDATION

**Objectif** : Base technique sur laquelle tout repose
**Branche** : `feature/module-00`
**Taille cible** : 150 lignes
**Prérequis** :
- ✅ Python 3.11 installé
- ✅ `.env` configuré avec clés API
- ⚠️ **PRÉREQUIS EXTERNE** : NinjaTrader 8 doit être configuré pour exporter les JSON live (flux toutes les 2s). Sans cette configuration, MODULE 00 n'est pas testable.

**Contenu** :
- `config/settings.py` : actifs, seuils, chemins, R/R par instrument
- `engine/data_reader.py` : lecture flux NT8/ATAS JSON
- `engine/staleness_monitor.py` : détection données périmées
- `utils/atomic_writer.py` : écritures atomiques sécurisées
- Création dossier `data/` avec structure correcte

**Rollback** : supprimer `data/` + restaurer `config/settings.py` depuis Git

**Tests** :
- [ ] `python -m py_compile` sur tous les fichiers
- [ ] `data_reader.py` lit un JSON de test sans erreur
- [ ] `staleness_monitor.py` détecte un fichier périmé
- [ ] `settings.py` contient R/R correct (1:2 GC/HG/CL · 1:1,5 ZW)

---

### MODULE 01 — CERVEAU BELKHAYATE

**Objectif** : KB → signaux → 10 prompts → structure signal 15 champs
**Branche** : `feature/module-01`
**Taille cible** : 200 lignes
**GATE BLOQUANT** :
- 🔴 **Attendre fin batch Gemini** (203 vidéos — en cours)
- 🔴 **Attendre fusion KB** (476 extractions S27 → master)
- ✅ MODULE 00 terminé et mergé

**Contenu** :
- `engine/claude_brain.py` : 10 prompts spécialisés (D-S30-3)
- Structure signal 15 champs (D-S30-2)
- Règle 3/4 + 2/3 en pré-filtre (avant appel API)
- Grille /10 Belkhayate (seuil ≥ 7,0)
- Prompt caching : cache_control sur KB (~90% économies)

**Rollback** : restaurer `claude_brain.py` depuis Git (version précédente)

**Tests** :
- [ ] Signal produit sur données de test contient 15 champs
- [ ] Filtre 3/4+2/3 bloque quand conditions non remplies
- [ ] Score /10 cohérent avec les règles Belkhayate
- [ ] Appel API Claude fonctionne avec prompt caching

---

### MODULE 02 — MOTEUR DE RISQUE

**Objectif** : Tous les garde-fous, kill switch, news gate, circuit breaker
**Branche** : `feature/module-02`
**Taille cible** : 180 lignes
**Prérequis** : MODULE 00 terminé
**Parallélisable avec** : MODULE 03 (branches séparées, pas de conflit)

**Contenu** :
- `engine/risk_manager.py` : risque 0,25–0,50% par trade (D-S30-5), suspension auto, revenge trading
- `engine/circuit_breaker.py` : timeout 15s → retry 2x → fallback ATTENDRE
- News gate : blocage 30min avant NFP/FOMC/CPI (timezone ET)
- Kill switch : 7 conditions de blocage total
- Détection comportements dangereux (sur-trading, après-perte)

**Rollback** : restaurer `risk_manager.py` et `circuit_breaker.py` depuis Git

**Tests** :
- [ ] Risque > 0,50% → signal bloqué
- [ ] News gate bloque correctement sur datetime simulé NFP
- [ ] Circuit breaker timeout → fallback ATTENDRE
- [ ] Kill switch bloque toute simulation sur condition déclenchée

---

### MODULE 03 — DASHBOARD FRONTEND

**Objectif** : Interface cockpit de décision — 10 écrans
**Branche** : `feature/module-03`
**Taille cible** : 200 lignes (spec) + fichiers React séparés
**GATE BLOQUANT** :
- 🔴 **"Sujet 1 — Frontend discussion" doit être validé avec Abdelkrim avant tout développement**
- ✅ MODULE 00 terminé

**Stack** : React 18 + Vite + Tailwind 3.4 (local)
**10 écrans** :
1. Décision instantanée (verdict en 5 secondes)
2. Analyse marché (7 Cercles)
3. Opportunité de trade (signal 15 champs)
4. Risque & money management
5. Paper trading (simulation live)
6. Journal des décisions
7. Performance & statistiques
8. Apprentissage & erreurs
9. Configuration & profil risque
10. Audit des signaux

**Rollback** : `git checkout feature/module-03` → supprimer la branche

**Tests** :
- [ ] `npm run build` sans erreur
- [ ] Écran 1 (décision) lisible en moins de 5 secondes
- [ ] Aucun bouton "ordre réel" présent
- [ ] Disclaimer légal visible sur tous les écrans

---

### MODULE 04 — PAPER TRADING & JOURNAL

**Objectif** : Simulation, journal, mémoire opérationnelle, audit post-trade
**Branche** : `feature/module-04`
**Taille cible** : 180 lignes
**Prérequis** : MODULE 01 + MODULE 02 + MODULE 03 terminés

**Contenu** :
- Moteur paper trading : ouvrir/fermer trades simulés, P&L fictif
- `engine/memory_manager.py` (à créer) : 10 mémoires opérationnelles (D-S30-4)
- Journal : 12 champs par décision (date, signal, score, émotion, résultat, erreur…)
- Audit post-trade : comparer scénario prévu vs résultat réel
- Rapport quotidien automatique (prompt 6 — D-S30-3)

**Rollback** : supprimer `memory_manager.py` + restaurer DB depuis backup Git

**Tests** :
- [ ] Trade simulé s'ouvre et se ferme avec P&L calculé
- [ ] Journal enregistre les 12 champs correctement
- [ ] Mémoire opérationnelle persiste entre les sessions
- [ ] Rapport quotidien généré sans erreur

---

### MODULE 05 — PERFORMANCE & STRATEGY LAB

**Objectif** : Stats, apprentissage, anti-répétition erreurs, Strategy Lab
**Branche** : `feature/module-05`
**Taille cible** : 160 lignes
**Prérequis** : MODULE 04 terminé

**Contenu** :
- Statistiques : win rate, profit factor, drawdown, discipline score
- Anti-répétition : 14 types d'erreurs détectées automatiquement
- Strategy Lab (D-S30-6) : fiches avec statuts active/test/suspendue/rejetée
- Rapport hebdomadaire : erreur la plus répétée + correction proposée

**Rollback** : restaurer depuis Git

**Tests** :
- [ ] Win rate calculé correctement sur historique de test
- [ ] Stratégie suspendue automatiquement si dégradation détectée
- [ ] Rapport hebdomadaire généré avec au moins 1 erreur identifiée

---

### MODULE 06 — NT8 AUTO (BLOQUÉ PAR DÉFAUT)

**Objectif** : Connexion NinjaTrader 8 ATI — exécution automatique des ordres
**Branche** : `feature/module-06`
**Taille cible** : 150 lignes
**GATE BLOQUANT** :
- 🔴 MODULE 00 → 05 tous terminés et validés
- 🔴 Paper trading validé sur au moins 4 semaines sans violation de règles
- 🔴 Circuit breaker actif et testé (actuellement INACTIF — voir DETTE_TECHNIQUE.md)
- 🔴 Autorisation explicite d'Abdelkrim session par session

**Contenu** :
- Connexion TCP/IP port 36973 (NT8 ATI)
- Envoi ordres : Buy/Sell/Close avec taille calculée par MODULE 02
- Garde-fous doublés : vérification risque avant CHAQUE ordre
- Log d'exécution irréfutable

**Rollback** : désactiver `AUTO_MODE = False` dans settings.py

---

## COUCHE 3 — AGENTS D'EXÉCUTION

| Agent | Rôle | Ce qu'il ne fait PAS |
|---|---|---|
| **Cowork** | Décide · Débat · Verrouille · Écrit les modules | N'écrit jamais de code |
| **Claude Code principal** | Lit MODULE_XX.md · Build · Test · Commit | Ne modifie pas les fichiers de gouvernance |
| **Sous-agents parallèles** | Tâches indépendantes simultanées (ex: M02 + M03) | Ne travaillent jamais sur la même branche |

### Protocole échec sous-agent
```
1. Sous-agent écrit dans batch_gemini_log.txt : [ERREUR] + détail
2. Stopper immédiatement — ne pas continuer
3. Créer un fichier ROLLBACK_MODULE_XX.md avec état exact
4. Alerter Cowork (Abdelkrim) avant toute reprise
5. Rollback Git si nécessaire : git checkout feature/module-XX -- fichier.py
```

---

## COUCHE 4 — FLUX DE TRAVAIL CORRIGÉ

```
PHASE 0 — GOUVERNANCE (maintenant)
├── Créer DECISIONS_VEROUILLEES.md ✅
├── Créer ARCHITECTURE_CONSTRUCTION.md ✅
├── Alléger CLAUDE.md → index
├── Audit code existant 05-saas/ (inventaire)
└── Recevoir et analyser tous les documents d'Abdelkrim

PHASE 1 — DISCUSSIONS PRÉALABLES (après docs)
├── Sujet 2 : Explication fonctionnement app → validation
└── Sujet 1 : Frontend discussion → décisions design verrouillées

PHASE 2 — FONDATION (après Sujet 2 validé)
├── MODULE 00 (Fondation) — branche feature/module-00
└── MODULE 02 (Risque) — branche feature/module-02 [PARALLÈLE]

PHASE 3 — CERVEAU + INTERFACE (après Sujets 1+2 validés + KB fusionnée)
├── MODULE 01 (Cerveau) — branche feature/module-01
└── MODULE 03 (Frontend) — branche feature/module-03 [PARALLÈLE]

PHASE 4 — SIMULATION (après M01+M02+M03 mergés)
└── MODULE 04 (Paper Trading)

PHASE 5 — APPRENTISSAGE (après M04 mergé)
└── MODULE 05 (Performance + Strategy Lab)

PHASE 6 — AUTO (bien plus tard — toutes conditions remplies)
└── MODULE 06 (NT8 Auto) 🔒
```

---

## COUCHE 5 — SÉCURITÉ DES FICHIERS

| Mécanisme | Détail |
|---|---|
| Git | Commit après chaque module terminé. Rollback toujours possible. |
| Branches | `feature/module-XX` → jamais coder directement sur `main` |
| .env | Jamais commité — vérifié avant tout `git push` |
| CLAUDE.md | Index seulement — ne grossit plus |
| Taille modules | Max 200 lignes — sinon découper |
| Sous-agent échec | Log → rollback → Cowork averti |

---

## INDICATEURS DE SANTÉ DU PROJET

À vérifier à chaque démarrage de session :

```
[ ] CLAUDE.md < 60 lignes ?
[ ] Tous les modules respectent < 200 lignes ?
[ ] Aucune branche feature non mergée depuis > 7 jours ?
[ ] DECISIONS_VEROUILLEES.md à jour ?
[ ] .env dans .gitignore ?
[ ] MODE AUTO = False dans settings.py ?
```

---

*Architecture v2 — Post-audit 9 corrections — Session S30 — 26/06/2026*
*Prochaine révision : après réception de tous les documents d'Abdelkrim*
