import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_initialization_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.name == name

    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_initialization_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.type == type_

    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_initialization_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.price == price

    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_get_name(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_get_type(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_type() == type_

    @pytest.mark.parametrize("name, type_, price", [
        ("Шницель", "Начинка", 65.00),
        ("Чесночный", "Соус", 20.00),
        ("Бекон", "Начинка", 40.00)
    ])
    def test_ingredient_get_price(self, name, type_, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_price() == price





