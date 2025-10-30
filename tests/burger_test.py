import pytest


class TestBurger:
    """Tests for the Burger class."""

    def test_burger_creation(self, empty_burger):
        """Test that a burger can be created and has correct initial state."""
        # Act - Use method to check burger state
        ingredients_count = len(empty_burger.ingredients)
        
        # Assert
        assert empty_burger.bun is None
        assert ingredients_count == 0

    def test_set_buns(self, empty_burger, test_bun):
        """Test that set_buns method correctly assigns buns to burger."""
        # Act
        empty_burger.set_buns(test_bun)
        assigned_bun = empty_burger.bun

        # Assert
        assert assigned_bun is test_bun
        assert assigned_bun.get_name() == "test bun"
        assert assigned_bun.get_price() == 100.0

    def test_add_ingredient(self, empty_burger, sauce_ingredient):
        """Test that add_ingredient method successfully adds ingredient to burger."""
        # Act
        empty_burger.add_ingredient(sauce_ingredient)
        ingredients_count = len(empty_burger.ingredients)
        added_ingredient = empty_burger.ingredients[0]

        # Assert
        assert ingredients_count == 1
        assert added_ingredient is sauce_ingredient
        assert added_ingredient.get_name() == "test sauce"
        assert added_ingredient.get_type() == "SAUCE"

    def test_remove_ingredient(
        self, empty_burger, sauce_ingredient, filling_ingredient
    ):
        """Test that remove_ingredient method correctly removes ingredient by index."""
        # Arrange
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        empty_burger.remove_ingredient(0)
        remaining_count = len(empty_burger.ingredients)
        remaining_ingredient = empty_burger.ingredients[0]

        # Assert
        assert remaining_count == 1
        assert remaining_ingredient is filling_ingredient
        assert remaining_ingredient.get_name() == "test filling"

    def test_move_ingredient(self, empty_burger, sauce_ingredient, filling_ingredient):
        """Test that move_ingredient method correctly reorders ingredients."""
        # Arrange
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        empty_burger.move_ingredient(0, 1)
        ingredients_count = len(empty_burger.ingredients)
        first_ingredient = empty_burger.ingredients[0]
        second_ingredient = empty_burger.ingredients[1]

        # Assert
        assert ingredients_count == 2
        assert first_ingredient is filling_ingredient
        assert second_ingredient is sauce_ingredient
        assert first_ingredient.get_name() == "test filling"
        assert second_ingredient.get_name() == "test sauce"

    def test_move_ingredient_backward(
        self, empty_burger, sauce_ingredient, filling_ingredient
    ):
        """Test move_ingredient method when moving from later to earlier position."""
        # Arrange: Add two ingredients
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)
        
        # Act: Move the second ingredient (index 1) to the first position (index 0)
        empty_burger.move_ingredient(1, 0)
        first_ingredient = empty_burger.ingredients[0]
        second_ingredient = empty_burger.ingredients[1]
        
        # Assert: The order should be swapped
        assert first_ingredient is filling_ingredient
        assert second_ingredient is sauce_ingredient
        assert first_ingredient.get_type() == "FILLING"
        assert second_ingredient.get_type() == "SAUCE"

    def test_get_price(
        self, empty_burger, test_bun, sauce_ingredient, filling_ingredient
    ):
        """Test that get_price method calculates total burger price correctly."""
        # Arrange
        empty_burger.set_buns(test_bun)  # 100.0 * 2 = 200.0
        empty_burger.add_ingredient(sauce_ingredient)  # 50.0
        empty_burger.add_ingredient(filling_ingredient)  # 150.0

        # Act
        total_price = empty_burger.get_price()
        expected_price = (test_bun.get_price() * 2) + sauce_ingredient.get_price() + filling_ingredient.get_price()

        # Assert
        assert total_price == expected_price
        assert total_price == 400.0

    def test_get_receipt(
        self, empty_burger, test_bun, sauce_ingredient, filling_ingredient
    ):
        """Test that get_receipt method generates formatted receipt string."""
        # Arrange
        empty_burger.set_buns(test_bun)
        empty_burger.add_ingredient(sauce_ingredient)
        empty_burger.add_ingredient(filling_ingredient)

        # Act
        receipt = empty_burger.get_receipt()
        total_price = empty_burger.get_price()

        # Assert - Check receipt structure and content
        expected_receipt = (
            f"(==== {test_bun.get_name()} ====)\n"
            f"= {sauce_ingredient.get_type().lower()} {sauce_ingredient.get_name()} =\n"
            f"= {filling_ingredient.get_type().lower()} {filling_ingredient.get_name()} =\n"
            f"(==== {test_bun.get_name()} ====)\n\n"
            f"Price: {total_price}"
        )
        assert receipt == expected_receipt
        assert "test bun" in receipt
        assert "test sauce" in receipt
        assert "test filling" in receipt
        assert str(total_price) in receipt

    def test_get_price_without_bun_raises(self, empty_burger):
        """Test that get_price raises an error if bun is not set."""
        with pytest.raises(ValueError, match="Bun is not set"):
            empty_burger.get_price()

    def test_get_receipt_without_bun_raises(self, empty_burger):
        """Test that get_receipt raises an error if bun is not set."""
        with pytest.raises(ValueError, match="Bun is not set"):
            empty_burger.get_receipt()
