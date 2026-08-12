from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_database_initialization(self,db):
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    def test_available_buns(self,db):
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients(self,db):
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        assert sauces[0].get_name() == "hot sauce"
        assert sauces[0].get_price() == 100
        assert sauces[1].get_name() == "sour cream"
        assert sauces[1].get_price() == 200
        assert sauces[2].get_name() == "chili sauce"
        assert sauces[2].get_price() == 300
        
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        assert fillings[0].get_name() == "cutlet"
        assert fillings[0].get_price() == 100
        assert fillings[1].get_name() == "dinosaur"
        assert fillings[1].get_price() == 200
        assert fillings[2].get_name() == "sausage"
        assert fillings[2].get_price() == 300

    def test_database_buns_are_different_objects(self,db):
        buns = db.available_buns()
        assert buns[0] is not buns[1]
        assert buns[1] is not buns[2]

    def test_database_ingredients_are_different_objects(self,db):
        ingredients = db.available_ingredients()
        for i in range(len(ingredients) - 1):
            assert ingredients[i] is not ingredients[i + 1]