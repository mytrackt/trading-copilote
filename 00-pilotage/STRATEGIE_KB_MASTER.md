# STRATÉGIE KB MASTER — TRADEX-AI
> Transformer les vidéos YouTube en méthode maître structurée et fiable
> Version 1.0 — 12/06/2026 — Remplace toute KB précédente

---

## CONSTAT DE DÉPART (vérité établie)

| Source actuelle | Réalité | Action |
|----------------|---------|--------|
| 142 `whisper_*.txt` | Synthèses NotebookLM (IA) — pas des transcriptions | ❌ SUPPRIMER |
| 6 PDFs `methode-belkhayate\` | Générés par `generateur-prompts-pro` (IA) — pas officiels | ❌ SUPPRIMER |
| `KNOWLEDGE_BASE_MASTER.json` | Haiku extrait depuis synthèses IA → double hallucination | ❌ SUPPRIMER |
| Chaîne YouTube `@MostafaBelkhayate` | Source primaire RÉELLE et vérifiable | ✅ À UTILISER |
| PDFs achetés directement chez Belkhayate | Source primaire si disponibles | ✅ À UTILISER |

---

## ARCHITECTURE DE LA NOUVELLE KB (3 COUCHES)

```
┌─────────────────────────────────────────────────────────────┐
│  COUCHE 1 — RÈGLES MATHÉMATIQUES (code Python pur)          │
│  BGC, Direction, Energie, Pivots = FORMULES, pas du texte   │
│  → Ne PAS mettre dans KB JSON → coder dans 05-saas\engine\  │
├─────────────────────────────────────────────────────────────┤
│  COUCHE 2 — MÉTHODE BELKHAYATE (sources YouTube + PDFs)     │
│  Timing, cassures, pullbacks, confirmation multi-actifs     │
│  → Source UNIQUE : vidéos @MostafaBelkhayate + PDFs payants  │
├─────────────────────────────────────────────────────────────┤
│  COUCHE 3 — SAVOIR UNIVERSEL (autres chaînes vérifiées)     │
│  Gestion risque, Volume/OI/COT, Psychologie, Macro          │
│  → Sources : grandes chaînes + documentation officielle CME/CFTC │
└─────────────────────────────────────────────────────────────┘
```

### Règle absolue de séparation
- Couche 1 : jamais dans KB JSON
- Couche 2 : ne mélanger AUCUNE autre méthode
- Couche 3 : ne jamais faire passer pour Belkhayate-spécifique

---

## SCHÉMA DE RÈGLE (format unique obligatoire)

```json
{
  "id": "BLK-C2-timing-0042",
  "couche": 2,
  "categorie": "timing",
  "sous_categorie": "entree_cassure",
  "texte": "Attendre la cassure ET le retour au niveau avant d'entrer.",
  "actifs": ["GC", "CL", "tous"],
  "source_type": "youtube",
  "source_url": "https://www.youtube.com/watch?v=XXXXXXXXX",
  "source_titre": "Trading Live sur l'Or avec Mostafa Belkhayate",
  "source_timestamp": "00:14:32",
  "verbatim": "ce n'est qu'à partir de là que s'il revient casser encore une fois c'est là que vous rentrez",
  "belkhayate_specifique": true,
  "confirme_multi_source": false,
  "confiance": "haute",
  "validated_by_human": false,
  "date_extraction": "2026-06-12"
}
```

**Règle d'or anti-hallucination :** `verbatim` obligatoire. Pas de verbatim = règle rejetée.

---

## PIPELINE TECHNIQUE (5 PHASES)

### PHASE 0 — Inventaire et tri des URLs (1 session)

**Objectif :** constituer 2 listes d'URLs vérifiées.

**Liste A — Belkhayate only (Couche 2)**
- Source : chaîne YouTube officielle `@MostafaBelkhayate`
- Critère d'inclusion : vidéo où Belkhayate enseigne sa méthode
- Critère d'exclusion : interviews, Q&A sans contenu technique, publicités

**Liste B — Savoir universel (Couche 3)**
- Sources : grandes chaînes (millions d'abonnés) sur futures, gestion risque, volumes
- Critère d'inclusion : compatible actifs GC/HG/CL/ZW/ES/VX, pas contradictoire Belkhayate
- Critère d'exclusion : Forex uniquement, crypto, scalping agressif

**Livrable :** `00-pilotage\SOURCES_KB.xlsx` avec URL, titre, chaîne, couche assignée

---

### PHASE 1 — Transcription réelle (yt-dlp)

**Outil :** `yt-dlp` — récupère les sous-titres NATIFS de YouTube (pas d'IA intermédiaire)

**Commande pour une vidéo :**
```powershell
yt-dlp `
  --write-sub `
  --write-auto-sub `
  --sub-lang fr `
  --sub-format srt `
  --convert-subs srt `
  --skip-download `
  --output "03-transcriptions\transcripts-bruts\%(id)s_%(title)s.%(ext)s" `
  "URL_YOUTUBE"
```

**Commande pour toute une playlist / chaîne :**
```powershell
yt-dlp `
  --write-sub --write-auto-sub `
  --sub-lang fr --sub-format srt --convert-subs srt `
  --skip-download `
  --output "03-transcriptions\transcripts-bruts\%(id)s.%(ext)s" `
  "https://www.youtube.com/@MostafaBelkhayate/videos"
```

**Important :** si sous-titres manuels disponibles → priorité automatique (précision 99%+).
Si seulement auto-générés → précision 85-95% — acceptable, traçable, vérifiable.

**Validation Phase 1 :**
```
✅ Fichier .srt créé pour chaque vidéo
✅ Titre + ID YouTube conservés dans le nom de fichier
✅ Langue FR confirmée
✅ status.json mis à jour avec URL + date téléchargement
```

---

### PHASE 2 — Extraction structurée (Sonnet, un fichier à la fois)

**Modèle :** `claude-sonnet-4-6` — jamais Haiku pour cette étape

**Prompt d'extraction (anti-hallucination) :**
```
Tu es un expert de la méthode Mustapha Belkhayate.
Voici le transcript SRT de la vidéo "[TITRE]" ([URL]).

RÈGLES STRICTES :
1. Extraire UNIQUEMENT les règles de trading clairement énoncées
2. Pour chaque règle, copier le verbatim exact du transcript (obligatoire)
3. Si tu ne trouves pas le verbatim = NE PAS créer la règle
4. Ne pas reformuler, ne pas interpréter, ne pas compléter
5. Catégories autorisées : timing, cassure, pullback, confirmation, gestion_risque, 
   psychologie, indicateurs_belkhayate, correlations, macro

Format JSON strict par règle :
{
  "texte": "[règle en 1-2 phrases]",
  "categorie": "[catégorie]",
  "verbatim": "[copie exacte du transcript]",
  "timestamp": "[HH:MM:SS du SRT]",
  "actifs": ["GC"|"HG"|"CL"|"ZW"|"ES"|"VX"|"tous"]
}

Retourner un tableau JSON. Rien d'autre.
```

**Traitement :** 1 vidéo → 1 fichier JSON intermédiaire → revue humaine → fusion KB

---

### PHASE 3 — Validation humaine (checkpoint obligatoire)

**Protocole :** pour chaque lot de 10 vidéos extraites :

```
1. Abdelkrim lit 20 règles tirées au sort
2. Pour chaque règle : vérifier que le verbatim correspond à ce qu'il a entendu
3. Taux de rejet acceptable : < 10%
4. Si > 10% → revoir le prompt d'extraction avant de continuer
```

**Grille de validation :**
| Critère | OUI | NON |
|---------|-----|-----|
| Verbatim reconnaissable comme Belkhayate | | |
| Règle applicable à GC/CL/ZW/HG | | |
| Pas de généralisation abusive | | |
| Pas d'invention de formule | | |

---

### PHASE 4 — Cross-validation et déduplication

**Étape 4.1 — Cross-validation entre vidéos**
Une règle mentionnée dans ≥ 2 vidéos différentes = `"confirme_multi_source": true`
Indicateur de fiabilité maximum.

**Étape 4.2 — Déduplication intelligente**
Deux règles = même concept exprimé différemment → garder les 2 avec lien entre elles.
Deux règles = contenu identique → garder celle avec le verbatim le plus clair.

**Étape 4.3 — Scoring final de confiance**
| Critère | Points |
|---------|--------|
| Verbatim présent | +3 |
| Confirmé dans ≥ 2 vidéos | +2 |
| Validé humainement | +2 |
| Compatible Belkhayate officiel (belkhayate.net) | +1 |
| **Total max** | **8** |

Confiance : 7-8 = haute / 4-6 = moyenne / < 4 = faible (ne pas utiliser en mode AUTO)

---

### PHASE 5 — Construction KB finale

**Cibles volumétriques réalistes :**
- Couche 2 (Belkhayate) : 200-400 règles de haute qualité
- Couche 3 (Universel) : 100-200 règles complémentaires
- Total KB : 300-600 règles (vs 2337 non fiables actuellement)

**Structure finale :**
```
04-cerveau-trading\
  KNOWLEDGE_BASE_MASTER.json      ← KB principale (Couche 2 + 3)
  KB_SOURCES_LOG.json             ← Traçabilité de chaque règle
  KB_VALIDATION_REPORT.md         ← Rapport de validation humaine
  processor_status.json           ← État du pipeline
```

---

## SOURCES ADDITIONNELLES VÉRIFIÉES (Couche 3)

### Documentation officielle (zéro hallucination possible)
| Source | Contenu | URL |
|--------|---------|-----|
| CME Group Education | Volume, OI, contrats futures | cmegroup.com/education |
| CFTC COT Reports | Positionnement institutionnel | cftc.gov/reports |
| TradingView scripts | Indicateurs Belkhayate implémentés | tradingview.com/scripts/belkhayate |
| NinjaTrader Forum | BGC implémentation technique | forum.ninjatrader.com |

### Chaînes YouTube (Couche 3 seulement — à confirmer avec URLs)
Critères d'acceptation :
- Trader identifié avec bilan vérifiable
- Contenu sur futures (pas uniquement Forex)
- Compatible approche Belkhayate (pas contradictoire)

---

## OBSTACLES ANTICIPÉS ET MESURES CORRECTIVES

| Obstacle | Probabilité | Mesure corrective |
|----------|-------------|-------------------|
| Vidéos sans sous-titres FR | Moyenne | Utiliser Whisper RÉEL (pip install openai-whisper) sur l'audio téléchargé |
| Sous-titres auto de mauvaise qualité | Faible (FR bien reconnu) | Validation humaine Phase 3 détecte les erreurs |
| Vidéos supprimées / inaccessibles | Faible | Log dans status.json, passer à suivante |
| Règles contradictoires entre vidéos | Probable | Garder les 2 + ajouter champ `contradictions` |
| Volume trop faible (< 150 règles) | Possible | Ajouter Couche 3 (autres chaînes) |

---

## PLAN D'EXÉCUTION (séquence sessions)

| Session | Tâche | Durée estimée |
|---------|-------|---------------|
| S06-A | Phase 0 : Abdelkrim fournit URLs → tri en listes A et B | 30 min |
| S06-B | Phase 1 : Pipeline yt-dlp + script d'extraction batch | 1h |
| S07 | Phase 2 : Extraction Sonnet (lot 1 — 20 vidéos Belkhayate) | 2h |
| S08 | Validation humaine Phase 3 + corrections prompt | 1h |
| S09 | Phase 2 suite + Phase 4 déduplication | 2h |
| S10 | Phase 5 : KB finale + tests moteur | 1h |

---

## COMMANDE ROLLBACK

Si la nouvelle KB s'avère problématique :
```powershell
# Restaurer l'ancienne KB (conservée en archive)
Copy-Item "04-cerveau-trading\_archive\KNOWLEDGE_BASE_MASTER_v1.json" `
          "04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json" -Force
```

---

*Source de vérité pour la reconstruction KB — Version 1.0 — 12/06/2026*
*Ne pas modifier sans valider avec Abdelkrim*
