import allure
from praktikum.database import Database

@allure.epic("Stellar Burgers")
@allure.feature("Юнит-тесты компонентов: База данных")
class TestDatabase:
    @allure.title("Проверка списка доступных булочек в базе данных")
    def test_available_buns_initialized_database_returns_three_buns(self):
        with allure.step("Инициализировать базу данных"):
            bd = Database()
        with allure.step("Получить список дотупных булочек"):
            buns = bd.available_buns()
        with allure.step("Проверить, что в базе данных ровно 3 булочки и они имеют корректные названия"):
            assert len(buns) == 3
            assert buns[0].get_name() == "black bun"
            assert buns[1].get_name() == "white bun"
            assert buns[2].get_name() == "red bun"
    @allure.title("Проверка списка доступных ингредиентов в базе данных")
    def test_available_ingredients_returns_correct_list_and_size(self):
        with allure.step("Инициализировать базу данных"):
            db = Database()
            
        with allure.step("Получить список доступных ингредиентов"):
            ingredients = db.available_ingredients()
            
        with allure.step("Проверить, что в базе ровно 6 ингредиентов"):
            assert len(ingredients) == 6
            
        with allure.step("Проверить названия первых трех соусов"):
            assert ingredients[0].get_name() == "hot sauce"
            assert ingredients[1].get_name() == "sour cream"
            assert ingredients[2].get_name() == "chili sauce"
            
        with allure.step("Проверить названия последних трех начинок"):
            assert ingredients[3].get_name() == "cutlet"
            assert ingredients[4].get_name() == "dinosaur"
            assert ingredients[5].get_name() == "sausage"
            