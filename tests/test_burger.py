import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        mock = Mock()
        mock.get_name.return_value = 'black bun'
        mock.get_price.return_value = 100
        return mock

    @pytest.fixture
    def mock_ingredient(self):
        mock = Mock()
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock.get_name.return_value = 'hot sauce'
        mock.get_price.return_value = 100
        return mock

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_ingredient):
        second_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 300  # bun*2 + ingredient

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert '(==== black bun ====)' in receipt
        assert '= sauce hot sauce =' in receipt
        assert 'Price: 300' in receipt

