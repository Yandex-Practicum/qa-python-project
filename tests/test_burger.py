from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_correct_creation(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_one_ingredient_correct_add(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)

        assert mock_ingredient1 in burger.ingredients

    def test_remove_ingredient_correct_index_success_remove(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.remove_ingredient(0)

        assert ingredient2 in burger.ingredients and ingredient1 not in burger.ingredients

    def test_move_ingredient_success_move(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price_success(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.set_buns(mock_bun)

        mock_bun.get_price.return_value = 100
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient2.get_price.return_value = 100

        assert burger.get_price() == 400

    def test_get_receipt_success(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.set_buns(mock_bun)

        mock_bun.get_name.return_value = 'test bun'
        mock_bun.get_price.return_value = 100

        mock_ingredient1.get_type.return_value = 'sauce'
        mock_ingredient2.get_type.return_value = 'filling'
        mock_ingredient1.get_name.return_value = 'test sauce'
        mock_ingredient2.get_name.return_value = 'test filling'
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient2.get_price.return_value = 100

        receipt = [
            '(==== test bun ====)',
            '= sauce test sauce =',
            '= filling test filling =',
            '(==== test bun ====)\n',
            'Price: 400'
        ]

        assert '\n'.join(receipt) == burger.get_receipt()
