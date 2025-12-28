from unittest.mock import Mock
from practikum.burger import Burger
from data import BunData, IngrData, Receipt


class TestBurger:

    def test_set_buns(self):
        mock_bun = Mock()
        file_o_fish = Burger()
        file_o_fish.set_buns(mock_bun)
        assert file_o_fish.bun == mock_bun

    def test_get_price(self):
        mock_bun = Mock()
        file_o_fish = Burger()
        mock_bun.get_price.return_value = 1000
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 600
        file_o_fish.bun = mock_bun
        file_o_fish.ingredients = [mock_ingredient]
        assert file_o_fish.get_price() == 1000*2+600

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        file_o_fish = Burger()
        file_o_fish.add_ingredient(mock_ingredient)
        assert file_o_fish.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        file_o_fish = Burger()
        file_o_fish.add_ingredient(mock_ingredient)
        file_o_fish.remove_ingredient(0)
        assert file_o_fish.ingredients == []

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        file_o_fish = Burger()
        file_o_fish.add_ingredient(mock_ingredient)
        file_o_fish.add_ingredient(mock_ingredient)
        file_o_fish.add_ingredient(mock_ingredient)
        file_o_fish.move_ingredient(0, 1)
        assert len(file_o_fish.ingredients) == 3

    def test_get_receipt(self):
        file_o_fish = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BunData.bun_name
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = IngrData.ingr_type
        mock_ingredient.get_name.return_value = IngrData.ingr_name
        mock_bun.get_price.return_value = 155
        mock_ingredient.get_price.return_value = 55
        file_o_fish.bun = mock_bun
        file_o_fish.ingredients = [mock_ingredient]
        expected_receipt = Receipt.receipt_body
        assert file_o_fish.get_receipt() == expected_receipt



