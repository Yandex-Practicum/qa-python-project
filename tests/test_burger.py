from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'test bun'
        mock_bun.get_price.return_value = 99.99
        burger.set_buns(mock_bun)

        assert (mock_bun.get_name() == burger.bun.get_name() and
                mock_bun.get_price() == burger.bun.get_price())

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'TEST_SAUCE'
        mock_ingredient.get_name.return_value = 'test sauce'
        mock_ingredient.get_price.return_value = 100.001
        burger.add_ingredient(mock_ingredient)

        assert (len(burger.ingredients) == 1 and
                mock_ingredient.get_type() == burger.ingredients[0].get_type() and
                mock_ingredient.get_name() == burger.ingredients[0].get_name() and
                mock_ingredient.get_price() == burger.ingredients[0].get_price())

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert (burger.ingredients.index(mock_ingredient_1) == 1 and
                burger.ingredients.index(mock_ingredient_2) == 0)


    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 19.09
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 9.99

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 48.17 # 19.09*2 + 9.99

    def test_get_recept(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'test bun'
        mock_bun.get_price.return_value = 9.99

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'TEST SAUCE'
        mock_ingredient.get_name.return_value = 'test-sauce'
        mock_ingredient.get_price.return_value = 10.01

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()

        assert (f'(==== {mock_bun.get_name()} ====)'+'\n'+f'= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} ='+'\n'+f'(==== {mock_bun.get_name()} ====)'+'\n'+'\n'+f'Price: {burger.get_price()}') == burger.get_receipt()