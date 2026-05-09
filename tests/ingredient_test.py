import pytest
from ingredient import Ingredient  # уточните импорт

class TestIngredient:

    @pytest.mark.parametrize("ing_type, name, price", [
        ("sauce", "Томатный соус", 30),
        ("cheese", "Сыр чеддер", 50),
        ("meat", "Говядина", 80)
    ])
    def test_ingredient_creation(self, ing_type, name, price):
        ing = Ingredient(ing_type, name, price)
        assert ing.get_type() == ing_type
        assert ing.get_name() == name
        assert ing.get_price() == price

    def test_get_type(self):
        ing = Ingredient("sauce", "Кетчуп", 20)
        assert ing.get_type() == "sauce"

    def test_get_name(self):
        ing = Ingredient("cheese", "Пармезан", 70)
        assert ing.get_name() == "Пармезан"

    def test_get_price(self):
        ing = Ingredient("meat", "Бекон", 90)
        assert ing.get_price() == 90