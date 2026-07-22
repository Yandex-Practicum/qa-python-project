from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    
    def test_set_buns_correct(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_to_ingredients_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_from_list_by_index(self):
        burger = Burger()
        mock_sauce = Mock()
        mock_cutlet = Mock()

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_cutlet)

        burger.remove_ingredient(1)

        assert mock_cutlet not in burger.ingredients
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_move_ingredient_position_in_list(self):
        burger = Burger()
        mock_sauce = Mock()
        mock_cutlet = Mock()
        mock_ketchup = Mock()

        burger.add_ingredient(mock_cutlet)
        burger.add_ingredient(mock_ketchup)
        burger.add_ingredient(mock_sauce)

        burger.move_ingredient(2, 0)

        assert burger.ingredients[0] == mock_sauce
        assert burger.ingredients[1] == mock_cutlet
        assert len(burger.ingredients) == 3


    def test_get_price_calculates_double_bun_plus_ingredients_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_cutlet = Mock()
        mock_ketchup = Mock()
        mock_sauce = Mock()

        mock_bun.get_price.return_value = 100.0
        mock_ketchup.get_price.return_value = 30.0
        mock_cutlet.get_price.return_value = 150.0
        mock_sauce.get_price.return_value = 50.0
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ketchup)
        burger.add_ingredient(mock_cutlet)
        burger.add_ingredient(mock_sauce)

        assert burger.get_price() == 430.0
        assert isinstance(burger.get_price(), float)

    def test_get_receipt_generates_correctly_formatted_string_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_ingredient_1 = Mock()

        mock_bun.get_name.return_value = "Булка с кунжутом"
        mock_bun.get_price.return_value = 100.0
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "ketchup"
        mock_ingredient.get_price.return_value = 30.0
        mock_ingredient_1.get_type.return_value = "FILLING"
        mock_ingredient_1.get_name.return_value = "cutlet"
        mock_ingredient_1.get_price.return_value = 150.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_1)

        expected_receipt = (
            "(==== Булка с кунжутом ====)\n"
            "= sauce ketchup =\n"
            "= filling cutlet =\n"
            "(==== Булка с кунжутом ====)\n\n"
            "Price: 380.0"
        )

        assert burger.get_receipt() == expected_receipt
