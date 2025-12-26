import pytest
from praktikum.ingredient import Ingredient


# класс TestIngredient содержит в себе набор тестов, которыми покрываем класс Ingredient
class TestIngredient:

    #1 тест на проверку что корректно инициализируется type ингредиента
    def test_ingredient_init_type_initialization_is_correct(self):
        ingredient = Ingredient('sauce', 'spicy sauce', 55 )
        assert ingredient.type == 'sauce'

    #2 тест на проверку что корректно инициализируется name ингредиента
    def test_ingredient_init_name_initialization_is_successful(self):
        ingredient = Ingredient('filling', 'meat filling', 109.99)
        assert ingredient.name == 'meat filling'

    #3 тест на проверку что корректно инициализируется price ингредиента
    def test_ingredient_init_price_initialization_is_successful(self):
        ingredient = Ingredient('filling', 'cheese filling', 99.99)
        assert ingredient.price == 99.99

    #4 тест на проверку что корректно работает метод get_price ингредиента
    @pytest.mark.parametrize('price', [109.99, 99.99, 75])
    def test_ingredient_get_price_is_successful(self, price):
        ingredient = Ingredient('sause', 'spicy sause', price)
        assert ingredient.get_price() == price

    #5 тест на проверку что корректно работает метод get_name ингредиента
    @pytest.mark.parametrize('name', ['spicy sause', 'cheese sause', 'sweet and sour sause'])
    def test_ingredient_get_name_is_successful(self, name):
        ingredient = Ingredient('sause', name, 125.99)
        assert ingredient.get_name() == name

    #6 тест на проверку что корректно работает метод get_type ингредиента
    @pytest.mark.parametrize('ingredient_type', ['sause', 'filling', ''])
    def test_ingredient_get_type_is_successful(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'burgers', 105.99)
        assert ingredient.get_type() == ingredient_type
