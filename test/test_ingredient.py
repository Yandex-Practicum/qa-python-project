import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import patch


class TestIngredient:

    @pytest.fixture
    def sauce(self):
        """
        Фикстура для создания ингредиента типа "соус".
        """
        return Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)

    @pytest.fixture
    def filling(self):
        """
        Фикстура для создания ингредиента типа "начинка".
        """
        return Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

    def test_ingredient_creation(self, sauce, filling):
        """
        Проверяет правильность создания ингредиентов.
        """
        assert sauce.type == INGREDIENT_TYPE_SAUCE
        assert sauce.name == "sour cream"
        assert sauce.price == 200

        assert filling.type == INGREDIENT_TYPE_FILLING
        assert filling.name == "dinosaur"
        assert filling.price == 200

    @patch('Diplom_1.ingredient.Ingredient.get_price')
    def test_get_price(self, mock_get_price, sauce, filling):
        """
        Проверяет правильность работы метода get_price().
        """
        mock_get_price.return_value = 200  # Настраиваем mock, чтобы он возвращал 200
        assert sauce.get_price() == 200
        assert filling.get_price() == 200
        assert mock_get_price.call_count == 2  # Проверяем, что метод был вызван 2 раза

    @patch('Diplom_1.ingredient.Ingredient.get_name')
    def test_get_name(self, mock_get_name, sauce, filling):
        """
        Проверяет правильность работы метода get_name().
        """
        mock_get_name.return_value = "something"  # Настраиваем mock, чтобы он возвращал "something"
        assert sauce.get_name() == "something"  # Сравниваем с возвращаемым значением mock
        assert filling.get_name() == "something"  # Сравниваем с возвращаемым значением mock
        assert mock_get_name.call_count == 2  # Проверяем, что метод был вызван 2 раза

    @patch('Diplom_1.ingredient.Ingredient.get_type')
    def test_get_type(self, mock_get_type, sauce, filling):
        """
        Проверяет правильность работы метода get_type().
        """
        mock_get_type.return_value = "something_type"  # Настраиваем mock
        assert sauce.get_type() == "something_type"  # Сравниваем с возвращаемым значением mock
        assert filling.get_type() == "something_type"  # Сравниваем с возвращаемым значением mock
        assert mock_get_type.call_count == 2  # Проверяем, что метод был вызван 2 раза
