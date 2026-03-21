import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    @pytest.fixture
    def database_instance(self):
        return Database()

    def test_database_initialization(self, database_instance):
        assert len(database_instance.buns) > 0
        assert len(database_instance.ingredients) > 0

    def test_available_buns_returns_list(self, database_instance):
        buns = database_instance.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3

        for bun in buns:
            assert isinstance(bun, Bun)

        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_ingredients_returns_list(self, database_instance):
        ingredients = database_instance.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6  

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

        first_ing = ingredients[0]
        from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
        assert first_ing.get_type() == INGREDIENT_TYPE_SAUCE
        assert first_ing.get_name() == "hot sauce"