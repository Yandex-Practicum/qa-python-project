import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Database


class TestDatabase:

    def test_database_init(self):
        db = Database()
        
        # Test buns initialization
        assert len(db.buns) == 3
        assert db.buns[0].name == "black bun"
        assert db.buns[0].price == 100
        assert db.buns[1].name == "white bun"
        assert db.buns[1].price == 200
        assert db.buns[2].name == "red bun"
        assert db.buns[2].price == 300
        
        
        assert len(db.ingredients) == 6
        
        
        sauces = [ing for ing in db.ingredients if ing.type == "SAUCE"]
        assert len(sauces) == 3
        assert sauces[0].name == "hot sauce"
        assert sauces[0].price == 100
        assert sauces[1].name == "sour cream"
        assert sauces[1].price == 200
        assert sauces[2].name == "chili sauce"
        assert sauces[2].price == 300
        
        
        fillings = [ing for ing in db.ingredients if ing.type == "FILLING"]
        assert len(fillings) == 3
        assert fillings[0].name == "cutlet"
        assert fillings[0].price == 100
        assert fillings[1].name == "dinosaur"
        assert fillings[1].price == 200
        assert fillings[2].name == "sausage"
        assert fillings[2].price == 300

    def test_database_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].name == "black bun"
        assert buns[1].name == "white bun"
        assert buns[2].name == "red bun"

    def test_database_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        
        sauce_count = len([ing for ing in ingredients if ing.type == "SAUCE"])
        filling_count = len([ing for ing in ingredients if ing.type == "FILLING"])
        assert sauce_count == 3
        assert filling_count == 3
