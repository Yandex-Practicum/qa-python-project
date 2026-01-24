# tests/test_burger.py
from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = "mock ingredient"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


# тест проверяет создание бургера, расчет его цены и что булочка действительно установлена
def test_burger_creation_and_price(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == 250  # 2 булочки + 1 ингредиент
    assert burger.bun.get_name() == "mock bun"  # Проверка установленной булочки


# тест проверяет, что булочка устанавливается, цена считается правильно и что
# при установке булочки количество ингредиентов не изменилось
def test_burger_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)

    assert burger.bun.get_name() == "mock bun"
    assert burger.get_price() == 200  # Цена булки * 2
    assert len(burger.ingredients) == 0  # Проверяем, что ингредиенты не добавлены


# тест проверяет добавление ингредиента в бургер, их цену и что ингредиент действительно добавлен
def test_burger_add_ingredient(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)

    burger.add_ingredient(mock_ingredient)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0].get_name() == "mock ingredient"  # Проверка добавленного ингредиента
    assert burger.get_price() == 250  # 2 булочки + 1 ингредиент


# тест проверяет функциональность получения чека
def test_burger_get_receipt(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    receipt = burger.get_receipt()
    assert "(==== mock bun ====)" in receipt
    assert "= filling mock ingredient =" in receipt
    assert "Price: 250" in receipt  # 2 булочки + цена ингредиента

# тест проверяет что указанный ингредиент из списка ингредиентов бургера корректно удаляются
def test_burger_remove_ingredient(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)

    ingredient2 = Mock()
    ingredient2.get_name.return_value = "another ingredient"
    ingredient2.get_price.return_value = 50
    ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(ingredient2)

    assert len(burger.ingredients) == 2  # Должно быть 2 ингредиента
    burger.remove_ingredient(0)  # Удаляем первый ингредиент
    assert len(burger.ingredients) == 1  # Должно остаться 1 ингредиент
    assert burger.ingredients[0].get_name() == "another ingredient"  # Проверяем, что остался нужный ингредиент


# тест проверяет что ингредиент бургера можно переместить
def test_burger_move_ingredient(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)

    ingredient2 = Mock()
    ingredient2.get_name.return_value = "another ingredient"
    ingredient2.get_price.return_value = 50
    ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger.add_ingredient(mock_ingredient)
    burger.add_ingredient(ingredient2)

    assert burger.ingredients[0].get_name() == "mock ingredient"  # Первый ингредиент
    burger.move_ingredient(0, 1)  # Перемещаем mock ingredient на вторую позицию
    assert burger.ingredients[1].get_name() == "mock ingredient"  # Проверяем, что mock ingredient теперь на второй позиции