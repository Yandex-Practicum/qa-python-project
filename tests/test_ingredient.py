import pytest

from data import INGREDIENTS_TEST_DATA
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_type_for_sauce(self, mock_ingredient_sauce):
        # Проверка метода get_type для соуса
        assert mock_ingredient_sauce.get_type() == "SAUCE"
        mock_ingredient_sauce.get_type.assert_called_once()

    def test_get_name_for_sauce(self, mock_ingredient_sauce):
        # Проверка метода get_name для соуса
        assert mock_ingredient_sauce.get_name() == "hot sauce"
        mock_ingredient_sauce.get_name.assert_called_once()

    def test_get_price_for_sauce(self, mock_ingredient_sauce):
        # Проверка метода get_price для соуса
        assert mock_ingredient_sauce.get_price() == 50
        mock_ingredient_sauce.get_price.assert_called_once()

    def test_get_type_for_filling(self, mock_ingredient_filling):
        # Проверка метода get_type для начинки
        assert mock_ingredient_filling.get_type() == "FILLING"
        mock_ingredient_filling.get_type.assert_called_once()

    def test_get_name_for_filling(self, mock_ingredient_filling):
        # Проверка метода get_name для начинки
        assert mock_ingredient_filling.get_name() == "cheese"
        mock_ingredient_filling.get_name.assert_called_once()

    def test_get_price_for_filling(self, mock_ingredient_filling):
        # Проверка метода get_price для начинки
        assert mock_ingredient_filling.get_price() == 30
        mock_ingredient_filling.get_price.assert_called_once()


    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_TEST_DATA)

    def test_real_ingredient_creation(self, ingredient_data):
        # Параметризованный тест для создания реальных ингредиентов с проверкой на тип данных
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_type() == ingredient_data["type"]
        assert ingredient.get_name() == ingredient_data["name"]
        assert ingredient.get_price() == ingredient_data["price"]
        assert isinstance(ingredient.get_price(), float)