# README DE TRANSITION — TRADEX-AI
**Date :** 14/06/2026 | **Session :** S08 | **Mode :** Claude Code

---

## 1. ÉTAT ACTUEL DU PROJET

110 transcrits Whisper Belkhayate audités/étiquetés (0 hallucination, 108 VALIDE / 2 A_VERIFIER).
Docs incohérents nettoyés (/21→/10, screenshot→JSON NT8, 5/8→3/4+2/3). Verdict coefficients COG figé
depuis le transcrit officiel "Belkhayate Gravity Center User Guide" et **appliqué dans `COGParams`**
(période 180, ordre 3, coeffs 0,618/1,618). 8/8 tests Belkhayate verts. Tout poussé sur `main`
(remote à jour, 0 commit en attente). Mode AUTO toujours **bloqué**, KB toujours **provisoire**,
Énergie toujours **non codée**. Aucun signal réel possible (KB à reconstruire).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit |
|---|---|---|
| Audit qualité 110 transcrits | `AUDIT_QUALITE.md` + `MANIFESTE_TRANSCRITS.csv` (108 VALIDE / 2 A_VERIFIER) | 116cdd4 |
| Correction règle source + registre | dossier=source Belkhayate, retrait marqueur v2.1, chiffres registre | b25fbe4 |
| Nettoyage cohérence docs | MASTER/MODULES/APPORTS/GARDE_FOUS/BACKLOG → /10, JSON NT8, 3/4+2/3 ; sources douteuses annotées | d57ae30 |
| Verdict coeffs COG | 0,8618 = FAUX ; vrais 1,618/0,618, période 180, ordre 3, repaint confirmé | e02186a, 53cc231 |
| **Correctif `COGParams`** | période 180, ordre 3, coeffs (0.618, 1.618) + `K_BANDS_COMMUNAUTE`=(2.618,4.236) [HYPOTHESE non utilisée] | **103c77f** |

---

## 3. MISSION SUIVANTE

1. **Phase B-02** : reconstruction de la KB canonique depuis les vrais transcrits Belkhayate (110 dispo).
2. **Énergie** : valider/coder depuis les transcrits (aujourd'hui stub `NotImplementedError`).
3. **Backtester** params COG (180/ordre 3/coeffs) — confirmés sur PÉTROLE uniquement, à valider GC/HG/ZW.
4. Vérifier/intégrer les **2 transcrits A_VERIFIER** ("Video 2", "Video 10") avant entrée KB.
5. Décider du **versioning des 110 transcrits** (untracked actuellement) : commit comme matière brute ou .gitignore.
6. **Phase C** : collecteurs data NT8/ATAS (`cot_data.json` etc.). **Phase E** : `prompt_builder.py`.

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| S08-1 | Coeffs COG depuis transcrit "Gravity Center User Guide" : 1,618 (trad.) + 0,618 (pétrole) ; 2,618/4,236 = NON-Belkhayate (communauté) | 🔒 |
| S08-2 | `COGParams` par défaut = période 180, ordre 3, k=(0.618,1.618) — params marqués `[BELKHAYATE-CONFIRME]`, structure reste `[RECONSTRUCTION]` | 🔒 |
| S08-3 | Provenance transcrits = dossier (chaîne officielle Belkhayate) ; 41/110 ont un titre sans 'Belkhayate' mais restent Belkhayate | 🔒 |
| S08-4 | GUIDE MAÎTRE 0,8618 confirmé FAUX (banni comme source de coeffs) | 🔒 |

---

## 5. DÉCISIONS TEMPORAIRES (à valider/backtester)

| # | Décision temporaire | Condition de levée |
|---|---|---|
| T1 | COG : couleur = signe de la pente à l'endpoint | Valider contre transcrits |
| T2 | Timing : normalisation `((pos×2)−1)×10` | Valider contre transcrits |
| T3 | COG defaults (180/ordre 3/0,618-1,618) = décrits pour PÉTROLE (range bars 5 ticks) | Backtest GC/HG/ZW |
| T4 | Grille /10 : seuils 7,0 / 5,0, pondérations | Backtest |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🔴 P0 | KB invalide (synthèses NotebookLM) → reconstruire depuis transcrits avant tout signal réel | OUI (trading réel) |
| 🟡 P1 | Énergie non codée (conflit MFI 20/80 vs proxy ATR/volume non tranché) | OUI (trading réel) |
| 🟡 P1 | Formules COG/Timing [RECONSTRUCTION] non validées ; params COG confirmés sur pétrole seulement | OUI (trading réel) |
| 🟡 P1 | 2 transcrits A_VERIFIER (0 terme Belkhayate détecté) | NON |
| 🟡 P1 | `prompt_builder.py` absent → `get_signal` toujours en fallback (Phase E) | NON (Auto bloqué) |
| ⚪ Info | 110 transcrits untracked + `.claude/settings.json` modifié non commités | NON |
| 🟡 P2 | Collecteurs data NT8/ATAS absents (`cot_data.json`) → Phase C | NON |

---

## 7. ÉTAT DES REPOS FIN SESSION

```
HEAD            : 103c77f (fix COGParams) — poussé sur origin/main
Commits en attente : aucun (origin/main..HEAD vide)
Working tree    : .claude/settings.json modifié + 110 transcrits untracked (non commités, à décider)
.env            : ignoré ; aucune clé API en dur (os.getenv)
```

---

## 8. PRE-FLIGHT SESSION SUIVANTE (S09)

1. Lire `CLAUDE.md` EN ENTIER (score /10)
2. Lire CE fichier (`README_TRANSITION_TRADEX_S08_20260614.md`)
3. Lire `00-pilotage\REGISTRE_VALIDITE.md` (statuts fiabilité + §7 nettoyage)
4. Décider versioning des 110 transcrits (commit matière brute ou .gitignore)
5. Choisir : Phase B-02 (reconstruction KB) prioritaire

---

## 9. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « Je reprends TRADEX-AI session S09. Lis CLAUDE.md + README_TRANSITION_TRADEX_S08_20260614.md +
> REGISTRE_VALIDITE.md. Décisions verrouillées : JSON NT8, port 36973, BTC/Yen = référence zéro ordre,
> score /10, précondition 3/4+2/3, Énergie non codée, mode AUTO bloqué, KB provisoire.
> `COGParams` est figé : période 180, ordre 3, coeffs 0,618/1,618 (confirmés sur PÉTROLE, à backtester
> GC/HG/ZW) ; 2,618/4,236 = non-Belkhayate (K_BANDS_COMMUNAUTE, non utilisé). 110 transcrits Belkhayate
> audités (108 VALIDE / 2 A_VERIFIER). Ordre des missions S09 : (1) décider versioning des 110 transcrits ;
> (2) Phase B-02 reconstruction KB canonique depuis les transcrits ; (3) valider/coder l'Énergie ;
> (4) backtester params COG ; (5) Phase C collecteurs data NT8/ATAS. »

---

*README_TRANSITION_TRADEX_S08_20260614.md — fin session S08*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
