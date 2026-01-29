from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_mock_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_mock_2, ingredient_mock_1]

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = 'black bun'
        bun_mock.get_price.return_value = 100.00
        burger.set_buns(bun_mock)

        receipt = [
            '(==== black bun ====)',
            '(==== black bun ====)\n',
            'Price: 200.0'
        ]

        assert burger.get_receipt() == '\n'.join(receipt)

