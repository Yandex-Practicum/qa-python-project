from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    """Tests for the Database class."""

    def test_available_buns_returns_list_of_buns(self):
        """available_buns should return a list of Bun objects pre-populated in the database."""
        db = Database()
        buns = db.available_buns()
        # It should return a list
        assert isinstance(buns, list), "available_buns() should return a list"
        # The list should not be empty (expected 3 buns in default database)
        assert len(buns) >= 1, "available_buns() should return at least one bun"
        # Every item should be a Bun instance
        assert all(isinstance(b, Bun) for b in buns), "available_buns() list items should be Bun instances"
        # Check that one of the known bun names is present (e.g., "black bun")
        bun_names = [b.get_name() for b in buns]
        assert "black bun" in bun_names, "Default buns should include 'black bun'"

    def test_available_ingredients_returns_list_of_ingredients(self):
        """available_ingredients should return a list of Ingredient objects pre-populated in the database."""
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list), "available_ingredients() should return a list"
        assert len(ingredients) >= 1, "available_ingredients() should return at least one ingredient"
        assert all(isinstance(ing, Ingredient) for ing in ingredients), "Items should be Ingredient instances"
        # Check that at least one sauce and one filling are present via their type or names
        types = {ing.get_type() for ing in ingredients}
        assert "SAUCE" in types and "FILLING" in types, "Default ingredients should include both sauces and fillings"
