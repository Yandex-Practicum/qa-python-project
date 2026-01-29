from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_set_buns(self):
        bun = MagicMock()
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 50)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 50)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ing2, ing1]

    def test_get_price(self):
        bun = MagicMock()
        bun.get_price.return_value = 100
        ing1 = MagicMock()
        ing1.get_price.return_value = 50
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        assert burger.get_price() == 250  # 100*2 + 50

    def test_get_receipt(self):
        bun = MagicMock()
        bun.get_name.return_value = "test bun"
        bun.get_price.return_value = 100
        ing = MagicMock()
        ing.get_name.return_value = "test sauce"
        ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ing.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing)

        expected_receipt = (
            "(==== test bun ====)\n"
            "= sauce test sauce =\n"
            "(==== test bun ====)\n"
            "\nPrice: 250\n"
        )
        assert burger.get_receipt() == expected_receipt
