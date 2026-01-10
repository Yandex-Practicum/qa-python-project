from praktikum.database import Database


class TestDatabase:

    def test_check_available_buns_successful(self):
        """Проверка доступности количества булок. ОР: в базе данных доступно 3 булки"""
        database = Database()

        assert len(database.available_buns()) == 3

    def test_check_available_ingredients_successful(self):
        """Проверка доступности количества ингедиентов. ОР: в базе данных доступно 6 ингредиентов"""
        database = Database()

        assert len(database.available_ingredients()) == 6
