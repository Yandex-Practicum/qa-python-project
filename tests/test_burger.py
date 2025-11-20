import pytest
from unittest.mock import Mock
from praktikumm.burger import Burger
from praktikumm.bun import Bun
from praktikumm.ingredient import Ingredient

@pytest.fixture
def burger():
    return Burger()

def test_set_buns(burger):
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    assert burger.bun == bun

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "hot sauce", 100),
    ("FILLING", "sausage", 300)
])
def test_add_ingredient(burger, ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient

def test_remove_ingredient(burger):
    ingredient = Ingredient("SAUCE", "sour cream", 150)
    burger.add_ingredient(ingredient)
    idx = 0
    burger.remove_ingredient(idx)
    assert len(burger.ingredients) == 0

def test_get_price_with_mock(burger):
    bun = Mock()
    bun.get_price.return_value = 60
    burger.set_buns(bun)

    ingredient = Mock()
    ingredient.get_price.return_value = 60
    burger.add_ingredient(ingredient)

    expected = 60 * 2 + 60  # <-- исправлено
    assert burger.get_price() == expected

def test_get_receipt(burger):
    bun = Bun("white bun", 200)
    burger.set_buns(bun)
    ingredient = Ingredient("SAUCE", "chili sauce", 300)
    burger.add_ingredient(ingredient)

    expected = "(==== white bun ====)\n= sauce chili sauce =\n(==== white bun ====)\nPrice: 700"
    assert burger.get_receipt() == expected