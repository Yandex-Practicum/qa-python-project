from mocks.mocks import Mocks
from praktikum.burger import Burger


class TestBurger:

    def test_burger_initialization_price(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        assert 200 == burger.get_price()

    def test_burger_initialization_name(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        assert 'black bun' in burger.get_receipt()

    def test_burger_add_ingredient_name(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient_filling)
        print(type(burger.get_receipt()))
        assert 'cutlet' in burger.get_receipt()

    def test_burger_add_ingredient_price(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient_filling)
        assert 300 == burger.get_price()

    def test_burger_remove_ingredient(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert 'cutlet' is not burger.get_receipt()

    def test_burger_get_receipt(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient_souce)
        burger.add_ingredient(Mocks.mock_ingredient_filling)
        right_receipt = []
        right_receipt.append('(==== black bun ====)')
        right_receipt.append('= sauce hot sauce =')
        right_receipt.append('= filling cutlet =')
        right_receipt.append('(==== black bun ====)\n')
        right_receipt.append('Price: 400')
        right_string = '\n'.join(right_receipt)
        assert right_string == burger.get_receipt()

    def test_burger_move_ingredient(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient_souce)
        burger.add_ingredient(Mocks.mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        right_receipt_moved = []
        right_receipt_moved.append('(==== black bun ====)')
        right_receipt_moved.append('= filling cutlet =')
        right_receipt_moved.append('= sauce hot sauce =')
        right_receipt_moved.append('(==== black bun ====)\n')
        right_receipt_moved.append('Price: 400')
        right_string = '\n'.join(right_receipt_moved)
        assert right_string == burger.get_receipt()
