from models.action import Action
 
 
class ActionDefend(Action):
 
    def appliquer(self, ennemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        return heros_hp, f"  → {ennemi.nom} se défend."