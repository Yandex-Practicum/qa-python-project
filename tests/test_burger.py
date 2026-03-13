from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "black bun"

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_name.return_value = "sausage"
        mock_ingredient.get_type.return_value = "FILLING"

        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_name.return_value = "sausage"
        mock_ingredient.get_type.return_value = "FILLING"

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient1.get_name.return_value = "sausage"
        mock_ingredient1.get_type.return_value = "FILLING"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 30
        mock_ingredient2.get_name.return_value = "ketchup"
        mock_ingredient2.get_type.return_value = "SAUCE"

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "black bun"

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient1.get_name.return_value = "sausage"
        mock_ingredient1.get_type.return_value = "FILLING"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 30
        mock_ingredient2.get_name.return_value = "ketchup"
        mock_ingredient2.get_type.return_value = "SAUCE"

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.get_price() == 280

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "black bun"

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient1.get_name.return_value = "sausage"
        mock_ingredient1.get_type.return_value = "FILLING"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 30
        mock_ingredient2.get_name.return_value = "ketchup"
        mock_ingredient2.get_type.return_value = "SAUCE"

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = '(==== black bun ====)\n= filling sausage =\n= sauce ketchup =\n(==== black bun ====)\n\nPrice: 280'

        assert burger.get_receipt() == expected_receipt                    