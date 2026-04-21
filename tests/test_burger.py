from praktikum.burger import Burger
from data import data
from unittest.mock import Mock
import pytest


class TestBurger:
    def test_create_burger_price_without_bun_raises_error(self):
        burger = Burger()

        with pytest.raises(AttributeError):
            burger.get_price()

    def test_create_burger_receipt_without_bun_raises_error(self):
        burger = Burger()

        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_set_buns_updates_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=data.bun_price)
        mock_bun.get_name = Mock(return_value=data.bun_name)

        burger.set_buns(mock_bun)

        expected_price = data.bun_price * 2
        assert burger.get_price() == expected_price

    def test_set_buns_adds_bun_name_to_receipt(self, burger):
        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=data.bun_price)
        mock_bun.get_name = Mock(return_value=data.bun_name)

        burger.set_buns(mock_bun)

        assert data.bun_name in burger.get_receipt()

    def test_add_ingredient_increases_price(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=data.bun_price)
        mock_bun.get_name = Mock(return_value=data.bun_name)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = data.bun_price * 2 + data.ingredient_price
        assert burger.get_price() == expected_price

    def test_add_ingredient_appears_in_receipt(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_name = Mock(return_value=data.ingredient_name)
        mock_ingredient.get_type = Mock(return_value=data.ingredient_type)
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_name = Mock(return_value=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert data.ingredient_name in burger.get_receipt()

    def test_remove_ingredient_decreases_price(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=data.bun_price)
        mock_bun.get_name = Mock(return_value=data.bun_name)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        price_before = burger.get_price()
        burger.remove_ingredient(0)
        price_after = burger.get_price()

        assert price_after < price_before

    def test_remove_ingredient_removes_from_receipt(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_name = Mock(return_value=data.ingredient_name)
        mock_ingredient.get_type = Mock(return_value=data.ingredient_type)
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_name = Mock(return_value=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        burger.remove_ingredient(0)

        assert data.ingredient_name not in burger.get_receipt()

    def test_move_ingredient_changes_order_in_receipt(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name = Mock(return_value="ingredient_first")
        mock_ingredient1.get_type = Mock(return_value=data.ingredient_type)
        mock_ingredient1.get_price = Mock(return_value=data.ingredient_price)

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name = Mock(return_value="ingredient_second")
        mock_ingredient2.get_type = Mock(return_value=data.ingredient_type)
        mock_ingredient2.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_name = Mock(return_value=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)

        receipt = burger.get_receipt()
        pos_first = receipt.find("ingredient_first")
        pos_second = receipt.find("ingredient_second")

        assert pos_second < pos_first

    def test_get_price_returns_correct_sum(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_price = Mock(return_value=data.bun_price)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = data.bun_price * 2 + data.ingredient_price
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_correct_format(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_name = Mock(return_value=data.ingredient_name)
        mock_ingredient.get_type = Mock(return_value=data.ingredient_type)
        mock_ingredient.get_price = Mock(return_value=data.ingredient_price)

        mock_bun = Mock()
        mock_bun.get_name = Mock(return_value=data.bun_name)
        mock_bun.get_price = Mock(return_value=data.bun_price)

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = data.bun_price * 2 + data.ingredient_price
        expected_receipt = f"(==== {data.bun_name} ====)\n= {data.ingredient_type.lower()} {data.ingredient_name} =\n(==== {data.bun_name} ====)\n\nPrice: {expected_price}"

        assert burger.get_receipt() == expected_receipt