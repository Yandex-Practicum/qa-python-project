import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger


class TestBurger:
    #Добавление булочки.
    def test_set_bun_burger(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    #Добавление ингредиента.
    def test_add_ingredient(self, mock_filling, burger):
        burger.add_ingredient(mock_filling)
        assert mock_filling in burger.ingredients

    #Удаление ингредиента.
    def test_remove_ingredient(self, mock_filling, burger):
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    #Перемещение ингредиентов.
    def test_move_ingredient(self, burger, mock_filling):
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 1

    #Получение стоимости бургера.
    def test_get_price_burger(self, mock_bun, burger, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == 260

    #Получение чека.
    def test_get_receipt_burger(self, mock_bun, mock_filling, burger, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert burger.get_receipt() == ("(==== Булка ====)\n" 
                                       "= filling meteor =\n" 
                                       "= sauce cheese =\n" 
                                       "(==== Булка ====)\n\n" 
                                       "Price: 420")
