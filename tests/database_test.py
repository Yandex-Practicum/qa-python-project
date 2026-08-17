import pytest
from praktikum.database import Database
from unittest.mock import Mock
from praktikum.burger import Burger


class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6

    @pytest.mark.parametrize("index, name, price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_parametrize(self, index, name, price):
        buns = self.database.available_buns()

        assert buns[index].get_name() == name
        assert buns[index].get_price() == price

    def test_available_buns_mock(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        mock_database = Mock()
        mock_database.available_buns.return_value = [mock_bun]

        burger = Burger()
        burger.database = mock_database
        buns = burger.database.available_buns()

        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
