class TestIngredient:

    def test_type_of_ingredient_true(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.type == "SAUCE"

    def test_name_of_ingredient_true(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.name == "hot sauce"

    def test_price_of_ingredient_true(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.price == 100

    def test_get_type_get_correct_type(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.get_type() == "SAUCE"

    def test_get_name_get_correct_name(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.get_name() == "hot sauce"

    def test_get_price_get_correct_price(self, mock_ingredient_type_name_price):
        ingredient = mock_ingredient_type_name_price
        assert ingredient.get_price() == 100