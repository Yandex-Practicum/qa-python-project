from burger import Burger



class TestBurger:
    def setup_method(self):
        self.burger = Burger()

    def test_set_buns(self, mock_bun):
        self.burger.set_buns(mock_bun)
        assert self.burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient1):
        self.burger.add_ingredient(mock_ingredient1)
        assert self.burger.ingredients[0] == mock_ingredient1

    def test_remove_ingredient(self, mock_ingredient1, mock_ingredient2):
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients[0] == self.mock_ingredient2

    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)
        self.burger.move_ingredient(0, 1)
        assert (self.burger.ingredients[0] == mock_ingredient2) and (self.burger.ingredients[1] == mock_ingredient1)

    def test_get_price(self, mock_bun, mock_ingredient1, mock_ingredient2):
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        expected_price = (110 * 2) + 140 + 170
        assert self.burger.get_price() == expected_price

    def test_get_receipt(self, mock_ingredient2, mock_ingredient1, mock_bun):
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        expected_receipt = [
            '(==== green bun ====)',
            '= bbq SAUCE =',
            '= cheese FILLING =',
            '(==== green bun ====)',
            '',
            f'Price: {(110 * 2) + 140 + 170}'
        ]

        assert self.burger.get_receipt() == '\n'.join(expected_receipt)

    def test_empty_burger_price(self, mock_bun):
        self.burger.set_buns(mock_bun)
        assert self.burger.get_price() == 220

    def test_empty_burger_receipt(self, mock_bun):
        self.burger.set_buns(mock_bun)
        expected_receipt = [
            '(==== green bun ====)',
            '(==== green bun  ====)',
            '',
            'Price: 220'
        ]
        assert self.burger.get_receipt() == '\n'.join(expected_receipt)