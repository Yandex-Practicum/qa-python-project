# tests/test_burger.py
import pytest
from unittest.mock import Mock

# Подгоняем импорты под предполагаемую структуру проекта.
# Если в вашем репозитории Burger находится в burger.py в корне,
# используйте: from burger import Burger
from burger import Burger

# Вспомог: создаём фиктивные Bun и Ingredient с нужным интерфейсом
def make_mock_bun(name="Sesame Bun", price=3.0):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

def make_mock_ingredient(name="Lettuce", ing_type="Vegetable", price=1.2):
    ing = Mock()
    ing.get_name.return_value = name
    ing.get_type.return_value = ing_type
    ing.get_price.return_value = price
    return ing

@pytest.fixture
def burger():
    return Burger()

@pytest.mark.parametrize(
    "bun_price, expected_price",
    [
        (3.0, 6.0),   # без ингредиентов: цена бекона стандартная двойная булочка
        (2.5, 5.0),
    ],
)
def test_price_without_ingredients(bun_price, expected_price):
    b = make_mock_bun(price=bun_price)
    burg = Burger()
    burg.set_buns(b)
    assert burg.get_price() == expected_price

def test_set_bun_and_add_ingredients_and_price():
    burg = Burger()
    bun = make_mock_bun(name="Big Bun", price=2.5)
    ing1 = make_mock_ingredient(name="Cheese", ing_type="Cheese", price=1.0)
    ing2 = make_mock_ingredient(name="Lettuce", ing_type="Vegetable", price=0.5)

    burg.set_buns(bun)

    burg.add_ingredient(ing1)
    burg.add_ingredient(ing2)

    # Цена: bun*2 + ингредиенты
    expected_price = bun.get_price.return_value * 2 + ing1.get_price.return_value + ing2.get_price.return_value
    assert burg.get_price() == expected_price

def test_move_and_remove_ingredients_order():
    burg = Burger()
    ing_a = make_mock_ingredient(name="Patty", ing_type="Meat", price=2.0)
    ing_b = make_mock_ingredient(name="Tomato", ing_type="Vegetable", price=0.5)
    ing_c = make_mock_ingredient(name="Cheese", ing_type="Cheese", price=1.5)

    burg.add_ingredient(ing_a)
    burg.add_ingredient(ing_b)
    burg.add_ingredient(ing_c)

    # начальная последовательность: [A, B, C]
    burg.move_ingredient(0, 2)  # A -> позиция 2 -> [B, C, A]
    assert burg.ingredients[0] is ing_b
    assert burg.ingredients[1] is ing_c
    assert burg.ingredients[2] is ing_a

    burg.remove_ingredient(1)  # удалить C -> [B, A]
    assert burg.ingredients == [ing_b, ing_a]

def test_receipt_format_includes_bun_and_ingredients(burger=None):
    burg = Burger()
    bun = make_mock_bun(name="Sesame", price=1.5)
    ing1 = make_mock_ingredient(name="Tomato", ing_type="Vegetable", price=0.6)
    ing2 = make_mock_ingredient(name="Beef", ing_type="Meat", price=2.4)

    burg.set_buns(bun)
    burg.add_ingredient(ing1)
    burg.add_ingredient(ing2)

    receipt = burg.get_receipt()
    assert f"(==== {bun.get_name()} ====)" in receipt
    assert f"= {str(ing1.get_type()).lower()} {ing1.get_name()} =" in receipt
    assert f"= {str(ing2.get_type()).lower()} {ing2.get_name()} =" in receipt
    assert f"(==== {bun.get_name()} ====)" in receipt
    # Цена должна быть рассчитана корректно
    expected_price = bun.get_price.return_value * 2 + ing1.get_price.return_value + ing2.get_price.return_value
    assert f"Price: {expected_price}" in receipt