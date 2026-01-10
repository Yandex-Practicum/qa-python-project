from unittest.mock import Mock

import pytest
from praktikum.praktikum import Burger


class TestBurger:

    @pytest.mark.parametrize("bun", ["Флюоресцентная булка", "Краторная булка", "Bun"])
    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("ingredient", ["Соус Spicy-X", "Соус с шипами Антарианского плоскоходца"])
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        ingredient = "Соус Spicy-X"
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        ingredient_first = "Соус Spicy-X"
        ingredient_second = "Соус с шипами Антарианского плоскоходца"
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        assert burger.ingredients[0] == ingredient_first and burger.ingredients[1] == ingredient_second
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_second and burger.ingredients[1] == ingredient_first

    def test_get_price(self):
        mock = Mock()
        burger = Burger()
        mock.get_price.return_value = 99.9
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        assert burger.get_price() == mock.get_price() * 3

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_price.return_value = 99.9
        mock.get_name.return_value = "Bun"
        mock.get_type.return_value = "type"
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        receipt = f'(==== {mock.get_name()} ====)\n= {mock.get_type()} {mock.get_name()} =\n(==== {mock.get_name()} ====)\n\nPrice: {mock.get_price()*3}'
        assert burger.get_receipt() == receipt
