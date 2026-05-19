import pytest
from unittest.mock import Mock
import allure 
from praktikum.burger import Burger

class TestBurger:
    
    
    @allure.title('Новый бургер не имеет булочки и ингредиентов')
    def test_new_burger_is_empty(self):

        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 0
        mock_bun.get_name.return_value = "without_bun"
        burger.set_buns(mock_bun)
        
        assert burger.get_price() == 0
        

    @allure.title('Проверка, можно ли установить булочку для бургера')
    def test_set_buns(self):

        burger = Burger()
        mock_bun = Mock()
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    @allure.title('Можно добавить ингредиент в бургер')
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        
        burger.add_ingredient(mock_ingredient)
        
        assert burger.ingredients[0] == mock_ingredient

    @allure.title('Можно удалить ингредиент из списка')
    def test_remove_ingredient(self):

        burger = Burger()
        first_ingredient = Mock()
        second_ingredient = Mock()

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        
        burger.remove_ingredient(0)
        
        assert burger.ingredients[0] == second_ingredient

    @allure.title('Перемещение ингредиента на другую позицию')
    def test_move_ingredient(self):

        burger = Burger()
        first_ingredient = Mock()
        second_ingredient = Mock()
        third_ingredient = Mock()

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.add_ingredient(third_ingredient)

        burger.move_ingredient(2, 1)

        assert burger.ingredients == [first_ingredient, third_ingredient, second_ingredient]

    @allure.title('Рассчет стоимости булочек')
    def test_get_bun_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        price = burger.get_price()
        
        assert price == 200


    @allure.title('Рассчет стоимости бургера')
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected", [
        (100, [10, 20], 230),
        (100, [10, 20, 30], 260),
        (50, [5, 5, 5, 5], 120),
        (100, [], 200),
    ])
    def test_get_burger_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected
    
    @allure.title('Рецепт с разными ингредиентами и типами ингредиентов')
    @pytest.mark.parametrize("bun_name, ingredient_type, ingredient_name, expected_line", [
    ("Флюоресцентная булка", "sauce", "Spicy-X", "= sauce Spicy-X ="),
    ("Краторная булка", "filling", "Говяжий метеорит", "= filling Говяжий метеорит ="),
    ("Краторная булка", "sauce", "Space Sauce", "= sauce Space Sauce ="),
    ])
    def test_receipt_with_different_ingredients(self, bun_name, ingredient_type, ingredient_name, expected_line):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100  
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = 50  
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert expected_line in receipt
