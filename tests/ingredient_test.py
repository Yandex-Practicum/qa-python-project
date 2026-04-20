

class TestIngredient:

    def test_get_name_ingredient(self, ingredient):
        ingredient_obj, name = ingredient[0], ingredient[2]
        assert ingredient_obj.get_name() == name

    def test_get_price_ingredient(self, ingredient):
        ingredient_obj, price = ingredient[0], ingredient[3]
        assert ingredient_obj.get_price() == price

    def test_get_type_ingredient(self, ingredient):
        ingredient_obj, ingredient_type = ingredient[0], ingredient[1]
        assert ingredient_obj.get_type() == ingredient_type
