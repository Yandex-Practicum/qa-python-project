from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    # Тест 006 - Позитивный - Проверка добавления булочки для бургера
    def test_set_bun_for_burger(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun is not None, f'Булочка не добавлена!'

    # Тест 007 - Позитивный - Проверка добавление ингредиента для бургера
    def test_add_ingredient_for_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1, f'Ингредиент не добавлен!'

    # Тест 008 - Позитивный - Проверка удаления ингредиента бургера
    def test_remove_ingredient_of_burger(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0, f'Ингредиент не удален!'

    # Тест 009 - Позитивный - Проверка перемещения ингредиента бургера
    def test_move_ingredients_of_burger(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)

        assert (id(mock_ingredient_1) == id(burger.ingredients[1]) and
                id(mock_ingredient_2) == id(burger.ingredients[0])), f'Ингредиент не перемещен!'

    # Тест 010 - Позитивный - Проверка получения стоимости бургера
    def test_get_price_of_burger(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 10
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 1
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 2
        burger.add_ingredient(mock_ingredient_2)

        assert burger.get_price() == 23, f'Неверная стоимость бургера!'

    # Тест 011 - Позитивный - Проверка получения рецепта бургера
    def test_get_receipt_of_burger(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булочка Кукурузная'
        mock_bun.get_price.return_value = 10
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = 'SAUCE'
        mock_ingredient_1.get_name.return_value = 'Свит Чили'
        mock_ingredient_1.get_price.return_value = 1
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = 'FILLING'
        mock_ingredient_2.get_name.return_value = 'Котлетка'
        mock_ingredient_2.get_price.return_value = 2
        burger.add_ingredient(mock_ingredient_2)

        result = ('(==== Булочка Кукурузная ====)'
                  '\n= sauce Свит Чили ='
                  '\n= filling Котлетка ='
                  '\n(==== Булочка Кукурузная ====)'
                  '\n'
                  '\nPrice: 23')

        assert burger.get_receipt() == result, f'Неверный рецепт бургера!'
