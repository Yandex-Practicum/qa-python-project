from data import Data
from praktikum.burger import Burger


# Проверки класса Burger с мокирование Bun и Ingredient
class TestBurger:
    def test_set_buns_bun_is_correct_value(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_ingredient_value_correct(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_get_price_burger_return_return_sum(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        result_mock = mock_bun.get_price() * 2 + mock_ingredient.get_price()

        assert burger.get_price() == result_mock

    def test_get_receipt_burger_return_string(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == Data.RESULT_GET_RECEIPT_FROM_MOCK

    def test_remove_ingredient_len_list_ingredient_is_zero(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_switch_burger_index(self, mock_ingredient, mock_ingredient_second_from_move_test):
        burger = Burger()
        second_burger = mock_ingredient_second_from_move_test
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_burger)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == second_burger
