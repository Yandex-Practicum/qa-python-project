from praktikum.database import Database


class TestDatabase:

    def test_database_buns_returns_all_buns(self, db: Database, mock_bun):
        
        db.buns = [mock_bun, mock_bun, mock_bun]

        buns = db.available_buns()
    
        assert len(buns) == 3
        assert buns[0].get_name() == mock_bun.get_name()
        assert buns[0].get_price() == mock_bun.get_price()

    def test_available_ingredients(self, db: Database, mock_sauce, mock_filling):

        db.ingredients = [mock_sauce, mock_filling]

        ingredients = db.available_ingredients()

        assert len(ingredients) == 2
        assert ingredients[0] is mock_sauce
        assert ingredients[0].get_type() == mock_sauce.get_type()
        assert ingredients[0].get_name() == mock_sauce.get_name()
        assert ingredients[0].get_price() == mock_sauce.get_price()

        assert ingredients[1] is mock_filling
        assert ingredients[1].get_type() == mock_filling.get_type()
        assert ingredients[1].get_name() == mock_filling.get_name()
        assert ingredients[1].get_price() == mock_filling.get_price()

