import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger."""

    def test_set_buns_saves_bun(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Краторная булка"

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun

    def test_add_ingredient_adds_to_list(self):
        # Создаём мок-ингредиент
        mock_ingredient = Mock()
        
        # Создаём бургер и добавляем ингредиент
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        
        # Проверяем, что ингредиент попал в список
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize("count", [1, 2, 3, 5])
    def test_add_ingredient_adds_multiple(self, count):
        # Создаём бургер
        burger = Burger()
        
        # Добавляем count мок-ингредиентов
        for _ in range(count):
            mock_ingredient = Mock()
            burger.add_ingredient(mock_ingredient)
        
        # Проверяем, что длина списка равна count
        assert len(burger.ingredients) == count