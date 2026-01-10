import pytest
from unittest.mock import Mock
from burger import Burger
from data import Data



class TestBurger:

    def test_set_bun(self):
        burger = Burger()
        burger.set_buns(Data.bulka_1)
        assert burger.bun == Data.bulka_1

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingr_1)
        assert burger.ingredients == [Data.ingr_1]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingr_1)
        burger.add_ingredient(Data.ingr_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [Data.ingr_2]

    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingr_1[0])
        burger.add_ingredient(Data.ingr_2[0])
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [Data.ingr_2[0], Data.ingr_1[0]]

    def test_get_price(self):
        burger = Burger()
        mock = Mock()
        mock.get_price.return_value = Data.bulka_1[1]
        mock1 = Mock()
        mock1.get_price.return_value = Data.ingr_1[2]
        burger.bun = mock
        burger.ingredients = [mock1]
        assert burger.get_price() == mock.get_price()*2+ mock1.get_price()

    def test_get_recept(self):
        burger = Burger()
        mock = Mock()
        mock.get_name.return_value = Data.bulka_1[0]
        mock.get_price.return_value = Data.bulka_1[1]
        burger.bun = mock
        mock1 = Mock()
        mock1.get_name.return_value = Data.ingr_1[1]
        mock1.get_type.return_value = Data.ingr_1[0]
        mock1.get_price.return_value = Data.ingr_1[2]
        burger.ingredients = [mock1]
        recept = f'(==== {Data.bulka_1[0]} ====)\n= начинки {Data.ingr_1[1]} =\n(==== {Data.bulka_1[0]} ====)\n\nPrice: 3313'
        assert burger.get_receipt() == recept