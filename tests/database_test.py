
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Tests for the Database class."""

    def test_database_creation(self, database):
        """Test that a database is initialized with the correct data through its methods."""
        # Act - Use methods to get data instead of accessing attributes directly
        available_buns = database.available_buns()
        available_ingredients = database.available_ingredients()
        
        # Assert - Test the methods return the expected data structure
        assert len(available_buns) == 3
        assert len(available_ingredients) == 6

        # Check that buns method returns correct buns
        assert isinstance(available_buns[0], Bun)
        assert available_buns[0].get_name() == "black bun"
        assert available_buns[0].get_price() == 100

        assert available_buns[1].get_name() == "white bun"
        assert available_buns[1].get_price() == 200

        assert available_buns[2].get_name() == "red bun"
        assert available_buns[2].get_price() == 300

        # Check that ingredients method returns correct ingredients
        assert isinstance(available_ingredients[0], Ingredient)
        assert available_ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[0].get_name() == "hot sauce"
        assert available_ingredients[0].get_price() == 100

        assert available_ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[1].get_name() == "sour cream"
        assert available_ingredients[1].get_price() == 200

        assert available_ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[2].get_name() == "chili sauce"
        assert available_ingredients[2].get_price() == 300

        assert available_ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert available_ingredients[3].get_name() == "cutlet"
        assert available_ingredients[3].get_price() == 100

        assert available_ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert available_ingredients[4].get_name() == "dinosaur"
        assert available_ingredients[4].get_price() == 200

        assert available_ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert available_ingredients[5].get_name() == "sausage"
        assert available_ingredients[5].get_price() == 300

    def test_available_buns(self, database):
        """Test that available_buns method returns all buns."""
        # Act
        buns = database.available_buns()

        # Assert
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self, database):
        """Test that available_ingredients method returns all ingredients."""
        # Act
        ingredients = database.available_ingredients()

        # Assert
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        # Check sauce ingredients
        sauce_count = sum(1 for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_FILLING)
        assert sauce_count == 3
        assert filling_count == 3
