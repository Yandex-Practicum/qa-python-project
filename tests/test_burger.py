import pytest 
from unittest.mock import MagicMock 


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients
    assert len(burger.ingredients) == 1

def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_move_ingredient(burger):
    ingredient1 = MagicMock()
    ingredient2 = MagicMock()
    ingredient3 = MagicMock()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)
    burger.move_ingredient(0, 2)
    assert burger.ingredients == [ingredient2,ingredient3, ingredient1]


@pytest.mark.parametrize("ingredients_count, expected_price", [
    (0, 400.0),
    (1, 480.0),
    (2, 560.0)
])
def test_get_price(burger, mock_bun, mock_ingredient, ingredients_count, expected_price):
    burger.set_buns(mock_bun)
    for _ in range(ingredients_count):
        burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == expected_price

def test_get_receipt(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()
    assert "(==== toasted bun ====)" in receipt
    assert "= filling cheddar slice =" in receipt
    assert "Price: 480.0" in receipt


def test_get_receipt_multiple_ingredients(burger, mock_bun):
    burger.set_buns(mock_bun)
    ing1 = MagicMock()
    ing1.get_price.return_value = 30
    ing1.get_name.return_value = "sauce"
    ing1.get_type.return_value = "SAUCE"
    ing2 = MagicMock()
    ing2.get_price.return_value = 70
    ing2.get_name.return_value = "meat"
    ing2.get_type.return_value = "FILLING"
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    receipt = burger.get_receipt()
    assert "= sauce sauce =" in receipt
    assert "= filling meat =" in receipt
    assert "Price: 500.0" in receipt