# Extraction StockCharts — Richard Rhodes' Trading Rules
**Source :** `bundles/stockcharts/richard_rhodes_trading_rules.md` (HTTP 200) · 0 image
**Méthode images :** aucune image (page texte, manifest 0/0)
**Décisions :** D3451 → D3464 · **Page :** chartschool.stockcharts.com/.../overview/richard-rhodes-trading-rules
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
Aucune image certifiée (page texte).

## DÉCISIONS

### D3451 — Philosophie : la simplicité gagne
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Règles simples transmises à Richard Rhodes ; « simple methods work best ». Trop d'indicateurs complexes (Stochastics, MM pondérées, Fibonacci…) empêchent une décision rationnelle. Adhérence difficile mais rentable dans la durée.
**TRADEX-AI C3** : Argument pour une grille déterministe sobre (cf. multicollinéarité) plutôt qu'un empilement d'indicateurs.
*Catégorie : gestion_risque_entree*

### D3452 — Règle 1 : en bull market, être long
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : En marché haussier, on doit être long ou sur la touche — jamais short. « Not having a position is a position ».
**TRADEX-AI C3** : Filtre directionnel — interdire les contre-tendances en tendance majeure confirmée sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D3453 — Règle 2 : acheter la force, vendre la faiblesse
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : « buy higher and sell higher », pas « buy low sell high ». Le pro achète parce que les prix ont monté. Comparer dans un groupe : acheter le plus fort, vendre le plus faible.
**TRADEX-AI C7** : Cohérent avec la force relative (RRG/RS-Ratio) — privilégier l'actif le plus fort du panier.
*Catégorie : signal*

### D3454 — Règle 3 : préparer chaque trade
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Entrer un trade comme s'il pouvait être le plus gros de l'année — après réflexion, avec un plan d'ajout et des plans de sortie de contingence.
**TRADEX-AI C3** : Exiger plan d'entrée/ajout/sortie avant tout signal (mode Manuel).
*Catégorie : gestion_risque_entree*

### D3455 — Règle 4 : ajouter sur corrections mineures
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Sur corrections mineures contre la tendance majeure, ajouter (en bull : sur replis vers le support ; en bear : sur rebonds vers la résistance). Utiliser le niveau de correction **33-50 %** du mouvement précédent ou la bonne moyenne mobile comme premier point d'ajout.
**TRADEX-AI C3** : Zones de pyramidage 33-50 % du swing (à confronter au risk_manager).
*Catégorie : gestion_risque_entree*

### D3456 — Règles 5-8 : patience
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Être patient — attendre une correction si un trade est manqué (R5) ; laisser le trade se développer (R6) ; ne pas prendre de petits profits (« you never go broke taking a profit » = pire conseil ; le gros argent vient d'1 à 3 grands trades/an) (R7) ; laisser le temps au trade de s'isoler du bruit (R8).
**TRADEX-AI C3** : Argument contre les sorties prématurées ; laisser courir les gagnants.
*Catégorie : gestion_risque_entree*

### D3457 — Règle 9 : être impatient sur les pertes
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Petites pertes et pertes rapides = les meilleures. Ce n'est pas la perte d'argent qui compte, mais le capital mental usé à rester sur un trade perdant.
**TRADEX-AI C3** : Couper vite les pertes — cohérent avec stops serrés.
*Catégorie : gestion_risque_entree*

### D3458 — Règle 10 : ne JAMAIS moyenner à la baisse
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Ne jamais ajouter à un trade perdant ni « moyenner ». Chaque nouvel achat doit être à un prix **plus haut** (chaque vente plus bas). À respecter sans question.
**TRADEX-AI C3** : Garde dur — interdire le moyennage à perte dans le risk_manager.
*Catégorie : gestion_risque_entree*

### D3459 — Règle 11 : faire plus de ce qui marche
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Ajouter au trade le plus profitable, retrancher au moins profitable/perdant. Base de « let your profits run ».
**TRADEX-AI C3** : Allocation dynamique vers les positions gagnantes.
*Catégorie : gestion_risque_entree*

### D3460 — Règle 12 : technique ET fondamental d'accord
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Ne pas trader tant que technique et fondamental ne sont pas alignés.
**TRADEX-AI C4** : Croiser signal technique et contexte macro (news gate) avant décision.
*Catégorie : gestion_risque_entree*

### D3461 — Règles 13-14 : gérer son mental et sa taille
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Après pertes vives, faire une pause (fermer tout, stopper plusieurs jours) — le besoin de « récupérer » est dangereux (R13). Quand on trade bien, trader plus gros (R14).
**TRADEX-AI C3** : Garde psychologique — suspendre après série perdante (cf. suspension Auto).
*Catégorie : gestion_risque_entree*

### D3462 — Règle 15 : taille d'ajout 1/4 à 1/2
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : En ajoutant, n'ajouter que 1/4 à 1/2 de la position courante (ex. 400 actions → +100/200). Le prix moyen bouge de moins de la moitié de la distance → permet de tenir des corrections de 50 % sans toucher le prix moyen.
**TRADEX-AI C3** : Règle de pyramidage dégressif à implémenter dans le sizing.
*Catégorie : gestion_risque_entree*

### D3463 — Règles 16-17 : guérilla et nature des tops/bottoms
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Combattre du côté gagnant du marché ; si aucun camp ne gagne, ne pas combattre (R16). Les marchés forment leurs **tops dans la violence** et leurs **bas dans le calme** (R17).
**TRADEX-AI C5** : Lecture de la volatilité aux extrêmes (tops violents vs bas calmes).
*Catégorie : structure_marche*

### D3464 — Règle 18 : asymétrie temps/prix du bull run
🔵 **ÉCOLE** (Source : richard_rhodes_trading_rules.md) : Les derniers 10 % du temps d'un bull run encapsulent souvent **50 %+** du mouvement de prix ; les premiers 50 % du prix prennent 90 % du temps (plus difficiles à trader). « Common sense is uncommon » (Voltaire).
**TRADEX-AI C3** : Anticiper l'accélération finale ; les phases initiales sont plus laborieuses.
*Catégorie : structure_marche*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3451 → D3464 (14) |
| Images citées | 0 (page texte) |
| Catégories | gestion_risque_entree · signal · structure_marche |
| Tags | 🔵 ÉCOLE (heuristiques qualitatives, jamais critères éliminatoires) |
| Belkhayate | NON CONCERNÉ |

> ⚠️ Règles heuristiques (psychologie/gestion), à NE PAS coder comme déclencheurs durs.
> Outil éducatif · validation/ — aucune fusion master sans OK.
