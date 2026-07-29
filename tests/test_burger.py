from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_to_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,"hot sauce",100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_from_list(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE,"hot sauce",100)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING,"cutlet",200)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE,"hot sauce",100)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING,"cutlet",200)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_total_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 100
        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 200
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 500

    def test_get_receipt(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        ingredient = Mock()
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_price.return_value = 100
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 300"
        )
        assert burger.get_receipt() == expected_receipt