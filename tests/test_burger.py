import pytest
from praktikum.burger import Burger


class TestBurger:

    def test_empty_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.get_name() == "Булка" and burger.ingredients == []

    def test_burger_price_without_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.get_price() == 200.6

    def test_add_one_ingredient(self, ingredient_sauce_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce_mock)
        assert burger.bun is None and burger.ingredients == [ingredient_sauce_mock]

    def test_burger_price_with_one_ingredient(self, bun_mock, ingredient_sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce_mock)
        assert burger.get_price() == 300.9

    def test_add_more_than_one_ingredients(self, ingredient_sauce_mock, ingredient_filling_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        assert burger.bun is None and burger.ingredients == [ingredient_sauce_mock, ingredient_filling_mock]

    def test_burger_price_with_more_than_one_ingredients(self, bun_mock, ingredient_sauce_mock, ingredient_filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        assert burger.get_price() == 501.2

    def test_remove_ingredient(self, ingredient_sauce_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_invalid_index_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_burger_price_after_remove_ingredient(self, bun_mock, ingredient_sauce_mock, ingredient_filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        burger.remove_ingredient(0)
        assert burger.get_price() == 400.9

    def test_move_ingredient(self, ingredient_sauce_mock, ingredient_filling_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [ingredient_filling_mock, ingredient_sauce_mock]

    def test_move_invalid_index_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 5)

    def test_burger_price_after_move_ingredients(self, bun_mock, ingredient_sauce_mock, ingredient_filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)
        burger.move_ingredient(0, 1)
        assert burger.get_price() == 501.2

    def test_get_receipt_without_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        expected_result = (
            f"(==== {bun_mock.get_name()} ====)\n"
            f"(==== {bun_mock.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_result

    def test_get_receipt_with_ingredients(self, bun_mock, ingredient_sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce_mock)
        expected_result = (
            f"(==== {bun_mock.get_name()} ====)\n"
            f"= {ingredient_sauce_mock.get_type().lower()} {ingredient_sauce_mock.get_name()} =\n"
            f"(==== {bun_mock.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_result

