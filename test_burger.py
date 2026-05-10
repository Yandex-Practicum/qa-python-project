import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_set_buns(self):
        bun = Bun("Black bun", 100)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 50)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        sauce = Ingredient("SAUCE", "hot sauce", 50)
        filling = Ingredient("FILLING", "cutlet", 200)
        burger = Burger()
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == filling

    def test_remove_ingredient_invalid_index(self):
        sauce = Ingredient("SAUCE", "hot sauce", 50)
        burger = Burger()
        burger.add_ingredient(sauce)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient(self):
        sauce = Ingredient("SAUCE", "hot sauce", 50)
        filling = Ingredient("FILLING", "cutlet", 200)
        burger = Burger()
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == filling
        assert burger.ingredients[1] == sauce

    def test_move_ingredient_same_index(self):
        sauce = Ingredient("SAUCE", "hot sauce", 50)
        burger = Burger()
        burger.add_ingredient(sauce)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == sauce

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected", [
        (100.0, [50.0, 200.0], 450.0),
        (50.0, [], 100.0),
        (75.0, [30.0, 30.0, 40.0], 250.0),
    ])
    def test_get_price(self, bun_price, ingredients_prices, expected):
        bun = Bun("Black bun", bun_price)
        burger = Burger()
        burger.set_buns(bun)
        for price in ingredients_prices:
            ingredient = Ingredient("SAUCE", "some sauce", price)
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected

    def test_get_receipt(self):
        bun = Bun("Black bun", 100)
        sauce = Ingredient("SAUCE", "hot sauce", 50)
        filling = Ingredient("FILLING", "cutlet", 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        receipt = burger.get_receipt()
        assert "(==== Black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        # Извлекаем цену из чека
        import re
        match = re.search(r"Price:\s*([\d.]+)", receipt)
        assert match is not None, "Price not found in receipt"
        price = float(match.group(1))
        assert price == 450.0

    def test_empty_burger_receipt(self):
        bun = Bun("Black bun", 100)
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert receipt.count("(==== Black bun ====)") == 2
        import re
        match = re.search(r"Price:\s*([\d.]+)", receipt)
        assert match is not None, "Price not found in receipt"
        price = float(match.group(1))
        assert price == 200.0