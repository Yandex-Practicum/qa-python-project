import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database
class TestBurger:
    """ Тест на установку булок """
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Type_bun', 100.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    """ Тест на добавление ингредиента """
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Type_bun'
        mock_ingredient.get_price.return_value = 8.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 8.0
        assert burger.ingredients[0].get_name() == 'Type_bun'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING


    """ Тест на перемещение ингредиента """
    def test_move_ingredient(self):
        burger = Burger()
        
        # Создаем mock-ингредиенты
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()
        
        # Добавляем ингредиенты в бургер
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        # Проверяем начальный порядок
        assert burger.ingredients == [ingredient1, ingredient2, ingredient3]
        
        # Перемещаем ингредиент с индексом 0 на позицию 2
        burger.move_ingredient(0, 2)
        
        # Проверяем новый порядок
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    """ Тест на удаление ингредиента """
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    """ Тест на получение цены бургера"""
    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        assert burger.get_price() == 400.0

    """ Тест на получение чека """
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= filling cutlet =\n"\
                           "(==== black bun ====)\n\n"\
                           "Price: 400"
        assert expected_receipt == burger.get_receipt()