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
    except NameError:
        raise (NameError("la classe n'existe pas"))


def test_next_method():
    # vérifie l'existence de
    #   * attribut grid
    #   * méthode next
    
    # grille vide format texte
    grid = """
4 8
........
........
........
........
"""
    # créer une grille vide
    g = Life()
    g.set_grid(grid)
    assert g.next() == grid

