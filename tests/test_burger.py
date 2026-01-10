import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        ingredient = mock_ingredient("Hot Sauce", 50, INGREDIENT_TYPE_SAUCE)
        initial_count = len(burger.ingredients)

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == initial_count + 1
        assert burger.ingredients[-1] == ingredient

    def test_remove_ingredient(self, burger, mock_ingredient):
        ing1 = mock_ingredient("Ing1", 10, INGREDIENT_TYPE_SAUCE)
        ing2 = mock_ingredient("Ing2", 20, INGREDIENT_TYPE_FILLING)
        ing3 = mock_ingredient("Ing3", 30, INGREDIENT_TYPE_SAUCE)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ing1, ing3]

    def test_move_ingredient(self, burger, mock_ingredient):
        ing1 = mock_ingredient("Ing1", 10, INGREDIENT_TYPE_SAUCE)
        ing2 = mock_ingredient("Ing2", 20, INGREDIENT_TYPE_FILLING)
        ing3 = mock_ingredient("Ing3", 30, INGREDIENT_TYPE_SAUCE)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient("Sauce", 50, INGREDIENT_TYPE_SAUCE))
        burger.add_ingredient(mock_ingredient("Filling", 100, INGREDIENT_TYPE_FILLING))

        expected_price = 100 * 2 + 50 + 100
        assert burger.get_price() == expected_price

    def test_get_price_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price() * 2

    def test_get_price_with_ingredients_only(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient("Sauce", 50, INGREDIENT_TYPE_SAUCE))
        assert burger.get_price() == 0

    def test_get_receipt_full_burger(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient("Hot Sauce", 50, INGREDIENT_TYPE_SAUCE))
        burger.add_ingredient(mock_ingredient("Cutlet", 200, INGREDIENT_TYPE_FILLING))

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce Hot Sauce =\n"
            "= filling Cutlet =\n"
            "Price: 450"
        )

        assert receipt == expected_receipt

    def test_get_receipt_no_bun(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient("Sauce", 50, INGREDIENT_TYPE_SAUCE))
        assert burger.get_receipt() == "Бургер без булочки."
