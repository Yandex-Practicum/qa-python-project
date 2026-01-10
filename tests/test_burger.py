import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    """Создаем экземпляр бургера с тестовой булочкой."""
    test_bun = Bun("Тестовая булочка", 100)
    burger = Burger()
    burger.set_buns(test_bun)
    return burger


@pytest.fixture
def filling():
    """Создаем тестовую начинку."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "Ингредиент 1", 200)


@pytest.fixture
def sauce():
    """Создаем тестовый соус."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Соус 1", 50)


def test_add_ingredient(burger, filling):
    """Проверяем, что начинка добавляется корректно."""
    burger.add_ingredient(filling)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0].get_name() == "Ингредиент 1"


def test_remove_ingredient(burger, filling):
    """Проверяем, что начинка удаляется корректно."""
    burger.add_ingredient(filling)
    burger.remove_ingredient(0)  # Удаляем ингредиент по индексу 0
    assert len(burger.ingredients) == 0


def test_move_ingredient(burger, filling, sauce):
    """Проверяем, что ингредиент можно переместить."""
    burger.add_ingredient(filling)
    burger.add_ingredient(sauce)

    burger.move_ingredient(0, 1)  # Перемещаем "Ингредиент 1" на позицию "Соус 1"

    assert burger.ingredients[0].get_name() == "Соус 1"
    assert burger.ingredients[1].get_name() == "Ингредиент 1"


def test_get_price(burger, filling):
    """Проверяем общую цену с булочкой и начинкой."""
    burger.add_ingredient(filling)
    assert burger.get_price() == 400  # 100 (булочка) * 2 + 200 (начинка)
