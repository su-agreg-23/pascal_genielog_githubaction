import pytest
from random import randint
from main import *


def test_integration_ok():
    # tests utilisés pour vérifier les tests automatiques
    # sur github à chaque push/commit
    assert 1 == 1
    assert not (1 > 2)


def test_class_creation():
    # création d'une classe Life du jeu de la vie
    try:
        g = Life()
        # dimision initiales de la grille
        assert g.height == 0
        assert g.width == 0
    except NameError:
        raise (NameError("la classe n'existe pas"))


# fichiers d'entrées
input_0 = """4 8
........
........
........
........"""

input_1 = """3 5
.*...
...*.
*...."""

input_2 = """4 8 
........
....*...
...**...
........"""


def test_next_method():
    # vérifie l'existence de
    #   * attribut grid
    #   * méthode next
    
    # créer une grille vide
    g = Life()

    g.set_grid(input_0)
    # mise à jour des dimensions de la grille
    assert g.height == 4
    assert g.width == 8
    assert g.grid == ['........', '........', '........', '........']

    g.set_grid(input_1)
    # mise à jour des dimensions de la grille
    assert g.height == 3
    assert g.width == 5
    assert g.grid == ['.*...', '...*.', '*....']


def test_nb_voisins():
    """
    vérifier que le nombre de voisin d'une
    cellule est bien représenté d'une grille de jeu (list)
    """
    g = Life()
    # cas de la grille vide
    g.set_grid(input_0)
    for i in range(4):
        for j in range(8):
            assert g.voisins(i,j) == 0

