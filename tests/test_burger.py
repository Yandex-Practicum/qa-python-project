import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient(self, prepared_burger, mock_sauce, mock_filling):
        initial_ingredients = prepared_burger.ingredients.copy()
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == len(initial_ingredients) - 1
        assert mock_sauce not in prepared_burger.ingredients
        assert mock_filling in prepared_burger.ingredients

    def test_move_ingredient(self, prepared_burger, mock_sauce, mock_filling):
        prepared_burger.move_ingredient(0, 1)
        assert prepared_burger.ingredients == [mock_filling, mock_sauce]

    def test_get_price(self, prepared_burger, mock_bun, mock_sauce, mock_filling):
        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert prepared_burger.get_price() == expected_price

    def test_get_receipt(self, prepared_burger, mock_bun, mock_sauce, mock_filling):
        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'
            f'= sauce {mock_sauce.get_name()} =\n'
            f'= filling {mock_filling.get_name()} =\n'
            f'(==== {mock_bun.get_name()} ====)\n'
            f'\nPrice: {prepared_burger.get_price()}'
        )
        assert prepared_burger.get_receipt() == expected_receipt

    def test_move_ingredient_invalid_index(self, prepared_burger):
        with pytest.raises(IndexError):
            prepared_burger.move_ingredient(10, 0)

    def test_remove_nonexistent_ingredient(self, prepared_burger):
        with pytest.raises(IndexError):
            prepared_burger.remove_ingredient(10)