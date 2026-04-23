import pytest
from unittest.mock import Mock, MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    """Тесты для класса Burger"""

    def test_burger_init(self):
        """Тест инициализации бургера"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """Тест установки булочки"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.name = "test bun"
        mock_bun.price = 100
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun
        assert burger.bun.name == "test bun"


    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.name = "test ingredient"
        
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("ingredient_name,ingredient_price,ingredient_type", [
        ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        ("cutlet", 200, INGREDIENT_TYPE_FILLING),
        ("sour cream", 150, INGREDIENT_TYPE_SAUCE),
    ])
    def test_add_ingredient_multiple(self, ingredient_name, ingredient_price, ingredient_type):
        """Тест добавления нескольких ингредиентов"""
        burger = Burger()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == ingredient_name
        assert burger.ingredients[0].get_price() == ingredient_price

    def test_remove_ingredient(self):
        """Тест удаления ингредиента"""
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)
        
        burger.ingredients = [ingredient1, ingredient2, ingredient3]
        
        burger.remove_ingredient(1)
        
        assert len(burger.ingredients) == 2
        assert ingredient1 in burger.ingredients
        assert ingredient2 not in burger.ingredients
        assert ingredient3 in burger.ingredients

 
    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)
        
        burger.ingredients = [ingredient1, ingredient2, ingredient3]
        
        burger.move_ingredient(2, 0)
        
        assert burger.ingredients == [ingredient3, ingredient1, ingredient2]


    def test_get_price_with_bun_no_ingredients(self):
        """Тест получения цены  с булочкой"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        
        price = burger.get_price()
        
        assert price == 200  # 2 булочки по 100

   
    def test_get_receipt(self):
        """Тест получения чека"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 150

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 400" in receipt
