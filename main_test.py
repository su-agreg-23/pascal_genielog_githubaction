import pytest
from random import randint
from main import *


def test_integration_ok():
    # tests utilisés pour vérifier les tests automatiques
    # sur github à chaque push/commit
    assert 1 == 1
    assert not (1 > 2)


# def test_class_creation():
#     # création d'une classe Life du jeu de la vie
#     try:
#         g = Life()
#     except NameError:
#         raise (NameError("la classe n'existe pas"))

