from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return ActionAttaque()