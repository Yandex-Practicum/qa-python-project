from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_burger_init(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    @pytest.mark.parametrize(
        'bun_name',
        [
            ['Флюоресцентная булка', 'Краторная булка']
        ]
    )
    def test_set_buns(self, bun_name):
        burger = Burger()

        assert burger.bun == burger.set_buns(bun_name)

    @pytest.mark.parametrize(
        'ingredient',
        [
            ['Соус традиционный галактический', 'Мясо бессмертных моллюсков Protostomia']
        ]
    )
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Соус традиционный галактический')
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Соус традиционный галактический')
        burger.add_ingredient('Мясо бессмертных моллюсков Protostomia')
        burger.move_ingredient(0, 1)
        assert burger.ingredients == ['Мясо бессмертных моллюсков Protostomia', 'Соус традиционный галактический']

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 1377
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert burger.get_price() == 1255 * 2 + 1377

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка'
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Соус традиционный галактический'
        mock_ingredient.get_type.return_value = 'SAUCE'
        mock = Mock()
        mock.get_price.return_value = 1991

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        burger.get_price = mock.get_price

        assert (burger.get_receipt() == '(==== Флюоресцентная булка ====)\n'
                                        '= sauce Соус традиционный галактический =\n'
                                        '(==== Флюоресцентная булка ====)\n'
                                        '\n'
                                        'Price: 1991')
