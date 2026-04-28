import pytest
from praktikum.ingredient import Ingredient
from data import ingredient_data, exception_receipt

class TestBurger:
    def test_set_buns_success(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun
       
    @pytest.mark.parametrize('ingredient_type, name, price', ingredient_data) 
    def test_add_ingredients_success(self, burger, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1
        
    def test_remove_ingredient_success(self, burger):
        ingredient1 = Ingredient(*ingredient_data[0])
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(*ingredient_data[1])
        burger.add_ingredient(ingredient2)
        assert ingredient1 in burger.ingredients
        assert ingredient2 in burger.ingredients
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(1)
        assert ingredient1 in burger.ingredients
        assert ingredient2 not in burger.ingredients
        assert len(burger.ingredients) == 1
        
    def test_move_ingredient_success(self, burger):
        ingredient1 = Ingredient(*ingredient_data[0])
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(*ingredient_data[1])
        burger.add_ingredient(ingredient2)
        assert ingredient1 == burger.ingredients[0]
        assert ingredient1 != burger.ingredients[1]
        burger.move_ingredient(0,1)
        assert ingredient1 == burger.ingredients[1]
        
    def test_get_price_success(self, burger, bun):
        burger.set_buns(bun)
        ingredient1 = Ingredient(*ingredient_data[0])
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(*ingredient_data[1])
        burger.add_ingredient(ingredient2)
        buns_price = bun.get_price() * 2
        ingredients_price = ingredient_data[0][2] + ingredient_data[1][2]
        assert burger.get_price() == buns_price + ingredients_price
        
    def test_get_receipt(self, burger, bun):
        burger.set_buns(bun)
        ingredient1 = Ingredient(*ingredient_data[0])
        burger.add_ingredient(ingredient1)
        ingredient2 = Ingredient(*ingredient_data[1])
        burger.add_ingredient(ingredient2)
        assert burger.get_receipt() == exception_receipt