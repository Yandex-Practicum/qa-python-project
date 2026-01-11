import allure
import pytest
from ya_praktikum.ingredient import Ingredient

class TestIngredient:
    @allure.title('Проверка инициализации ингредиента')
    @allure.description('Тест проверяет, что ингредиент инициализируется с правильными данными')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('Соус', 'Сырный', 100),
        ('Начинка', 'Повидло', 200),
    ])
    def test_init_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient.type, f'Ожидается тип: {ingredient.type}, получено: {ingredient.get_type()}'
        assert ingredient.get_name() == ingredient.name, f'Ожидается название: {ingredient.name}, получено: {ingredient.get_name()}'
        assert ingredient.get_price() == ingredient.price, f'Ожидается цена: {ingredient.price}, получено: {ingredient.get_price()}'
        print('\nТест пройден!')
        print(f'Ингредиент инициализировался с типом {ingredient.get_type()}')
        print(f'Ингредиент инициализировался с названием {ingredient.get_name()}')
        print(f'Ингредиент инициализировался с ценой {ingredient.get_price()}')

    @allure.title('Проверка получения типа ингредиента')
    @allure.description('Тест проверяет, что можно получить тип ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('Соус', 'Сырный', 100),
        ('Начинка', 'Повидло', 200),
    ])
    def test_type_change(self, create_ingredient, ingredient_type, name, price):
        ingredient = create_ingredient
        assert ingredient.get_type() == ingredient.type, f"Ожидается тип ингредиента: {ingredient.type}"
        print('\nТест пройден!')
        print(f'Ингредиент получен с типом {ingredient.get_type()}')

    @allure.title('Проверка получения названия ингредиента')
    @allure.description('Тест проверяет, что можно получить название ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('Соус', 'Сырный', 100),
        ('Начинка', 'Повидло', 200),
    ])
    def test_name_change(self, create_ingredient, ingredient_type, name, price):
        ingredient = create_ingredient
        assert ingredient.get_name() == ingredient.name, f"Ожидается название ингредиента: {ingredient.name}"
        print('\nТест пройден!')
        print(f'Ингредиент инициализировался с названием {ingredient.get_name()}')

    @allure.title('Проверка получения цены ингредиента')
    @allure.description('Тест проверяет, что можно получить цену ингредиента')
    @pytest.mark.parametrize('ingredient_type, name, price', [
        ('Соус', 'Сырный', 100),
        ('Начинка', 'Повидло', 200),
    ])
    def test_price_change(self, create_ingredient, ingredient_type, name, price):
        ingredient = create_ingredient
        assert ingredient.get_price() == ingredient.price, f"Ожидается цена ингредиента:  {ingredient.price}"
        print('\nТест пройден!')
        print(f'Ингредиент инициализировался с ценой {ingredient.get_price()}')


