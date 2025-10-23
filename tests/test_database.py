import pytest

from praktikum.database import Database


class TestDatabase:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ],
    )
    def test_available_buns_and_price(self, name, price):
        buns = Database().available_buns()
        assert any(bun.name == name and bun.price == price for bun in buns), f"Булочка с именем '{name}' и ценой {price} не найдена в базе"

    @pytest.mark.parametrize(
        "name, price",
        [
            ("hot sauce", 100),
            ("sour cream", 200),
            ("chili sauce", 300),
            ("cutlet", 100),
            ("dinosaur", 200),
            ("sausage", 300),
        ],
    )
    def test_available_ingredients_and_price(self, name, price):
        ingredients = Database().available_ingredients()
        assert any(ingredient.name == name and ingredient.price == price for ingredient in ingredients), f"Ингредиент с именем '{name}' и ценой {price} не найден в базе"