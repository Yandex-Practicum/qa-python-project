from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, create_burger, create_bun):
        create_burger.set_buns(create_bun)
        assert create_burger.bun == create_bun

    def test_add_ingredient(self, create_burger, create_ingredient):
        create_burger.add_ingredient(create_ingredient)
        assert create_burger.ingredients == [create_ingredient]

    def test_remove_ingredient(self, create_burger, create_ingredient):
        create_burger.add_ingredient(create_ingredient)
        assert create_burger.ingredients == [create_ingredient]
        create_burger.remove_ingredient(0)
        assert create_burger.ingredients == []

    def test_move_ingredient(self, create_burger):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        create_burger.add_ingredient(mock_ingredient_1)
        create_burger.add_ingredient(mock_ingredient_2)
        assert create_burger.ingredients == [mock_ingredient_1, mock_ingredient_2]
        create_burger.move_ingredient(0, 1)
        assert create_burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price(self, create_burger, create_bun, create_ingredient):
        create_burger.set_buns(create_bun)
        create_burger.add_ingredient(create_ingredient)
        expected_price = (create_bun.price * 2) + create_ingredient.price
        assert create_burger.get_price() == expected_price

    def test_get_receipt(self, create_burger, create_bun, create_ingredient):
        create_burger.set_buns(create_bun)
        create_burger.add_ingredient(create_ingredient)
        expected_receipt = (
            f'(==== {create_bun.get_name()} ====)'
            f'\n= {str(create_ingredient.get_type()).lower()} {create_ingredient.get_name()} ='
            f'\n(==== {create_bun.get_name()} ====)\n'
            f'\nPrice: {create_burger.get_price()}')
        receipt = create_burger.get_receipt()
        assert receipt == expected_receipt
