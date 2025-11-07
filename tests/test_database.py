from praktikum.database import Database

class TestDatabase:
    
    def test_available_buns_returns_list_of_available_buns(self):
        database = Database()
        list_with_buns = database.available_buns()
        
        assert isinstance(list_with_buns, list) 
        assert list_with_buns == database.buns

    
    def test_available_ingredients_returns_list_of_available_ingredients(self):
        database = Database()
        list_with_ingredients = database.available_ingredients()
        
        assert isinstance(list_with_ingredients, list) 
        assert list_with_ingredients == database.ingredients