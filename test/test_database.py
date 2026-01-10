import pytest
from Diplom_1.database import Database
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient

class Test_Database:
    """
    Класс для тестирования класса Database.
    """

    @pytest.fixture
    def database(self):
        """
        Фикстура для создания экземпляра Database.
        """
        return Database()

    def test_available_buns(self, database):
        """
        Проверяет, что метод available_buns() возвращает список булок.
        """
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)  # Проверяем, что все элементы списка - Bun

    def test_available_ingredients(self, database):
        """
        Проверяет, что метод available_ingredients() возвращает список ингредиентов.
        """
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients) # Проверяем, что все элементы списка - Ingredient

    def test_initial_buns(self, database):
        """
        Проверяет, что в базе данных изначально присутствуют нужные булки.
        """
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].name == "black bun"
        assert buns[1].name == "white bun"
        assert buns[2].name == "red bun"

    def test_initial_ingredients(self, database):
        """
        Проверяет, что в базе данных изначально присутствуют нужные ингредиенты.
        """
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].name == "hot sauce"
        assert ingredients[1].name == "sour cream"
        assert ingredients[2].name == "chili sauce"
        assert ingredients[3].name == "cutlet"
        assert ingredients[4].name == "dinosaur"
        assert ingredients[5].name == "sausage"
