import pytest


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, ingredient_factory):
        ingredient = ingredient_factory(name="cutlet", price=150, type="FILLING")
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, ingredient_factory):
        ing1 = ingredient_factory(name="first")
        ing2 = ingredient_factory(name="second")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2

    def test_move_ingredient(self, burger, ingredient_factory):
        ing_a = ingredient_factory(name="A")
        ing_b = ingredient_factory(name="B")
        ing_c = ingredient_factory(name="C")
        burger.add_ingredient(ing_a)
        burger.add_ingredient(ing_b)
        burger.add_ingredient(ing_c)
        burger.move_ingredient(2, 1)
        assert burger.ingredients[0] == ing_a
        assert burger.ingredients[1] == ing_c
        assert burger.ingredients[2] == ing_b

    def test_get_price(self, burger, mock_bun, ingredient_factory):
        burger.set_buns(mock_bun)
        ing1 = ingredient_factory(price=50)
        ing2 = ingredient_factory(price=30)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        expected = 200 * 2 + 50 + 30
        assert burger.get_price() == expected

    def test_receipt_formatting(self, burger, mock_bun, ingredient_factory):
        burger.set_buns(mock_bun)
        ing1 = ingredient_factory(name="hot sauce", type="SAUCE")
        ing2 = ingredient_factory(name="cutlet", price=150, type="FILLING")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        expected_price = mock_bun.get_price() * 2 + ing1.get_price() + ing2.get_price()
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== white bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== white bun ====)\n"
            "\n"
            f"Price: {expected_price}"
        )
        assert receipt == expected_receipt
