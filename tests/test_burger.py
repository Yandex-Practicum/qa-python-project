from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:
    """
    Тестирование класса Burger (собранный бургер).
    Проверяет корректность работы основных методов бургера.
    """

    def test_set_buns_should_set_bun_correctly(self):
        """Проверяет установку булочки в бургер."""
        burger = Burger()
        test_bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        burger.set_buns(test_bun)
        assert burger.bun == test_bun

    def test_add_ingredient_should_add_ingredient_to_burger(self):
        """Проверяет добавление ингредиента в бургер."""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == 'cutlet'

    def test_remove_ingredient_should_remove_ingredient_from_burger(self):
        """Проверяет удаление ингредиента из бургера."""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price_should_calculate_correct_total_price(self):
        """Проверяет расчет общей стоимости бургера."""
        burger = Burger()
        data = Database()

        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        assert burger.get_price() == 800

    def test_get_receipt_should_return_properly_formatted_receipt(self):
        """Проверяет форматирование чека для бургера."""
        burger = Burger()
        data = Database()

        burger.set_buns(data.available_buns()[2])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        expected_receipt = (
            '(==== red bun ====)\n'
            '= sauce hot sauce =\n'
            '= sauce sour cream =\n'
            '= sauce chili sauce =\n'
            '(==== red bun ====)\n\n'
            'Price: 1200'
        )
        assert burger.get_receipt() == expected_receipt

    def test_move_ingredient_should_change_ingredients_order(self):
        """Проверяет изменение порядка ингредиентов в бургере."""
        burger = Burger()

        first_ingredient = Mock()
        first_ingredient.get_name.return_value = 'cutlet'

        second_ingredient = Mock()
        second_ingredient.get_name.return_value = 'sausage'

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0].get_name() == 'sausage'
        assert burger.ingredients[1].get_name() == 'cutlet'