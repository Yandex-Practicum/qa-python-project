import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.test_data import INGREDIENTS_TEST_DATA

def test_burger_initialization():
    """Тестируем начальную инициализацию бургера."""
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []

def test_set_buns(db):
    """Тестируем установку булочек в бургер."""
    burger = Burger()
    bun = db.available_buns()[0]
    burger.set_buns(bun)
    assert burger.bun == bun

@pytest.mark.parametrize("ing_type, name, price", INGREDIENTS_TEST_DATA)
def test_add_ingredient(db, ing_type, name, price):
    """Тестируем добавление ингредиентов в бургер."""
    burger = Burger()
    ingredient = next((i for i in db.available_ingredients() if i.get_name() == name), None)
    burger.add_ingredient(ingredient)
    # Проверяем только количество и свойства добавленного ингредиента
    assert len(burger.ingredients) == 1
    added_ingredient = burger.ingredients[0]
    assert added_ingredient.get_name() == name
    assert added_ingredient.get_type() == ing_type
    assert added_ingredient.get_price() == price

def test_remove_ingredient(db):
    """Тестируем удаление ингредиентов из бургера."""
    burger = Burger()
    ingredient = db.available_ingredients()[0]
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    # Проверка, что ингредиент был удалён
    assert len(burger.ingredients) == 0

def test_move_ingredient(db):
    """Тестируем перемещение ингредиентов в бургере."""
    burger = Burger()
    ingredient1, ingredient2 = db.available_ingredients()[:2]
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    # Проверка правильности перемещения ингредиентов
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1

def test_get_price(db):
    """Тестируем расчет цены бургера."""
    burger = Burger()
    bun = db.available_buns()[0]
    burger.set_buns(bun)
    ingredients = db.available_ingredients()[:2]
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    # Учитываем, что булочка добавляется дважды в расчет цены
    expected_price = bun.get_price() * 2 + sum(ingredient.get_price() for ingredient in ingredients)

    # Проверка правильности расчёта цены
    assert burger.get_price() == expected_price

def test_get_receipt(db):
    """Тестируем получение чека бургера."""
    burger = Burger()
    bun = db.available_buns()[0]
    burger.set_buns(bun)
    ingredients = db.available_ingredients()[:2]
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    # Проверка корректности содержания чека
    assert f'(==== {bun.get_name()} ====)' in receipt
    for ingredient in ingredients:
        assert f'= {ingredient.get_type().lower()} {ingredient.get_name()} =' in receipt
    assert f'Price: {burger.get_price()}' in receipt
