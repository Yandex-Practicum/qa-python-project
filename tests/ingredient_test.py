import sys
import os

# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE)

class TestIngredient:
    
    #Тест создания ингридиента с валидными параметрами
    def test_init_with_valid_parameters(self):
        type = INGREDIENT_TYPE_SAUCE
        name = "Горчица"
        price = 2.5
        ingredient = Ingredient(type, name, price)

        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "Горчица"
        assert ingredient.price == 2.5

    #Тест метода get_price возвращает правильную цену
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 3.0)
        
        assert ingredient.get_price() == 3.0

   #Тест метода get_name возвращает правильное название
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Горчица", 1.5)

        assert ingredient.get_name() == "Горчица"

   #Тест метода get_type возвращает правильный тип ингридиента
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Салат", 0.5)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
