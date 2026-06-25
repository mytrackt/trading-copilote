# Extraction AdamGrimes — What Happens After Big Spikes In The VIX?
**Source :** `bundles/adamgrimes/what_happens_after_big_spikes_in_the_vix.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7431 → D7450 · **Page :** https://www.adamhgrimes.com/what-happens-after-big-spikes-in-the-vix/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Comportement du VIX post-spike comme signal de sentiment C5 — acheter la peur, pas la fuir.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D7431 — Les grands spikes VIX surviennent après des baisses, pas avant
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Historiquement, les grands événements volatils sur les actions surviennent après des baisses. Ce sont donc des opportunités d'achat consistantes — pas des signaux de danger futur.
**TRADEX-AI C5** : Un pic soudain du VIX (cercle C5) ne doit pas bloquer les signaux d'achat sur ES/GC — au contraire, il signale historiquement un contexte favorable à l'achat après épuisement vendeur. Revoir le garde-fou VIX > seuil critique pour ne pas bloquer à tort en mode Auto.
*Catégorie : indicateurs_momentum*

### D7432 — Après un gros spike VIX, acheter les actions est historiquement la bonne décision
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Quand le VIX monte fortement, il faut ACHETER les actions — contrairement à la croyance populaire qui voit le VIX comme un "harbinger of doom". Les grands spikes VIX sont historiquement de bonnes opportunités d'achat.
**TRADEX-AI C5** : Le rôle de VX dans TRADEX est confirmation, pas blocage systématique. Un spike VIX extrême aligné avec un signal d'achat Belkhayate sur ES/GC est à traiter comme confirmation haussière potentielle, pas comme filtre éliminatoire automatique.
*Catégorie : indicateurs_momentum*

### D7433 — La volatilité décroît après un choc — modèle "pond ripple"
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Les chocs de volatilité tendent à décroître après l'événement. L'analogie est celle des ondulations dans un étang après y avoir jeté une grosse pierre — la volatilité se comporte ainsi (capturé dans les modèles GARCH).
**TRADEX-AI C5** : Après un spike VIX majeur, anticiper une décroissance progressive de la volatilité dans les jours suivants. Cela justifie d'élargir progressivement les cibles (T1 → T2) sur les trades GC/ES car l'amplitude des swings va se réduire.
*Catégorie : gestion_position_active*

### D7434 — La mesure du choc de volatilité importe peu
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Qu'on mesure le choc de volatilité via grands déclines S&P, grands sauts en points du VIX, ou grands sauts de volatilité historique 20j — les résultats de la décroissance post-choc sont similaires. La méthode de mesure n'influence pas significativement les conclusions.
**TRADEX-AI C5** : Pour le filtre VIX du News Gate / circuit breaker, l'indicateur exact (VX, HVol, ou SigmaSpikes ES) est secondaire — l'important est de détecter le régime de choc, quelle que soit la mesure utilisée.
*Catégorie : indicateurs_momentum*

### D7435 — Hausse à court terme de la volatilité historique vs décroissance du VIX
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Il existe une divergence intéressante : après un gros spike VIX, la volatilité historique (HVol) augmente à court terme tandis que le VIX lui-même décroît. Les traders d'options peuvent en tirer parti.
**TRADEX-AI C5** : Dans les jours suivant un spike VIX, le VX (terme court) peut baisser même si la volatilité réalisée reste élevée. Ne pas interpréter la baisse du VX comme un retour à la normalité immédiate — les ranges réels GC/CL peuvent rester larges.
*Catégorie : indicateurs_momentum*

### D7436 — Petite taille d'échantillon : résultats indicatifs, non conclusifs
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : Les tailles d'échantillon des événements de volatilité extrême sont petites. Les effets semblent persistants mais les résultats sont indicatifs, pas conclusifs — les moyennes cachent une large dispersion des résultats.
**TRADEX-AI C5** : Les règles KB basées sur le comportement post-spike VIX doivent être taguées VOLATILE (badge ⏳) dans la Knowledge Base — elles guident l'analyse mais ne constituent pas des règles déterministes de signal.
*Catégorie : psychologie*

### D7437 — Segmenter par régime volatilité : low vol vs high vol
🟡 **SYNTHÈSE** (Source : what_happens_after_big_spikes_in_the_vix.md) : Pour affiner l'analyse post-spike, il est recommandé de segmenter les résultats selon le régime de volatilité ambiant (événement en régime low vol vs high vol) pour obtenir des statistiques plus exploitables.
**TRADEX-AI C5** : La grille de score TRADEX /10 doit pondérer différemment le signal VX selon le régime : en régime high vol chronique (VIX > 25 plusieurs semaines), un spike additionnel a moins de valeur prédictive qu'en régime low vol.
*Catégorie : indicateurs_momentum*

### D7438 — Le "knuckle" de la volatilité historique peut être un artefact de mesure
🟢 **FAIT VÉRIFIÉ** (Source : what_happens_after_big_spikes_in_the_vix.md) : La légère hausse observée dans la volatilité historique 20j après un événement pourrait être un artefact dû au bord droit de la fenêtre d'évaluation de 20 jours, pas un phénomène réel.
**TRADEX-AI C5** : Lors du calcul du Staleness Monitor, vérifier que les périodes de calcul de volatilité (HVol, ATR) ne créent pas d'artefacts aux bords de fenêtre — utiliser des indicateurs à base exponentielle (ATR EWM) plutôt que des moyennes simples si possible.
*Catégorie : configuration*

### D7439 — Cadre opérationnel : spike VIX = contexte achat ES à surveiller
🟡 **SYNTHÈSE** (Source : what_happens_after_big_spikes_in_the_vix.md) : L'article fournit des lignes directrices pratiques pour les semaines suivant un gros spike VIX : surveiller le contexte d'achat sur les actions plutôt que de fuir le marché.
**TRADEX-AI C4/C5** : Dans le prompt Claude, quand VX a spiké > 40% en 1 journée sur ES, le cerveau doit noter "régime post-spike VIX — biais achat ES historique dominant, surveiller signal confirmation" avant d'analyser les signaux de trading GC/CL.
*Catégorie : macro_evenements*

### D7440 — La "fear gauge" narrative est contre-productive pour le trading
🟡 **SYNTHÈSE** (Source : what_happens_after_big_spikes_in_the_vix.md) : Présenter le VIX comme un "harbinger of doom" est contre-productif et statistiquement faux. Cette narrative pousse les traders à vendre au pire moment.
**TRADEX-AI C5/C7** : Dans l'interface TRADEX, ne jamais afficher d'alerte rouge "DANGER — VIX spike" seule — toujours contextualiser avec "historiquement = opportunité achat ES + décroissance volatilité attendue" pour éviter la panique d'Abdelkrim en mode Manuel.
*Catégorie : psychologie*

