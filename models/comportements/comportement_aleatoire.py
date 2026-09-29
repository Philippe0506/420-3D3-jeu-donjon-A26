import random
from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefend

class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice([ActionAttaque(), ActionDefend()])