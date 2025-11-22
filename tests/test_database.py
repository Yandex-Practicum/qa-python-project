from unittest.mock import patch
import pytest
from practikum.database import Database
from practikum.constants import H_DB, H_DB_BUNS, H_DB_INGREDIENTS

class TestDatabase:
    # Проверяем доступные булки через метод available_buns().
    @pytest.mark.parametrize("bun_name, bun_price", H_DB_BUNS)
    def test_available_buns(self, bun_name, bun_price):
        db = Database()
        buns = db.available_buns()
        for bun in buns:    # Для каждой булки в заданном списке проверяем её имя и цену
            if bun.name == bun_name:
                assert bun.price == bun_price, "Метод available_buns возвращает неверную цену."

    # Проверяем доступные ингредиенты через метод available_ingredients().
    @pytest.mark.parametrize("ingredient_type, name, price", H_DB_INGREDIENTS)
    def test_available_ingredients(self, ingredient_type, name, price):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients: # Для каждого ингредиента в списке проверяем его имя, тип и цену
            if ingredient.name == name:
                assert ingredient.type == ingredient_type, "Метод available_ingredients возвращает неверный тип."
                assert ingredient.price == price, "Метод available_ingredients возвращает неверную цену."


    # Мокируем данные в Database, параметризуем эти данные
    @pytest.mark.parametrize("mock_buns, mock_ingredients", H_DB)
    @patch('practikum.database.Database.__init__', return_value=None)
    def test_mocked_database_with_parametrize(self, mock_init, mock_buns, mock_ingredients):
        db = Database()
        db.buns = mock_buns
        db.ingredients = mock_ingredients

        # Проверяем, что метод available_buns возвращает правильные данные
        available_buns = db.available_buns()
        assert len(available_buns) == len(mock_buns), "Возвращаемое количество булок не соответствует заданному."
        for i in range(len(available_buns)):
            assert available_buns[i].name == mock_buns[i].name, "Метод available_buns возвращает неверное имя."
            assert available_buns[i].price == mock_buns[i].price, "Метод available_buns возвращает неверную цену."

        # Проверяем, что метод available_ingredients возвращает правильные данные
        available_ingredients = db.available_ingredients()
        assert len(available_ingredients) == len(mock_ingredients), "Возвращаемое количество ингредиентов не соответствует заданному."
        for i in range(len(available_ingredients)):
            assert available_ingredients[i].name == mock_ingredients[i].name, "Метод available_ingredients возвращает неверное имя."
            assert available_ingredients[i].type == mock_ingredients[i].type, "Метод available_ingredients возвращает неверный тип."
            assert available_ingredients[i].price == mock_ingredients[i].price, "Метод available_ingredients возвращает неверную цену."

