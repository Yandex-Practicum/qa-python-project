import sys
sys.path.insert(0,"C:/Users/alekberovalf/PycharmProjects/Diplom_1/")
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from unittest.mock import Mock
class TestBurger:

    # Тест на добавление булочки

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Флюоресцентная булка R2-D3", 988.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Тест на добавление ингредиентов

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.type = "sauce"
        mock_ingredient.name = 'Соус с шипами Антарианского плоскоходца'
        mock_ingredient.price = 88.0
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Тест на удаление ингредиентов
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    # Тест на изменения порядка ингредиентов
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_2

    # Тест на получение цены бургера
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 1337.0
        mock_ingredient.get_price.return_value = 88.0
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 2762

    # Тест на получение состава бургера

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_bun.get_price.return_value = 988.0
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'sauce'
        mock_ingredient.get_name.return_value = 'Соус Spicy-X'
        mock_ingredient.get_price.return_value = 90.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_result = '\n'.join([
            '(==== Флюоресцентная булка R2-D3 ====)',
            '= sauce Соус Spicy-X =',
            '(==== Флюоресцентная булка R2-D3 ====)\n',
            'Price: 2066.0'
        ])
        result = burger.get_receipt()
        assert expected_result == result




