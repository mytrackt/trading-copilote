# Extraction NinjaTrader — Cumulative Delta (Order Flow)
**Source :** `bundles/ninjatrader/what_is_cumulative_delta_in_order_flow_trading.md` (HTTP 200 · blog NinjaTrader, 30/03/2021) + 0 image certifiée
**Méthode images :** ancrage figcaption locale (HTML statique) · 0/0 certifiée · aucune `<figure>+<figcaption>` sur la page
**Décisions :** D359 → D366 · **Page :** ninjatrader.com/futures/blogs/what-is-cumulative-delta-in-order-flow-trading
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** — Cumulative Delta alimente directement le **cercle C2 (order flow)** : différence achats/ventes au marché, divergences delta/prix, absorption. Source **Tier 2 broker** (NinjaTrader, éditeur de l'outil Order Flow +) : les faits de définition sont 🟢 ; les interprétations de trading et la promotion de la suite Order Flow + sont marquées 🔵 ÉCOLE (interprétation maison de l'éditeur).
> ⚠️ Exemples de la source en **MES (Micro E-mini S&P 500)** → recadrés sur actifs TRADEX-AI : TRADING GC·HG·CL·ZW ; CONFIRMATION ES·DX·VX ; RÉFÉRENCE MBT·6J. ES (S&P 500) reste un actif de CONFIRMATION, pas de TRADING.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | aucune `<figure>+<figcaption>` détectée (manifest : 0 certifiée · 0 à vérifier · 0 décorative) | — | — |

> Le bundle décrit 2 graphiques (chart Session/Bar · chart divergence) mais **sans figure/figcaption ancrable** : non certifiables, cités en texte seulement.

---

## DÉCISIONS

### D359 — Delta : définition (différence acheteurs / vendeurs au marché)
🟢 **FAIT VÉRIFIÉ** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Le Delta (Δ) désigne la **différence entre acheteurs et vendeurs**. Il est **positif quand l'achat l'emporte sur la vente**, **négatif quand la vente l'emporte sur l'achat**.
**TRADEX-AI C2** : Brique de base order flow — signe du delta = pression nette acheteuse/vendeuse instantanée sur GC/HG/CL/ZW (lecture ATAS / Order Flow).
*Catégorie : structure_marche*

---

### D360 — Cumulative Delta : tally cumulé tracé en indicateur
🟢 **FAIT VÉRIFIÉ** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Le Cumulative Delta **consolide l'information de delta accumulée** et la trace visuellement comme indicateur graphique. En enregistrant un **cumul courant** indiquant si acheteurs ou vendeurs ont eu le contrôle et de combien, le trader order flow peut mieux extrapoler le flux du marché.
🔵 **ÉCOLE** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : NinjaTrader présente le Cumulative Delta comme une **pierre angulaire de l'analyse order flow**, aidant à déterminer direction du marché, force de tendance, zones de support/résistance.
**TRADEX-AI C2** : Calculer un cumul courant du delta par session sur GC/HG/CL/ZW ; pente du Cumulative Delta = proxy de contrôle acheteur/vendeur (cercle C2).
*Catégorie : structure_marche*

---

### D361 — Deux modes d'affichage : Session vs Bar
🟢 **FAIT VÉRIFIÉ** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Deux affichages. **Session** : le Cumulative Delta est tracé comme un chandelier traditionnel, la clôture de la barre précédente étant reportée à l'ouverture de la barre courante pendant que le delta s'accumule. **Bar** : tracé en histogramme, chaque nouvelle barre **ouvre à 0** et le delta s'accumule sur la durée de la barre de prix correspondante.
**TRADEX-AI C2** : Choix de mode = choix d'horizon. Session = cumul intra-session continu (biais directionnel) ; Bar = delta net par barre (lecture micro). Exposer les deux dans la config ATAS/export sur GC/HG/CL/ZW.
*Catégorie : configuration*

---

### D362 — Cumulative Delta : usages multiples, dépendants du contexte
🔵 **ÉCOLE** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Le Cumulative Delta est utilisé de **multiples façons** par les analystes techniques ; chaque approche **varie selon le trader, le marché et le timeframe** tradés.
**TRADEX-AI C2** : Aucun réglage universel — paramétrer la lecture du Cumulative Delta par actif (GC/HG/CL/ZW) et par mode/timeframe Belkhayate (Standard 15min / Range Bar / Scalping). Ne pas transposer aveuglément un réglage MES vers un autre actif.
*Catégorie : configuration*

---

### D363 — Divergence delta / prix = signal de retournement potentiel
🟢 **FAIT VÉRIFIÉ** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Dans l'exemple, une **divergence est repérée entre prix et Cumulative Delta**, indiquant un **retournement de marché potentiel**. Le prix inscrit un **nouveau plus bas** (panneau haut, flèche rouge) tandis que le Cumulative Delta inscrit un **plus bas plus haut** (higher low) par rapport au même point de départ (panneau bas, flèche verte).
🔵 **ÉCOLE** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Cette configuration peut s'interpréter comme un **signal haussier**, aidant les longs à éviter un *headfake* / à ne pas se faire « secouer » hors d'une position en confirmant un biais haussier ; alternativement, elle peut servir à **initier une position longue**.
**TRADEX-AI C2** : Détecter la divergence prix/Cumulative Delta (prix plus-bas-plus-bas vs delta plus-bas-plus-haut → haussier, et symétrique baissier) comme signal de retournement sur GC/HG/CL/ZW. Cas réciproque baissier **non explicité par la source** → voir D364.
*Catégorie : divergence*

---

### D364 — Divergence baissière (symétrique) — déduction projet
🔴 **NON VÉRIFIÉ** (déduction TRADEX-AI, NON affirmée par la source) : Par symétrie de D363, une **divergence baissière** s'écrirait : prix inscrit un **plus haut plus haut** alors que le Cumulative Delta inscrit un **plus haut plus bas** (lower high), suggérant un retournement baissier. La source ne décrit **que** le cas haussier.
**TRADEX-AI C2** : Implémenter le miroir baissier **avec prudence** — à confirmer sur une source order flow dédiée (ATAS / footprint) avant pondération forte. Marqué 🔴 jusqu'à validation.
*Catégorie : divergence*

---

### D365 — Garde-fou : faux signaux et primauté du risque
🟢 **FAIT VÉRIFIÉ** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Note explicite de la source — comme **tout indicateur technique**, le Cumulative Delta peut **produire de faux signaux**, et la **gestion du risque doit rester primordiale** sur des marchés imprévisibles.
**TRADEX-AI C2** : Garde permanent — un signal de divergence Cumulative Delta sur GC/HG/CL/ZW ne s'arme **jamais seul** : exiger confirmation (price action Belkhayate, structure, autre cercle) + R/R ≥ 1:2. Aligne sur les sécurités obligatoires (News Gate, staleness).
*Catégorie : gestion_risque_entree*

---

### D366 — Appartenance outil : suite Order Flow + (positionnement éditeur)
🔵 **ÉCOLE** (Source : what_is_cumulative_delta_in_order_flow_trading.md) : Le Cumulative Delta est **inclus dans la suite Order Flow +** de NinjaTrader (outils premium), aux côtés de **Volume Profile, Volumetric Bars, VWAP** et autres.
⏳ **VOLATILE** : Le périmètre/packaging commercial de la suite Order Flow + (composants, statut premium) peut évoluer ; ne pas figer en règle de trading.
**TRADEX-AI C2** : Information de provenance outil, **pas** une règle de signal. Côté TRADEX-AI, l'order flow vient d'**ATAS Pro (Rithmic)** — vérifier l'équivalence Cumulative Delta NinjaTrader ↔ ATAS avant tout calage.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D359 → D366 (8) |
| Images certifiées citées | 0/0 (aucune `<figure>+<figcaption>` sur la page) |
| Catégories utilisées | structure_marche · configuration · divergence · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🔴 NON VÉRIFIÉ · ⏳ VOLATILE |
| Cercle dominant | **C2 (order flow)** — page PRIORITAIRE |
| Belkhayate | Indirect — Cumulative Delta = entrée C2 (ATAS), complémentaire des 4 étapes (Pivots → BGC → Direction → Énergie) ; jamais signal isolé |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.

### CAS « À VÉRIFIER »
- **D364** (divergence baissière) : déduction par symétrie, **non affirmée par la source** → confirmer sur source order flow dédiée (ATAS / footprint) avant pondération.
- **D366** : équivalence Cumulative Delta **NinjaTrader ↔ ATAS Pro (Rithmic)** non établie — calage outil à vérifier côté implémentation TRADEX-AI.
- Exemples source en **MES (S&P 500)** : ES est CONFIRMATION (pas TRADING) dans TRADEX-AI ; logique transposée à GC/HG/CL/ZW mais **non testée** sur ces actifs par la source.
