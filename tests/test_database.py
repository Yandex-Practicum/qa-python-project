import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
        def test_available_buns_returns_list(self):
            db = Database()
            buns = db.available_buns()
            assert isinstance(buns, list), "Метод должен возвращать список"

        def test_available_buns_contains_bun_objects(self):
            db = Database()
            buns = db.available_buns()
            assert all(isinstance(b, Bun) for b in buns), "Все элементы должны быть экземплярами Bun"

        def test_available_buns_has_correct_length(self):
            db = Database()
            buns = db.available_buns()
            assert len(buns) == 3, "Должно быть 3 вида булочек"

        def test_available_buns_has_correct_names(self):
            db = Database()
            buns = db.available_buns()
            bun_names = [bun.get_name() for bun in buns]
            assert "black bun" in bun_names
            assert "white bun" in bun_names
            assert "red bun" in bun_names

        def test_available_buns_has_correct_prices(self):
            db = Database()
            buns = db.available_buns()
            bun_prices = [bun.get_price() for bun in buns]
            assert 100 in bun_prices
            assert 200 in bun_prices
            assert 300 in bun_prices

        def test_available_ingredients_returns_list(self):
            db = Database()
            ingredients = db.available_ingredients()
            assert isinstance(ingredients, list), "Метод должен возвращать список"

        def test_available_ingredients_contains_ingredient_objects(self):
            db = Database()
            ingredients = db.available_ingredients()
            assert all(isinstance(i, Ingredient) for i in ingredients), "Все элементы должны быть экземплярами Ingredient"

        def test_available_ingredients_has_correct_length(self):
            db = Database()
            ingredients = db.available_ingredients()
            assert len(ingredients) == 6, "Должно быть 6 ингредиентов"

        def test_available_ingredients_has_correct_types_and_names(self):
            db = Database()
            ingredients = db.available_ingredients()

            sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
            sauce_names = [i.get_name() for i in sauces]
            assert len(sauces) == 3
            assert "hot sauce" in sauce_names
            assert "sour cream" in sauce_names
            assert "chili sauce" in sauce_names

            fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
            filling_names = [i.get_name() for i in fillings]
            assert len(fillings) == 3
            assert "cutlet" in filling_names
            assert "dinosaur" in filling_names
            assert "sausage" in filling_names

        def test_available_ingredients_has_correct_prices(self):
            db = Database()
            ingredients = db.available_ingredients()
            prices = [i.get_price() for i in ingredients]
            assert 100 in prices
            assert 200 in prices
            assert 300 in prices
            assert prices.count(100) == 2
            assert prices.count(200) == 2
            assert prices.count(300) == 2
