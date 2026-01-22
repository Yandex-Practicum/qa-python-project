import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    @pytest.mark.parametrize("name, price", [("black bun", 100),("white bun", 200),])
    def test_set_buns_sets_bun_successfully(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun is bun

    @pytest.mark.parametrize("type, name, price", [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),(INGREDIENT_TYPE_FILLING, "cutlet", 100),(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),])
    def test_add_ingredient_successfully(self, type, name, price):
        burger = Burger()
        ingredient = Ingredient(type, name, price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_removes_ingredient_by_index_successfully(self):
        burger = Burger()
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        dinosaur = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(dinosaur)
        burger.add_ingredient(sauce)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert cutlet in burger.ingredients
        assert sauce in burger.ingredients
        assert dinosaur not in burger.ingredients

    def test_move_ingredient_moves_ingredient_by_index_successfully(self):
        burger = Burger()
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        dinosaur = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        hot_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(dinosaur)
        burger.add_ingredient(hot_sauce)
        burger.move_ingredient(2,3)
        assert len(burger.ingredients) == 4
        assert burger.ingredients[0] is sauce
        assert burger.ingredients[1] is cutlet
        assert burger.ingredients[2] is hot_sauce
        assert burger.ingredients[3] is dinosaur

  
    @pytest.mark.parametrize('bun_name, bun_price, ingredients_data, expected_price', 
                            [("black bun", 100, [(INGREDIENT_TYPE_FILLING, "cutlet", 100)], 300),
                             ("black bun", 100, [], 200),
                             ("white bun", 200, [(INGREDIENT_TYPE_FILLING, "dinosaur", 200), (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)], 700)])
    def test_get_price_cost_of_a_ready_made_burger(self, bun_name, bun_price, ingredients_data, expected_price ):
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)

        for type, name, price in ingredients_data:
            ingredient = Ingredient(type, name, price)
            burger.add_ingredient(ingredient)
        
        price = burger.get_price()
        assert price == expected_price


    def test_get_receipt_uses_mocked_bun_and_ingredient(self):
        bun="red bun"
        bun_price=300

        ingredient_type=INGREDIENT_TYPE_FILLING
        ingredient_name="cutlet"
        ingredient_price=200        

        mock_bun = Mock()
        mock_bun.get_name.return_value = bun
        mock_bun.get_price.return_value = bun_price

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected = f"(==== {bun} ====)\n= {ingredient_type.lower()} {ingredient_name} =\n(==== {bun} ====)\n\nPrice: {bun_price*2 + ingredient_price}"
        assert receipt == expected