from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)

from tests.data.test_data import (
    BLACK_BUN_NAME,
    BLACK_BUN_PRICE,
    HOT_SAUCE_NAME,
    HOT_SAUCE_PRICE,
    CUTLET_NAME,
    CUTLET_PRICE,
    EXPECTED_RECEIPT_SINGLE_SAUCE
)


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(
            INGREDIENT_TYPE_SAUCE,
            HOT_SAUCE_NAME,
            HOT_SAUCE_PRICE
        )

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(
            INGREDIENT_TYPE_FILLING,
            CUTLET_NAME,
            CUTLET_PRICE
        )

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()

        ingredient1 = Ingredient(
            INGREDIENT_TYPE_SAUCE,
            HOT_SAUCE_NAME,
            HOT_SAUCE_PRICE
        )
        ingredient2 = Ingredient(
            INGREDIENT_TYPE_FILLING,
            CUTLET_NAME,
            CUTLET_PRICE
        )

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)

        burger.set_buns(bun)
        burger.add_ingredient(
            Ingredient(
                INGREDIENT_TYPE_SAUCE,
                HOT_SAUCE_NAME,
                HOT_SAUCE_PRICE
            )
        )
        burger.add_ingredient(
            Ingredient(
                INGREDIENT_TYPE_FILLING,
                CUTLET_NAME,
                CUTLET_PRICE
            )
        )

        assert burger.get_price() == 450

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        ingredient = Ingredient(
            INGREDIENT_TYPE_SAUCE,
            HOT_SAUCE_NAME,
            HOT_SAUCE_PRICE
        )

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_receipt() == EXPECTED_RECEIPT_SINGLE_SAUCE
