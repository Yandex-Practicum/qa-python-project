import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:
    @pytest.mark.parametrize("expected_names, expected_prices", [
        (["black bun", "white bun", "red bun"], [100, 200, 300]),
    ])
    def test_available_buns(self, expected_names, expected_prices):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

        names = sorted([bun.get_name() for bun in buns])
        prices = sorted([bun.get_price() for bun in buns])

        assert names == sorted(expected_names)
        assert prices == sorted(expected_prices)

    @pytest.mark.parametrize("expected_names, expected_prices", [
        (
            ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"],
            [100, 200, 300, 100, 200, 300]
        ),
    ])
    def test_available_ingredients(self, expected_names, expected_prices):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

        names = sorted([i.get_name() for i in ingredients])
        prices = sorted([i.get_price() for i in ingredients])
        types = [i.get_type() for i in ingredients]

        assert names == sorted(expected_names)
        assert prices == sorted(expected_prices)
        assert INGREDIENT_TYPE_SAUCE in types
        assert INGREDIENT_TYPE_FILLING in types
