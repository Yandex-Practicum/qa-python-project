from typing import List
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.bun import Bun

class TestDatabase:

    # проверка получения списка булок
    def test_available_buns(self):
        list_buns: List[Bun] = [] # присваиваем переменной пустой список
        test_database = Database() # создаем экземпляр database
        list_buns = test_database.available_buns() #получаем список булок
        assert len(list_buns) > 0  # проверяем, что список булок непустой

    # проверка получения списка ингредиентов
    def test_available_ingredients(self):
        ingredients: List[Ingredient] = [] # присваиваем переменной пустой список
        test_database = Database() # создаем экземпляр database
        list_ingredients = test_database.available_ingredients() #получаем список ингредиентов
        assert len(list_ingredients) > 0 # проверяем, что список ингредиентов непустой
