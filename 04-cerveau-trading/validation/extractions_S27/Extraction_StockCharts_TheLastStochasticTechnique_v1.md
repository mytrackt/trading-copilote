# Extraction StockCharts — The Last Stochastic Technique
**Source :** `bundles/stockcharts/the_last_stochastic_technique.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage (src + contexte section) · 4/4 certifiées · 0 à vérifier
**Décisions :** D4431 → D4450 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-last-stochastic-technique.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Technique Stochastique 39 périodes avec confirmation OBV — applicable comme filtre momentum C1 sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/0sHiLz7yWVg96f5St2CF | Slow Stochastic (39,1) sur graphique journalier MSFT — signal haussier %K croise au-dessus de 50 le 14 juin | Stochastic Signals | D4431 |
| /files/eYtgbCkG8kss59a9Movc | Slow Stochastic (39,1) sur graphique hebdomadaire MSFT 3 ans — %K reste au-dessus de 50 pendant plus de 2 ans, cassure sous 50 en février 2000 | Stochastic Signals | D4432 |
| /files/tPY5YCMzoBzLTyID7frT | Slow Stochastic (39,1) sur graphique journalier CSCO — %K au-dessus de 50 de novembre 1999 à avril 2000 avec whipsaws sur les bords | Stochastic Signals | D4433 |
| /files/AIeVLFcHR5w2U1tRyaTN | Slow Stochastic (39,1) + OBV + MA 30j sur CSCO — confirmation OBV novembre 1999, non-confirmation avril 2000, double confirmation juin | Stochastic Signals | D4434 |

## DÉCISIONS

### D4431 — Paramètre clé : Slow Stochastic 39 périodes, signal au croisement de 50
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md, image_0sHiLz7yWVg96f5St2CF) : Une étude publiée dans "The Encyclopedia of Technical Market Indicators" a identifié des signaux de qualité avec un Fast Stochastic 39 périodes. Signal d'achat : %K croise au-dessus de 50 ET le cours de clôture est au-dessus du plus haut de clôture de la semaine précédente. Signal de vente : %K croise en dessous de 50 ET le cours de clôture est en dessous du plus bas de clôture de la semaine précédente.
**TRADEX-AI C1** : Le Stochastique Lent 39 périodes (39,1) est une règle d'entrée précise applicable sur GC/HG/CL/ZW — le seuil 50 comme ligne de partage est directement intégrable comme filtre momentum dans le score /10 du Cercle C1.
*Catégorie : indicateurs_momentum*

### D4432 — Persistance tendance : %K au-dessus de 50 peut durer des années
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md, image_eYtgbCkG8kss59a9Movc) : Sur un graphique hebdomadaire MSFT sur 3 ans, le Slow Stochastic (39,1) est resté au-dessus de 50 pendant plus de 2 ans avant de croiser sous 50 fin février 2000. Les techniques overbought/oversold classiques auraient généré des pertes continues pendant cette tendance.
**TRADEX-AI C1** : Règle critique pour TRADEX-AI : sur GC/CL en tendance forte, ne pas utiliser le Stochastique comme indicateur de retournement (overbought) — le seuil 50 comme signal de continuation est plus fiable que les seuils 80/20 en tendance.
*Catégorie : indicateurs_momentum*

### D4433 — Risque de whipsaws aux extrémités de la tendance
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md, image_tPY5YCMzoBzLTyID7frT) : Sur le graphique journalier CSCO, le Slow Stochastic (39,1) est resté au-dessus de 50 de novembre 1999 à avril 2000 (bonne tendance capturée), mais avec des whipsaws (faux signaux) des deux côtés aux transitions.
**TRADEX-AI C1** : Les whipsaws aux transitions de tendance sur GC/HG/CL/ZW sont un risque connu — le filtre Stochastique 39 périodes seul est insuffisant ; une confirmation supplémentaire est obligatoire (voir D4434 sur OBV).
*Catégorie : indicateurs_momentum*

### D4434 — Règle de confirmation OBV + MA 30j avec le Stochastique
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md, image_AIeVLFcHR5w2U1tRyaTN) : Protocole de confirmation à deux indicateurs : (1) Croisement OBV au-dessus de sa MA 30j en novembre 1999 alors que %K > 50 → signal valide. (2) %K < 50 en avril confirmé par OBV sous sa MA 30j → sortie valide. (3) %K remonte au-dessus de 50 fin avril MAIS OBV ne confirme pas → pas de signal. (4) Les deux repassent haussiers en juin → double confirmation, signal valide.
**TRADEX-AI C2** : Règle de confluence directement applicable : signal TRADEX sur GC/HG/CL/ZW = Stochastique Lent(39,1) %K > 50 ET OBV au-dessus de sa MA 30j. La non-confirmation OBV invalide le signal prix, cohérent avec la règle 2/3 confirmation alignés de TRADEX-AI.
*Catégorie : volume_liquidite*

### D4435 — Problème fondamental des techniques overbought/oversold classiques
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md) : Les techniques Stochastique basées sur les zones overbought (>80) / oversold (<20) produisent des pertes systématiques dans les tendances fortes car elles cherchent le retournement contre la tendance. Cette technique "Last Stochastic" adresse ce défaut en utilisant le seuil 50 comme ligne directionnelle et non les extrêmes 80/20.
**TRADEX-AI C1** : Décision de design : dans TRADEX-AI, si le Stochastique est utilisé pour GC/HG/CL/ZW, utiliser le seuil 50 (directional) et NON les seuils 80/20 (reversal) — les marchés futures en tendance peuvent rester overbought pendant des mois.
*Catégorie : indicateurs_momentum*

### D4436 — Fast vs Slow Stochastic : lissage et réduction des whipsaws
🔵 **ÉCOLE** (Source : the_last_stochastic_technique.md) : Une période longue (39) sans lissage donne le Fast Stochastic dans sa forme la plus pure, mais augmente les whipsaws. Lisser %K avec une SMA 3 périodes produit le Slow Stochastic — réduit les faux signaux au coût d'un léger retard.
**TRADEX-AI C1** : Pour TRADEX-AI, préférer le Slow Stochastic (39,1) sur GC/HG/CL/ZW — le lissage réduit les whipsaws qui génèrent des frais inutiles en trading futures ; la réduction de la réactivité est acceptable car on cible les tendances, pas le scalp.
*Catégorie : indicateurs_momentum*

### D4437 — Adaptation du seuil par actif : certains actifs signalent à 40/60 plutôt que 50
🟢 **FAIT VÉRIFIÉ** (Source : the_last_stochastic_technique.md) : Certains actifs ont montré une tendance à signaler l'entrée quand %K croise au-dessus de 40 (et non 50) et la vente quand %K croise sous 60 — chaque actif est unique et les paramètres doivent être testés spécifiquement sur l'historique de l'actif.
**TRADEX-AI C1** : Le seuil optimal du Stochastique Lent doit être validé par actif dans TRADEX-AI — GC, HG, CL et ZW n'auront pas forcément le même seuil optimal ; ce paramètre doit être testé lors de la Phase C (validation range bars NT8) avant toute intégration dans le score /10.
*Catégorie : indicateurs_momentum*

### D4438 — Confirmation obligatoire pour les actifs volatils
🔵 **ÉCOLE** (Source : the_last_stochastic_technique.md) : Pour les actifs volatils, l'auteur recommande d'utiliser un ou deux indicateurs supplémentaires en confirmation — le Stochastique seul est insuffisant sur les actifs à forte amplitude.
**TRADEX-AI C1** : CL (Pétrole WTI) et HG (Cuivre) sont des actifs particulièrement volatils — pour ces actifs, le signal Stochastique Lent (39,1) doit impérativement être confirmé par au moins un indicateur additionnel (OBV ou CMF) avant d'être intégré dans le score C1.
*Catégorie : gestion_risque_entree*

### D4439 — Timeframe weekly : utilité pour vision long terme
🔵 **ÉCOLE** (Source : the_last_stochastic_technique.md) : Les chartistes avec une vision long terme peuvent utiliser le Stochastique Lent (39,1) sur données hebdomadaires — la persistance des signaux est bien plus longue (tendances de plusieurs mois à années), réduisant drastiquement le nombre de trades.
**TRADEX-AI C1** : Pour TRADEX-AI, le Stochastique Lent (39,1) sur timeframe hebdomadaire peut servir de filtre de contexte macro sur GC/CL — si le Stochastic weekly est sous 50, les signaux d'achat intraday doivent être pondérés à la baisse dans le score /10.
*Catégorie : timing*

### D4440 — Synthèse technique Last Stochastic : règle opérationnelle complète
🟡 **SYNTHÈSE** (Source : the_last_stochastic_technique.md) : La technique Last Stochastic complète se résume : (1) Utiliser Slow Stochastic (39,1) ; (2) Signal achat = %K > 50 ET clôture > plus haut de clôture semaine précédente ; (3) Signal vente = %K < 50 ET clôture < plus bas de clôture semaine précédente ; (4) Confirmer avec OBV/MA30j pour éviter les faux signaux ; (5) Tester le seuil optimal par actif (peut être 40/60 plutôt que 50/50) ; (6) Ajouter 1-2 indicateurs supplémentaires sur actifs volatils.
**TRADEX-AI C1** : Cette règle opérationnelle complète est une brique momentum C1 candidate pour le score /10 de TRADEX-AI — applicable sur GC/HG/CL/ZW avec paramétrage individualisé. À valider en Phase C sur range bars NT8 avant intégration en production.
*Catégorie : indicateurs_momentum*
