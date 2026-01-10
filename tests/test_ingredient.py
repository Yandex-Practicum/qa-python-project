import pytest
from praktikum.praktikum import Ingredient


class TestIngridient:

    @pytest.mark.parametrize("type_ingredient", ["Соус", "Начинка", "Sauce", "Filling"])
    def test_get_price_ingredient(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, "Соус Spicy-X", 99.9)
        assert ingredient.get_type() == type_ingredient

    @pytest.mark.parametrize("name_ingredient", ["Соус Spicy-X", "Соус с шипами Антарианского плоскоходца",
                                                 "Мясо бессмертных моллюсков Protostomia", "Мини-салат Экзо-Плантаго"])
    def test_get_name_ingredient(self, name_ingredient):
        ingredient = Ingredient("type", name_ingredient, 99.9)
        assert ingredient.get_name() == name_ingredient

    @pytest.mark.parametrize("price_ingredient", [99.9, 100, 1000000.1, 1.000001])
    def test_get_price_ingredient(self, price_ingredient):
        ingredient = Ingredient("type", "ingredient", price_ingredient)
        assert ingredient.get_price() == price_ingredient
