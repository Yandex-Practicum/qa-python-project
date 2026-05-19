import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    # Тесты для класса Database
    
    def setup_method(self):
        # Создание экземпляра базы данных перед каждым тестом
        self.database = Database()
    
    def test_available_buns_returns_list_of_buns(self):
        # Проверка: метод available_buns возвращает список булок
        buns = self.database.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_buns_contains_three_buns(self):
        # Проверка: база данных содержит 3 булки
        buns = self.database.available_buns()
        assert len(buns) == 3
    
    def test_available_buns_returns_correct_bun_names(self):
        # Проверка: булки имеют правильные названия
        buns = self.database.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names
    
    def test_available_buns_returns_correct_bun_prices(self):
        # Проверка: булки имеют правильные цены
        buns = self.database.available_buns()
        bun_prices = [bun.get_price() for bun in buns]
        assert 100 in bun_prices
        assert 200 in bun_prices
        assert 300 in bun_prices
    
    def test_available_ingredients_returns_list_of_ingredients(self):
        # Проверка: метод available_ingredients возвращает список ингредиентов
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    
    def test_available_ingredients_contains_six_ingredients(self):
        # Проверка: база данных содержит 6 ингредиентов
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
    
    def test_available_ingredients_contains_correct_sauces(self):
        # Проверка: соусы имеют правильные названия
        ingredients = self.database.available_ingredients()
        sauce_names = [ing.get_name() for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert "hot sauce" in sauce_names
        assert "sour cream" in sauce_names
        assert "chili sauce" in sauce_names
    
    def test_available_ingredients_contains_correct_fillings(self):
        # Проверка: начинки имеют правильные названия
        ingredients = self.database.available_ingredients()
        filling_names = [ing.get_name() for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert "cutlet" in filling_names
        assert "dinosaur" in filling_names
        assert "sausage" in filling_names
    
    def test_available_ingredients_returns_correct_prices(self):
        # Проверка: ингредиенты имеют правильные цены
        ingredients = self.database.available_ingredients()
        prices = [ing.get_price() for ing in ingredients]
        assert 100 in prices
        assert 200 in prices
        assert 300 in prices
        