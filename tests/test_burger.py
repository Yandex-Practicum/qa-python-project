import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_move_ingredient(self, burger):
        # Создаем два разных ингредиента
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_name.return_value = "ingredient1"
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "ingredient2"
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        # Перемещаем первый ингредиент на место второго
        burger.move_ingredient(0, 1)
        
        # Проверяем, что порядок изменился
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1
    
    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        # Цена: 2 булочки (100 * 2) + ингредиент (50) = 250
        assert burger.get_price() == 250
    
    def test_get_price_without_bun(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        
        # Без булочки цена должна быть 0 + ингредиент (50)
        # Но в текущей реализации будет ошибка при вызове bun.get_price()
        # Это нужно протестировать
        with pytest.raises(AttributeError):
            burger.get_price()
    
    def test_get_price_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200  # 100 * 2
    
    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        # Проверяем, что в чеке есть нужная информация
        assert "test bun" in receipt
        assert "test ingredient" in receipt
        assert "250" in receipt  # Общая цена
        assert "=== test bun ===" in receipt
        assert "Price: 250" in receipt
    
    @pytest.mark.parametrize("ingredient_type, expected_type_str", [
        (INGREDIENT_TYPE_SAUCE, "sauce"),
        (INGREDIENT_TYPE_FILLING, "filling"),
        ("CUSTOM", "custom")  # Для нестандартных типов
    ])
    def test_get_receipt_with_different_ingredient_types(self, burger, mock_bun, ingredient_type, expected_type_str):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "test"
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_type.return_value = ingredient_type
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        # Проверяем, что тип ингредиента в нижнем регистре есть в чеке
        assert expected_type_str in receipt.lower()
    
    def test_add_multiple_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        
        # Создаем несколько разных ингредиентов
        for i in range(5):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = i * 10
            burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 5
    
    def test_remove_ingredient_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)  # Пустой список
    
    def test_move_ingredient_invalid_index(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)  # Индекс 1 не существует

        def test_get_price_empty_burger(self, burger):

            with pytest.raises(AttributeError):
                burger.get_price()
    
        def test_get_receipt_empty_burger(self, burger):
            with pytest.raises(AttributeError):
                burger.get_receipt()
    
        def test_move_ingredient_same_index(self, burger, mock_ingredient):
            burger.add_ingredient(mock_ingredient)
            burger.move_ingredient(0, 0)  # Должно работать без ошибок
            assert len(burger.ingredients) == 1