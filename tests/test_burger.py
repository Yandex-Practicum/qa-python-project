from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:
    @pytest.mark.parametrize('bun_name, bun_price', [['Булка', 0], ['БУЛКА', -1], ['булка', 1], ['123', 1.0], ['Булка_123', 123.45]])
    def test_burger_set_buns(self, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price',
                             [['начинка', 'Котлета', 0], ['соус', 'Чесночный', -1], ['начинка', 'Салат', 1],
                              ['соус', 'Heinz', 1.0], ['начинка', 'Помидор', 123.45]])
    def test_burger_add_one_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_one_ingredient_from_burger(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'начинка'
        mock_ingredient.name = 'Котлета'
        mock_ingredient.price = 100.00
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredients_in_burger(self):
        mock_first_ingredient = Mock()
        mock_first_ingredient.type = 'начинка'
        mock_first_ingredient.name = 'Котлета'
        mock_first_ingredient.price = 100.00
        mock_second_ingredient = Mock()
        mock_second_ingredient.type = 'Соус'
        mock_second_ingredient.name = 'Чесночный'
        mock_second_ingredient.price = 20.50
        burger = Burger()
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_second_ingredient
        assert burger.ingredients[1] == mock_first_ingredient

    @pytest.mark.parametrize('bun_price, ingredient_price', [[0, 0], [-1, -1], [1, 1], [1.0, 1.0], [123.45, 123.45]])
    def test_get_burger_price(self, bun_price, ingredient_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == bun_price*2 + ingredient_price

    @pytest.mark.parametrize('bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price',
                             [['Булочка', 0, 'начинка', 'Котлета', 0], ['БУЛКА', -1, 'соус', 'Чесночный', -1],
                              ['булка', 1, 'начинка', 'Салат', 1], ['123', 1.0, 'соус', 'Heinz', 1.0],
                              ['Булка_123', 123.45, 'начинка', 'Помидор', 123.45]])
    def test_get_burger_receipt(self, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_receipt() == f'(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n(==== {bun_name} ====)\n\nPrice: {bun_price*2 + ingredient_price}'
