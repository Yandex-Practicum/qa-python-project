import pytest
from burger import Burger
from unittest.mock import Mock


class TestBurger:
# Тест на проверку, что булка корректно присваивается
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun is bun_mock
# Тест на проверку добавления ингридиентов
    def test_add_ingredient(self, multiple_mock_ingredients):
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = multiple_mock_ingredients
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        assert len(burger.ingredients) == 3
# Тест на проверку добавления ингридиентов
    def test_remove_ingredient_existant(self, multiple_mock_ingredients):
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = multiple_mock_ingredients
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 2 and burger.ingredients[0] is ingredient2
# Тест на проверку перемещения ингридиентов
    def test_move_ingredient_first_element_at_the_end(self, multiple_mock_ingredients):
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = multiple_mock_ingredients
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]
# Тест на проверку подсчета цены
    def test_get_price_bun(self, bun_mock, multiple_mock_ingredients):
        burger = Burger()
        burger.bun = bun_mock
        for ingredient in multiple_mock_ingredients:
            burger.add_ingredient(ingredient)
        expected_price = (bun_mock.get_price() * 2) + sum(
            ingredient.get_price() for ingredient in multiple_mock_ingredients)
        assert burger.get_price() == expected_price
# Тест на проверку вывода чека
    def test_get_receipt(self, bun_mock, multiple_mock_ingredients):
        burger = Burger()
        burger.bun = bun_mock
        ingredient1, ingredient2, ingredient3 = multiple_mock_ingredients
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.get_price = Mock(return_value=2515.0)
        expected_receipt = (
        '(==== Булка ====)\n'
        '= фирменный Соус =\n'
        '= отбивная Начинка =\n'
        '= котлета Начинка2 =\n'
        '(==== Булка ====)\n'
        '\nPrice: 2515.0')
        assert burger.get_receipt() == expected_receipt