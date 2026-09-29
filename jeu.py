from models.ennemi import Ennemi
from models.comportements.comportement_agressif import ComportementAgressif
from models.comportements.comportement_defensif import ComportementDefensif
from models.comportements.comportement_aleatoire import ComportementAleatoire
from models.comportements.comportement_furtif import ComportementFurtif
from models.comportements.comportement_berserker import ComportementBerserker
from models.comportements.comportement_boss import ComportementBoss
from models.actions.action_defense import ActionDefend


class Jeu:
    def __init__(self):
        self.heros_hp = 300
        self.heros_hp_max = 300
        self.heros_attaque = 20

        self.ennemis = [
            Ennemi("Goblin",  hp=50,  attaque=8,  comportement=ComportementAgressif()),
            Ennemi("Dragon",  hp=100, attaque=12, comportement=ComportementDefensif()),
            Ennemi("Spectre", hp=40,  attaque=10, comportement=ComportementAleatoire()),
            Ennemi("Voleur",  hp=30,  attaque=10, comportement=ComportementFurtif()),
            Ennemi("Boss",   hp=150, attaque=15, comportement=ComportementBoss())
        ]

    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1

        while self.heros_hp > 0 and self.ennemis_vivants():
            # Afficher l'état
            print(f"Tour {tour} — Héros (HP: {self.heros_hp}/{self.heros_hp_max})")
            print("\nEnnemis :")
            vivants = self.ennemis_vivants()
            for i, ennemi in enumerate(vivants, 1):
                print(f"  [{i}] {ennemi.nom} (HP: {ennemi.hp}/{ennemi.hp_max}) — {type(ennemi).__name__}")
            print()

            # Demander l'action du héros
            while True:
                action = input("Votre action ? (a)ttaquer / (d)éfendre : ").strip().lower()
                if action in ["a", "d"]:
                    break
                print("Choix invalide.")
            action_heros = "attaque" if action == "a" else "defend"

            # Demander la cible si attaque
            cible = None
            if action_heros == "attaque":
                if len(vivants) == 1:
                    cible = vivants[0]
                else:
                    while True:
                        try:
                            choix = int(input(f"Quel ennemi ? (1-{len(vivants)}) : "))
                            if 1 <= choix <= len(vivants):
                                cible = vivants[choix - 1]
                                break
                        except ValueError:
                            pass
                        print("Choix invalide.")

            # Chaque ennemi décide de son action
            actions_ennemis = {e: e.agir() for e in vivants}

            print("--- Résultats ---")

            # Résoudre l'attaque du héros
            if action_heros == "attaque" and cible:
                if actions_ennemis.get(cible) == ActionDefend():
                    degats = self.heros_attaque // 2
                    print(f"Vous attaquez {cible.nom} — il se défend ! Seulement {degats} dégâts infligés.")
                else:
                    degats = self.heros_attaque
                    print(f"Vous attaquez {cible.nom} pour {degats} dégâts !")
                cible.recevoir_degats(degats)

            # Résoudre les actions des ennemis
            for ennemi in vivants:
                if not ennemi.est_vivant():
                    continue
                action = ennemi.agir()                                          # ← un objet Action
                self.heros_hp, msg = action.appliquer(ennemi, self.heros_hp, action_heros)
                print(msg)

            # Adaptation des comportements
            for ennemi in self.ennemis_vivants():
                if ennemi.hp < ennemi.hp_max * 0.3 and ennemi.get_comportement().__class__ != ComportementBoss:
                    ennemi.set_comportement(ComportementDefensif())
                    print(f"  ⚡ {ennemi.nom} change de tactique — il devient Défensif !")

            print()
            tour += 1

        if self.heros_hp > 0:
            print("\n===========================================")
            print("  🏆 VICTOIRE ! Tous les ennemis sont vaincus !")
            print("===========================================\n")
        else:
            print("\n===========================================")
            print("  💀 DÉFAITE ! Le héros est tombé...")
            print("===========================================\n")
