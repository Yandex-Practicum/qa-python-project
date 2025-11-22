import pytest
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from practikum.constants import TB_ING_SAUSE_PEICE, TB_ING_SAUSE_NAME, TB_ING_CHEESE_NAME, TB_ING_CHEESE_PRICE, H_INGREDIENTS

class TestIngredient:
    # Тестируем получение цены ингредиента
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, TB_ING_SAUSE_NAME, TB_ING_SAUSE_PEICE)
        assert ingredient.get_price() == TB_ING_SAUSE_PEICE, "Метод get_price() возвращает неверную цену."

    # Тестируем получение имени ингредиента
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, TB_ING_SAUSE_NAME, TB_ING_SAUSE_PEICE)
        assert ingredient.get_name() == TB_ING_SAUSE_NAME, "Метод get_name() возвращает неверное имя."

    # Тестируем получение типа ингредиента
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, TB_ING_CHEESE_NAME, TB_ING_CHEESE_PRICE)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING, "Метод get_type() возвращает неверный тип."


    # Используем параметризацию для тестирования создания ингредиентов
    @pytest.mark.parametrize("ingredient_type, name, price", H_INGREDIENTS)
    def test_ingredient_parametrized_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, "Метод get_price() возвращает неверную цену."
        assert ingredient.get_name() == name, "Метод get_name() возвращает неверное имя."
        assert ingredient.get_type() == ingredient_type, "Метод get_type() возвращает неверный тип."

