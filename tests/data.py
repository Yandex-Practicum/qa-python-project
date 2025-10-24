"""
Модуль с тестовыми данными для тестирования
"""
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Данные для тестирования Bun
class BunData:
    BLACK_BUN = {"name": "black bun", "price": 100.0}
    WHITE_BUN = {"name": "white bun", "price": 200.0}
    RED_BUN = {"name": "red bun", "price": 300.0}
    FREE_BUN = {"name": "free bun", "price": 0.0}
    SPECIAL_CHAR_BUN = {"name": "bun #1", "price": 150.0}
    PRECISE_BUN = {"name": "precise bun", "price": 99.99}


# Данные для тестирования Ingredient
class IngredientData:
    HOT_SAUCE = {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100.0}
    SOUR_CREAM = {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200.0}
    CHILI_SAUCE = {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300.0}
    CUTLET = {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100.0}
    DINOSAUR = {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200.0}
    SAUSAGE = {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300.0}
    MINIMAL_SAUCE = {"type": INGREDIENT_TYPE_SAUCE, "name": "minimal sauce", "price": 0.01}


# Данные для тестирования Database
class DatabaseData:
    EXPECTED_BUNS = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ]

    EXPECTED_INGREDIENTS = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]


# Данные для тестирования Burger
class BurgerData:
    TEST_BUN_NAME = "black bun"
    TEST_BUN_PRICE = 100.0
    TEST_SAUCE_NAME = "hot sauce"
    TEST_SAUCE_PRICE = 100.0
    TEST_SAUCE_TYPE = "SAUCE"
    TEST_FILLING_NAME = "cutlet"
    TEST_FILLING_PRICE = 100.0
    TEST_FILLING_TYPE = "FILLING"


# Константы для проверок
class ExpectedPrices:
    BURGER_WITH_INGREDIENTS = 400.0  # 100*2 + 100 + 100
    BURGER_WITH_BUN_ONLY = 200.0     # 100*2
    EMPTY_BURGER = 0


# Фабричные методы для создания мок-объектов
def get_mock_bun(bun_data=None):
    """Возвращает мок булочки"""
    if bun_data is None:
        bun_data = BunData.BLACK_BUN

    bun = Mock()
    bun.get_name.return_value = bun_data["name"]
    bun.get_price.return_value = bun_data["price"]
    return bun


def get_mock_ingredient(ingredient_data=None):
    """Возвращает мок ингредиента"""
    if ingredient_data is None:
        ingredient_data = IngredientData.HOT_SAUCE

    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_data["type"]
    ingredient.get_name.return_value = ingredient_data["name"]
    ingredient.get_price.return_value = ingredient_data["price"]
    return ingredient


def get_mock_ingredient_sauce():
    return get_mock_ingredient(IngredientData.HOT_SAUCE)


def get_mock_ingredient_filling():
    return get_mock_ingredient(IngredientData.CUTLET)


def get_mock_ingredient_cheese():
    return get_mock_ingredient(IngredientData.SOUR_CREAM)
