import pytest
import allure
from unittest.mock import Mock
from unittest.mock import patch

from conftest import *
from helpers import ingredients_list
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    @allure.title("Добавление булочки в бургер")
    @allure.description("Тест проверяет Добавление булочки в бургере")
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    @allure.title("Добавление ингредиентов в бургер")
    @allure.description("Тест проверяет Добавление ингредиентов в бургере")
    @pytest.mark.parametrize(
        "ingredient",
        [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        ],
    )
    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        with allure.step(
            "Проверяем, что последний добавленный ингредиент = ingredient"
        ):
            assert burger.ingredients[-1] == ingredient

    @allure.title("Удаление ингредиента из бургера")
    @allure.description("Тест проверяет удаление ингредиента из бургера")
    def test_remove_ingredient(self, burger):
        with allure.step("Добавляем ингредиенты в бургер"):
            for ingredient in ingredients_list():
                burger.add_ingredient(ingredient)
            with allure.step("Удаляем второй ингредиент"):
                burger.remove_ingredient(1)
                with allure.step("Проверяем, что ингредиент 'dinosaur' удален"):
                    assert len(burger.ingredients) == 1
                    assert burger.ingredients[0].get_name() == "sour cream"

    @allure.title("Перемещение ингредиентов")
    @allure.description(
        "Тест проверяет возможность переместить ингредиент внутри бургера"
    )
    def test_move_ingredient(self, burger):

        with allure.step("Добавляем ингредиенты в бургер"):
            for ingredient in ingredients_list():

                burger.add_ingredient(ingredient)
            with allure.step("Меняем местами первый и второй ингредиент"):
                burger.move_ingredient(0, 1)

                with allure.step("Проверяем, что ингредиенты поменялись местами"):
                    assert burger.ingredients[0].get_name() == "dinosaur"
                    assert burger.ingredients[1].get_name() == "sour cream"

    @allure.title("Расчет стоимости бургера без ингредиентов")
    @allure.description("Тест проверяет расчет стоимости бургера без ингредиентов")
    def test_get_price_without_ingredients(self, burger):
        with allure.step("создаем мок булочки"):
            mock_bun = Mock()
            mock_bun.get_price.return_value = 100
            with allure.step("кладем мок расчета стоимости булочек в бургер"):
                burger.set_buns(mock_bun)
                with allure.step("проверяем расчет стоимости бургера без ингредиентов"):
                    assert burger.get_price() == 200

    @allure.title("Расчет стоимости бургера с ингредиентами")
    @allure.description("Тест проверяет расчет стоимости бургера с ингредиентами")
    def test_get_price_with_ingredients(self, burger):
        with allure.step("мокаем стоимость булочек"):
            mock_bun = Mock()
            mock_bun.get_price.return_value = 100
            burger.set_buns(mock_bun)
            with allure.step("добавляем ингредиент и мокаем его стоимость"):
                mock_ingredient1 = Mock()
                mock_ingredient1.get_price.return_value = 200
                burger.add_ingredient(mock_ingredient1)

                mock_ingredient2 = Mock()
                mock_ingredient2.get_price.return_value = 300
                burger.add_ingredient(mock_ingredient2)
                
                mock_ingredient3 = Mock()
                mock_ingredient3.get_price.return_value = 50.5
                burger.add_ingredient(mock_ingredient3)
                
                with allure.step("проверяем расчет стоимости бургера"):
                    assert burger.get_price() == 750.5
                    
                    
    @allure.title("Формирование строк чека с именем верхней и нижней булочки")
    @allure.description("Тест проверяет корректность формирование строк в чеке по формату (==== <get_name> ====) для верхней и нижней булочки")
    def test_get_receipt_shows_bun_on_top_and_bottom(self, burger):
        with allure.step("мокаем булочку"):
            mock_bun = Mock()
            mock_bun.get_name.return_value = 'white bun'
            mock_bun.get_price.return_value = 100
            burger.set_buns(mock_bun)
            with allure.step("Сохраняем вызов get_receipt() в переменную и разбиваем чек на строки"):
                receipt_lines = burger.get_receipt().split('\n')
                with allure.step("проверяем корректность формирование строки с нижней булочкой"):
                    assert receipt_lines[0] == "(==== white bun ====)"
                    assert receipt_lines[-3] == "(==== white bun ====)"
                    
    @allure.title("Формирование строки чека со стоимостью бургера")
    @allure.description("Тест проверяет корректность формирования строки чека  со стоимостью бургера")
    def test_get_receipt_shows_correct_price_line(self, burger):
        with allure.step("мокаем булочку"):
            mock_bun = Mock()
            mock_bun.get_name.return_value = 'white bun'
            mock_bun.get_price.return_value = 100
            burger.set_buns(mock_bun)
            with allure.step("Сохраняем вызов get_receipt() в переменную и разбиваем чек на строки"):
                receipt_lines = burger.get_receipt().split('\n')
                with allure.step("проверяем корректность формирование строки со стоимостью бургера"):
                    assert receipt_lines[-1] == 'Price: 200'
                    
    @allure.title("Формирование строки чека со стоимостью ингредиентов бургера")
    @allure.description("Тест проверяет корректность формирования строки чека  со стоимостью ингредиентов бургера")
    def test_get_receipt_shows_correct_ingredient_line(self, burger):
        with allure.step("мокаем булочку"):
            mock_bun = Mock()
            mock_bun.get_name.return_value = 'white bun'
            mock_bun.get_price.return_value = 100
            burger.set_buns(mock_bun)
            mock_ingredient1 = Mock()
            mock_ingredient1.get_type.return_value = "SAUCE"
            mock_ingredient1.get_name.return_value = "hot sauce"
            mock_ingredient1.get_price.return_value = 100
            burger.add_ingredient(mock_ingredient1)
            mock_ingredient2 = Mock()
            mock_ingredient2.get_type.return_value = "FILLING"
            mock_ingredient2.get_name.return_value = "dinosaur"
            mock_ingredient2.get_price.return_value = 100
            burger.add_ingredient(mock_ingredient2)
            with allure.step("Сохраняем вызов get_receipt() в переменную и разбиваем чек на строки"):
                receipt_lines = burger.get_receipt().split('\n')
                with allure.step("проверяем корректность формирование строки со стоимостью бургера"):
                    assert receipt_lines[1] == '= sauce hot sauce ='