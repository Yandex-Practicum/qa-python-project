import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self, database_fixture):
        expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        actual_buns = database_fixture.available_buns()

        assert len(expected_buns) == len(actual_buns), "Количество булочек не совпадает"
        for expected_bun, actual_bun in zip(expected_buns, actual_buns):
            assert expected_bun.name == actual_bun.name, f"Имя булочки не совпадает: {expected_bun.name} != {actual_bun.name}"
            assert expected_bun.price == actual_bun.price, f"Цена булочки не совпадает: {expected_bun.price} != {actual_bun.price}"

    def test_available_ingredients(self, database_fixture):
        expected_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
        actual_ingredients = database_fixture.available_ingredients()
        assert len(expected_ingredients) == len(actual_ingredients), "Количество ингредиентов не совпадает"
        for expected_ingredient, actual_ingredient in zip(expected_ingredients, actual_ingredients):
            assert expected_ingredient.type == actual_ingredient.type, f"Тип ингредиента не совпадает: {expected_ingredient.name} != {actual_ingredient.name}"
            assert expected_ingredient.name == actual_ingredient.name, f"Имя ингредиента не совпадает: {expected_ingredient.name} != {actual_ingredient.name}"
            assert expected_ingredient.price == actual_ingredient.price, f"Цена ингредиента не совпадает: {expected_ingredient.price} != {actual_ingredient.price}"
