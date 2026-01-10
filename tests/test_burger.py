import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from data import buns_data, test_ingredient_data


class TestBurger:

    @pytest.mark.parametrize("bun_data", buns_data)
    def test_set_buns(self, bun_data):
        burger = Burger()
        bun = Bun(bun_data['name'], bun_data['price'])
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_data['name']

    @pytest.mark.parametrize("ingredient_data", test_ingredient_data)
    def test_add_ingredients(self, ingredient_data):
        burger = Burger()
        ingredient = Ingredient(ingredient_data[0], ingredient_data[1], ingredient_data[2])
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()

        ingredient_1 = Ingredient(*test_ingredient_data[1])
        ingredient_2 = Ingredient(*test_ingredient_data[0])

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]

    def test_move_ingredient(self):
        burger = Burger()

        ingredient_1 = Ingredient(*test_ingredient_data[1])
        ingredient_2 = Ingredient(*test_ingredient_data[0])

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_price.return_value = 988.0
        ingredient_mock.get_price.return_value = 200.0
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]
        assert burger.get_price() == 2176.0

    def test_get_receipt(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_name.return_value = 'Флюоресцентная булка R2-D3'
        ingredient_mock.get_type.return_value = 'sauce'
        ingredient_mock.get_name.return_value = 'Соус Spicy-X'
        bun_mock.get_price.return_value = 988.0
        ingredient_mock.get_price.return_value = 90.0
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]

        expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price()
        assert burger.get_receipt() == (
            f'(==== {bun_mock.get_name()} ====)\n'
            f'= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =\n'
            f'(==== {bun_mock.get_name()} ====)\n\n'
            f'Price: {expected_price}'
        )
