from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    
    def test_set_buns_sets_correct_bun_value(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun


    def test_add_ingredient_adds_ingredient_to_list_of_ingredients(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1


    def test_remove_ingredient_remove_first_ingredient_removes_correct_ingredient(self):
        burger = Burger()
        mock_first_ingredient = Mock()
        mock_second_ingredient = Mock()
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.remove_ingredient(0)

        assert mock_first_ingredient not in burger.ingredients
        assert len(burger.ingredients) == 1


    def test_move_ingredient_move_first_ingredient_moves_ingredient_on_correct_place(self):
        burger = Burger()
        mock_first_ingredient = Mock()
        mock_second_ingredient = Mock()
        mock_third_ingredient = Mock()
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        burger.add_ingredient(mock_third_ingredient)
        burger.move_ingredient(0,2)

        assert burger.ingredients[2] == mock_first_ingredient


    def test_get_price_for_buns_with_ingredients_returns_correct_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 200
        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 300
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_price.return_value = 200
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert burger.get_price() == 900

    
    def test_get_receipt_for_buns_with_ingredients_returns_expected_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "red bun"
        mock_bun.get_price.return_value = 300

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_name.return_value = "dinosaur"
        mock_first_ingredient.get_type.return_value = "filling"
        mock_first_ingredient.get_price.return_value = 200

        mock_second_ingredient = Mock()
        mock_second_ingredient.get_name.return_value = "hot sauce"
        mock_second_ingredient.get_type.return_value = "sauce"
        mock_second_ingredient.get_price.return_value = 100

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        burger_receipt = burger.get_receipt()

        assert "(==== red bun ====)" in burger_receipt
        assert "= filling dinosaur =" in burger_receipt
        assert "= sauce hot sauce =" in burger_receipt
        assert f"Price: {str(burger.get_price())}" in burger_receipt