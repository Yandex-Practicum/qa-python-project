import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns_assigns_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_appends_to_list(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_remove_ingredient_deletes_by_index(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert mock_sauce not in burger.ingredients

    def test_move_ingredient_changes_order(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (100, [],         200), # только булка: 100 * 2
        (100, [50],       250), # булка + один ингредиент
        (200, [100, 150], 650), # булка + два ингредиента
        (0,   [10, 20],    30), # нулевая цена булки
        (100, [0],        200), # бесплатный ингредиент
    ])
    def test_get_price_calculates_correctly(self, bun_price, ingredient_prices, expected_total):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(bun)
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_total

    def test_get_receipt_contains_bun_name(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert "black bun" in burger.get_receipt()

    def test_get_receipt_contains_ingredient_name(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert "hot sauce" in burger.get_receipt()

    def test_get_receipt_contains_ingredient_type_lowercase(self, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert "filling" in burger.get_receipt()

    def test_get_receipt_contains_price(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert "Price: 200" in burger.get_receipt()
