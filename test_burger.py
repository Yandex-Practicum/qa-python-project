import pytest
from burger import Burger


class TestBurger:

    def test_add_bun_at_order(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingriedient_at_order(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce
