from unittest.mock import Mock
from practikum.burger import Burger
from practikum.bun import Bun
from practikum.ingredient import Ingredient


class TestBurger:
        def test_burger_price(self):
            bun = Mock(spec=Bun)
            bun.get_price.return_value = 100
            ingredient1 = Mock(spec=Ingredient)
            ingredient1.get_price.return_value = 50
            ingredient2 = Mock(spec=Ingredient)
            ingredient2.get_price.return_value = 75

            burger = Burger()
            burger.set_buns(bun)
            burger.add_ingredient(ingredient1)
            burger.add_ingredient(ingredient2)

            assert burger.get_price() == 325  # 100*2 + 50 + 75


        def test_burger_receipt(self):
            bun = Mock(spec=Bun)
            bun.get_name.return_value = "black bun"
            bun.get_price.return_value = 100
            ingredient = Mock(spec=Ingredient)
            ingredient.get_name.return_value = "cutlet"
            ingredient.get_type.return_value = "FILLING"
            ingredient.get_price.return_value = 100

            burger = Burger()
            burger.set_buns(bun)
            burger.add_ingredient(ingredient)

            receipt = burger.get_receipt()
            assert "(==== black bun ====)" and "= filling cutlet =" and "Price: 300" in receipt
