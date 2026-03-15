import allure

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    @allure.title("Получение списка доступных булочек")
    def test_available_buns_returns_list_of_buns(self, db):
        with allure.step(
            "Создаем пустой список для названий булочек и список для доступных булочек, в который положим результат вызова available_buns()"
        ):
            bun_names = []
            buns_list = db.available_buns()

        with allure.step(
            "Складываем в пустой список все полученные названия булочек и проверяем, что они там есть"
        ):
            for bun in buns_list:
                bun_names.append(bun.get_name())
            assert "black bun" in bun_names
            assert "white bun" in bun_names
            assert "red bun" in bun_names

        with allure.step("Проверяем, что все полученные сущности — булочки"):
            for bun in buns_list:
                assert isinstance(bun, Bun)

    @allure.title("Получение списка доступных ингредиентов")
    def test_available_ingredients_returns_list_of_ingredients(self, db):
        with allure.step(
            "Создаем пустой список для названий ингредиаентов и список для доступных ингредиентов, в который положим результат вызова available_ingredients()"
        ):
            ingredient_names = []
            ingredient_list = db.available_ingredients()

        with allure.step(
            "Складываем в пустой список все полученные названия ингредиентов и проверяем, что они там есть"
        ):
            for ingredient in ingredient_list:
                ingredient_names.append(ingredient.get_name())
            assert "hot sauce" in ingredient_names
            assert "sour cream" in ingredient_names
            assert "chili sauce" in ingredient_names
            assert "cutlet" in ingredient_names
            assert "dinosaur" in ingredient_names
            assert "sausage" in ingredient_names
        with allure.step("Проверяем, что все полученные сущности — ингредиенты"):
            for ingredient in ingredient_list:
                assert isinstance(ingredient, Ingredient)
