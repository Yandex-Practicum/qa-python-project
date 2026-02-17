import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:

    def test_init_bun_is_none(self, create_burger):
        assert create_burger.bun == None

    def test_init_ingredients_is_empty_list(self, create_burger):
        assert create_burger.ingredients == []

    def test_set_buns(self, create_burger, mock_bun):
        create_burger.set_buns(mock_bun)
        assert create_burger.bun == mock_bun

    def test_add_ingredient(self, create_burger, mock_ingredient):
        create_burger.add_ingredient(mock_ingredient)
        assert len(create_burger.ingredients) == 1
        assert create_burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, create_burger, mock_ingredient, index = 0):
        create_burger.add_ingredient(mock_ingredient)
        create_burger.remove_ingredient(index)
        assert len(create_burger.ingredients) == 0

    def test_move_ingredient(self, create_burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        create_burger.add_ingredient(mock_ingredient1)
        create_burger.add_ingredient(mock_ingredient2)
        create_burger.add_ingredient(mock_ingredient3)
        create_burger.move_ingredient(0, 1)
        assert create_burger.ingredients == [mock_ingredient2, mock_ingredient1, mock_ingredient3]
        
    def test_get_price(self, create_burger, mock_bun, mock_ingredient):
        create_burger.set_buns(mock_bun)
        create_burger.add_ingredient(mock_ingredient)
        create_burger.add_ingredient(mock_ingredient)
        assert create_burger.get_price() == 3330

    def test_get_receipt(self, create_burger, mock_bun, mock_ingredient):
        create_burger.set_buns(mock_bun)
        create_burger.add_ingredient(mock_ingredient)
        create_burger.add_ingredient(mock_ingredient)
        receipt = create_burger.get_receipt()
        expected_receipt  = "(==== Crazy bun ====)\n= filling Crazy ham =\n= filling Crazy ham =\n(==== Crazy bun ====)\n\nPrice: 3330"
        assert receipt == expected_receipt
        