import pytest

from praktikum.ingredient_types import *


class TestDatabase:

    def test_available_buns_expected_length(self, db): # проверяет, что метод возвращает правильное количество булочек.
        buns = db.available_buns()

        assert len(buns) == 3, f"Ожидаем 3 булочки, но получили {len(buns)}"

    def test_available_ingredients_expected_length(self, db): # проверяет, что метод возвращает правильное количество ингредиентов.
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6 , f"Ожидаем 6 ингредиентов, но получили {len(ingredients)}"

    @pytest.mark.parametrize('buns_name, buns_price, num', [
        ('black bun', 100, 0),
        ('white bun', 200, 1),
        ('red bun', 300, 2)
    ])
    def test_available_buns(self, db, buns_name, buns_price, num): # проверяет, что метод возвращает корректные данные о булочках (название и цену).
        buns = db.available_buns()

        assert buns[num].get_name() == buns_name , f"Ожидаем название {buns_name}, но получили {buns[num].get_name()}"
        assert buns[num].get_price() == buns_price, f"Ожидаем цену {buns_price}, но получили {buns[num].get_price()}"

    @pytest.mark.parametrize('ingredients_name, ingredients_price, ingredients_type, num', [
        ('hot sauce', 100, INGREDIENT_TYPE_SAUCE, 0),
        ('sour cream', 200, INGREDIENT_TYPE_SAUCE, 1),
        ('chili sauce', 300, INGREDIENT_TYPE_SAUCE, 2),
        ('cutlet', 100, INGREDIENT_TYPE_FILLING, 3),
        ('dinosaur', 200, INGREDIENT_TYPE_FILLING, 4),
        ('sausage', 300, INGREDIENT_TYPE_FILLING, 5),
    ])
    def test_available_ingredients(self, db, ingredients_name, ingredients_price, ingredients_type, num): # Тестирует available_ingredients: проверяет, что метод возвращает корректные данные о ингредиентах (название, цена и тип).
        ingredients = db.available_ingredients()

        assert ingredients[num].get_name() == ingredients_name , f"Ожидаем название {ingredients_name}, но получили {ingredients[num].get_name()}"
        assert ingredients[num].get_price() == ingredients_price , f"Ожидаем цену {ingredients_price}, но получили {ingredients[num].get_price()}"
        assert ingredients[num].get_type() == ingredients_type, f"Ожидаем тип {ingredients_type}, но получили {ingredients[num].get_type()}"