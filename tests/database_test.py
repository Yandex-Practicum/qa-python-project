import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    # тест проверяет, что булка с соответствующим именем была найдена и ее цена совпадает с ожидаемой
    @pytest.mark.parametrize(
        'name, expected_price',
        [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ])
    def test_available_buns(self, mock_database, name, expected_price):
        mock_database.available_buns.return_value = mock_database.buns
        available_buns = mock_database.available_buns()
        bun = next((b for b in available_buns if b.name == name), None)
        assert bun is not None and bun.price == expected_price

    # тест проверяет, что ингредиент с соответствующим именем был найден и его цена совпадает с ожидаемой
    @pytest.mark.parametrize(
        'ingredient_type, name, expected_price',
        [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 200)
        ])
    def test_available_ingredients(self, mock_database, ingredient_type, name, expected_price):
        mock_database.available_ingredients.return_value = mock_database.ingredients
        available_ingredients = mock_database.available_ingredients()
        ingredient = next((i for i in available_ingredients if i.type == ingredient_type and i.name == name), None)
        assert ingredient is not None and ingredient.price == expected_price

    # тест проверяет, что если в базе данных нет данных по булкам, приходит пустой список
    def test_available_buns_empty(self):
        db = Database()
        db.buns = []
        assert db.available_buns() == []

    # тест проверяет, что если в базе данных нет данных по ингредиентам, приходит пустой список
    def test_available_ingredients_empty(self):
        db = Database()
        db.ingredients = []
        assert db.available_ingredients() == []

    # тест проверяет, что метод available_buns возвращает список
    def test_available_buns_type(self):
        db = Database()
        assert isinstance(db.available_buns(), list)

    # тест проверяет, что метод available_ingredients возвращает список
    def test_available_ingredients_type(self):
        db = Database()
        assert isinstance(db.available_ingredients(), list)
