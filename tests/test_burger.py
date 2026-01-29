from data import Data
from praktikum.bun import Bun
from praktikum.burger import Burger
from unittest.mock import Mock

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


#Тестируем класс Бургеров
class TestClassBurger:
    # Тестируем установку булочек
    def test_set_buns_create_and_set_bun_get_bun(self):
        burger = Burger()
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun.get_name() == Data.BUN_NAME
        assert burger.bun.get_price() == Data.BUN_PRICE

    # Тестируем добавление ингредиентов с использованием моков
    def test_add_ingredient_add_two_mock_ingredient_successful_add(self):
        mock_ingredient1 = Mock()
        mock_ingredient1.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.name = Data.INGREDIENT_SPICE
        mock_ingredient1.price = Data.SPICE_PRICE
        mock_ingredient2 = Mock()
        mock_ingredient2.type = INGREDIENT_TYPE_FILLING
        mock_ingredient2.name = Data.INGREDIENT_METEORIT
        mock_ingredient2.price = Data.METEORIT_PRICE
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert burger.ingredients == [mock_ingredient1, mock_ingredient2]

    # Тестируем удаление ингредиента с использованием мока
    def test_remove_ingredient_add_mock_ingredient_successful_remove(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    # Тестируем перемещение ингредиентов
    def test_move_ingredient_add_two_mock_ingredient_successful_move(self):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    # Тестируем получение цены бургера
    def test_get_price_bun_and_ingredient_price_correct_calculate_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 800
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 300
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        # 800 * 2 + 300 == 1900
        assert burger.get_price() == 1900

    # Тестируем получение чека c использованием database
    def test_get_receipt_create_burger_on_database_correct_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_result = '(==== black bun ====)\n'\
                          '= sauce hot sauce =\n'\
                          '= filling cutlet =\n'\
                          '(==== black bun ====)\n\n'\
                          'Price: 400'
        assert expected_result == burger.get_receipt()








