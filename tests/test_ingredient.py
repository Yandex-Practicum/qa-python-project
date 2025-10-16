import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Тестовые данные
    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    SAUCE_NAME = "hot sauce"
    FILLING_NAME = "cutlet"
    UPPERCASE_NAME = "VEGGIE PATTY"
    NORMAL_PRICE = 100.0
    HIGH_PRICE = 200.0
    ZERO_PRICE = 0.0

    # Тесты для метода get_type()
    def test_get_type_for_sauce(self):
        # Создаем ингредиент-соус с заданными параметрами
        ingredient = Ingredient(self.SAUCE_TYPE, self.SAUCE_NAME, self.NORMAL_PRICE)
        assert ingredient.get_type() == self.SAUCE_TYPE

    def test_get_type_for_filling(self):
        # Создаем ингредиент-начинку с заданными параметрами
        ingredient = Ingredient(self.FILLING_TYPE, self.FILLING_NAME, self.HIGH_PRICE)
        assert ingredient.get_type() == self.FILLING_TYPE

    # Тесты для метода get_name()
    def test_get_name_for_sauce(self):
        # Создаем ингредиент-соус с заданными параметрами
        ingredient = Ingredient(self.SAUCE_TYPE, self.SAUCE_NAME, self.NORMAL_PRICE)
        assert ingredient.get_name() == self.SAUCE_NAME

    def test_get_name_for_filling(self):
        # Создаем ингредиент-начинку с заданными параметрами
        ingredient = Ingredient(self.FILLING_TYPE, self.FILLING_NAME, self.HIGH_PRICE)
        assert ingredient.get_name() == self.FILLING_NAME

    def test_get_name_for_uppercase(self):
        # Создаем ингредиент с именем в верхнем регистре
        ingredient = Ingredient(self.FILLING_TYPE, self.UPPERCASE_NAME, self.HIGH_PRICE)
        assert ingredient.get_name() == self.UPPERCASE_NAME

    # Тесты для метода get_price()
    def test_get_price_normal(self):
        # Создаем ингредиент с обычной ценой
        ingredient = Ingredient(self.SAUCE_TYPE, self.SAUCE_NAME, self.NORMAL_PRICE)
        assert ingredient.get_price() == self.NORMAL_PRICE

    def test_get_price_high(self):
        # Создаем ингредиент с высокой ценой
        ingredient = Ingredient(self.FILLING_TYPE, self.FILLING_NAME, self.HIGH_PRICE)
        assert ingredient.get_price() == self.HIGH_PRICE

    def test_get_price_zero(self):
        # Создаем ингредиент с нулевой ценой
        ingredient = Ingredient(self.SAUCE_TYPE, self.SAUCE_NAME, self.ZERO_PRICE)
        assert ingredient.get_price() == self.ZERO_PRICE