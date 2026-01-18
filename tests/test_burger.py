import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_init_bun(self):
        burger = Burger()

        assert burger.bun is None

    def test_init_ingridients(self):
        burger = Burger()

        assert not burger.ingredients

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)

        assert mock_sauce in burger.ingredients

    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(1)

        assert mock_sauce in burger.ingredients
        assert mock_filling not in burger.ingredients

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)

        assert mock_sauce in burger.ingredients
        assert burger.ingredients.index(mock_sauce) == 1
        assert mock_filling in burger.ingredients
        assert burger.ingredients.index(mock_filling) == 0

    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == (mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price())

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_receipt() == (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =\n"
            f"= {mock_filling.get_type().lower()} {mock_filling.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
