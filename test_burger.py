import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Black bun"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50.0
    return sauce

@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 200.0
    return filling

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

    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_remove_ingredient_invalid_index(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_move_ingredient_same_index(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == mock_sauce

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected", [
        (100.0, [50.0, 200.0], 450.0),
        (50.0, [], 100.0),
        (75.0, [30.0, 30.0, 40.0], 250.0),
    ])
    def test_get_price(self, bun_price, ingredients_prices, expected):
        
        bun = Mock()
        bun.get_price.return_value = bun_price

        burger = Burger()
        burger.set_buns(bun)

        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()
        assert "(==== Black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450.0" in receipt or "Price: 450" in receipt

    def test_empty_burger_receipt(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert receipt.count("(==== Black bun ====)") == 2
        assert "Price: 200.0" in receipt or "Price: 200" in receipt