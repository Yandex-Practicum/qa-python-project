import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_remove_ingredient(self, burger):
        ing1, ing2 = Mock(spec=Ingredient), Mock(spec=Ingredient)
        burger.ingredients = [ing1, ing2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_remove_ingredient_invalid_index_raises_error(self, burger):
        burger.ingredients = [Mock(spec=Ingredient)]
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient(self, burger):
        ing1, ing2, ing3 = Mock(spec=Ingredient), Mock(spec=Ingredient), Mock(spec=Ingredient)
        burger.ingredients = [ing1, ing2, ing3]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1]

    def test_move_ingredient_invalid_source_index_raises_error(self, burger):
        burger.ingredients = [Mock(spec=Ingredient), Mock(spec=Ingredient)]
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)  # неверный исходный индекс

    def test_move_ingredient_valid_source_with_invalid_target_does_not_raise(self, burger):
        burger.ingredients = [Mock(spec=Ingredient), Mock(spec=Ingredient)]
        # Не должно быть исключения, т.к. insert при выходе за границы просто добавляет в конец
        burger.move_ingredient(0, 5)

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (50, [10, 20], 130.0),
            (100, [], 200.0),
            (30, [15, 25, 35], 135.0),
            (0, [10, 10], 20.0),
            (50.5, [10.2, 20.3], 131.5),
        ]
    )
    def test_get_price(self, burger, bun_price, ingredient_prices, expected_price):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger_with_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger_with_bun.add_ingredient(mock_ingredient_sauce)
        burger_with_bun.add_ingredient(mock_ingredient_filling)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 700"   # убрали .0
        )
        assert burger_with_bun.get_receipt() == expected_receipt

    def test_receipt_without_ingredients(self, burger_with_bun):
        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200"   # убрали .0
        )
        assert burger_with_bun.get_receipt() == expected_receipt

    def test_price_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_receipt_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()