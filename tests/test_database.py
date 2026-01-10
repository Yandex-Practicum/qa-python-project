# Проверки класса Database без моков
from praktikum.database import Database


class TestDatabase:
    def test_available_buns_len_is_three(self):
        database = Database()

        assert len(database.available_buns()) == 3

    def test_available_ingredients_len_is_six(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
