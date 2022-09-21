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


    def set_grid(self, text_grid: str) -> None:
        # setter pour la grille actuelle
        
        # transformation de la grille en tableau de string
        tab_grid =  text_grid.split("\n")
        # récupération de la hauteur et la largeur de la grille
        self.height, self.width = map(int, tab_grid[0].split() )
        self.grid = tab_grid[1:]


    def next(self):
        # méthode qui renvoie la prochaine grille en fonction
        # de self.grid actuel
        # respecte les règles du jeu de la vie
        return self.grid


    def voisins(self, i: int, j: int) -> int:
        """ renvoie le nombre de voisins de la cellule (i,j)
        de la grille de jeux
        precondition:   * 0 <= i < height
                        * 0 <= j < width
        """
        return 0
        
