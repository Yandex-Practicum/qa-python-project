from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Tests for the Ingredient class."""

    def test_ingredient_creation(self):
        """Test that an ingredient can be created with a type, name, and price."""
        # Arrange
        ingredient_type = INGREDIENT_TYPE_SAUCE
        name = "ketchup"
        price = 50.0

        # Act
        ingredient = Ingredient(ingredient_type, name, price)

        # Assert
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        """Test that get_price method returns the correct price."""
        # Arrange
        price = 75.0
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", price)

        # Act
        result = ingredient.get_price()

        # Assert
        assert result == price

    def test_get_name(self):
        """Test that get_name method returns the correct name."""
        # Arrange
        name = "mayo"
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 60.0)

        # Act
        result = ingredient.get_name()

        # Assert
        assert result == name

    def test_get_type(self):
        """Test that get_type method returns the correct type."""
        # Arrange
        ingredient_type = INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(ingredient_type, "chicken", 120.0)

        # Act
        result = ingredient.get_type()

        # Assert
        assert result == ingredient_type

    def test_ingredient_types(self):
        """Test that ingredient types are correctly defined."""
        # Assert
        assert INGREDIENT_TYPE_SAUCE == "SAUCE"
        assert INGREDIENT_TYPE_FILLING == "FILLING"
