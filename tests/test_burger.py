from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Бриошь', 100.0)
        burger.set_buns(bun)

        assert burger.bun.get_name() == 'Бриошь'

    def test_add_ingredients(self):
        burger = Burger()
        ingredient = Ingredient('секретный', 'ингридиент', 100.0)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ингридиент', 'соус', 100.0)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ингридиент', 'начинка', 200.0)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ингридиент', 'соус', 100.0)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ингридиент', 'начинка', 200.0)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_price.return_value = 250.0
        ingredient_mock.get_price.return_value = 200.0
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]

        assert burger.get_price() == 700.0

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булочка'
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Соус"
        mock_ingredient1.get_type.return_value = "ингридиент"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Котлетька"
        mock_ingredient2.get_type.return_value = "мясо"
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = Mock(return_value=300)

        expected_receipt = "(==== Булочка ====)\n= ингридиент Соус =\n= мясо Котлетька =\n(==== Булочка ====)\n\nPrice: 300"
        assert burger.get_receipt() == expected_receipt
