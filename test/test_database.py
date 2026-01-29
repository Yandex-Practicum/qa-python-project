import allure
from praktikum.database import Database


@allure.feature("Тестирование класса Database")
class TestDatabase:


    @allure.title("Проверка создания объекта класса Database")
    def test_create_class_object(self):
        db_tst = Database()
        db_tst_buns = db_tst.buns
        db_tst_ingridients = db_tst.ingredients
        assert len(db_tst_buns) == 3 and len(db_tst_ingridients) == 6


    @allure.title("Проверка метода available_buns")
    def test_available_buns(self):
        db_tst = Database()
        db_tst_buns = db_tst.available_buns()
        assert len(db_tst_buns) == 3


    @allure.title("Проверка метода available_ingredients")
    def test_available_ingredients(self):
        db_tst = Database()
        db_tst_ingridients = db_tst.available_ingredients()
        assert len(db_tst_ingridients) == 6
