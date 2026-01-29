import allure
from ingredient import Ingredient


@allure.feature("Ingredient Class Tests")
class TestIngredient:

    @allure.title("Test Get Ingredient Price")
    @allure.step("Verifying price of Ingredient")
    def test_get_price(self):
        ingredient = Ingredient("FILLING", "Lettuce", 10.0)
        price = ingredient.get_price()

        assert price == 10.0

    @allure.title("Test Get Ingredient Name")
    @allure.step("Verifying name of Ingredient")
    def test_get_name(self):
        ingredient = Ingredient("FILLING", "Lettuce", 10.0)
        name = ingredient.get_name()

        assert name == "Lettuce"

    @allure.title("Test Get Ingredient Type")
    @allure.step("Verifying type of Ingredient")
    def test_get_type(self):
        ingredient = Ingredient("FILLING", "Lettuce", 10.0)
        ingredient_type = ingredient.get_type()

        assert ingredient_type == "FILLING"
