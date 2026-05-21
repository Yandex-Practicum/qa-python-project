import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database


class TestBurger:

    # Тест на установку булочек
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Testbun', 300.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Тест на добавление ингридиента  
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Testbun'
        mock_ingredient.get_price.return_value = 300.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_name() == 'Testbun'
        assert burger.ingredients[0].get_price() == 300.0
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    # Тест на удаление ингридиента
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Тест на перемещение слоя с ингридиентом
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    # Тест на получение цены бургера
    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[2])
        assert burger.get_price() == 600.0
