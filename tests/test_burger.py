from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import TestData

class TestBurger:
    def test_set_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[10][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[10][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1][1]
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[1][2]
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[1][0] # Флюоресцентная булка R2-D3
        mock_bun.get_price.return_value = TestData.buns[1][1] # цена = 988.0

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.ingredients[10][1] # Мясо бессмертных моллюсков
        mock_ingredient1.get_price.return_value = TestData.ingredients[10][2] # цена = 1337.0
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = TestData.ingredients[0][1] # Соус с шипами Антарианского плоскоходца
        mock_ingredient2.get_price.return_value = TestData.ingredients[0][2] # цена = 88.0
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        receipt_text = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= filling Мясо бессмертных моллюсков =\n'
            '= sauce Соус с шипами Антарианского плоскоходца =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n\n'
            'Price: 3401.0' # Булка 988.0 + ингредиент1 1337.0 + ингредиент2 88.0 + булка 988.0 = 3401.0
        )
        assert burger.get_receipt() == receipt_text
