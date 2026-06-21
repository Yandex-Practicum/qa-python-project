from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    # Провека что база данных инициализируется с непустыми списками булочек и ингридиентов
    def test_database_creation_success(self):
        db = Database()
        assert len(db.buns) > 0 and len(db.ingredients) > 0

    # ровека что cписок доступных булочек возвращается
    def test_available_buns_success(self):
        db = Database()
        buns = db.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    # ровека что cписок доступных ингридиентов возвращается
    def test_available_ingredients_success(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)