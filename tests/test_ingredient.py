import allure
import pytest

from ingredient import Ingredient
from data import BurgerInfo as b


class TestIngredient:
    """
    Тесты методов класса Ingredient.
    """

    @allure.title('Проверяем конструктор __init__() с пустым или незаданным типом ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['', None])
    def test_init_ingredient_type(self, ingredient_type):
        sauce = Ingredient(ingredient_type, b.SAUCE_NAME, b.SAUCE_PRICE)
        assert sauce.type == ingredient_type

    @allure.title('Проверяем конструктор __init__() с пустым или незаданным названием ингредиента')
    @pytest.mark.parametrize('name', ['', None])
    def test_init_ingredient_name(self, name):
        sauce = Ingredient(b.SAUCE_TYPE, name, b.SAUCE_PRICE)
        assert sauce.name == name

    @allure.title('Проверяем конструктор __init__() с нулевой или незаданной стоимостью ингредиента')
    @pytest.mark.parametrize('price', [0.0, None])
    def test_init_ingredient_price(self, price):
        sauce = Ingredient(b.SAUCE_TYPE, b.SAUCE_NAME, price)
        assert sauce.price == price

    @allure.title('Проверяем метод get_type() - получить тип ингредиента')
    def test_get_type(self):
        sauce = Ingredient(b.SAUCE_TYPE, b.SAUCE_NAME, b.SAUCE_PRICE)
        assert sauce.get_type() == b.SAUCE_TYPE

    @allure.title('Проверяем метод get_name() - получить название ингредиента')
    def test_get_name(self):
        sauce = Ingredient(b.SAUCE_TYPE, b.SAUCE_NAME, b.SAUCE_PRICE)
        assert sauce.get_name() == b.SAUCE_NAME

    @allure.title('Проверяем метод get_price() - получить стоимость ингредиента')
    def test_get_price(self):
        sauce = Ingredient(b.SAUCE_TYPE, b.SAUCE_NAME, b.SAUCE_PRICE)
        assert sauce.get_price() == b.SAUCE_PRICE

