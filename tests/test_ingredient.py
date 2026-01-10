import pytest
from praktikum import ingredient_types
from data import Data
from praktikum.ingredient import Ingredient


# Проверки Ingredient отдельно, без моков
class TestIngredient:
    def test_get_name_ingredient_return_name_ingredient(self):
        ingredient = Ingredient(Data.INGREDIENTS_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_name() == Data.INGREDIENT_NAME

    def test_get_price_ingredient_return_price_ingredient(self):
        ingredient = Ingredient(Data.INGREDIENTS_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_price() == Data.INGREDIENT_PRICE

    @pytest.mark.parametrize('ingredient', [ingredient_types.INGREDIENT_TYPE_FILLING,
                                            ingredient_types.INGREDIENT_TYPE_SAUCE])
    def test_get_price_ingredient_return_type_ingredient(self, ingredient):
        ingredient = Ingredient(ingredient_type=Data.INGREDIENTS_TYPE, name=Data.INGREDIENT_NAME,
                                price=Data.INGREDIENT_PRICE)
        ingredient.type = ingredient

        assert ingredient.get_type() == ingredient
