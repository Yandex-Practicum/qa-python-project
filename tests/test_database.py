from unittest.mock import Mock, patch

from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:

    @patch('database.Bun')
    def test_available_buns_returns_correct_bun(self, mock_bun_class):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun_class.side_effect = [mock_bun, Mock(), Mock()]

        buns = Database().available_buns()

        assert buns[0].get_name() == "black bun"

    @patch('database.Ingredient')
    def test_available_ingredients_returns_correct_ingredient(self, mock_ingredient_class):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_class.side_effect = [mock_ingredient, Mock(), Mock(), Mock(), Mock(), Mock()]

        ingredients = Database().available_ingredients()

        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
