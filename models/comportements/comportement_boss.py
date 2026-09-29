from models.comportement import Comportement
from models.actions.action_attaque_double import ActionAttaqueDouble
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefend

class ComportementBoss(Comportement):
    def agir(self, ennemi) -> str:
        if ennemi.hp >= ennemi.hp_max * 0.6:
            return ActionDefend()
        elif ennemi.hp < ennemi.hp_max * 0.6 and ennemi.hp >= ennemi.hp_max * 0.3:
            return ActionAttaque()
        else:
            return ActionAttaqueDouble()