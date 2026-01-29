import pytest
from praktikum.ingredient import Ingredient
from data import DataBurgerIngredients


class TestIngredient:
    # Проверяем получение цены добавляемого ингредиента
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             DataBurgerIngredients.data_ingredients)
    def test_get_price_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        expected_ingredient_price = ingredient_price
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        actual_ingredient_price = ingredient.get_price()

        assert actual_ingredient_price == expected_ingredient_price

    # Проверяем получение имени добавляемого ингредиента, с корректными параметрами
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             DataBurgerIngredients.data_ingredients)
    def test_get_name_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        expected_ingredient_name = ingredient_name
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        actual_ingredient_name = ingredient.get_name()

        assert actual_ingredient_name == expected_ingredient_name

    # Проверяем получение типа добавляемого ингредиента
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             DataBurgerIngredients.data_ingredients)
    def test_get_type_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        expected_ingredient_type = ingredient_type
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        actual_ingredient_type = ingredient.get_type()

        assert actual_ingredient_type == expected_ingredient_type
