import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    """Тест-кейсы для класса Ingredient"""
    
    # 1. Тест создания ингредиента с валидными параметрами
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Сырный соус", 50),
        (INGREDIENT_TYPE_FILLING, "Говяжья котлета", 100)
    ])
    def test_ingredient_creation_when_valid_params_then_success(self, ingredient_type, name, price):
        """1. Можно создать ингредиент с валидными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
    
    # 2. Тест строкового представления ингредиента
    def test_str_when_ingredient_created_then_returns_name(self):
        """2. При создании ингредиента str() возвращает его название"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", 50)
        assert str(ingredient) == "Соус"
    
    # 3. Тест mock-ингредиента
    def test_mock_ingredient_when_created_then_returns_mock_values(self, mock_ingredient):
        """3. Mock-ингредиент возвращает заданные значения"""
        assert mock_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    
    # 4. Тест создания ингредиента с невалидным типом
    def test_create_ingredient_when_type_invalid_then_raises_exception(self):
        """4. При создании ингредиента с невалидным типом возникает исключение"""
        with pytest.raises(ValueError):
            Ingredient("UNKNOWN", "Соус", 50)
    
    # 5. Тест создания ингредиента с пустым названием
    def test_create_ingredient_when_name_empty_then_raises_exception(self):
        """5. При создании ингредиента с пустым названием возникает исключение"""
        with pytest.raises(ValueError):
            Ingredient(INGREDIENT_TYPE_SAUCE, "", 50)
    
    # 6. Тест создания ингредиента с отрицательной ценой
    def test_create_ingredient_when_price_negative_then_raises_exception(self):
        """6. При создании ингредиента с отрицательной ценой возникает исключение"""
        with pytest.raises(ValueError):
            Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", -10)