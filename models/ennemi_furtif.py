import random
from models.ennemi import Ennemi


class EnnemiFurtif(Ennemi):
    """Alterne entre attaque et défense à chaque tour."""

    def __init__(self, nom: str, hp: int, degats_attaque: int) -> None:
        super().__init__(nom, hp, degats_attaque)
        self._tour = 0

    def agir(self) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return "attaque"
        return "defend"