import pytest
import allure
from Diplom_1.ingredient import Ingredient


class TestIngredient:
    @allure.title('Проверка создания объекта с правильными атрибутами')
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Начинки", "Мясо с рисом ", 199),
        ("Начинки", "Рис с Мясом", 249),
        ("Соусы", "Кетчуп", 300)
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
        assert ingredient.get_type() == ingredient_type

    @allure.title('Тест метода get_price')
    def test_get_price(self, ingredient_fixture):
        assert ingredient_fixture.get_price() == 300

    @allure.title('Тест метода get_name')
    def test_get_name(self, ingredient_fixture):
        assert ingredient_fixture.get_name() == "Биокотлета"

    @allure.title('Тест метода get_type')
    def test_get_type(self, ingredient_fixture):
        assert ingredient_fixture.get_type() == 'Начинки'

    @allure.title('Тест на изменеие имени')
    def test_set_name(self, ingredient_fixture):
        ingredient_fixture.name = "Космокартошка"
        assert ingredient_fixture.get_name() == "Космокартошка"

    @allure.title('Тест на изменеие прайса')
    def test_set_price(self, ingredient_fixture):
        ingredient_fixture.price = 400
        assert ingredient_fixture.get_price() == 400

    def test_set_type(self, ingredient_fixture):
        ingredient_fixture.type = "Соусы"
        assert ingredient_fixture.get_type() == "Соусы"


    @allure.title('Негативная Проверка на поле Имя: значение name не является строкой')
    @pytest.mark.parametrize("ingredient_type, invalid_name, price", [
        ("Начинки", None, 199),
        ("Начинки", 4, 249),
    ])
    def test_ingredient_creation_with_invalid_name(self, ingredient_type, invalid_name, price):
        ingredient = Ingredient(ingredient_type, invalid_name, price)
        assert not isinstance(ingredient.get_name(), (str))


    @allure.title('Негативная Проверка на поле Прайс: значение price не является числом')
    @pytest.mark.parametrize("ingredient_type, name, invalid_price", [
        ("Начинки", "Мясо с рисом", None),
        ("Начинки", "Рис", "no int"),
    ])
    def test_ingredient_creation_with_invalid_price(self, ingredient_type, name, invalid_price):
        ingredient = Ingredient(ingredient_type, name, invalid_price)
        assert not isinstance(ingredient.get_price(), (int, float))

    @allure.title('Негативная Проверка на поле Тип: значение typ не является строкой')
    @pytest.mark.parametrize("invalid_ingredient_type, name, price", [
        (3, "Мясо с рисом", 300),
        (None, "Рис", 199),
    ])
    def test_ingredient_creation_with_invalid_type(self, invalid_ingredient_type, name, price):
        ingredient = Ingredient(invalid_ingredient_type, name, price)
        assert not isinstance(ingredient.get_type(), (str))

    @allure.title('Негативная проверка поля Цена: отрицательные и не отрицательное числа')
    @pytest.mark.parametrize("price", [-10, 0, -55])
    def test_invalid_price(self, price):
        ingredient = Ingredient(ingredient_type="Соус", name="Мясо", price=price)
        assert ingredient.price == price
        assert ingredient.price <= 0

