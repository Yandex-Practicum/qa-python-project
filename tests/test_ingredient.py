import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        # Соусы
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        # Начинки
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
        # Граничные случаи
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "special", 999.99),
    ])
    def test_ingredient_creation_and_getters(self, ingredient_type, name, price):
        """
        Параметризованный тест для проверки создания ингредиента и работы геттеров.
        """
        ingredient = Ingredient(ingredient_type, name, price)
        
        # Проверяем все геттеры в одном тесте
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price