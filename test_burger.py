from unittest.mock import Mock
from burger import Burger

def test_set_buns():
    burger = Burger()
    mock_bun = Mock()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock()
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

def test_remove_ingredient():
    burger = Burger()
    mock_ingredient = Mock()
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert mock_ingredient not in burger.ingredients

def test_move_ingredient():
    burger = Burger()
    mock_ing1 = Mock()
    mock_ing2 = Mock()
    burger.add_ingredient(mock_ing1)
    burger.add_ingredient(mock_ing2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == mock_ing1

def test_get_price_with_buns():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    burger.set_buns(mock_bun)
    assert burger.get_price() == 200
