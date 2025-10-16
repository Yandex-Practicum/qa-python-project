import allure

from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @allure.title('Тест на успешную проверку получения начинки')
    def test_get_type_filling_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                name=Data.filling_crispy_mineral_rings,
                                price=Data.filling_crispy_mineral_rings_price)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    @allure.title('Тест на успешную проверку получения соуса')
    def test_get_type_sauce_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE,
                                name=Data.sauce_spicy,
                                price=Data.sauce_spicy_price)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    @allure.title('Тест на успешную проверку получения цены начинки')
    def test_get_price_filling_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                name=Data.filling_beef_meteorite,
                                price=Data.filling_beef_meteorite_price)
        assert ingredient.get_price() == Data.filling_beef_meteorite_price

    @allure.title('Тест на успешную проверку получения цены соуса')
    def test_get_price_sauce_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE,
                                name=Data.sause_traditional_galaxy,
                                price=Data.sause_traditional_galaxy_price)
        assert ingredient.get_price() == Data.sause_traditional_galaxy_price

    @allure.title('Тест на успешную проверку получения названия начинки')
    def test_get_name_filling_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                                name=Data.filling_beef_meteorite,
                                price=Data.filling_beef_meteorite_price)
        assert ingredient.get_name() == Data.filling_beef_meteorite

    @allure.title('Тест на успешную проверку получения названия соуса')
    def test_get_name_sauce_successfully(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE,
                                name=Data.sauce_spicy,
                                price=Data.sauce_spicy_price)
        assert ingredient.get_name() == Data.sauce_spicy
