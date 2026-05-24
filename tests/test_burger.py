import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def setup_method(self):
        # Мок булочки
        self.bun = MagicMock()
        self.bun.get_name.return_value = "black bun"
        self.bun.get_price.return_value = 100.0

        # Мок ингредиентов
        self.sauce = MagicMock()
        self.sauce.get_name.return_value = "hot sauce"
        self.sauce.get_price.return_value = 50.0
        self.sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE

        self.filling = MagicMock()
        self.filling.get_name.return_value = "cutlet"
        self.filling.get_price.return_value = 100.0
        self.filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    def test_set_buns_assigns_bun(self):
        burger = Burger()
        burger.set_buns(self.bun)
        assert burger.bun == self.bun

    def test_add_ingredient_appends_to_list(self):
        burger = Burger()
        burger.add_ingredient(self.sauce)
        assert self.sauce in burger.ingredients

    def test_remove_ingredient_removes_from_list(self):
        burger = Burger()
        burger.add_ingredient(self.sauce)
        burger.add_ingredient(self.filling)
        burger.remove_ingredient(0)
        assert self.sauce not in burger.ingredients
        assert self.filling in burger.ingredients

    def test_move_ingredient_changes_order(self):
        burger = Burger()
        burger.add_ingredient(self.sauce)
        burger.add_ingredient(self.filling)
        # sauce на индексе 0, filling на индексе 1
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == self.filling
        assert burger.ingredients[1] == self.sauce

    def test_get_price_returns_bun_price_twice_plus_ingredients(self):
        burger = Burger()
        burger.set_buns(self.bun)
        burger.add_ingredient(self.sauce)
        burger.add_ingredient(self.filling)
        # 100 * 2 + 50 + 100 = 350
        assert burger.get_price() == 350.0

    def test_get_price_without_ingredients_returns_bun_price_twice(self):
        burger = Burger()
        burger.set_buns(self.bun)
        assert burger.get_price() == 200.0

    def test_get_receipt_contains_bun_name(self):
        burger = Burger()
        burger.set_buns(self.bun)
        receipt = burger.get_receipt()
        assert "black bun" in receipt

    def test_get_receipt_contains_ingredient_name(self):
        burger = Burger()
        burger.set_buns(self.bun)
        burger.add_ingredient(self.sauce)
        receipt = burger.get_receipt()
        assert "hot sauce" in receipt

    def test_get_receipt_contains_ingredient_type_lowercase(self):
        burger = Burger()
        burger.set_buns(self.bun)
        burger.add_ingredient(self.sauce)
        receipt = burger.get_receipt()
        assert "sauce" in receipt

    def test_get_receipt_contains_price(self):
        burger = Burger()
        burger.set_buns(self.bun)
        burger.add_ingredient(self.sauce)
        receipt = burger.get_receipt()
        assert "Price: 250.0" in receipt

    def test_get_receipt_format_bun_wraps_ingredients(self):
        burger = Burger()
        burger.set_buns(self.bun)
        burger.add_ingredient(self.filling)
        receipt = burger.get_receipt()
        lines = receipt.split("\n")
        # Первая строка — верхняя булочка
        assert lines[0] == "(==== black bun ====)"
        # Строка с ценой — последняя
        assert lines[-1].startswith("Price:")