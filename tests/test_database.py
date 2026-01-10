from praktikum.database import Database
from data import Data


class TestDataBase:

    # Проверка доступных булок
    def test_available_buns(self):
        bun = Database()
        available_buns = bun.available_buns()
        assert len(available_buns) == Data.AVAILABLE_BUNS

    # Проверка доступных ингридиентов
    def test_available_ingredients(self):
        ingredient = Database()
        available_ingredients = ingredient.available_ingredients()
        assert len(available_ingredients) == Data.AVAILABLE_INGREDIENTS
