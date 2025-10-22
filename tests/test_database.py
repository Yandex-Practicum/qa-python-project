from typing import List

from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_available_buns(self, database_module):
        db = database_module.Database()

        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3

        names = [b.get_name() for b in buns]
        prices = [b.get_price() for b in buns]
        assert names == ["black bun", "white bun", "red bun"]
        assert prices == [100, 200, 300]

    def test_database_available_ingredients(self, database_module):
        db = database_module.Database()

        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6

        names = [i.get_name() for i in ingredients]
        prices = [i.get_price() for i in ingredients]
        types = [i.get_type() for i in ingredients]

        assert names == [
            "hot sauce",
            "sour cream",
            "chili sauce",
            "cutlet",
            "dinosaur",
            "sausage",
        ]
        assert prices == [100, 200, 300, 100, 200, 300]
        assert types == [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
            INGREDIENT_TYPE_FILLING,
            INGREDIENT_TYPE_FILLING,
        ]
