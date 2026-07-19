import pytest
from database import Database
from testdata.data_database import EXPECTED_BUNS, EXPECTED_INGREDIENTS


class TestDatabaseBuns:
    """Тесты метода available_buns."""

    @pytest.mark.unit
    def test_available_buns_returns_list(self):
        """
        Given: экземпляр Database
        When: вызываем available_buns
        Then: возвращается список
        """
        db = Database()

        result = db.available_buns()

        assert isinstance(result, list)

    @pytest.mark.unit
    def test_available_buns_returns_three_buns(self):
        """
        Given: экземпляр Database
        When: вызываем available_buns
        Then: возвращается 3 булочки
        """
        db = Database()

        result = db.available_buns()

        assert len(result) == 3

    @pytest.mark.unit
    def test_available_buns_returns_expected_data(self):
        """
        Given: экземпляр Database
        When: вызываем available_buns
        Then: булочки соответствуют ожидаемым данным
        """
        db = Database()

        result = db.available_buns()

        for bun, (name, price) in zip(result, EXPECTED_BUNS):
            assert bun.get_name() == name
            assert bun.get_price() == price


class TestDatabaseIngredients:
    """Тесты метода available_ingredients."""

    @pytest.mark.unit
    def test_available_ingredients_returns_list(self):
        """
        Given: экземпляр Database
        When: вызываем available_ingredients
        Then: возвращается список
        """
        db = Database()

        result = db.available_ingredients()

        assert isinstance(result, list)

    @pytest.mark.unit
    def test_available_ingredients_returns_six_ingredients(self):
        """
        Given: экземпляр Database
        When: вызываем available_ingredients
        Then: возвращается 6 ингредиентов
        """
        db = Database()

        result = db.available_ingredients()

        assert len(result) == 6

    @pytest.mark.unit
    def test_available_ingredients_returns_expected_data(self):
        """
        Given: экземпляр Database
        When: вызываем available_ingredients
        Then: ингредиенты соответствуют ожидаемым данным
        """
        db = Database()

        result = db.available_ingredients()

        for ingredient, (type_, name, price) in zip(result, EXPECTED_INGREDIENTS):
            assert ingredient.get_type() == type_
            assert ingredient.get_name() == name
            assert ingredient.get_price() == price


class TestDatabaseState:
    """Тесты состояния базы данных."""

    @pytest.mark.unit
    def test_database_two_instances_have_separate_data(self):
        """
        Given: два экземпляра Database
        When: проверяем их данные
        Then: данные независимы (разные объекты)
        """
        db1 = Database()
        db2 = Database()

        buns1 = db1.available_buns()
        buns2 = db2.available_buns()

        assert buns1 is not buns2

    @pytest.mark.unit
    def test_available_buns_returns_bun_instances(self):
        """
        Given: экземпляр Database
        When: получаем булочки
        Then: каждая булочка — экземпляр класса Bun
        """
        from bun import Bun
        db = Database()

        for bun in db.available_buns():
            assert isinstance(bun, Bun)

    @pytest.mark.unit
    def test_available_ingredients_returns_ingredient_instances(self):
        """
        Given: экземпляр Database
        When: получаем ингредиенты
        Then: каждый ингредиент — экземпляр класса Ingredient
        """
        from ingredient import Ingredient
        db = Database()

        for ingredient in db.available_ingredients():
            assert isinstance(ingredient, Ingredient)
