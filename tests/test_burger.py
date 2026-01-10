from unittest.mock import Mock
from praktikum.burger import Burger
from data import TestData
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from data import EXPECTED_RECEIPTS

class TestBurger:
    def test_set_bun(self):     # тестирование метода выбора булки
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):      # тестирование метода добавления ингредиента
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[9][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[9][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):       # тестирование метода удаления ингредиента
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):     # тестирование метода перемещения ингредиента
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self):      # тестирование метода получения цены
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1][1]
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[1][2]
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self):      # тестирование метода получения чека
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[1][0]
        mock_bun.get_price.return_value = TestData.buns[1][1]
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = TestData.ingredients[9][2]
        mock_ingredient2.get_name.return_value = TestData.ingredients[9][1]
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        assert burger.get_receipt() == EXPECTED_RECEIPTS['complex_burger']