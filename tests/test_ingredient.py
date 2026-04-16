import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    #Тесты для класса Ingredient

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_get_name_returns_correct_name(self, ing_type, name, price):
        #Проверяем, что get_name возвращает правильное название ингредиента
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_get_price_returns_correct_price(self, ing_type, name, price):
        #Проверяем, что get_price возвращает правильную цену ингредиента
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_get_type_returns_correct_type(self, ing_type, name, price):
        #Проверяем, что get_type возвращает правильный тип ингредиента
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type