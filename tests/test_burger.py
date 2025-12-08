import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    @pytest.fixture
    def mock_ingredients(self):
        """Фикстура для создания нескольких моков ингредиентов"""
        sauce = Mock()
        sauce.get_type.return_value = 'SAUCE'
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 50.0
        
        filling = Mock()
        filling.get_type.return_value = 'FILLING'
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 80.0
        
        return sauce, filling

    def test_burger_initialization(self, burger):
        """Проверяем, что бургер инициализируется пустым"""
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self, burger, mock_bun):
        """Проверяем установку булочки"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_sauce_adds_to_list(self, burger, mock_ingredient_sauce):
        """Проверяем добавление соуса"""
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_add_ingredient_filling_adds_to_list(self, burger, mock_ingredient_filling):
        """Проверяем добавление начинки"""
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    @pytest.mark.parametrize("ingredient_count", [1, 2, 3, 5])
    def test_add_multiple_ingredients(self, burger, mock_ingredient_sauce, mock_ingredient_filling, ingredient_count):
        """Проверяем добавление нескольких ингредиентов"""
        for i in range(ingredient_count):
            if i % 2 == 0:
                burger.add_ingredient(mock_ingredient_sauce)
            else:
                burger.add_ingredient(mock_ingredient_filling)
        
        assert len(burger.ingredients) == ingredient_count

    def test_remove_ingredient_removes_from_list(self, burger, mock_ingredients):
        """Проверяем удаление ингредиента"""
        sauce, filling = mock_ingredients
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == filling

    def test_move_ingredient_changes_order(self, burger, mock_ingredients):
        """Проверяем перемещение ингредиента"""
        sauce, filling = mock_ingredients
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == filling
        assert burger.ingredients[1] == sauce

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (100.0, [50.0, 80.0], 330.0),  # 2*100 + 50 + 80
        (0.0, [10.0, 20.0], 30.0),     # 2*0 + 10 + 20
        (50.0, [], 100.0),             # Только булочки
        (75.5, [25.5, 30.0], 206.5),   # 2*75.5 + 25.5 + 30
    ])
    def test_get_price_calculates_correct_total(self, burger, bun_price, ingredient_prices, expected_total):
        """Проверяем расчет общей цены"""
        # Создаем мок булочки
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        
        burger.set_buns(mock_bun)
        
        # Добавляем моки ингредиентов
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_total

    def test_get_receipt_contains_correct_info(self, burger, mock_bun, mock_ingredients):
        """Проверяем формирование чека"""
        sauce, filling = mock_ingredients
        
        # Настраиваем моки
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        receipt = burger.get_receipt()
        
        # Проверяем обязательные элементы
        assert "(==== black bun ====)" in receipt
        assert "Price:" in receipt
        # Проверяем, что чек содержит общую цену (2*100 + 50 + 80 = 330)
        assert "330" in receipt

    def test_remove_ingredient_raises_index_error_for_invalid_index(self, burger, mock_ingredient_sauce):
        """Проверяем исключение при удалении с невалидным индексом"""
        burger.add_ingredient(mock_ingredient_sauce)
        
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)
            