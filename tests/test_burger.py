from data import DataBurger


class TestBurger:
    def test_move_ingredient_burger_mock_bun_mock_sauce_mock_filling_moved(self, burger, mock_bun, mock_sauce,
                                                                           mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == mock_sauce

    def test_remove_ingredient_burger_mock_bun_mock_sauce_mock_filling_removed(self, burger, mock_bun,
                                                                               mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_get_price_burger_mock_bun_mock_sauce_received(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        expected_results = 2 * mock_bun.get_price() + mock_sauce.get_price()

        assert burger.get_price() == expected_results

    def test_get_receipt_burger_mock_bun_mock_sauce_received(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        assert DataBurger.RECEIPT == burger.get_receipt()


