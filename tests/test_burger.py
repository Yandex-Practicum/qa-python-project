class TestBurger:

    def test_set_buns_one_bun_bun_set(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_one_ingredient_ingredient_added(self, burger, mock_ingredients_sauce):
        burger.add_ingredient(mock_ingredients_sauce)
        assert mock_ingredients_sauce in burger.ingredients

    def test_remove_ingredient_two_ingredient_one_ingredient_removed(self, burger, mock_ingredients_sauce, mock_ingredients_filling):
        burger.add_ingredient(mock_ingredients_sauce)
        burger.add_ingredient(mock_ingredients_filling)
        burger.remove_ingredient(0)
        assert mock_ingredients_sauce not in burger.ingredients

    def test_move_ingredient_two_ingredient_ingredient_moved(self, burger, mock_ingredients_sauce, mock_ingredients_filling):
        burger.add_ingredient(mock_ingredients_sauce)
        burger.add_ingredient(mock_ingredients_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredients_filling, mock_ingredients_sauce]

    def test_get_price_one_complete_burger_price_received(self, burger, mock_bun, mock_ingredients_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients_filling)
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredients_filling.get_price()

    def test_get_receipt_one_complete_burger_receipt_received(self, burger, mock_bun, mock_ingredients_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients_filling)
        price = mock_bun.get_price() * 2 + mock_ingredients_filling.get_price()
        assert burger.get_receipt() == f"(==== {mock_bun.get_name()} ====)\n= {mock_ingredients_filling.get_type().lower()} {mock_ingredients_filling.get_name()} =\n(==== {mock_bun.get_name()} ====)\n\nPrice: {price}"
