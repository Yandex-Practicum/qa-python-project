import praktikum.ingredient_types as IT
from data import Data
from praktikum.ingredient import Ingredient


class TestIngredients:

    def test_get_type_for_ingredient_successful(self):
        """Проверка типа ингредиента"""
        add_ingredients = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert add_ingredients.get_type() == Data.INGREDIENT_TYPE, 'Не правильный тип ингредиента'

    def test_get_price_for_ingredient_successful(self):
        """Проверка цены ингредиента"""
        add_ingredients = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert add_ingredients.get_price() == Data.INGREDIENT_PRICE, 'Не правильная цена ингредиента'

    def test_get_name_for_ingredient_successful(self):
        """Проверка имени ингредиента"""
        add_ingredients = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert add_ingredients.get_name() == Data.INGREDIENT_NAME, 'Неверное имя ингредиента'
