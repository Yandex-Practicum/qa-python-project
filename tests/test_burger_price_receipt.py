from praktikum.burger import Burger
from praktikum.bun import Bun
import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

def test_get_price(mock_bun, mock_ingredient_cutlet, mock_ingredient_sauce):

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_cutlet)
    burger.add_ingredient(mock_ingredient_sauce)

    assert burger.get_price() == 500



def test_get_receipt(mock_bun, mock_ingredient_cutlet, mock_ingredient_sauce):
    
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_cutlet)
    burger.add_ingredient(mock_ingredient_sauce)

    assert isinstance(burger.get_receipt(), str)


def test_get_receipt_conten(mock_bun, mock_ingredient_cutlet, mock_ingredient_sauce):
    
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_cutlet)
    burger.add_ingredient(mock_ingredient_sauce)

    expected_receipt = """(==== black bun ====)
= filling cutlet =
= sauce hot sauce =
(==== black bun ====)

Price: 500"""

    assert burger.get_receipt() == expected_receipt