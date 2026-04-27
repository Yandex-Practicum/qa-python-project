import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient_moves_ingredient_to_new_index(self):
        burger = Burger()
        ingredient_1 = Mock(name='ingredient_1')
        ingredient_2 = Mock(name='ingredient_2')
        ingredient_3 = Mock(name='ingredient_3')

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]

    @pytest.mark.parametrize('bun_price, ingredients_prices, expected_price',
        [
            (100, [], 200),
            (50, [30], 130),
            (40.5, [10, 20.5], 111.5),
            (25, [5, 10, 15], 80),
        ])
    def test_get_price_returns_correct_price(self, bun_price, ingredients_prices, expected_price):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        actual_price = burger.get_price()

        assert actual_price == expected_price

    def test_get_receipt_returns_correct_receipt(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = 'black bun'
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient_1 = Mock()
        ingredient_1.get_type.return_value = 'SAUCE'
        ingredient_1.get_name.return_value = 'hot sauce'
        ingredient_1.get_price.return_value = 100

        ingredient_2 = Mock()
        ingredient_2.get_type.return_value = 'FILLING'
        ingredient_2.get_name.return_value = 'cutlet'
        ingredient_2.get_price.return_value = 100

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 400'
        )

        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt


