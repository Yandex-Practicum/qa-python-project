from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self):
        """Проверяем, что set_buns устанавливает булку"""
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        """Проверяем, что add_ingredient добавляет ингредиент в список"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):
        """Проверяем, что remove_ingredient удаляет ингредиент по индексу"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self):
        """Проверяем, что move_ingredient перемещает ингредиент на новую позицию"""
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_1

    def test_get_price(self):
        """Проверяем, что get_price считает цену: булка*2 + ингредиенты"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        # цена = 100*2 + 200 = 400
        assert burger.get_price() == 400

    def test_get_price_without_ingredients(self):
        """Проверяем цену бургера только с булками (без ингредиентов)"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 150
        burger.set_buns(mock_bun)
        # цена = 150*2 = 300
        assert burger.get_price() == 300

    def test_get_receipt(self):
        """Проверяем, что get_receipt возвращает корректный чек"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = 'hot sauce'
        mock_ingredient.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert '(==== black bun ====' in receipt
        assert '= sauce hot sauce =' in receipt
        assert 'Price: 300' in receipt

    def test_get_receipt_with_filling(self):
        """Проверяем чек с ингредиентом типа начинка"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'white bun'
        mock_bun.get_price.return_value = 200
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert '(==== white bun ====' in receipt
        assert '= filling cutlet =' in receipt
        assert 'Price: 500' in receipt
