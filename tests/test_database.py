import pytest
from unittest.mock import patch
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_returns_three_buns(self, database):
        """Проверяем, что база данных содержит 3 булочки"""
        buns = database.available_buns()
        assert len(buns) == 3
        
        # Проверяем названия булочек
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients_returns_six_ingredients(self, database):
        """Проверяем, что база данных содержит 6 ингредиентов"""
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        
        # Проверяем количество соусов и начинок
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(sauces) == 3
        assert len(fillings) == 3

    def test_available_methods_return_lists(self, database):
        """Проверяем, что методы возвращают списки"""
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        assert isinstance(buns, list)
        assert isinstance(ingredients, list)
        
                