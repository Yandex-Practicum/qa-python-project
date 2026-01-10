from praktikum.database import Database


class TestDatabase:

    # Проверка доступных булочек
    def test_count_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    # Проверка доступных ингредиентов
    def test_count_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
