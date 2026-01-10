import pytest

class TestDatabase:
    @pytest.mark.parametrize("expected_buns", [
        (["black bun", "white bun", "red bun"])
    ])
    def test_available_buns(self, database, expected_buns):
        buns = database.available_buns()
        assert len(buns) == len(expected_buns)
        for i, bun in enumerate(buns):
            assert bun.name == expected_buns[i]

    @pytest.mark.parametrize("expected_ingredients", [
        (["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"])
    ])
    def test_available_ingredients(self, database, expected_ingredients):
        ingredients = database.available_ingredients()
        assert len(ingredients) == len(expected_ingredients)
        for i, ingredient in enumerate(ingredients):
            assert ingredient.name == expected_ingredients[i]