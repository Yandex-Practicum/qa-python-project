from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns_one_bun_successful(self):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булочка', 300)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        assert burger.bun.get_name() == ('Булочка'), 'Неправильное наименование булочки'

    def test_add_ingredient_one_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "Соус", 135)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.ingredients != [['SAUCE', "Соус", 135]]

    def test_remove_ingredient_one_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "hot sauce", 100)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    '''Проверка смены мест ингредиентов'''
    def test_move_ingredients_successful(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredients_1 = Ingredient('SAUCE', "Соус", 135)
        mock_ingredient.ingredients_1 = Ingredient('FILLING', "Кетчуп", 250)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients_1)
        burger.add_ingredient(mock_ingredient.ingredients_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients.index(mock_ingredient.ingredients_1) == 1

    @patch('praktikum.bun.Bun.get_price', return_value=300)
    @patch('praktikum.ingredient.Ingredient.get_price', return_value=135)
    def test_get_price_for_one_burger_successful(self, mock_bun_get_price, mock_ingredient_get_price):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булочка', 1000)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('SAUCE', "Соус", 135)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_price() == 735

    @patch('praktikum.bun.Bun.get_name', return_value='Булочка')
    @patch('praktikum.ingredient.Ingredient.get_type', return_value='FILLING')
    @patch('praktikum.ingredient.Ingredient.get_name', return_value='Кетчуп')
    def test_get_receipt_for_one_burger_successful(self, mock_bun_get_name, mock_ingredient_get_type, mock_ingredient_get_name):
        mock_bun = Mock()
        mock_bun.bun = Bun('Булочка с изюмом', 300)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient('FILLING', "Кетчуп", 250)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)
        assert burger.get_receipt() == '(==== Булочка ====)\n''= filling Кетчуп =\n''(==== Булочка ====)\n''\n''Price: 850'
