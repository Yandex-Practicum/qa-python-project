import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [ingredient_2]

    @pytest.mark.parametrize(
        'index,new_index,expected_order',
        [
            (0, 1, [1, 0, 2]),
            (2, 0, [2, 0, 1]),
            (1, 2, [0, 2, 1]),
        ]
    )
    def test_move_ingredient_changes_order(
        self,
        index,
        new_index,
        expected_order
    ):
        burger = Burger()

        ingredients = [Mock(), Mock(), Mock()]

        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        expected = [ingredients[i] for i in expected_order]

        assert burger.ingredients == expected

    def test_get_price_returns_correct_price(self):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = 100

        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 50

        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 70

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        result = burger.get_price()

        assert result == 320

    def test_get_receipt_returns_correct_receipt(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = 'Black bun'
        bun.get_price.return_value = 100

        ingredient_1 = Mock()
        ingredient_1.get_type.return_value = 'SAUCE'
        ingredient_1.get_name.return_value = 'Hot sauce'
        ingredient_1.get_price.return_value = 50

        ingredient_2 = Mock()
        ingredient_2.get_type.return_value = 'FILLING'
        ingredient_2.get_name.return_value = 'Cutlet'
        ingredient_2.get_price.return_value = 70

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        expected_receipt = (
            '(==== Black bun ====)\n'
            '= sauce Hot sauce =\n'
            '= filling Cutlet =\n'
            '(==== Black bun ====)\n\n'
            'Price: 320'
        )

        assert burger.get_receipt() == expected_receipt