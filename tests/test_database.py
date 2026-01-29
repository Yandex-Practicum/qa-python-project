from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDataBase:
    def test_available_buns(self,database): #тест_метода_available_buns
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun" and buns[0].get_price() == 100
        assert buns[-1].get_name() == "red bun" and buns[-1].get_price() == 300
        assert len(buns) == 3

    def test_available_ingredients(self,database): #тест_метода_available_ingredients
        ingredients = database.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce" and ingredients[0].get_price() == 100
        assert ingredients[-1].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[-1].get_name() == "sausage" and ingredients[-1].get_price() == 300
        assert len(ingredients) == 6