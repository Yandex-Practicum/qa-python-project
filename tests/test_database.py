from praktikum.database import Database


class TestDatabase:
    """
    Тестирование класса Database (база данных ингредиентов).
    Проверяет корректность работы методов available_buns() и available_ingredients().
    """

    def test_available_buns_should_return_three_buns(self):
        """Проверяет, что available_buns() возвращает 3 вида булочек."""
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_should_return_six_ingredients(self):
        """Проверяет, что available_ingredients() возвращает 6 ингредиентов."""
        database = Database()
        assert len(database.available_ingredients()) == 6