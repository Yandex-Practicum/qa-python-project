from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDataBase:
    def test_get_available_ingredients_correct(self):
        data_ingredients = Database()

        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6
        
    def test_get_available_buns_correct(self):
        data_bun = Database()

        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

    def test_get_available_ingredients_prices_correct(self):
        data_price = Database()

        ingredients = data_price.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}

        assert price['hot sauce'] == 100

    def test_get_count_available_sauces_correct(self):
        count_ingredients = Database()

        ingredients = count_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]

        assert len(type_sauce) == 3

    def test_get_count_available_fillings_correct(self):
        correct_ingredients = Database()

        ingredients = correct_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(type_fillings) == 3
