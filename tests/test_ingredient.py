from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as IT
import pytest


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type', [IT.INGREDIENT_TYPE_FILLING, IT.INGREDIENT_TYPE_SAUCE])
    def test_get_ingr_type(self, ingredient_type):
        ingr = Ingredient(ingredient_type, "name", 10)
        assert ingr.get_type() == ingredient_type
    
    @pytest.mark.parametrize('name', ["Имя", "Name", "1111", " ", "@@@@"])
    def test_get_ingr_name(self, name):
        ingr = Ingredient(IT.INGREDIENT_TYPE_FILLING, name, 10)
        
        assert ingr.get_name() == name
    
    @pytest.mark.parametrize('price', [0, 666, 1111.00, " ", -9])
    def test_get_ingr_price(self, price):
        ingr = Ingredient(IT.INGREDIENT_TYPE_FILLING, 'name',price)
        assert ingr.get_price() == price