from src.praktikum.database import Database
from src.praktikum.bun import Bun
from src.praktikum.ingredient import Ingredient
from src.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_database_initialization(self):
        """Тест инициализации базы данных"""
        db = Database()
        assert (len(db.buns) == 3
                and len(db.ingredients) == 6)

    def test_available_buns(self):
        """Тест получения доступных булок"""
        db = Database()
        buns = db.available_buns()

        assert (len(buns) == 3
                and buns[0].get_name() == "black bun"
                and buns[1].get_name() == "white bun"
                and  buns[2].get_name() == "red bun")
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_buns_prices(self):
        """Тест цен доступных булок"""
        db = Database()
        buns = db.available_buns()

        assert (buns[0].get_price() == 100
                and buns[1].get_price() == 200
                and buns[2].get_price() == 300)

    def test_available_ingredients(self):
        """Тест получения доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    def test_available_ingredients_types(self):
        """Тест типов доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()

        # Первые три - соусы
        for i in range(3):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE

        # Следующие три - начинки
        for i in range(3, 6):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_FILLING

    def test_available_ingredients_names(self):
        """Тест названий доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()

        expected_names = ["hot sauce", "sour cream", "chili sauce",
                          "cutlet", "dinosaur", "sausage"]

        for i, expected_name in enumerate(expected_names):
            assert ingredients[i].get_name() == expected_name

    def test_database_buns_are_independent(self):
        """Тест независимости списка булок при создании новой БД"""
        db1 = Database()
        db2 = Database()

        assert db1.buns is not db2.buns
        assert len(db1.buns) == len(db2.buns)

    def test_database_ingredients_are_independent(self):
        """Тест независимости списка ингредиентов при создании новой БД"""
        db1 = Database()
        db2 = Database()

        assert db1.ingredients is not db2.ingredients
        assert len(db1.ingredients) == len(db2.ingredients)