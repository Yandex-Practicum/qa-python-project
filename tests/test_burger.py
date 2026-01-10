import pytest
from unittest.mock import Mock
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        burg_ingredient = Burger()
        burg_ingredient.add_ingredient(mock_ingredient)
        assert len(burg_ingredient.ingredients) != 0

    def test_remove_ingredient(self):
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burg_ingredient = Burger()
        burg_ingredient.add_ingredient(ingredient_mock_1)
        burg_ingredient.add_ingredient(ingredient_mock_2)
        burg_ingredient.remove_ingredient(1)
        assert len(burg_ingredient.ingredients) == 1

    def test_move_ingredient(self):
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        ingredient_mock_3 = Mock()
        burg_ingredient = Burger()
        burg_ingredient.add_ingredient(ingredient_mock_1)
        burg_ingredient.add_ingredient(ingredient_mock_2)
        burg_ingredient.add_ingredient(ingredient_mock_3)
        burg_ingredient.move_ingredient(2, 1)
        assert burg_ingredient.ingredients[1] == ingredient_mock_3

    @patch('praktikum.bun.Bun.get_price', return_value=150.3)
    @patch('praktikum.ingredient.Ingredient.get_price', return_value=30.7)
    def test_get_price(self, mock_bun_get_price, mock_ingredient_get_price):
        mock_bun = Mock()
        mock_bun.configure_mock(bun=Bun('Пирожок', 150.3))
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredients=Ingredient('Соус', 'Кетчуп', 30.7))
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_price() == (150.3*2+30.7)

    @patch('praktikum.bun.Bun.get_name', return_value='Булочка')
    @patch('praktikum.ingredient.Ingredient.get_type', return_value='Соус')
    @patch('praktikum.ingredient.Ingredient.get_name', return_value='Барбекю')
    @patch('praktikum.burger.Burger.get_price', return_value=356.7)
    def test_get_receipt(self, mock_bun_get_name, mock_ingredient_get_type, mock_ingredient_get_name, mock_burger_get_price):
        mock_bun = Mock()
        mock_bun.configure_mock(bun=Bun('Булочка', 150.3))
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredients=Ingredient('Соус', 'Барбекю', 30.7))
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_receipt() == '(==== Булочка ====)\n= соус Барбекю =\n(==== Булочка ====)\n\nPrice: 356.7'
