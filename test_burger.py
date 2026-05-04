import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    ing = Mock(spec=Ingredient)
    ing.get_type.return_value = "SAUCE"
    ing.get_name.return_value = "hot sauce"
    ing.get_price.return_value = 50.0
    return ing


@pytest.fixture
def mock_filling():
    ing = Mock(spec=Ingredient)
    ing.get_type.return_value = "FILLING"
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 200.0
    return ing


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
    def test_get_price(self, mock_bun, bun_price, ingredients_prices, expected):
        mock_bun.get_price.return_value = bun_price
        ingredients = []
        for price in ingredients_prices:
            ing = Mock(spec=Ingredient)
            ing.get_price.return_value = price
            ingredients.append(ing)

        burger = Burger()
        burger.set_buns(mock_bun)
        for ing in ingredients:
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        original_get_price = burger.get_price
        burger.get_price = lambda: 450.0
        receipt = burger.get_receipt()
        burger.get_price = original_get_price

        assert "(==== Black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450.0" in receipt

    def test_empty_burger_receipt(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        original_get_price = burger.get_price
        burger.get_price = lambda: 200.0
        receipt = burger.get_receipt()
        burger.get_price = original_get_price

        assert receipt.count("(==== Black bun ====)") == 2
        assert "Price: 200.0" in receipt