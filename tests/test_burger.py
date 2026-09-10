import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BUNS, INGREDIENT_TYPE_FILLING, ALL_INGREDIENTS


class TestBurger:

    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_set_buns_correct(self, bun_name, bun_price, burger):

        my_bun = Bun(bun_name, bun_price)

        burger.set_buns(my_bun)

        assert burger.bun == my_bun


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_name_check(self, bun_name, bun_price, burger):
            
            my_bun = Bun(bun_name, bun_price)
    
            burger.set_buns(my_bun)
    
            assert burger.bun.get_name() == bun_name


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_set_buns_price_check(self, bun_name, bun_price, burger):
            
            my_bun = Bun(bun_name, bun_price)
    
            burger.set_buns(my_bun)
    
            assert burger.bun.get_price() == bun_price



    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_added_success(self, ingredient_type, name, price, burger):

        my_ingredient = Ingredient(ingredient_type, name, price)

        burger.add_ingredient(my_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == my_ingredient



    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_type_check(self, ingredient_type, name, price, burger):
        
        my_ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(my_ingredient)
        
        assert burger.ingredients[0].get_type() == ingredient_type


    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_name_check(self, ingredient_type, name, price, burger):
    
        my_ingredient = Ingredient(ingredient_type, name, price)
    
        burger.add_ingredient(my_ingredient)
    
        assert burger.ingredients[0].get_name() == name


    @pytest.mark.parametrize("ingredient_type, name, price", ALL_INGREDIENTS)
    def test_add_ingredient_price_check(self, ingredient_type, name, price, burger):
        
        my_ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(my_ingredient)
        
        assert burger.ingredients[0].get_price() == price


    def test_add_ingredient_add_two_ingredients(self, burger):

        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)

        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)


        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == my_ingredient_1
        assert burger.ingredients[1] == my_ingredient_2



    def test_remove_ingredient_from_burger(self, burger):
        
        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)

        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    
    def test_move_ingredient_ingredient_forward(self, burger):

        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)
        my_ingredient_3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)

        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)
        burger.add_ingredient(my_ingredient_3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [my_ingredient_2, my_ingredient_3, my_ingredient_1]

    def test_move_ingredient_ingredient_backward(self, burger):
    
        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)
        my_ingredient_3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)
        
        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)
        burger.add_ingredient(my_ingredient_3)
        
        burger.move_ingredient(2, 0)
        
        assert burger.ingredients == [my_ingredient_3, my_ingredient_1, my_ingredient_2]


    def test_move_ingredient_ingredient_same_position(self, burger):
        
        my_ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        my_ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)
        my_ingredient_3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)
            
        burger.add_ingredient(my_ingredient_1)
        burger.add_ingredient(my_ingredient_2)
        burger.add_ingredient(my_ingredient_3)
            
        burger.move_ingredient(0, 0)
            
        assert burger.ingredients == [my_ingredient_1, my_ingredient_2, my_ingredient_3]



    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_price_price_burger_without_ingredients(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        burger.set_buns(mock_bun)

        expected_price = bun_price * 2
        actual_price = burger.get_price()

        assert expected_price == actual_price


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_price_burger_with_one_ingredient(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 90
        burger.add_ingredient(mock_ingredient)


        expected_price = bun_price * 2 + 90
        actual_price = burger.get_price()

        assert expected_price == actual_price


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_price_burger_with_multiple_ingredients(self, bun_name, bun_price, burger):


        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price 
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_1.get_price.return_value = 90
        mock_ingredient_2.get_price.return_value = 1337
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        
        expected_price = bun_price * 2 + 90 + 1337
        actual_price = burger.get_price()

        assert expected_price == actual_price


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_receipt_without_ingredients(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = bun_name
        burger.set_buns(mock_bun)
        
        expected_price = bun_price * 2
        expected_receipt = f"(==== {bun_name} ====)\n(==== {bun_name} ====)\n\nPrice: {expected_price}"

        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_receipt_with_one_ingredient(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = bun_name
        burger.set_buns(mock_bun)


        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Соус Spicy-X"
        mock_ingredient.get_price.return_value = 90        
        burger.add_ingredient(mock_ingredient)
        
        expected_price = bun_price * 2 + 90
        expected_receipt = f"(==== {bun_name} ====)\n= sauce Соус Spicy-X =\n(==== {bun_name} ====)\n\nPrice: {expected_price}"

        assert burger.get_receipt() == expected_receipt


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_receipt_with_multiple_ingredients(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = bun_name
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_1.get_type.return_value = "SAUCE"
        mock_ingredient_1.get_name.return_value = "Соус Spicy-X"
        mock_ingredient_1.get_price.return_value = 90 

        mock_ingredient_2.get_type.return_value = "FILLING"
        mock_ingredient_2.get_name.return_value = "Мясо бессмертных моллюсков Protostomia"
        mock_ingredient_2.get_price.return_value = 1337
    
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        expected_price = bun_price * 2 + 90 + 1337
        expected_receipt = f"(==== {bun_name} ====)\n= sauce Соус Spicy-X =\n= filling Мясо бессмертных моллюсков Protostomia =\n(==== {bun_name} ====)\n\nPrice: {expected_price}"
        
        assert burger.get_receipt() == expected_receipt


    @pytest.mark.parametrize("bun_name, bun_price", BUNS)
    def test_get_receipt_actual_price_check(self, bun_name, bun_price, burger):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 90 
        burger.add_ingredient(mock_ingredient)

        expected_price = bun_price * 2 + 90
        receipt = burger.get_receipt()

        assert f"Price: {expected_price}" in receipt