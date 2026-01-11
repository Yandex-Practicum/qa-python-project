import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabaseBuns:
    def test_available_buns_count(self, db):
        """Проверка количества и названий доступных булочек."""
        buns = db.available_buns()
        assert len(buns) == 3
        assert [bun.name for bun in buns] == ["black bun", "white bun", "red bun"]


class TestDatabaseIngredients:
    def test_available_ingredients_count(self, db):
        """Проверка количества доступных ингредиентов."""
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    @pytest.mark.parametrize("index, name, price", [
        (0, "hot sauce", 100),
        (1, "sour cream", 200),
        (2, "chili sauce", 300),
        (3, "cutlet", 100),
        (4, "dinosaur", 200),
        (5, "sausage", 300),
    ])
    def test_ingredient_data(self, db, index, name, price):
        """Проверка данных отдельных ингредиентов по индексу."""
        ingredient = db.available_ingredients()[index]
        assert ingredient.name == name
        assert ingredient.price == price

    def test_ingredient_types(self, db):
        """Проверка типов ингредиентов: соусы и начинки."""
        ingredients = db.available_ingredients()
        sauces = ingredients[:3]
        fillings = ingredients[3:]

        for sauce in sauces:
            assert sauce.type == INGREDIENT_TYPE_SAUCE

        for filling in fillings:
            assert filling.type == INGREDIENT_TYPE_FILLING
