# RAPPORT — Sélection de la vidéo Belkhayate pour le CALAGE de l'indicateur Centre de Gravité (COG) + Timing

> Objectif : identifier, parmi les transcriptions déjà réalisées, la vidéo où Belkhayate **montre l'indicateur COG à l'écran** en précisant idéalement le **marché** et l'**unité de temps**, afin de caler une reconstruction paramétrée (régression + bandes en multiples du nombre d'or).
> Date : 2026-06-17 — Périmètre : `C:\trading-copilote\` uniquement (récursif).

---

## ÉTAPE 1 — Périmètre confirmé

`C:\trading-copilote\` **existe**.

Sous-dossiers principaux (niveau 1) : `_archive`, `_temp`, `.claude`, `00-pilotage`, `01-moteur-transvideo`, `02-sources-brutes`, `03-transcriptions`, `04-cerveau-trading`, `05-saas`, `06-skills`, `data`.

Fichiers de transcription trouvés (récursif, extensions `.srt/.vtt/.txt/.md/.json`) :

| Extension | Nombre |
|-----------|-------:|
| `.json`   | 432 (dont ~220 `*.info.json` = **métadonnées yt-dlp, pas des transcriptions**) |
| `.txt`    | 368 |
| `.md`     | 276 |
| `.srt`    | 0 |
| `.vtt`    | 0 |
| **TOTAL** | **1076** |

**Corpus utile** = les **110 transcriptions texte Belkhayate** dans
`03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\*.txt`
(les `whisper_*.txt` de `transcripts-bruts\` en sont des **doublons** ; ils ont été dédoublonnés).

⚠️ **Aucun fichier `.srt`/`.vtt` n'existe.** Les transcriptions sont du **texte brut Whisper sans timestamps**.
→ Conséquence : pour TOUS les fichiers, les repères de capture sont donnés en **n° de ligne**, et les captures d'écran sont à **repérer manuellement** dans la vidéo source.

---

## ÉTAPE 2 — Candidats retenus

Le corpus entier est consacré à Belkhayate, donc le filtre "belkhayate / centre de gravité / barycentre / timing / COG / nombre d'or" retient la quasi-totalité des fichiers. Le filtre **discriminant pour le calage COG** est : la vidéo concerne explicitement le **Centre de Gravité / Gravity Center** (et non les Pivots, l'order flow, la psychologie, etc.).

12 vidéos au titre "Gravity Center / Centre de Gravité / 6 dimensions / Indicateur" ont été isolées (voir tableau ÉTAPE 4).

---

## ÉTAPE 3 — Méthode de scoring (déterministe, insensible casse + accents)

Comptage pondéré des occurrences (texte normalisé : minuscules, accents retirés, apostrophes uniformisées) :

- **Poids 3 — Paramètres** : `régression, polynomial, période, déviation, écart, bande, barycentre, nombre d'or, 1.618, 2.618, 4.236, 0.618` → **c'est le signal de calage**.
- **Poids 2 — Timeframe** : `unité de temps, M5, M15, H1, H4, D1, 5/15 minutes, 1 heure, 4 heures, horaire, journalier, daily, weekly`.
- **Poids 2 — Marché** : `CAC, DAX, or, gold, EURUSD, pétrole, CL, futures, ES, NQ, Nasdaq, S&P, Dow Jones`.
- **Poids 1 — Démonstration** : `vous voyez, regardez, ici, à l'écran, le cours touche, cette bande, la ligne bleue, la zone`.

> ⚠️ Limite assumée : le **Total** est dominé par le Poids 1 (mots "ici/regardez" ∝ longueur du texte) et par le bruit lexical du Poids 2 marché ("or" la conjonction). **Pour le calage, la colonne décisive est P3 (paramètres) couplée au caractère COG de la vidéo**, pas le Total brut.

---

## ÉTAPE 4 — Classement

Tableau des vidéos COG (titre Gravity Center / Centre de Gravité / 6 dimensions), triées par P3 :

| Fichier (`belkhayate-youtube\transcripts\`) | P3 | P2 tf | P2 mkt | P1 | Total | Timestamps ? |
|---|--:|--:|--:|--:|--:|---|
| **`57DtXQp35Eo_Belkhayate Gravity Center User Guide.txt`** | **9** | 10 | 13 | 68 | 141 | NON (txt brut) |
| **`ubKv-05qdbU_Mode d'Emploi Belkhayate Gravité Center.txt`** | **9** | 10 | 7 | 64 | 125 | NON (txt brut) |
| **`TQ7hYcJx9OE_..._Centre de Gravité..._Leçon N°9.txt`** | **3** | 4 | 6 | 38 | 67 | NON (txt brut) |
| `1yu1CrC0HS0_Voici les 2 Indicateurs Bonus...txt` | 1 | 3 | 3 | 76 | 91 | NON |
| `TAWkII5CI-k_Présentation de Belkhayate Gravity Center.txt` | 1 | 0 | 4 | 38 | 49 | NON |
| `_Bbzx2lITEQ_Belkhayate Indicateurs sur Tradingview.txt` | 0 | 2 | 12 | 95 | 123 | NON |
| `BOENPfxIptU_Trading simple du Dow Jones...txt` | 0 | 5 | 7 | 71 | 95 | NON |
| `oEPSHUdIV0U_Mode d'Emploi de Belkhayate Centre de Gravité.txt` | 0 | 9 | 3 | 19 | 43 | NON |
| `J00s5ROFnKA_Comment Utiliser le Gravity Center ? Leçon N°10.txt` | 0 | 1 | 2 | 37 | 43 | NON |
| `pX5_n4GxatA_..._Indicateur 6 Dimensions Leçon N°8.txt` | 0 | 0 | 9 | 7 | 25 | NON |
| `0ul4j0d6uCQ_video 1 : Belkhayate Gravity Center on Ninjatrader.txt` | 0 | 0 | 4 | 14 | 22 | NON |
| `Plmyxm6qFq8_Belkhayate Gravity Center User Guide.txt` | 0 | 0 | 3 | 9 | 15 | NON |

Pour mémoire (Total brut élevé mais **hors-sujet COG** — Pivots / range / général, ignorés pour le calage) :
`gTgNe0P4SVw_Belkhayate Pivots Method` (Total 250, mais c'est l'indicateur **Pivots**), `doUa5le9fFs_Identifier le trading range` (248), `ajTvB8oz4Ag_Gagner facilement...` (191).

**Conclusion du classement : `57DtXQp35Eo` est la vidéo la plus utile au calage paramétré du COG** (P3 maximal + timeframe + marché tous présents, et paramètres chiffrés explicites).

---

## ÉTAPE 5 — Fiches détaillées

### 🥇 TOP 1 — `57DtXQp35Eo_Belkhayate Gravity Center User Guide.txt`

- **Chemin complet** : `C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\57DtXQp35Eo_Belkhayate Gravity Center User Guide.txt`
- **Titre vidéo** : *Belkhayate Gravity Center User Guide* (ID YouTube `57DtXQp35Eo`)
- **Format** : transcription Whisper **bilingue** — partie anglaise (l.1-47), partie française mode d'emploi (l.48-107), installation EN (l.108-137) puis installation FR sur NinjaTrader (l.138-182). **Pas de timestamps.**

**MARCHÉ détecté** (verbatim + ligne) :
- l.2 : « *We see here the chart of the crude oil on range bar, 5 range bar.* »
- l.49 : « Nous voyons ici le marché du **pétrole** sur une unité de temps de 5 range bar. »
- l.156 / l.179 : « ouvrir un chart. Par exemple, le **pétrole**. » / « votre centre de gravité sur le **pétrole**, sur 5 ticks. »

**TIMEFRAME détecté** (verbatim + ligne) — *information clé* :
- l.49-50 : « ...sur une **unité de temps de 5 range bar**. Autrement dit, chaque bougie ici représente 5 ticks. »
- l.16 : « *you should use Belgrade Gravity Center in the small time frame like **range bar, five range bar or four range bar**.* »
- l.53-54 : « ...lorsqu'on va trader sur des unités de temps de **15 minutes**... certains qui vont traiter sur du **4 heures**. » (citées comme **trop longues**, à éviter)
- l.57 : « ...sur une **unité de temps courte comme par exemple 5 range bar ou 1 minute**. »
- l.135 / l.161 : « par «Range Bar», «Five Range Bar» » / « ...mettre **quatre range bars ou cinq range bars**. »

**PARAMÈTRES explicitement énoncés** (verbatim + ligne) — *le cœur du calage* :
- l.128-130 : « ...ici, c'est **0.618**, instead de **1.618**, pour le «Traditional Gravity Center». Vous pouvez changer l'**ordre**, ici, et le «**Period**», comme vous voulez. »
- l.172-177 : « ...sur le gravity center ici, l'**écart** n'est plus de **1,618**, mais de **0,618**. ... L'**ordre, il est de 3**. Et bien sûr, vous pouvez changer les **périodes**. Moi, je recommande **180 en période** ici. »
- l.104 : « ...cet indicateur, bien qu'il retrace, qu'il repeint, ... à chaque bougie, **toutes les bandes se recalculent**. » (→ nature **repaint** : implication forte pour le calage/backtest)

> ✅ **Cohérence avec `COGParams` figés du projet** : période **180**, ordre **3**, coefficients **0,618 / 1,618**. Cette vidéo est la **source documentaire directe** de ces paramètres.

**5–10 repères pour CAPTURE D'ÉCRAN** (⚠️ pas de timestamp → à repérer manuellement dans la vidéo, ancrés au n° de ligne du discours) :
1. **l.2-4** — chart pétrole brut SANS l'indicateur, puis ajout du COG : capture l'état "avant/après" (calibration visuelle de l'overlay).
2. **l.6-7** — "*oscillating by 30 ticks*" : capture montrant l'amplitude bande haute↔bande basse (échelle des bandes).
3. **l.63-66** — "amplitude... range d'environ 30 ticks... 15 ticks vers le centre" : capture des 3 lignes (haute / centre bleu / basse) avec mesure.
4. **l.78-80** — "zone rouge / centre de gravité / **ligne bleue** / zone verte" : capture nommant chaque bande (mapping couleurs↔multiples).
5. **l.88-92** — "queue de 4 ticks dans la zone verte" : capture d'un rebond sur bande extrême (déviation extérieure).
6. **l.119-122** — écran NinjaTrader "New Chart → Oil Market → Range → template" : capture du choix marché/type de barres.
7. **l.127-130** — boîte de dialogue Indicator "Gravity Center" montrant **0.618 vs 1.618** : **capture la plus importante** (valeur du multiple).
8. **l.171-177** — paramètres FR à l'écran : **écart 0,618 / 1,618**, **ordre = 3**, **période = 180** : capture du panneau de réglages complet.
9. **l.179-180** — résultat final : COG appliqué sur pétrole 5 ticks : capture de validation du rendu paramétré.

---

### 🥈 Remplaçant 1 — `ubKv-05qdbU_Mode d'Emploi Belkhayate Gravité Center.txt`

- **Chemin** : `C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\ubKv-05qdbU_Mode d'Emploi Belkhayate Gravité Center.txt`
- **Titre** : *Mode d'Emploi Belkhayate Gravité Center* (ID `ubKv-05qdbU`)
- **Nature** : **version FR seule** du même mode d'emploi que le TOP 1 (transcription en lignes très fragmentées). Contenu paramétrique **identique** → bon document de **recoupement/confirmation**. Pas de timestamps.

**MARCHÉ** : l.2 « Nous voyons ici le marché du **pétrole** sur une unité de temps de 5 range bar. » ; l.348/427 « le **pétrole** ».

**TIMEFRAME** : l.2-3 « **5 range bar** ... chaque bougie ici représente 5 tics » ; l.6-7 « unités de temps de **15 minutes**... du **4 heures** » (à éviter) ; l.11 « **5 range bar ou 1 minute** » ; l.372-374 « **4 range bas ou 5 range bas** ».

**PARAMÈTRES** (verbatim + ligne) :
- l.207-209 : « **0.618** instead de **1.618** pour le ... traditionnel Gravity Center » ; l.215-217 « changer **order** ... et **period** comme vous voulez ».
- l.407-418 : « l'**écart** n'est plus de **1,618** mais de **0,618** ... l'**ordre il est de 3** ... moi je recommande **180 en période** ».

**Repères capture** (manuel, n° de ligne) : l.16-21 (overlay avant/après), l.95-99 (amplitude 30/15 ticks), l.207-209 (0.618 vs 1.618 EN), l.407-418 (panneau FR : écart/ordre/période), l.427-432 (rendu final pétrole 5 ticks).

---

### 🥈 Remplaçant 2 — `TQ7hYcJx9OE_Pourquoi le nouveau Centre de Gravité est-il puissant ? Leçon N°9.txt`

- **Chemin** : `C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\TQ7hYcJx9OE_Pourquoi le nouveau Centre de Gravité est-il puissant ？ Leçon N°9.txt`
- **Titre** : *Pourquoi le nouveau Centre de Gravité est-il puissant ? Leçon N°9* (ID `TQ7hYcJx9OE`)
- **Intérêt complémentaire** : présente **2 indicateurs** (BGC + "nouvelle version" multi-unités de temps) sur un **autre marché et un autre timeframe** → utile pour valider le calage sur un 2ᵉ cas. Pas de timestamps.

**MARCHÉ** : l.6 « ici, nous avons l'**or** sur 30 minutes » ; l.12 « Nous avons l'**or** » ; l.100 « je mets l'**or** ».

**TIMEFRAME** : l.6-7 « l'or sur **30 minutes**... chaque ligne ici représente... la journée » ; l.29 « ...à la fois en **30 minutes, en 15 minutes, en 10 minutes, en 5 minutes, en 1 minute** » (le "nouveau" COG = combinaison sur **6 unités de temps**, cf. l.4) ; l.51 « en **deux minutes** » ; l.46 « en **délit**/daily ».

**PARAMÈTRES** (verbatim + ligne) :
- l.16-21 : « Le premier, c'est ... **BGC** ... Et ici, vous allez avoir **1,618**. ... pour le moment, vous, vous mettez **0,618**. »
- l.4 : « une combinaison du centre de gravité sur **6 unités de temps différentes** » (structure de la "nouvelle version").
- ⚠️ l.149-152 : Belkhayate montre l'**accès au code** de l'indicateur dans NinjaTrader (« vous avez le code... au code en deux indicateurs ») — **le code est MONTRÉ à l'écran mais son contenu n'est PAS dicté** → la structure interne (régression/polynôme) **N'EST PAS énoncée** dans la transcription. **NON PRÉCISÉ DANS LA TRANSCRIPTION.**

**Repères capture** (manuel, n° de ligne) : l.6-13 (or 30 min + BGC), l.16-24 (bascule 1,618 → 0,618, COG bleu), l.28-30 (multi-timeframe), l.149-152 (**écran d'édition du code NinjaTrader** — précieux pour la rétro-ingénierie de la formule).

---

## ÉTAPE 6 — Règles anti-hallucination appliquées

- Toutes les valeurs ci-dessus sont **citées au mot près** avec **n° de ligne** (aucun fichier ne contient de timestamp SRT/VTT).
- **Aucun paramètre ni timeframe inventé** : seuls figurent ceux littéralement présents (0,618 / 1,618 ; ordre 3 ; période 180 ; pétrole / or ; 5 range bar / 30 min).
- **Multiples 2.618 et 4.236** : **NON PRÉSENTS** dans les transcriptions analysées (le discours ne cite que 0,618 et 1,618). Toute reconstruction utilisant 2.618/4.236 relèverait d'une hypothèse, pas de la source.
- **Formule de régression / barycentre / ordre du polynôme au-delà de "ordre = 3"** : **NON DÉTAILLÉE** dans les transcriptions (Belkhayate dit "vous pouvez changer l'ordre" et montre le code à l'écran sans le dicter). → reste **[RECONSTRUCTION]** à valider par capture du code (TQ7hYcJx9OE l.149-152) ou par calage empirique.
- **DIT vs MONTRÉ** : ce qui est chiffré ci-dessus est **DIT** (transcription fiable). Le tracé des bandes, les couleurs exactes, et le code source sont **MONTRÉS** → nécessitent une **capture d'écran**.
- **Fichiers sans timestamps** : tous → captures à **repérer manuellement** dans la vidéo source à partir des ancres de ligne fournies.

---

## SYNTHÈSE / RECOMMANDATION

**Vidéo à exploiter en priorité pour caler la reconstruction paramétrée du COG :**
`57DtXQp35Eo — Belkhayate Gravity Center User Guide`.

Elle fournit, **dicté à l'oral**, le jeu de paramètres complet :
**marché = pétrole**, **timeframe = 5 range bar (ticks)**, **écart = 0,618 (vs 1,618 "traditionnel")**, **ordre = 3**, **période = 180**, indicateur **repaint** (bandes recalculées à chaque bougie).
→ Cohérent avec les `COGParams` figés du projet.

Recoupement : `ubKv-05qdbU` (mêmes paramètres, FR). Second cas marché/TF (or, 30 min + multi-TF) et **accès au code à l'écran** : `TQ7hYcJx9OE`.

**Prochaine action recommandée** : ouvrir la vidéo `57DtXQp35Eo` et capturer l'écran aux ancres l.127-130 et l.171-177 (panneau de réglages : 0,618 / ordre 3 / période 180), puis `TQ7hYcJx9OE` l.149-152 (code NinjaTrader) pour tenter de lire la formule de régression non dictée.

---

## URLs + consignes de capture

> Ajout 2026-06-17. Métadonnées lues dans les fichiers `*.info.json` du dossier
> `03-transcriptions\nouvelles-sources\belkhayate-youtube\audio\` (yt-dlp).
> **Titre, durée, chaîne et date sont des valeurs RÉELLES extraites des métadonnées** (non inventées).
> Les transcriptions `.txt` restent **sans timestamps** → localisation par n° de ligne + ratio.

### Métadonnées vérifiées (source : `*.info.json`)

| ID | Titre exact (métadonnées) | Durée | Chaîne | Date | URL |
|---|---|---|---|---|---|
| `TQ7hYcJx9OE` | *Pourquoi le nouveau Centre de Gravité est-il puissant ? Leçon N°9* | **12:01** (721 s) | Mostafa Belkhayate - ENG | 2018-03-08 | https://www.youtube.com/watch?v=TQ7hYcJx9OE |
| `57DtXQp35Eo` | *Belkhayate Gravity Center User Guide* | **20:27** (1227 s) | Mostafa Belkhayate - ENG | 2015-09-15 | https://www.youtube.com/watch?v=57DtXQp35Eo |
| `ubKv-05qdbU` | *Mode d'Emploi Belkhayate Gravité Center* | **13:40** (820 s) | Mostafa Belkhayate - ENG | 2015-09-15 | https://www.youtube.com/watch?v=ubKv-05qdbU |

### Fiche capture par vidéo

| ID | Titre exact | URL | Ce qu'il faut capturer | Repère transcription |
|---|---|---|---|---|
| `TQ7hYcJx9OE` | Pourquoi le nouveau Centre de Gravité est-il puissant ? Leçon N°9 | https://www.youtube.com/watch?v=TQ7hYcJx9OE | **Écran où le CODE NinjaTrader est OUVERT** (éditeur indicateur). ⚠️ Le code est MONTRÉ mais **non dicté** → la formule des bandes n'apparaît pas dans le texte ; capture nécessaire pour la lire. | l.149-152 / **161 lignes** → **~93 % = toute fin de vidéo** |
| `57DtXQp35Eo` | Belkhayate Gravity Center User Guide | https://www.youtube.com/watch?v=57DtXQp35Eo | **PANNEAU DE RÉGLAGES** de l'indicateur : écart **0,618** (vs 1,618), **ordre = 3**, **période = 180**. Marché = **crude oil / pétrole**, barres **RANGE 5 ticks** (PAS du temps). | EN partiel l.127-130 (~70 %) ; **panneau FR complet l.171-177 / 182 lignes → ~94 % = fin de vidéo** |
| `ubKv-05qdbU` | Mode d'Emploi Belkhayate Gravité Center | https://www.youtube.com/watch?v=ubKv-05qdbU | **Mêmes réglages** (recoupement FR) : écart **0,618**, **ordre 3**, **période 180**. | l.407-418 / **438 lignes** → **~93 % = fin de vidéo** |

### Détail verbatim — `TQ7hYcJx9OE` (CODE NinjaTrader)

Passage l.144-157 (cible l.149-152 + 5 lignes avant/après) — **citer au mot près ce que dit Belkhayate au moment où le code est à l'écran** :

```
144  Puisque vous allez prendre le premier gain, puis vous allez rester dans le sens.
145  Vous allez encore rester dans le sens.
146  Donc, ça, c'est très, très important de maîtriser ce premier exercice pour ensuite pouvoir faire l'exercice, disons, numéro 1, d'utilisation de la nouvelle version de Belchiat Graviti,
147  qui est cet indicateur qui va toujours essayer de vous donner le centre de gravité d'un mouvement.
148  Voilà.
149  J'espère que vous allez faire bon usage de cet indicateur puisque cet indicateur-là, comme je vais vous le montrer ici, l'indicateur de Belchiat ici, vous venez ici, regardez, dans Tool,
150  et là, vous venez dans Edit Ninja Trader, vous allez venir dans Indicateur, et là, vous allez dans Belchiat Center, là, et vous avez le code.
151  Donc, j'ai laissé, j'ai laissé le code ici, ouvert.
152  Donc, vous voyez que vous avez accès au code, et au code en deux indicateurs, parce que je voudrais offrir à la jeunesse africaine,
153  et même tous les jeunes qui me suivent, ils sont les bienvenus à bénéficier de ce code et à combiner, à tester.
154  Et, évidemment, dans les autres cours, je vais essayer de montrer comment on peut améliorer cet indicateur,
155  et de manière à ce que tout le monde puisse profiter, et pourquoi pas en vivre.
156  Voilà, c'était la première vidéo de présentation de mode d'emploi de Belchiat Graviti,
157  et je vous souhaite un très bon usage.
```

**Phrase-repère à écouter pour déclencher la capture** (l.149-150) :
« *…comme je vais vous le montrer ici, l'indicateur de Belchiat ici, vous venez ici, regardez, dans Tool, et là, vous venez dans Edit Ninja Trader… et là, vous allez dans Belchiat Center, là, et vous avez le code.* »
→ À ce moment, l'**éditeur de code NinjaTrader** est ouvert à l'écran. **Scruber la dernière minute (~11:00 / 12:01).**

### Détail verbatim — `57DtXQp35Eo` (PANNEAU réglages)

Passage l.171-177 — **panneau de réglages FR à l'écran** :

```
171  Et vous vous remarquez bien que sur le gravity center ici,
172  l'écart n'est plus de 1,618, mais de 0,618.
173  Vous le voyez ici.
174  L'ordre, il est de 3.
175  Et bien sûr, vous pouvez changer les périodes.
176  Moi, je recommande 180 en période ici.
177  Mais bien sûr, là, vous pouvez changer la période.
```

Capture EN antérieure (l.127-130, ~70 % du texte, ~14:00/20:27) :
« *…ici, c'est 0.618, instead de 1.618, pour le « Traditional Gravity Center ». Vous pouvez changer l'ordre, ici, et le « Period », comme vous voulez.* »

**Phrase-repère** (l.172/174/176) : « *l'écart n'est plus de 1,618, mais de 0,618… L'ordre, il est de 3… je recommande 180 en période ici.* »

**MARCHÉ + TIMEFRAME de CETTE vidéo** (verbatim) :
- l.2 : « *We see here the chart of the crude oil on range bar, 5 range bar.* »
- l.49-50 : « Nous voyons ici le marché du **pétrole** sur une unité de temps de **5 range bar**. Autrement dit, chaque bougie ici représente **5 ticks**. »
- l.179-180 : « …votre centre de gravité sur le **pétrole**, sur **5 ticks**. Chaque bougie ici représente **5 ticks**. »

### Détail verbatim — `ubKv-05qdbU` (recoupement FR)

Passage l.404-418 — **panneau de réglages** (transcription très fragmentée) :

```
404  que sur le
405  Graffiti Center
406  ici
407  l'écart n'est plus
408  de 1,618
409  mais de 0,618
410  vous le voyez ici
411  l'ordre
412  il est de 3
413  et bien sûr
414  vous pouvez changer
415  les périodes
416  moi je recommande
417  180
418  en période
```

**Phrase-repère** (l.407-418) : « *l'écart n'est plus de 1,618 mais de 0,618… l'ordre il est de 3… moi je recommande 180 en période.* »

**MARCHÉ + TIMEFRAME RÉELLEMENT mentionnés DANS CETTE transcription** (verbatim + ligne — ne PAS supposer identiques aux autres) :
- l.2-3 : « Nous voyons ici le marché du **pétrole** sur une unité de temps de **5 range bar**. Autrement dit, chaque bougie ici représente **5 tics**. »
- l.10-11 : « …utiliser le Belchiat Gravity Center sur une unité de temps courte comme par exemple **5 range bar ou 1 minute**… »
- l.371-374 : « vous voulez mettre **4 range bas ou 5 range bas** » *(« range bas » = transcription Whisper de « range bars »)*.
- l.427-432 : « votre centre de gravité sur le **pétrole** sur **5 ticks**. Chaque bougie ici représente **5 ticks**. »
→ **Identique au TOP 1** (pétrole / 5 range bar) — **confirmé par cette transcription, pas supposé.**

### ÉTAPE 3 — Timeframe EXACT à reproduire (anti-erreur)

| ID | Timeframe / type de bougie à reproduire | Preuve verbatim + ligne |
|---|---|---|
| `TQ7hYcJx9OE` | **OR (gold) en 30 MINUTES** (temps, PAS range bars). Multi-TF aussi évoqué (30/15/10/5/1 min) mais l'écran de base = 30 min. ⚠️ **Le timeframe du moment où le CODE est montré (l.149-152) n'est PAS reprécisé** → pour la capture du code, le timeframe est **NON DÉTERMINANT** (on lit du code, pas un graphique). | l.6 : « ici, nous avons l'**or** sur **30 minutes** » ; l.29 : « …à la fois en 30 minutes, en 15 minutes, en 10 minutes, en 5 minutes, en 1 minute » |
| `57DtXQp35Eo` | **PÉTROLE (crude oil) — barres RANGE de 5 ticks** (chaque bougie = 5 ticks). PAS une unité de temps. | l.49-50 : « le marché du **pétrole** sur une unité de temps de **5 range bar**… chaque bougie ici représente **5 ticks** » |
| `ubKv-05qdbU` | **PÉTROLE — barres RANGE de 5 ticks** (chaque bougie = 5 tics). PAS une unité de temps. | l.2-3 : « le marché du **pétrole** sur une unité de temps de **5 range bar**… chaque bougie ici représente **5 tics** » |

> ⚠️ Anti-erreur : « 5 range bar » = **barres de RANGE (5 ticks d'amplitude par bougie)**, ce n'est **PAS** « 5 minutes ». Reproduire un graphe en minutes fausserait totalement le calage des bandes.

---

> ### 🎯 ENCADRÉ — ORDRE DE CAPTURE
>
> **PRIORITÉ 1 :** https://www.youtube.com/watch?v=TQ7hYcJx9OE — capturer le **CODE** (formule des bandes, éditeur NinjaTrader ouvert) — phrase-repère : «*…vous venez dans Edit Ninja Trader… vous allez dans Belchiat Center, là, et vous avez le code.*» (l.149-150, **~93 % = toute fin de vidéo, ~11:00/12:01**). ⚠️ Code MONTRÉ mais non dicté.
>
> **PRIORITÉ 2 :** https://www.youtube.com/watch?v=57DtXQp35Eo — capturer le **PANNEAU réglages** (0,618 / ordre 3 / période 180) — **crude oil / 5-range (5 ticks)** — phrase-repère : «*l'écart n'est plus de 1,618, mais de 0,618… L'ordre, il est de 3… je recommande 180 en période ici.*» (l.171-177, **~94 % = fin de vidéo**).
>
> **PRIORITÉ 3 :** https://www.youtube.com/watch?v=ubKv-05qdbU — **recoupement** des mêmes réglages — timeframe = **pétrole / 5 range bar (5 ticks)** (confirmé verbatim l.2-3, l.427-432, **pas supposé**) — phrase-repère : «*l'écart n'est plus de 1,618 mais de 0,618… l'ordre il est de 3… 180 en période.*» (l.407-418, **~93 % = fin de vidéo**).
