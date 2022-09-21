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


    def get_neighbours(self, i: int, j: int) -> int:
        """ renvoie le nombre de voisins de la cellule (i,j)
        de la grille de jeux
        precondition:   * 0 <= i < height
                        * 0 <= j < width
        """
        neighbours: int = 0
        # au dessus
        if i > 0:
            if j-1>0 and self.grid[i-1][j-1] == '*':
                    neighbours += 1
            if self.grid[i-1][j] == '*':
                    neighbours += 1
            if j+1<self.width and self.grid[i-1][j+1] == '*':
                    neighbours += 1
        # au dessous
        if i+1 < self.height:
            if j-1>0 and self.grid[i+1][j-1] == '*':
                    neighbours += 1
            if self.grid[i+1][j] == '*':
                    neighbours += 1
            if j+1<self.width and self.grid[i+1][j+1] == '*':
                    neighbours += 1
        # à gauche
        if j-1>0 and self.grid[i][j-1] == '*':
            neighbours += 1
        # à droite
        if j+1<self.width and self.grid[i][j+1] == '*':
            neighbours += 1

        return neighbours


    def next(self):
        # méthode qui renvoie la prochaine grille en fonction
        # de self.grid actuel
        # respecte les règles du jeu de la vie
        
        # nouvelle grille qui sera renvoyée
        new_grid: list[str] = []
        return self.grid