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

    @pytest.mark.parametrize("index_to_remove, expected_remaining_indices", [
        (0, [1, 2]),   # удалили первый — остались исходные 1 и 2
        (1, [0, 2]),   # удалили средний — остались исходные 0 и 2
        (2, [0, 1]),   # удалили последний — остались исходные 0 и 1
    ])
    def test_remove_ingredient_by_index(self, index_to_remove, expected_remaining_indices):
        # Создаём три мок-ингредиента
        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()
        originals = [ing1, ing2, ing3]
        
        burger = Burger()
        for ing in originals:
            burger.add_ingredient(ing)
        
        # Удаляем ингредиент по индексу
        burger.remove_ingredient(index_to_remove)
        
        # Собираем ожидаемый список — объекты по исходным индексам
        expected = [originals[i] for i in expected_remaining_indices]
        
        # Проверяем, что остались именно эти объекты и в нужном порядке
        assert burger.ingredients == expected