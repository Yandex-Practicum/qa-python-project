from data import BurgerData
from burger import Burger


class TestBurger:
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == BurgerData.BUN_NAME

    def test_add_ingredient(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) != 0

    def test_remove_ingredient(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0, 1)

        assert (burger.ingredients[0].name == BurgerData.SAUCE_NAME
                and burger.ingredients[1].name == BurgerData.FILLING_NAME)

    def test_get_price(self, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == BurgerData.BUN_PRICE * 2 + BurgerData.FILLING_PRICE

    def test_get_receipt(self, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()

        assert (len(receipt) > 0 and BurgerData.BUN_NAME in receipt
                and BurgerData.FILLING_NAME.lower() in receipt.lower())
