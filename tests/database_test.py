from models.bun import Bun
from models.database import Database
from models.ingridient import Ingredient


class TestDatabase:
    """Тесты для класса Database"""


    def test_available_buns(self):
        """Проверяем, что метод available_buns() класса Database возвращает список из 3 доступных булочек"""
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)

    def test_available_ingredients(self):
        """Проверяем, что метод available_ingredients() класса Database возвращает список из 6 доступных ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
