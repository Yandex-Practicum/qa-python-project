import pytest
from unittest.mock import MagicMock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_data():
    """Фикстура для тестирования класса Bun без использования моков."""
    return [
        Bun(name="black bun", price=100),
        Bun(name="white bun", price=200),
        Bun(name="red bun", price=300)
    ]


@pytest.fixture
def db():
    """Фикстура для мокированного экземпляра базы данных."""
    mock_db = MagicMock(spec=Database)

    # Мокированные булочки
    mock_db.available_buns.return_value = [
        MagicMock(name="black bun", spec=Bun, get_name=MagicMock(return_value="black bun"),
                  get_price=MagicMock(return_value=100)),
        MagicMock(name="white bun", spec=Bun, get_name=MagicMock(return_value="white bun"),
                  get_price=MagicMock(return_value=200)),
        MagicMock(name="red bun", spec=Bun, get_name=MagicMock(return_value="red bun"),
                  get_price=MagicMock(return_value=300))
    ]

    # Мокированные ингредиенты с правильными типами
    mock_db.available_ingredients.return_value = [
        MagicMock(name="hot sauce", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE),
                  get_name=MagicMock(return_value="hot sauce"), get_price=MagicMock(return_value=100)),
        MagicMock(name="sour cream", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE),
                  get_name=MagicMock(return_value="sour cream"), get_price=MagicMock(return_value=200)),
        MagicMock(name="chili sauce", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE),
                  get_name=MagicMock(return_value="chili sauce"), get_price=MagicMock(return_value=300)),
        MagicMock(name="cutlet", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING),
                  get_name=MagicMock(return_value="cutlet"), get_price=MagicMock(return_value=100)),
        MagicMock(name="dinosaur", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING),
                  get_name=MagicMock(return_value="dinosaur"), get_price=MagicMock(return_value=200)),
        MagicMock(name="sausage", spec=Ingredient, get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING),
                  get_name=MagicMock(return_value="sausage"), get_price=MagicMock(return_value=300))
    ]

    return mock_db


@pytest.fixture
def burger():
    """Фикстура для мокированного экземпляра бургера."""
    mock_burger = MagicMock(spec=Burger)
    mock_burger.get_name.return_value = "Test Burger"
    mock_burger.get_price.return_value = 1500
    mock_burger.get_ingredients.return_value = ["black bun", "cutlet", "hot sauce"]
    return mock_burger


