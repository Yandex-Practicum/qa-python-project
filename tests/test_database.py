from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_available_buns_returns_list_of_buns():
    db = Database()

    buns = db.available_buns()

    assert isinstance(buns, list)
    assert buns, 'Ожидался непустой список булочек'
    assert all(isinstance(bun, Bun) for bun in buns)

    # Проверяем, что возвращаемые объекты можно корректно использовать через публичные методы
    for bun in buns:
        assert isinstance(bun.get_name(), str)
        assert isinstance(bun.get_price(), (int, float))


def test_available_ingredients_returns_list_of_ingredients():
    db = Database()

    ingredients = db.available_ingredients()

    assert isinstance(ingredients, list)
    assert ingredients, 'Ожидался непустой список ингредиентов'
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    for ingredient in ingredients:
        assert ingredient.get_type() in (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)
        assert isinstance(ingredient.get_name(), str)
        assert isinstance(ingredient.get_price(), (int, float))
