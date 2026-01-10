from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from data import TestData

class TestBurger:
    # Тестирование метода выбора булки
    def test_set_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тестирование метода добавления ингредиента
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[3][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[3][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Тестирование метода удаления ингредиента
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # Тестирование метода перемещения ингредиента
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient

    # Тестирование метода получения цены
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1][1]
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[1][2]
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    # Тестирование метода получения чека
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[1][0] # Флюоресцентная булка R2-D3
        mock_bun.get_price.return_value = TestData.buns[1][1] # 988
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.ingredients[0][1] # Соус Spicy-X
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_price.return_value = TestData.ingredients[0][2] # 90
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = TestData.ingredients[3][2] # Соус с шипами Антарианского плоскоходца
        mock_ingredient2.get_name.return_value = TestData.ingredients[3][1] # 88
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        receipt_text = (
            '(==== Флюоресцентная булка R2-D3 ====)\n'
            '= filling Соус Spicy-X =\n'
            '= sauce Соус с шипами Антарианского плоскоходца =\n'
            '(==== Флюоресцентная булка R2-D3 ====)\n\n'
            'Price: 2154' # Булка 988 + ингредиент1 90 + ингредиент2 88 + булка 988 = 2154
        )
        assert burger.get_receipt() == receipt_text

