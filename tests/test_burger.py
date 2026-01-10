import pytest
from unittest.mock import Mock
from diplom_1.praktikum.burger import Burger


class TestBurger:
    # Позитивные тесты
    def test_set_buns_sets_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_removes_from_list(self, burger_with_ingredients, mock_ingredient):
        burger = burger_with_ingredients
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_changes_position(self, mock_ingredient):
        burger = Burger()
        second_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, mock_ingredient]

    def test_get_price_calculates_correctly(self, burger_with_ingredients):
        assert burger_with_ingredients.get_price() == 250  # 100*2 + 50

    def test_get_receipt_returns_correct_format(self, burger_with_ingredients):
        receipt = burger_with_ingredients.get_receipt()
        assert '(==== Краторная булочка ====)\n= sauce Острый соус =\n(==== Краторная булочка ====)\n\nPrice: 250'

    # Негативные тесты
    def test_remove_ingredient_invalid_index_raises_exception(self, burger_with_ingredients):
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(5)

    def test_move_ingredient_invalid_index_raises_exception(self, burger_with_ingredients):
        with pytest.raises(IndexError):
            burger_with_ingredients.move_ingredient(5, 0)

    def test_get_price_without_bun_raises_exception(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_without_bun_raises_exception(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()