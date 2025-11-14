from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Чиабатта'
        mock_bun.get_price.return_value = 50
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'FILLING'
        mock_ingredient.name = 'Сыр Чеддер'
        mock_ingredient.price = 10
        mock_ingredient2 = Mock()
        mock_ingredient2.type = 'SAUCE'
        mock_ingredient2.name = 'Барбекю'
        mock_ingredient2.price = 15
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        assert burger.ingredients == [mock_ingredient, mock_ingredient2]

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient]

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 30
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 50

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Ржаная'
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = 'Фалафель'
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = 'Дзадзики'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 250
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.get_price = mock_burger.get_price

        expected_result = '(==== Ржаная ====)\n' '= filling Фалафель =\n' '= sauce Дзадзики =\n' '(==== Ржаная ====)\n' \
                          '\nPrice: 250'

        assert burger.get_receipt() == expected_result