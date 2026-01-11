from ingredient import Ingredient


class TestIngredient:

    def test_init_ingredient_type(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.type == "sauce"

    def test_init_ingredient_name(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.name == "heinz"

    def test_init_ingredient_price(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.price == 250

    def test_get_price(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.get_price() == 250

    def test_get_name(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.get_name() == "heinz"

    def test_get_type(self):
        ingredient = Ingredient("sauce", "heinz", 250)
        assert ingredient.get_type() == "sauce"




