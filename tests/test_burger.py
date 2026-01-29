import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import MagicMock

def test_burger_initialization(sample_burger):
    assert sample_burger.bun is None
    assert sample_burger.ingredients == []

def test_set_buns(sample_burger, sample_bun):
    sample_burger.set_buns(sample_bun)
    assert sample_burger.bun == sample_bun

def test_add_ingredient(sample_burger, sample_ingredient):
    sample_burger.add_ingredient(sample_ingredient)
    assert sample_burger.ingredients == [sample_ingredient]

def test_remove_ingredient(sample_burger, sample_ingredient):
    sample_burger.ingredients = [sample_ingredient]
    sample_burger.remove_ingredient(0)
    assert sample_burger.ingredients == []

def test_move_ingredient(sample_burger, sample_ingredient):
    mock_ingredient = MagicMock()
    sample_burger.ingredients = [mock_ingredient, sample_ingredient]
    sample_burger.move_ingredient(1, 0)
    assert sample_burger.ingredients == [sample_ingredient, mock_ingredient]

def test_get_price(sample_burger, sample_bun, sample_ingredient):
    sample_burger.set_buns(sample_bun)
    sample_burger.add_ingredient(sample_ingredient)
    sample_burger.add_ingredient(sample_ingredient)
    assert sample_burger.get_price() == 160.0

@pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
    (50.0, [20.0, 30.0], 150.0),
    (30.0, [15.0, 25.0], 100.0),
    (40.0, [], 80.0)
])
def test_get_price_parametrized(sample_burger, bun_price, ingredient_prices, expected_price):
    sample_bun = Bun("test bun", bun_price)
    sample_burger.set_buns(sample_bun)
    for price in ingredient_prices:
        sample_burger.add_ingredient(Ingredient("test type", "test ingredient", price))
    assert sample_burger.get_price() == expected_price

def test_get_receipt(sample_burger, sample_bun, sample_ingredient):
    sample_burger.set_buns(sample_bun)
    sample_burger.add_ingredient(sample_ingredient)
    expected_receipt = f"(==== test bun ====)\n= test type test ingredient =\n(==== test bun ====)\n\nPrice: 130.0"
    assert sample_burger.get_receipt() == expected_receipt
