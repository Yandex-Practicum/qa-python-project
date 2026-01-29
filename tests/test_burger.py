class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_1):
        burger.add_ingredient(mock_ingredient_1)
        assert mock_ingredient_1 in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient_1):
        burger.add_ingredient(mock_ingredient_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_ingredient_1, mock_ingredient_2):
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_1
        assert burger.ingredients[0] == mock_ingredient_2

    def test_get_price(self, burger, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == 700

    def test_get_receipt(self, burger, mock_bun, mock_ingredient_1, mock_ingredient_2):
        receipt = '\n'.join(['(==== black bun ====)',
                   '= sauce hot sauce =',
                   '= filling cutlet =',
                   '(==== black bun ====)\n',
                   'Price: 700'])
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_receipt() == receipt


