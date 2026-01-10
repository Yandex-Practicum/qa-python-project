from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mocked_ingredients = [
            Mock(spec=Ingredient, name="hot sauce", price=100),
            Mock(spec=Ingredient, name="sour cream", price=200),
            Mock(spec=Ingredient, name="chili sauce", price=300),
        ]
        burger.ingredients = mocked_ingredients[:]
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mocked_ingredients[2], mocked_ingredients[0], mocked_ingredients[1]]

    def test_get_price(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_price = bun.get_price() * 2 + ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        bun = Bun("black bun", 100)
        ingredient = Ingredient("SAUCE", "hot sauce", 50)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            f"(==== black bun ====)\n"
            f"= sauce hot sauce =\n"
            f"(==== black bun ====)\n"
            f"\n"
            f"Price: 250"
        )
        assert burger.get_receipt() == expected_receipt