import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:
    
    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = "black bun"
        bun_mock.get_price.return_value = 100
        
        burger.set_buns(bun_mock)
        
        assert burger.bun == bun_mock

    @pytest.mark.parametrize("type_ing, name_ing, price_ing", [
        ("SAUCE", "hot sauce", 100),
        ("FILLING", "cutlet", 100)
    ])
    def test_add_ingredient(self, type_ing, name_ing, price_ing):
        burger = Burger()
        ing_mock = Mock(spec=Ingredient)
        ing_mock.get_type.return_value = type_ing
        ing_mock.get_name.return_value = name_ing
        ing_mock.get_price.return_value = price_ing
        
        burger.add_ingredient(ing_mock)
        
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)
        
        ing_mock = Mock(spec=Ingredient)
        ing_mock.get_price.return_value = 50
        burger.add_ingredient(ing_mock)
        
        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = "black bun"
        bun_mock.get_price.return_value = 100  # ДОБАВИЛИ ЦЕНУ
        burger.set_buns(bun_mock)
        
        ing_mock = Mock(spec=Ingredient)
        ing_mock.get_type.return_value = "SAUCE"
        ing_mock.get_name.return_value = "hot sauce"
        ing_mock.get_price.return_value = 50   # ДОБАВИЛИ ЦЕНУ
        burger.add_ingredient(ing_mock)
        
        receipt = burger.get_receipt()
        
        # ИСПРАВЛЕНИЕ: точная проверка вместо проверки через in
        expected_receipt = '''(==== black bun ====)
SAUCE is hot sauce
(==== black bun ====)

Price: 250'''
        assert receipt == expected_receipt, f"Ожидался чек:\n{expected_receipt}\nПолучен:\n{receipt}"
