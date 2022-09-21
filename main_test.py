import pytest
from random import randint
from main import *


def test_integration_ok():
    assert 1 == 1


def test_integration_ko():
    assert not (1 > 2)


def test_foo():
    assert foo() == 1

def test_integration_ko():
    assert False