
from unittest.mock import Mock, patch
from database import Database


class TestDatabaseMethods:
    @patch("database.Bun")
    def test_database_buns_initialisation_true(self, MockBun):

        mock_bun1 = Mock()
        mock_bun1.name = "black bun"
        mock_bun1.price = 100

        mock_bun2 = Mock()
        mock_bun2.name = "white bun"
        mock_bun2.price = 200

        mock_bun3 = Mock()
        mock_bun3.name = "red bun"
        mock_bun3.price = 300
        MockBun.side_effect = [mock_bun1, mock_bun2, mock_bun3]
        db = Database()

        assert len(db.buns) == 3

    @patch("database.Ingredient")
    def test_database_ingredient_initialisation_true(self, MockIngredient):

        mock_sauce1 = Mock()
        mock_sauce1.ingredient_type = "INGREDIENT_TYPE_SAUCE"
        mock_sauce1.name = "hot sauce"
        mock_sauce1.price = 100

        mock_sauce2 = Mock()
        mock_sauce2.ingredient_type = "INGREDIENT_TYPE_SAUCE"
        mock_sauce2.name = "sour cream"
        mock_sauce2.price = 200

        mock_sauce3 = Mock()
        mock_sauce3.ingredient_type = "INGREDIENT_TYPE_SAUCE"
        mock_sauce3.name = "chili sauce"
        mock_sauce3.price = 300

        mock_filling1 = Mock()
        mock_filling1.ingredient_type = "INGREDIENT_TYPE_FILLING"
        mock_filling1.name = "cutlet"
        mock_filling1.price = 100

        mock_filling2 = Mock()
        mock_filling2.ingredient_type = "INGREDIENT_TYPE_FILLING"
        mock_filling2.name = "dinosaur"
        mock_filling2.price = 200

        mock_filling3 = Mock()
        mock_filling3.ingredient_type = "INGREDIENT_TYPE_FILLING"
        mock_filling3.name = "sausage"
        mock_filling3.price = 300

        MockIngredient.side_effect = [mock_sauce1, mock_sauce2, mock_sauce3, mock_filling1, mock_filling2, mock_filling3]
        db = Database()


        assert len(db.ingredients) == 6



    def test_database_available_buns_true(self):

        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_database_available_ingredients_true(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6