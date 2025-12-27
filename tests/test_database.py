import sys
sys.path.insert(0,"C:/Users/alekberovalf/PycharmProjects/Diplom_1/")
from praktikum.database import Database

class TestDatabase:

    # Тест на получение количества булочек:
    def test_available_buns(self):
        data = Database()
        buns = data.available_buns()
        assert len(buns) == 3

    # Тест на получение количества доступных ингредиентов
    def test_available_ingredients(self):
        data = Database()
        buns = data.available_ingredients()
        assert len(buns) == 6