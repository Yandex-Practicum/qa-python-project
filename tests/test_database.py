from source_code.bun import Bun
from source_code.ingredient import Ingredient


class TestDatabase:


    def test_available_buns(self, dbase):
        buns = dbase.available_buns()
        assert (isinstance(buns, list)
                and all(isinstance(bun, Bun) for bun in buns)
                and len(buns) == 3)


    def test_available_ingredients(self, dbase):
        ingredients = dbase.available_ingredients()
        assert (isinstance(ingredients, list)
                and all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
                and len(ingredients) == 6)
