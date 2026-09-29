from models.comportement import Comportement
from models.actions.action_attaque_double import ActionAttaqueDouble
from models.actions.action_attaque import ActionAttaque

class ComportementBerserker(Comportement):
    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return ActionAttaqueDouble()
        return ActionAttaque()