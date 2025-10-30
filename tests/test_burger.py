import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    
    def setup_method(self):
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient2 = Mock(spec=Ingredient)
    
    def test_set_buns(self):
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun
    
    def test_add_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1
    
    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient2
    
    def test_remove_ingredient_index_error(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(5)
    
    def test_move_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == self.mock_ingredient2
        assert self.burger.ingredients[1] == self.mock_ingredient1
    
    def test_move_ingredient_same_position(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        original_order = self.burger.ingredients.copy()
        self.burger.move_ingredient(0, 0)
        assert self.burger.ingredients == original_order
    
    def test_move_ingredient_index_error(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        
        with pytest.raises(IndexError):
            self.burger.move_ingredient(5, 0)
    
    def test_get_price_with_bun_and_ingredients(self):
        self.mock_bun.get_price.return_value = 1255
        self.mock_ingredient1.get_price.return_value = 3000
        self.mock_ingredient2.get_price.return_value = 4400
        
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        expected_price = 1255 * 2 + 3000 + 4400 
        assert self.burger.get_price() == expected_price
    
    def test_get_price_only_bun(self):
        self.mock_bun.get_price.return_value = 988
        
        self.burger.set_buns(self.mock_bun)
        
        assert self.burger.get_price() == 1976 
    
    def test_get_price_no_bun_raises_error(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.mock_ingredient1.get_price.return_value = 424
        
        # Бургер без булки должен вызывать ошибку
        with pytest.raises(AttributeError):
            self.burger.get_price()
    
    def test_get_receipt_with_bun_and_ingredients(self):
        self.mock_bun.get_name.return_value = "Краторная булка N-200i"
        self.mock_bun.get_price.return_value = 1255
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "Соус Spicy-X"
        mock_sauce.get_price.return_value = 90
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "Говяжий метеорит (отбивная)"
        mock_filling.get_price.return_value = 3000
        
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)
        
        receipt = self.burger.get_receipt()
        
        expected_lines = [
            "(==== Краторная булка N-200i ====)",
            "= sauce Соус Spicy-X =",
            "= filling Говяжий метеорит (отбивная) =", 
            "(==== Краторная булка N-200i ====)",
            "",
            "Price: 5600"
        ]
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt
    
    def test_get_receipt_only_bun(self):
        self.mock_bun.get_name.return_value = "Флюоресцентная булка R2-D3"
        self.mock_bun.get_price.return_value = 988
        
        self.burger.set_buns(self.mock_bun)
        
        receipt = self.burger.get_receipt()
        
        expected_lines = [
            "(==== Флюоресцентная булка R2-D3 ====)",
            "(==== Флюоресцентная булка R2-D3 ====)",
            "",
            "Price: 1976"
        ]
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt
    
    def test_get_receipt_no_bun_raises_error(self):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Соус традиционный галактический"
        mock_ingredient.get_price.return_value = 15
        
        self.burger.add_ingredient(mock_ingredient)
        
        # Бургер без булки должен вызывать ошибку
        with pytest.raises(AttributeError):
            self.burger.get_receipt()
    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (1255, [3000, 4400], 9910),
        (988, [], 1976),
        (200, [100], 500),
    ])
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected_total):
        self.mock_bun.get_price.return_value = bun_price
        self.burger.set_buns(self.mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            self.burger.add_ingredient(mock_ingredient)
        
        assert self.burger.get_price() == expected_total
    
    def test_get_receipt_with_russian_ingredients(self):
        self.mock_bun.get_name.return_value = "Краторная булка N-200i"
        self.mock_bun.get_price.return_value = 1255
        
        mock_ingredients = [
            ("Соус Spicy-X", INGREDIENT_TYPE_SAUCE, 90),
            ("Говяжий метеорит (отбивная)", INGREDIENT_TYPE_FILLING, 3000),
            ("Биокотлета из марсианской Магнолии", INGREDIENT_TYPE_FILLING, 424),
            ("Хрустящие минеральные кольца", INGREDIENT_TYPE_FILLING, 300)
        ]
        
        self.burger.set_buns(self.mock_bun)
        
        for name, ing_type, price in mock_ingredients:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_name.return_value = name
            mock_ingredient.get_type.return_value = ing_type
            mock_ingredient.get_price.return_value = price
            self.burger.add_ingredient(mock_ingredient)
        
        receipt = self.burger.get_receipt()
        
        assert "Краторная булка N-200i" in receipt
        assert "Соус Spicy-X" in receipt
        assert "Говяжий метеорит (отбивная)" in receipt
        assert "Биокотлета из марсианской Магнолии" in receipt
        assert "Хрустящие минеральные кольца" in receipt
        assert "Price: 6324" in receipt 
    
    def test_get_price_with_zero_bun_price(self):
        """Тест с нулевой ценой булки"""
        self.mock_bun.get_price.return_value = 0
        self.mock_ingredient1.get_price.return_value = 424
        self.mock_ingredient2.get_price.return_value = 762
        
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        # 0*2 + 424 + 762 = 1186
        assert self.burger.get_price() == 1186