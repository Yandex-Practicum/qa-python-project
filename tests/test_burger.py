import pytest
from unittest.mock import Mock

# Правильные импорты, так как код теперь лежит в папке praktikum
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    
    @pytest.fixture
    def burger(self):
        """Фикстура для создания экземпляра бургера перед каждым тестом"""
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        """Мок для булочки"""
        mock = Mock(spec=Bun)
        mock.get_name.return_value = "Булочка с кунжутом"
        mock.get_price.return_value = 100.0
        return mock

    @pytest.fixture
    def mock_ingredient(self):
        """Мок для ингредиента"""
        mock = Mock(spec=Ingredient)
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock.get_name.return_value = "Соус барбекю"
        mock.get_price.return_value = 50.0
        return mock

    # --- Тесты для set_buns ---
    
    def test_set_buns_sets_bun_correctly(self, burger, mock_bun):
        """Проверяем, что булочка устанавливается"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    # --- Тесты для add_ingredient ---

    def test_add_ingredient_adds_to_list(self, burger, mock_ingredient):
        """Проверяем, что ингредиент добавляется в список"""
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient


    # --- Тесты для remove_ingredient ---

    @pytest.mark.parametrize("index_to_remove", [0, 1, 2])
    def test_remove_ingredient_removes_correct_item(self, burger, index_to_remove):
        """Параметризация: удаляем ингредиенты с разными индексами"""
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        ingredient_to_remove = ingredients[index_to_remove]
        burger.remove_ingredient(index_to_remove)
        
        assert len(burger.ingredients) == 2
        assert ingredient_to_remove not in burger.ingredients

    def test_remove_ingredient_out_of_range_raises_error(self, burger, mock_ingredient):
        """Проверка граничного случая: удаление несуществующего индекса"""
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)


    # --- Тесты для move_ingredient ---

    @pytest.mark.parametrize("start_index, new_index", [
        (0, 2), # Перемещаем первый в конец
        (2, 0), # Перемещаем последний в начало
        (1, 1)  # Перемещаем на то же место
    ])
    def test_move_ingredient_moves_item(self, burger, start_index, new_index):
        """Параметризация: перемещаем ингредиенты в разные позиции"""
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        ingredient_to_move = burger.ingredients[start_index]
        burger.move_ingredient(start_index, new_index)
        
        assert burger.ingredients[new_index] == ingredient_to_move


    # --- Тесты для get_price ---

    def test_get_price_calculates_correctly(self, burger, mock_bun, mock_ingredient):
        """Проверяем расчет цены: булочка умножается на 2 + ингредиенты"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        # Булочка 100 * 2 = 200. Два ингредиента по 50 = 100. Итого 300.
        assert burger.get_price() == 300.0


    # --- Тесты для get_receipt ---

    def test_get_receipt_returns_correct_string(self, burger, mock_bun, mock_ingredient):
        """Проверяем формирование чека"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        expected_receipt = (
            "(==== Булочка с кунжутом ====)\n"
            "= sauce Соус барбекю =\n"
            "(==== Булочка с кунжутом ====)\n"
            "\n"
            "Price: 250.0"
        )
        
        assert burger.get_receipt() == expected_receipt