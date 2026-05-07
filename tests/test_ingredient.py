import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000),
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80),
        (INGREDIENT_TYPE_FILLING, "Биокотлета из марсианской Магнолии", 424)
    ])
    def test_ingredient_initialization_with_different_values(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        
        actual_type = ingredient.get_type()
        actual_name = ingredient.get_name()
        actual_price = ingredient.get_price()
        
        assert actual_type == ingredient_type
        assert actual_name == name
        assert actual_price == price
    
    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)
        actual_price = ingredient.get_price()
        assert actual_price == 15
    
    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)
        actual_name = ingredient.get_name()
        assert actual_name == "Мясо бессмертных моллюсков Protostomia"
    
    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)
        actual_type = ingredient.get_type()
        assert actual_type == INGREDIENT_TYPE_SAUCE
    
    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING
    ])
    def test_ingredient_with_different_types(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Тестовый ингредиент", 100)
        actual_type = ingredient.get_type()
        assert actual_type == ingredient_type
    
    @pytest.mark.parametrize("price", [0, 100, 999.99])
    def test_ingredient_with_different_prices(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый соус", price)
        actual_price = ingredient.get_price()
        assert actual_price == price