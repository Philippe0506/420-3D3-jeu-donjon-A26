from models.comportement import Comportement
from models.actions.action_defense import ActionDefend
from models.actions.action_attaque import ActionAttaque



class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return ActionDefend()
        return ActionAttaque()