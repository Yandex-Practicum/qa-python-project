import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    """
    Тесты для класса Ingredient.
    """

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["chili_sauce"]["name"], Data.ingredients["chili_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["hot_sauce"]["name"], Data.ingredients["hot_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["sour_cream"]["name"], Data.ingredients["sour_cream"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["cutlet"]["name"], Data.ingredients["cutlet"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["dinosaur"]["name"], Data.ingredients["dinosaur"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["sausage"]["name"], Data.ingredients["sausage"]["price"])
    ])
    def test_init(self, ingredient_type, name, price):
        """
        Проверяет корректную инициализацию объекта Ingredient.
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type, (
            f"Тип ингредиента некорректен. Ожидалось: {ingredient_type}, "
            f"получено: {ingredient.type}"
        )
        assert ingredient.name == name, (
            f"Имя ингредиента некорректно. Ожидалось: {name}, "
            f"получено: {ingredient.name}"
        )
        assert ingredient.price == price, (
            f"Цена ингредиента некорректна. Ожидалось: {price}, "
            f"получено: {ingredient.price}"
        )

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["chili_sauce"]["name"], Data.ingredients["chili_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["hot_sauce"]["name"], Data.ingredients["hot_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["sour_cream"]["name"], Data.ingredients["sour_cream"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["cutlet"]["name"], Data.ingredients["cutlet"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["dinosaur"]["name"], Data.ingredients["dinosaur"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["sausage"]["name"], Data.ingredients["sausage"]["price"])
    ])
    def test_get_price(self, ingredient_type, name, price):
        """
        Проверяет метод get_price().
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, (
            f"Метод get_price() вернул некорректную цену. Ожидалось: {price}, "
            f"получено: {ingredient.get_price()}"
        )

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["chili_sauce"]["name"], Data.ingredients["chili_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["hot_sauce"]["name"], Data.ingredients["hot_sauce"]["price"]),
        (INGREDIENT_TYPE_SAUCE, Data.ingredients["sour_cream"]["name"], Data.ingredients["sour_cream"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["cutlet"]["name"], Data.ingredients["cutlet"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["dinosaur"]["name"], Data.ingredients["dinosaur"]["price"]),
        (INGREDIENT_TYPE_FILLING, Data.ingredients["sausage"]["name"], Data.ingredients["sausage"]["price"])
    ])
    def test_get_name(self, ingredient_type, name, price):
        """
        Проверяет метод get_name().
        """
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, (
            f"Метод get_name() вернул некорректное имя. Ожидалось: {name}, "
            f"получено: {ingredient.get_name()}"
        )

    def test_invalid_price(self):
        """
        Проверяет, что попытка создать ингредиент с отрицательной ценой вызывает исключение.
        """
        with pytest.raises(ValueError, match="Цена ингредиента должна быть положительной"):
            Ingredient(INGREDIENT_TYPE_SAUCE, "Invalid Sauce", -50)

    def test_invalid_type(self):
        """
        Проверяет, что попытка создать ингредиент с некорректным типом вызывает исключение.
        """
        with pytest.raises(ValueError, match="Некорректный тип ингредиента"):
            Ingredient("INVALID_TYPE", "Some Name", 100)
