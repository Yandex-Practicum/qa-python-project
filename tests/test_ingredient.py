import pytest
import allure
from praktikum.ingredient import Ingredient
from helpers.generate_price import generate_float_price
from helpers.create_objects import create_ingredient

@allure.story('Проверка класса Ingredient')
class TestIngredient:
    @allure.title('Проверка создания объекта Ingredient')
    @allure.description('Создаётся объект с переменными self.type, self.ingredients, self.price и соотв. значениями')
    @pytest.mark.parametrize('type, name, price', [('any_type', 'any_name', generate_float_price())])
    def test_creation_object_ingredient(self, type, name, price):
        new_ingredient = Ingredient(type, name, price)

        assert new_ingredient.type == type and new_ingredient.name == name and new_ingredient.price == price

    @allure.title('Проверка метода get_price')
    @allure.description('Метод get_get_price() возвращает self.price')
    def test_get_price(self):
        new_ingredient = create_ingredient()

        assert new_ingredient.get_price() == new_ingredient.price

    @allure.title('Проверка метода get_name')
    @allure.description('Метод get_name() возвращает self.name')
    def test_get_name(self):
        new_ingredient = create_ingredient()

        assert new_ingredient.get_name() == new_ingredient.name

    @allure.title('Проверка метода get_type')
    @allure.description('Метод get_type() возвращает self.type')
    def test_get_type(self):
        new_ingredient = create_ingredient()

        assert new_ingredient.get_type() == new_ingredient.type
