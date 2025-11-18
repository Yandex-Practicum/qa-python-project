import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData


class TestIngredient:
    # Проверка получения названия ингредиента
    def test_get_name_returns_correct_ingredient_name(self):
        ingredient = Ingredient(IngredientData.sauce_type, IngredientData.ingredient_name, IngredientData.ingredient_price_int)
        assert ingredient.get_name() == IngredientData.ingredient_name

    # Проверяет, что метод get_price возвращает корректную цену ингредиента для целочисленных и дробных значений
    @pytest.mark.parametrize('price', [IngredientData.ingredient_price_int, IngredientData.ingredient_price_float])
    def test_get_price_returns_correct_ingredient_price(self, price):
        ingredient = Ingredient(IngredientData.sauce_type, IngredientData.ingredient_name, price)
        assert ingredient.get_price() == price

    # Проверяет, что метод get_type возвращает корректный тип ингредиента для соуса и начинки
    @pytest.mark.parametrize('ingredient_type', [IngredientData.sauce_type, IngredientData.filling_type])
    def test_get_type_returns_correct_ingredient_type(self, ingredient_type):

        ingredient = Ingredient(ingredient_type, IngredientData.ingredient_name, IngredientData.ingredient_price_int)
        assert ingredient.get_type() == ingredient_type