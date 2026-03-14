import pytest
from praktikum.database import Database
from conftest import database
from conftest import expected_ingredients
import allure


@allure.feature('Database Operations')
class TestDatabase:

    @allure.title('Check that available_buns() returns a list')
    def test_available_buns_returns_list(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list), f"Expected list, but got {type(buns)}"

    @allure.title('Check that there are exactly 3 buns in the database')
    def test_len_list_buns_is_three(self, database):
        buns = database.available_buns()
        assert len(buns) == 3, f"Expected 3 buns, but found {len(buns)}"

    @allure.title('Verify bun data at index: {index}')
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_buns_content(self, database, index):
        bun = database.available_buns()[index]
        expected_bun = Database().available_buns()[index]
        assert (bun.name, bun.price) == (expected_bun.name, expected_bun.price), f"Bun at index {index} does not match expected data"

    @allure.title('Verify ingredient data at index: {index}')
    @pytest.mark.parametrize('index', list(range(6)))
    def test_available_ingredients_content(self, database, expected_ingredients, index):
        ingredient = database.available_ingredients()[index]
        expected_content = expected_ingredients[index]
        assert (ingredient.type, ingredient.name, ingredient.price) == expected_content, f"Ingredient at index {index} does not match expected data"
