import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("bun_name, bun_price", [
    ("Булочка Дипломная", 100.5),
    ("Булочка от Практикума", 50.0)
])
def test_set_buns(bun_name, bun_price):
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = bun_name
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

@pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", [
    (INGREDIENT_TYPE_SAUCE, "Соус Дипломный", 50.5),
    (INGREDIENT_TYPE_FILLING, "Начинка Дипломная", 30.3)
])
def test_add_ingredient(ingredient_type, ingredient_name, ingredient_price):
    burger = Burger()
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = ingredient_type
    mock_ingredient.get_name.return_value = ingredient_name
    mock_ingredient.get_price.return_value = ingredient_price
    burger.add_ingredient(mock_ingredient)
    assert burger.ingredients == [mock_ingredient]

def test_remove_ingredient():
    burger = Burger()
    mock_ingredient_sauce = Mock()
    mock_ingredient_filling = Mock()
    burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
    burger.remove_ingredient(0)
    assert mock_ingredient_sauce not in burger.ingredients

def test_move_ingredient():
    burger = Burger()
    mock_ingredient_sauce = Mock()
    mock_ingredient_filling = Mock()
    burger.ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [mock_ingredient_filling, mock_ingredient_sauce]

def test_get_price():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка Дипломная'
    mock_bun.get_price.return_value = 100.5

    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.get_name.return_value = 'Соус Дипломный'
    mock_ingredient_sauce.get_price.return_value = 50.5

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.get_name.return_value = 'Начинка Дипломная'
    mock_ingredient_filling.get_price.return_value = 30.3

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    assert burger.get_price() == 281.8

def test_get_receipt():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка Дипломная'
    mock_bun.get_price.return_value = 100.5

    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.get_name.return_value = 'Соус Дипломный'
    mock_ingredient_sauce.get_price.return_value = 50.5

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.get_name.return_value = 'Начинка Дипломная'
    mock_ingredient_filling.get_price.return_value = 30.3

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    burger.add_ingredient(mock_ingredient_sauce)

    expected_receipt = (
        '(==== Булочка Дипломная ====)\n'
        '= filling Начинка Дипломная =\n'
        '= sauce Соус Дипломный =\n'
        '(==== Булочка Дипломная ====)\n'
        '\nPrice: 281.8'
    )
    assert burger.get_receipt() == expected_receipt
