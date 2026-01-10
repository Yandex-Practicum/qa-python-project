
class TestIngredient:
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 0.75

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Tomato"

    def test_get_type(self, ingredient, sauce):
        assert ingredient.get_type() == "filling"
        assert sauce.get_type() == "sauce"