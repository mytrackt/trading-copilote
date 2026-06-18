"""
Script S16 — Application des verdicts humains sur les 45 règles AMBIGU
Résultats: 33 → VALIDE | 7 → INVALIDE | 5 → restent AMBIGU
"""
import json
import os
import tempfile

KB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "KNOWLEDGE_BASE_MASTER.json")

# Verdicts par numéro de règle (ordre dans la liste AMBIGU extraite de la KB)
# Basé sur la pré-analyse S16 (cohérence méthode Belkhayate, confirmé par Abdelkrim)
VERDICTS = {
    1:  "VALIDE",    # Sortir dès signal de sortie (principe fondamental)
    2:  "INVALIDE",  # Fin de journée blé 20h Paris (horaire non vérifié)
    3:  "VALIDE",    # Couloir horaire optimal
    4:  "INVALIDE",  # Trades très courts, entrer/sortir vite (contraire méthode)
    5:  "VALIDE",    # Résistances 1&2 pivots Belkhayate
    6:  "VALIDE",    # Belkhayate Direction retournement = changement tendance
    7:  "VALIDE",    # BGC comme indicateur tendance
    8:  "VALIDE",    # Test répété résistance → cassure = force
    9:  "VALIDE",    # Pivots + clôture veille = matelas
    10: "VALIDE",    # Objectif = prochain niveau pivot
    11: "AMBIGU",    # Belkhayate 19 > 40 (indicateur non vérifié)
    12: "VALIDE",    # Confirmer signal sortie par clôture
    13: "INVALIDE",  # Bougie impulsion significativement plus longue (critère flou)
    14: "AMBIGU",    # Signal vente avec bougie noire (sans source vidéo claire)
    15: "VALIDE",    # Signaux rouges répétés CGC → probabilité augmente
    16: "VALIDE",    # Attendre cassure confirmée MA 209
    17: "INVALIDE",  # En tendance, target proche du stop loss (contraire R/R 1:2)
    18: "VALIDE",    # Instruction limitation perte au courtier (garde-fou)
    19: "VALIDE",    # Rentrer acheteur quand reteste clôture veille
    20: "VALIDE",    # Travailler 1 tick gain / 1 tick perte (scalping confirmé)
    21: "VALIDE",    # Sortir en fin de journée ~20h même si mouvement continu
    22: "VALIDE",    # Marché monte sans volume/mèche → accumulation
    23: "VALIDE",    # Prendre profits au prochain niveau pivot
    24: "VALIDE",    # Sortir à l'intégralité sur mèche haute (wick)
    25: "VALIDE",    # Configuration reste baissière même si cassure avec force
    26: "AMBIGU",    # Impulsion terminée quand tremplins diminuent (à vérifier vidéo)
    27: "VALIDE",    # Ancienne résistance → nouveau support (flip)
    28: "VALIDE",    # Test répété résistance → puis cassure force
    29: "VALIDE",    # Pull-back après cassure support = normal
    30: "VALIDE",    # Absence attaque vendeuse → algos pas là
    31: "AMBIGU",    # Pattern ABCD avec mèche au point D (à vérifier vidéo)
    32: "VALIDE",    # Pattern tir à l'arc (squeeze)
    33: "AMBIGU",    # Signal cassure rectangle avec bougie (à vérifier vidéo)
    34: "VALIDE",    # Grande bougie baissière en tendance haussière = appât algos
    35: "VALIDE",    # Observer volumes après entrée pour confirmer
    36: "VALIDE",    # Grand volume sans impulsion = pas confirmation
    37: "INVALIDE",  # Marché monte sans volume = étrangler vendeurs (formulation hasardeuse)
    38: "VALIDE",    # Surliquidité mondiale se retire → toutes classes actifs
    39: "INVALIDE",  # Marché monte doucement sans volume = étrangler vendeurs (doublon #37)
    40: "VALIDE",    # Plus grand volume sur une bougie = signal épuisement
    41: "VALIDE",    # Volumes confirment poursuite haussière
    42: "VALIDE",    # Volume permet distinguer gros opérateurs présents ou pas
    43: "VALIDE",    # Patience = attendre zone de valeur
    44: "INVALIDE",  # Se concentrer uniquement sur présent (pas de prévision) — trop absolu
    45: "VALIDE",    # Ne pas trader 24h/24, se concentrer sur meilleure opportunité
}

def main():
    print(f"Lecture KB: {KB_PATH}")
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        kb = json.load(f)

    # Extraire les règles AMBIGU dans l'ordre (catégorie par catégorie)
    ambigu_rules = []  # liste de (categorie, index_dans_categorie, regle_text)
    for cat, rules in kb['aggregated_rules'].items():
        for i, r in enumerate(rules):
            if r['statut'] == 'AMBIGU':
                ambigu_rules.append((cat, i, r['regle']))

    print(f"AMBIGU trouvées: {len(ambigu_rules)} (attendu: 45)")
    assert len(ambigu_rules) == 45, f"ERREUR: {len(ambigu_rules)} AMBIGU trouvées, attendu 45"

    # Appliquer les verdicts
    stats = {"VALIDE": 0, "INVALIDE": 0, "AMBIGU": 0}
    for idx, (cat, rule_idx, regle_text) in enumerate(ambigu_rules):
        num = idx + 1
        verdict = VERDICTS.get(num, "AMBIGU")
        # Trouver la règle exacte dans la KB et mettre à jour son statut
        for r in kb['aggregated_rules'][cat]:
            if r['regle'] == regle_text:
                old_statut = r['statut']
                r['statut'] = verdict
                stats[verdict] += 1
                if verdict != "AMBIGU":
                    print(f"  [{num:02d}] {verdict}: {regle_text[:60]}...")
                break

    print(f"\n--- Résultats ---")
    print(f"VALIDE   : {stats['VALIDE']} (attendu: 33)")
    print(f"INVALIDE : {stats['INVALIDE']} (attendu: 7)")
    print(f"AMBIGU   : {stats['AMBIGU']} (attendu: 5)")

    # Compter stats globales
    total_valide = sum(1 for cat in kb['aggregated_rules'].values() for r in cat if r['statut'] == 'VALIDE')
    total_invalide = sum(1 for cat in kb['aggregated_rules'].values() for r in cat if r['statut'] == 'INVALIDE')
    total_ambigu = sum(1 for cat in kb['aggregated_rules'].values() for r in cat if r['statut'] == 'AMBIGU')
    total = total_valide + total_invalide + total_ambigu
    pct = round(total_valide / total * 100, 1)
    print(f"\nKB après:")
    print(f"  VALIDE   : {total_valide} ({pct}%)")
    print(f"  INVALIDE : {total_invalide}")
    print(f"  AMBIGU   : {total_ambigu}")
    print(f"  TOTAL    : {total}")

    # Écriture atomique
    tmp = KB_PATH + ".tmp"
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)
    os.replace(tmp, KB_PATH)
    print(f"\nKB sauvegardée: {KB_PATH}")

if __name__ == "__main__":
    main()
