import pytest
import allure


from ingredient import Ingredient
from data import SAUCE_TYPE, SAUCE_NAME,SAUCE_PRICE


class TestIngredient:
    @allure.title("Testing Ingredient constructorgit stat")
    def test_ingredient_init(self):
        ingredient = Ingredient(SAUCE_TYPE, SAUCE_NAME,SAUCE_PRICE)
        assert (ingredient.type == SAUCE_TYPE and
               ingredient.name == SAUCE_NAME and
               ingredient.price == SAUCE_PRICE)