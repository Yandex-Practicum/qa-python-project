import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData


class TestBurger:

    def test_burger_initial_state(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @pytest.mark.parametrize("bun_name, bun_price", BunData)
    def test_set_bun(self, bun_name, bun_price):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    @pytest.mark.parametrize("name, type_i, price", IngredientData)
    def test_add_ingredient(self, name, type_i, price):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_type.return_value = type_i
        mock_ingredient.get_price.return_value = price

        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "mock bun" in receipt
        assert "mock ingredient" in receipt
        assert str(mock_bun.get_price() * 2 + mock_ingredient.get_price()) in receipt