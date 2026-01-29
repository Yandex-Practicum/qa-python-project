import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BURGER_PRICE_TEST_DATA


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100.0
    bun.get_name.return_value = "Black Bun"
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 20.0
    ingredient.get_name.return_value = "Ketchup"
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


@pytest.fixture
def burger_with_bun(burger, mock_bun):
    burger.set_buns(mock_bun)
    return burger


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


@pytest.mark.parametrize("ingredient_count, expected_price", BURGER_PRICE_TEST_DATA)
def test_get_price(burger_with_bun, mock_ingredient, ingredient_count, expected_price):
    for _ in range(ingredient_count):
        burger_with_bun.add_ingredient(mock_ingredient)
    assert burger_with_bun.get_price() == expected_price


def test_get_receipt(burger_with_bun, mock_ingredient):
    burger_with_bun.add_ingredient(mock_ingredient)
    receipt = burger_with_bun.get_receipt()
    assert "Black Bun" in receipt
    assert "Ketchup" in receipt
    assert f"Price: {burger_with_bun.get_price()}" in receipt


def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient


def test_remove_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(burger, mock_ingredient):
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]
