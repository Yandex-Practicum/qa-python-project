import allure
from unittest.mock import Mock
import pytest
from burger import Burger


@allure.feature("Burger Class Tests")
class TestBurger:

    @allure.title("Test Setting Buns")
    @allure.step("Setting a bun for the Burger and verifying it")
    def test_set_buns(self, sesame_bun):
        burger = Burger()
        burger.set_buns(sesame_bun)

        assert burger.bun == sesame_bun

    @allure.title("Test Adding Ingredient")
    @allure.step("Adding an ingredient to the Burger and verifying it")
    def test_add_ingredient(self, lettuce_ingredient):
        burger = Burger()
        burger.add_ingredient(lettuce_ingredient)

        assert lettuce_ingredient in burger.ingredients

    @allure.title("Test Removing Ingredient")
    @allure.step("Removing an ingredient from the Burger and verifying it is removed")
    def test_remove_ingredient(self, lettuce_ingredient):
        burger = Burger()
        burger.add_ingredient(lettuce_ingredient)
        burger.remove_ingredient(0)

        assert lettuce_ingredient not in burger.ingredients

    @allure.title("Test Moving Ingredient")
    @allure.step("Moving ingredients within the Burger and verifying the order")
    def test_move_ingredient(self, lettuce_ingredient, tomato_ingredient):
        burger = Burger()
        burger.add_ingredient(lettuce_ingredient)
        burger.add_ingredient(tomato_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [tomato_ingredient, lettuce_ingredient]

    @allure.title("Test Burger Price Calculation with Mocked Bun and Ingredients")
    @pytest.mark.parametrize("bun_price, ingredient_price, expected_total", [
        (100.0, 20.0, 100.0 * 2 + 20.0),
        (50.0, 10.0, 50.0 * 2 + 10.0),
        (75.0, 15.0, 75.0 * 2 + 15.0)
    ])
    @allure.step("Creating a Burger with mock bun and ingredients, and verifying total price")
    def test_get_price(self, bun_price, ingredient_price, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        total_price = burger.get_price()

        assert total_price == expected_total

    @allure.title("Test Receipt Generation")
    @allure.step("Generating a receipt for Burger and verifying output format")
    def test_get_receipt(self, sesame_bun, lettuce_ingredient):
        burger = Burger()
        burger.set_buns(sesame_bun)
        burger.add_ingredient(lettuce_ingredient)
        receipt = burger.get_receipt()

        assert "(==== Sesame Bun ====)" in receipt
        assert "= filling Lettuce =" in receipt
        assert "Price: 110.0" in receipt
