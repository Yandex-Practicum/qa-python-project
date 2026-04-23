import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock, patch


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns_success(self, burger, mock_bun):
        """Тест: установка булочки"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == "Флюоресцентная булка R2-D3"
        assert burger.bun.get_price() == 100

    def test_add_ingredient_success(self, burger, mock_sauce):
        """Тест: добавление ингредиента"""
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce
        assert burger.ingredients[0].get_name() == "Горячий соус"

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient_success(self, burger, mock_ingredients, index):
        """Тест: удаление ингредиента по индексу (параметризация)"""
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        initial_length = len(burger.ingredients)
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == initial_length - 1

    @pytest.mark.parametrize("old_index, new_index", [
        (0, 2),
        (2, 0),
        (1, 3),
        (3, 1)
    ])
    def test_move_ingredient_success(self, burger, mock_ingredients, old_index, new_index):
        """Тест: перемещение ингредиента (параметризация)"""
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        moved_ingredient = burger.ingredients[old_index]
        burger.move_ingredient(old_index, new_index)
        assert burger.ingredients[new_index] == moved_ingredient

    def test_get_price_without_bun(self, burger, mock_ingredients):
        """Тест: получение цены без булочки (должна быть ошибка)"""
        for ing in mock_ingredients[:2]:
            burger.add_ingredient(ing)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_price_success(self, burger, mock_bun, mock_ingredients):
        """Тест: расчёт цены с булочкой и ингредиентами"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])  # Сырный соус, 50
        burger.add_ingredient(mock_ingredients[1])  # Мясо бессмертных, 150
        
        expected_price = mock_bun.get_price() * 2 + 50 + 150
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [50, 30], 100*2 + 80),
        (200, [100, 150, 200], 200*2 + 450),
        (150, [], 150*2 + 0),
    ])
    def test_get_price_parametrized(self, bun_price, ing_prices, expected):
        """Тест: параметризованная проверка цены"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ing_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
        
        assert burger.get_price() == expected

    def test_get_receipt_success(self, burger, mock_bun, mock_ingredients):
        """Тест: получение чека"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])  # Сырный соус
        burger.add_ingredient(mock_ingredients[1])  # Мясо бессмертных
        
        receipt = burger.get_receipt()
        
        assert "(==== Флюоресцентная булка R2-D3 ====)" in receipt
        assert "= sauce Сырный соус =" in receipt
        assert "= filling Мясо бессмертных =" in receipt
        assert "Price: 400" in receipt  # 100*2 + 50 + 150 = 400

    def test_get_receipt_empty_burger(self, burger, mock_bun):
        """Тест: чек пустого бургера (только булочка)"""
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert receipt.count("(==== Флюоресцентная булка R2-D3 ====)") == 2
        assert "Price: 200" in receipt

from unittest.mock import Mock, patch

from unittest.mock import Mock, patch

@patch('praktikum.bun.Bun.get_price')
@patch('praktikum.ingredient.Ingredient.get_price')
def test_get_price_with_mocks(mock_ingredient_price, mock_bun_price):
    """Тест: использование моков для расчёта цены"""
    
    burger = Burger()
    
    mock_bun_price.return_value = 100
    mock_ingredient_price.return_value = 50
    
    mock_bun = Mock(spec=Bun)
    mock_bun.get_price = mock_bun_price
    
    mock_ing = Mock(spec=Ingredient)
    mock_ing.get_price = mock_ingredient_price
    
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ing)
    
    assert burger.get_price() == 250
    
    mock_bun_price.assert_called_once()
    mock_ingredient_price.assert_called_once()