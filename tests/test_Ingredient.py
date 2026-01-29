import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

@pytest.fixture
def sample_ingredient():
    # Фикстура для создания экземпляра Ingredient с типом "SAUCE", именем "test sauce" и ценой 30.0
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 30.0)

def test_ingredient_initialization(sample_ingredient):
    # Проверка инициализации Ingredient: тип должен быть "SAUCE", имя - "test sauce", цена - 30.0
    assert sample_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    assert sample_ingredient.get_name() == "test sauce"
    assert sample_ingredient.get_price() == 30.0

def test_ingredient_type(sample_ingredient):
    # Проверка метода get_type(): он должен возвращать "SAUCE"
    assert sample_ingredient.get_type() == INGREDIENT_TYPE_SAUCE

def test_ingredient_name(sample_ingredient):
    # Проверка метода get_name(): он должен возвращать "test sauce"
    assert sample_ingredient.get_name() == "test sauce"

def test_ingredient_price(sample_ingredient):
    # Проверка метода get_price(): он должен возвращать 30.0
    assert sample_ingredient.get_price() == 30.0