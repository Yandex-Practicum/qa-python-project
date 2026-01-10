from data.data import ORDER_DATA_CORRECT


class TestBurger:


    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert mock_bun.get_name() == burger.bun.get_name()


    def test_add_ingredient(self, burger, mock_ingredient0):
        burger.add_ingredient(mock_ingredient0)
        assert len(burger.ingredients) > 0 and isinstance(burger.ingredients, list)


    def test_remove_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert mock_ingredient1 not in burger.ingredients


    def test_move_ingredient(self, burger, mock_ingredient0, mock_ingredient1):
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient1 and len(burger.ingredients) == 2


    def test_get_price(self, burger, mock_bun, mock_ingredient0, mock_ingredient1):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        expected_price = ((ORDER_DATA_CORRECT[0]["bun_price"] * 2) + ORDER_DATA_CORRECT[0]["ingredient_price"] + ORDER_DATA_CORRECT[1]["ingredient_price"])
        total_price = burger.get_price()
        assert total_price == expected_price and isinstance(total_price, float)


    def test_get_receipt(self, burger, mock_bun, mock_ingredient0):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient0)
        receipt = burger.get_receipt()
        expected_receipt =  (f"(==== {mock_bun.get_name()} ====)"
                             f"\n= {str(mock_ingredient0.get_type()).lower()} {mock_ingredient0.get_name()} ="
                             f"\n(==== {mock_bun.get_name()} ====)\n"
                             f"\nPrice: {burger.get_price()}")
        assert receipt == expected_receipt

