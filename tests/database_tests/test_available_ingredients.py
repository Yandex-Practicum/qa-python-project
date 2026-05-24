from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabaseAvailableIngredients:
    
    def setup_method(self):
        self.database = Database()
    
    def test_available_ingredients_returns_six_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
    
    def test_available_ingredients_contains_three_sauces(self):
        ingredients = self.database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
    
    def test_available_ingredients_contains_three_fillings(self):
        ingredients = self.database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
    
    def test_available_ingredients_returns_same_reference(self):
        ingredients1 = self.database.available_ingredients()
        ingredients2 = self.database.available_ingredients()
        assert ingredients1 is ingredients2