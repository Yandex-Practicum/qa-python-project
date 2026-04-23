import pytest
from praktikum.database import Database
from praktikum.burger import Burger


class TestPraktikum:
    
    def test_main_functionality(self):
        """Тест: проверка основной логики из praktikum.py"""
        db = Database()
        burger = Burger()
        
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        
        assert len(buns) > 0
        assert len(ingredients) > 0
        
        burger.set_buns(buns[0])
        assert burger.bun is not None
        
        burger.add_ingredient(ingredients[0])
        assert len(burger.ingredients) == 1
        
        price = burger.get_price()
        assert price > 0
        
        receipt = burger.get_receipt()
        assert "Price:" in receipt
        assert "(====" in receipt
    
    def test_move_ingredient(self):
        """Тест: перемещение ингредиента"""
        db = Database()
        burger = Burger()
        
        burger.set_buns(db.available_buns()[0])
        ingredients = db.available_ingredients()[:3]
        
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        original_order = [burger.ingredients[0], burger.ingredients[1], burger.ingredients[2]]
        
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[2] == original_order[0]
    
    def test_remove_ingredient(self):
        """Тест: удаление ингредиента"""
        db = Database()
        burger = Burger()
        
        burger.set_buns(db.available_buns()[0])
        ingredients = db.available_ingredients()[:2]
        
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        initial_length = len(burger.ingredients)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == initial_length - 1
    
    def test_main_function_runs(self):
        """Тест: вызов функции main() из praktikum.py"""
        from praktikum.praktikum import main
        
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() raised an exception: {e}")