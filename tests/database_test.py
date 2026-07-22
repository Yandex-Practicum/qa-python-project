from praktikum.database import Database


class TestDatabase:

    def test_available_buns_return_list_of_buns(self):
        db = Database()
        buns = db.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) == 3
        
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200.0

    def test_available_ingredients_return_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        
        assert ingredients[3].get_type() == "FILLING"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100.0
