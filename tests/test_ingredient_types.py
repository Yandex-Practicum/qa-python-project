import pytest
from praktikum import ingredient_types

class TestIngredientTypes:

    def test_ingredient_types_constants(self):
        # Проверяем точное наличие и строковые значения констант из вашей заготовки
        assert ingredient_types.INGREDIENT_TYPE_SAUCE == 'SAUCE'
        assert ingredient_types.INGREDIENT_TYPE_FILLING == 'FILLING'
