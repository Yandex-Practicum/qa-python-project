import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    
    def setup_method(self):
        #Подготовка данных перед каждым тестом
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "mock bun"
        self.mock_bun.get_price.return_value = 100
        
        self.mock_sauce = Mock(spec=Ingredient)
        self.mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.mock_sauce.get_name.return_value = "mock sauce"
        self.mock_sauce.get_price.return_value = 50
        
        self.mock_filling = Mock(spec=Ingredient)
        self.mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        self.mock_filling.get_name.return_value = "mock filling"
        self.mock_filling.get_price.return_value = 75
    
    def test_burger_initialization(self):
        #Проверка инициализации пустого бургера
        assert self.burger.bun is None
        assert len(self.burger.ingredients) == 0
    
    def test_set_buns(self):
        #Проверка установки булочек
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun
    
    def test_add_ingredient(self):
        #Проверка добавления ингредиента
        self.burger.add_ingredient(self.mock_sauce)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_sauce
    
    def test_remove_ingredient(self):
        #Проверка удаления ингредиента
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        self.burger.remove_ingredient(0)
        
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_filling
    
    def test_move_ingredient(self):
        #Проверка перемещения ингредиента
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        self.burger.move_ingredient(1, 0)
        
        assert self.burger.ingredients[0] == self.mock_filling
        assert self.burger.ingredients[1] == self.mock_sauce

    def test_get_price_with_bun_only(self):
        #Проверка расчета цены только с булочкой
        self.burger.set_buns(self.mock_bun)
        expected_price = self.mock_bun.get_price() * 2
        
        assert self.burger.get_price() == expected_price

    def test_get_price_with_ingredients(self):
        #Проверка расчета цены с ингредиентами
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
        
        expected_price = (self.mock_bun.get_price() * 2 + 
                         self.mock_sauce.get_price() + 
                         self.mock_filling.get_price())
        
        assert self.burger.get_price() == expected_price
    
    def test_get_receipt_with_bun_only(self):
        #Проверка формирования чека только с булочкой
        self.burger.set_buns(self.mock_bun)
    
        receipt = self.burger.get_receipt()
        expected_lines = [
            f"(==== {self.mock_bun.get_name()} ====)",
            f"(==== {self.mock_bun.get_name()} ====)",
            "",
            f"Price: {self.burger.get_price()}"
        ]
    
        assert receipt == "\n".join(expected_lines)
    
    def test_get_receipt_with_ingredients(self):
        #Проверка формирования чека с ингредиентами
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_sauce)
        self.burger.add_ingredient(self.mock_filling)
    
        receipt = self.burger.get_receipt()
    
        receipt_lines = [line for line in receipt.split('\n') if line != ""]
        expected_order = [
            f"(==== {self.mock_bun.get_name()} ====)",
            f"= sauce {self.mock_sauce.get_name()} =",
            f"= filling {self.mock_filling.get_name()} =",
            f"(==== {self.mock_bun.get_name()} ====)",
            f"Price: {self.burger.get_price()}"
        ]
        assert receipt_lines == expected_order
    