from praktikum.ingredient_types import *

class TestDatabase:
    
    def test_get_available_buns(self, database):
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    def test_get_avaliable_ingredients(self, database):
        avaliable_ingredients = database.available_ingredients()
        assert len(avaliable_ingredients) == 6

    def test_get_avaliable_sauces(self, database):
        available_sauces = database.available_ingredients()
        sause_type = [i for i in available_sauces if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sause_type) == 3

    def test_get_avaliable_fillings(self, database):
        available_fillings = database.available_ingredients()
        filling_type = [i for i in available_fillings if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(filling_type) == 3
