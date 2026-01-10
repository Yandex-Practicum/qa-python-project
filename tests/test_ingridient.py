from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient("мясо", "Котлетька", 100)
        assert ingredient.get_name() == "Котлетька"

    def test_get_price(self):
        ingredient = Ingredient("мясо", "Котлетька", 100)
        assert ingredient.get_price() == 100

    def test_get_type(self):
        ingredient = Ingredient("мясо", "Котлетька", 100)
        assert ingredient.get_type() == "мясо"
