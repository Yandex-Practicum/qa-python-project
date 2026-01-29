from unittest.mock import Mock, patch
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:

    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self):
        bun = Bun("Bulochka red", 500.5)
        burger = Burger()

        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Ingredient("SAUCE", "Mazik", 80.0)
        burger = Burger()

        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient1 = Ingredient("SAUCE", "Mazik", 80.0)
        ingredient2 = Ingredient("FILLING", "Pomidor", 85.0)

        burger = Burger()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(1)

        assert ingredient1 in burger.ingredients
        assert ingredient2 not in burger.ingredients

    def test_move_ingredient(self):
        ingredient1 = Ingredient("SAUCE", "Mazik", 80.0)
        ingredient2 = Ingredient("FILLING", "Pomidor", 85.0)

        burger = Burger()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)

        assert ingredient1 != burger.ingredients[0]
        assert ingredient1 == burger.ingredients[1]

    def test_get_price(self):
        bun = Bun("Chili Bun", 888.9)
        ingredient1 = Ingredient("FILLING", "Pomidor", 85.0)
        ingredient2 = Ingredient("SAUCE", "Gorchica", 99.9)

        burger = Burger()

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price()
        actual_price = burger.get_price()

        assert expected_price == actual_price

    def test_get_receipt(self):
        bun1 = Bun("Blue Bun", 9.99)
        bun2 = Bun("Blue Bun", 8.99)

        ing1 = Ingredient("sauce", "CHEESE", 9.9)
        ing2 = Ingredient("filling", "MEAT", 35.39)
        ing3 = Ingredient("filling", "KAPUSTA", 12.45)

        burger = Burger()

        burger.set_buns(bun1)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.set_buns(bun2)

        receipt = burger.get_receipt()

        expected_receipt = (
            f'(==== {bun1.get_name()} ====)\n'
            f'= sauce CHEESE =\n'
            f'= filling MEAT =\n'
            f'= filling KAPUSTA =\n'
            f'(==== {bun2.get_name()} ====)\n'
            f"\n"
            f"Price: {burger.get_price()}"
        )
        assert receipt == expected_receipt
