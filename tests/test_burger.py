import pytest

class TestBurger:
    def test_burger_creation(self, empty_burger):
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns(self, empty_burger, kunzhutnaya_bun):
        empty_burger.set_buns(kunzhutnaya_bun)
        assert empty_burger.bun == kunzhutnaya_bun

    def test_add_ingredient(self, empty_burger, ketchup):
        empty_burger.add_ingredient(ketchup)
        assert empty_burger.ingredients == [ketchup]

    def test_remove_ingredient(self, empty_burger, ketchup, mayonnaise):
        empty_burger.add_ingredient(ketchup)
        empty_burger.add_ingredient(mayonnaise)
        empty_burger.remove_ingredient(1)
        assert empty_burger.ingredients == [ketchup]

    def test_move_ingredient(self, empty_burger, ketchup, mayonnaise, cucumber):
        empty_burger.add_ingredient(ketchup)
        empty_burger.add_ingredient(mayonnaise)
        empty_burger.add_ingredient(cucumber)

        empty_burger.move_ingredient(2, 0)
        expected_ingredients = [cucumber, ketchup, mayonnaise]
        assert empty_burger.ingredients == expected_ingredients

    def test_get_price(self, empty_burger, kunzhutnaya_bun, ketchup):
        empty_burger.set_buns(kunzhutnaya_bun)
        empty_burger.add_ingredient(ketchup)

        expected_price = kunzhutnaya_bun.get_price() * 2 + ketchup.get_price()
        assert empty_burger.get_price() == expected_price

    def test_get_receipt(self, empty_burger, kunzhutnaya_bun, ketchup):
        empty_burger.set_buns(kunzhutnaya_bun)
        empty_burger.add_ingredient(ketchup)

        expected_receipt = (
            "(==== Кунжутная ====)\n"
            "= sauce Кетчуп =\n"
            "(==== Кунжутная ====)\n"
            "\n"
            "Price: 10.5"
        )
        assert empty_burger.get_receipt() == expected_receipt

