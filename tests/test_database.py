from unittest.mock import patch

from data.burger_data import BurgerData
from data.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_available_buns(self, db):
        buns = db.available_buns()
        assert len(buns) == 3
        assert [bun.get_name() for bun in buns] == BurgerData.DB_BUNS_NAMES
        assert [bun.get_price() for bun in buns] == BurgerData.DB_BUNS_PRICES

    def test_database_available_ingredients(self, db):
        available_ingredients = db.available_ingredients()
        sauces = [ing for ing in available_ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [ing for ing in available_ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3
        assert len(available_ingredients) == 6
        assert [sauce.get_name() for sauce in sauces] == BurgerData.DB_SAUCES
        assert [filling.get_name() for filling in fillings] == BurgerData.DB_FILLINGS

    def test_db_with_mocked_buns(self, db):
        # подмена класса Bun моком
        with patch('praktikum.bun.Bun') as MockBun:
            MockBun.return_value.get_name.return_value = "db mock bun"
            MockBun.return_value.get_price.return_value = 123

            db.buns = [MockBun(), MockBun()]
            buns = db.available_buns()
            assert buns == [MockBun(), MockBun()]

    def test_mocked_ingredients(self, db):
        # подмена класса Ingredient моком
        with patch('praktikum.ingredient.Ingredient') as MockIngredient:
            MockIngredient.return_value.get_type.return_value = INGREDIENT_TYPE_SAUCE
            MockIngredient.return_value.get_name.return_value = "mock sauce"
            MockIngredient.return_value.get_price.return_value = 99

            db.ingredients = [MockIngredient(), MockIngredient()]
            ingredients = db.available_ingredients()
            assert ingredients == [MockIngredient(), MockIngredient()]

