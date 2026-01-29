from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        #Проверяем, что метод возвращает список из 3 доступных булочек

        database = Database()

        assert len(database.available_buns()) == 3
        assert database.available_buns()[0].get_name() == "black bun"
        assert database.available_buns()[0].get_price() == 100

    def test_available_ingredients(self):
        #Проверяем, что метод возвращает список из 6 доступных ингридиентов
        database = Database()

        assert len(database.available_ingredients()) == 6
        assert database.available_ingredients()[2].get_name() == "chili sauce"
        assert database.available_ingredients()[2].get_price() == 300

