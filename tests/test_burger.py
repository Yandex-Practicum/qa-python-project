from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_new_burger_has_no_bun_and_no_ingredients(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    def test_remove_ingredient_removes_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_3]

    def test_move_ingredient_moves_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_3, mock_ingredient_1]

    def test_get_price_calculates_total_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 50
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 30
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        total_price = burger.get_price()
        expected_price = (100 * 2) + 50 + 30
        assert total_price == expected_price

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black_bun"
        mock_bun.get_price.return_value = 100

        mock_filling = Mock()
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_name.return_value = "dinosaur"
        mock_filling.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert receipt == (
            "(==== black_bun ====)\n"
            "= filling dinosaur =\n"
            "(==== black_bun ====)\n"
            "\n"
            "Price: 250"
        )