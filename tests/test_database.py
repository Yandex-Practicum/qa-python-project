import pytest
from unittest.mock import patch
from tests import data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == len(data.DatabaseData.EXPECTED_BUNS)

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == len(data.DatabaseData.EXPECTED_INGREDIENTS)

    def test_buns_have_name_and_price(self):
        db = Database()
        buns = db.available_buns()

        for bun in buns:
            assert isinstance(bun, Bun)
            name = bun.get_name()
            price = bun.get_price()
            assert isinstance(name, str)
            assert isinstance(price, (int, float))
            assert len(name) > 0
            assert price >= 0

    def test_ingredients_have_type_name_and_price(self):
        db = Database()
        ingredients = db.available_ingredients()

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
            ingredient_type = ingredient.get_type()
            name = ingredient.get_name()
            price = ingredient.get_price()

            assert isinstance(ingredient_type, str)
            assert ingredient_type in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
            assert isinstance(name, str)
            assert isinstance(price, (int, float))
            assert len(name) > 0
            assert price >= 0

    def test_database_contains_correct_buns(self):
        db = Database()
        buns = db.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        bun_prices = [bun.get_price() for bun in buns]

        for expected_name, expected_price in data.DatabaseData.EXPECTED_BUNS:
            assert expected_name in bun_names
            for i, name in enumerate(bun_names):
                if name == expected_name:
                    assert bun_prices[i] == expected_price

    def test_database_contains_correct_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        for expected_type, expected_name, expected_price in data.DatabaseData.EXPECTED_INGREDIENTS:
            found = False
            for ingredient in ingredients:
                if (ingredient.get_type() == expected_type and
                    ingredient.get_name() == expected_name and
                    ingredient.get_price() == expected_price):
                    found = True
                    break
            assert found, f"Не найден ингредиент: {expected_type}, {expected_name}, {expected_price}"

    def test_database_contains_sauces_and_fillings(self):
        db = Database()
        ingredients = db.available_ingredients()

        sauce_count = 0
        filling_count = 0

        for ingredient in ingredients:
            if ingredient.get_type() == INGREDIENT_TYPE_SAUCE:
                sauce_count += 1
            elif ingredient.get_type() == INGREDIENT_TYPE_FILLING:
                filling_count += 1

        expected_sauces = len([ing for ing in data.DatabaseData.EXPECTED_INGREDIENTS if ing[0] == INGREDIENT_TYPE_SAUCE])
        expected_fillings = len([ing for ing in data.DatabaseData.EXPECTED_INGREDIENTS if ing[0] == INGREDIENT_TYPE_FILLING])

        assert sauce_count == expected_sauces, f"Ожидалось {expected_sauces} соусов, но найдено {sauce_count}"
        assert filling_count == expected_fillings, f"Ожидалось {expected_fillings} начинок, но найдено {filling_count}"
