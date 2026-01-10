from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_comparison_ingredient_type(self):
        ingredient = Ingredient("Начинки", "Говяжий метеорит (отбивная)", 3000)
        assert ingredient.get_type() == "Начинки"

    def test_comparison_ingredient_name(self):
        ingredient = Ingredient("Начинки", "Говяжий метеорит (отбивная)", 3000)
        assert ingredient.get_name() == "Говяжий метеорит (отбивная)"

    def test_comparison_ingredient_price(self):
        ingredient = Ingredient("Начинки", "Говяжий метеорит (отбивная)", 3000)
        assert ingredient.get_price() == 3000