import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    """
    Тестирование класса Ingredient (ингредиент для бургера).
    Проверяет корректность работы методов конструктора, get_price(),
    get_name() и get_type().
    """

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            (INGREDIENT_TYPE_SAUCE, Data.CHILI_SAUCE, Data.CHILI_SAUCE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
        ]
    )
    def test_constructor_should_set_correct_attributes(self, ingredient_type, ingredient_name, ingredient_price):
        """Проверяет корректность установки атрибутов при создании ингредиента."""
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    def test_get_price_should_return_correct_price_for_sauce(self):
        """Проверяет получение цены для соуса."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        assert ingredient.get_price() == Data.HOT_SAUCE_PRICE

    def test_get_name_should_return_correct_name_for_filling(self):
        """Проверяет получение названия для начинки."""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE)
        assert ingredient.get_name() == Data.DINOSAUR

    def test_get_type_should_return_correct_type_for_ingredient(self):
        """Проверяет получение типа ингредиента."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.CHILI_SAUCE, Data.CHILI_SAUCE_PRICE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE