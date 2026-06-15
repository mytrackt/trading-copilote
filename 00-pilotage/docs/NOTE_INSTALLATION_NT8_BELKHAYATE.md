# NOTE — Installation NinjaTrader 8 selon Belkhayate

> Source : Transcription officielle "Belkhayate Trading : Vidéo 2"
> Fichier : `03-transcriptions/nouvelles-sources/belkhayate-youtube/transcripts/StGyS6POO_Q_Belkhayate Trading ： Vidéo 2.txt`
> Statut : HORS_PÉRIMÈTRE KB trading — documentation projet Phase C uniquement
> ⚠️ Instructions probablement datées (mpfutur.com + CQG ≠ notre stack Rithmic/NTB actuelle)

---

## Ce que Belkhayate recommande

### 1. Compte démo
- URL : **mpfutur.com**
- Chercher "NinjaTrader" sur le site → remplir formulaire → compte démo gratuit
- Astuce Belkhayate : quand la démo expire → créer un nouveau compte avec un autre email

### 2. Provider de flux de données
- Belkhayate utilise : **CQG** (gratuit en démo via mpfutur.com)
- Confirmation en temps réel : bouton **vert** dans NT8 = flux live actif

### 3. Procédure connexion NT8
1. Télécharger NinjaTrader 8 (lien fourni lors de l'inscription mpfutur.com)
2. Ouvrir NT8 → "Ajouter une connexion"
3. Choisir **CQG** comme provider
4. Copier-coller username + password reçus par email
5. Se connecter → vérifier voyant vert

### 4. Marchés disponibles
- Pétrole, Or, etc. (marchés futures CME/CBOT) — cohérent avec nos actifs TRADING

### 5. Coût plateforme réelle
- Belkhayate indique : **~1 000 $** pour la licence NT8 complète (mode live)
- Démo = gratuite et illimitée (en recréant un compte à chaque expiration)

---

## Écart avec notre stack actuelle

| Élément | Belkhayate (vidéo) | TRADEX-AI (actuel) |
|---|---|---|
| Provider flux | CQG | **Rithmic** |
| Broker | mpfutur.com | **NTB** |
| Compte démo | mpfutur.com | NTB |
| Connexion NT8 | CQG plugin | Rithmic plugin |

**Conclusion :** La logique d'installation est identique, seul le provider change.
En Phase C, suivre la même procédure mais choisir **Rithmic** au lieu de CQG.

---

*Créé S11 — 15/06/2026*
