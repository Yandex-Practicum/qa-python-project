from database import Database

class TestDatabase:

    def test_available_buns_returns_correct_count(self):
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3

    def test_available_ingredients_returns_correct_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6

    def test_database_has_specific_bun(self):
        db = Database()
        buns = db.available_buns()
        
        names = [bun.get_name() for bun in buns]
        assert "white bun" in names

    def test_database_has_specific_ingredient(self):
        db = Database()
        ingredients = db.available_ingredients()
        
        names = [ing.get_name() for ing in ingredients]
        assert "hot sauce" in names