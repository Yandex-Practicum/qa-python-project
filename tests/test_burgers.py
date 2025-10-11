import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_burger_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce

    def test_burger_remove_ingredient(self,burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling


    def test_burger_get_price(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert burger.get_price() == 1100

    def test_burger_get_receipt(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        receipt = burger.get_receipt()
        assert "red bun" in receipt
        assert "chili sauce" in receipt
        assert "filling dinosaur" in receipt
        assert "1100" in receipt


    @pytest.mark.parametrize(
        "ingredients, expected_price",
        [
            (["hot sauce", "cutlet"], 100),
            (["sour cream", "sausage"], 200),
            (["chili sauce", "dinosaur"], 300),
        ]
    )
    def test_burger_add_ingredient_parametrized(self, ingredients, expected_price):
        mock_buns = MagicMock(spec=Bun)
        mock_buns.get_price.return_value = 100
        mock_buns.get_name.return_value = "red bun"

        burger = Burger()
        burger.set_buns(mock_buns)

        for name_ingredient in ingredients:
            mock_ingredient = MagicMock(spec=Ingredient)
            mock_ingredient.get_name.return_value = name_ingredient
            mock_ingredient.get_price.return_value = 100
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING if name_ingredient != "hot sauce" else INGREDIENT_TYPE_SAUCE
            burger.add_ingredient(mock_ingredient)

        expected_total_price = mock_buns.get_price() * 2 + len(ingredients) * 100
        assert burger.get_price() == expected_total_price
