class TestBurger:

    def test_set_buns(self, burger, mock_bun):
            burger.set_buns(mock_bun)
            assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_sauce):
            burger.add_ingredient(mock_sauce)
            assert mock_sauce in burger.ingredients

    def test_remove_ingredient(self, full_burger):
            initial_count = len(full_burger.ingredients)
            full_burger.remove_ingredient(0)
            assert len(full_burger.ingredients) == initial_count - 1

    def test_move_ingredient(self, full_burger):
            first_ingredient = full_burger.ingredients[0]
            second_ingredient = full_burger.ingredients[1]
            full_burger.move_ingredient(0, 1)
            assert full_burger.ingredients == [second_ingredient, first_ingredient]

    def test_get_price(self, full_burger, mock_bun, mock_sauce, mock_filling):
            expected_price = (mock_bun.get_price() * 2 +
                            mock_sauce.get_price() +
                            mock_filling.get_price())
            assert full_burger.get_price() == expected_price

    def test_get_receipt(self, full_burger):
            expected_receipt = ('(==== white bun ====)\n'
                              '= sauce sour cream =\n'
                              '= filling dinosaur =\n'
                              '(==== white bun ====)\n'
                              '\n'
                              'Price: 800')
            assert full_burger.get_receipt() == expected_receipt