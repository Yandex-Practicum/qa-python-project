from burger import Burger
from unittest.mock import Mock
import pytest

class TestBurgerMethods:

    def test_burger_bun_true(self):
        burger = Burger()
        burger.bun = "red bun"
        assert burger.bun == "red bun"

    def test_burger_ingredient_true(self):
        burger = Burger()
        burger.ingredients.append(1)
        assert burger.ingredients == [1]


    def test_burger_set_buns_true(self):
        burger = Burger()
        burger.set_buns("black bun")

        assert burger.bun == "black bun"



    @pytest.mark.parametrize(
        "ingredients, expected_result",
        [
            (["chili sauce"], ["chili sauce"]),
            (["chili sauce", "hot sauce"], ["chili sauce", "hot sauce"]),
            (["chili sauce", "hot sauce", "sour cream"], ["chili sauce", "hot sauce", "sour cream"])
        ],
        ids=[
            "single_ingredient",
            "two_ingredients",
            "three_ingredients",
        ]
    )
    def test_add_ingredients(self, ingredients, expected_result):
        """Параметризованный тест добавления ингредиентов."""
        burger = Burger()

        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.ingredients == expected_result


    def test_burger_remove_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient("chili sauce")
        burger.add_ingredient("hot sauce")
        burger.remove_ingredient(0)

        assert burger.ingredients == ["hot sauce"]

    def test_burger_move_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient("chili sauce")
        burger.add_ingredient("hot sauce")
        burger.move_ingredient(0,1)

        assert burger.ingredients == ["hot sauce" , "chili sauce"]

    def test_burger_get_price_true(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 10

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 20

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        assert burger.get_price() == 50 * 2 + 10 + 20


    def test_burger_get_receipt_true(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "red bun"

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "cutlet"

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        burger.get_price = Mock(return_value=300)

        assert burger.get_receipt() == "(==== red bun ====)\n= filling cutlet =\n(==== red bun ====)\n\nPrice: 300"

