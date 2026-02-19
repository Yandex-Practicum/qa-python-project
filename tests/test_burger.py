from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)

        assert burger.ingredients == [ingredient_mock]

    def test_remove_ingredient(self):
        burger = Burger()

        i1 = Mock()
        i2 = Mock()

        burger.add_ingredient(i1)
        burger.add_ingredient(i2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [i2]

    def test_move_ingredient(self):
        burger = Burger()

        i1 = Mock()
        i2 = Mock()
        i3 = Mock()

        burger.ingredients = [i1, i2, i3]

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [i2, i3, i1]

    @pytest.mark.parametrize('bun_price, ing_prices, expected', [
        (100, [], 200),
        (100, [50], 250),
        (200, [10, 20], 430),
    ])
    def test_get_price(self, bun_price, ing_prices, expected):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ing_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price

            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    def test_get_receipt_without_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)

        expected = '(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200'

        assert burger.get_receipt() == expected

    def test_get_receipt_with_ingredients(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)

        sauce = Mock()
        sauce.get_type.return_value = 'SAUCE'
        sauce.get_name.return_value = 'hot sauce'
        sauce.get_price.return_value = 50

        filling = Mock()
        filling.get_type.return_value = 'FILLING'
        filling.get_name.return_value = 'cutlet'
        filling.get_price.return_value = 100

        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n\n'
            'Price: 350'
        )

        assert burger.get_receipt() == expected
