# RAPPORT D'EXPLORATION — `D:\TRADING MBK`

> **Nature de cette passe :** reconnaissance en **LECTURE SEULE**. Rien n'a été copié, déplacé, renommé ou supprimé. Aucun fichier n'a été extrait sur le disque D:. Le seul fichier écrit est le présent rapport.
> **Date d'exploration :** 2026-06-17
> **Méthode :** arborescence + ouverture du contenu réel (lecture en mémoire des archives, lecture des sources, métadonnées PDF, lecture visuelle des images). Le **nom d'un fichier n'est qu'un indice** ; les constats ci-dessous reposent sur le contenu ouvert, sauf mention « non lisible ».

---

## SOMMAIRE
1. Carte générale (Phase 0)
2. Contenu par sous-dossier (Phase 1)
3. Aperçu par fichier (Phase 2)
4. Synthèse d'exploration (Phase 3)
5. Questions ouvertes (décisions attendues)
6. Encadré récapitulatif

---

## 1. CARTE GÉNÉRALE (Phase 0)

**Total : 37 fichiers — 6 sous-dossiers — ~704,5 Mo (704 541 665 octets).**

### Arborescence (tous niveaux)

```
D:\TRADING MBK\
│  (racine : 8 fichiers — ~226,4 Mo)
│
├─ IDM 2012+crack\                                    3 fichiers — ~4,6 Mo
│   └─ crack\                                         1 fichier  — ~0,3 Mo
│
├─ Indicateurs\                                       9 fichiers — ~0,69 Mo
│
├─ MBK VIP Groupe\                                   12 fichiers — ~37,6 Mo
│   └─ Explications Des indicateurs Belkhayate\       1 fichier  — ~433,6 Mo
│
└─ Ninja Workspace - Templates\                       3 fichiers — ~1,29 Mo
```

> Aucun dossier système masqué de type `d---s` rencontré ; aucun accès refusé. Présence de fichiers système mineurs (`desktop.ini`, `movie.ini`) dans `IDM 2012+crack`.

### Tableau par extension (fichiers « en clair » sur le disque)

| Catégorie / extension | Nombre | Remarque |
|---|---:|---|
| `.cs` (source C#) | 0 en clair | **Tout le code C# est à l'intérieur des archives** (voir §3) |
| `.dll` | 0 en clair | 6 instances **dans** les archives `.zip` |
| `.mq4 / .mq5 / .ex4 / .ex5` | 0 | Aucun fichier MetaTrader |
| `.pdf` | 6 | |
| `.md / .txt / .docx` | 2 (`.txt`) | dont 1 = code (Pine Script) |
| `.mp4 / .avi / .mkv` | 2 (`.mp4`) | |
| `.png / .jpg` | 2 | ⚠️ documents d'identité (voir §4) |
| `.xlsx / .csv` | 1 (`.xlsx`) | |
| `.lnk / .url` | 4 (`.lnk`) | cibles **hors** périmètre |
| `.zip` | 11 | contiennent code + binaires |
| `.rar` | 1 | **non listable** (aucun outil RAR disponible) |
| `.xml` | 4 | workspaces/templates NinjaTrader |
| `.exe` | 2 | logiciel + crack (voir « À signaler ») |
| `.ini` | 2 | fichiers système (IDM) |
| crack / keygen | 1 patch (`patsh.exe`) | à signaler |
| **Total** | **37** | |

---

## 2. CONTENU PAR SOUS-DOSSIER (Phase 1)

### Racine `D:\TRADING MBK\`
Mélange hétérogène : 1 grosse vidéo « erreurs des traders » (~226 Mo), 2 documents d'identité (passeport + photo CV), 4 raccourcis vers des formations situées ailleurs, 1 workspace NinjaTrader (`Carnet D'ordre.xml`). **Pas de code ici.** Dossier « fourre-tout » personnel + pointeurs.

### `IDM 2012+crack\` (+ `crack\`)
Contient **Internet Download Manager** (`idman607.exe`) accompagné d'un patch (`crack\patsh.exe`) et de fichiers `.ini`. **Sans rapport avec le trading** ; logiciel + outil de contournement de licence (voir « À signaler »).

### `Indicateurs\`
Cœur technique « indicateurs » : 8 archives `.zip` d'indicateurs **NinjaTrader 8** (code C# + DLL) + 1 classeur Excel « plan de trading ». On y trouve à la fois du code Belkhayate, des indicateurs publics NinjaTrader, et des indicateurs order-flow tiers (dont un commercial sous licence).

### `MBK VIP Groupe\` (+ `Explications Des indicateurs Belkhayate\`)
Contenu « premium / VIP » : archives d'indicateurs Belkhayate (surtout des **DLL binaires**), plusieurs PDF (documents conceptuels, marketing/projet, code « Smeers »), 2 fichiers texte, une grosse archive `.rar` (~18 Mo, non lisible) et **une vidéo explicative de ~433 Mo** (la plus grosse pièce du dossier). Mélange cours + binaires + documents de projet.

### `Ninja Workspace - Templates\`
3 fichiers `.xml` = espaces de travail / templates NinjaTrader 8 (« MBK Système », « Zakaria Workspace », « Carnet D'ordre »). Configuration d'interface, pas du code de calcul.

---

## 3. APERÇU PAR FICHIER (Phase 2)

### A) CODE SOURCE (ouvert et lu)

> Tous les `.cs` sont **à l'intérieur des `.zip`** ; lus en mémoire sans extraction.

**`Indicateurs\belkhayate direction-NT8.zip`**
- `Indicators/belkhayate direction .cs` — ⚠️ **NOM ≠ CONTENU**. Le contenu réel est un indicateur **« Chande Kroll Stop »**, classe `amaChandeKrollStop`. **Copyright © 2021 LizardIndicators.com – AlderLab UG**, licence GNU GPL v3. Calcul présent : **OUI** (stop de volatilité basé ATR). Paramètres par défaut : **OUI** (`length=20`, `periodATR=10`, `multiplier=3.0`). → Ce n'est **pas** un indicateur « direction Belkhayate ».
- `ATR.cs`, `@MAX.cs`, `@MIN.cs`, `@SMA.cs`, `@EMA.cs` — briques de calcul standard NinjaTrader (ATR, max, min, moyennes). Calcul : OUI. **Semblent standard/public.**

**`Indicateurs\Belkhayate Gravity Center - NT8 (1).zip`**
- `Indicators\JOO\JOOBelkhayateCOG.cs` — classe `JOOBelkhayateCOG` (namespace auteur **« JOO »**). Contient une **régression polynomiale par matrice** (`double[10,10]`, résolution de système) = calcul d'un **Center of Gravity / canal de Belkhayate**. Calcul : **OUI**. Paramètres par défaut : description laissée en placeholder (« Enter the description… »). → **Semble Belkhayate (COG)**, portage tiers signé « JOO ».

**`Indicateurs\FootPrint_NT8_FreeCode.zip`**
- `Indicators\Infinity\FootPrint.cs` (~70 Ko) — classe `FootPrint` (namespace **Infinity**). Indicateur **footprint / volume par niveau de prix**. Calcul : OUI. → **Semble standard/public** (« FreeCode »).

**`Indicateurs\NTSvePivots-Indicator-NT8.zip`**
- `Indicators\NTSvePivots.cs` — **Copyright © 2018 NinjaTrader LLC**. Indicateur de **points pivots**. Calcul : OUI. → **Standard/public (éditeur NinjaTrader)**.

**`Indicateurs\OrderFlowsTrader_NT8.zip`** (~50 fichiers `.cs`)
- `Indicators/OrderFlowsTrader.cs` (~68 Ko) — classe `OrderFlowsTrader : IndicatorMallFootprintBase`. Catégorie « License » + `AddOns/LicensingManager.cs` (~37 Ko) → **indicateur order-flow COMMERCIAL sous licence** (famille « IndicatorMall / Orderflows »). Calcul : OUI (footprint, imbalance, delta, POC…). → **Tiers commercial**, pas Belkhayate.

**`Indicateurs\MbkIndicators_v3.zip`** et **`Indicateurs\MbkIndicators trend + cycle.zip`** (⚠️ **doublons exacts**, voir §4)
- `MbkIndicators_v3.cs` — uniquement le **code « glue » auto-généré** NinjaScript ; référence `Belkhayate.BelkhayateCycle(period)` et `Belkhayate.BelkhayateTrend()`. **La logique réelle est dans `MbkIndicators_v3.dll` (binaire).** Calcul lisible dans le `.cs` : NON (déporté en DLL). → indices : indicateurs Belkhayate « Cycle » et « Trend ».

**`MBK VIP Groupe\EMG_NT8_v1 (1).zip`**
- `EMG_NT8_v1.cs` — **stub vide** (aucune logique). Tout est dans `EMG_NT8_v1.dll` (binaire). Calcul lisible : NON.

**`MBK VIP Groupe\TokyoSessionRange.txt`** (fichier texte, mais c'est du code)
- **Pine Script v6 (TradingView)**, indicator `"Tokyo Session"`, **© SeekingMastery**, licence MPL 2.0. Trace la plage horaire de la session de Tokyo. Calcul : OUI. → **≠ Belkhayate**, indicateur public TradingView.

**`MBK VIP Groupe\BelkhayateOrderFlowV1.zip` → `AdditionalReferences.txt`**
- Simple **liste de références de compilation** NinjaTrader 8 (DLL système + NinjaTrader.Core/Gui/SharpDX). Pas un cours, pas une formule.

### B) BINAIRES (⚫ non lisibles — aucune décompilation effectuée)
*Indices tirés du nom = non vérifiables.*

| Fichier (dans archive) | Taille | Indice (nom, NON vérifié) |
|---|---:|---|
| `Indicateurs\Colored Vwap - NT8.zip → MbkVwapV01.dll` | ~595 Ko | VWAP coloré « Mbk » |
| `Indicateurs\MbkIndicators_v3.zip → MbkIndicators_v3.dll` | ~678 Ko | Belkhayate Cycle + Trend |
| `Indicateurs\MbkIndicators trend + cycle.zip → MbkIndicators_v3.dll` | ~678 Ko | (copie du précédent) |
| `MBK VIP Groupe\Belkhayate_Copy_TradeVBETA.zip → …VBETA.dll` | ~730 Ko | « copy trade » Belkhayate (bêta) |
| `MBK VIP Groupe\BelkhayateOrderFlowV1.zip → …V1.dll` | ~4,4 Mo | order flow Belkhayate |
| `MBK VIP Groupe\EMG_NT8_v1 (1).zip → EMG_NT8_v1.dll` | ~545 Ko | « EMG » |
| `IDM 2012+crack\idman607.exe` | ~4,3 Mo | Internet Download Manager 6.07 |
| `IDM 2012+crack\crack\patsh.exe` | ~313 Ko | **patch/crack** (voir « À signaler ») |

### C) DOCUMENTS (PDF / Excel / XML)

> **PDF** : exportés depuis **Google Docs** (producteur « Skia/PDF Google Docs Renderer »). Le **texte n'a pas pu être extrait** (polices sous-ensemble / CMap personnalisée, et aucun `pdftotext`/Python fonctionnel sur la machine). **Titres** récupérés via métadonnées ; thèmes ci-dessous = déduction à partir du **titre uniquement** (non vérifiés page par page).

| PDF (dans `MBK VIP Groupe\`) | Taille | Titre (métadonnée) — thème probable | Formules/params ? |
|---|---:|---|---|
| `code Smeers .pdf` | ~48 Ko | « code Smeers » — doc technique/code | non vérifié |
| `cadeau pour mes abonnes VIP.pdf` | ~372 Ko | « cadeau pour mes abonnés VIP » — marketing/bonus | non vérifié |
| `sachant_que_je_veux_decortiquer_…3_phases.pdf` | ~22 Ko | Concept : combiner **constante de Feigenbaum** (sur le carnet d'ordres) + **coefficients de Lyapunov** pour identifier en temps réel 3 phases de marché (imprévisible / repos / prévisible) | conceptuel ; 🔴 à vérifier |
| `Why This Project Can Interest BlackRock.pdf` | ~85 Ko | « Why This Project Can Interest BlackRock » — pitch/projet | non vérifié |
| `JSTX Financial Projections_ Unlocking Africa's Potential.pdf` | ~76 Ko | « JSTX Financial Projections: Unlocking Africa's Potential » — projections financières/business | 🔴 chiffres non vérifiés |
| `AI World Championship v.2 (2).pdf` | ~13,8 Mo | **Aucune métadonnée, aucun texte extractible** — volumineux (probable PDF riche en images). Contenu non vérifiable sans ouverture manuelle. | non vérifié |

**Excel — `Indicateurs\MBK +PLAN+DE+TRADING (1).xlsx`**
- Lu (chaînes internes). C'est un **template « PLAN DE TRADING MBK SYSTEM »** : checklist avant séance, gestion du risque (taille de position **0,5–2 % / trade**, pertes consécutives 3–10, arrêt si perte > X %), stratégie déclarée = **VWAP + Volume + RSI**, unité **15 min**, séance **9h–17h**, règles d'achat/vente autour du **VWAP** (cassure, effet ressort, volume). Contient des **paramètres** : OUI.

**XML — workspaces / templates NinjaTrader 8** (`<NinjaTrader>…`)
- `Carnet D'ordre.xml` (racine) & `Ninja Workspace - Templates\Carnet D'ordre.xml` — **doublons exacts** (voir §4). Onglet « carnet d'ordre ».
- `Ninja Workspace - Templates\MBK Système.xml` — espace de travail « MBK Système ».
- `Ninja Workspace - Templates\Zakaria Workspace.xml` (~1,2 Mo) — espace de travail complet (Market Analyzer, fenêtres). Configuration d'UI, pas de formule.

### D) VIDÉOS / IMAGES

| Fichier | Taille | Constat |
|---|---:|---|
| `90% des traders font ces erreurs ! … (1).mp4` (racine) | ~226 Mo | Vidéo pédagogique/marketing. Durée non mesurée (pas d'outil média). Source potentielle — non « lue ». |
| `MBK VIP Groupe\…\1060xzy.mp4` | ~433,6 Mo | « Explications des indicateurs Belkhayate ». Plus gros fichier du dossier. Durée non mesurée. Source potentielle — non « lue ». |
| `20250303_121830.jpg` (racine) | ~217 Ko | ⚠️ **Image d'un PASSEPORT** (pièce d'identité, données personnelles sensibles). **Aucun code / aucun panneau de réglages.** |
| `2025-06-14 … Cv zakaria … .png` (racine) | ~63 Ko | Photo d'identité type CV (capture d'écran Edge). **Aucun code / aucun panneau de réglages.** Donnée personnelle. |

### E) RACCOURCIS (.lnk) — cibles résolues

| Raccourci (racine) | Cible résolue | Dans le périmètre ? |
|---|---|---|
| `Belkhayat Formation 2 - Raccourci.lnk` | `D:\Bureau\Formations Trading\Belkhayat Formation 2` | ❌ **hors** `D:\TRADING MBK` |
| `Belkhayate Formation Order Flow Francais - Raccourci.lnk` | `D:\Bureau\Formations Trading\Belkhayate Formation Order Flow Francais` | ❌ hors périmètre |
| `BELKHAYATE GOLD - Raccourci.lnk` | `D:\Bureau\Formations Trading\BELKHAYATE GOLD` | ❌ hors périmètre |
| `Michael Valtos - Order Flow Trading Course - Raccourci.lnk` | `D:\Bureau\Formations Trading\Michael Valtos - Order Flow Trading Course` | ❌ hors périmètre |

> Les 4 raccourcis pointent vers `D:\Bureau\Formations Trading\` (existence des cibles **non vérifiée** — hors périmètre de cette passe).

### F) À SIGNALER (sans juger)
- 🛑 **Logiciel craqué** : `IDM 2012+crack\` = Internet Download Manager (`idman607.exe`) + **patch de contournement de licence** (`crack\patsh.exe`). Sans rapport avec le trading.
- 🔒 **Données personnelles sensibles** : `20250303_121830.jpg` = **passeport** (nom, photo, n°, MRZ). + `…Cv zakaria….png` = photo CV. (Détails non recopiés ici.)
- 📦 **Archive non listable** : `MBK VIP Groupe\MBK VIP Groupe.rar` (~18,4 Mo) — **aucun outil RAR/7z présent**, contenu **non vérifié**.
- ♊ **Doublons exacts confirmés (hash MD5 identiques)** :
  - `Indicateurs\MbkIndicators_v3.zip` ≡ `Indicateurs\MbkIndicators trend + cycle.zip`
  - `Carnet D'ordre.xml` (racine) ≡ `Ninja Workspace - Templates\Carnet D'ordre.xml`
- 🏷️ **Étiquette trompeuse** : `belkhayate direction .cs` = en réalité un **Chande Kroll Stop** (LizardIndicators), pas un indicateur de direction Belkhayate.
- 🗂️ Fichiers système mineurs : `IDM 2012+crack\desktop.ini`, `movie.ini`.

---

## 4. SYNTHÈSE D'EXPLORATION (Phase 3)

### Tableau récapitulatif

| Chemin (relatif à `D:\TRADING MBK`) | Type | Identité réelle (si code) | Calcul ? | Remarque |
|---|---|---|---|---|
| `\…belkhayate direction .cs` *(zip)* | Code C# | `amaChandeKrollStop` (LizardIndicators ©2021) | Oui | ⚠️ nom ≠ contenu |
| `\…ATR/@SMA/@EMA/@MAX/@MIN .cs` *(zip)* | Code C# | briques standard NinjaTrader | Oui | public |
| `\…JOOBelkhayateCOG.cs` *(zip)* | Code C# | `JOOBelkhayateCOG` (COG, auteur « JOO ») | Oui | semble Belkhayate |
| `\…FootPrint.cs` *(zip)* | Code C# | `FootPrint` (Infinity) | Oui | public/free |
| `\…NTSvePivots.cs` *(zip)* | Code C# | `NTSvePivots` (NinjaTrader LLC ©2018) | Oui | public |
| `\…OrderFlowsTrader.cs` (+~50 .cs) *(zip)* | Code C# | `OrderFlowsTrader` + LicensingManager | Oui | tiers **commercial** |
| `\…MbkIndicators_v3.cs` *(zip ×2)* | Code C# (glue) | wrappers `BelkhayateCycle/Trend` → DLL | Non (en DLL) | doublon |
| `\…EMG_NT8_v1.cs` *(zip)* | Code C# (stub) | vide → DLL | Non (en DLL) | — |
| `\…TokyoSessionRange.txt` | Code Pine v6 | `"Tokyo Session"` (SeekingMastery) | Oui | public TradingView |
| `\…*.dll` *(zip ×6)* | Binaire | — | ⚫ non lisible | indices nom only |
| `\IDM…\idman607.exe`, `crack\patsh.exe` | Binaire | — | ⚫ non lisible | crack |
| `\MBK VIP\*.pdf` (×6) | Document | — | partiel/non vérifié | texte non extractible |
| `\Indicateurs\MBK…PLAN DE TRADING.xlsx` | Tableur | — | Oui (params) | plan VWAP/Vol/RSI |
| `\…*.xml` (×4) | Config NT8 | — | Non | workspaces; 2 en doublon |
| `\…*.mp4` (×2) | Vidéo | — | — | non lues; 226 Mo + 434 Mo |
| `\…passeport.jpg`, `…CV.png` | Image | — | Non (pas de code) | 🔒 PII |
| `\…*.lnk` (×4) | Raccourci | — | — | cibles hors périmètre |
| `\MBK VIP\MBK VIP Groupe.rar` | Archive | — | ⚫ non listable | pas d'outil RAR |

### Listes thématiques brutes

**Code source lisible (hypothèses d'attribution — à confirmer ensemble) :**
- *Semble Belkhayate :* `JOOBelkhayateCOG.cs` (COG) ; `MbkIndicators_v3.cs` (wrappers Cycle/Trend, logique en DLL).
- *Semble standard / public :* `ATR/@SMA/@EMA/@MAX/@MIN.cs`, `FootPrint.cs` (Infinity), `NTSvePivots.cs` (NinjaTrader LLC), `TokyoSessionRange.txt` (SeekingMastery).
- *Tiers tiers/commercial, ≠ Belkhayate :* `belkhayate direction .cs` (= Chande Kroll Stop, LizardIndicators) ; `OrderFlowsTrader.cs` (+modules, sous licence).
- *Incertain (logique en binaire) :* `EMG_NT8_v1.cs` (stub vide).

**Binaires non lisibles :** `MbkVwapV01.dll`, `MbkIndicators_v3.dll` (×2), `Belkhayate_Copy_TradeVBETA.dll`, `BelkhayateOrderFlowV1.dll`, `EMG_NT8_v1.dll`, `idman607.exe`, `patsh.exe`.

**Documents / cours :** 6 PDF (concept Feigenbaum/Lyapunov, pitch BlackRock, JSTX Africa, « code Smeers », bonus VIP, AI World Championship), 1 Excel (plan de trading MBK), 4 XML (workspaces NT8).

**Vidéos / images :** 2 vidéos (erreurs des traders 226 Mo ; explications indicateurs Belkhayate 434 Mo), 2 images (passeport, photo CV).

**Raccourcis (+ cibles) :** 4 `.lnk` → tous vers `D:\Bureau\Formations Trading\…` (hors périmètre).

**À signaler :** crack IDM (+patch) ; passeport + photo CV (PII) ; `.rar` non listable ; 2 paires de doublons exacts ; étiquette trompeuse `belkhayate direction` ; `.ini` système.

> 🔴 **Claims non vérifiés** : tout chiffre de performance/projection (PDF JSTX, BlackRock) et le concept Feigenbaum/Lyapunov n'ont **pas** été vérifiés (texte PDF non extractible). À traiter comme hypothèses.

---

## 5. QUESTIONS OUVERTES (décisions attendues — on tranche ensemble)

1. **Vidéos lourdes (~660 Mo à elles deux)** : garde-t-on les 2 `.mp4` dans le futur classement, ou archivage séparé / suppression ?
2. **Doublons** : pour `MbkIndicators_v3.zip` ≡ `MbkIndicators trend + cycle.zip` (identiques) et `Carnet D'ordre.xml` (racine) ≡ celui des templates — lequel garde-t-on, lequel écarte-t-on ?
3. **Dossier `IDM 2012+crack` (logiciel craqué)** : hors trading et légalement sensible — on l'exclut totalement du périmètre « trading » ?
4. **Documents d'identité (passeport `.jpg` + photo CV `.png`)** : à sortir du dossier trading et sécuriser à part ? (données personnelles)
5. **Archive `MBK VIP Groupe.rar` (~18 Mo, non listable)** : faut-il installer/autoriser un outil RAR pour l'inventorier lors d'une prochaine passe ?
6. **PDF non extractibles (Google Docs)** : souhaites-tu une passe dédiée avec rendu page→image (outil OCR/`pdftoppm`) pour en lire le contenu réel, notamment `AI World Championship v.2` (14 Mo) ?
7. **Indicateurs binaires (`.dll` Belkhayate, EMG, VWAP, Copy Trade)** : leur logique est inaccessible sans décompilation (non faite). Veux-tu, plus tard, retrouver les **sources** correspondantes plutôt que les DLL ?
8. **Étiquette trompeuse** `belkhayate direction` (= Chande Kroll Stop tiers) : on le reclasse en « indicateur tiers » et on cherche le **vrai** indicateur de direction Belkhayate ailleurs (ex. cibles des raccourcis `D:\Bureau\Formations Trading`) ?

---

## 6. ENCADRÉ RÉCAPITULATIF

```
┌────────────────────────────────────────────────────────────────────────────┐
│ EXPLORÉ : 37 fichiers / 6 dossiers                                           │
│ CODE SOURCE LISIBLE : ~65 fichiers .cs/.txt (dans archives) —                │
│                       9 modules clés identifiés (2 « semblent Belkhayate »)  │
│ BINAIRES : 8 (.exe ×2 + .dll ×6, dans archives) — non lisibles               │
│ DOCS : 11 (6 PDF + 1 Excel + 4 XML workspaces)                               │
│ VIDÉOS/IMAGES : 4 (2 vidéos + 2 images)                                      │
│ RACCOURCIS : 4 (toutes cibles hors périmètre)                                │
│ À SIGNALER : 6 (crack IDM, PII passeport+CV, .rar non listable,              │
│                 2 paires de doublons, étiquette trompeuse)                   │
│ DÉCISIONS ATTENDUES : 8 (voir §5 Questions ouvertes)                         │
└────────────────────────────────────────────────────────────────────────────┘
```

*Fin du rapport — passe en lecture seule. Aucune décision de tri prise ; aucun fichier modifié.*
