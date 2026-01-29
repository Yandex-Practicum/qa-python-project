from praktikum.ingredient import Ingredient
import pytest

class TestIngredient:

    @pytest.mark.parametrize(
        "type, name, price",
        [
            ("bun", "black bun", 100),
            ("sauce", "sour cream", 200),
            ("filling", "sausage", 300),

        ]
    )
    def test_get_price(self, type, name, price):
        assert Ingredient(type, name, price).get_price() == price

    @pytest.mark.parametrize(
        "type, name, price",
        [
            ("bun", "black bun", 100),
            ("sauce", "sour cream", 200),
            ("filling", "sausage", 300),

        ]
    )
    def test_get_name(self, type, name, price):
        assert Ingredient(type, name, price).get_name() == name

    @pytest.mark.parametrize(
        "type, name, price",
        [
            ("bun", "black bun", 100),
            ("sauce", "sour cream", 200),
            ("filling", "sausage", 300),

        ]
    )
    def test_get_type(self, type, name, price):
        assert Ingredient(type, name, price).get_type() == type

