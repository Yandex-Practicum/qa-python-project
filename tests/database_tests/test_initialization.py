from database import Database
from bun import Bun
from ingredient import Ingredient

class TestDatabaseInitialization:
    
    def setup_method(self):
        self.database = Database()
    
    def test_initialization_creates_three_buns(self):
        assert len(self.database.buns) == 3
    
    def test_initialization_buns_are_bun_instances(self):
        assert all(isinstance(bun, Bun) for bun in self.database.buns)
    
    def test_initialization_creates_six_ingredients(self):
        assert len(self.database.ingredients) == 6
    
    def test_initialization_ingredients_are_ingredient_instances(self):
        assert all(isinstance(ing, Ingredient) for ing in self.database.ingredients)