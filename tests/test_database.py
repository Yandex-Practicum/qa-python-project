from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    def test_available_buns(self, create_base):
        buns = create_base.available_buns()
        assert len(buns) == 3
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_ingredients(self,create_base):
        ingredients = create_base.available_ingredients()
        assert len(ingredients) == 6
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)