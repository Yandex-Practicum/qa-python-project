import allure
from praktikum.ingredient import Ingredient

@allure.feature('Ingredients')
class TestIngredient:

    @allure.title('Getting the name')
    def test_get_name_success(self):
        ingredient = Ingredient("SAUCE", "Ketchup", 50)
        assert ingredient.get_name() == "Ketchup"

    @allure.title('Getting the price')
    def test_get_price_success(self):
        ingredient = Ingredient("SAUCE", "Ketchup", 50)
        assert ingredient.get_price() == 50

    @allure.title('Getting the type')
    def test_get_type_success(self):
        ingredient = Ingredient("SAUCE", "Ketchup", 50)
        assert ingredient.get_type() == "SAUCE"
