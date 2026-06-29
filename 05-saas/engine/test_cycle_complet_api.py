"""
test_cycle_complet_api.py -- Test cycle complet TRADEX-AI Phase C
NT8 mock -> Phase C data -> get_signal() avec VRAIE API Claude

Test valide si :
  - Claude API repond (pas fallback)
  - Signal contient exactement 15 champs
  - mode_auto_autorise = false
  - confiance dans [0, 100]

Execution (OBLIGATOIRE depuis 05-saas/) :
  cd C:\\trading-copilote\\05-saas
  python -m engine.test_cycle_complet_api

NE PAS lancer avec 'python test_cycle_complet_api.py' (imports relatifs KB echouent).
"""
import os
import sys
import json
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s -- %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("TEST_CYCLE")

# =============================================================================
# CHEMINS ABSOLUS
# =============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 05-saas/
ROOT_DIR = os.path.dirname(BASE_DIR)                                      # C:\trading-copilote\

# =============================================================================
# CHARGER .env AVANT tout import (la cle API doit etre presente au moment
# ou anthropic.Anthropic() est instancie lors de l'import de claude_brain)
# =============================================================================
_env_path = os.path.join(ROOT_DIR, ".env")
if os.path.exists(_env_path):
    with open(_env_path, "r", encoding="utf-8") as _fenv:
        for _line in _fenv:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())
    logger.info(f".env charge depuis {_env_path}")
else:
    logger.warning(f".env introuvable : {_env_path}")

# =============================================================================
# IMPORTS TRADEX-AI (apres chargement .env)
# =============================================================================
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    import engine.claude_brain as cb
    from engine.data_collector_runner import load_current_phase_c
    logger.info("Imports engine.* OK")
except ImportError as e:
    print(f"\n[ERREUR] Import echoue : {e}")
    print("Verifier que vous etes dans C:\\trading-copilote\\05-saas")
    print("Commande : python -m engine.test_cycle_complet_api")
    sys.exit(1)

# =============================================================================
# CONTEXTE NT8 MOCK -- GC / H1, conditions favorables Belkhayate
# Valeurs inspirees de data/mock/GC.json
# =============================================================================
CONTEXT_MOCK = {
    "actif":        "GC",
    "timeframe":    "H1",
    "c1": {
        "bgc_signal":   True,
        "direction":    "LONG",
        "direction_ok": True,
        "timing":       5.2,    # timing Belkhayate (0-10)
    },
    "c2": {
        "delta_positif": True,
        "big_trades_ok": True,
    },
    "risk": {
        "dd_today": 0.005,   # 0.5% -- sous le seuil critique de 2%
        "dd_week":  0.010,   # 1.0%
    },
    "vix":          15.5,    # VIX bas : favorable (< 18)
    "no_news_gate": True,    # aucun evenement macro bloquant
}

# 15 champs obligatoires dans la reponse Claude
CHAMPS_OBLIGATOIRES = [
    "signal", "confiance", "raison", "taille", "taille_contrats",
    "stop_loss", "take_profit", "mode_auto_autorise", "alerte", "score_kb",
    "timing_belkhayate", "bandes_belkhayate", "cot_contexte",
    "macro_contexte", "news_contexte"
]


def _sep(titre: str = "") -> None:
    print(f"\n{'='*62}")
    if titre:
        print(f"  {titre}")
        print(f"{'='*62}")


def _verifier_15_champs(signal: dict) -> tuple:
    """Retourne (ok:bool, manquants:list)."""
    manquants = [c for c in CHAMPS_OBLIGATOIRES if c not in signal]
    return len(manquants) == 0, manquants


def main() -> int:

    # ---------------------------------------------------------------
    # ETAPE 0 -- Verifier cle API
    # ---------------------------------------------------------------
    _sep("TEST CYCLE COMPLET TRADEX-AI -- Phase C Track B")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERREUR : ANTHROPIC_API_KEY absente")
        print("  -> Verifier que .env contient ANTHROPIC_API_KEY=sk-ant-...")
        return 1
    print(f"  ANTHROPIC_API_KEY : {api_key[:16]}... OK")
    print(f"  Actif mock        : {CONTEXT_MOCK['actif']} / {CONTEXT_MOCK['timeframe']}")

    # ---------------------------------------------------------------
    # ETAPE 1 -- Charger KB Belkhayate
    # ---------------------------------------------------------------
    _sep("ETAPE 1 -- Chargement KB (4142 regles attendues)")
    t0 = time.time()
    kb_result = cb.load_kb_rules()
    kb_rules   = kb_result["rules"]
    kb_prov    = kb_result.get("kb_provisoire", False)
    kb_nb_car  = len(kb_rules)
    t_kb = time.time() - t0

    print(f"  KB chargee en {t_kb:.2f}s")
    print(f"  Taille texte   : {kb_nb_car:,} caracteres")
    print(f"  kb_provisoire  : {kb_prov}")

    if kb_nb_car < 50_000:
        print("  AVERTISSEMENT : KB tres courte -- verifier KNOWLEDGE_BASE_MASTER.json")

    # ---------------------------------------------------------------
    # ETAPE 2 -- Charger donnees Phase C (fichiers JSON existants)
    # ---------------------------------------------------------------
    _sep("ETAPE 2 -- Chargement donnees Phase C (lecture seule)")
    try:
        phase_c = load_current_phase_c()
        cot_ok   = bool(phase_c.get("cot"))
        macro_ok = bool(phase_c.get("macro"))
        news_ok  = bool(phase_c.get("news"))
        print(f"  COT   : {'OK' if cot_ok  else 'VIDE (cot_data.json absent ou vide)'}")
        print(f"  MACRO : {'OK' if macro_ok else 'VIDE (macro_data.json absent ou vide)'}")
        print(f"  NEWS  : {'OK' if news_ok  else 'VIDE (news_data.json absent ou vide)'}")
        if not any([cot_ok, macro_ok, news_ok]):
            print("  -> Lancer d'abord : python -m engine.data_collector_runner --force")
    except Exception as e:
        logger.error(f"Erreur Phase C : {e}")
        phase_c = {"cot": {}, "macro": {}, "news": {}}
        print(f"  ERREUR Phase C ({e}) -- contexte vide injecte")

    # ---------------------------------------------------------------
    # ETAPE 3 -- Appel Claude API via get_signal()
    # ---------------------------------------------------------------
    _sep("ETAPE 3 -- Appel Claude API (get_signal)")
    print("  Envoi prompt GOD_MODE a claude-sonnet-4-6...")
    print("  Attendre 15-30 secondes...\n")

    t1 = time.time()
    signal = cb.get_signal(
        context=CONTEXT_MOCK,
        kb_rules=kb_rules,
        kb_provisoire=False,
        phase_c_data=phase_c
    )
    t_api = time.time() - t1
    print(f"  Reponse recue en {t_api:.1f}s")

    # ---------------------------------------------------------------
    # ETAPE 4 -- Validation 15 champs + regles absolues
    # ---------------------------------------------------------------
    _sep("ETAPE 4 -- Validation signal")

    ok_15, manquants = _verifier_15_champs(signal)
    print(f"  15/15 champs      : {'OK' if ok_15 else 'KO -- manquants : ' + str(manquants)}")

    ok_auto = signal.get("mode_auto_autorise") is False
    print(f"  mode_auto=false   : {'OK' if ok_auto else 'VIOLATION'}")

    confiance = signal.get("confiance", -1)
    ok_conf = 0 <= confiance <= 100
    print(f"  confiance [0-100] : {confiance} -> {'OK' if ok_conf else 'KO'}")

    raison = str(signal.get("raison", ""))
    source_api = "FALLBACK" not in raison and "FALLBACK" not in str(signal.get("alerte", ""))
    print(f"  Source signal     : {'CLAUDE_API' if source_api else 'FALLBACK_LOCAL'}")

    if not source_api:
        alerte = signal.get("alerte", "")
        print(f"  Alerte fallback   : {alerte}")
        print("  -> Verifier la cle API et la connexion Internet")

    # ---------------------------------------------------------------
    # ETAPE 5 -- Affichage signal complet
    # ---------------------------------------------------------------
    _sep("SIGNAL COMPLET (15 champs)")
    for champ in CHAMPS_OBLIGATOIRES:
        val = signal.get(champ, "<<ABSENT>>")
        marker = "" if champ in signal else " [ABSENT]"
        print(f"  {champ:22s} : {val}{marker}")

    # ---------------------------------------------------------------
    # BILAN FINAL
    # ---------------------------------------------------------------
    _sep("BILAN FINAL")
    tests = {
        "KB chargee"         : kb_nb_car > 50_000,
        "15 champs presents" : ok_15,
        "mode_auto=false"    : ok_auto,
        "confiance valide"   : ok_conf,
        "Source = Claude API": source_api,
    }
    all_ok = all(tests.values())
    for nom, res in tests.items():
        print(f"  {'OK' if res else 'KO'}  {nom}")

    print(f"\n  => {'TEST REUSSI (cycle complet avec vraie API)' if all_ok else 'TEST PARTIEL -- voir details ci-dessus'}")

    if all_ok:
        print("\n  Prochaine etape : Phase C Track B terminee.")
        print("  -> Correctifs P2 (News Gate post-event, _collected_at)")
        print("  -> Puis mise en route moteur temps reel NT8")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
