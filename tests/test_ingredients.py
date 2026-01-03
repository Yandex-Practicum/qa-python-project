import pytest
import allure
import random

from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as it
from helpers import GenerateData


class TestIngredient:


    @allure.title('Тестирование создания экземпляра Ingredient')
    @allure.description('Проверка, что создан экземпляр с переменными, чьи значения равны заанным при создании')
    def test_init (self):
        ingr_type = random.choice([it.INGREDIENT_TYPE_FILLING, it.INGREDIENT_TYPE_SAUCE])
        ingr_price = float(GenerateData.generate_num())
        ingr_name = GenerateData.generate_string(7)
        ingr_whole = Ingredient(ingredient_type=ingr_type, name=ingr_name, price = ingr_price)
        assert \
            (ingr_whole.type == ingr_type) and \
            (ingr_whole.price == ingr_price) and \
            (ingr_whole.name == ingr_name)
    # да, здесь можно вынести создание сразу всех данных в отдельный метод, но для одного раза это нерационально


    @allure.title('Тестирование метода get_price()')
    @allure.description('Сравнение результатов работы метода и переменной price.')
    def test_get_price (self, ingredient_creation):
        ingr = ingredient_creation
        assert (ingr.get_price() == ingr.price)


    @allure.title('Тестирование метода get_name()')
    @allure.description('Сравнение результатов работы метода и переменной name')
    def test_get_name (self, ingredient_creation):
        ingr = ingredient_creation
        assert (ingr.get_name() == ingr.name)


    @allure.title('Тестирование метода get_type()')
    @allure.description('Сравнение результатов работы метода и переменной type')
    def test_get_type (self, ingredient_creation):
        ingr = ingredient_creation
        assert (ingr.get_type() == ingr.type)

 