from unittest.mock import Mock
from praktikum.burger import Burger
from data import BunData, IngredientData, Receipt


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
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        file_o_fish = Burger()
        file_o_fish.add_ingredient(mock_ingredient_1)
        file_o_fish.add_ingredient(mock_ingredient_2)
        file_o_fish.add_ingredient(mock_ingredient_3)
        file_o_fish.move_ingredient(0, 2)
        assert file_o_fish.ingredients == [mock_ingredient_2, mock_ingredient_3, mock_ingredient_1]

    def test_get_receipt(self):
        file_o_fish = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BunData.bun_name
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = IngredientData.ingredient_type
        mock_ingredient.get_name.return_value = IngredientData.ingredient_name
        mock_bun.get_price.return_value = 988
        mock_ingredient.get_price.return_value = 4142
        file_o_fish.bun = mock_bun
        file_o_fish.ingredients = [mock_ingredient]
        expected_receipt = Receipt.receipt_body
        assert file_o_fish.get_receipt() == expected_receipt

