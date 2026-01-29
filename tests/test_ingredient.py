import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "Mayo", 1.0),
        ("FILLING", "Cheese", 2.0),
    ])
    #Тест добавление нового ингредиента
    def test_new_ingredient(self, ingredient_type, name, price):
        #Создаем новый ингредиент new_ingredient с переданными параметрами
        new_ingredient = Ingredient(ingredient_type, name, price)
        #Проверяем, что тип нового ингредиента соответствует переданному параметру ingredient_type
        assert new_ingredient.get_type() == ingredient_type
        #Проверяем, что название нового ингредиента соответствует переданному параметру name
        assert new_ingredient.get_name() == name
        #Проверяем, что цена нового ингредиента соответствует переданному параметру price
        assert new_ingredient.get_price() == price

    #Тест получение цены нового ингредиента
    def test_get_price(self):
        #Cоздаем новый ингредиент с типом "SAUCE", названием "Mayo" и ценой 1.0
        new_ingredient = Ingredient("SAUCE", "Mayo", 1.0)
        #Проверяем, что цена этого ингредиента равна 1.0
        assert new_ingredient.get_price() == 1.0

    # Тест получение наименования ингредиента
    def test_get_name(self):
        #Cоздаем новый ингредиент с типом "SAUCE", названием "Mayo" и ценой 1.0
        new_ingredient = Ingredient("SAUCE", "Mayo", 1.0)
        #Проверяем, что название этого ингредиента равно "Mayo"
        assert new_ingredient.get_name() == "Mayo"

    # Тест получение типа ингредиента
    def test_get_type(self):
        #Cоздаем новый ингредиент с типом "SAUCE", названием "Mayo" и ценой 1.0
        new_ingredient = Ingredient("SAUCE", "Mayo", 1.0)
        #Проверяем, что тип этого ингредиента равен "SAUCE"
        assert new_ingredient.get_type() == "SAUCE"
