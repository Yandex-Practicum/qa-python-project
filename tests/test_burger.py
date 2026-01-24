from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger):
        mock_bun = Mock()

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_second_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == mock_second_ingredient
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 4
        mock_ingredient.get_price.return_value = 3

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        price = burger.get_price()
        assert price == expected_price

    def test_get_receipt(self, burger):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_name.return_value = 'bulochka'
        mock_bun.get_price.return_value = 4
        mock_ingredient.get_name.return_value = 'kotleta'
        mock_ingredient.get_type.return_value = 'nachinka'
        mock_ingredient.get_price.return_value = 3

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_receipt = (f'(==== {mock_bun.get_name()} ====)\n'
                            f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =\n'
                            f'(==== {mock_bun.get_name()} ====)\n\n'
                            f'Price: {burger.get_price()}')
        receipt = burger.get_receipt()
        assert receipt == expected_receipt
