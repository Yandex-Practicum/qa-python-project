import pytest
from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тесты set_buns.
# - test_set_buns_sets_bun: проверяет базовый сценарий первого вызова метода.
# - test_set_buns_uses_latest_bun: проверяет сценарий повторного вызова метода(обновление состояния)

def test_set_buns_sets_bun(burger):
    bun = Mock()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_set_buns_uses_latest_bun(burger):
    bun1 = Mock()
    bun2 = Mock()
    burger.set_buns(bun1)
    burger.set_buns(bun2)
    assert burger.bun == bun2

# Тесты add_ingredient:
# - test_add_ingredient_adds_to_list: проверяет, что метод корректно добавляет ингредиент
# (независимо от его типа — соус или начинка) в список ингредиентов.
# - test_add_multiple_ingredients: проверяет, что метод поддерживает
# многократные вызовы подряд: каждый новый ингредиент добавляется в конец списка,
# при этом порядок ингредиентов сохраняется.


@pytest.mark.parametrize(
    "ingredient_type",
    [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
)
def test_add_ingredient_adds_to_list(burger, ingredient_type):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_add_multiple_ingredients(burger):
    ing1 = Mock()
    ing2 = Mock()
    ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing2.get_type.return_value = INGREDIENT_TYPE_FILLING

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert burger.ingredients == [ing1, ing2]

# Тесты remove_ingredient:
# - test_remove_ingredient_removes_correct_item: проверяет, что метод
# удаляет ингредиент по указанному индексу. После удаления список должен 'сжаться':
# элементы, стоявшие после удалённого, сдвигаются влево, а порядок оставшихся ингредиентов сохраняется.


def test_remove_ingredient_removes_correct_item(burger):
    ing1 = Mock()
    ing2 = Mock()
    ing3 = Mock()

    ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
    ing3.get_type.return_value = INGREDIENT_TYPE_SAUCE

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    burger.remove_ingredient(1)

    assert burger.ingredients == [ing1, ing3]

# Тесты move_ingredient:
# - test_move_ingredient_changes_order: проверяет, что метод корректно переставляет
# ингредиенты при разных комбинациях. После перемещения
# итоговый порядок ингредиентов должен соответствовать ожидаемому.

@pytest.mark.parametrize(
    "source,target,expected",
    [
        (0, 2, [1, 2, 0]),   # первый → в конец
        (2, 0, [2, 0, 1]),   # последний → в начало
    ]
)
def test_move_ingredient_changes_order(burger, source, target, expected):
    ingredients = [Mock(), Mock(), Mock()]
    for ing in ingredients:
        ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(ing)

    burger.move_ingredient(source, target)

    assert burger.ingredients == [ingredients[i] for i in expected]

# Тесты get_price:
# - test_get_price_sums_bun_and_ingredients: проверяет единое поведение метода get_price —
# корректный расчёт итоговой стоимости и обращение к методам зависимостей
# (булки и ингредиентов) для получения их цен.


def test_get_price_sums_bun_and_ingredients(burger):
    bun = Mock()
    bun.get_price.return_value = 100

    ing1 = Mock()
    ing2 = Mock()
    ing1.get_price.return_value = 30
    ing2.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert burger.get_price() == 100 * 2 + 30 + 50

    bun.get_price.assert_called()
    ing1.get_price.assert_called_once()
    ing2.get_price.assert_called_once()

# Тесты get_receipt:
# - test_get_receipt_format: проверяет формат возвращаемого текста —
# верхняя булка, строка ингредиента, нижняя булка, пустая строка-разделитель и строка с ценой.

def test_get_receipt_format(burger):
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ing = Mock()
    ing.get_name.return_value = "hot sauce"
    ing.get_price.return_value = 50
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE

    burger.set_buns(bun)
    burger.add_ingredient(ing)

    receipt = burger.get_receipt()
    lines = receipt.split("\n")

    assert lines[0] == "(==== black bun ====)"
    assert lines[1] == "= sauce hot sauce ="
    assert lines[2] == "(==== black bun ====)"
    assert lines[3] == ""                  # пустая строка
    assert lines[4].startswith("Price: ")  # цена начинается с Price

