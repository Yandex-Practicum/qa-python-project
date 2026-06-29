import pytest

from unittest.mock import Mock

from praktikum.bun import Bun 
from praktikum.burger import Burger 
from praktikum.ingredient import Ingredient

class TestBurger:
    #проверка метода выбора булочки
    def test_set_buns(self,burger: Burger, bun: Bun):    

        burger.set_buns(bun)
       
        assert burger.bun == bun

    #проверка метода добавления ингредиента    
    def test_add_ingredient(self, burger: Burger, ingredient1: Ingredient):

        burger.add_ingredient(ingredient1)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient1

    #проверка метода удаления ингредиента
    def test_remove_ingredient(self, burger: Burger, ingredient1: Ingredient):

        burger.add_ingredient(ingredient1)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients
    
    #проверка метода перемещения ингредиента
    def test_move_ingredient(self, burger: Burger, ingredient1: Ingredient, ingredient2: Ingredient, ingredient3: Ingredient):

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[2] == ingredient1
    
    #проверка метода подсчета стоимости
    @pytest.mark.parametrize(
        "bun_price, ingredient_price",
        [
        (200, []), #проверяется булка без наполнителя 
        (200, [100]), #проверяется булка и один ингредиент  
        (300, [200, 300]) #проверяется булка и два ингредиента  
        ]
    )
    def test_get_price(self, burger: Burger, bun_price, ingredient_price):

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_price:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        expected_price = bun_price * 2 + sum(ingredient_price)

        assert burger.get_price() == expected_price

    #проверка метода конечного состава бургера и его стоимости
    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredients_data",
        [
        ("white bun", 200, []), #проверяется булка без наполнителя 
        ("black bun", 100, [("SAUCE", "hot sauce", 100)]), #проверяется булка и один ингредиент  
        ("red bun", 300, [("SAUCE", "hot sauce", 100), ("FILLING", "dinosaur", 200)]) #проверяется булка и два ингредиента  
        ]
    )
    def test_get_receipt(self, burger: Burger, bun_name, bun_price, ingredients_data):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for ingredient_type, ingredient_name, ingredient_price in ingredients_data:
            mock_ingredient = Mock()
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_price.return_value = ingredient_price
            burger.add_ingredient(mock_ingredient)

        expected_price = bun_price * 2 + sum(
            price for _, _, price in ingredients_data
        )

        bun_top_lines = [f"(==== {bun_name} ====)"]

        for ingredient_type, ingredient_name, _ in ingredients_data:
            bun_top_lines.append(f"= {ingredient_type.lower()} {ingredient_name} =")

        bun_top_lines.append(f"(==== {bun_name} ====)\n")
        bun_top_lines.append(f"Price: {expected_price}")

        expected_answer = "\n".join(bun_top_lines)

        assert burger.get_receipt() == expected_answer