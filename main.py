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
        self.height = 0
        self.width = 0


    def text_to_grid(self, text_grid: str) -> None:
        # setter pour la grille actuelle
        
        # transformation de la grille en tableau de string
        tab_grid =  text_grid.split("\n")
        # récupération de la hauteur et la largeur de la grille
        self.height, self.width = map(int, tab_grid[0].split() )
        # print(f"INFO: height = {h-1+1}, width = {w-1+1}")

        self.grid = text_grid


    def next(self):
        # méthode qui renvoie la prochaine grille en fonction
        # de self.grid actuel
        # respecte les règles du jeu de la vie
        return self.grid

