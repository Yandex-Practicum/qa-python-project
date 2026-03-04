import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "Very long ingredient name", 999.99)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        #Проверка инициализации ингредиента с разными параметрами
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
    
    def test_ingredient_price_getter(self):
        #Проверка получения цены ингредиента
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 150)
        assert ingredient.get_price() == 150
    
    def test_ingredient_name_getter(self):
        #Проверка получения названия ингредиента
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
        assert ingredient.get_name() == "cutlet"
    
    def test_ingredient_type_getter(self):
        #Проверка получения типа ингредиента
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("invalid_type", "sauce", 100),
        (None, "sauce", 100),
        (INGREDIENT_TYPE_SAUCE, None, 100),
        (INGREDIENT_TYPE_SAUCE, "sauce", None),
        (INGREDIENT_TYPE_SAUCE, "sauce", "100"),
        (123, "sauce", 100),
        (INGREDIENT_TYPE_SAUCE, 456, 100),
        (INGREDIENT_TYPE_SAUCE, "sauce", "not a number")
    ])
    def test_ingredient_accepts_any_types(self, ingredient_type, name, price):
        #Проверка, что класс принимает любые типы данных
        ingredient = Ingredient(ingredient_type, name, price)
        
        # Проверяем, что объект создался
        assert ingredient is not None
        
        # Проверяем, что значения сохранились
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price