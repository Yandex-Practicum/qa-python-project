import pytest

from unittest.mock import Mock


class MockBun:
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Марсианская булочка'
    mock_bun.get_price.return_value = 1000


class MockIngredientSauce:
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_name.return_value = 'Соус XX'
    mock_ingredient_sauce.get_price.return_value = 50
    mock_ingredient_sauce.get_type.return_value = 'SAUCE'


class MockIngredientFilling:
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_name.return_value = 'Котлетка До-до'
    mock_ingredient_filling.get_price.return_value = 3000
    mock_ingredient_filling.get_type.return_value = 'FILLING'


class TestBurger:

    def test_burger_set_buns(self, burger):
        assert burger.get_price() == 2000

    @pytest.mark.parametrize('ingredient, total_price',
                             [[MockIngredientSauce.mock_ingredient_sauce,2050],
                              [MockIngredientFilling.mock_ingredient_filling, 5000]])
    def test_burger_add_ingredient(self, burger, ingredient, total_price):
        burger.add_ingredient(ingredient)
        assert burger.get_price() == total_price

    def test_burger_remove_ingredient(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.get_price() == 2000

    def test_burger_move_ingredient(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        burger.add_ingredient(MockIngredientSauce.mock_ingredient_sauce)
        burger.move_ingredient(0, 1)
        assert burger.get_price() == 5050
        assert burger.ingredients[0].get_name() == 'Соус XX'
        assert burger.ingredients[1].get_name() == 'Котлетка До-до'

    def test_burger_get_receipt(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        receipt = burger.get_receipt()
        assert '(==== Марсианская булочка ====)' in receipt
        assert receipt.count('(==== Марсианская булочка ====)') == 2
        assert '= filling Котлетка До-до =' in receipt
        assert 'Price: 5000' in receipt
        