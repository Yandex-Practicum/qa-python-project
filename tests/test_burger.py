import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns(self, mocker):
        """Тест: установка булочки"""
        mock_bun = mocker.Mock()
        mock_bun.get_name.return_value = "Краторная булка N-200i"
        mock_bun.get_price.return_value = 1255.0
        
        burger = Burger()
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mocker):
        """Тест: добавление ингредиента"""
        mock_ingredient = mocker.Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mocker):
        """Тест: удаление ингредиента по индексу"""
        mock_ingredient = mocker.Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mocker):
        """Тест: перемещение ингредиента"""
        mock_ing_1 = mocker.Mock()
        mock_ing_1.get_name.return_value = "Соус 1"
        mock_ing_2 = mocker.Mock()
        mock_ing_2.get_name.return_value = "Соус 2"
        
        burger = Burger()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ing_2
        assert burger.ingredients[1] == mock_ing_1

    def test_get_price(self, mocker):
        """Тест: расчет цены бургера (цена булочки * 2 + ингредиенты)"""
        mock_bun = mocker.Mock()
        mock_bun.get_price.return_value = 100.0
        
        mock_ing_1 = mocker.Mock()
        mock_ing_1.get_price.return_value = 50.0
        
        mock_ing_2 = mocker.Mock()
        mock_ing_2.get_price.return_value = 30.0
        
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        # 100 * 2 + 50 + 30 = 280.0
        assert burger.get_price() == 280.0

    def test_get_receipt(self, mocker):
        """Тест: формирование чека"""
        mock_bun = mocker.Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 100.0
        
        mock_ing = mocker.Mock()
        mock_ing.get_name.return_value = "Соус"
        mock_ing.get_price.return_value = 50.0
        mock_ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)
        
        receipt = burger.get_receipt()
        
        assert "(==== Булка ====)\n" in receipt
        assert "= sauce Соус =\n" in receipt
        assert "Price: 250.0" in receipt