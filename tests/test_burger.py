from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun  
from praktikum.ingredient import Ingredient  


class TestBurger:


    def test_set_buns_adds_bun(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0  
        
        burger.set_buns(mock_bun)
        
        assert burger.get_price() == 200.0

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 0.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 50.0  
        
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == 50.0

    def test_remove_ingredient_clears_list(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 0.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 50.0
        
        burger.add_ingredient(mock_ingredient)
        
        burger.remove_ingredient(0)
        
        assert burger.get_price() == 0.0

    def test_move_ingredient_swaps_positions(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 0.0
        burger.set_buns(mock_bun)

        mock_ing1 = Mock(spec=Ingredient)
        mock_ing1.get_name.return_value = "соус"
        mock_ing1.get_type.return_value = "SAUCE"
        mock_ing1.get_price.return_value = 0.0
        
        mock_ing2 = Mock(spec=Ingredient)
        mock_ing2.get_name.return_value = "котлета"
        mock_ing2.get_type.return_value = "FILLING"
        mock_ing2.get_price.return_value = 0.0

        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        
        burger.move_ingredient(0, 1)
        
        receipt = burger.get_receipt()
        assert receipt.index("котлета") < receipt.index("соус")


    @pytest.mark.parametrize(
        "bun_price, ingredient_price, expected_total",
        [
            (100.0, 50.0, 250.0),
            (0.0, 10.0, 10.0),
            (250.5, 0.0, 501.0),
            (150.0, 100.0, 400.0),
        ],
    )
    def test_get_price_calculation(
        self, bun_price, ingredient_price, expected_total
    ):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_total

    @pytest.mark.parametrize(
        "bun_name, bun_price, ing_type, ing_name, ing_price, expected_total_price",
        [
            ("Краторная булка", 100.0, "SAUCE", "чили", 50.0, 250.0),
            ("Супер булка", 100.0, "FILLING", "биг котлета", 150.0, 350.0),
        ],
    )
    def test_get_receipt_formatting(
        self, bun_name, bun_price, ing_type, ing_name, ing_price, expected_total_price
    ):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = ing_type
        mock_ingredient.get_name.return_value = ing_name
        mock_ingredient.get_price.return_value = ing_price
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"= {ing_type.lower()} {ing_name} =\n"
            f"(==== {bun_name} ====)\n\n"
            f"Price: {expected_total_price}"
        )
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_ingredients(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Марсианская булка"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        expected_receipt = (
            f"(==== Марсианская булка ====)\n"
            f"(==== Марсианская булка ====)\n\n"
            f"Price: 200.0"
        )
        assert burger.get_receipt() == expected_receipt
