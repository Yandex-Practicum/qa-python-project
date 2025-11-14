from models.ingridient import Ingredient
from models.ingridient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from utils.constants import INGREDIENT_CUTLET, PRICE_INGREDIENT, SAUCE_KETCHUP, PRICE_SAUCE


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_ingredient_init(self):
        """Проверяем, что конструктор инициализирует поля type, name и price корректно"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_INGREDIENT)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient.get_name() == INGREDIENT_CUTLET
        assert ingredient.get_price() == PRICE_INGREDIENT

    def test_ingredient_get_price(self):
        """Проверяем, что метод get_price() возвращает ожидаемое значение"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, PRICE_SAUCE)
        assert ingredient.get_price() == PRICE_SAUCE

    def test_ingredient_get_name(self):
        """Проверяем, что метод get_name() возвращает ожидаемое значение"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_INGREDIENT)
        assert ingredient.get_name() == INGREDIENT_CUTLET

    def test_ingredient_get_type(self):
        """Проверяем, что метод get_type() возвращает ожидаемое значение"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, PRICE_SAUCE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
