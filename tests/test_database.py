import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_available_buns_returns_list_of_buns(self):
        #Проверяем, что available_buns возвращает список из трёх объектов Bun
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_available_buns_contains_correct_data(self, index, expected_name, expected_price):
        #Параметризованный тест: проверяем конкретные булочки из базы
        db = Database()
        buns = db.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    def test_available_ingredients_returns_list_of_ingredients(self):
        #Проверяем, что available_ingredients возвращает список из шести объектов Ingredient
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_available_ingredients_contains_correct_data(
        self, index, expected_type, expected_name, expected_price
    ):
        #Параметризованный тест: проверяем конкретные ингредиенты из базы
        db = Database()
        ingredients = db.available_ingredients()
        ing = ingredients[index]
        assert ing.get_type() == expected_type
        assert ing.get_name() == expected_name
        assert ing.get_price() == expected_price