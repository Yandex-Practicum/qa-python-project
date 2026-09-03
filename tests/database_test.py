import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    
    @pytest.fixture
    def database(self):
        return Database()
    
    def test_database_creation(self, database):
        assert database is not None
    
    def test_available_buns_count(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
    
    def test_available_buns_are_buns(self, database):
        buns = database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_buns_names(self, database):
        buns = database.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert bun_names == ["black bun", "white bun", "red bun"]
    
    def test_available_buns_prices(self, database):
        buns = database.available_buns()
        bun_prices = [bun.get_price() for bun in buns]
        assert bun_prices == [100, 200, 300]
    
    def test_available_ingredients_count(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
    
    def test_available_ingredients_are_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    
    def test_available_sauce_count(self, database):
        ingredients = database.available_ingredients()
        sauce_count = sum(1 for ing in ingredients if ing.get_type() == 'SAUCE')
        assert sauce_count == 3
    
    def test_available_filling_count(self, database):
        ingredients = database.available_ingredients()
        filling_count = sum(1 for ing in ingredients if ing.get_type() == 'FILLING')
        assert filling_count == 3
        