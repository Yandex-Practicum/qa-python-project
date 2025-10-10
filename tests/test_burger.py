import pytest

from practicum.burger import Burger
from data import TestData

class TestBurger:

    def test_set_buns_correct_bun_sets(self, bun_data):
        """Проверка установки булочки"""
        burger = Burger()
        burger.set_buns(bun_data)
        assert burger.bun == bun_data

    @pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", TestData.ingredients)
    def test_add_ingredient_increases_quantity(self, burger_with_bun, mock_ingredient,
                                               ingredient_type, ingredient_name, ingredient_price):
        """Проверка добавления ингредиентов в булочку – количество увеличивается на 1 позицию"""
        initial_count = len(burger_with_bun.ingredients)
        burger_with_bun.add_ingredient(mock_ingredient(ingredient_type, ingredient_name, ingredient_price))
        assert len(burger_with_bun.ingredients) == initial_count + 1

    def test_remove_ingredient_decreases_quantity(self, burger_with_bun, mock_ingredient):
        """Проверка удаления ингредиентов из булочки – количество уменьшается на 1 позицию"""
        burger_with_bun.add_ingredient(mock_ingredient("Соус", "Лунный кетчунез", 100))
        initial_count = len(burger_with_bun.ingredients)
        burger_with_bun.remove_ingredient(0)
        assert len(burger_with_bun.ingredients) == initial_count - 1

    def test_move_ingredient_changes_order(self, burger_with_bun, mock_ingredient):
        """Проверка перемещения ингредиентов в булочке –
                        сравнение позиций ингредиентов до и после перемещения"""
        test_ingredient1 = mock_ingredient("Соус", "Квантово-сырный", 50)
        test_ingredient2 = mock_ingredient("Начинка", "Лапидарный осьминог", 1500)
        burger_with_bun.add_ingredient(test_ingredient1)
        burger_with_bun.add_ingredient(test_ingredient2)
        original_order = burger_with_bun.ingredients[0]
        burger_with_bun.move_ingredient(0, 1)
        assert burger_with_bun.ingredients[1] == original_order

    def test_get_price_returns_correct_calculation(self, bun_data, mock_ingredient):
        """Проверка корректного расчета цены бургера"""
        burger = Burger()
        burger.set_buns(bun_data)
        burger.add_ingredient(mock_ingredient("Соус", "Юпитеровый", 100))
        expected_price = bun_data.get_price() * 2 + 100
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", TestData.ingredients)
    def test_get_receipt_returns_correct_format(self, burger_with_bun, mock_ingredient,
                                                ingredient_type, ingredient_name, ingredient_price):
        """Проверка корректного формата чека: отображаются все добавленные ингредиенты"""
        burger_with_bun.add_ingredient(mock_ingredient(ingredient_type, ingredient_name, ingredient_price))
        expected_receipt = [
            f'(==== {burger_with_bun.bun.get_name()} ====)',
            f'= {ingredient_type.lower()} {burger_with_bun.ingredients[0].get_name()} =',
            f'(==== {burger_with_bun.bun.get_name()} ====)',
            '',
            f'Price: {burger_with_bun.get_price()}'
        ]
        assert burger_with_bun.get_receipt() == '\n'.join(expected_receipt)
