class TestIngredient:
    def test_get_price_of_ingredient(self, create_ingredient):
        actual_price = create_ingredient.get_price()
        expected_price = create_ingredient.price
        assert actual_price == expected_price

    def test_get_name_of_ingredient(self, create_ingredient):
        actual_name = create_ingredient.get_name()
        expected_name = create_ingredient.name
        assert actual_name == expected_name


    def test_get_type_of_ingredient(self, create_ingredient):
        actual_type = create_ingredient.get_type()
        expected_type = create_ingredient.type
        assert actual_type == expected_type
