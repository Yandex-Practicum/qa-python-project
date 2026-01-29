from unittest.mock import Mock, patch
from copy import deepcopy
from data import buns, ingreds


class TestBurger:

    def test_set_buns(self, burger):
        mock_bun = Mock()
        mock_bun.configure_mock(name=buns[1]['name'], price=buns[1]['price'])
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingred2 = Mock()
        mock_ingred2.configure_mock(type=ingreds[1]['type'], name=ingreds[1]['name'], price=ingreds[1]['price'])

        burger.add_ingredient(mock_ingred2)

        assert mock_ingred2 in burger.ingredients

    def test_remove_ingredient(self, burger):
        burger.remove_ingredient(0)

        assert ingreds[0] not in burger.ingredients

    def test_move_ingredient(self, burger):
        moved_burger = deepcopy(burger)
        moved_burger.ingredients[0] = burger.ingredients[1]
        moved_burger.ingredients[1] = burger.ingredients[0]

        burger.move_ingredient(0, 1)

        assert burger.ingredients == moved_burger.ingredients

    def test_get_price(self, burger):
        expected_price = 500

        assert burger.get_price() == expected_price

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, mock_get_price, burger):
        expected_receipt = ('(==== black bun ====)\n'
                            '= sauce hot sauce =\n'
                            '= filling dinosaur =\n'
                            '(==== black bun ====)\n'
                            '\n'
                            'Price: 500')

        mock_get_price.return_value = 500

        assert burger.get_receipt() == expected_receipt
