import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import MagicMock

class TestBurger:
    """Tests for the Burger class and its methods."""

    def test_set_buns_assigns_bun_object(self):
        """Burger.set_buns should correctly assign the bun to the burger."""
        burger = Burger()
        bun = Bun("Test Bun", 123)  # create a Bun instance
        burger.set_buns(bun)
        # After setting, the burger.bun should refer to the same bun object
        assert burger.bun is bun, "Burger.bun should be set to the given bun instance"

    def test_add_ingredient_appends_to_list(self):
        """Burger.add_ingredient should add an ingredient to the ingredients list."""
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "Sauce A", 10)
        ingredient2 = Ingredient("FILLING", "Filling B", 20)
        burger.set_buns(Bun("Bun", 50))  # set a bun to avoid issues in other methods
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        # After adding two ingredients, the list should contain them in order
        assert burger.ingredients == [ingredient1, ingredient2], "Ingredients list should contain added ingredients in order"

    def test_remove_ingredient_removes_correct_item(self):
        """Burger.remove_ingredient should remove the ingredient at the specified index."""
        burger = Burger()
        burger.set_buns(Bun("Bun", 50))
        ing_a = Ingredient("SAUCE", "Sauce A", 5)
        ing_b = Ingredient("FILLING", "Filling B", 15)
        ing_c = Ingredient("SAUCE", "Sauce C", 8)
        burger.add_ingredient(ing_a)
        burger.add_ingredient(ing_b)
        burger.add_ingredient(ing_c)
        # Remove the ingredient in the middle (index 1, which is ing_b)
        burger.remove_ingredient(1)
        # Now the ingredients list should have ing_a and ing_c, with ing_b removed
        assert ing_b not in burger.ingredients, "Removed ingredient should no longer be in the list"
        assert burger.ingredients == [ing_a, ing_c], "Ingredients list should have removed the specified element"

    @pytest.mark.parametrize("initial_order, index, new_index, expected_order", [
        (["A", "B", "C"], 0, 2, ["B", "C", "A"]),   # move first element to end
        (["A", "B", "C"], 2, 0, ["C", "A", "B"]),   # move last element to start
    ])
    def test_move_ingredient_reorders_list(self, initial_order, index, new_index, expected_order):
        """Burger.move_ingredient should insert the ingredient at new_index position."""
        # Set up burger with dummy ingredients named as initial_order letters
        burger = Burger()
        burger.set_buns(Bun("Bun", 10))
        ingredients = []
        for name in initial_order:
            ing = Ingredient("FILLING", name, 1)
            ingredients.append(ing)
            burger.add_ingredient(ing)
        # Perform move
        burger.move_ingredient(index, new_index)
        # Check the new order of ingredient names
        new_order_names = [ing.get_name() for ing in burger.ingredients]
        assert new_order_names == expected_order, f"Ingredients should be reordered to {expected_order}"

    def test_get_price_calculates_sum(self):
        """Burger.get_price should return 2*bun_price + sum of ingredient prices."""
        # Use MagicMock to simulate Bun and Ingredient with specific prices
        bun = MagicMock()
        bun.get_price.return_value = 100  # bun price
        ingredient1 = MagicMock()
        ingredient1.get_price.return_value = 40
        ingredient2 = MagicMock()
        ingredient2.get_price.return_value = 60
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        total_price = burger.get_price()
        # Expected price = 2*100 (two buns) + 40 + 60
        assert total_price == 2*100 + 40 + 60, "Total price should equal double bun price plus all ingredient prices"

    def test_get_receipt_formats_correctly(self):
        """Burger.get_receipt should format the receipt string with bun and ingredients."""
        # Create mock bun and ingredients with known return values for name/type/price
        bun = MagicMock()
        bun.get_name.return_value = "TestBun"
        bun.get_price.return_value = 50
        ing1 = MagicMock()
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "Chili"
        ing1.get_price.return_value = 30
        ing2 = MagicMock()
        ing2.get_type.return_value = "FILLING"
        ing2.get_name.return_value = "Cutlet"
        ing2.get_price.return_value = 70
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        receipt = burger.get_receipt()
        # Construct the expected receipt string manually
        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {ing1.get_type().lower()} {ing1.get_name()} =\n"
            f"= {ing2.get_type().lower()} {ing2.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert receipt == expected_receipt, "Receipt format or content is incorrect"
