from praktikum.bun import Bun


class TestBun:
    """Tests for the Bun class."""

    def test_bun_creation(self):
        """Test that a bun can be created with a name and price."""
        # Arrange
        name = "sesame bun"
        price = 150.0

        # Act
        bun = Bun(name, price)

        # Assert
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        """Test that get_name method returns the correct name."""
        # Arrange
        name = "white bun"
        bun = Bun(name, 200.0)

        # Act
        result = bun.get_name()

        # Assert
        assert result == name

    def test_get_price(self):
        """Test that get_price method returns the correct price."""
        # Arrange
        price = 250.0
        bun = Bun("black bun", price)

        # Act
        result = bun.get_price()

        # Assert
        assert result == price
