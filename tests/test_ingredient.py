import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Тесты для класса Ingredient
    
    def test_ingredient_creation_returns_correct_type(self):
        # Проверка: создание ингредиента возвращает правильный тип
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    
    def test_ingredient_creation_returns_correct_name(self):
        # Проверка: создание ингредиента возвращает правильное название
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert ingredient.get_name() == "cutlet"
    
    def test_ingredient_creation_returns_correct_price(self):
        # Проверка: создание ингредиента возвращает правильную цену
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert ingredient.get_price() == 200
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_ingredient_creation_with_different_params(self, ingredient_type, name, price):
        # Параметризованный тест: создание ингредиентов с разными параметрами
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

