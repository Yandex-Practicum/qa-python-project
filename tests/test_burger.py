from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        bun = mock_bun()
        burger.set_buns(bun)
        assert bun == burger.bun

    def test_add_ingredient_success(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        assert burger.ingredients == [sauce]

    def test_remove_ingredient_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        filling = mock_filling()
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [filling]

    def test_move_ingredient_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun())
        sauce = mock_sauce()
        burger.add_ingredient(sauce)
        filling = mock_filling()
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling, sauce]

    def test_get_price_success(self, mock_bun, mock_filling):
        burger = Burger()
        bun = mock_bun()
        filling = mock_filling()
        bun.get_price.return_value = 100.0
        filling.get_price.return_value = 200.0
        burger.set_buns(bun)
        burger.add_ingredient(filling)
        expected_price = bun.get_price.return_value * 2 + filling.get_price.return_value
        assert burger.get_price() == expected_price

    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        bun = mock_bun
        burger.set_buns(bun)
        sauce = mock_sauce
        burger.add_ingredient(sauce)
        filling = mock_filling
        burger.add_ingredient(filling)
        expected_receipt = (
            '(==== White bun ====)\n'
            '= sauce Chili sauce =\n'
            '= filling Dinosaur =\n'
            '(==== White bun ====)\n\n'
            'Price: 900.0'
        )
        assert burger.get_receipt() == expected_receipt
