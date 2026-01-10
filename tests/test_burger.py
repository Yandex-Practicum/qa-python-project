import pytest
from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient
from data import Data




def test_bun_name(burger):
    assert burger.bun.get_name() == Data.BUNS[0][0]

def test_bun_price(burger):
    assert burger.bun.get_price() == Data.BUNS[0][1]


@pytest.mark.parametrize("ingredient_type, ingredient_name, price", Data.INGREDIENTS)
def test_add_ingredient(burger, ingredient1, ingredient_type, ingredient_name, price):
    ingredient1.get_name.return_value = ingredient_name
    ingredient1.get_price.return_value = price
    ingredient1.get_type.return_value = ingredient_type  # Устанавливаем тип ингредиента
    # Добавляем ингредиент в бургер
    burger.add_ingredient(ingredient1)
    # Проверяем, что ингредиент добавлен
    assert len(burger.ingredients) == 1

@pytest.mark.parametrize("ingredient_type, ingredient_name, price", Data.INGREDIENTS)
def test_add_ingredient_name(burger, ingredient1, ingredient_type, ingredient_name, price):
    ingredient1.get_name.return_value = ingredient_name
    ingredient1.get_price.return_value = price
    ingredient1.get_type.return_value = ingredient_type  # Устанавливаем тип ингредиента
    # Добавляем ингредиент в бургер
    burger.add_ingredient(ingredient1)
    # Проверяем, что имя ингредиента правильно
    assert burger.ingredients[0].get_name() == ingredient_name

@pytest.mark.parametrize("ingredient_type, ingredient_name, price", Data.INGREDIENTS)
def test_add_ingredient_price(burger, ingredient1, ingredient_type, ingredient_name, price):
    ingredient1.get_name.return_value = ingredient_name
    ingredient1.get_price.return_value = price
    ingredient1.get_type.return_value = ingredient_type  # Устанавливаем тип ингредиента
    # Добавляем ингредиент в бургер
    burger.add_ingredient(ingredient1)
    # Проверяем, что цена ингредиента правильна
    assert burger.ingredients[0].get_price() == price

@pytest.mark.parametrize("ingredient_type, ingredient_name, price", Data.INGREDIENTS)
def test_add_ingredient_type(burger, ingredient1, ingredient_type, ingredient_name, price):
    ingredient1.get_name.return_value = ingredient_name
    ingredient1.get_price.return_value = price
    ingredient1.get_type.return_value = ingredient_type  # Устанавливаем тип ингредиента
    # Добавляем ингредиент в бургер
    burger.add_ingredient(ingredient1)
    assert burger.ingredients[0].get_type() == ingredient_type  # Проверяем тип ингредиента




def test_move_ingredient(burger, ingredient1, ingredient2):
    # Добавляем два ингредиента
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    # Перемещаем ингредиенты
    burger.move_ingredient(0, 1)
    # Проверяем, что ингредиенты перемещены
    assert burger.ingredients[0].get_name() == ingredient2.get_name() and burger.ingredients[1].get_name() == ingredient1.get_name()



def test_remove_ingredient(burger, ingredient2):
    # Добавляем ингредиент
    burger.add_ingredient(ingredient2)
    # Удаляем ингредиент
    burger.remove_ingredient(0)
    # Проверяем, что ингредиент удалён
    assert len(burger.ingredients) == 0



def test_get_price_with_ingredient(burger, ingredient2):
    # Добавляем ингредиент
    burger.add_ingredient(ingredient2)
    # Проверяем общую цену
    expected_price = Data.BUNS[0][1] * 2 + ingredient2.get_price()
    assert burger.get_price() == expected_price




def test_get_price_without_ingredient(burger):
    # Проверяем цену только с булочкой
    assert burger.get_price() == Data.BUNS[0][1] * 2




def test_get_receipt(burger, ingredient1, ingredient2):
    # Добавляем ингредиенты в бурге
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    # Получаем чек
    receipt = burger.get_receipt()
    # Ожидаемый результат
    expected_receipt = (
        f'(==== {Data.BUNS[0][0]} ====)\n'
        f'= {Data.INGREDIENTS[0][0].lower()} {Data.INGREDIENTS[0][1]} =\n'
        f'= {Data.INGREDIENTS[1][0].lower()} {Data.INGREDIENTS[1][1]} =\n'
        f'(==== {Data.BUNS[0][0]} ====)\n'

        f'Price: {burger.get_price()}'
    )

    # Проверяем, что полученный чек соответствует ожидаемому
    assert receipt == expected_receipt