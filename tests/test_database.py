from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestDatabase:
    def test_available_buns_returns_expected_buns(self):
        db = Database()

        buns = db.available_buns()

        assert len(buns) == 3
        assert all(isinstance(b, Bun) for b in buns)

        names = [b.get_name() for b in buns]
        prices = [b.get_price() for b in buns]

        assert names == ["black bun", "white bun", "red bun"]
        assert prices == [100, 200, 300]

    def test_available_ingredients_returns_expected_ingredients(self):
        db = Database()

        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(i, Ingredient) for i in ingredients)

        names = [i.get_name() for i in ingredients]
        types = [i.get_type() for i in ingredients]
        prices = [i.get_price() for i in ingredients]

        expected_names = [
            "hot sauce",
            "sour cream",
            "chili sauce",
            "cutlet",
            "dinosaur",
            "sausage",
        ]
        assert names == expected_names

        assert types[:3] == [INGREDIENT_TYPE_SAUCE] * 3
        assert types[3:] == [INGREDIENT_TYPE_FILLING] * 3

        assert prices == [100, 200, 300, 100, 200, 300]