
class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == mock_bun.get_name() and burger.bun.get_price() == mock_bun.get_price()

    def test_add_ingredient(self, burger, mock_bun, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].get_name() == mock_ingredient_filling.get_name()

    def test_remove_ingredient(self, burger, mock_bun, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == mock_ingredient_sauce.get_name() and burger.ingredients[1].get_name() == mock_ingredient_filling.get_name()

    def test_get_price(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient_filling.get_price() + mock_ingredient_sauce.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        receipt = burger.get_receipt()
        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'
            f'= filling {mock_ingredient_filling.get_name()} =\n'
            f'= sauce {mock_ingredient_sauce.get_name()} =\n'
            f'(==== {mock_bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )
        assert receipt == expected_receipt
