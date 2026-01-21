from data import Data
from call_mock import CallMock


class TestBurger:

    def test_set_buns(self, new_bun, new_burger):
        new_burger.set_buns(new_bun)
        assert new_burger.bun == new_bun

    def test_add_ingredient(self, new_burger):
        new_burger.add_ingredient(CallMock.mock_ingredient())
        new_burger.add_ingredient(CallMock.mock_ingredient_2())
        assert len(new_burger.ingredients) == 2
        assert new_burger.ingredients[0].get_name() == Data.INGREDIENT_NAME
        assert new_burger.ingredients[1].get_name() == Data.INGREDIENT_NAME_2

    def test_remove_ingredient(self, new_burger):
        new_burger.add_ingredient(CallMock.mock_ingredient())
        new_burger.remove_ingredient(0)
        assert new_burger.ingredients == []

    def test_move_ingredient(self, new_burger):
        new_burger.add_ingredient(CallMock.mock_ingredient())
        new_burger.add_ingredient(CallMock.mock_ingredient_2())
        new_burger.move_ingredient(0, 1)
        assert new_burger.ingredients[0].get_name() == Data.INGREDIENT_NAME_2

    def test_get_price(self, new_bun, new_burger):
        new_burger.set_buns(new_bun)
        new_burger.add_ingredient(CallMock.mock_ingredient())
        assert new_burger.get_price() == Data.BUN_PRICE*2 + Data.INGREDIENT_PRICE

    def test_get_receipt(self, new_bun, new_burger):
        new_burger.set_buns(new_bun)
        new_burger.add_ingredient(CallMock.mock_ingredient())
        receipt_list = [f'(==== {new_bun.get_name()} ====)',
                        f'= {str(CallMock.mock_ingredient().get_type()).lower()} {CallMock.mock_ingredient().get_name()} =',
                        f'(==== {new_bun.get_name()} ====)\n', f'Price: {new_burger.get_price()}']
        receipt_list = '\n'.join(receipt_list)
        assert new_burger.get_receipt() == receipt_list
