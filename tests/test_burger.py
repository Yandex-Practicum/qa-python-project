from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_set_buns_sets_bun(self, bun):
        
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_item_to_list(self, ingredient_main):
        
        burger = Burger()
        burger.add_ingredient(ingredient_main)

        assert burger.ingredients == [ingredient_main]

    def test_remove_ingredient_removes_item_by_index(self, ingredient_main, ingredient_sauce):
        
        burger = Burger()
        burger.add_ingredient(ingredient_main)
        burger.add_ingredient(ingredient_sauce)
        burger.remove_ingredient(0)

        assert burger.ingredients == [ingredient_sauce]

    def test_move_ingredient_moves_item_to_new_index(self, ingredient_main, ingredient_sauce):
        
        second_ingredient = Mock()
        second_ingredient.get_price.return_value = 100
        second_ingredient.get_name.return_value = 'Сыр с астероидной плесенью'
        second_ingredient.get_type.return_value = 'Начинка'

        burger = Burger()
        burger.add_ingredient(ingredient_main)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(2, 0)

        assert burger.ingredients == [second_ingredient, ingredient_main, ingredient_sauce]

    def test_get_price_returns_sum_of_bun_and_ingredients_prices(self):
       
        bun = Mock()
        bun.get_price.return_value = 100

        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 50

        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 25

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == 275

    def test_get_receipt_returns_expected_string(self):
        
        bun = Mock()
        bun.get_name.return_value = 'Булка'
        bun.get_price.return_value = 100

        ingredient = Mock()
        ingredient.get_type.return_value = 'Соус'
        ingredient.get_name.return_value = 'Соус Spicy-X'
        ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected = '(==== Булка ====)\n= соус Соус Spicy-X =\n(==== Булка ====)\n\nPrice: 250'

        assert burger.get_receipt() == expected