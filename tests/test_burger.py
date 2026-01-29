from unittest.mock import patch, Mock
import ingredient_types
from praktikum.burger import Burger


class TestBurger:
    @patch("praktikum.burger.Burger.add_ingredient", return_value=["Соус"])
    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        assert burger.add_ingredient(mock_ingredient) == ["Соус"]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.ingredients = ingredient_types.INGREDIENTS_FOR_REMOVE_INGREDIENT
        burger.remove_ingredient(1)

        assert (
            burger.ingredients == ingredient_types.INGREDIENTS_AFTER_REMOVED_INGREDIENT
        )

    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = ingredient_types.INGREDIENTS_FOR_MOVE_INGREDIENT
        burger.move_ingredient(1, 0)

        assert (
            burger.ingredients == ingredient_types.INGREDIENTS_AFTER_MOVED_INGREDIENTS
        )

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        bun_mock.get_price.return_value = 10
        first_ingredient_mock.get_price.return_value = 5
        second_ingredient_mock.get_price.return_value = 3
        burger.bun = bun_mock
        burger.ingredients = [first_ingredient_mock, second_ingredient_mock]
        expected_price = 10 * 2 + 5 + 3

        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_result = (
            "(==== Кунжутная булочка ====)\n"
            "= наполнение Соус =\n"
            "(==== Кунжутная булочка ====)\n"
            "\n"
            "Price: 110"
        )
        assert burger.get_receipt() == expected_result
