import data


class TestDatabase:

    def test_getting_available_buns(self, database):
        actual_list = [(bun.name, bun.price) for bun in database.available_buns()]
        assert actual_list == data.AVAILABLE_BUNS

    def test_getting_available_ingredients(self, database):
        actual_list = [(ingredient.name, ingredient.price) for ingredient in database.available_ingredients()]
        assert actual_list == data.AVAILABLE_INGREDIENTS
