from unittest.mock import Mock
from praktikum.database import Database


class TestDatabase:

    # Проверяем количество доступных булочек
    def test_check_available_buns(self):
        data_buns = Database()
        buns = data_buns.available_buns()
        assert len(buns) == 3

    # Проверяем количество доступных начинок в целом
    def test_check_available_ingredients(self):
        data_buns = Database()
        ingredients = data_buns.available_ingredients()
        assert len(ingredients) == 6

    # Проверяем количество доступных соусов
    def test_check_available_sauces(self):
        data_buns = Database()
        ingredients = data_buns.available_ingredients()
        sauces = []
        for i in ingredients:
            if i.type == 'SAUCE':
                sauces.append(i)
        assert len(sauces) == 3

    # Проверяем количество доступных начинок
    def test_check_available_fillings(self):
        data_buns = Database()
        ingredients = data_buns.available_ingredients()
        fillings = []
        for i in ingredients:
            if i.type == 'FILLING':
                fillings.append(i)
        assert len(fillings) == 3
