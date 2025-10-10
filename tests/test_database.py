import allure
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BUN_NAME, BUN_PRICE, SAUCE_NAME, FILLING_NAME

class TestDatabase:
    @allure.title('Получение доступных булочек')
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == BUN_NAME
        assert buns[0].get_price() == BUN_PRICE

    @allure.title('Получение доступных ингредиентов')
    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3
        assert sauces[0].get_name() == SAUCE_NAME
        assert fillings[0].get_name() == FILLING_NAME
