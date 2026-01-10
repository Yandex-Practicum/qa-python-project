from praktikum.burger import Burger
from praktikum.database import Database

class TestBurger:

    def test_set_buns_add_bun(self, mock_bun_name_price):
        burger = Burger()
        bun = mock_bun_name_price
        burger.set_buns(bun)
        assert burger.bun.name == "black bun"

    def test_add_ingredient_check_name(self, mock_ingredient_type_name_price):
        burger = Burger()
        ingredient = mock_ingredient_type_name_price
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].name == "hot sauce"

    def test_remove_ingredient_remove_one_ingredient(self,mock_ingredient_type_name_price):
        burger = Burger()
        ingredient = mock_ingredient_type_name_price
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_change_two_ingredients(self):
        burger = Burger()
        available_ingredients = Database()
        burger.add_ingredient(available_ingredients.ingredients[0])
        burger.add_ingredient(available_ingredients.ingredients[1])
        burger.move_ingredient(0,1)
        assert burger.ingredients[0].name == "sour cream"

    def test_get_price_check_price(self):
        burger = Burger()
        available_ingredients = Database()
        burger.set_buns(available_ingredients.buns[0])
        burger.add_ingredient(available_ingredients.ingredients[0])
        assert burger.get_price() == 300

    def test_get_receipt_check_receipt_price(self):
        burger = Burger()
        available_ingredients = Database()
        burger.set_buns(available_ingredients.buns[0])
        burger.add_ingredient(available_ingredients.ingredients[0])
        assert "Price: 300" in burger.get_receipt()