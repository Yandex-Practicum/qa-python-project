import pytest

from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:


    def test_set_buns_succsess(self):
        burger = Burger()
        test_bun = Bun("Origin bun",50)
        burger.set_buns(test_bun)
        assert burger.bun == test_bun


    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_FILLING,"chicken",100),
        (INGREDIENT_TYPE_FILLING,"meet",120),       
        (INGREDIENT_TYPE_SAUCE, "salsa", 50),
        (INGREDIENT_TYPE_SAUCE, "ancle bens", 60)    
        ])    
    def test_add_ingredient_several_succsess(self,ingredient_type, name, price):
        burger = Burger()
        bun = Bun("Origin Bun", 40)
        burger.set_buns(bun) 

        initial_count=  len(burger.ingredients)      
        ingredient = Ingredient( ingredient_type,name,price)
        burger.add_ingredient(ingredient)
        final_count = len(burger.ingredients)
        assert final_count == initial_count + 1
        assert ingredient in burger.ingredients


    def test_rremove_ingredient_only_one_leaves_empty_list(self):

        burger = Burger()
        burger.set_buns(Bun("Origin Bun", 40))
        
        one_ing= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        burger.add_ingredient(one_ing)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0
        assert one_ing not in burger.ingredients


    def test_remove_ingredient_from_empty_list_wait_error(self):

        burger = Burger()
        burger.set_buns(Bun("Origin Bun", 40))
     
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_remove_ingredient_for_index_del_correctly_ingredient(self):

        burger = Burger()
        burger.set_buns(Bun("Origin Bun", 40))
        
        first_ing= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        second_ing= Ingredient(INGREDIENT_TYPE_SAUCE, "salsa", 50)
        burger.add_ingredient(first_ing)
        burger.add_ingredient(second_ing)        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert first_ing not in burger.ingredients
 
    def test_move_ingredient_single_to_new_position(self):
        burger = Burger()
        burger.set_buns(Bun("Origin Bun", 40))

        ing1= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        ing2= Ingredient(INGREDIENT_TYPE_SAUCE, "salsa", 50)
        ing3 = Ingredient(INGREDIENT_TYPE_FILLING,"meet",120)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 1)

        moved_ingredients = burger.ingredients
        assert len(moved_ingredients) == 3
        assert moved_ingredients[0] is ing2
        assert moved_ingredients[1] is ing1
        assert moved_ingredients[2] is ing3

    def test_move_ingredient_from_bad_position_wait_error(self):
        burger = Burger()
        burger.set_buns(Bun("Origin Bun", 40))

        ing1= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        ing2= Ingredient(INGREDIENT_TYPE_SAUCE, "salsa", 50)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        with pytest.raises(IndexError):
            burger.move_ingredient(5,0)

    def test_get_price_includes_bun_twice_and_ingredients(self):
        burger = Burger()
        bun =Bun("Origin Bun", 40)
        burger.set_buns(bun)

        ing1= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        ing2= Ingredient(INGREDIENT_TYPE_SAUCE, "salsa", 50)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        expected_price = (bun.get_price() * 2) + ing1.get_price() + ing2.get_price()

        assert burger.get_price() == expected_price

    def test_get_receipt_full_content(self):
        burger = Burger()
        bun =Bun("Origin Bun", 40)
        burger.set_buns(bun)

        ing1= Ingredient(INGREDIENT_TYPE_FILLING,"chicken",100)
        ing2= Ingredient(INGREDIENT_TYPE_SAUCE, "salsa", 50)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()

        expected_lines: List[str] = [
            f'(==== {bun.get_name()} ====)',
            f'= {str(ing1.get_type()).lower()} {ing1.get_name()} =',
            f'= {str(ing2.get_type().lower())} {ing2.get_name()} =',  # исправлено: .lower() после get_type()
            f'(==== {bun.get_name()} ====)',
            "",                  
            f'Price: {burger.get_price()}',
        ]
        expected = '\n'.join(expected_lines)
        assert receipt == expected        