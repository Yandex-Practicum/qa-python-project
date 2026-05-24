import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        ingredient_1 = Ingredient(INGREDIENT_TYPE_FILLING, "Плазма", 300)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Buldak 3x", 360)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient_2

    def test_get_price(self, burger, bun):
        burger.set_buns(bun)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_FILLING, "Плазма", 300)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Buldak 3x", 360)

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == 860

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert 'Булка звездной пыли' in receipt
        assert 'Кольца j1407b' in receipt
        assert 'Price:' in receipt