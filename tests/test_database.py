import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestDatabase:   
    
    @pytest.mark.parametrize("index, name, price", [(0, "black bun", 100),
                                                    (1, "white bun", 200),
                                                    (2, "red bun", 300)])
    def test_available_buns(self, index, name, price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].name == name 
        assert buns[index].price == price
        
    @pytest.mark.parametrize("index, type, name, price", [(0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                                                    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                                    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                                    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                                    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                                    (5, INGREDIENT_TYPE_FILLING, "sausage", 300)])
    def test_available_ingredients(self, index, type, name, price):
        db = Database()
        ingr = db.available_ingredients()
        assert ingr[index].type == type
        assert ingr[index].name == name
        assert ingr[index].price == price


    