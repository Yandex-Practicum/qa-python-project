from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:

    def test_burger_initial_state(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_burger_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize('remove_index', [0, 1])
    def test_burger_remove_ingredient(self, remove_index):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        removed_ingredient = burger.ingredients[remove_index]
        burger.remove_ingredient(remove_index)

        assert len(burger.ingredients) == 1
        assert removed_ingredient not in burger.ingredients

    @pytest.mark.parametrize(
        'start_index, new_index',
        [
            (0, 1),
            (1, 0),
            (0, 2),
            (2, 1),
        ]
    )
    def test_burger_move_ingredient(self, start_index, new_index):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        mock_ing_3 = Mock()
        ingredients = [mock_ing_1, mock_ing_2, mock_ing_3]

        for ing in ingredients:
            burger.add_ingredient(ing)

        target_ing = burger.ingredients[start_index]
        burger.move_ingredient(start_index, new_index)

        assert burger.ingredients[new_index] == target_ing

    @pytest.mark.parametrize(
        'bun_price, ing_prices, expected_total_price',
        [
            (100, [], 200),
            (150, [50, 75], 425),
            (0, [100], 100),
            (200.5, [10.5, 20.0, 30.0], 461.5),
        ]
    )
    def test_burger_get_price(self, bun_price, ing_prices, expected_total_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ing_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_total_price
        mock_bun.get_price.assert_called_once()

    def test_burger_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ing_1 = Mock()
        mock_ing_1.get_type.return_value = 'SAUCE'
        mock_ing_1.get_name.return_value = 'hot sauce'
        mock_ing_1.get_price.return_value = 100.0

        mock_ing_2 = Mock()
        mock_ing_2.get_type.return_value = 'FILLING'
        mock_ing_2.get_name.return_value = 'cutlet'
        mock_ing_2.get_price.return_value = 100.0

        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n\n'
            'Price: 400.0'
        )

        assert burger.get_receipt() == expected_receipt
        mock_bun.get_name.assert_called()
        mock_ing_1.get_name.assert_called_once()
        mock_ing_2.get_name.assert_called_once()
