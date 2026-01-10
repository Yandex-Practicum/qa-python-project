from practikum.burger import Burger
from mock import get_mock_bun, get_mock_ingredient_filling, get_mock_ingredient_sauce
def test_set_buns():
    burger = Burger()
    bun = get_mock_bun()

    burger.set_buns(bun)
    assert burger.bun == bun

def test_add_single_ingredient():
    burger = Burger()
    ingredient = get_mock_ingredient_filling()

    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients
    assert len(burger.ingredients) == 1  # Проверяем, что ингредиент один

def test_add_multiple_ingredients():
    burger = Burger()
    ingredient1 = get_mock_ingredient_filling()
    ingredient2 = get_mock_ingredient_sauce()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    assert ingredient1 in burger.ingredients
    assert ingredient2 in burger.ingredients
    assert len(burger.ingredients) == 2  # Проверяем, что  два ингредиента
    assert burger.ingredients == [ingredient1, ingredient2]  # Проверяем порядок

def test_add_duplicate_ingredients():
    burger = Burger()
    ingredient1 = get_mock_ingredient_filling()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient1)  # Добавляем  ингредиент дважды

    assert burger.ingredients.count(ingredient1) == 2  # Проверяем, что ингредиент добавлен дважды
    assert len(burger.ingredients) == 2  # Проверяем количество ингредиентов

def test_remove_ingredient():
    burger = Burger()
    ingredient1 = get_mock_ingredient_filling()
    ingredient2 = get_mock_ingredient_sauce()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    burger.remove_ingredient(0)  # Удаляем первый ингредиент (ingredient1)
    assert ingredient1 not in burger.ingredients
    assert ingredient2 in burger.ingredients

def test_move_ingredient():
    burger = Burger()
    ingredient1 = get_mock_ingredient_filling()
    ingredient2 = get_mock_ingredient_sauce()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    burger.move_ingredient(0, 1)  # Перемещаем первый ингредиент на вторую позицию
    assert burger.ingredients == [ingredient2, ingredient1]

def test_get_price():
    burger = Burger()
    bun = get_mock_bun()
    ingredient1 = get_mock_ingredient_filling()
    ingredient2 = get_mock_ingredient_sauce()

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    # Стоимость: (400 * 2) + 200 + 50 = 550
    assert burger.get_price() == 1050

def test_get_receipt():
    burger = Burger()
    bun = get_mock_bun()
    ingredient1 = get_mock_ingredient_filling()
    ingredient2 = get_mock_ingredient_sauce()

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    receipt = burger.get_receipt()

    # Проверяем ключевые части чека
    assert "(==== blue bun ====)" in receipt
    assert "= filling dinosaur =" in receipt
    assert "= sauce sour cream =" in receipt
    assert "Price: 1050" in receipt


