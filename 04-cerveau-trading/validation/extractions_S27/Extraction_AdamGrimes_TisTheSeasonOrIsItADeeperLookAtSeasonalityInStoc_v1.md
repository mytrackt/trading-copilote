# Extraction AdamGrimes — 'Tis the Season or Is It? A Deeper Look at Seasonality in Stocks
**Source :** `bundles/adamgrimes/tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md` (HTTP 200) + 0 images certifiées
**Méthode images :** N/A · 0/0 certifiées · 0 à vérifier
**Décisions :** D7011 → D7022 · **Page :** https://www.adamhgrimes.com/tis-the-season-or-is-it-a-deeper-look-at-seasonality-in-stocks/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Saisonnalité boursière — forces et limites pour filtrer les signaux macro (ES/DX/GC) selon mois/décennie.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D7011 — Décembre statistiquement le mois le plus positif (long terme)
🟢 **FAIT VÉRIFIÉ** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Sur ~90 ans de données US, décembre est le mois le plus régulièrement positif, avec une surperformance constante par rapport à la moyenne mensuelle, à l'exception des années 1930.
**TRADEX-AI C4** : Pour ES (S&P500 confirmation), un signal long en décembre bénéficie d'un biais saisonnier favorable historique — contexte macro favorable, non décisif seul.
*Catégorie : saisonnalite*

### D7012 — Novembre aussi fort que Décembre dans les données récentes
🟢 **FAIT VÉRIFIÉ** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Sur les 20-30 dernières années, novembre présente une performance au moins équivalente à décembre. Les données récentes montrent novembre stable et fort, parfois supérieur à décembre.
**TRADEX-AI C4** : Fenêtre novembre–décembre constitue une double période favorable pour ES. À intégrer dans la couche C4 (macro/saisonnier) comme contexte de confirmation long.
*Catégorie : saisonnalite*

### D7013 — Septembre : le pire mois boursier de façon persistante
🟢 **FAIT VÉRIFIÉ** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Septembre est décrit comme "an absolute bloodbath" pour le marché actions sur l'ensemble des décennies analysées. L'effet négatif de septembre dépasse en magnitude l'effet positif de décembre.
**TRADEX-AI C4** : En septembre, le biais saisonnier ES est négatif. Signal court sur ES renforcé statistiquement ; signal long sur GC possible si corrélation refuge inverse ES est activée (C7).
*Catégorie : saisonnalite*

### D7014 — Juin persistamment faible en données récentes (phénomène nouveau)
🟡 **SYNTHÈSE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Juin est persistamment rouge dans les décennies récentes selon les deux métriques (fréquence et amplitude), mais l'auteur note que cela semble être un phénomène récent, absent des données plus anciennes.
**TRADEX-AI C4** : Biais saisonnier négatif pour ES en juin — à pondérer avec prudence car la persistance historique longue est limitée. Signal court ES en juin : contexte macro légèrement défavorable.
*Catégorie : saisonnalite*

### D7015 — Ajustement par rapport à la moyenne de la décennie (méthode relative)
🔵 **ÉCOLE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Pour isoler l'effet saisonnier réel, soustraire la performance mensuelle moyenne de la décennie à la performance du mois étudié. Cela élimine le biais des décennies globalement haussières ou baissières.
**TRADEX-AI C4** : Méthode correcte pour calibrer les filtres saisonniers dans TRADEX. Un mois "positif" dans une décennie très haussière n'est pas équivalent à un mois positif dans une décennie neutre.
*Catégorie : saisonnalite*

### D7016 — La saisonnalité ne prédit pas l'avenir avec certitude
🟢 **FAIT VÉRIFIÉ** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : "past performance is not indicative of future results" est présenté comme une vérité fondamentale des marchés financiers, pas seulement une obligation légale. La saisonnalité donne un biais probabiliste, jamais une certitude.
**TRADEX-AI C4** : Les filtres saisonniers dans TRADEX ne bloquent/ne déclenchent jamais seuls un signal. Ils contribuent à la grille /10 comme contexte de probabilité relative, non comme déclencheur.
*Catégorie : saisonnalite*

### D7017 — Donner priorité aux données récentes (20-30 ans) sur l'historique long
🟡 **SYNTHÈSE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : L'auteur recommande de regarder l'historique long mais de pondérer fortement les 20-30 dernières années. Si les données récentes diffèrent de l'historique, donner le bénéfice du doute aux données récentes. Si une tendance persiste sur longue période malgré les changements structurels, l'accepter comme potentiellement stable.
**TRADEX-AI C4** : Pour calibrer les paramètres saisonniers de TRADEX, priorité aux données 2000-2025 sur les données 1930-2000. Cohérent avec l'approche "recent data first" de la méthode Belkhayate.
*Catégorie : saisonnalite*

### D7018 — Analyser fréquence ET amplitude des mouvements saisonniers
🔵 **ÉCOLE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : Deux dimensions à analyser : (1) pourcentage de mois positifs (fréquence binaire) ; (2) rendement moyen mensuel (amplitude). Un mois peut avoir beaucoup de petits gains régulièrement annulés par de grandes perses rares — la fréquence seule est trompeuse.
**TRADEX-AI C4** : Double vérification requise pour tout filtre saisonnier : cohérence entre fréquence et amplitude. Un biais saisonnier n'est robuste que si les deux métriques pointent dans le même sens.
*Catégorie : saisonnalite*

### D7019 — Question clé : combien de données historiques sont suffisantes ?
⚫ **HYPOTHÈSE PROJET** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : L'auteur pose la question ouverte : trop d'historique risque d'inclure des régimes de marché obsolètes ; trop peu manque de robustesse statistique. Il n'y a pas de réponse universelle ; le jugement doit combiner profondeur historique et pertinence contemporaine.
**TRADEX-AI C4** : Pour les actifs TRADEX (GC, HG, CL, ZW), déterminer individuellement la période de référence saisonnière optimale. GC et CL peuvent nécessiter des périodes différentes de ZW en raison de changements structurels distincts.
*Catégorie : saisonnalite*

### D7020 — Le "Santa Claus Rally" dépasse le seul mois de décembre
🟡 **SYNTHÈSE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : L'auteur annonce que le "Santa Claus rally" ne se limite pas à décembre — une nuance développée dans un article ultérieur. Novembre étant au moins aussi fort, la fenêtre de biais haussier est plus large.
**TRADEX-AI C4** : La fenêtre saisonnière favorable pour ES s'étend probablement sur novembre–décembre voire au-delà. Éviter de restreindre le filtre saisonnier haussier au seul mois de décembre.
*Catégorie : saisonnalite*

### D7021 — Signification statistique requise avant d'utiliser un pattern saisonnier
🔵 **ÉCOLE** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : L'auteur signale qu'il abordera la signification statistique dans un article suivant, sous-entendant qu'un pattern saisonnier visible n'est pas utilisable sans vérification statistique formelle.
**TRADEX-AI C4** : Tout filtre saisonnier intégré à TRADEX doit être statistiquement significatif (p < 0,05 minimum). L'aspect visuel des patterns ne suffit pas.
*Catégorie : saisonnalite*

### D7022 — Risque de voir des patterns là où il n'y en a pas (data snooping)
🟢 **FAIT VÉRIFIÉ** (Source : tis_the_season_or_is_it_a_deeper_look_at_seasonality_in_stoc.md) : L'auteur signale explicitement le risque de "seeing patterns where none exist" (data snooping / overfitting). Multiplier les questions sur un même dataset augmente mécaniquement la probabilité de faux positifs.
**TRADEX-AI C4** : Garde-fou contre le data snooping : tout pattern saisonnier doit survivre à un test out-of-sample avant intégration dans la KB TRADEX. Un pattern observé sur une seule décennie ne qualifie pas.
*Catégorie : saisonnalite*
