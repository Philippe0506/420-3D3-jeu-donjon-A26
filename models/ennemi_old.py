from random import random

class Ennemi:
    def __init__(self, nom, hp, attaque, comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.comportement = comportement  # "agressif", "defensif", "aleatoire", "furtif"
        self._tour_furtif = 0

    def agir(self):
        """Décide si l'ennemi attaque ou se défend selon son comportement."""
        if self.comportement == "agressif":
            return "attaque"

        elif self.comportement == "defensif":
            if self.hp < self.hp_max * 0.5:
                return "defend"
            else:
                return "attaque"

        elif self.comportement == "aleatoire":
            return random.choice(["attaque", "defend"])

        elif self.comportement == "furtif":
            self._tour_furtif += 1
            if self._tour_furtif % 2 == 0:
                return "defend"
            else:
                return "attaque"

    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0