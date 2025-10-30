from unittest.mock import patch, MagicMock
from praktikum.praktikum import main


class TestPraktikum:
    """Tests for the praktikum main module."""

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_initializes_database_and_burger(self, mock_burger_class, mock_database_class):
        """Test that main function initializes Database and Burger classes."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        mock_database_class.assert_called_once()
        mock_burger_class.assert_called_once()

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_gets_available_data_from_database(self, mock_burger_class, mock_database_class):
        """Test that main function retrieves available buns and ingredients from database."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_sets_bun_on_burger(self, mock_burger_class, mock_database_class):
        """Test that main function sets the first available bun on the burger."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_buns = [MagicMock(), MagicMock(), MagicMock()]
        mock_database.available_buns.return_value = mock_buns
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        mock_burger.set_buns.assert_called_once_with(mock_buns[0])

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_adds_ingredients_to_burger(self, mock_burger_class, mock_database_class):
        """Test that main function adds four ingredients to the burger."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        assert mock_burger.add_ingredient.call_count == 4

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_moves_ingredient(self, mock_burger_class, mock_database_class):
        """Test that main function moves an ingredient from index 2 to index 1."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        mock_burger.move_ingredient.assert_called_once_with(2, 1)

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_removes_ingredient(self, mock_burger_class, mock_database_class):
        """Test that main function removes ingredient at index 3."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Mock Receipt"

        # Act
        main()

        # Assert
        mock_burger.remove_ingredient.assert_called_once_with(3)

    @patch("praktikum.praktikum.Database")
    @patch("praktikum.praktikum.Burger")
    def test_main_returns_burger_receipt(self, mock_burger_class, mock_database_class):
        """Test that main function returns the burger receipt."""
        # Arrange
        mock_burger = MagicMock()
        mock_burger_class.return_value = mock_burger
        mock_database = MagicMock()
        mock_database_class.return_value = mock_database
        mock_database.available_buns.return_value = [MagicMock()]
        mock_database.available_ingredients.return_value = [MagicMock() for _ in range(6)]
        mock_receipt = "Mock Receipt"
        mock_burger.get_receipt.return_value = mock_receipt

        # Act
        result = main()

        # Assert
        mock_burger.get_receipt.assert_called_once()
        assert result == mock_receipt
