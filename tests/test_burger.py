import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

# фикстура для создания тестового бургера
@pytest.fixture
def sample_burger():
    burger = Burger()
    burger.set_buns(Bun("Вкусная булочка", 49.90))
    burger.add_ingredient(Ingredient("соус", "чили", 15.50))
    burger.add_ingredient(Ingredient("начинка", "говядина", 99.90))
    return burger


def test_set_buns(sample_burger):
    """Тест установки булочек"""
    assert sample_burger.bun.get_name() == "Вкусная булочка"
    assert sample_burger.bun.get_price() == 49.90


def test_add_ingredient(sample_burger):
    """Тест добавления ингредиента"""
    assert len(sample_burger.ingredients) == 2
    assert sample_burger.ingredients[0].get_name() == "чили"
    assert sample_burger.ingredients[1].get_name() == "говядина"


def test_remove_ingredient(sample_burger):
    """Тест удаления ингредиента"""
    sample_burger.remove_ingredient(0)
    assert len(sample_burger.ingredients) == 1
    assert sample_burger.ingredients[0].get_name() == "говядина"


def test_move_ingredient(sample_burger):
    """Тест перемещения ингредиента"""
    sample_burger.move_ingredient(0, 1)
    assert sample_burger.ingredients[0].get_name() == "говядина"
    assert sample_burger.ingredients[1].get_name() == "чили"


def test_get_price(sample_burger):
    """Тест расчета цены бургера"""
    # 2 булочки по 100 + кетчуп 50 + сыр 80 = 330
    assert sample_burger.get_price() == 215.20


def test_get_price_with_mock():
    """Тест расчета цены с использованием моков"""
    # Создаем моки
    mock_bun = Mock()
    mock_bun.get_price.return_value = 50.0

    mock_ingredient1 = Mock()
    mock_ingredient1.get_price.return_value = 30.0
    mock_ingredient2 = Mock()
    mock_ingredient2.get_price.return_value = 70.0

    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)

    # 2 булочки по 50 + ингредиенты 30 + 70 = 200
    assert burger.get_price() == 200.0
    mock_bun.get_price.assert_called()
    mock_ingredient1.get_price.assert_called()
    mock_ingredient2.get_price.assert_called()


def test_get_receipt(sample_burger):
    """Тест формирования чека"""
    receipt = sample_burger.get_receipt()
    assert "(==== Вкусная булочка ====)" in receipt
    assert "= соус чили =" in receipt
    assert "= начинка говядина =" in receipt
    assert "Price: 215.2" in receipt

