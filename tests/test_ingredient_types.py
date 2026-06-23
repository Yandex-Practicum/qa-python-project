import allure

from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredientTypes:

    @allure.title("Проверяем, что константа соуса определена верно")
    def test_ingredient_type_sauce(self):

        assert INGREDIENT_TYPE_SAUCE == "SAUCE"

    @allure.title("Проверяем, что константа начинки определена верно")
    def test_ingredient_type_filling(self):

        assert INGREDIENT_TYPE_FILLING == "FILLING"