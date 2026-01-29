from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('bun_name', 100.0)
        burger.set_buns(bun)

        assert burger.bun.get_name() == 'bun_name'

    def test_add_ingredients(self):
        burger = Burger()
        ingredient = Ingredient('ingredient_type', 'name', 100.0)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ingredient_type', 'sauce', 100.0)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ingredient_type', 'filling', 200.0)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ingredient_type', 'sauce', 100.0)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ingredient_type', 'filling', 200.0)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_price.return_value = 300.0
        ingredient_mock.get_price.return_value = 200.0
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]

        assert burger.get_price() == 800.0

    def test_get_receipt_(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_name.return_value = 'red bun'
        ingredient_mock.get_type.return_value = 'sauce'
        ingredient_mock.get_name.return_value = 'sour cream'
        bun_mock.get_price.return_value = 300.0
        ingredient_mock.get_price.return_value = 200.0
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]

        assert burger.get_receipt() == '(==== red bun ====)\n= sauce sour cream =\n(==== red bun ====)\n\nPrice: 800.0'




