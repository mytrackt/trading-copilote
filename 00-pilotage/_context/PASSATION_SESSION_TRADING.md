# 📦 PASSATION DE SESSION — TRADEX-AI / trading-copilote

> **But de ce fichier :** transmettre à la session Cowork *trading-copilote* (orchestrateur de la conception de l'app TRADEX-AI) tout le contexte produit dans une session claude.ai. À lire en entier avant toute action.

---

## 1. CONTEXTE GÉNÉRAL

- **Projet :** TRADEX-AI — système de trading assisté par IA (Claude), basé sur la méthode Belkhayate + approches universelles.
- **Workspace :** `C:\trading-copilote`
- **Rôle de Cowork ici :** orchestrer la conception de l'app et de son « cerveau » (base de connaissances).
- **Profil utilisateur :** non-développeur, pédagogie niveau débutant requise, français.

---

## 2. CE QUI A ÉTÉ PRODUIT DANS LA SESSION

### 2.1 Un méta-prompt « Mentor Trader Senior »
- Fichier associé : `PROMPT_Mentor_Trader_Senior_Futures.md`
- Objectif : former l'utilisateur au métier de trader senior (futures, scalping & day trading).
- Fonctionnement : affiche un **sommaire de 14 chapitres**, puis développe **un chapitre à la fois** après validation.
- Réglages choisis : marché = **Futures (indices, matières)** · méthode = **Belkhayate + universelle combinées** · langue = **FR détaillé**.

### 2.2 Avancement de la formation (contenu pédagogique déjà rédigé)
- **Chapitre 1** — Le métier de trader senior ✅
- **Chapitre 2** — Fondamentaux des futures (contrat, ES/NQ/CL/GC, micros, tick & valeur du tick, marge, levier, sessions, liquidité) ✅
- **Chapitre 3** — Brokers & plateformes ✅, avec approfondissements détaillés sur :
  - **Section 5 — DOM / carnet d'ordres** (liquidité au repos, bid/ask/spread, murs/iceberg/spoofing, DOM vs Time & Sales).
  - **Section 6 — Types d'ordres** (marché, limite, stop-market vs stop-limite, MIT, trailing stop, bracket/OCO, ATM Strategy NinjaTrader 8).
- Chapitres 4 à 14 : **non encore développés**.

---

## 3. STRATÉGIE VALIDÉE POUR LE CERVEAU DE TRADEX-AI

Décision clé : **ne jamais coller de la prose de cours brute** dans la base. On transforme le savoir en **briques de connaissance atomiques, typées et vérifiées**.

**Architecture en 3 couches :**
1. Modèle Claude (figé).
2. System prompt (persona + règles dures).
3. Contexte récupéré (RAG / `KNOWLEDGE_BASE_MASTER.json`).

**Règle :** 1 concept = 1 brique.

**Double classement de chaque brique :**
- `type` : `DEFINITION` · `REGLE` · `PIEGE`
- `fiabilite` : `FAIT_STABLE` · `DEPEND_DU_BROKER` · `ECOLE_DE_PENSEE`

**Règles d'industrialisation :**
- Les briques `REGLE` (règles dures de sécurité) vont **AUSSI** dans le system prompt (jamais dépendre de la chance de la recherche).
- Les `DEPEND_DU_BROKER` portent la consigne « vérifier auprès du broker, ne jamais inventer de chiffre ».
- Méta-règle anti-hallucination : le cerveau **explique / vérifie / alerte**, il **ne prédit pas** et **n'émet aucun signal certain**.

**Schéma JSON cible (exemple validé) :**
```json
{
  "id": "ordres-stop-limite-piege",
  "type": "PIEGE",
  "fiabilite": "FAIT_STABLE",
  "domaine": "futures",
  "sujet": "types-ordres",
  "niveau": "debutant",
  "langue": "FR",
  "titre": "Ne jamais utiliser un stop-limite comme stop-loss",
  "contenu": "Un stop-limite devient un ordre limite une fois déclenché : son exécution n'est PAS garantie. Dans une chute rapide, le prix peut sauter par-dessus la limite sans remplir l'ordre, laissant une position perdante non protégée.",
  "regle_associee": "Un stop-loss doit être un stop-AU-MARCHÉ.",
  "mots_cles": ["stop", "stop-limit", "stop-market", "stop-loss"]
}
```

---

## 4. PROCHAINE ACTION EN ATTENTE (à reprendre par Cowork)

➡️ **Transformer les sections 5 (DOM) et 6 (types d'ordres) en ~12–15 briques JSON** au schéma ci-dessus, prêtes à fusionner dans `KNOWLEDGE_BASE_MASTER.json`.

Puis, à terme : faire de même pour chaque chapitre validé de la formation, afin d'enrichir progressivement le cerveau de TRADEX-AI.

---

## 5. GARDE-FOUS À CONSERVER

- Aucune promesse de gain, rappel systématique du risque de perte.
- Contenu = éducatif, **pas un conseil financier ni un signal**.
- Aucun chiffre inventé : valeurs broker/marge/commission marquées `DEPEND_DU_BROKER`.
- Tout test/apprentissage d'abord sur **simulateur (compte démo)**.
