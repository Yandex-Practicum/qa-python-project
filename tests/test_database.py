import pytest


class TestDatabase:
    def test_initial_buns_count(self, db):
        assert len(db.buns) == 3

    def test_initial_ingredients_count(self, db):
        assert len(db.ingredients) == 6

    @pytest.mark.parametrize("index,expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun")
    ])
    def test_bun_names(self, db, index, expected_name):
        assert db.available_buns()[index].get_name() == expected_name

    @pytest.mark.parametrize("index,expected_price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_bun_prices(self, db, index, expected_price):
        assert db.available_buns()[index].get_price() == expected_price

    @pytest.mark.parametrize("index,expected_type", [
        (0, "SAUCE"),
        (3, "FILLING")
    ])
    def test_ingredient_types(self, db, index, expected_type):
        assert db.available_ingredients()[index].get_type() == expected_type

    @pytest.mark.parametrize("index,expected_name", [
        (0, "hot sauce"),
        (3, "cutlet")
    ])
    def test_ingredient_names(self, db, index, expected_name):
        assert db.available_ingredients()[index].get_name() == expected_name

    @pytest.mark.parametrize("index,expected_price", [
        (0, 100),
        (3, 100)
    ])
    def test_ingredient_prices(self, db, index, expected_price):
        assert db.available_ingredients()[index].get_price() == expected_price