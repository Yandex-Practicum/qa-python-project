from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        first = Mock()
        second = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second, first]

    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert "black bun" in receipt
        assert "hot sauce" in receipt
        assert "Price: 250" in receipt
