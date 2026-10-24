from praktikum.burger import Burger
from praktikum.bun import Bun
import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


def test_init_bun_is_none():
    burger = Burger()
    assert burger.bun is None



def test_init_ingredients_list_is_empty():
    burger = Burger()
    assert burger.ingredients == []



def test_set_buns(mock_bun):
    burger = Burger()

    burger.set_buns(mock_bun)
    
    assert burger.bun is mock_bun


