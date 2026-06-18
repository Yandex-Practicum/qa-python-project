import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    return Bun('Флюоресцентная булка R2-D3', 988)


@pytest.fixture
def ingredient_main():
    return Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)


@pytest.fixture
def ingredient_sauce():
    return Ingredient('Соус', 'Соус Spicy-X', 90)