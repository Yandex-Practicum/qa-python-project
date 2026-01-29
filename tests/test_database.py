import allure
from bun import Bun
from ingredient import Ingredient


@allure.feature("Database Class Tests")
class TestDatabase:

    @allure.title("Test Available Buns Retrieval")
    @allure.step("Retrieving available buns from Database and verifying type and count")
    def test_available_buns(self, db):
        buns = db.available_buns()

        assert len(buns) > 0
        assert isinstance(buns[0], Bun)

    @allure.title("Test Available Ingredients Retrieval")
    @allure.step("Retrieving available ingredients from Database and verifying type and count")
    def test_available_ingredients(self, db):
        ingredients = db.available_ingredients()

        assert len(ingredients) > 0
        assert isinstance(ingredients[0], Ingredient)
