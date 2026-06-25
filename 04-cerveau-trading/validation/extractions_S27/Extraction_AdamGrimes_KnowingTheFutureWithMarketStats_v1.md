# Extraction AdamGrimes — Knowing The Future With Market Stats
**Source :** `bundles/adamgrimes/knowing_the_future_with_market_stats.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6191 → D6205 · **Page :** https://www.adamhgrimes.com/knowing-the-future-with-market-stats/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : épistémologie des statistiques de marché — contexte C4/C5 pour éviter les pièges de sur-optimisation dans la KB Belkhayate et la grille de score /10.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6191 — Différence fondamentale : statistiques descriptives vs statistiques prédictives
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : Il faut distinguer deux types de statistiques de marché : (1) celles qui décrivent ce qui vient de se passer (rétrospecitves), et (2) celles qui ont une valeur prédictive sur ce qui va se passer. Les deux sont très différentes. La valeur est dans les secondes.
**TRADEX-AI C4** : Toute règle dans la KB Belkhayate doit être catégorisée selon sa nature : descriptive (éducative, badge 🔵) ou prédictive (actionnable, badge 🟢). Seules les règles prédictives valides alimentent la grille de score TRADEX. Les règles descriptives restent dans la KB mais ne comptent pas dans le calcul du signal.
*Catégorie : structure_marche*

### D6192 — L'histoire du marché est le meilleur guide vers le futur
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : Bien que l'histoire ne se répète pas littéralement, elle "rime". Supposer que "le futur ressemblera à ce qu'on a vu" est un postulat plus raisonnable qu'anticiper quelque chose d'entièrement nouveau. La connaissance historique donne des insights sur le probable futur.
**TRADEX-AI C4** : Ce principe justifie l'existence de la KB Belkhayate (2337+ règles) comme base de décision. L'historique des comportements de GC/CL/ZW/HG sous conditions Belkhayate similaires est le meilleur guide. La KB n'est pas infaillible mais elle est le meilleur proxy disponible.
*Catégorie : structure_marche*

### D6193 — Danger du data mining : chercher jusqu'à trouver quelque chose qui marche
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : Le processus suivant crée une illusion statistique : (1) regarder des stats haut niveau, garder ce qui montre un edge, (2) ajouter des conditions, ne garder que ce qui améliore l'edge, (3) répéter. Le résultat montre souvent un fort edge historique qui n'existe pas en réalité.
**TRADEX-AI C1** : La grille de score TRADEX (/10) doit être construite sur des règles Belkhayate définies a priori, pas sélectionnées a posteriori sur leurs performances passées. Interdit d'ajuster les poids de la grille de score en optimisant sur l'historique sans validation out-of-sample. Risque de sur-optimisation = fausse carte.
*Catégorie : structure_marche*

### D6194 — Un event de 99e percentile ne donne pas automatiquement un edge prédictif
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : L'auteur décrit avoir analysé un move historiquement extrême (top 10 sur des milliers d'événements observés) par plusieurs métriques (volatilité ajustée, pourcentage brut, "surprise" depuis les hauts, bande de Bollinger). Résultat : aucun edge statistique clair dans les jours suivants.
**TRADEX-AI C5** : Règle pour le moteur : une lecture extrême de VX (VIX > 99e percentile) ou un move exceptionnel sur ES n'est PAS automatiquement un signal. Il faut les 3/4 actifs trading + 2/3 confirmation alignés même dans les conditions extrêmes. L'extrémité d'un événement n'est pas un edge en soi.
*Catégorie : macro_evenements*

### D6195 — Facilité de trouver des études contradictoires sur le même événement
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : Sur un même événement de marché, il est facile de trouver des études montrant à la fois une surperformance ET une sous-performance future selon les critères choisis pour le modèle. C'est un signe que le phénomène n'a pas d'edge robuste.
**TRADEX-AI C4** : Dans la KB Belkhayate, si deux règles contradictoires s'appliquent au même contexte, elles s'annulent dans le score TRADEX. Le moteur ne doit pas arbitrairement choisir celle qui confirme un biais. En cas de contradiction, le score est neutre sur ce critère.
*Catégorie : structure_marche*

### D6196 — Comment mesurer un move : plusieurs approches légitimes mais pas équivalentes
🔵 **ÉCOLE** (Source : knowing_the_future_with_market_stats.md) : Mesurer l'amplitude d'un move de marché peut se faire de plusieurs façons : variation en points, variation en pourcentage, variation ajustée à la volatilité (ATR), sur différentes fenêtres temporelles (jour, semaine, 5 jours glissants, swing). Aucune n'est universellement correcte — chaque mesure pose une question différente.
**TRADEX-AI C1** : Pour les actifs TRADEX (GC/HG/CL/ZW), l'Énergie Belkhayate doit être mesurée de façon cohérente et documentée (quelle mesure, quel lookback). Changer la définition de l'Énergie = changer la question posée = risque de comparaisons invalides. La définition doit être figée dans settings.py.
*Catégorie : indicateurs_tendance*

### D6197 — Les mesures de "surprise" (rupture depuis niveau extrême) sont valides
🟡 **SYNTHÈSE** (Source : knowing_the_future_with_market_stats.md) : L'auteur utilise des mesures de "surprise" comme indicateurs statistiques — par exemple un déclin depuis un nouveau plus haut, ou un move rapide depuis le haut vers le bas d'une bande de Bollinger ou Keltner. Ces mesures capturent la nature inattendue d'un move.
**TRADEX-AI C5** : Le VIX (VX) remplit ce rôle de "surprise gauge" dans TRADEX. Une montée soudaine de VX depuis un niveau calme est plus significative qu'un VX élevé stable. Le circuit breaker et le suspend_auto_mode peuvent être déclenchés par la vitesse de montée de VX, pas seulement son niveau absolu.
*Catégorie : indicateurs_momentum*

### D6198 — Moins d'hypothèses = meilleure robustesse dans les conditions extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : knowing_the_future_with_market_stats.md) : Face à un environnement de marché extrême, la conclusion pratique est : "moins on assume, mieux on se porte". Réduire les hypothèses dans des conditions inhabituelles améliore la robustesse de la décision.
**TRADEX-AI C1** : Principe Belkhayate aligné : dans des conditions de marché extrêmes (VIX > seuil critique, news gate actif, circuit breaker déclenché), le fallback TRADEX est ATTENDRE avec confiance max 65%. Réduire les hypothèses = revenir au signal le plus simple et le plus conservateur.
*Catégorie : gestion_risque_entree*

### D6199 — La résolution des questions statistiques dépend des paramètres choisis
🔵 **ÉCOLE** (Source : knowing_the_future_with_market_stats.md) : Pour toute question statistique sur les marchés, les réponses dépendent fortement des choix de paramètres : quelle métrique, quelle fenêtre, comment définir les swings, trading days vs calendar days. Ces choix ne sont pas arbitraires — ils doivent correspondre à la question précise qu'on pose.
**TRADEX-AI C1** : Dans settings.py, tous les paramètres des indicateurs Belkhayate (période COG 180, ordre 3, lookback corrélations 30j, etc.) sont FIGÉS. Ne pas tenter de les optimiser rétrospectivement. Ces paramètres définissent les questions posées au marché — les changer change les questions, pas les réponses.
*Catégorie : structure_marche*
