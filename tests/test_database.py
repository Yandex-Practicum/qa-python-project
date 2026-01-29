from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns_success_return(self):
        data = Database()
        data_buns = data.available_buns()

        assert data_buns[0].get_name() == 'black bun' and data_buns[0].get_price() == 100

    def test_available_ingredients_success_return(self):
        data = Database()
        data_ingredients = data.available_ingredients()

        assert (
                data_ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE and
                data_ingredients[0].get_name() == 'hot sauce' and
                data_ingredients[0].get_price() == 100
        )
