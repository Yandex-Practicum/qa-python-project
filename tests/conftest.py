import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    """Фикстура: пустой бургер"""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура: мок-булочка"""
    bun = Bun("Флюоресцентная булка R2-D3", 100)
    return bun


@pytest.fixture
def mock_ingredients():
    """Фикстура: список мок-ингредиентов"""
    ingredients = [
        Ingredient("SAUCE", "Сырный соус", 50),
        Ingredient("FILLING", "Мясо бессмертных", 150),
        Ingredient("SAUCE", "Кисло-сладкий соус", 30),
        Ingredient("FILLING", "Хрустящие огурчики", 70)
    ]
    return ingredients


@pytest.fixture
def mock_sauce():
    """Фикстура: соус"""
    return Ingredient("SAUCE", "Горячий соус", 60)


@pytest.fixture
def mock_filling():
    """Фикстура: начинка"""
    return Ingredient("FILLING", "Котлета", 120)