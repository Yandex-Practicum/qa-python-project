import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_set_buns(self):
        """Тест установки булочки в бургер"""
        # Arrange
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.name = "white bun"
        mock_bun.price = 200
        
        # Act
        burger.set_buns(mock_bun)
        
        # Assert
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self):
        """Тест добавления ингредиента в бургер"""
        # Arrange
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100
        
        # Act
        burger.add_ingredient(mock_ingredient)
        
        # Assert
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self):
        """Тест удаления ингредиента из бургера"""
        # Arrange
        burger = Burger()
        
        # Создаем моки ингредиентов
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        
        # Добавляем ингредиенты
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        # Act
        burger.remove_ingredient(0)  # Удаляем первый ингредиент
        
        # Assert
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling
    
    def test_move_ingredient(self):
        """Тест перемещения ингредиента в бургере"""
        # Arrange
        burger = Burger()
        
        # Создаем моки ингредиентов
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        
        mock_another_sauce = Mock(spec=Ingredient)
        mock_another_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_another_sauce.get_name.return_value = "sour cream"
        
        # Добавляем ингредиенты
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_another_sauce)
        
        # Act
        burger.move_ingredient(0, 2)  # Перемещаем первый ингредиент в конец
        
        # Assert
        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_another_sauce
        assert burger.ingredients[2] == mock_sauce
    
    def test_get_price_calculation(self):
        """Тест расчета цены бургера"""
        # Arrange
        burger = Burger()
        
        # Моки для булочки и ингредиентов
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_price.return_value = 100
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_price.return_value = 150
        
        # Устанавливаем компоненты
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        # Act
        price = burger.get_price()
        
        # Assert
        expected_price = 200 * 2 + 100 + 150  # Булочка * 2 + соус + начинка
        assert price == expected_price
    
    def test_get_receipt_formatting(self):
        """Тест форматирования чека"""
        # Arrange
        burger = Burger()
        
        # Моки для булочки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        
        # Моки для ингредиентов
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        
        # Устанавливаем компоненты
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        # Настраиваем возвращаемые значения для get_price
        mock_bun.get_price.return_value = 200
        mock_sauce.get_price.return_value = 100
        mock_filling.get_price.return_value = 150
        
        # Act
        receipt = burger.get_receipt()
        
        # Assert - проверяем весь чек целиком
        expected_receipt = (
            "(==== white bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== white bun ====)\n"
            "\n"
            "Price: 650"
        )
        
        assert receipt == expected_receipt
    
    def test_burger_with_only_bun_price(self):
        """Тест цены бургера только с булочкой"""
        # Arrange
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200
        
        burger.set_buns(mock_bun)
        
        # Act
        price = burger.get_price()
        
        # Assert
        assert price == 400  # 200 * 2
    
    def test_remove_nonexistent_ingredient(self):
        """Тест попытки удаления несуществующего ингредиента"""
        # Arrange
        burger = Burger()
        
        # Act & Assert
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
    
    def test_move_nonexistent_ingredient(self):
        """Тест попытки перемещения несуществующего ингредиента"""
        # Arrange
        burger = Burger()
        
        # Act & Assert
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)
    
    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        # Arrange
        burger = Burger()
        
        # Создаем 5 моков ингредиентов
        mock_ingredients = []
        for i in range(5):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE if i % 2 == 0 else INGREDIENT_TYPE_FILLING
            mock_ingredient.get_name.return_value = f"ingredient_{i}"
            mock_ingredients.append(mock_ingredient)
        
        # Act
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        # Assert
        assert len(burger.ingredients) == 5
        for i, mock_ingredient in enumerate(mock_ingredients):
            assert burger.ingredients[i] == mock_ingredient
    
    @patch('praktikum.burger.Burger.get_price')
    def test_receipt_uses_get_price(self, mock_get_price):
        """Тест, что get_receipt использует метод get_price для расчета стоимости"""
        # Arrange
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        
        burger.set_buns(mock_bun)
        mock_get_price.return_value = 500
        
        # Act
        receipt = burger.get_receipt()
        
        # Assert
        mock_get_price.assert_called_once()
        assert "500" in receipt