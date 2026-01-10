from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database

class TestBurger:

    def test_set_bun_for_burger(self):
        burger = Burger()
        bun = Bun('bun_name', 200)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'bun_name'
        mock_ingredient.get_price.return_value = 200.0
        burger.add_ingredient(mock_ingredient)
        assert (burger.ingredients[0].get_price() == 200.0 and
                burger.ingredients[0].get_name() == 'bun_name')

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(2, 1)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_3, mock_ingredient_2]

    def test_delete_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_count_burger_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.add_ingredient(database.available_ingredients()[4])
        assert burger.get_price() == 600.0

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.add_ingredient(database.available_ingredients()[4])
        expected_receipt = "(==== black bun ====)\n" \
                           "= sauce sour cream =\n" \
                           "= filling dinosaur =\n" \
                           "(==== black bun ====)\n\n" \
                           "Price: 600"
        assert expected_receipt == burger.get_receipt()

