from unittest.mock import Mock, patch

import pytest

from src.praktikum.bun import Bun
from src.praktikum.burger import Burger
from src.praktikum.ingredient import Ingredient
from src.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def setup_method(self):
        """Подготовка данных для каждого теста"""
        self.burger = Burger()
        self.bun = Mock(spec=Bun)
        self.bun.get_name.return_value = "black bun"
        self.bun.get_price.return_value = 100.0

        self.ingredient1 = Mock(spec=Ingredient)
        self.ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.ingredient1.get_name.return_value = "hot sauce"
        self.ingredient1.get_price.return_value = 50.0

        self.ingredient2 = Mock(spec=Ingredient)
        self.ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        self.ingredient2.get_name.return_value = "cutlet"
        self.ingredient2.get_price.return_value = 100.0

    def test_set_buns(self):
        """Тест установки булочки"""
        self.burger.set_buns(self.bun)
        assert self.burger.bun == self.bun

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        self.burger.add_ingredient(self.ingredient1)
        assert (len(self.burger.ingredients) == 1
                and self.burger.ingredients[0] == self.ingredient1)

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        ingredients = self.burger.ingredients
        assert (len(ingredients) == 2
                and ingredients.count(self.ingredient1)
                and ingredients.count(self.ingredient2))

    def test_remove_ingredient(self):
        """Тест удаления ингредиента"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.remove_ingredient(0)
        ingredients = self.burger.ingredients
        assert (len(ingredients) == 1
                and ingredients.count(self.ingredient2))

    def test_remove_ingredient_invalid_index(self, exc_info=None):
        """Тест удаления ингредиента по неверному индексу"""
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(0)
            assert str(exc_info.value) == "list index out of range"

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.add_ingredient(self.ingredient1)

        self.burger.move_ingredient(2, 0)

        ingredients = self.burger.ingredients
        assert (len(ingredients) == 3
                and ingredients[0] == self.ingredient1
                and ingredients[1] == self.ingredient1
                and ingredients[2] == self.ingredient2)

    def test_move_ingredient_same_position(self):
        """Тест перемещения ингредиента на ту же позицию"""
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        self.burger.move_ingredient(1, 1)

        ingredients = self.burger.ingredients
        assert (len(ingredients) == 2
                and ingredients[1] == self.ingredient2)

    def test_get_price_without_bun(self):
        """Тест получения цены без булочки"""
        with pytest.raises(AttributeError):
            self.burger.get_price()

    def test_get_price(self):
        """Тест получения полной цены бургера"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        # Цена: булочка*2 (200) + ингредиент1 (50) + ингредиент2 (100) = 350
        expected_price = 350.0
        assert self.burger.get_price() == expected_price

    def test_get_receipt(self):
        """Тест получения чека бургера"""
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)

        receipt = self.burger.get_receipt()

        assert ("(==== black bun ====)" in receipt
                and "= sauce hot sauce =" in receipt
                and "= filling cutlet =" in receipt
                and "Price: 350.0" in receipt)

    @patch('src.praktikum.burger.Burger.get_price')
    def test_get_receipt_with_mock(self, mock_get_price):
        """Тест чека с использованием мока цены"""
        mock_get_price.return_value = 500.0
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)

        receipt = self.burger.get_receipt()
        assert "Price: 500.0" in receipt
