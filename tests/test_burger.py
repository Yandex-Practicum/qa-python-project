from conftest import burger, mock_bun, mock_ingredient_1, mock_ingredient_2
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient_add_one_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        assert len(burger.ingredients) == 1
        assert mock_ingredient_1 in burger.ingredients


    def test_remove_ingredient_remove_one_ingredient(self, burger):
        ingredient_1 = burger.ingredients[0]
        ingredient_2 = burger.ingredients[1]
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert ingredient_1 in burger.ingredients
        assert ingredient_2 not in burger.ingredients


    def test_move_ingredient(self, burger):
        ingredient_1 = burger.ingredients[0]
        ingredient_2 = burger.ingredients[1]
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_1


    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        mock_bun.get_price.return_value = 50
        mock_ingredient_1.get_price.return_value = 100
        mock_ingredient_2.get_price.return_value = 150
        assert burger.get_price() == 350


    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        mock_bun.get_name.return_value = 'bun'
        mock_bun.get_price.return_value = 50
        mock_ingredient_1.get_name.return_value = 'sauce'
        mock_ingredient_1.get_price.return_value = 100
        mock_ingredient_1.get_type.return_value = 'sauce'
        mock_ingredient_2.get_name.return_value = 'filling'
        mock_ingredient_2.get_price.return_value = 150
        mock_ingredient_2.get_type.return_value = 'filling'
        receipt = [
            '(==== bun ====)',
            '= sauce sauce =',
            '= filling filling =',
            '(==== bun ====)\n',
            'Price: 350'
        ]
        assert '\n'.join(receipt) == burger.get_receipt()