# Extraction_NinjaTrader_VolumeProfileShapes_v1.md
**Source :** NinjaTrader (blog) — Volume Profile Shapes: The 4 Patterns Every Futures Trader Should Know  
**URL :** https://ninjatrader.com/futures/blogs/trade-futures-understanding-the-4-common-volume-profile-shapes/  
**Décisions :** D163 → D167  
**Images :** 0 (page texte · scraper_static v1.1)  
**Date extraction :** 23/06/2026  
**Nature source :** Tier 2 — blog plateforme (NinjaTrader). Comble P2 #10 (VWAP/Volume Profile).

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — VOLUME PROFILE : LES 4 FORMES

### D163 — Volume Profile : définition et formes

🟢 **FAIT VÉRIFIÉ** (Source : volume_profile_shapes.md §intro) : Le **volume profile** affiche le volume total exécuté à chaque niveau de prix sur une période, tracé **horizontalement** sur l'axe des prix. Contrairement à une barre de volume par intervalle de temps, il révèle **où le marché a passé le plus de volume** — exposant support, résistance et zones de valeur. Les formes récurrentes (**D, P, b, B**) signalent balance, épuisement ou continuation de tendance.

**TRADEX-AI C2/C1** : Volume profile = lecture horizontale du volume (vs footprint intra-barre D112). POC + value area (68 %, cf. D151) + nœuds haut/bas volume.

---

### D164 — P-Shape (haussier)

🟢 **FAIT VÉRIFIÉ** (Source : volume_profile_shapes.md §P-Shaped) : Une forme **P** se forme quand le marché monte fortement puis consolide. Partie basse longue et fine = rejet à faible volume ; partie haute large = prix « juste » atteint, activité élevée. Souvent en uptrend, mais peut marquer la fin d'un downtrend (**short covering** = force temporaire). **Généralement signal haussier.**

**TRADEX-AI C1/C2** : P-shape = short covering / consolidation haute. Recoupe le 'P' Market Profile (D155, accumulation/short covering).

---

### D165 — b-Shape (baissier)

🟢 **FAIT VÉRIFIÉ** (Source : volume_profile_shapes.md §b-Shaped) : Une forme **b** se forme quand le marché chute fortement puis consolide (opposé du P) — résultat d'une **long liquidation**. Partie haute longue et fine = faible volume, prix « injuste » ; partie basse large = nouvelle balance. Commune en downtrend ; un b en uptrend peut indiquer un **retournement**. **Généralement signal baissier.**

**TRADEX-AI C1/C2** : b-shape = long liquidation. Recoupe le 'b' Market Profile (D155, liquidation).

---

### D166 — D-Shape (balance)

🟢 **FAIT VÉRIFIÉ** (Source : volume_profile_shapes.md §D-Shaped) : Une forme **D** = balance temporaire, **POC au centre** (équilibre acheteurs/vendeurs). Interprétable comme marché sans direction, MAIS les traders order-flow patients recherchent les D-shapes en **anticipation d'un breakout** (les institutionnels construisent leurs positions).

**TRADEX-AI C1** : D-shape = range/équilibre → préparer un breakout (cf. trading range Wyckoff D103, construction de cause).

---

### D167 — B-Shape (continuation)

🟢 **FAIT VÉRIFIÉ** (Source : volume_profile_shapes.md §B-Shaped) : Une forme **B** = deux D-shapes dans la période (une seule value area/POC, mais séparable en deux « D-areas »). Généralement **continuation de tendance** ; noter quel **POC est dominant** (activité max en haut ou en bas).

**TRADEX-AI C1/C2** : B-shape = double distribution → continuation. Le POC dominant indique le biais. Cohérent avec les single prints séparant distributions (D154).

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D163
Dernière décision session  : D167
Prochaine décision         : D168
Total décisions            : 5
Total KB cumulé            : D1 → D167
```

---

*Extraction_NinjaTrader_VolumeProfileShapes_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
