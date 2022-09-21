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
