from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

import pytest
from unittest.mock import Mock

class TestBurger:

    def test_burger_init(self):

        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self):

        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):

        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient and len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredient1, ingredient2, ingredient3, index',
                             [
                                ['Sauce 1', 'Sauce 2', 'Filling', 0],
                                ['Sauce', 'Filling 1', 'Filling 2', 1],
                                ['Sauce', 'Filling 1', 'Filling 2', 2] ])
    def test_remove_ingredient(self, ingredient1, ingredient2, ingredient3, index):

        burger = Burger()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        removed_ingredient = burger.ingredients[index]
        burger.remove_ingredient(index)

        assert removed_ingredient not in burger.ingredients

    @pytest.mark.parametrize('ingredient1, ingredient2, ingredient3, old_index, new_index',
                             [
                                 ['Sauce 1', 'Sauce 2', 'Filling', 0, 1],
                                 ['Sauce', 'Filling 1', 'Filling 2', 1, 2],
                                 ['Sauce', 'Filling 1', 'Filling 2', 2, 0],
                                 ['Sauce', 'Filling 1', 'Filling 2', 0, 2],
                                 ['Sauce', 'Filling 1', 'Filling 2', 1, 0],
                                 ['Sauce', 'Filling 1', 'Filling 2', 2, 1],
                                 ['Sauce', 'Filling 1', 'Filling 2', 1, 1],
                                 ['Sauce', 'Filling 1', 'Filling 2', 0, 0],
                                 ['Sauce', 'Filling 1', 'Filling 2', 2, 2] ])
    def test_move_ingredient(self, ingredient1, ingredient2, ingredient3, old_index, new_index):

        burger = Burger()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        moved_ingredient = burger.ingredients[old_index]
        burger.move_ingredient(old_index, new_index)

        assert moved_ingredient == burger.ingredients[new_index]

    @pytest.mark.parametrize('bun_price, ingredient1_price, ingredient2_price, final_price',
                             [ [100.00, 10.00, 20.00, 230.00],
                               [200.00, 0, 30.00, 430.00],
                               [300.00, 10.00, 0, 610.00],
                               [0, 50.00, 20.00, 70.00],
                               [400.00, 0, 0, 800.00],
                               [0, 0, 0, 0] ])
    def test_get_price(self, bun_price, ingredient1_price, ingredient2_price, final_price):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = ingredient1_price

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = ingredient2_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.get_price() == final_price

    def test_get_receipt_bun_sauce_filling(self):
            mock_bun = Mock()
            mock_bun.get_name.return_value = 'Tasty bun'
            mock_bun.get_price.return_value = 100.00

            mock_ingredient1 = Mock()
            mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
            mock_ingredient1.get_name.return_value = 'Tasty sauce'
            mock_ingredient1.get_price.return_value = 10.00

            mock_ingredient2 = Mock()
            mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
            mock_ingredient2.get_name.return_value = 'Tasty filling'
            mock_ingredient2.get_price.return_value = 20.00

            burger = Burger()
            burger.set_buns(mock_bun)
            burger.add_ingredient(mock_ingredient1)
            burger.add_ingredient(mock_ingredient2)

            receipt = [
                '(==== Tasty bun ====)',
                '= sauce Tasty sauce =',
                '= filling Tasty filling =',
                '(==== Tasty bun ====)\n',
                'Price: 230.0'
            ]

            assert burger.get_receipt() == '\n'.join(receipt)

    def test_get_receipt_bun(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Tasty bun'
        mock_bun.get_price.return_value = 100.00

        burger = Burger()
        burger.set_buns(mock_bun)

        receipt = [
            '(==== Tasty bun ====)',
            '(==== Tasty bun ====)\n',
            'Price: 200.0'
        ]

        assert burger.get_receipt() == '\n'.join(receipt)