import pytest
import allure
from praktikum.burger import Burger


@allure.feature("Burger Operations")
class TestBurger:

    @allure.title('Adding one ingredient')
    def test_add_ingredient_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    @allure.title("Removing an ingredient")
    def test_remove_ingredient_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
    
    @allure.title('Moving an ingredient')
    def test_move_ingredient_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        ing1 = mock_ingredient
        ing2 = mock_ingredient
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    @pytest.mark.parametrize(
        'bun_price, ingredient_price, expected_price',
        [
            (100, 50, 250),  # 100*2 + 50
            (0, 200, 200),   # 0*2 + 200
        ]
    )

    @allure.title('Calculating the price')
    def test_get_price_success(self, mock_bun, mock_ingredient, bun_price, ingredient_price, expected_price):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price


    @pytest.mark.parametrize(
        "bun_name, ingredient_name, ingredient_type, bun_price, ingredient_price, expected_receipt",
        [
            (
                "Булка", "Сыр", "ингредиент", 100, 50,
                "(==== Булка ====)\n= ингредиент Сыр =\n(==== Булка ====)\n\nPrice: 250"
            ),
            (
                "Булочка", "Соус", "ингредиент", 80, 20,
                "(==== Булочка ====)\n= ингредиент Соус =\n(==== Булочка ====)\n\nPrice: 180"
            ),
        ]
    )

    @allure.title('Getting a full receipt')
    def test_get_receipt_success(
        self, mock_bun, mock_ingredient, bun_name, ingredient_name, ingredient_type, bun_price, ingredient_price, expected_receipt):
        
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert receipt == expected_receipt
