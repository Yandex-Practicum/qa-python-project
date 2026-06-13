import pytest
from data import EXPECTED_BUNS, EXPECTED_INGREDIENTS

class TestDatabase:

    def test_available_buns_returns_list(self, database):
        """Метод available_buns возвращает список"""
        result = database.available_buns()
        assert isinstance(result, list)

    def test_available_buns_not_empty(self, database):
        """Список булочек не пустой"""
        result = database.available_buns()
        assert len(result) > 0

    def test_available_buns_count(self, database):
        """Количество булочек"""
        result = database.available_buns()
        assert len(result) == 3

    def test_available_ingredients_returns_list(self, database):
        """Метод available_ingredients возвращает список"""
        result = database.available_ingredients()
        assert isinstance(result, list)

    def test_available_ingredients_not_empty(self, database):
        """Список ингредиентов не пустой"""
        result = database.available_ingredients()
        assert len(result) > 0

    def test_available_ingredients_count(self, database):
        """Количество ингредиентов"""
        result = database.available_ingredients()
        assert len(result) == 6

    @pytest.mark.parametrize("expected_bun", EXPECTED_BUNS)
    def test_available_buns_contains_expected(self, database, expected_bun):
        """Проверяет, что каждая ожидаемая булочка присутствует"""
        buns = database.available_buns()
        assert any(
            bun.get_name() == expected_bun.get_name() and
            bun.get_price() == expected_bun.get_price()
            for bun in buns
        )

    @pytest.mark.parametrize("expected_ingredient", EXPECTED_INGREDIENTS)
    def test_available_ingredients_contains_expected(self, database, expected_ingredient):
        """Проверяет, что каждый ожидаемый ингредиент присутствует"""
        ingredients = database.available_ingredients()
        assert any(
            ingredient.get_type() == expected_ingredient.get_type() and
            ingredient.get_name() == expected_ingredient.get_name() and
            ingredient.get_price() == expected_ingredient.get_price()
            for ingredient in ingredients
        )