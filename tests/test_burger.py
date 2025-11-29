import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_initialization_empty(self):
        """Тест инициализации бургера"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Тест установки булочки"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_single_ingredient(self, mock_ingredient_sauce):
        """Тест добавления ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_add_multiple_ingredients(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест добавления нескольких ингредиентов"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_removes_correctly(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест удаления ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient_changes_order(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест перемещения ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce

    def test_get_price_with_bun_and_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест расчета цены с булочкой и ингредиентами"""
        burger = Burger()
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_price.return_value = 50
        mock_ingredient_filling.get_price.return_value = 75
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        price = burger.get_price()
        assert price == 325

    def test_get_price_no_bun_returns_zero(self, mock_ingredient_sauce):
        """Тест расчета цены без булочки"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.get_price() == 0

    def test_get_price_only_bun_no_ingredients(self, mock_bun):
        """Тест расчета цены только с булочкой"""
        burger = Burger()
        mock_bun.get_price.return_value = 150
        burger.set_buns(mock_bun)
        assert burger.get_price() == 300

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [100, 200], 500),
        (200, [150, 250, 300], 1100),
        (150, [], 300),
    ])
    def test_get_price_parameterized(self, bun_price, ingredient_prices, expected_total):
        """Параметризованный тест расчета цены"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_total

    def test_get_receipt_with_bun_and_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест генерации чека"""
        burger = Burger()
        mock_bun.get_name.return_value = "black bun"
        mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_sauce.get_name.return_value = "hot sauce"
        mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_filling.get_name.return_value = "cutlet"
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt

    def test_get_receipt_no_bun_shows_none(self):
        """Тест генерации чека без булочки"""
        burger = Burger()
        receipt = burger.get_receipt()
        assert "(==== None ====)" in receipt
        assert "Price: 0" in receipt

    def test_remove_ingredient_from_empty_list_raises_error(self):
        """Тест удаления из пустого списка"""
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)