# PROMPT CLAUDE CODE — ÉTAPE 7 PIPELINE KB
# Fusion — Ticket 0.b · KB_CHAP5_BELKHAYATE.json → KNOWLEDGE_BASE_MASTER.json · S18 · 2026-06-20

## CONTEXTE

Projet : TRADEX-AI — `C:\trading-copilote\`
Ticket 0.b : audit VALIDE (100 %) → fusionner les 14 briques dans la KB maître.
**Règle absolue** : sauvegarder avant tout. Zéro perte de données.

---

## ÉTAPES À EXÉCUTER (dans cet ordre EXACT)

### 1. Backup obligatoire

```powershell
cd C:\trading-copilote
Copy-Item "04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json" "04-cerveau-trading\KNOWLEDGE_BASE_MASTER.bak_chap5_20260620.json"
```

Vérifier que le .bak existe avant de continuer.

### 2. Lire les deux fichiers

- `04-cerveau-trading\validation\KB_CHAP5_BELKHAYATE.json` → les 14 briques à fusionner
- `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` → la KB maître (à modifier)

### 3. Fusionner les 14 briques

La structure de KNOWLEDGE_BASE_MASTER.json est :
```json
{
  "metadata": {
    "ajouts_manuels": [...]  ← ajouter un bloc ici
  },
  "aggregated_rules": {
    "indicateurs_tendance": [...],   ← ajouter les briques par catégorie ici
    "indicateurs_momentum": [...],
    "gestion_risque_entree": [...],
    "gestion_position_active": [...],
    "structure_marche": [...],
    ...
  }
}
```

**Format d'une règle dans aggregated_rules :**
```json
{
  "regle": "[titre] — [contenu court]",
  "statut": "VALIDE",
  "source": "TRADEX_KB_Chap5_Methode_Belkhayate",
  "type": "[DEFINITION|REGLE|PIEGE]",
  "fiabilite": "[FAIT_STABLE|ECOLE_DE_PENSEE]",
  "id_brique": "[id de la brique source]"
}
```

**Mapping catégorie → aggregated_rules pour les 14 briques :**

| id brique | categorie_kb → clé aggregated_rules | regle (format condensé) |
|-----------|--------------------------------------|-------------------------|
| cog-structure-visuelle | indicateurs_tendance | Structure visuelle COG Belkhayate : ligne médiane bleue + bandes parallèles rouge/verte. Le COG est composé d'une ligne centrale bleue (régression) et de bandes parallèles supports/résistances dynamiques. Bandes les plus éloignées : rouge haut (surachat présumé), verte bas (survente présumée). |
| cog-bandes-nombre-or | indicateurs_tendance | Bandes COG espacées par multiples du nombre d'or (φ ≈ 1,618) — valeur exacte non publiée, deux reconstitutions tierces divergent (nombre d'or vs 3 écarts-types). Ne jamais affirmer une formule exacte. |
| cog-logique-mean-reversion | indicateurs_tendance | Postulat Belkhayate : le prix oscille autour de sa médiane et tend à y revenir (mean reversion). En marché fortement directionnel, le prix peut rester étiré longtemps — la reversion n'est pas une loi universelle. |
| timing-structure-zones | indicateurs_momentum | Belkhayate Timing : oscillateur sous le prix en zones neutre / extrême haute / extrême basse. Zone neutre = ne rien faire. Zone extrême = biais directeur. Nombre de zones variable selon le portage (3 à 5). |
| timing-biais-directionnel | indicateurs_momentum | Biais Timing : zone haute → biais vendeur / zone basse → biais acheteur / zone neutre → attendre. Zone intermédiaire (grise) = signal plus faible, stratégie agressive uniquement. |
| setup-type-confluence | gestion_risque_entree | Setup type Belkhayate : 3 confluences simultanées requises — (1) prix en bande extrême COG, (2) Timing en zone extrême correspondante, (3) chandelier de retournement confirmatoire. Un signal isolé n'est pas utilisé. |
| objectifs-sortie-cog | gestion_position_active | Objectifs Belkhayate : OBJ1 = retour à la médiane (ligne bleue). OBJ2+3 = poursuite vers bandes opposées. Grille d'objectifs pour la sortie progressive d'une position. |
| filtre-tendance-htf | gestion_risque_entree | Filtre tendance HTF : ne prendre que les signaux dans le sens de la tendance de fond (timeframe supérieur). Ajout externe à la méthode native — réduit le risque en tendance forte. |
| confluence-cog-timing-vwap-volume | indicateurs_tendance | Confluence obligatoire futures CME : COG + Timing + VWAP + volume — jamais signal isolé. Sur GC/CL/ZW/HG, le volume tick est réel, contrairement au Forex. Minimum 2 outils en confluence pour valider. |
| piege-repainting-cog | indicateurs_tendance | PIÈGE repainting COG : fenêtre glissante → la courbe se redessine sur le passé. Backtest visuel sur historique = trompeur (trop optimiste). Tester uniquement en forward (temps réel ou démo). |
| piege-biais-reversion-tendance-forte | gestion_risque_entree | PIÈGE méthode réversive en tendance forte : le prix peut rester étiré sans revenir. Un système purement réversif saigne en tendance. Stop-loss obligatoire défini avant toute entrée. |
| piege-versions-tierces-divergentes | indicateurs_tendance | PIÈGE versions tierces divergentes : deux indicateurs nommés Belkhayate peuvent signaler différemment (nombre d'or vs 3 écarts-types). Ne jamais supposer leur équivalence sans vérification. |
| piege-formule-proprietaire | indicateurs_tendance | PIÈGE formule propriétaire : le calcul exact du COG n'est pas public. Toute formule trouvée sur MT4/TradingView est une reconstitution tierce. Ne jamais affirmer connaître la formule exacte de Belkhayate. |
| piege-claims-performance-non-prouves | indicateurs_tendance | PIÈGE claims non prouvés : taux de réussite 80%/90%/95% = arguments marketing sans backtest rigoureux. Le "95%" emprunté aux 2 écarts-types Bollinger ne s'applique pas prouvablement aux bandes Belkhayate. Ne jamais citer ces chiffres. |

### 4. Ajouter le bloc dans metadata.ajouts_manuels

```json
{
  "phase": "S18",
  "ticket": "0.b",
  "source": "TRADEX_KB_Chap5_Methode_Belkhayate.md",
  "couche_kb": 2,
  "statut": "VALIDE",
  "audit_score": "14/14 (100%)",
  "date_integration": "2026-06-20",
  "nb_regles": 14,
  "regles": [
    {"categorie": "indicateurs_tendance", "regle": "Structure visuelle COG Belkhayate..."},
    ...
  ],
  "rules_after": "[valeur avant + 14]"
}
```

### 5. Valider le JSON après modification

```powershell
python -c "import json; f=open('04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json', encoding='utf-8'); kb=json.load(f); total=sum(len(v) for v in kb['aggregated_rules'].values() if isinstance(v, list)); print(f'OK — {total} règles dans aggregated_rules')"
```

Résultat attendu : `OK — [valeur avant + 14] règles dans aggregated_rules`

### 6. Mettre à jour le BACKLOG

Fichier : `00-pilotage\BACKLOG_ENRICHISSEMENTS.md`
Changer `🔀 À FUSIONNER` → `🟢 INTÉGRÉ` pour le ticket 0.b
Ajouter en dessous de la ligne : `→ Integration : 2026-06-20 · 14 briques · commit S18`

### 7. Mettre à jour le REGISTRE_VALIDITE.md

Fichier : `04-cerveau-trading\validation\REGISTRE_VALIDITE.md`
Ajouter après le rapport d'audit :

```markdown
### FUSION — [2026-06-20]
- Briques fusionnées : 14
- Cible : 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json
- Injection dans aggregated_rules : indicateurs_tendance (+8), indicateurs_momentum (+2), gestion_risque_entree (+3), gestion_position_active (+1)
- Backup : KNOWLEDGE_BASE_MASTER.bak_chap5_20260620.json
- Ticket : 0.b → 🟢 INTÉGRÉ
```

### 8. Commit final

```powershell
cd C:\trading-copilote
git add 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json 04-cerveau-trading/validation/REGISTRE_VALIDITE.md 00-pilotage/BACKLOG_ENRICHISSEMENTS.md
git commit -m "feat(KB): integration ticket 0.b Chap5 Belkhayate 14 briques valide"
```

**Ne pas committer le .bak** — il est local uniquement.

### 9. Annoncer à Cowork

```
✅ FUSION TERMINÉE — Ticket 0.b
14 briques intégrées dans KNOWLEDGE_BASE_MASTER.json
Ticket 0.b → 🟢 INTÉGRÉ
Backup : KNOWLEDGE_BASE_MASTER.bak_chap5_20260620.json (local, non commité)
Commit : [hash]
KB mise à jour : [total avant] + 14 = [total après] règles
```

---

## RÈGLES ANTI-HALLUCINATION POUR LA FUSION

1. Copier le contenu des règles EXACTEMENT depuis le tableau ci-dessus — 0 reformulation libre
2. Placer chaque brique dans la BONNE catégorie aggregated_rules (cf. mapping ci-dessus)
3. Vérifier le total avant et après (total avant + 14 = total après)
4. Ne jamais supprimer ou modifier des règles existantes
5. Si le JSON est invalide après modification → restaurer le .bak immédiatement

---

*Généré par Cowork — Session S18 · 2026-06-20 · Pipeline Enrichissement KB Étape 7*
*Audit Étape 6 : 14/14 VALIDE (100%) — commit ba63597*
