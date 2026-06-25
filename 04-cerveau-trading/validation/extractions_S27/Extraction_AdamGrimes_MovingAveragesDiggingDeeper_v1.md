# Extraction AdamGrimes — Moving Averages: Digging Deeper
**Source :** `bundles/adamgrimes/moving_averages_digging_deeper.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6311 → D6330 · **Page :** https://www.adamhgrimes.com/moving-averages-digging-deeper/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Résultats quantitatifs sur les moyennes mobiles — directement applicable à C1 (Prix) pour calibrer les indicateurs de tendance dans TRADEX-AI (notamment : aucune MM n'est "spéciale", la vraie force est la mean reversion).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D6311 — Aucune moyenne mobile n'est "spéciale" statistiquement
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Grimes a testé des centaines de moyennes mobiles (périodes de 10 à 200, types SMA et EMA). Résultat : les performances sont statistiquement indiscernables entre les périodes 20, 45, 50, 65, 150, 185, 200, 233. "In the data and the results, we cannot distinguish between the different periods of moving averages." Les MM100 et MM200 n'ont aucun statut particulier.
**TRADEX-AI C1** : Ne pas accorder de poids particulier à la MM200 ou MM50 dans l'analyse de tendance de TRADEX-AI. Si des MMs sont utilisées, elles sont interchangeables — le signal provient de la structure prix, pas de la période exacte.
*Catégorie : indicateurs_tendance*

### D6312 — Franchissement de MM : non-tradable comme signal isolé
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Les tests montrent que "Price touching or crossing a moving average does not appear to be a tradable event." Un croisement de MM seul n'a pas d'avantage statistique mesurable. Grimes conclut : "We observe a small effect in stocks when a moving average breaks, but this effect is explainable through mean reversion."
**TRADEX-AI C1** : Dans TRADEX-AI, un croisement de MM ne doit JAMAIS être utilisé seul comme signal d'entrée. Il peut être un contexte secondaire, mais l'avantage statistique réel provient d'ailleurs (structure, momentum Belkhayate).
*Catégorie : indicateurs_tendance*

### D6313 — Le vrai edge autour des MMs est la mean reversion, pas les MMs elles-mêmes
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Grimes démontre que l'edge observé lors des "breakouts" de MM n'est pas dû à la MM elle-même. Il reproduit le test SANS la MM (critère seul : close en dessous du bas de la veille) et obtient les mêmes résultats. Conclusion : l'edge est un effet de mean reversion — les closes en dehors du range de la veille tendent à revenir. "This is an expression of mean reversion, which is one of the verifiable, fundamental aspects of price movement."
**TRADEX-AI C1** : L'indicateur de mean reversion (fermeture hors du range précédent) est plus robuste que les croisements de MM. À intégrer comme signal secondaire de retournement potentiel dans la grille de scoring C1.
*Catégorie : structure_marche*

### D6314 — Mean reversion prouve que les actions ne suivent pas une marche aléatoire
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Le test de mean reversion (600 actions, 10 ans) produit un résultat statistiquement significatif positif pour les achats et négatif pour les ventes après une close hors range précédent. "We can say, based on this sample of 600 stocks over the past 10 years, that we find sufficient evidence to reject the random walk hypothesis for equities." Les actions ne suivent pas une marche aléatoire.
**TRADEX-AI C1** : La mean reversion est un phénomène statistiquement réel et exploitable dans les actifs equity/indices (ES). Pour GC, HG, CL, ZW (futures), l'effet est plus faible (voir D6315) — ne pas l'utiliser comme signal primaire sur les futures.
*Catégorie : structure_marche*

### D6315 — Futures et Forex : effet mean reversion très faible, économiquement non significatif seul
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Pour les futures et le forex, la différence statistique de mean reversion est "very, very small" — Futures baseline : 50.6% closes haussières vs 52.6%/47.9% pour les signaux buy/sell. "This is certainly too small to be economically significant on its own." Les futures et forex "consistently tend to more closely approximate random walks than equities."
**TRADEX-AI C1** : Pour GC, HG, CL, ZW (tous des futures), la mean reversion pure via close hors-range est insuffisante comme signal seul. Elle peut contribuer marginalement en combinaison avec d'autres facteurs (Belkhayate, Order Flow C2, COT C3). Ceci valide l'approche multi-cercle de TRADEX-AI.
*Catégorie : gestion_risque_entree*

### D6316 — Test "Fade Break" : vendre la première clôture au-dessus d'une MM = edge négatif en équités
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Les tests de "Moving Average Penetration — Fade Break" sur équités montrent : "sell signals (shorting the first bar that closes above a moving average) show a consistent negative edge, and this edge is statistically significant." Shorter la première clôture au-dessus d'une MM en équités produit un rendement négatif systématique.
**TRADEX-AI C1** : Sur ES (S&P 500, actif de confirmation), ne pas shorter le premier bar qui clôture au-dessus d'une MM. L'effet statistique joue contre cette position. Applicable pour valider ou invalider des setups de confirmation ES dans TRADEX-AI.
*Catégorie : indicateurs_tendance*

### D6317 — Decay du signal buy : hausse initiale puis dégradation en signal négatif à 5-10 jours
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Les signaux "buy on first close below MA" en équités montrent "an initial small positive edge that appears to decay into a negative edge between 5 to 10 days from the signal." L'avantage statistique initial s'érode et devient négatif. Ceci est cohérent dans toutes les capitalisations boursières (large/mid/small cap), donc non attribuable à un outlier.
**TRADEX-AI C1** : Les signaux basés sur des closes sous MA en continuation doivent être gérés avec un horizon court (< 5 jours). Au-delà, la statistique se retourne. Pertinent pour calibrer les durées de position dans le mode Manuel de TRADEX-AI.
*Catégorie : gestion_position_active*

### D6318 — Les assets ne se comportent pas tous de la même façon
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Grimes observe systématiquement que les équités, futures et forex se comportent différemment face aux mêmes indicateurs techniques. "This is the strongest clue we have had so far in these tests that perhaps not all assets trade the same from a quantitative perspective." Il remet en question la croyance que les outils techniques fonctionnent universellement sur tous les actifs.
**TRADEX-AI C1** : Les règles de scoring pour GC, HG, CL, ZW (futures) ne doivent pas être copiées-collées de celles des actions (ES). La calibration doit être spécifique à chaque classe d'actif. Valide la nécessité d'une KB Belkhayate dédiée aux futures.
*Catégorie : structure_marche*

### D6319 — Les closes dans le top/bottom décile du range ont plus de "jus" (rendement)
🟡 **SYNTHÈSE** (Source : moving_averages_digging_deeper.md) : Grimes observe que "stocks tend to have stronger returns following closes in the top and bottom deciles of their range--that's where a lot of the juice is." Les fermetures dans les extrêmes du range quotidien génèrent des rendements plus forts que les closes médianes.
**TRADEX-AI C1** : Pour GC, HG, CL, ZW, privilégier les setups où le close se situe dans les 10% supérieurs ou inférieurs du range de la session. C'est une condition de qualité supplémentaire pour valider un signal Belkhayate avant d'appeler Claude API (Niveau 3).
*Catégorie : gestion_risque_entree*

### D6320 — Conclusions opérationnelles synthétiques sur les MMs
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages_digging_deeper.md) : Grimes liste 4 conclusions directes : (1) Aucune MM n'est "spéciale" (100, 200, etc.) en actions, futures ou devises. (2) Le contact ou croisement d'une MM n'est pas un événement tradable. (3) Le petit effet observé en équités est explicable par la mean reversion. (4) Tous les actifs ne se comportent pas de la même façon — remettre en question l'applicabilité universelle des outils.
**TRADEX-AI C1** : Règle opérationnelle TRADEX-AI : (1) Ne jamais déclencher un signal uniquement sur croisement de MM. (2) Traiter la MM comme contexte de tendance (direction), non comme niveau clé de support/résistance. (3) Appliquer des règles différentes selon que l'actif est un future (GC/HG/CL/ZW) ou un indice (ES).
*Catégorie : indicateurs_tendance*
