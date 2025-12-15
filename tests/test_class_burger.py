import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    #Проверка конструктора
    def test_init_creates_empty_burger(self):

        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    #Название и цена булочки
    def test_set_buns_correctly(self):

        burger = Burger()
        mock_bun = Mock()

        mock_bun.get_name.return_value = "tastybun"
        mock_bun.get_price.return_value = 99.9

        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    #Добавка ингредиентов
    def test_add_ingredient_to_list(self):

        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "tastybun"
        mock_ingredient.get_price.return_value = 99.9
        mock_ingredient.get_type.return_value = "Малина"
        
        burger.add_ingredient(mock_ingredient)
        
        assert burger.ingredients[0] == mock_ingredient

    #Удаление ингредиентов
    def test_remove_ingredient_correctly(self):

        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "tastybun"
        mock_ingredient.get_price.return_value = 99.9
        mock_ingredient.get_type.return_value = "Малина"

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "tastybun2"
        mock_ingredient2.get_price.return_value = 89.9
        mock_ingredient2.get_type.return_value = "Клубника"
        
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        
        assert burger.ingredients[0] == mock_ingredient2

    #Перемещение ингредиентов
    def test_move_ingredient(self):
        burger = Burger()

        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()

        mock_ingredient1.get_name.return_value = "tastybun"
        mock_ingredient2.get_name.return_value = "tastybun1"
        mock_ingredient3.get_name.return_value = "tastybun2"
        
    
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
    
        burger.move_ingredient(0, 2)
    
        assert burger.ingredients == [mock_ingredient2, mock_ingredient3, mock_ingredient1]


    #Цена булочки
    def test_get_price_with_only_bun(self):

        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 50.0
        
        burger.set_buns(mock_bun)
        
        assert burger.get_price() == 100.0
    
    #Цена булочки с добавками
    def test_get_price_with_bun_and_ingredients(self):

        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 30.0
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 20.0
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 15.0
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        expected_price = 30.0 * 2 + 20.0 + 15.0
        
        assert burger.get_price() == expected_price

    #Чек только булочки
    def test_get_receipt_with_only_bun(self):

        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "tastybun"
        mock_bun.get_price.return_value = 50.0
        
        burger.set_buns(mock_bun)
        
        receipt = burger.get_receipt()
        expected_lines = [
            "(==== tastybun ====)",
            "(==== tastybun ====)",
            "",
            "Price: 100.0"]
        
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt

    #Чек булочки с добавками
    def test_get_receipt_with_bun_and_ingredients(self):
    
        burger = Burger()
    
        mock_bun = Mock()
        mock_bun.get_name.return_value = "tastybun"
        mock_bun.get_price.return_value = 40.0
    
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = "SAUCE"
        mock_sauce.get_name.return_value = "острый соус"
        mock_sauce.get_price.return_value = 10.0
    
        mock_filling = Mock()
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_name.return_value = "котлета"
        mock_filling.get_price.return_value = 30.0
    
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
    
        receipt = burger.get_receipt()

        expected_receipt = (
        "(==== tastybun ====)\n"
        "= sauce острый соус =\n"
        "= filling котлета =\n"
        "(==== tastybun ====)\n\n"
        "Price: 120.0")
    
        assert receipt == expected_receipt

