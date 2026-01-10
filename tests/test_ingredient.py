from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
import allure


class TestIngredient:

    @allure.title('Создание ингредиента с типом, именем и ценой')
    def test_create_ingredient_actual_type_name_and_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.type == Data.INGREDIENT_TYPE and ingredient.name == Data.INGREDIENT_NAME and ingredient.price == Data.INGREDIENT_PRICE

    @allure.title('Получение цены ингредиента через метод get_price')
    def test_get_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_price() == Data.INGREDIENT_PRICE

    @allure.title('Получение имени ингредиента через метод get_name')
    def test_get_name_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_name() == Data.INGREDIENT_NAME

    @allure.title('Получение типа соуса через метод get_type')
    def test_get_sauce_type_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        result_type = 'SAUCE'

        assert ingredient.get_type() == result_type

    @allure.title('Получение типа начинки через метод get_type')
    def test_get_filling_type_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        result_type = 'FILLING'

        assert ingredient.get_type() == result_type