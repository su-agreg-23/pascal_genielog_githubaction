"""
jeux de la vie 
développent :
    * TDD
    * CI (via github)
"""

class Life():
    # classe de jeu de la vie

    def __init__(self):
        # grille actuelle
        self.grid = ""


    def set_grid(self, text_grid: str) -> None:
        # setter pour la grille actuelle
        self.grid = text_grid


    def next(self):
        # méthode qui renvoie la prochaine grille en fonction
        # de self.grid actuel
        # respecte les règles du jeu de la vie
        return self.grid

