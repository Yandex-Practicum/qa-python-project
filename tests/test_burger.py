from praktikum.burger import Burger
import helper

class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert mock_sauce in burger.ingredients
        assert mock_filling in burger.ingredients
        assert len(burger.ingredients) == 2


    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.remove_ingredient(0)

        assert mock_sauce not in burger.ingredients
        assert mock_filling in burger.ingredients

    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce


    def test_get_price_burger(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = helper.calculate_burger_price([mock_sauce, mock_filling],mock_bun)
        assert burger.get_price() == expected_price


    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'
            f'= sauce {mock_sauce.get_name()} =\n'
            f'= filling {mock_filling.get_name()} =\n'
            f'(==== {mock_bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )

        assert burger.get_receipt() == expected_receipt